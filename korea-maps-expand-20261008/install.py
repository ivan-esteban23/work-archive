from pathlib import Path
import json,hashlib,re,shutil,csv
b=Path(__file__).resolve().parent;v=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((b/'manifest.json').read_text())
stems={p.stem for p in v.rglob('*.md')}
for i in manifest:
 p=v/i['relative'];s=b/'staged'/i['relative']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==i['expected'],p
 if s.suffix=='.md':
  text=s.read_text();assert text.count('```')%2==0
  for name in re.findall(r'\[\[([^\]]+)\]\]',text):assert name.split('|')[0].split('#')[0] in stems,name
  for block in re.findall(r'```mapview\n(.*?)\n```',text,re.S):json.loads(block)
 if s.suffix=='.json':json.loads(s.read_text())
view=(b/'staged/Korea 2026 — Map View.md').read_text()
assert len(re.findall(r'\]\(geo:',view))==39
assert 'locations:' in view.split('---',2)[1]
for i in manifest:
 p=v/i['relative'];s=b/'staged'/i['relative'];shutil.copy2(s,p)
 assert p.read_bytes()==s.read_bytes()
print('Saved and read back eight updated files; 39 Korea pins, map JSON, wiki targets and preserved source files checked.')
