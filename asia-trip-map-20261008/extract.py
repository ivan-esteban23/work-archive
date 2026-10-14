from pathlib import Path
from urllib.parse import urlparse,parse_qs
import re,json,csv,collections

vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
out=Path(__file__).resolve().parent
records={}
for country in ['China','Japan','Korea']:
 for path in sorted(vault.glob(country+'*.md')):
  text=path.read_text()
  for match in re.finditer(r'https://(?:www\.google\.com/maps/search/|uri\.amap\.com/search)[^\s)\]>]+',text):
   url=match.group(0)
   fields=parse_qs(urlparse(url).query)
   query=(fields.get('query') or fields.get('keyword') or [''])[0]
   city=(fields.get('city') or [''])[0]
   if not query: continue
   key=(country,query.casefold().strip(),city)
   line=text[text.rfind('\n',0,match.start())+1:text.find('\n',match.end()) if '\n' in text[match.end():] else len(text)]
   r=records.setdefault(key,{'country':country,'search_text':query,'city_scope':city,'map_search_url':url,'coordinate_status':'Search only; exact place/branch/entrance not resolved','source_notes':[],'context_lines':[]})
   if path.name not in r['source_notes']: r['source_notes'].append(path.name)
   if line not in r['context_lines']: r['context_lines'].append(line)
data=list(records.values())
(out/'All destination searches.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
with (out/'All destination searches.csv').open('w',encoding='utf-8-sig',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['country','search_text','city_scope','map_search_url','coordinate_status','source_notes'])
 writer.writeheader()
 for r in data: writer.writerow({k:'; '.join(r[k]) if isinstance(r[k],list) else r[k] for k in writer.fieldnames})
pins=[]
for country in ['Japan','Korea']:
 path=vault/(('Japan 2027' if country=='Japan' else 'Korea 2026')+' — Map View.md')
 for m in re.finditer(r'\[([^\]]+)\]\(geo:([-\d.]+),([-\d.]+)\)([^\n]*)',path.read_text()):
  pins.append({'country':country,'name':m[1],'latitude':float(m[2]),'longitude':float(m[3]),'tags':m[4].strip(),'source_note':path.name,'status':'Inherited orientation coordinate; entrance not reverified'})
(out/'Existing orientation pins.json').write_text(json.dumps(pins,ensure_ascii=False,indent=2))
prompt='''Use the attached destination-search CSV as the source inventory for my China, Japan, and Korea travel research. Please display the listed places using your native map view if this chat supports it.

Keep countries separate in clearly labeled views. Work in manageable batches by country and city so no entries are silently omitted. Retain optional destinations as research candidates, not confirmed itinerary stops. The CSV includes source note names; keep a count of mapped, unresolved, and pending entries.

These are search queries, not verified place IDs. Resolve the exact place and branch before pinning. Flag ambiguous queries, broad areas, and coordinate conflicts rather than invent locations. Deduplicate only when two entries refer to the same place; preserve genuinely different branches. Some queries include native-language names. Use Amap searches for China navigation; do not assume coordinates from Amap and another map system are interchangeable.

Existing orientation pins are inherited from the notes and are not verified entrance locations. No bookings or travel dates are confirmed by this inventory. If native maps cannot accept this list or preserve all pins, explain the limitation and give me a batch-by-batch place list with navigation links.

Begin with an inventory summary, then the China locations grouped by city.'''
(out/'ChatGPT Maps prompt.txt').write_text(prompt)
counts=collections.Counter(r['country'] for r in data)
(out/'README.md').write_text('# Combined trip location inventory\n\nExtracted from live Obsidian travel notes on 8 October 2026.\n\n'+str(dict(counts))+' unique search text/city combinations; '+str(len(pins))+' inherited orientation coordinates.\n\nThis is a source inventory, not a completed map. Similar searches may refer to the same place. Places named only in prose without map searches are not included, so this does not claim exhaustive coverage of every named destination. Source/context lines are retained in JSON for review. Optional ideas remain optional; no cross-country itinerary is inferred.\n\nAttach the CSV to a chat with map support and use ChatGPT Maps prompt.txt. Native rendering, importing, persistent saved maps, and cross-device availability have not been tested.\n')
assert all(r['source_notes'] for r in data)
assert all(-90<=p['latitude']<=90 and -180<=p['longitude']<=180 for p in pins)
print(dict(counts),'orientation pins',len(pins))
