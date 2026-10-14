"""GitHub's standard LFS batch/basic API; never print tokens or signed URLs."""
import base64
import concurrent.futures
import json
from pathlib import Path
import subprocess
import urllib.request
import urllib.parse


def ensure_uploaded(repo, slug, gh, env):
    files = json.loads(subprocess.check_output(
        ['git', '-C', str(repo), 'lfs', 'ls-files', '--json'], env=env))['files']
    objects = {f['oid']: f['size'] for f in files}
    if not objects:
        return 0
    token = subprocess.check_output([str(gh), 'auth', 'token', '--hostname', 'github.com']).strip()
    auth = 'Basic ' + base64.b64encode(slug.split('/')[0].encode() + b':' + token).decode()
    endpoint = f'https://github.com/{slug}.git/info/lfs/objects/batch'

    def request(url, body, headers=None):
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme != 'https':
            raise RuntimeError('LFS action must use HTTPS')
        h = {'Accept': 'application/vnd.git-lfs+json', 'Content-Type': 'application/vnd.git-lfs+json'}
        h.update(headers or {})
        if parsed.hostname == 'github.com':
            h.setdefault('Authorization', auth)
        with urllib.request.urlopen(urllib.request.Request(
                url, data=json.dumps(body).encode(), headers=h), timeout=30) as response:
            data = response.read()
            return json.loads(data) if data else {}

    gitdir = Path(subprocess.check_output(
        ['git', '-C', str(repo), 'rev-parse', '--absolute-git-dir']).decode().strip())
    missing = []
    items = list(objects.items())
    for start in range(0, len(items), 100):
        batch = request(endpoint, {'operation': 'upload', 'transfers': ['basic'],
            'objects': [{'oid': oid, 'size': size} for oid, size in items[start:start + 100]]})
        returned = batch.get('objects', [])
        if len(returned) != len(items[start:start + 100]):
            raise RuntimeError('Incomplete LFS batch response')
        for obj in returned:
            if obj.get('error'):
                raise RuntimeError(f'LFS server refused an object: {obj["error"].get("code")}')
            if obj.get('actions', {}).get('upload'):
                missing.append(obj)

    def upload(obj):
        oid = obj['oid']
        asset = gitdir / 'lfs' / 'objects' / oid[:2] / oid[2:4] / oid
        if not asset.is_file() or asset.stat().st_size != obj['size']:
            raise RuntimeError('Missing local LFS object')
        action = obj['actions']['upload']
        if urllib.parse.urlparse(action['href']).scheme != 'https':
            raise RuntimeError('LFS upload must use HTTPS')
        args = ['curl', '--http1.1', '--fail', '--silent', '--show-error',
                '--connect-timeout', '20', '--max-time', '180', '--speed-limit', '1024',
                '--speed-time', '30', '--request', 'PUT', '--header', 'Expect:',
                '--header', 'Content-Type: application/octet-stream', '--upload-file', str(asset),
                '--output', '/dev/null', '--url', action['href']]
        for key, value in action.get('header', {}).items():
            args.extend(['--header', key + ': ' + value])
        result = subprocess.run(args, capture_output=True, timeout=190)
        if result.returncode:
            raise RuntimeError(f'LFS upload failed (curl exit {result.returncode}); commit remains local')
        verify = obj.get('actions', {}).get('verify')
        if verify:
            request(verify['href'], {'oid': oid, 'size': obj['size']}, verify.get('header'))

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(upload, missing))
    return len(missing)
