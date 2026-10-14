#!/usr/bin/env python3
"""Explicitly scoped, incremental project backups to existing private GitHub repos."""
import argparse
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import fcntl
from lfs_upload import ensure_uploaded

HERE = Path(__file__).resolve().parent
TEXT = {'.md', '.txt', '.json', '.toml', '.yaml', '.yml', '.py', '.sh', '.js', '.mjs', '.css', '.html', '.csv', '.xml'}
MEDIA = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.pdf', '.zip', '.ttf', '.woff', '.woff2', '.mp4'}
SECRET = re.compile(rb'(?<![A-Za-z0-9+/])(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-proj-[A-Za-z0-9_-]{30,}|tvly-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)')
ASSIGNMENT = re.compile(rb'(?im)^\s*(?:export\s+)?[A-Z_]*(?:API_KEY|ACCESS_TOKEN|CLIENT_SECRET|PASSWORD)[A-Z_]*\s*=\s*[\x27\"]?([A-Za-z0-9_-]{16,})')
DIR_BLOCK = {'.git', '.aws', '.codex', '.agents', '.obsidian', '.venv', 'venv', 'node_modules', '__pycache__', 'uv-cache'}


def gh_binary():
    versions = Path.home() / '.local/share/mise/installs/gh'
    found = list(versions.glob('*/gh_*_linux_amd64/bin/gh'))
    return max(found, key=lambda p: p.stat().st_mtime) if found else Path(shutil.which('gh') or '/usr/bin/gh')


def destination(path, config, check_symlinks=True):
    """Reject symlinks and paths outside the two authorized source roots."""
    path = Path(os.path.abspath(path))
    for key, prefix in [('work_root', ''), ('vault_root', 'Obsidian Vault/')]:
        root = Path(config[key])
        if path.is_relative_to(root) and path != root:
            relative = path.relative_to(root)
            if not prefix and relative.parts[0] in {'Obsidian Vault', '_github-upload'}:
                raise ValueError('Work path conflicts with reserved archive metadata')
            if not check_symlinks:
                return prefix + relative.as_posix()
            cursor = path
            while cursor != root:
                if cursor.is_symlink():
                    raise ValueError('Symlink source is excluded: ' + str(path))
                cursor = cursor.parent
            if not path.resolve().is_relative_to(root.resolve()):
                raise ValueError('Source escapes its root')
            return prefix + relative.as_posix()
    raise ValueError('Use explicit files or project folders inside Work or the Obsidian vault')


def blocked(relative, exclusions):
    parts = Path(relative).parts
    if any(x in DIR_BLOCK or x.startswith('qa-profile-') for x in parts):
        return True
    if any(x.startswith('github-upload-preparation-') for x in parts):
        return True
    if relative.startswith('github-project-sync/backups/') or relative.startswith('github-project-sync/.'):
        return True
    if any(fnmatch.fnmatch(x, pattern) for x in parts for pattern in exclusions['directory_patterns']):
        return True
    if relative in exclusions['files']:
        return True
    name = parts[-1]
    return name.startswith('.env') or name in {'credentials', 'hosts.yml', 'id_rsa', 'id_ed25519', 'Cookies', 'Login Data'} or name.endswith(('.pem', '.key', '.log'))


def check_content(path, data):
    if Path(path).suffix.lower() in TEXT or '.bak' in Path(path).name:
        if SECRET.search(data) or ASSIGNMENT.search(data):
            raise ValueError('Potential credential in ' + str(path) + '; no commit created')
    if Path(path).suffix.lower() == '.json':
        def inspect(value):
            if isinstance(value, dict):
                for key, item in value.items():
                    normalized = key.lower().replace('-', '_')
                    if normalized in {'api_key', 'apikey', 'access_token', 'client_secret', 'password', 'authorization'} and isinstance(item, str) and len(item) >= 16 and not item.startswith(('$', '{env:', 'YOUR_')):
                        raise ValueError('Credential assignment in ' + str(path) + '; no commit created')
                    inspect(item)
            elif isinstance(value, list):
                for item in value:
                    inspect(item)
        try:
            inspect(json.loads(data))
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass
    if Path(path).suffix.lower() == '.zip':
        import io
        import zipfile
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            for member in archive.infolist():
                if Path(member.filename).name.startswith('.env') or Path(member.filename).name in {'id_rsa', 'id_ed25519', 'credentials', 'hosts.yml'}:
                    raise ValueError('Credential file inside ZIP: ' + str(path))
                if Path(member.filename).suffix.lower() in TEXT and not member.is_dir():
                    content = archive.read(member)
                    check_content(member.filename, content)


