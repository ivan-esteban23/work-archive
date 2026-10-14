from pathlib import Path
import re,shutil,csv,json
from PIL import Image
base=Path('/home/ivanaguilera/Work/portrait-edit-vault-update');out=base/'staged';out.mkdir(exist_ok=True)
a=out/'Attachments'/'The Portrait Edit - Issue 01';a.mkdir(parents=True,exist_ok=True)
orig=Path('/home/ivanaguilera/Downloads/upscaled_2x');enh=Path('/home/ivanaguilera/Downloads/Upscaled Images')
chapters=[('I','The Light',1,1),('II','The Face',2,3),('III','The Myth',4,4),('IV','The Archive',5,6),('V','The Lookbook',7,9),('VI','The Second Edit',10,14),('VII','The Third Edit',15,22),('VIII','The Fourth Edit',23,28),('IX','The Fifth Edit',29,34),('X','The Sixth Edit',35,40),('XI','The Seventh Edit',41,46),('XII','The Eighth Edit',47,52),('XIII','The Ninth Edit',53,58),('XIV','The Tenth Edit',59,65),('XV','The Eleventh Edit',66,71),('XVI','The Twelfth Edit',72,77),('XVII','The Thirteenth Edit',78,83)]
raw=Path('/tmp/portrait-raw.txt').read_text();studies=[]
for page,txt in enumerate(raw.split('\f'),1):
 for m in re.finditer(r'Nº (\d{2})\n(.*?)Reference · ([^\n]+)',txt,re.S):
  n=int(m[1]);body=m[2].strip();head,rest=body.split('\nArt direction\n',1);direction,prompt=rest.split('\nImage prompt\n',1);lines=head.splitlines();title,subtitle=lines[:2];desc=' '.join(lines[2:]);chapter=next(c for c in chapters if c[2]<=n<=c[3])
  source=orig/f'study-{n:02}.jpg';assert source.exists()
  candidates=list(enh.rglob(f'study-{n:02}-enhanced.png'));assert len(candidates)<=1
  selected=candidates[0] if candidates else source
  target=f'study-{n:02}-selected{selected.suffix}';ref=f'study-{n:02}-reference.jpg'
  shutil.copy2(selected,a/target);shutil.copy2(source,a/ref)
  with Image.open(selected) as im:im.load();size=im.size
  studies.append(dict(number=n,title=title,subtitle=subtitle,chapter=f'{chapter[0]} {chapter[1]}',pdf_page=page,original_reference=m[3],status='enhanced' if candidates else 'original fallback',selected=target,reference=ref,width=size[0],height=size[1],source_path=str(source),selected_source_path=str(selected),description=desc,art_direction=' '.join(direction.split()),prompt=' '.join(prompt.split())))
assert [s['number'] for s in studies]==list(range(1,84))
shutil.copy2('/home/ivanaguilera/Downloads/The_Portrait_Edit_Issue_01_Redesign-2.pdf',a/'The Portrait Edit - Issue 01.pdf');shutil.copy2(base/'cover-preview.png',a/'Issue 01 - Cover Preview.png')
for source in sorted(orig.glob('cover-*.jpg')):
 candidates=list(enh.rglob(source.stem+'-enhanced.png'));assert len(candidates)<=1
 selected=candidates[0] if candidates else source
 shutil.copy2(source,a/(source.stem+'-reference.jpg'));shutil.copy2(selected,a/(source.stem+'-selected'+selected.suffix))
