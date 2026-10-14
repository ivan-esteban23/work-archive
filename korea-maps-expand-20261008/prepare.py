from pathlib import Path
from urllib.parse import urlencode,parse_qs,urlparse
import json,re,csv,hashlib,collections

b=Path(__file__).resolve().parent;v=Path('/home/ivanaguilera/Documents/Obsidian Vault');s=b/'staged';s.mkdir(exist_ok=True)
manifest=[]
def save(name,new):
 p=v/name;raw=p.read_bytes();backup=b/'backup'/name;backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(raw)
 t=s/name;t.parent.mkdir(parents=True,exist_ok=True);t.write_text(new,encoding='utf-8')
 manifest.append({'relative':name,'expected':hashlib.sha256(raw).hexdigest()})
def search(q):return 'https://www.google.com/maps/search/?'+urlencode({'api':'1','query':q})
groups={
 'Seoul — more sights, records, cafés and browsing':[
 ('Changdeokgung','창덕궁 서울','Optional palace; existing orientation pin'),
 ('Bukchon Hanok Village','북촌한옥마을 서울','Neighborhood; observe posted visitor restrictions'),
 ('Gwangjang Market','광장시장 서울','Food browsing; individual vendors not selected'),
 ('N Seoul Tower','남산서울타워','Optional viewpoint; admission/weather needs checking'),
 ('Inwangsan','인왕산 서울','Optional hike; select a suitable trail'),
 ('Euljiro','을지로 서울','Neighborhood browsing, not one shop'),
 ('Cheonggyecheon','청계천 서울','Stream walk; select the actual access point'),
 ('Dongdaemun Design Plaza','동대문디자인플라자 서울','Optional architecture/design outing; exhibitions separately checked'),
 ('National Museum of Korea','국립중앙박물관 서울','Optional museum alternative; visit details still to check'),
 ('Mangwon Station','망원역 서울','Transport anchor for the west-Seoul block'),
 ('House of Vinyl — Mangwon branch','House of Vinyl 23 Heeujeong-ro 16-gil Mapo Seoul','Researched listening café; 1F at the supplied address; [[Korea 2026 — Places Shortlist]]'),
 ('Clique Records','Clique Records 8 Eulji-ro 12-gil Jung-gu Seoul','Researched record shop; room 301; [[Korea 2026 — Places Shortlist]]'),
 ('Dongmyo Flea Market area','동묘벼룩시장 서울','Researched secondhand district; stalls vary'),
 ('Ohsaegyehyang','오세계향 서울 인사동12길 14-5','Optional researched restaurant; unrestricted diet remains current'),
 ('Hongdae browsing area','홍대 서울','Neighborhood search, not a selected shop'),
 ('Yeonnam-dong','연남동 서울','West-Seoul browsing area'),
 ],
 'Gyeongju — museum and researched breaks':[
 ('Gyeongju National Museum','국립경주박물관','Optional historic-center museum; do not crowd a transfer day'),
 ('Bitgguri','빛꾸리 경주 손효자길 16-1','Researched tea-break candidate; no tea class established'),
 ('YELLA','YELLA 경주 태종로791번길 17','Meal candidate from destination guide; operation/hours need recheck'),
 ('El Rato Gyeongju','El Rato 경주 포석로 1045','Meal alternative from destination guide; operation/hours need recheck'),
 ],
 'Busan — food, café districts and eastern alternatives':[
 ('Jagalchi Market','자갈치시장 부산','Food/market option; existing orientation pin'),
 ('Haeundae Beach','해운대해수욕장 부산','Eastern-day alternative, not another default cross-city stop'),
 ('Jeonpo Café Street','전포카페거리 부산 동천로 92','Researched district; choose the café on arrival'),
 ('Seomyeon Station','서면역 부산','Transport and browsing anchor near the Jeonpo district'),
 ('Vegenarang — conditional address','베지나랑 부산 광안해변로370번길 9-32','Address based on weaker secondary evidence; recheck branch/floor before a special trip'),
 ('Busan Museum of Contemporary Art','부산현대미술관','Optional art outing; no exhibition or Biennale dates assumed'),
 ]}
