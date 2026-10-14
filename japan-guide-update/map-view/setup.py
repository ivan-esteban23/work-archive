from pathlib import Path
import json,shutil,re,hashlib,urllib.parse
stage=Path('/home/ivanaguilera/Work/japan-guide-update/map-view')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
backup=stage/'backup';backup.mkdir(exist_ok=True)
manifest=json.loads((stage/'manifest.json').read_text());assert manifest['id']=='obsidian-map-view'
plugin=vault/'.obsidian/plugins'/manifest['id'];plugin.mkdir(parents=True,exist_ok=True)
for name in ('manifest.json','main.js','styles.css'):
 dest=plugin/name
 if dest.exists():shutil.copy2(dest,backup/('plugin-'+name))
 shutil.copy2(stage/name,dest)
 assert hashlib.sha256(dest.read_bytes()).digest()==hashlib.sha256((stage/name).read_bytes()).digest()
config=vault/'.obsidian/community-plugins.json'
if config.exists():shutil.copy2(config,backup/config.name)
enabled=json.loads(config.read_text()) if config.exists() else []
assert isinstance(enabled,list)
if manifest['id'] not in enabled:enabled.append(manifest['id'])
config.write_text(json.dumps(enabled,indent=2)+'\n')
entities=json.loads((stage/'entities.json').read_text())['entities']
items=[('Q615183','Sensō-ji','tokyo','sightseeing'),('Q776863','Shinjuku Gyoen','tokyo','sightseeing'),('Q746216','Ueno Park','tokyo','sightseeing'),('Q283196','Tokyo Station','tokyo','transport'),('Q428811','Shibuya Station','tokyo','transport'),('Q221716','Kiyomizu-dera','kyoto','sightseeing'),('Q714828','Fushimi Inari-taisha','kyoto','sightseeing'),('Q692714','Yasaka Shrine','kyoto','sightseeing'),('Q1013399','Nijō Castle','kyoto','sightseeing'),('Q801046','Kyoto Station','kyoto','transport'),('Q61094','Byōdō-in — optional Uji excursion','uji','sightseeing')]
lines=['---','locations:','---','# 🗺️ Japan 2027 — Interactive maps','', '[[Japan 2027 — Start Here|← Dashboard]] · [[Japan 2027 — Maps|All Google Maps destinations]] · [[Japan Travel Guide 2027|Full guide]]','', '**Starter map · prepared 6 October 2026.** Eleven landmarks and stations from the guide, grouped into Tokyo and Kyoto/Uji. Pins use Wikidata location records; park, temple, and station coordinates identify the site, not a verified entrance or platform. Uji remains an optional excursion. Shops and cafés are in the complete Google Maps index and still need exact-branch coordinates before being pinned.','', '## Using the maps','', 'Open this note in **Reading view** to see the interactive maps. Click a pin to identify its place; use the Google Maps link below for walking or train directions. The **Open** control opens the full Map View, where you can adjust the query. Map tiles need internet unless downloaded in Map View beforehand.','', 'Suggested full-map queries: `tag:#japan2027`, `tag:#japan2027 AND tag:#tokyo`, or `tag:#japan2027 AND tag:#transport`.','']
for title,lat,lng,query in [('Tokyo',35.69,139.75,'tag:#japan2027 AND tag:#tokyo'),('Kyoto and optional Uji',35.0,135.77,'tag:#japan2027 AND (tag:#kyoto OR tag:#uji)')]:
 state=dict(name='Japan 2027 — '+title,mapZoom=12,centerLat=lat,centerLng=lng,query=query,chosenMapSource=0,autoFit=True,lock=False,showLinks=False,markerLabels='off',embeddedHeight=430)
 lines+=['## '+title,'','```mapview',json.dumps(state,indent=2),'```','']
lines+=['## Pin directory','','Each line is a Map View location with inline tags. Sources link to the coordinate record; navigation searches include the named destination.','']
for q,name,city,kind in items:
 e=entities[q];coords=[c for c in e['claims']['P625'] if c['rank']!='deprecated'];coord=coords[0]['mainsnak']['datavalue']['value'];lat,lng=coord['latitude'],coord['longitude']
 assert coord['globe'].endswith('/Q2') and 34<lat<36 and 135<lng<141
 maps='https://www.google.com/maps/search/?api=1&query='+urllib.parse.quote_plus(name.split(' —')[0]+' '+city+' Japan')
 lines += [f'- [{name}](geo:{lat:.6f},{lng:.6f}) tag:japan2027 tag:{city} tag:{kind}',f'  [Google Maps]({maps}) · [Coordinate source](https://www.wikidata.org/wiki/{q})','']
lines+=['## Add your next place','','For a shop or café, confirm its exact branch and coordinates first, then add a line in the same format:','','```text','[Place name](geo:LATITUDE,LONGITUDE) tag:japan2027 tag:tokyo tag:shopping','```','','Use `tag:cafe`, `tag:music`, or `tag:film` for your other interests. Replace both coordinate placeholders with verified numbers. Add hotel pins after booking the exact property.','','[Map View documentation](https://esm7.github.io/obsidian-map-view/) · [Location formats](https://esm7.github.io/obsidian-map-view/location-formats.html)','']
note=vault/'Japan 2027 — Map View.md'
if note.exists():shutil.copy2(note,backup/note.name)
note.write_text('\n'.join(lines))
for name in ['Japan 2027 — Start Here.md','Japan Travel Guide 2027.md','Japan 2027 — Maps.md']:
 p=vault/name;text=p.read_text();shutil.copy2(p,backup/name)
 link='**Interactive maps:** [[Japan 2027 — Map View|🗺️ Tokyo and Kyoto/Uji pins]]'
 if link not in text:
  pos=text.index('\n')+1;text=text[:pos]+'\n'+link+'\n'+text[pos:]
 p.write_text(text)
blocks=re.findall(r'```mapview\n(.*?)\n```',note.read_text(),re.S)
assert len(blocks)==2
for block in blocks:assert json.loads(block)['autoFit'] is True
assert sum(line.startswith('- [') and '](geo:' in line for line in note.read_text().splitlines())==11
print('Setup validated')
