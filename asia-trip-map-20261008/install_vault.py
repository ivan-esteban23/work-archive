from pathlib import Path
import json,hashlib,re,shutil
b=Path(__file__).resolve().parent;v=Path('/home/ivanaguilera/Documents/Obsidian Vault')
m=json.loads((b/'vault-manifest.json').read_text())
stems={p.stem for p in v.rglob('*.md')}|{Path(i['relative']).stem for i in m}
for i in m:
 p=v/i['relative'];e=i['expected'];s=b/'staged'/i['relative']
 if e:assert hashlib.sha256(p.read_bytes()).hexdigest()==e,p
 else:assert not p.exists(),p
 if s.suffix=='.md':
  for name in re.findall(r'\[\[([^\]]+)\]\]',s.read_text()):assert name.split('|')[0].split('#')[0] in stems,name
  assert s.read_text().count('```')%2==0
for i in m:
 p=v/i['relative'];p.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(b/'staged'/i['relative'],p)
 assert p.read_bytes()==(b/'staged'/i['relative']).read_bytes()
print('Saved and read back combined map note, four attachments, three dashboard links and three session recap additions.')