mapsname='Korea 2026 — Maps.md';old=(v/mapsname).read_text()
intro='\n\n## Expanded directory · 8 October 2026\n\nAdded missing researched stops and optional landmarks. Existing links above remain. These are name/address searches, not saved venue IDs or confirmed entrances. Source context: [[Korea 2026 — Solo Plan]], [[Korea 2026 — Places Shortlist]] and [[Korea 2026 — Map View]]. Recheck business operation and visit conditions for your chosen dates. Use Korean names in your preferred local navigator if needed.\n'
addition=intro
for heading,rows in groups.items():
 addition+='\n### '+heading+'\n\n'
 for name,q,desc in rows: addition+=f'- [{name}]({search(q)}) — {q}. {desc}.\n'
addition+='\nFresh business checks: [House of Vinyl city listing](https://english.visitseoul.net/restaurants/House%20of%20Vinyl%20Mangwon%20Branch/ENPcq5rwf), edited 4 September 2026, and [Clique Records operator address](https://cliquerecords.kr/about), reopened 8 October 2026. Other researched business addresses retain the evidence and limits in [[Korea 2026 — Places Shortlist]]. Unresolved names in [[Korea 2026 — Cafés and Shops]] remain an inbox rather than verified venues.\n'
save(mapsname,old+addition)
newpins=[
 ('Seoullo 7017',37.556978,126.974766,'seoul','nature','Seoullo_7017','Linear-park orientation point; choose stairs/access separately'),
 ('Cheonggyecheon — stream orientation point',37.57000,127.00639,'seoul','nature','Cheonggyecheon','One point along the stream, not its western entrance'),
 ('Dongdaemun Design Plaza',37+34/60+0.84/3600,127+33.84/3600,'seoul','sightseeing',None,'Complex orientation point; exact building entrance not surveyed'),
 ('National Museum of Korea',37.5239,126.9803,'seoul','museum','National_Museum_of_Korea','Optional museum; building orientation, not checked entrance'),
 ('Hongik University Station — not the campus',37.55667,126.92361,'seoul','transport','Hongik_University_station','Station anchor; choose the required line and exit'),
 ('Mangwon Station',37.55611,126.91000,'seoul','transport','Mangwon_station','Station anchor; choose the required exit'),
 ('Dongmyo shrine — flea-market area anchor',37.5731,127.0182,'seoul','shopping','Dongmyo','This pin is the shrine, not a particular market stall'),
 ('Gyeongju National Museum',35.8289833,129.228361,'gyeongju','museum','Gyeongju_National_Museum','Optional museum; orientation rather than surveyed entrance'),
 ('Seomyeon Station',35.15778,129.05917,'busan','transport','Seomyeon_station','Station anchor; Jeonpo cafés are a separate walk/location'),
]
viewname='Korea 2026 — Map View.md';view=(v/viewname).read_text()
assert 'locations:' not in view.split('---',2)[1]
view=view.replace('---\n','---\nlocations:\n',1)
view+='\n\n## Additional sourced orientation pins · 8 October 2026\n\nNine coordinate records checked against the linked Wikimedia pages. These are orientation points, not independently surveyed entrances. Existing inherited pins above retain their earlier caveats. Shop/café searches are listed separately below rather than given guessed coordinates. New museums and DDP are optional research alternatives, not additions to the chosen itinerary.\n\n'
for name,lat,lon,city,tag,page,desc in newpins:
 url='https://en.wikipedia.org/wiki/'+page if page else 'https://www.wikidata.org/wiki/Q5295847'
 view+=f'- [{name}](geo:{lat:.7f},{lon:.7f}) tag:korea2026 tag:{city} tag:{tag}\n  {desc}. [Coordinate record]({url}) · [Location search]({search(name+" South Korea")})\n\n'
