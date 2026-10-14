from pathlib import Path
import re,json,hashlib
b=Path(__file__).parent; v=Path('/home/ivanaguilera/Documents/Obsidian Vault'); out=b/'staged'; notes=out/'The Portrait Edit — Reading Edition'; notes.mkdir(exist_ok=True)
source=Path('/home/ivanaguilera/Downloads/The Portrait Edit — Issue 01 — The Fashion Issue.pdf')
pages=Path('/tmp/portrait-final.txt').read_text().split('\f')[:103]
sections=[('Opening',1,3),('I — Golden Hour',4,4),('II — Quiet Gestures',5,6),('III — Frost & Fiction',7,7),('IV — Velvet Reverie',8,9),('V — Soft Structure',10,11),('VI — Ribbons & Lines',12,14),('VII — Afterlight',15,19),('VIII — Sculpted Drama',20,23),('IX — Winter Passage',24,27),('X — Blue & Gold',28,31),('XI — City Ornament',32,35),('XII — Everyday Theatre',36,39),('XIII — Romantic Geometry',40,43),('XIV — Modern Proportion',44,47),('XV — The Statement',48,51),('XVI — Texture in Motion',52,55),('XVII — The New Uniform',56,59),('The Visual Language',60,60)]
sections += [(f'Reference Archive — {start:03d}–{min(start+5,102):03d}',start,min(start+5,102)) for start in range(61,103,6)]
sections += [('Source and Edition Notes',103,103)]
hub='The Portrait Edit — Issue 01 — Obsidian Reading Edition'
folder=notes.name; asset='Attachments/The Portrait Edit - Issue 01/Final Edition Pages'
for idx,(title,start,end) in enumerate(sections):
 name=f'{idx+1:02d} — {title}'
 nav=f'[[{hub}|Contents]]'
 if idx: nav+=f' · [[{folder}/{idx:02d} — {sections[idx-1][0]}|Previous]]'
 if idx+1<len(sections): nav+=f' · [[{folder}/{idx+2:02d} — {sections[idx+1][0]}|Next]]'
 s=f'---\ntype: magazine-section\nissue: 1\npages: "{start}–{end}"\ntags: [editorial, magazine]\n---\n\n# {title}\n\n{nav}\n'
 for n in range(start,end+1):
  s+=f'\n## Page {n:03d}\n\n![[{asset}/page-{n:03d}.jpg|850]]\n\n> [!quote]- Searchable page text\n'
  s+='\n'.join('> '+line for line in pages[n-1].strip().splitlines())+'\n'
 s+='\n'+nav+'\n'; (notes/(name+'.md')).write_text(s)
s=f'---\ntitle: {hub}\ntype: editorial-magazine\nstatus: final\nsource: "{source.name}"\npages: 103\ntags: [photography, editorial, magazine]\n---\n\n# The Portrait Edit\n## The Fashion Issue\n\n*Issue 01 · October 2026 · Dressing the Light*\n\n![[{asset}/page-001.jpg|650]]\n\nThe finished magazine, adapted for Obsidian with its original page designs and expandable searchable text. Open a section below to read it.\n\n[[Attachments/The Portrait Edit - Issue 01/{source.name}|Full-resolution final PDF]] · [[The Portrait Edit — Issue 01 — The Fashion Issue|Study descriptions, art direction, prompts and original references]]\n\n## Contents\n\n| Section | PDF pages |\n| --- | --- |\n'
for idx,(title,start,end) in enumerate(sections): s+=f'| [[{folder}/{idx+1:02d} — {title}|{title}]] | {start}–{end} |\n'
s+='\n> [!info] Reading this edition\n> Page previews preserve the PDF layout. Expand “Searchable page text” to select or search its text; PDF extraction may wrap lines or read columns in a different order. Use the original PDF for print quality.\n'
(out/(hub+'.md')).write_text(s)
checks={}
for name in ['The Portrait Edit — Issue 01.md','The Portrait Edit — Issue 01 — The Fashion Issue.md']:
 p=v/name; old=p.read_text(); checks[name]=hashlib.sha256(p.read_bytes()).hexdigest(); (b/'backup').mkdir(exist_ok=True); (b/'backup'/name).write_text(old)
 new=old+f'\n## Read the final magazine in Obsidian\n\n[[{hub}|Open the final reading edition]] — original page layouts, linked chapters and searchable page text.\n'
 (out/name).write_text(new)
(b/'before-hashes.json').write_text(json.dumps(checks))
(b/'SESSION.md').write_text('Built a reading edition from the user-designated final Downloads PDF (103 pages). Existing vault PDF is byte-identical. Preserved companion study content; added chapter navigation, page previews, expandable PDF text, and links from the existing issue notes. No Obsidian settings changed.\n')
print('Prepared',len(sections),'section notes and reading dashboard.')
