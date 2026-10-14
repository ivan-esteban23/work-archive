from pathlib import Path
import json,hashlib,shutil,re
from PIL import Image
b=Path(__file__).parent; s=b/'staged'; v=Path('/home/ivanaguilera/Documents/Obsidian Vault')
checks=json.loads((b/'before-hashes.json').read_text())
for name,h in checks.items(): assert hashlib.sha256((v/name).read_bytes()).hexdigest()==h,'Changed during preparation: '+name
imgs=list((s/'pages').glob('*.jpg')); assert len(imgs)==103
for p in imgs:
 with Image.open(p) as im: im.verify()
for p in s.rglob('*.md'):
 target=v/p.relative_to(s)
 if p.name not in checks: assert not target.exists(),'Existing target: '+str(target)
assets=v/'Attachments/The Portrait Edit - Issue 01/Final Edition Pages'
assert not assets.exists()
shutil.copytree(s/'pages',assets)
for p in s.rglob('*.md'):
 target=v/p.relative_to(s); target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,target); assert target.read_bytes()==p.read_bytes()
count=0
for p in s.rglob('*.md'):
 text=(v/p.relative_to(s)).read_text()
 for raw in re.findall(r'\[\[([^\]]+)\]\]',text):
  t=raw.split('|')[0].split('#')[0]
  if not t: continue
  assert (v/t).exists() or (v/(t+'.md')).exists(),'Missing link: '+t
 count+=1
print('Saved and read back',count,'Markdown notes; verified 103 JPEG pages and every wiki-link target.')