def run_git(repo, *args, env=None):
    return subprocess.check_output(['git', '-C', str(repo), *args], env=env, stderr=subprocess.STDOUT).decode().strip()


def push(repo, slug, gh, env):
    expected = f'https://github.com/{slug}.git'
    if run_git(repo, 'remote', 'get-url', 'origin') != expected:
        raise ValueError('Unexpected origin; refusing automatic upload')
    info = json.loads(subprocess.check_output([str(gh), 'repo', 'view', slug, '--json', 'visibility']))
    if info['visibility'] != 'PRIVATE':
        raise ValueError('Automatic sync requires the configured private repository')
    ensure_uploaded(repo, slug, gh, env)
    run_git(repo, '-c', 'credential.helper=', '-c', 'credential.helper=!' + shlex.quote(str(gh)) + ' auth git-credential',
            'push', 'origin', 'HEAD:refs/heads/main', env=env)
    sha = run_git(repo, 'rev-parse', 'HEAD')
    remote = json.loads(subprocess.check_output([str(gh), 'api', f'repos/{slug}/git/ref/heads/main']))
    if remote['object']['sha'] != sha:
        raise RuntimeError('Remote commit verification failed')
    return sha


def synchronize(paths, message, dry_run=False, config=None, do_push=True, deletions=None):
    config = config or json.loads((HERE / 'config.json').read_text())
    repo = Path(config['archive'])
    exclusions = json.loads((repo / '_github-upload/excluded.json').read_text())
    manifest_path = repo / '_github-upload/manifest.json'
    manifest = {x['path']: x for x in json.loads(manifest_path.read_text())}
    chosen = {}
    removed = []
    skipped = []
    for raw in paths:
        source = Path(os.path.abspath(raw))
        relative = destination(source, config)
        if blocked(relative, exclusions):
            skipped.append(str(source))
            continue
        if source.is_dir():
            candidates = []
            for base, dirs, names in os.walk(source):
                dirs[:] = [name for name in dirs if not (Path(base) / name).is_symlink() and not blocked(
                    destination(Path(base) / name, config, check_symlinks=False), exclusions)]
                candidates.extend(Path(base) / name for name in names)
        else:
            candidates = [source]
        for candidate in candidates:
            # Ignore excluded names before inspecting browser-profile symlinks.
            preliminary = destination(candidate, config, check_symlinks=False)
            if blocked(preliminary, exclusions):
                continue
            if candidate.is_symlink():
                skipped.append(str(candidate))
                continue
            rel = destination(candidate, config)
            if not candidate.is_file():
                raise ValueError('Missing source; use --delete for an intentionally deleted file: ' + str(candidate))
            before = candidate.stat()
            data = candidate.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            if candidate.stat().st_mtime_ns != before.st_mtime_ns:
                raise RuntimeError('Source changed while reading: ' + str(candidate))
            if manifest.get(rel, {}).get('sha256') == digest:
                continue
            check_content(candidate, data)
            chosen[rel] = (candidate, digest, len(data))
    for raw in deletions or []:
        source = Path(os.path.abspath(raw))
        rel = destination(source, config)
        if source.exists() or blocked(rel, exclusions) or rel not in manifest:
            raise ValueError('Deletion requires an absent, previously archived, authorized source: ' + str(source))
        if not (repo / rel).is_file():
            raise ValueError('Archived deletion target is missing: ' + rel)
        removed.append(rel)
    plan = {'changed_files': sorted(chosen), 'deleted_files': sorted(removed), 'excluded_paths': skipped}
    if dry_run:
        return plan
    if run_git(repo, 'status', '--porcelain'):
        raise ValueError('Archive checkout has pending changes; preserve/reconcile them before syncing')
    env = dict(os.environ)
    env['PATH'] = str(Path(config['lfs_binary']).parent) + os.pathsep + env['PATH']
    env['GODEBUG'] = env.get('GODEBUG', '') + ',http2client=0'
    attrs = repo / '.gitattributes'
    attribute_text = attrs.read_text()
    for rel, (source, digest, size) in chosen.items():
        target = repo / rel
        if not target.resolve().is_relative_to(repo.resolve()):
            raise ValueError('Archive target escapes its checkout: ' + rel)
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(target.name + '.sync-tmp')
        shutil.copyfile(source, temporary)
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != digest:
            temporary.unlink()
            raise RuntimeError('Source changed before copying: ' + str(source))
        temporary.replace(target)
        manifest[rel] = {'path': rel, 'bytes': size, 'sha256': digest}
        # Large media use LFS; ordinary HTML stays in Git unless over Git's limit.
        if Path(rel).suffix.lower() in MEDIA or size >= 95 * 1024 * 1024:
            entry = json.dumps(rel, ensure_ascii=False) + ' filter=lfs diff=lfs merge=lfs -text\n'
            if entry not in attribute_text:
                attribute_text += entry
    for rel in removed:
        (repo / rel).unlink()
        del manifest[rel]
    if chosen or removed:
        attrs.write_text(attribute_text)
        manifest_path.write_text(json.dumps(list(manifest.values()), indent=2) + '\n')
        documentation = []
        if 'README.md' not in manifest:
            (repo / 'README.md').write_text(
                '# Project archive\n\n'
                'Private project archive, updated after completed Codex tasks. '
                'Contains selected Work project files and relevant live Obsidian notes under `Obsidian Vault/`.\n\n'
                f'The manifest currently records {len(manifest):,} source files. '
                'Media and large exports use Git LFS; install it before cloning and run `git lfs pull` to download assets.\n\n'
                '[Sync workflow](github-project-sync/README.md) · '
                '[File paths and SHA-256 hashes](_github-upload/manifest.json) · '
                '[Credential and cache exclusions](_github-upload/excluded.json)\n\n'
                'Website source and history: [The Reference Edit](https://github.com/ivan-esteban23/the-reference-edit). '
                'Notion content is saved as dated exports/readbacks; those copies update when a task explicitly refreshes them.\n')
            documentation.append('README.md')
        run_git(repo, 'add', '-f', '-A', '--', *chosen, *removed, '.gitattributes', '_github-upload/manifest.json', *documentation, env=env)
        run_git(repo, 'commit', '-m', message, env=env)
    result = dict(plan)
    if do_push:
        gh = gh_binary()
        login = subprocess.check_output([str(gh), 'api', 'user', '--jq', '.login']).decode().strip()
        if login != config['account']:
            raise ValueError('Active GitHub account differs from the configured account')
        result['archive_commit'] = push(repo, config['archive_repo'], gh, env)
        if any(Path(p).absolute().is_relative_to(Path(config['website'])) for p in list(paths) + list(deletions or [])):
            website = Path(config['website'])
            # The normal website workflow creates its commit; never sweep up unrelated edits.
            if run_git(website, 'status', '--porcelain'):
                raise ValueError('Commit the completed website changes before syncing its repository')
            result['website_commit'] = push(website, config['website_repo'], gh, env)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--path', action='append', default=[], help='Completed task file/folder; may be repeated')
    parser.add_argument('--delete', action='append', default=[], help='Original path of an intentionally deleted file')
    parser.add_argument('--message', default='Sync completed project update')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if not args.path and not args.delete:
        parser.error('Provide at least one --path or --delete')
    with (HERE / '.sync.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            result = synchronize(args.path, args.message, args.dry_run, deletions=args.delete)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as error:
            text = str(error)
            text = re.sub(r'https?://\S+', '[URL]', text)
            text = SECRET.sub(b'[REDACTED]', text.encode()).decode(errors='replace')
            print('Sync stopped: ' + text[:1200], file=sys.stderr)
            raise SystemExit(1)


if __name__ == '__main__':
    main()
