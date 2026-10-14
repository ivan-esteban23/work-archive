from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
PICS=Path('/home/ivanaguilera/Pictures')
manifest=json.loads((ROOT/'manifest.json').read_text())
for name,expected in manifest.items():
 p=PICS/name
 actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
 assert actual==expected,'Changed since staging: '+name
for name in manifest:
 p=PICS/name
 p.parent.mkdir(parents=True,exist_ok=True)
 data=(ROOT/'staged'/name).read_bytes()
 p.write_bytes(data)
 assert p.read_bytes()==data,name
md=(PICS/'Editorial Portrait Prompt Library.md').read_text()
for ref in re.findall(r'\]\(<([^>]+)>\)',md):
 assert (PICS/ref).exists(),ref
assert md.count('```')%2==0
print('Saved and read back all four files; reference images and generated-image links verified.')
