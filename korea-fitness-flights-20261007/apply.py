from pathlib import Path
import hashlib,json,re
root=Path('/home/ivanaguilera/Work/korea-fitness-flights-20261007')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((root/'original-hashes.json').read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
for n,expected in manifest.items():
 assert digest(vault/n)==expected,'Live note changed; stopping: '+n
for n,expected in manifest.items():
 assert digest(vault/n)==expected,'Live note changed; stopping: '+n
 if expected is not None: assert digest(root/'backup'/n)==expected
 (vault/n).write_bytes((root/'staged'/n).read_bytes())
 assert (vault/n).read_bytes()==(root/'staged'/n).read_bytes()
for n in manifest:
 text=(vault/n).read_text()
 for raw in re.findall(r'\[\[([^\]]+)\]\]',text):
  target=raw.split('|')[0].rstrip('\\'); base,_,anchor=target.partition('#')
  p=vault/((base or Path(n).stem)+'.md')
  assert p.exists(),(n,base)
  if anchor:
   headings=[re.sub(r'^#+\s+','',x).strip() for x in p.read_text().splitlines() if x.startswith('#')]
   assert anchor in headings,(n,target)
(root/'applied-hashes.json').write_text(json.dumps({n:digest(vault/n) for n in manifest},indent=2))
print('Saved and read back',len(manifest),'notes. Wiki-link targets and section anchors verified.')
