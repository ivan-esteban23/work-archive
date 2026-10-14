from pathlib import Path
import hashlib,json,shutil,re
root=Path('/home/ivanaguilera/Work/spotify-music-prompts-20261008');vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((root/'manifest.json').read_text())
for rel,expected in manifest.items():
 p=vault/rel;actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
 if actual!=expected:raise RuntimeError('Live note changed: '+rel)
for rel,expected in manifest.items():
 p=vault/rel
 if expected:
  backup=root/'backup'/rel;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,backup)
 p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/'staged'/rel,p)
known={p.stem for p in vault.rglob('*.md')}
for rel in manifest:
 p=vault/rel
 assert p.read_bytes()==(root/'staged'/rel).read_bytes(),rel
 body=p.read_text();assert body.count('```')%2==0,rel
 for target in re.findall(r'\[\[([^\]|#]+)',body):assert target in known,(rel,target)
print('Saved and read back 10 notes. Backed up 9 existing notes; verified wiki targets and code fences.')
