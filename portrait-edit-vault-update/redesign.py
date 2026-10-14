from pathlib import Path
import re,csv,json,shutil,hashlib
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape
from PIL import Image
base=Path('/home/ivanaguilera/Work/portrait-edit-vault-update/fashion-edition');base.mkdir(exist_ok=True)
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault');assets=vault/'Attachments/The Portrait Edit - Issue 01'
old=vault/'The Portrait Edit — Issue 01.md';oldtext=old.read_text();(base/'backup').mkdir(exist_ok=True);shutil.copy2(old,base/'backup'/old.name)
rows=list(csv.DictReader((assets/'Issue 01 - Image Index.csv').open()));shutil.copy2(assets/'Issue 01 - Image Index.csv',base/'backup/Issue 01 - Image Index.csv')
for f,n in [('NotoSerifDisplay-Regular.ttf','Display'),('NotoSerif-Regular.ttf','Serif'),('NotoSans-Regular.ttf','Sans'),('NotoSans-Bold.ttf','Bold')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/noto/'+f))
chapters=[('I','Golden Hour',1,1,'Late light. Lasting impressions.'),('II','Quiet Gestures',2,3,'The face, reduced to its essentials.'),('III','Frost & Fiction',4,4,'Costume becomes a world of its own.'),('IV','Velvet Reverie',5,6,'Warm shadows and remembered textures.'),('V','Soft Structure',7,9,'Knit, color and the everyday silhouette.'),('VI','Ribbons & Lines',10,14,'Small details set the rhythm.'),('VII','Afterlight',15,22,'Heritage, winter and the darker frame.'),('VIII','Sculpted Drama',23,28,'Shape and color take the lead.'),('IX','Winter Passage',29,34,'Pale textures against a changing landscape.'),('X','Blue & Gold',35,40,'Deep color. Delicate ornament.'),('XI','City Ornament',41,46,'Tailoring meets richly patterned surfaces.'),('XII','Everyday Theatre',47,52,'Familiar clothes, unexpected presence.'),('XIII','Romantic Geometry',53,58,'Florals, checks and considered accents.'),('XIV','Modern Proportion',59,65,'Volume, contrast and clean tailoring.'),('XV','The Statement',66,71,'Bows, jewels and a commanding line.'),('XVI','Texture in Motion',72,77,'Tweed, velvet, denim and a tactile mood.'),('XVII','The New Uniform',78,83,'The wardrobe, seen with fresh eyes.')]
raw=Path('/tmp/portrait-raw.txt').read_text();data={}
for m in re.finditer(r'Nº (\d{2})\n(.*?)Reference · ([^\n]+)',raw,re.S):
 head,tail=m[2].strip().split('\nArt direction\n',1);direction,prompt=tail.split('\nImage prompt\n',1);ls=head.splitlines();data[int(m[1])]=dict(title=ls[0],subtitle=ls[1],description=' '.join(ls[2:]),direction=' '.join(direction.split()),prompt=' '.join(prompt.split()),ref=m[3])
W,H=612,792;ink='#181614';paper='#F4F1EB';accent='#8E1E2A';page_map={};pages=[]
pdf=base/'The Portrait Edit — Issue 01 — The Fashion Issue.pdf';c=canvas.Canvas(str(pdf),pagesize=(W,H));c.setTitle('The Portrait Edit — Issue 01 — The Fashion Issue');c.setAuthor('The Portrait Edit');c.setSubject('Fashion, film & visual studies — editorial edition')
def text(s,x,y,size=10,font='Sans',color=ink):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,y,s)
def para(s,x,top,width,size=10,font='Sans',color=ink,leading=None):
 p=Paragraph(escape(s),ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.45,textColor=HexColor(color)))
 _,h=p.wrap(width,700);p.drawOn(c,x,top-h);return top-h
num=0
def start(label,dark=False):
 global num
 num+=1;c.setFillColor(HexColor(ink if dark else paper));c.rect(0,0,W,H,fill=1,stroke=0)
 col=paper if dark else ink;text('THE PORTRAIT EDIT',36,764,8,'Bold',col);text('ISSUE 01 / OCTOBER 2026',390,764,7,'Sans',col)
 c.setStrokeColor(HexColor('#6E6A64' if dark else '#D1CCC3'));c.line(36,750,576,750)
 text(label.upper(),36,24,7,'Sans',col);text(f'{num:03}',550,24,8,'Sans',col);pages.append({'page':num,'label':label})
def end():c.showPage()
def photo(n,x,y,w,h):
 p=assets/rows[n-1]['selected'];im=Image.open(p);iw,ih=im.size;ratio=min(w/iw,h/ih);dw,dh=iw*ratio,ih*ratio
 c.drawImage(ImageReader(str(p)),x+(w-dw)/2,y+(h-dh)/2,width=dw,height=dh)
 page_map[n]=num