view+='## Cafés and shops — address searches pending coordinates\n\nUse [[Korea 2026 — Maps#Expanded directory · 8 October 2026|the expanded Maps directory]] for House of Vinyl, Clique Records, Dongmyo, Bitgguri, YELLA, El Rato, Jeonpo Café Street, and the conditional Vegenarang address. A station or district marker is not a substitute for the café/shop entrance.\n'
save(viewname,view)

# Refresh the combined inventory directly from the expanded source notes.
att='Attachments/Asia Trip Maps/'
data=json.loads((v/(att+'All destination searches.json')).read_text())
for text,note in [(old+addition,mapsname),(view,viewname)]:
 for m in re.finditer(r'https://www\.google\.com/maps/search/[^\s)\]>]+',text):
  url=m[0];q=parse_qs(urlparse(url).query).get('query',[''])[0]
  if not q:continue
  found=next((r for r in data if r['country']=='Korea' and r['search_text'].casefold()==q.casefold()),None)
  if found:
   if note not in found['source_notes']:found['source_notes'].append(note)
  else:data.append({'country':'Korea','search_text':q,'city_scope':'','map_search_url':url,'coordinate_status':'Search only; exact branch/entrance not resolved','source_notes':[note],'context_lines':[]})
pins=json.loads((v/(att+'Existing orientation pins.json')).read_text())
for name,lat,lon,city,tag,page,desc in newpins:
 pins.append({'country':'Korea','name':name,'latitude':lat,'longitude':lon,'tags':f'tag:korea2026 tag:{city} tag:{tag}','source_note':viewname,'status':desc+'; record checked 2026-10-08','coordinate_source':'https://en.wikipedia.org/wiki/'+page if page else 'https://www.wikidata.org/wiki/Q5295847'})
save(att+'All destination searches.json',json.dumps(data,ensure_ascii=False,indent=2))
save(att+'Existing orientation pins.json',json.dumps(pins,ensure_ascii=False,indent=2))
import io
f=io.StringIO();fields=['country','search_text','native_search_text','city_scope','map_search_url','coordinate_status','planning_status','source_notes']
w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
for r in data:w.writerow({k:'; '.join(r[k]) if isinstance(r.get(k),list) else r.get(k,'') for k in fields})
save(att+'All destination searches.csv','\ufeff'+f.getvalue())
combinedname='Asia Trips — Combined Map and Destination Inventory.md';combined=(v/combinedname).read_text()
count=sum(r['country']=='Korea' for r in data)
combined=re.sub(r'\| Korea \| \d+ \|',f'| Korea | {count} |',combined)
combined=combined.replace('**41 orientation pins**','**50 orientation pins**')
combined+='\n\n## Korea expansion · 8 October 2026\n\n[[Korea 2026 — Maps]] now includes 26 additional search entries and [[Korea 2026 — Map View]] has nine additional sourced orientation pins (39 Korea pins total). The CSV/JSON inventories were refreshed. Counts include aliases, broad areas, and unresolved queries; they are not a count of distinct verified venues. Rendering and exact entrances remain untested.\n'
save(combinedname,combined)
for n in ['Korea 2026 — Start Here.md','Korea 2026 — Session Recap 2026-10-08.md']:
 t=(v/n).read_text()
 t+='\n\n## Expanded map directory · 8 October 2026\n\nAdded 26 search entries for missing sights, transport anchors and researched café/shop/meal candidates in [[Korea 2026 — Maps]]. Added nine sourced orientation pins to [[Korea 2026 — Map View]], for 39 total. Shop entrances remain pending coordinate checks. Refreshed [[Asia Trips — Combined Map and Destination Inventory]] and its CSV/JSON attachments; no native ChatGPT map upload or live Obsidian rendering was performed.\n'
 save(n,t)
assert sum(len(r) for r in groups.values())==26
assert len(re.findall(r'\]\(geo:',view))==39
(b/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Prepared 26 added search entries, nine new orientation pins; Korea inventory rows:',count,'updated files:',len(manifest))
