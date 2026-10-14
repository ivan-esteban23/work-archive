from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((ROOT/'manifest.json').read_text())
for name,expected in manifest.items():
    dest=VAULT/name
    current=hashlib.sha256(dest.read_bytes()).hexdigest() if dest.exists() else None
    if current!=expected: raise RuntimeError('Changed since staging: '+name)
for name in manifest:
    dest=VAULT/name
    staged=(ROOT/'staged'/name).read_bytes()
    dest.write_bytes(staged)
    assert dest.read_bytes()==staged,name
print('Saved and read back '+str(len(manifest))+' notes.')
