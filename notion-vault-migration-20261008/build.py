from pathlib import Path
from collections import defaultdict,Counter
from urllib.parse import quote,unquote,urlsplit
from html.parser import HTMLParser
import os,re,html,json,csv,hashlib,shutil,zipfile,datetime
import markdown
BASE=Path('/home/ivanaguilera/Work/notion-vault-migration-20261008')
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
OUT=BASE/'deliverables';OUT.mkdir(exist_ok=True)
SNAP=BASE/'content-snapshot';IMPORT=BASE/'html-import'/'Obsidian Vault Import'
assert not SNAP.exists() and not IMPORT.exists(),'Use a new output directory for a new snapshot.'
allfiles=sorted(p for p in VAULT.rglob('*') if p.is_file())
visible=[];excluded=[]
for p in allfiles:
 rel=p.relative_to(VAULT)
 if any(part.startswith('.') for part in rel.parts):excluded.append(str(rel));continue
 if p.is_symlink():raise RuntimeError('Symlink requires explicit handling: '+str(rel))
 visible.append(p)
manifest=[]
for p in visible:
 rel=p.relative_to(VAULT);dest=SNAP/rel;dest.parent.mkdir(parents=True,exist_ok=True);raw=p.read_bytes();dest.write_bytes(raw)
 manifest.append({'path':str(rel),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
files={str(p.relative_to(SNAP)):p for p in SNAP.rglob('*') if p.is_file()}
backups=[r for r in files if '.bak-' in r]
content=[r for r in files if r not in backups]
images={r for r in content if Path(r).suffix.lower() in {'.png','.jpg','.jpeg','.webp','.gif','.svg'}}
notes={r for r in content if Path(r).suffix.lower()=='.md'}
data=set(content)-images-notes
mapping={r:(str(Path(r).with_suffix('.html')) if r in notes else r+'.html') for r in notes|data}
for r in images:
 d=IMPORT/r;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(files[r],d)
lookup=defaultdict(list)
for r in content:
 for k in {r,Path(r).name,Path(r).stem,(r[:-3] if r.endswith('.md') else r)}:lookup[k.casefold()].append(r)
issues=[];stats=Counter();linklog=[]
def issue(source,kind,target,detail):issues.append({'source':source,'type':kind,'target':target,'detail':detail})
def resolve(target,source):
 target=unquote(target).strip().replace('\\','/')
 if not target:return source
 candidates=[]
 for x in [(Path(source).parent/target).as_posix(),target]:
  x=os.path.normpath(x)
  if x in files and x in content:return x
  if x+'.md' in notes:return x+'.md'
 candidates=list(dict.fromkeys(lookup.get(target.casefold(),[])))
 if len(candidates)==1:return candidates[0]
 if len(candidates)>1:issue(source,'ambiguous-link',target,'Multiple matching source files: '+', '.join(candidates))
 else:issue(source,'missing-link',target,'No matching vault file; original label retained.')
 return None
def desthref(target,source):
 out=target if target in images else mapping[target]
 return quote(os.path.relpath(out,Path(mapping[source]).parent).replace(os.sep,'/'),safe='/')
def wikiconvert(segment,source):
 def sub(m):
  embed=bool(m[1]);raw=m[2];target,sep,label=raw.partition('|');target,hashmark,section=target.partition('#')
  found=resolve(target,source);display=label or (Path(target).stem if target else section)
  if section:
   stats['section_links']+=1
   issue(source,'section-link',raw,'Converted to the target page; Notion section anchors require manual repair.')
   display=(label or Path(target or source).stem)+' — section: '+section
  if found is None:return html.escape(display or raw)
  href=desthref(found,source);stats['wiki_embeds' if embed else 'wiki_links']+=1
  linklog.append({'source':source,'target':found,'kind':'image' if embed and found in images else 'page'})
  if embed and found in images:
   size=label if re.fullmatch(r'\d+(?:x\d+)?',label or '') else ''
   width=f' width="{size.split("x")[0]}"' if size else ''
   return f'<img src="{href}" alt="{html.escape(Path(found).stem,quote=True)}"{width} />'
  if embed:
   issue(source,'note-transclusion',raw,'Preserved as a link to its page; no live transclusion in Notion.')
  return f'<a href="{href}">{html.escape(display or Path(found).stem)}</a>'
 return re.sub(r'(!?)\[\[([^\]\n]+)\]\]',sub,segment)
def convertmd(text,source):
 metadata=''
 if text.startswith('---\n'):
  match=re.match(r'\A---\n(.*?)\n---\n',text,re.S)
  if match:
   metadata='<h2>Original note metadata</h2><pre><code>'+html.escape(match[1])+'</code></pre>'
   text=text[match.end():];stats['frontmatter_notes']+=1
   issue(source,'frontmatter',source,'Preserved as visible metadata text, not native Notion properties.')
 lines=text.splitlines(keepends=True);output=[];normal=[];i=0
 def flush():
  if normal:
   s=''.join(normal)
   # Callout labels become ordinary, readable blockquotes.
   def callout(m):
    stats['callouts']+=1;return '> **'+m[1].capitalize()+'**'+(' — '+m[2] if m[2] else '')+'\n'
   s=re.sub(r'^>\s*\[!([^\]]+)\][+-]?\s*(.*?)\n',callout,s,flags=re.M)
   # Inline code stays literal.
   chunks=re.split(r'(`+[^`\n]*`+)',s)
   output.append(''.join(c if c.startswith('`') else wikiconvert(c,source) for c in chunks));normal.clear()
 while i<len(lines):
  m=re.match(r'^\s{0,3}(`{3,}|~{3,})([^\n]*)',lines[i])
  if not m:normal.append(lines[i]);i+=1;continue
  flush();fence=m[1];lang=m[2].strip();block=[lines[i]];i+=1
  while i<len(lines):
   block.append(lines[i]);i+=1
   if re.match(r'^\s{0,3}'+re.escape(fence[0])+r'{'+str(len(fence))+r',}\s*$',block[-1].rstrip('\n')):break
  if lang in {'mapview','dataview','dataviewjs','leaflet','mermaid','query'}:
   stats['plugin_blocks']+=1
   issue(source,'plugin-block',lang,'Retained as code. Rebuild this interactive feature in Notion or embed a separately hosted tool.')
   output.append(f'\n> **Migration note:** This `{lang}` block is preserved as configuration text. It will not execute in Notion.\n\n')
  output.append(''.join(block))
 flush()
 rendered=markdown.markdown(''.join(output),extensions=['tables','fenced_code','sane_lists'])
 return rendered+metadata
class Rewriter(HTMLParser):
 def __init__(self,source):super().__init__(convert_charrefs=False);self.source=source;self.out=[]
 def attrs(self,attrs):
  result=[]
  for key,value in attrs:
   if key in {'href','src'} and value:
    parsed=urlsplit(value)
    if parsed.scheme:
     if parsed.scheme in {'obsidian','geo','file'}:issue(self.source,'app-or-local-link',value,'Not a native Notion page link; needs a compatible app or manual replacement.')
    elif not parsed.netloc:
     # Already-converted wiki paths are .html or image files; ordinary Markdown paths still need conversion.
     decoded=unquote(parsed.path)
     candidate=os.path.normpath(str(Path(mapping[self.source]).parent/decoded))
     if candidate in mapping.values() or candidate in images:
      if parsed.fragment:
       issue(self.source,'section-link',value,'Dropped section anchor; target-page navigation retained.');value=value.split('#')[0]
     elif decoded or parsed.fragment:
      target=resolve(decoded,self.source)
      if target:
       value=desthref(target,self.source)
       if parsed.fragment:issue(self.source,'section-link',parsed.fragment,'Dropped Markdown section anchor; target-page navigation retained.')
      else:
       # Preserve the label, but do not leave a computer-specific or missing file URL.
       result.append('title="'+html.escape(value,quote=True)+'"')
       continue
   result.append(key if value is None else f'{key}="{html.escape(value,quote=True)}"')
  return (' '+' '.join(result)) if result else ''
 def handle_starttag(self,tag,attrs):self.out.append('<'+tag+self.attrs(attrs)+'>')
 def handle_startendtag(self,tag,attrs):self.out.append('<'+tag+self.attrs(attrs)+' />')
 def handle_endtag(self,tag):self.out.append('</'+tag+'>')
 def handle_data(self,data):self.out.append(data)
 def handle_entityref(self,name):self.out.append('&'+name+';')
 def handle_charref(self,name):self.out.append('&#'+name+';')
 def handle_comment(self,data):self.out.append('<!--'+data+'-->')
def document(title,body):return '<!doctype html>\n<html><head><meta charset="utf-8"><title>'+html.escape(title)+'</title></head><body>\n'+body+'\n</body></html>\n'
for source in sorted(notes|data):
 if source in notes:
  body=convertmd(files[source].read_text(),source);rw=Rewriter(source);rw.feed(body);body=''.join(rw.out)
 else:
  raw=files[source].read_text(encoding='utf-8-sig');body='<h1>'+html.escape(Path(source).name)+'</h1>'
  body+='<p>Preserved attachment content. This is a readable copy, not an interactive app or an automatically configured database. The original file is in the content archive.</p>'
  if source.endswith('.csv'):
   rows=list(csv.reader(raw.splitlines()));body+='<table>'
   for n,row in enumerate(rows):
    tag='th' if n==0 else 'td';body+='<tr>'+''.join(f'<{tag}>{html.escape(cell)}</{tag}>' for cell in row)+'</tr>'
   body+='</table>'
   issue(source,'csv-attachment',source,'Readable table in HTML pack; import original CSV separately if a native database is wanted.')
  else:body+='<pre><code>'+html.escape(raw)+'</code></pre>'
  stats['attachment_pages']+=1
 p=IMPORT/mapping[source];p.parent.mkdir(parents=True,exist_ok=True);p.write_text(document(Path(source).stem,body))
# A portable index keeps original names and paths without imposing a new organization on the vault.
items=[]
for source in sorted(notes,key=str.casefold):items.append('<li><a href="'+quote(mapping[source],safe='/')+'">'+html.escape(source[:-3])+'</a></li>')
landing='<h1>Obsidian Vault — Imported Content</h1><p>Snapshot: 8 October 2026. Imported from a copy; live vault unchanged. Check page links and images after import. Map View configurations and other app features do not execute here. Original metadata is retained as text.</p><h2>Notes</h2><ul>'+''.join(items)+'</ul>'
landing+='<h2>Readable attachment pages</h2><ul>'+''.join('<li><a href="'+quote(mapping[r],safe='/')+'">'+html.escape(r)+'</a></li>' for r in sorted(data))+'</ul>'
(IMPORT/'00 — Start Here.html').write_text(document('Obsidian Vault — Imported Content',landing))
# Check every local generated image/link against the actual packaged files.
class Checker(HTMLParser):
 def __init__(self,p):super().__init__();self.p=p
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k not in {'href','src'} or not v:continue
   parsed=urlsplit(v)
   if parsed.scheme or parsed.netloc:continue
   target=(self.p.parent/unquote(parsed.path)).resolve()
   assert target.is_relative_to(IMPORT.resolve()),'Output link points outside packaged root: '+v
   if not target.exists():raise RuntimeError('Broken output link: '+str(self.p)+' -> '+v)
for p in IMPORT.rglob('*.html'):
 c=Checker(p);c.feed(p.read_text())
# Ensure none of the live source content changed while the snapshot was prepared.
for row in manifest:
 assert hashlib.sha256((VAULT/row['path']).read_bytes()).hexdigest()==row['sha256'],'Live file changed: '+row['path']
assert len(list(IMPORT.rglob('*.html')))==len(notes)+len(data)+1
assert len(list(IMPORT.rglob('*.png')))+len(list(IMPORT.rglob('*.jpeg')))+len(list(IMPORT.rglob('*.jpg')))==len(images)
def zipfolder(folder,path,select=None):
 with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(folder.rglob('*')):
   if p.is_file() and (select is None or p in select):z.write(p,str(Path(folder.name)/p.relative_to(folder)))
 with zipfile.ZipFile(path) as z:assert z.testzip() is None
zipfolder(IMPORT,OUT/'Obsidian Vault — Notion HTML Import.zip')
zipfolder(SNAP,OUT/'Obsidian Vault — Original Content Archive.zip')
# A portrait-only pilot includes its linked TXT library page and all ten image resources.
pilot=BASE/'pilot'/'Portrait Import Test';pilot.mkdir(parents=True)
for r in ['Editorial Portrait Prompt Library.md','Attachments/Editorial Portraits/Editorial Portrait — Prompt.txt']:
 dest=pilot/mapping[r];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(IMPORT/mapping[r],dest)
for r in images:
 dest=pilot/r;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(IMPORT/r,dest)
zipfolder(pilot,OUT/'Portrait Library — Notion Import Test.zip')
# CSV originals remain separate to avoid accidental database creation during the HTML migration.
CSVOUT=OUT/'CSV for optional Notion databases';CSVOUT.mkdir(exist_ok=True)
for r in data:
 if r.endswith('.csv'):shutil.copy2(files[r],CSVOUT/Path(r).name)
(OUT/'Source manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False))
(OUT/'Link conversion log.json').write_text(json.dumps(linklog,indent=2,ensure_ascii=False))
with (OUT/'Migration issues.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['source','type','target','detail']);w.writeheader();w.writerows(issues)
counts=Counter(x['type'] for x in issues)
summary={'notes':len(notes),'original_content_files':len(files),'images':len(images),'readable_attachment_pages':len(data),'historical_backups_archived_only':len(backups),'hidden_files_excluded':len(excluded),'stats':dict(stats),'issue_counts':dict(counts),'total_html_pages':len(list(IMPORT.rglob('*.html')))}
(OUT/'Summary.json').write_text(json.dumps(summary,indent=2))
report=f'''# Notion migration report — 8 October 2026

Built from a consistent read-only snapshot of `/home/ivanaguilera/Documents/Obsidian Vault`. Live notes and settings were not changed. Nothing has been uploaded to Notion.

## Contents

- {len(notes)} original Markdown notes converted to HTML pages.
- {len(images)} unchanged images bundled with valid local image paths.
- {len(data)} non-image attachments preserved as readable HTML pages (CSV tables or literal text), with originals in the content archive.
- One generated start page listing every note and readable attachment page.
- {len(backups)} historical backup files retained only in the original-content archive, avoiding duplicate imported pages.
- Hidden files and folders, including `.obsidian` plugin settings, excluded from both packages. This is a note/content archive, not a complete Obsidian configuration backup.

## Transformations

- {stats['wiki_links']} wiki links converted to ordinary HTML links.
- {stats['wiki_embeds']} image/embed references converted.
- {stats['section_links']} wiki section links converted to page links with visible section labels; Notion heading navigation may need manual repair.
- {stats['frontmatter_notes']} note metadata blocks kept as readable text, not native database properties.
- {stats['callouts']} callout labels kept as ordinary blockquotes.
- {stats['plugin_blocks']} plugin blocks kept as readable configuration; they are not interactive maps.
- Fenced prompt examples remain literal code; links inside examples are not rewritten as live navigation.

## Import limitations

Notion may not remap every relative HTML page link to a native Notion page link. Local output links were checked, but this does not prove successful Notion remapping. Inspect your dashboards after import. Section anchors, application links, metadata properties, image sizing, table layout, and plugin functions may need repair. CSVs in the optional folder can be imported separately as databases; importing them in addition to HTML tables creates separate copies with no automatic synchronization.

Notion's official guide documents desktop/web imports, HTML with reachable bundled images, and ZIP imports. It also documents plan-specific per-file limits and roughly 120 file imports per 12 hours; this pack has {summary['total_html_pages']} HTML pages, so an import may be throttled or partial. Check progress and partial pages before retrying. The portrait test has just two HTML pages and ten images.

Source checked 8 October 2026: https://www.notion.com/help/import-data-into-notion

## Issues for review

'''+''.join(f'- {k}: {v}\n' for k,v in sorted(counts.items()))+'''
See `Migration issues.csv` for per-file details. Missing source links are preserved as readable labels rather than inventing destinations. Native Notion page links and working map views require review after import.

## Verification performed

All source hashes were checked against the live files after conversion. The original archive preserves each included file byte for byte. Every generated local HTML href/src resolves to a packaged file. All ZIP archives passed integrity checks. These are filesystem/conversion checks, not a live test inside Notion.
'''
(OUT/'Migration report.md').write_text(report)
readme='''# Import your Obsidian content into Notion

## 1. Test the portrait library

On Notion desktop or web, go to Settings → Import → Convert Zip to pages. Upload `Portrait Library — Notion Import Test.zip` into a temporary/private test location. Inspect entry 05 and the other reference/result pairs: ten images should be present. The ZIP also has the linked prompt-library text as an HTML page. Check the prompt code blocks and image links. Remove the temporary test pages before the full import if you want to avoid duplicates.

## 2. Import the full pack

Use the same importer with `Obsidian Vault — Notion HTML Import.zip`. Choose a private destination named “Obsidian Vault Import” if the importer offers destination selection. Open the generated “00 — Start Here” page and inspect the Japan/Korea/China dashboards, Music Prompt Library, Goth Rock and Spotify prompts, and Editorial Portrait Prompt Library.

The package preserves original note names and folder paths. Native Notion hierarchy and page-link remapping need checking after import. The official importer has rate and plan limits: this full pack exceeds roughly 120 page files. If the import stops, check Import progress and partially created pages; wait for the import allowance to reset before retrying affected files, and avoid blindly importing the whole ZIP again. The extracted `html-import` folder in the workspace can support targeted retries with the same asset paths.

## 3. Repair special features

Consult `Migration report.md` and `Migration issues.csv`. Map View blocks remain text, and should be rebuilt as Notion Map database views or separately hosted embeds. Convert preserved metadata into properties only if you want databases. Section links may need to be replaced with Notion heading links. Unsupported original attachments remain in the archive; upload manually as files where useful.

## 4. Optional CSV databases

The `CSV for optional Notion databases` folder contains the original two CSV files. Import through Settings → Import → CSV only if you want native databases in addition to the readable HTML tables. The destination searches are search leads, not a fully verified unique-venue database. Add/verify a Place property before using a Notion Map view.

## 5. Keep the original archive

`Obsidian Vault — Original Content Archive.zip` includes unchanged notes, attachments, and three historical backup files. It excludes hidden configuration folders. Keep your live Obsidian vault until you have reviewed the imported content. Importing creates a snapshot, not ongoing synchronization. Nothing in this pack modifies your vault or creates content in Notion automatically.

Official import instructions, checked 8 October 2026: https://www.notion.com/help/import-data-into-notion
'''
(OUT/'READ ME FIRST.md').write_text(readme)
print(json.dumps(summary,indent=2))
