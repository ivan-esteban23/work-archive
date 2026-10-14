from pathlib import Path
import shutil,hashlib,json,re,csv
base=Path('/home/ivanaguilera/Work/portrait-edit-vault-update/fashion-edition');v=Path('/home/ivanaguilera/Documents/Obsidian Vault');a=v/'Attachments/The Portrait Edit - Issue 01';m=json.loads((base/'manifest.json').read_text())
old=v/'The Portrait Edit — Issue 01.md';assert hashlib.sha256(old.read_bytes()).hexdigest()==m['original_note_sha256'],'Live note changed during work'
new=v/m['new_note'];assert not new.exists()
pdfname='The Portrait Edit — Issue 01 — The Fashion Issue.pdf';downloads=Path('/home/ivanaguilera/Downloads')/pdfname
for dest in [downloads,a/pdfname,a/'Issue 01 - Fashion Edition Image Index.csv',a/'Issue 01 - Fashion Cover Preview.png']:assert not dest.exists(),dest
pairs=[(base/pdfname,downloads),(base/pdfname,a/pdfname),(base/'Issue 01 - Fashion Edition Image Index.csv',a/'Issue 01 - Fashion Edition Image Index.csv'),(base/'Issue 01 - Fashion Cover Preview.png',a/'Issue 01 - Fashion Cover Preview.png'),(base/m['new_note'],new),(base/'redirect.md',old)]
for source,dest in pairs:
 shutil.copy2(source,dest);assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(dest.read_bytes()).digest()
s=new.read_text();headers=[line.lstrip('# ').strip() for line in s.splitlines() if line.startswith('#')]
for target in re.findall(r'!?\[\[([^]|]+)',s):
 if target.startswith('#'):assert target[1:] in headers,target
 else:assert (v/target).exists(),target
rows=list(csv.DictReader((a/'Issue 01 - Fashion Edition Image Index.csv').open()));assert len(rows)==83
print('Installed, verified hashes, 83 CSV rows, and all note links.');print(downloads);print(new)
