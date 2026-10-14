from pathlib import Path
import subprocess
b=Path(__file__).parent;p=b/'The Portrait Edit — Issue 01 — The Fashion Issue.pdf'
r=subprocess.run(['pdfimages','-list',str(p)],capture_output=True,text=True,check=True)
counts={}
for line in r.stdout.splitlines()[2:]:
 parts=line.split()
 if parts and parts[0].isdigit() and parts[2]=='image':counts[int(parts[0])]=counts.get(int(parts[0]),0)+1
for page in range(61,103):assert counts.get(page,0)==(1 if page==102 else 2),(page,counts.get(page))
print('All 42 archive pages contain reference images; 83 reference images verified.')
