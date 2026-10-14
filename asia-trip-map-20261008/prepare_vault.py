from pathlib import Path
from urllib.parse import urlencode
import csv,json,re,hashlib,shutil,collections

b=Path(__file__).resolve().parent
v=Path('/home/ivanaguilera/Documents/Obsidian Vault')
s=b/'staged'
data=json.loads((b/'All destination searches.json').read_text())
pins=json.loads((b/'Existing orientation pins.json').read_text())
# Explicitly reviewed prose-only research leads; generated links remain searches.
extras=[
 ('China','Beijing','北京','China Travel Guide.md','Beijing','Proposed base'),
 ('China','Xi’an','西安','China Travel Guide.md','Xi’an','Proposed base'),
 ('China','Shanghai','上海','China Travel Guide.md','Shanghai','Proposed base'),
 ('China','Suzhou','苏州','China — More Ideas and Route Choices.md','Suzhou','Optional excursion'),
 ('China','Hangzhou','杭州','China — More Ideas and Route Choices.md','Hangzhou','Optional tea base'),
 ('China','Chengdu','成都','China — More Ideas and Route Choices.md','Chengdu','Alternative base'),
 ('China','Chongqing','重庆','China — More Ideas and Route Choices.md','Chongqing','Alternative base'),
 ('China','Zhangjiajie','张家界','China — More Ideas and Route Choices.md','Zhangjiajie','Alternative landscape base'),
 ('China','Dongcheng','东城','China Travel Guide.md','Dongcheng','Hotel search area; no selected hotel'),
 ('China','Jing’an','静安','China Travel Guide.md','Jing’an','Hotel search area; no selected hotel'),
 ('China','Xuhui','徐汇','China Travel Guide.md','Xuhui','Hotel search area; no selected hotel'),
 ('China','Xi’an Bell Tower','西安钟楼','China Travel Guide.md','Bell Tower','Hotel search area anchor'),
 ('China','Lingering Garden','留园','China — More Ideas and Route Choices.md','Lingering Garden','Optional garden alternative'),
 ('China','Kuanzhai lanes','宽窄巷子','China — More Ideas and Route Choices.md','Kuanzhai','Optional research candidate'),
 ('China','Chengdu panda base','成都大熊猫繁育研究基地','China — More Ideas and Route Choices.md','panda base','Exact attraction/access research pending'),
 ('China','Liziba','李子坝','China — More Ideas and Route Choices.md','Liziba','Viewpoint/access research pending'),
 ('China','Fangsheng Bridge','放生桥','China — More Ideas and Route Choices.md','Fangsheng Bridge','Optional Zhujiajiao sight'),
 ('Japan','Teshima Kagawa Japan','','Japan 2027 — Best Islands.md','Teshima','Optional second island day'),
 ('Japan','Jomon Sugi Yakushima Japan','','Japan 2027 — Best Islands.md','Jomon Sugi','Separate strenuous hiking research option'),
]
added=[]
for country,name,native,note,needle,status in extras:
 text=(v/note).read_text()
 assert needle in text,(note,needle)
 if any(name.casefold() in r['search_text'].casefold() for r in data if r['country']==country):continue
 query=native or name
 url='https://uri.amap.com/search?'+urlencode({'keyword':query,'view':'list','callnative':'1'}) if country=='China' else 'https://www.google.com/maps/search/?'+urlencode({'api':'1','query':query})
 r={'country':country,'search_text':name,'native_search_text':native,'city_scope':'','map_search_url':url,'coordinate_status':'No coordinate; generated search from reviewed prose','planning_status':status,'source_notes':[note],'context_lines':[line for line in text.splitlines() if needle in line]}
 data.append(r);added.append(r)

# Include inherited coordinate entries absent from the search inventory.
for p in pins:
 if not any(p['name'].casefold().split(' — ')[0] in r['search_text'].casefold() for r in data if r['country']==p['country']):
  data.append({'country':p['country'],'search_text':p['name'],'city_scope':'','map_search_url':'','coordinate_status':p['status'],'source_notes':[p['source_note']],'context_lines':[]})

