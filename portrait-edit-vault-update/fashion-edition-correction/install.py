from pathlib import Path
import json,hashlib,shutil
b=Path(__file__).parent;checks=json.loads((b/'before-hashes.json').read_text());pdf=b/'The Portrait Edit — Issue 01 — The Fashion Issue.pdf'
for name,h in checks.items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==h,'Live file changed: '+name
for name in checks:
 p=Path(name)
 if p.suffix=='.pdf':shutil.copy2(pdf,p);assert hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(pdf.read_bytes()).digest()
 else:
  s=p.read_text();s+='\n> [!info] Fashion edition layout\n> Ivory backgrounds are used throughout. The reference archive on pages 61–102 includes all 83 original reference images beside their art direction and prompts.\n';p.write_text(s);assert 'all 83 original reference images' in p.read_text()
print('Corrected PDF saved and hash verified in Downloads and vault; companion note updated.')
