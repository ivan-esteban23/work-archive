from pathlib import Path
import re,json,hashlib,shutil,html
v=Path('/home/ivanaguilera/Documents/Obsidian Vault');work=Path('/home/ivanaguilera/Work/visual-edit-vault-sync-20261014');expected={}
names=['Attachments/Pinterest Alternatives/Pinterest Alternatives — Visual Research and Moodboarding.html','Pinterest Alternatives — Visual Research and Moodboarding.md','The Visual Edit — Modern Luxury UI Suggestions.md','The Visual Edit — Website Updates.md']
for n in names:
 p=v/n;expected[n]=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
 if p.exists():
  b=work/'backup'/n;b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,b)
def stage(n,s):
 p=work/'staged'/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
site=Path('/home/ivanaguilera/Work/visual-edit-public/dist/index.html').read_text();stage(names[0],site)
s=(v/names[1]).read_text().replace('updated: 2026-10-13','updated: 2026-10-14',1).replace('**Research directory · Updated 2026-10-13 · 52 sources and tools**','**Research directory · Updated 2026-10-14 · 58 sources and tools**',1)
link='\n\n[[The Visual Edit — Website Updates|Latest website updates and full A–Z source index]] · [[The Visual Edit — Modern Luxury UI Suggestions|Modern luxury design plan]] · [Live website](https://visual-edit-ivan.greymelon66.chatgpt.site)\n'
position=s.index('\n\n> [!tip]');s=s[:position]+link+s[position:]
rows=json.loads(Path('/home/ivanaguilera/Work/visual-edit-sources-20261014/sources.json').read_text())
for category in dict.fromkeys(r[3] for r in rows):
 marker='### '+category+'\n';start=s.index(marker);end=s.find('\n#',start+len(marker));end=len(s) if end==-1 else end
 section=s[start:end];new=[]
 for name,url,country,cat,lang,content,access,purpose,note,context,evidence,initials in rows:
  if cat==category:new.append(f'| {initials} | [{name}]({url}) | {country} | Global | {lang} | {content} | {access} | 2026-10-14 | {purpose} | {note} [Official context]({context}). [Country/base evidence]({evidence}). |')
 lines=section.splitlines();table_rows=[x for x in lines if x.startswith('| ') and not x.startswith('| Logo') and not x.startswith('| ---')]
 table_rows+=new;table_rows.sort(key=lambda x:re.search(r'\| \[([^]]+)\]',x)[1].casefold())
 header=[x for x in lines if x.startswith('| Logo') or x.startswith('| ---')]
 section=marker+'\n'+'\n'.join(header+table_rows)+'\n';s=s[:start]+section+s[end:]
s=s.replace('Official pages were checked on 2026-10-13.','Existing sources were checked on 2026-10-13; six additions were checked on 2026-10-14.',1);stage(names[1],s)
s=(v/names[2]).read_text().replace('Status: Design proposal; no website changes applied.','Status: Typography and color palette implemented on the live website, 14 October 2026. Other sections remain design proposals.',1)
s+='\n\n## Implementation progress · 14 October 2026\n\n- **Typography — completed:** retained Instrument Serif and Source Sans 3; fluid type scale, larger supporting text, reduced uppercase metadata, regional CJK font stacks.\n- **Color palette — completed:** applied the proposed light palette; added stronger essential control borders and a coordinated dark palette. Checked text, focus, selected and hover states.\n- **Directory — completed:** 58 sources in A–Z order; supporting website menus and reference lists alphabetized.\n- **Remaining proposals:** layout and spacing, source-card structure, navigation refinements, and editorial section design.\n\nSee [[The Visual Edit — Website Updates]] for saved version details and verification limits.\n';stage(names[2],s)
s='''# The Visual Edit — Website Updates

Updated: 14 October 2026  
Live website: https://visual-edit-ivan.greymelon66.chatgpt.site  
Current published version: **32**

[[Pinterest Alternatives — Visual Research and Moodboarding|Research directory]] · [[The Visual Edit — Modern Luxury UI Suggestions|UI design plan]] · [[Attachments/Pinterest Alternatives/Pinterest Alternatives — Visual Research and Moodboarding.html|Open the updated local HTML directory]]

## Saved changes

- Added Booooooom, Colossal, IGNANT, Frieze, The Met Collection and Rijksmuseum Collection, bringing the directory to 58 sources.
- Alphabetized all website source cards, editor picks, routes, category filters, coverage/access choices, navigation links and independent reading topics. Workflow instructions keep their logical step order.
- Retained Instrument Serif and Source Sans 3; refined headline/body scale, source-title weight, supporting text and multilingual font stacks.
- Applied warm ivory, soft white, charcoal, warm gray, pale stone and muted bronze. Essential control boundaries use a darker stone shade; dark mode uses a lighter bronze accent.
- Updated app theme colors and offline cache version. Existing favorites remain URL-based and local to each browser/device.

## Palette

| Role | Light | Dark |
| --- | --- | --- |
| Page | `#F7F4EE` | `#191817` |
| Surface | `#FFFDF9` | `#22211F` |
| Primary text | `#232323` | `#F7F4EE` |
| Supporting text | `#615B54` | `#C2BBB0` |
| Decorative dividers | `#DCD5CB` | `#49443D` |
| Bronze accent / links / focus | `#80623D` | `#BFA27A` |
| Essential control border | `#8D8274` | `#8D8274` |

## Verification and limits

Checked 24 screen-width/language combinations (320, 390, 768, 1440 px × six languages), light/dark screenshots, A–Z ordering, search/country filters, and favorite persistence. Checked 34 palette contrast pairings plus computed control-border and selected-hover states. These focused checks do not establish full WCAG conformance.

CJK fonts use regional system fallbacks and can vary by device. Physical-device installation and offline mode were not retested during these design passes. The local HTML is self-contained for its visual assets and avoids service-worker registration under `file://`; linked external sources require internet. This copied snapshot does not automatically synchronize with the hosted website. No Obsidian in-app rendering test was performed.

Source-review dates remain per source; the UI update does not constitute fresh research of all providers. The historical country audit remains dated 13 October; new-source country evidence is included in the research directory.

## Full source index · A–Z

'''
for c in re.findall(r'<article class="source".*?</article>',site,re.S):
 m=re.search(r'<h3><a href="([^"]+)"[^>]*>(.*?)<span',c,re.S);name=html.unescape(m[2].strip());s+=f'- [{name}]({html.unescape(m[1])})\n'
s+='\n## Publication record\n\nVersion 32; commit `2493e625b2414a5da315852061b02de998c59ca2`. Native Sites deployment succeeded. Workspace backups and staged copies: `/home/ivanaguilera/Work/visual-edit-vault-sync-20261014/`.\n';stage(names[3],s)
(work/'expected.json').write_text(json.dumps(expected,ensure_ascii=False,indent=2))
assert len(re.findall(r'^\| .*?\| \[', (work/'staged'/names[1]).read_text(),re.M))==58
print('Staged updated HTML, 58-source research directory, design progress, and website update note. Existing files backed up.')