att=Path('Attachments/Asia Trip Maps')
target=s/att;target.mkdir(parents=True,exist_ok=True)
(target/'All destination searches.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(target/'Existing orientation pins.json').write_text(json.dumps(pins,ensure_ascii=False,indent=2))
with (target/'All destination searches.csv').open('w',encoding='utf-8-sig',newline='') as f:
 fields=['country','search_text','native_search_text','city_scope','map_search_url','coordinate_status','planning_status','source_notes']
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in data:w.writerow({k:'; '.join(r[k]) if isinstance(r.get(k),list) else r.get(k,'') for k in fields})
shutil.copy2(b/'ChatGPT Maps prompt.txt',target/'ChatGPT Maps prompt.txt')
counts=collections.Counter(r['country'] for r in data)
title='Asia Trips — Combined Map and Destination Inventory'
note=f'''# {title}

[[China — Start Here]] · [[Japan 2027 — Start Here]] · [[Korea 2026 — Start Here]]

**Vault review: 8 October 2026.** Shared geographic overview of three separate research projects. It does not combine their itineraries or confirm any destination, booking, season, or trip date.

## Location inventory

| Project | Search / location entries |
| --- | ---: |
| China | {counts['China']} |
| Japan | {counts['Japan']} |
| Korea | {counts['Korea']} |

Counts are source entries, **not unique verified venues**. Aliases and different queries may point to the same place; different branches must remain separate. The original search extraction was expanded with {len(added)} reviewed prose-only leads. Pins missing from that inventory were retained too. No exhaustive claim is made for every place mentioned in prose or future additions.

- [CSV — attach to a map-capable ChatGPT chat](Attachments/Asia%20Trip%20Maps/All%20destination%20searches.csv)
- [Full inventory with source-note/context evidence](Attachments/Asia%20Trip%20Maps/All%20destination%20searches.json)
- [Existing orientation coordinates](Attachments/Asia%20Trip%20Maps/Existing%20orientation%20pins.json)
- [Copy-ready ChatGPT Maps prompt](Attachments/Asia%20Trip%20Maps/ChatGPT%20Maps%20prompt.txt)

## Combined Obsidian map

The map below uses the existing Japan and Korea coordinate directories: **{len(pins)} orientation pins**. It requires an available Obsidian Map View plugin. No settings were changed and rendering was not tested. Coordinates are inherited, not newly surveyed entrances. China and most shops/cafés remain in the inventory until exact place identity and coordinates are checked. Do not assume Amap coordinates and another map’s coordinate system are interchangeable.

```mapview
{{
  "name": "Asia Trips — Existing Orientation Pins",
  "mapZoom": 4,
  "centerLat": 36.5,
  "centerLng": 133.0,
  "query": "tag:#japan2027 OR tag:#korea2026",
  "chosenMapSource": 0,
  "autoFit": true,
  "lock": false,
  "showLinks": false,
  "markerLabels": "off",
  "embeddedHeight": 540
}}
```

Existing pin directories: [[Japan 2027 — Map View]] and [[Korea 2026 — Map View]]. The combined block reads their existing tagged locations; the inventory does not assign guessed coordinates to unresolved places.

## Added from reviewed prose

'''+ '\n'.join(f"- **{r['country']} — {r['search_text']}**: {r['planning_status']}. [[{Path(r['source_notes'][0]).stem}]] · [Location search]({r['map_search_url']})" for r in added)+'''

## Use with ChatGPT Maps

Attach the CSV and copy the prompt file into a chat that supports native maps. Resolve places country by country and city by city, tracking mapped, unresolved, and pending entries. This session has no native ChatGPT map-writing tool; no upload, saved native map, phone handoff, or cross-device map rendering has been performed.

## Remaining checks

Confirm exact shop branches, area versus entrance pins, old unresolved business names, duplicates, and regional map results before navigating. Keep conditional/optional candidates separate from chosen route stops. Places mentioned without a map link may still need a further chapter-specific review.
'''
(s/(title+'.md')).write_text(note)
manifest=[]
def item(rel,expected=None):manifest.append({'relative':str(rel),'expected':expected})
for p in s.rglob('*'):
 if p.is_file():
  rel=p.relative_to(s)
  assert not (v/rel).exists(),rel
  item(rel)
dashboards=['China — Start Here.md','Japan 2027 — Start Here.md','Korea 2026 — Start Here.md']
recaps=['China — Session Recap 2026-10-08.md','Japan 2027 — Session Recap 2026-10-08.md','Korea 2026 — Session Recap 2026-10-08.md']
for name in dashboards+recaps:
 raw=(v/name).read_bytes();old=raw.decode()
 backup=b/'backup'/name;backup.parent.mkdir(exist_ok=True);backup.write_bytes(raw)
 addition=f'\n\n## Combined destination inventory · 8 October 2026\n\n[[{title}]] collects the three projects’ location searches and reviewed prose-only leads, with a combined Obsidian block for existing Japan/Korea orientation pins. China and unresolved places remain listed for coordinate checking. It does not merge itineraries or update ChatGPT Maps automatically.\n'
 (s/name).write_text(old+addition)
 item(name,hashlib.sha256(raw).hexdigest())
(b/'vault-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(dict(counts),'prose-only additions',len(added),'orientation pins',len(pins),'staged files',len(manifest))
