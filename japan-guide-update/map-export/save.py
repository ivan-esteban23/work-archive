from pathlib import Path
import csv,json,re,xml.etree.ElementTree as E,urllib.parse,shutil
v=Path('/home/ivanaguilera/Documents/Obsidian Vault');out=v/'Attachments/Japan 2027 Maps';out.mkdir(parents=True,exist_ok=True)
index=v/'Japan 2027 — Maps.md';entries=[];seen=set()
for name,url in re.findall(r'^- \[([^\]]+)\]\((https://www.google.com/maps/[^\s)]+)\)',index.read_text(),re.M):
 query=urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get('query',[''])[0]
 if not query or query in seen:continue
 seen.add(query);entries.append({'Name':name,'Place query':query,'Google Maps URL':url,'Status':'Search query; confirm exact branch and entrance'})
with (out/'Japan 2027 — All places.csv').open('w',newline='',encoding='utf-8-sig') as f:
 writer=csv.DictWriter(f,fieldnames=['Name','Place query','Google Maps URL','Status']);writer.writeheader();writer.writerows(entries)
geo=(v/'Japan 2027 — Map View.md').read_text();pins=[]
pattern=r'^- \[([^\]]+)\]\(geo:([-0-9.]+),([-0-9.]+)\) tag:japan2027 tag:([a-z]+) tag:([a-z]+)\n  \[Google Maps\]\(([^)]+)\) · \[Coordinate source\]\(([^)]+)\)'
for name,lat,lng,city,kind,maps,source in re.findall(pattern,geo,re.M):pins.append(dict(name=name,lat=float(lat),lng=float(lng),city=city,kind=kind,maps=maps,source=source))
assert len(pins)==11
ns='http://www.opengis.net/kml/2.2';E.register_namespace('',ns)
def el(parent,name,text=None):
 child=E.SubElement(parent,'{'+ns+'}'+name)
 if text is not None:child.text=text
 return child
root=E.Element('{'+ns+'}kml');doc=el(root,'Document');el(doc,'name','Japan 2027 — 11 sourced starter pins')
for p in pins:
 mark=el(doc,'Placemark');el(mark,'name',p['name']);el(mark,'description',f"{p['city'].title()} / {p['kind']}\nSite coordinate; verify the entrance separately.\nGoogle Maps: {p['maps']}\nCoordinate record: {p['source']}");point=el(mark,'Point');el(point,'coordinates',f"{p['lng']},{p['lat']},0")
E.ElementTree(root).write(out/'Japan 2027 — Starter pins.kml',encoding='utf-8',xml_declaration=True)
assert len(E.parse(out/'Japan 2027 — Starter pins.kml').findall('.//{'+ns+'}Placemark'))==11
note=v/'Japan 2027 — Saved Maps.md'
text=f'''# 🗺️ Japan 2027 — Saved map files and offline setup

[[Japan 2027 — Start Here|← Dashboard]] · [[Japan 2027 — Maps|All Google Maps links]] · [[Japan 2027 — Map View|Interactive starter maps]]

**Saved 6 October 2026.** These files contain your guide’s places and pins. They are not downloaded Google Maps offline areas. No Google account import or iPhone download has been performed.

## Your saved map files

- [[Attachments/Japan 2027 Maps/Japan 2027 — All places.csv|All places CSV]] — {len(entries)} distinct search queries, including shops, cafés, transport anchors, and sightseeing ideas. Some rows are chain searches or alternate queries for the same place. They are not {len(entries)} independently verified venues.
- [[Attachments/Japan 2027 Maps/Japan 2027 — Starter pins.kml|Starter pins KML]] — 11 sourced location records for Tokyo, Kyoto, and optional Uji. Coordinates identify sites, not confirmed entrances or station platforms.

## Download Google Maps areas on your iPhone

On Wi-Fi, open **Google Maps → profile picture → Offline maps → Select your own map**. Adjust the rectangle and tap **Download**. Repeat for each area below, where downloads are available. Downloaded areas stay inside the Google Maps app.

- [ ] **Tokyo:** include your booked hotel, Asakusa/Ueno, Ginza/Tokyo Station, Shinjuku, Shibuya, and the western neighborhoods you choose to visit. Download overlapping areas if one selection cannot include everything.
- [ ] **Airport coverage:** include Haneda or Narita and the surrounding area after confirming your flights. Narita is far from central Tokyo; check its coverage separately.
- [ ] **Kyoto:** include your booked hotel, Kyoto Station, central/eastern Kyoto, and Arashiyama if selected. Add Ohara separately if you choose that outing.
- [ ] **Optional excursion:** add Uji, Kamakura, Nara, or Osaka only for the destinations you actually select.
- [ ] Turn on **Auto-update offline maps** in Offline maps settings. Recheck downloads and expiry dates during the week before your March 2027 departure.
- [ ] Test downloaded coverage in airplane mode and save screenshots of important station exits and the airport/hotel journeys while online.

**Offline limitation:** Google Maps does not provide walking, public-transport, or cycling directions offline. Keep your eSIM available for transit planning and store the important route details separately. Offline areas are separate from saved-place lists and these CSV/KML exports.

[Google’s official iPhone download instructions](https://support.google.com/maps/answer/6291838?co=GENIE.Platform%3DiOS&hl=en)

## Import the files into a custom Google My Maps map

On your computer, sign in to [Google My Maps](https://www.google.com/mymaps), create a map called **Japan 2027**, then **Add layer → Import**.

1. Import the KML for the 11 sourced pins.
2. In a separate layer, import the CSV. Select **Place query** as the location column and **Name** as the title column.
3. Review Google’s matches and correct ambiguous branches, broad chain searches, and duplicate destinations before relying on the result.

Importing places into My Maps does not download an offline Google Maps area. [Google’s import instructions](https://support.google.com/mymaps/answer/3024836?hl=en)
'''
note.write_text(text)
backup=Path('/home/ivanaguilera/Work/japan-guide-update/map-export/backup');backup.mkdir(exist_ok=True)
for name in ['Japan 2027 — Start Here.md','Japan 2027 — Maps.md']:
 p=v/name;s=p.read_text();shutil.copy2(p,backup/name)
 link='**Saved map files and offline setup:** [[Japan 2027 — Saved Maps]]'
 if link not in s:
  pos=s.index('\n')+1;s=s[:pos]+'\n'+link+'\n'+s[pos:];p.write_text(s)
print(json.dumps({'place_queries':len(entries),'sourced_pins':len(pins),'saved_directory':str(out),'guide':str(note)},indent=2))
