import json,re
from pathlib import Path
root=Path(__file__).parent;rows=json.loads((root/'records.json').read_text());covers=json.loads((root/'covers.json').read_text());out=root/'ready';out.mkdir(exist_ok=True)
folder='Goth Rock — Notion Snapshot 2026-10-09';encyclopedia='Goth Rock — Encyclopedia History';bands='Goth Rock — Bands and Contributions';guide='Goth Rock — Expanded Listening Guide'
def clean(s):return re.sub(r'[\\/:*?"<>|]','—',s).strip()
def link(r):return '[['+folder+'/Album — '+clean(r['artist'])+' — '+clean(r['album'])+'|'+r['artist']+' — '+r['album']+']]'
header='Research checked **9 October 2026**. Added manually to both the live Notion project and this local library; the two versions do not synchronize automatically.\n\n'
for name in [encyclopedia,bands]:
 text=(root/(name+'.md')).read_text();text=text.replace('## Listening routes','## Listening routes')
 text+='\n## Companion notes\n\n[['+encyclopedia+']] · [['+bands+']] · [['+guide+']] · [[Goth Rock — Start Here]]\n'
 if name==encyclopedia:
  diagram='''## Period map

```mermaid
flowchart TD
 A["Late 1970s–early 1980s: post-punk foundations"] --> B["Early 1980s: UK scenes and clubs"]
 A --> C["Parallel US deathrock"]
 B --> D["Mid–late 1980s: guitar-led expansion"]
 A --> E["Atmospheric branches"]
 D --> F["1990s–2000s: continuation and recombination"]
 C --> F
 E --> F
 F --> G["2010s–2020s: multiple contemporary paths"]
```

The arrows organize the account chronologically; they are not assertions that every band in one box directly influenced every band in the next.

'''
  text=text.replace('## What developed:',diagram+'## What developed:',1)
 (out/(name+'.md')).write_text(text)
body='# '+guide+'\n\n'+header+'**28 additional original studio albums**, organized by period and listening purpose. Together with the 11 existing dossier albums, the gallery contains 39 albums. The separate 2026 Bandcamp discovery shelf remains available in the listening room. This is an editorial exploration library, not a ranking or a record of albums you have heard.\n\n'
body+='## Start with three\n\nFor your raw-deathrock interest: **UK Decay — For Madmen Only → Sex Gang Children — Song and Legend → Nox Novacula — Feed the Fire**. This route moves from a punk-rooted historical comparison to theatrical arrangements and a newer deathrock experiment. Keep 45 Grave, Kommunity FK, and Cinema Strange as your existing reference route.\n\n'
body+='For the larger guitar sound: **The Mission — God’s Own Medicine → Fields of the Nephilim — Dawnrazor → Rosetta Stone — An Eye for the Main Chance**. For atmosphere: **Cocteau Twins — Treasure → Faith and the Muse — Elyria → Drab Majesty — The Demonstration**.\n\n'
body+='## How to read the records\n\nThe year is the original album year. Linked pages may describe later editions or archival boxes. A catalog/history page is labeled as such and may require following its listening link. Personal listening status stays unknown. The questions are suggestions, not findings from direct audio access. Twenty dossiers include authentic artwork or edition product images downloaded from their official source pages. The remaining eight retain source links while separate cover selection remains open.\n\n'
for period in dict.fromkeys(r['period'] for r in rows):
 body+='## '+period+'\n\n| Dossier | Original year | Direction |\n| --- | --- | --- |\n'
 for r in rows:
  if r['period']==period:body+='| '+link(r).replace('|','\\|')+' | '+str(r['year'])+' | '+r['style']+' |\n'
 body+='\n'
