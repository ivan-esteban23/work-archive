from pathlib import Path
import re,json,hashlib,datetime
b=Path(__file__).parent;v=Path('/home/ivanaguilera/Documents/Obsidian Vault');out=b/'native-staged';out.mkdir(exist_ok=True)
source=v/'The Portrait Edit — Issue 01 — The Fashion Issue.md';s=source.read_text();hub='The Portrait Edit — Issue 01 — Obsidian Reading Edition';folder='The Portrait Edit — Reading Edition'
backup=b/('native-backup-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'));backup.mkdir();checks={}
def stage(p,text):
 rel=p.relative_to(v); dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text)
 old=p.read_bytes();checks[str(rel)]=hashlib.sha256(old).hexdigest();bp=backup/rel;bp.parent.mkdir(parents=True,exist_ok=True);bp.write_bytes(old)
# Use actual images and native study content, preserving all source reference links.
chapters=list(re.finditer(r'^## Chapter (.+)$',s,re.M))
for i,m in enumerate(chapters):
 end=chapters[i+1].start() if i+1<len(chapters) else s.index('\n## ',m.end())
 body=s[m.end():end].strip().strip('-').strip()
 p=next((v/folder).glob(f'{i+2:02d} — *.md'))
 old=p.read_text();nav=next(line for line in old.splitlines() if line.startswith('[['+hub))
 text=f'---\ntype: magazine-chapter\nissue: 1\ntags: [editorial, magazine]\n---\n\n# {m.group(1)}\n\n{nav}\n\n{body}\n\n{nav}\n'
 text=text.replace('|650]]','|850]]')
 stage(p,text)
p=v/(hub+'.md');h=p.read_text();h=h.replace('![[Attachments/The Portrait Edit - Issue 01/Final Edition Pages/page-001.jpg|650]]','![[Attachments/The Portrait Edit - Issue 01/Issue 01 - Fashion Cover Preview.png|650]]')
h=h.replace('The finished magazine, adapted for Obsidian with its original page designs and expandable searchable text. Open a section below to read it.','The finished issue adapted into native Obsidian chapters: full-resolution enhanced photographs, editable descriptions, art direction and expandable prompts. Original page layouts remain available in the PDF and reference archive.')
h=h.replace('> Page previews preserve the PDF layout. Expand “Searchable page text” to select or search its text; PDF extraction may wrap lines or read columns in a different order. Use the original PDF for print quality.','> Chapters use the full-resolution image files matched to the supplied Upscaled Images folder. Studies 18 and 44 retain their original references, as in the final PDF. The PDF preserves the exact printed typography and page layout; native Obsidian text follows your vault theme.')
# Escape aliases only in table rows, so Obsidian does not split them into extra columns.
for line in h.splitlines():
 if line.startswith('|'): h=h.replace(line,re.sub(r'\[\[([^\]]+)\]\]',lambda m:'[['+m.group(1).replace('|',r'\|')+']]',line))
stage(p,h)
# Also repair the existing companion contents table.
for line in s.splitlines():
 if line.startswith('|'):s=s.replace(line,re.sub(r'\[\[([^\]]+)\]\]',lambda m:'[['+m.group(1).replace('|',r'\|')+']]',line))
stage(source,s)
(b/'native-before-hashes.json').write_text(json.dumps(checks));print('Prepared',len(checks),'updated notes; backups:',backup)