fields=['number','title','subtitle','chapter','pdf_page','original_reference','status','selected','reference','width','height','source_path','selected_source_path']
with (a/'Issue 01 - Image Index.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(studies)
def link(name):return f'Attachments/The Portrait Edit - Issue 01/{name}'
def embed(name,width=650):return f'![[{link(name)}|{width}]]'
lines=['---','title: The Portrait Edit — Issue 01','date: 2026-10-11','type: editorial-magazine','status: final','tags: [photography, editorial, magazine, portrait]','studies: 83','chapters: 17','---','','# The Portrait Edit','*Issue 01 · October 2026 · Fashion, film & visual studies*','',embed('Issue 01 - Cover Preview.png'),'', '> [!abstract] The issue at a glance','> **83 visual studies · 17 editorial chapters · 66 PDF pages**','> Eighty-three faces, eighty-three ways of dressing the light.','',f'[[{link("The Portrait Edit - Issue 01.pdf")}|Open the final magazine PDF]] · [[{link("Issue 01 - Image Index.csv")}|Download the CSV image index]]','', '> [!info] Image edition','> Enhanced images are used where available. Studies **18** and **44** use original references. Each study also links to its source reference. AI enhancements may change details and dimensions; original references are preserved.','', '## Editor’s letter','', 'This first issue is a study of how one detail — a ribbon, a collar, a flash of gold — can carry an entire mood. Read it slowly, borrow freely, and treat every prompt inside as an invitation to make something new.','', '## Contents','', '| Chapter | Studies |', '| --- | --- |']
for roman,title,start,end in chapters:lines.append(f'| [[#Chapter {roman} — {title}|{roman} · {title}]] | {start:02}–{end:02} |')
for roman,title,start,end in chapters:
 lines+=['','---','',f'## Chapter {roman} — {title}','']
 for s in studies[start-1:end]:
  lines += [f'### {s["number"]:02} · {s["title"]}',f'*{s["subtitle"]} · PDF page {s["pdf_page"]}*','',embed(s['selected']),'',s['description'],'','**Art direction**',s['art_direction'],'','> [!example]- Image prompt', '> '+s['prompt'],'',f'[[{link(s["reference"])}|View source reference]] · Reference filename in PDF: `{s["original_reference"]}` · **{s["status"]}**','']
lines+=['---','','## Editor’s desk','','### The palette','','| Tone | Hex |','| --- | --- |']
for tone,color in [('Amber sun','#E8B04B'),('Porcelain white','#F4F1EB'),('Ink black','#181614'),('Frozen indigo','#2F3D5C'),('Aged velvet brown','#5E3B2D'),('Soft ivory','#EFE6D2'),('Powder blue','#B7CBDD'),('Mustard ochre','#B98A2E'),('Cherry red','#8E1E2A'),('Jade teal','#2F6E66')]:lines.append(f'| {tone} | `{color}` |')
lines+=['','### Photographer’s notes','','**Lens language:** portrait compression and shallow backgrounds for intimate studies, standard perspective for full-length fashion.','','**Lighting:** use one clearly defined lighting approach per image. Amber direct light for street scenes, soft high key diffusion for studio studies, directional cinema light for the gothic scenes.','','**Composition:** protect hair silhouettes, jewelry and garment details. Leave negative space where editorial text might be added later.','','**Continuity for new prompt generation:** all generated subjects should be original adults and should not reproduce the identities of photographed people.','','## Cover image references','']
for source in sorted(orig.glob('cover-*.jpg')):
 selected=next(a.glob(source.stem+'-selected.*'));lines += [f'### Cover reference {source.stem.split("-")[-1]}','',embed(selected.name,450),'',f'[[{link(source.stem+"-reference.jpg")}|View source reference]]','']
lines+=['## Image index','','| Nº | Study | Chapter | PDF page | Image edition | Reference |','| --- | --- | --- | --- | --- | --- |']
for s in studies:lines.append(f'| {s["number"]:02} | [[#{s["number"]:02} · {s["title"]}|{s["title"]}]] | {s["chapter"]} | {s["pdf_page"]} | {s["status"]} | `{s["original_reference"]}` |')
lines+=['','> [!note] Archive','> Text and study names follow the final supplied PDF. The PDF remains the fixed layout edition; this note provides searchable text, local attachments, and chapter navigation.','']
note=out/'The Portrait Edit — Issue 01.md';note.write_text('\n'.join(lines))
for target in re.findall(r'!?\[\[([^]|]+)',note.read_text()):
 if target.startswith('#'):continue
 assert (out/target).exists(),target
assert len(studies)==83
(base/'manifest.json').write_text(json.dumps({'studies':83,'enhanced':sum(s['status']=='enhanced' for s in studies),'fallback':[s['number'] for s in studies if s['status']!='enhanced'],'files':len(list(out.rglob('*'))),'note':note.name},indent=2))
print((base/'manifest.json').read_text())