body+='## Continue into 2026\n\n[[Goth Rock — Notion Snapshot 2026-10-09/Goth Rock — Research and Listening|Open the listening room]] for its existing six released 2026 discoveries, direct Bandcamp links and covers, plus the separately marked preorder. Follow Normal Weirds and Illegal Funeral for the current raw-deathrock leads, or Ductape for a darkwave contrast. That list is a dated sample, not an exhaustive latest-release list.\n\n'
body+='## Record an actual reaction\n\n- **Album and edition:**\n- **Sample or full listen:**\n- **Date, if known:**\n- **What worked:**\n- **What did not:**\n- **Memorable track or moment:**\n- **Next action:**\n- **Optional personal score:**\n\n[['+encyclopedia+']] · [['+bands+']] · [[Goth Rock — Start Here]]\n'
(out/(guide+'.md')).write_text(body)
album_payload=[]
for i,r in enumerate(rows):
 c=covers.get(str(i));image=c and c.get('url');r['note']='Album — '+clean(r['artist'])+' — '+clean(r['album']);content='Research checked 2026-10-09. **Original studio full-length · original year '+str(r['year'])+' · personal listening status unknown.**\n\n'
 if image:
  caption=r['artist']+' — '+r['album']+'. Artwork or edition product image from the linked official source; reflects that edition.'
  content+='!['+caption+']('+image+')\n\n[Artwork / edition source]('+r['source']+')\n\n'
 content+='## Place in the history\n\n'+r['period']+' · '+r['style']+'. This classification is a listening-guide category; related styles and a band’s other albums may differ.\n\n'
 content+='## Original and linked edition\n\n'+r['edition']+'\n\n[Album / edition page]('+r['source']+')'
 if r['year_source']!=r['source']:content+=' · [Original-year evidence]('+r['year_source']+')'
 content+='\n\n## Listening question\n\n'+r['question']+' This is an editorial question, not a report of direct listening.\n\n## Your reaction\n\nNo listening session or score has been added. Record the exact edition and whether you sampled or heard the full album when you report feedback.\n'
 props={'Album':r['album'],'Artist':r['artist'],'Original year':r['year'],'Order':12+i,'Listening status':'Unknown','Listen':r['source'],'Edition':r['edition'],'Entry track':'Use the original album sequence; see dossier question','Shelf':'Atmospheric detour' if r['style'] in {'Darkwave','Ethereal / atmospheric'} else 'Historical reference','Style':json.dumps([r['style']])}
 page={'properties':props,'content':content,'icon':'💿'}
 if image:page['cover']=image
 album_payload.append(page)
 local=content
 if image:local=re.sub(r'!\[([^\]]*)\]\([^)]+\)',lambda m:'![['+folder+'/Attachments/encyclopedia-'+c['file']+']]\n\n*'+m[1]+'*',local,count=1)
 local='# '+r['note']+'\n\n'+local+'\n[['+encyclopedia+']] · [['+bands+']] · [['+guide+']]\n'
 (out/(r['note']+'.md')).write_text(local)
(root/'album-payload.json').write_text(json.dumps(album_payload,ensure_ascii=False,indent=2));(root/'records.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
# Source index records claims, limitations, and only the sources actually used.
sources={}
for r in rows:
 for url in {r['source'],r['year_source']}:sources.setdefault(url,[]).append(r['artist']+' — '+r['album']+': original year / linked edition / catalog identity')
for name in [encyclopedia,bands]:
 for url in re.findall(r'\]\((https?://[^)]+)\)',(out/(name+'.md')).read_text()):sources.setdefault(url,[]).append(name+': adjacent cited statement')
index='# Goth Rock encyclopedia — source index\n\nChecked 9 October 2026. Artist/label catalogs establish their own metadata; promotional influence claims remain attributed. Histories and specialist reporting supply interpretations. Existing-dossier references were retained from the supplied local notes. Publication dates are included where visible in the encyclopedia; missing dates are not invented.\n\n'
for url,claims in sources.items():index+='- ['+url.split('/')[2]+']('+url+') — '+('; '.join(dict.fromkeys(claims)))+'\n'
(root/'SOURCE INDEX.md').write_text(index)
print(json.dumps({'new_albums':len(rows),'profiles':26,'new_artwork':sum(bool(c and c.get('url')) for c in covers.values()),'ready_notes':len(list(out.glob('*.md')))}))
