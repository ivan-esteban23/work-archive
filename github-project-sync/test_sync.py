import hashlib
import json
import subprocess
import tempfile
import unittest
from unittest import mock
from pathlib import Path
from sync import synchronize, destination, check_content, push
from lfs_upload import ensure_uploaded


class SyncChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.work = self.root / 'work'
        self.vault = self.root / 'vault'
        self.repo = self.root / 'archive'
        for p in [self.work, self.vault, self.repo / '_github-upload']:
            p.mkdir(parents=True)
        self.config = {'work_root': str(self.work), 'vault_root': str(self.vault),
            'archive': str(self.repo), 'lfs_binary': '/home/ivanaguilera/Work/github-upload-preparation-20261014/tools/git-lfs-3.8.0/git-lfs'}
        (self.repo / '_github-upload/manifest.json').write_text('[]\n')
        (self.repo / '_github-upload/excluded.json').write_text(json.dumps({'files': {'config.json': 'credentials'}, 'directory_patterns': []}))
        (self.repo / '.gitattributes').write_text('')
        for command in [['init', '-b', 'main'], ['config', 'user.name', 'Sync test'], ['config', 'user.email', 'sync-test@example.invalid'], ['add', '.'], ['commit', '-m', 'Baseline']]:
            subprocess.run(['git', '-C', str(self.repo), *command], check=True, capture_output=True)

    def tearDown(self):
        self.tmp.cleanup()

    def sync(self, paths, **kwargs):
        return synchronize(paths, 'Project update', config=self.config, do_push=False, **kwargs)

    def test_vault_note_and_idempotent_replay(self):
        note = self.vault / 'Japan — Café.md'
        note.write_text('[[Japan Travel Guide 2027]]\nA café to research.\n')
        result = self.sync([note])
        self.assertEqual(result['changed_files'], ['Obsidian Vault/Japan — Café.md'])
        self.assertEqual((self.repo / 'Obsidian Vault/Japan — Café.md').read_bytes(), note.read_bytes())
        head = subprocess.check_output(['git', '-C', str(self.repo), 'rev-parse', 'HEAD'])
        self.assertEqual(self.sync([note])['changed_files'], [])
        self.assertEqual(head, subprocess.check_output(['git', '-C', str(self.repo), 'rev-parse', 'HEAD']))

    def test_secret_aborts_entire_scope_before_commit(self):
        project = self.work / 'project'
        project.mkdir()
        (project / 'good.md').write_text('Normal research')
        (project / 'bad.md').write_text('ghp_' + 'x' * 36)
        with self.assertRaises(ValueError):
            self.sync([project])
        self.assertFalse((self.repo / 'project/good.md').exists())

    def test_excluded_credentials_and_browser_symlinks(self):
        (self.work / 'config.json').write_text('ghp_' + 'x' * 36)
        self.assertEqual(self.sync([self.work / 'config.json'])['changed_files'], [])
        project = self.work / 'project'
        (project / 'qa-profile-123').mkdir(parents=True)
        (project / 'qa-profile-123/SingletonLock').symlink_to('/outside')
        (project / '.env').write_text('PRIVATE_PASSWORD=really-secret-value')
        (project / 'note.md').write_text('Keep this')
        self.assertEqual(self.sync([project])['changed_files'], ['project/note.md'])

    def test_external_source_and_symlink_rejected(self):
        with self.assertRaises(ValueError):
            destination(self.root / 'outside.md', self.config)
        link = self.work / 'link.md'
        link.symlink_to(self.root / 'outside.md')
        with self.assertRaises(ValueError):
            destination(link, self.config)

    def test_json_credential_rejected(self):
        with self.assertRaises(ValueError):
            check_content('settings.json', b'{"api_key":"nonstandard-but-secret-value"}')

    def test_website_without_lfs_does_not_request_credentials(self):
        with mock.patch('lfs_upload.subprocess.check_output', return_value=b'{"files":null}') as command:
            self.assertEqual(ensure_uploaded(self.repo, 'account/site', '/unused/gh', {}), 0)
            self.assertEqual(command.call_count, 1)

    def test_unexpected_public_visibility_aborts_before_asset_upload(self):
        with mock.patch('sync.run_git', return_value='https://github.com/account/site.git'), mock.patch('sync.subprocess.check_output', return_value=b'{"visibility":"PUBLIC"}'), mock.patch('sync.ensure_uploaded') as upload:
            with self.assertRaises(ValueError):
                push(self.repo, 'account/site', '/unused/gh', {}, 'PRIVATE')
            upload.assert_not_called()

    def test_explicit_public_policy_verifies_the_remote_commit(self):
        with mock.patch('sync.run_git', side_effect=['https://github.com/account/site.git', '', 'abc']), mock.patch('sync.subprocess.check_output', side_effect=[b'{"visibility":"PUBLIC"}', b'{"object":{"sha":"abc"}}']), mock.patch('sync.ensure_uploaded'):
            self.assertEqual(push(self.repo, 'account/site', '/unused/gh', {}, 'PUBLIC'), 'abc')

    def test_explicit_deletion_preserves_history(self):
        note = self.work / 'old.md'
        note.write_text('Previous note')
        self.sync([note])
        note.unlink()
        self.assertEqual(self.sync([], deletions=[note])['deleted_files'], ['old.md'])
        self.assertFalse((self.repo / 'old.md').exists())
        old = subprocess.check_output(['git', '-C', str(self.repo), 'show', 'HEAD~1:old.md'])
        self.assertEqual(old, b'Previous note')


if __name__ == '__main__':
    unittest.main()