# Cover: photograph retains its complete framing.
c.setFillColor(HexColor(paper));c.rect(0,0,W,H,fill=1,stroke=0);num=1;pages.append({'page':1,'label':'Cover'})
text('THE',36,742,18,'Display');text('PORTRAIT EDIT',34,694,47,'Display');text('THE FASHION ISSUE',36,668,10,'Bold');text('01 / OCTOBER 2026',432,669,8)
photo(69,70,122,472,525);page_map.pop(69)
text('DRESSING THE LIGHT',36,88,24,'Display');text('Portraits, texture & the art of presence',36,64,10);text('83 STUDIES / 17 STORIES',397,42,8,'Bold');end()
start('Editor’s letter');text('A study in',36,680,43,'Display');text('presence.',36,628,43,'Display');y=para('Eighty-three faces, eighty-three ways of dressing the light.',36,565,470,21,'Serif')
y=para('This first issue is a study of how one detail — a ribbon, a collar, a flash of gold — can carry an entire mood. Read it slowly, borrow freely, and treat every prompt inside as an invitation to make something new.',36,y-32,440,12,'Serif')
text('83',36,280,60,'Display');text('VISUAL STUDIES',36,253,9,'Bold');text('17',240,280,60,'Display');text('EDITORIAL STORIES',240,253,9,'Bold');text('01',450,280,60,'Display');text('FASHION ISSUE',450,253,9,'Bold');para('Photography leads the issue. The reference archive preserves the art direction, prompts and source filenames behind every study.',36,180,470,10);end()
start('Contents');text('The stories',36,685,36,'Display');y=622
# Page numbers set after layout, drawn later through reserved contents data is predicted.
chapter_pages={};pageno=4
for idx,(roman,title,a,b,tag) in enumerate(chapters):
 chapter_pages[roman]=pageno;remaining=b-a
 pageno+=1+(remaining+1)//2
for roman,title,a,b,tag in chapters:
 text(roman,36,y,9,'Bold',accent);text(title,83,y,13,'Serif');text(f'{a:02}–{b:02}',468,y,9);text(f'{chapter_pages[roman]:03}',551,y,9);y-=30
