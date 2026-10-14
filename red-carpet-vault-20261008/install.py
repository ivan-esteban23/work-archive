from pathlib import Path
import hashlib,json,shutil,re
root=Path('/home/ivanaguilera/Work/red-carpet-vault-20261008');vault=Path('/home/ivanaguilera/Documents/Obsidian Vault');manifest=json.loads((root/'manifest.json').read_text())
for rel,expected in manifest.items():
 p=vault/rel;actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
 if actual!=expected:raise RuntimeError('File changed: '+rel)
for rel,expected in manifest.items():
 p=vault/rel
 if expected:
  backup=root/'backup'/rel;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,backup)
 p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/'staged'/rel,p)
for rel in manifest:assert (vault/rel).read_bytes()==(root/'staged'/rel).read_bytes(),rel
body=(vault/'Editorial Portrait Prompt Library.md').read_text()
for target in re.findall(r'!\[\[([^\]|]+)',body):assert (vault/target).is_file(),target
print('Saved and verified 4 files; backed up both existing library files; all image embeds resolve.')
