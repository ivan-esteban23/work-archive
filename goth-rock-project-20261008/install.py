from pathlib import Path
import hashlib,json,shutil
root=Path('/home/ivanaguilera/Work/goth-rock-project-20261008');vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((root/'manifest.json').read_text())
for rel,expected in manifest.items():
 p=vault/rel;actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
 if actual!=expected:raise RuntimeError('Live note changed: '+rel)
for rel,expected in manifest.items():
 p=vault/rel
 if expected:
  backup=root/'backup'/rel;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,backup)
 p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/'staged'/rel,p)
for rel in manifest:
 assert (vault/rel).read_bytes()==(root/'staged'/rel).read_bytes(),rel
print('Saved and read back all 8 notes; backed up the existing prompt index.')