text('REFERENCE ARCHIVE',36,76,8,'Bold');text(f'{pageno+1:03}',551,76,9);end()
for idx,(roman,title,a,b,tag) in enumerate(chapters):
 dark=idx in [2,3,6,7,9,14];start(title,dark);col=paper if dark else ink
 assert num==chapter_pages[roman]
 c.bookmarkPage('chapter-'+roman);c.addOutlineEntry(title,'chapter-'+roman,0)
 text(roman,36,704,12,'Bold',accent if not dark else '#E8B04B');para(title,36,674,540,36,'Display',col)
 photo(a,36,122,346,480);s=data[a];y=para(tag,406,594,170,19,'Serif',col);y=para(f'{a:02} / {s["title"]}',406,y-30,170,10,'Bold',col);para(s['description'],406,y-20,170,9,'Sans',col)
 text('FASHION, FILM & VISUAL STUDIES',36,72,8,'Sans',col);end()
 rest=list(range(a+1,b+1))
 for k in range(0,len(rest),2):
  pair=rest[k:k+2];start(title)
  if len(pair)==1:
   n=pair[0];s=data[n];photo(n,36,164,362,552);text(f'{n:02}',425,679,11,'Bold',accent);y=para(s['title'],425,646,150,24,'Display');y=para(s['subtitle'],425,y-22,150,9,'Bold');para(s['description'],425,y-20,150,9)
  else:
   # Two images in a balanced spread; alternating image heights create rhythm.
   for j,n in enumerate(pair):
    x=36+j*278;s=data[n];height=465 if (k//2)%2==0 else 425;photo(n,x,240,262,height)
    y=para(f'{n:02} / {s["title"]}',x,217,260,17,'Display');y=para(s['subtitle'],x,y-12,260,8,'Bold');bottom=para(s['description'],x,y-12,260,8.5)
    assert bottom>49,(n,bottom)
  end()
start('Editor’s desk');text('The visual language',36,682,33,'Display');palette=[('Amber sun','#E8B04B'),('Porcelain white','#F4F1EB'),('Ink black','#181614'),('Frozen indigo','#2F3D5C'),('Aged velvet brown','#5E3B2D'),('Soft ivory','#EFE6D2'),('Powder blue','#B7CBDD'),('Mustard ochre','#B98A2E'),('Cherry red','#8E1E2A'),('Jade teal','#2F6E66')]
for i,(name,col) in enumerate(palette):
 x=36+(i%5)*110;y=580-(i//5)*107;c.setFillColor(HexColor(col));c.rect(x,y,100,55,fill=1,stroke=0);text(name,x,y-18,8);text(col,x,y-33,8)
y=348
for title,s in [('Lens language','Portrait compression and shallow backgrounds for intimate studies; standard perspective for full-length fashion.'),('Lighting','One clearly defined approach per image: amber street light, soft studio diffusion, or directional cinema light.'),('Composition','Protect hair silhouettes, jewelry and garment details. Give each photograph room to breathe.')]:
 text(title.upper(),36,y,8,'Bold');y=para(s,36,y-16,530,10)-30
end()
archive_start=num+1
for pair in range(1,84,2):
 start('Reference archive');c.bookmarkPage('archive-'+str(pair))
 if pair==1:c.addOutlineEntry('Reference archive','archive-1',0)
 text('Behind the image',36,697,28,'Display')
 for j,n in enumerate(range(pair,min(pair+2,84))):
  s=data[n];top=644-j*292;text(f'{n:02} / {s["title"]}',36,top,17,'Display');text(f'REFERENCE {s["ref"]} / EDITORIAL PAGE {page_map[n]:03}',36,top-22,7,'Bold',accent)
  y=para('Art direction: '+s['direction'],36,top-42,540,9)
  y=para(s['prompt'],36,y-14,540,9)
  assert y>top-275,(n,y,top)
 end()
start('Credits & image index');text('Source & edition notes',36,679,30,'Display');y=para('Reference photography is supplied by the editor. Individual photographer and rights-holder details were not provided; source filenames are retained in the accompanying CSV and Obsidian archive.',36,619,530,11)
y=para('81 study images use AI-enhanced editions; studies 18 and 44 retain the original references. Enhancements can change details and image dimensions. These are not exact 2× reproductions.',36,y-28,530,11)
y=para('The complete original reference set, four cover references, searchable prompts and CSV image index are preserved in the Obsidian companion. Prompts describe new, original adult subjects; they are distinct from the identity-preserving enhancement workflow.',36,y-28,530,11)
para('THE PORTRAIT EDIT / ISSUE 01 / THE FASHION ISSUE\nOctober 2026',36,y-45,530,16,'Serif');end();c.save()
# Edition CSV, keeping old PDF page provenance alongside redesigned page.
for row in rows:
 n=int(row['number']);row['original_pdf_page']=row.pop('pdf_page');row['pdf_page']=str(page_map[n]);row['chapter']=next(f'{r} {t}' for r,t,a,b,_ in chapters if a<=n<=b)
with (base/'Issue 01 - Fashion Edition Image Index.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Update current note from live content, retain original archive and preserve old-name backlinks using redirect.
newname='The Portrait Edit — Issue 01 — The Fashion Issue.md';s=oldtext.replace('title: The Portrait Edit — Issue 01','title: The Portrait Edit — Issue 01 — The Fashion Issue').replace('# The Portrait Edit\n','# The Portrait Edit\n## The Fashion Issue\n').replace('66 PDF pages',f'{num} PDF pages').replace('The Portrait Edit - Issue 01.pdf','The Portrait Edit — Issue 01 — The Fashion Issue.pdf').replace('Issue 01 - Image Index.csv','Issue 01 - Fashion Edition Image Index.csv').replace('Issue 01 - Cover Preview.png','Issue 01 - Fashion Cover Preview.png')
oldnames=['The Light','The Face','The Myth','The Archive','The Lookbook','The Second Edit','The Third Edit','The Fourth Edit','The Fifth Edit','The Sixth Edit','The Seventh Edit','The Eighth Edit','The Ninth Edit','The Tenth Edit','The Eleventh Edit','The Twelfth Edit','The Thirteenth Edit']
for (r,t,a,b,_),oldtitle in zip(chapters,oldnames):s=s.replace(f'{r} — {oldtitle}',f'{r} — {t}').replace(f'{r} · {oldtitle}',f'{r} · {t}').replace(f'| {r} {oldtitle} |',f'| {r} {t} |')
for row in rows:
 n=int(row['number']);pattern=rf'(### {n:02} · [^\n]+\n\*[^\n]+ · PDF page )\d+'
 s,count=re.subn(pattern,lambda m:m[1]+row['pdf_page'],s);assert count==1
 pattern=rf'(\| {n:02} \| .*? \| {re.escape(row["chapter"])} \| )\d+'
 s,count=re.subn(pattern,lambda m:m[1]+row['pdf_page'],s);assert count==1
s+='\n## Original edition\n\n[[Attachments/The Portrait Edit - Issue 01/The Portrait Edit - Issue 01.pdf|Open the original 66-page edition]]\n'
(base/newname).write_text(s)
(base/'redirect.md').write_text('---\ntype: redirect\n---\n\n# The Portrait Edit — Issue 01\n\nThe current magazine is [[The Portrait Edit — Issue 01 — The Fashion Issue]].\n')
(base/'manifest.json').write_text(json.dumps({'pages':num,'archive_start':archive_start,'studies':83,'page_map':page_map,'chapters':chapter_pages,'original_note_sha256':hashlib.sha256(oldtext.encode()).hexdigest(),'new_note':newname},indent=2));print('Created',pdf,'pages',num)
