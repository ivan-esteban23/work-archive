from pathlib import Path
from urllib.parse import urlencode,urlparse,parse_qs,unquote
from shutil import copy2
import re,json
v=Path('/home/ivanaguilera/Documents/Obsidian Vault'); work=Path('/home/ivanaguilera/Work/japan-guide-update/maps-audit')
work.mkdir(exist_ok=True)
files=sorted(v.glob('Japan*.md'))
texts={p.name:p.read_text() for p in files}
before={name:len(re.findall(r'https://www\.google\.com/maps/[^\s)]+',s)) for name,s in texts.items()}
def ml(label,query):return '['+label+'](https://www.google.com/maps/search/?'+urlencode({'api':1,'query':query})+')'
def add_after(name,needle,extra):
 s=texts[name];assert needle in s,(name,needle)
 texts[name]=s.replace(needle,needle+'\n\n'+extra,1)
main='Japan Travel Guide 2027.md'; gems='Japan 2027 — Hidden Gems.md'; shops='Japan 2027 — Shops and Cafés.md'
add_after(main,'### Existing quieter alternatives', '**Maps:** '+ml('Yanaka Ginza','Yanaka Ginza Tokyo Japan')+' · '+ml('Nezu neighborhood','Nezu Tokyo Japan')+' · '+ml('Ohara village','Ohara Kyoto Japan'))
add_after(main,'### 🎟️ Optional attractions requiring a separate decision','**Maps:** '+ml('Ghibli Museum','Ghibli Museum Mitaka Tokyo Japan')+' · '+ml('Universal Studios Japan','Universal Studios Japan Osaka')+' · '+ml('SUPER NINTENDO WORLD','SUPER NINTENDO WORLD Universal Studios Japan Osaka'))
needle='[Official tea room](https://www.byodoin.or.jp/en/touka/)'
add_after(main,needle,ml('Maps: Sabo TOKA / Byodoin tea room','Sabo TOKA Byodoin Uji Kyoto Japan')+' · '+ml('Maps: Uji River','Uji River Uji Kyoto Japan'))
add_after(main,'### Airport transfer decision','**Airport Maps:** '+ml('Haneda (HND)','Haneda Airport Tokyo Japan')+' · '+ml('Narita (NRT)','Narita International Airport Japan')+' · '+ml('Kansai (KIX), optional departure','Kansai International Airport Osaka Japan')+' · '+ml('Santiago (SCL)','Arturo Merino Benitez International Airport Santiago Chile')+'\n\nSelect the terminal shown on your ticket; airport links do not identify an airline’s check-in counter.')
add_after(main,'### 🍜 Ramen alternatives and affordable sushi','**Nearby branch searches — branches still undecided:**\n\n| Chain | Tokyo search | Kyoto search |\n| --- | --- | --- |\n'+'\n'.join('| '+chain+' | '+ml('Tokyo branches',chain+' Tokyo Japan')+' | '+ml('Kyoto branches',chain+' Kyoto Japan')+' |' for chain in ['Hidakaya','Ippudo','Tenkaippin','Ichiran','Sushiro','Kura Sushi'])+'\n\nThese search for branches; they do not confirm a branch exists in every area, select a restaurant, or verify menus. Choose near the day’s actual location.')
add_after(main,'### 🍵 Choosing your matcha experience', '**Doutor nearby searches:** '+ml('Tokyo','Doutor Coffee Tokyo Japan')+' · '+ml('Kyoto','Doutor Coffee Kyoto Japan')+' — chain comparison only; no branch selected.')
add_after(gems,'## ☕ Tokyo — Kagurazaka backstreets','**Individual Maps:** '+ml('Hyogo Yokocho','Hyogo Yokocho Kagurazaka Tokyo')+' · '+ml('Zenkokuji Temple','Zenkokuji Temple Kagurazaka Tokyo')+' · '+ml('Akagi-jinja Shrine','Akagi Shrine Kagurazaka Tokyo'))
add_after(gems,'## 🗿 Kyoto — Otagi Nenbutsuji and Saga-Toriimoto','**Additional Maps:** '+ml('Saga-Toriimoto preserved street','Saga Toriimoto Preserved Street Kyoto Japan')+' · '+ml('Adashino Nenbutsuji, reference only','Adashino Nenbutsuji Kyoto Japan')+' — the latter is the differently named temple mentioned below, not an added itinerary stop.')
add_after(gems,'### 🌳 Kyoto — Shimogamo, Tadasu no Mori, and the Demachi riverbank','**Forest Maps:** '+ml('Tadasu no Mori','Tadasu no Mori Shimogamo Kyoto Japan'))
add_after(gems,'### 🌿 Kyoto — Hōnen-in, the small detour near Philosopher’s Path','**Reference Maps:** '+ml('Ginkaku-ji','Ginkakuji Kyoto Japan')+' — an optional comparison mentioned below, not an extra required temple.')
# Explicit neighborhood anchors and station searches fill remaining transport/district references.
areas=[('Tokyo','Tokyo Japan'),('Kyoto','Kyoto Japan'),('Nara','Nara Japan'),('Osaka','Osaka Japan'),('Ginza','Ginza Tokyo Japan'),('Shibuya','Shibuya Tokyo Japan'),('Shinjuku','Shinjuku Tokyo Japan'),('Asakusa','Asakusa Tokyo Japan'),('Ueno','Ueno Tokyo Japan'),('Akihabara','Akihabara Tokyo Japan'),('Ikebukuro','Ikebukuro Tokyo Japan'),('Kamakura','Kamakura Kanagawa Japan'),('Koenji','Koenji Tokyo Japan'),('Kichijoji','Kichijoji Musashino Tokyo Japan'),('Daikanyama','Daikanyama Tokyo Japan'),('Nakameguro','Nakameguro Tokyo Japan'),('Kuramae','Kuramae Tokyo Japan'),('Kiyosumi-Shirakawa','Kiyosumi Shirakawa Tokyo Japan'),('Kagurazaka','Kagurazaka Tokyo Japan'),('Shibamata','Shibamata Tokyo Japan'),('Gion','Gion Kyoto Japan'),('Ebisu','Ebisu Tokyo Japan'),('Saigoyama Park','Saigoyama Park Tokyo Japan')]
stations=[('Tokyo Station','Tokyo Station Japan'),('Shinagawa Station','Shinagawa Station Tokyo Japan'),('Kyoto Station','Kyoto Station Japan'),('Shinjuku Station','Shinjuku Station Tokyo Japan'),('Shibuya Station','Shibuya Station Tokyo Japan'),('Ueno Station','Ueno Station Tokyo Japan'),('Asakusa Station','Asakusa Station Tokyo Japan'),('Ginza Station','Ginza Station Tokyo Japan'),('Higashi-ginza Station','Higashi Ginza Station Tokyo Japan'),('Shintomicho Station','Shintomicho Station Tokyo Japan'),('Shimokitazawa Station','Shimokitazawa Station Tokyo Japan'),('Setagaya-Daita Station','Setagaya Daita Station Tokyo Japan'),('Kichijoji Station','Kichijoji Station Tokyo Japan'),('Koenji Station','Koenji Station Tokyo Japan'),('Nakano Station','Nakano Station Tokyo Japan'),('Daikanyama Station','Daikanyama Station Tokyo Japan'),('Ebisu Station','Ebisu Station Tokyo Japan'),('Nakameguro Station','Nakameguro Station Tokyo Japan'),('Kuramae Station','Kuramae Station Tokyo Japan'),('Iidabashi Station','Iidabashi Station Tokyo Japan'),('Kiyosumi-Shirakawa Station','Kiyosumi Shirakawa Station Tokyo Japan'),('Shibamata Station','Shibamata Station Tokyo Japan'),('Chofu Station','Chofu Station Tokyo Japan'),('Tsutsujigaoka Station','Tsutsujigaoka Station Chofu Tokyo Japan'),('Kyoto Shiyakusho-mae Station','Kyoto Shiyakusho mae Station Japan'),('Karasuma Oike Station','Karasuma Oike Station Kyoto Japan'),('Kyoto-Kawaramachi Station','Kyoto Kawaramachi Station Japan'),('Gion-Shijo Station','Gion Shijo Station Kyoto Japan'),('JR Saga-Arashiyama Station','Saga Arashiyama Station Kyoto Japan'),('Demachiyanagi Station','Demachiyanagi Station Kyoto Japan')]
# Prefer address-qualified queries for moved/combined stores.
fixes={
'Disk+Union+Ikebukuro+Tokyo+Japan':'Disk+Union+Ikebukuro+2-27-8+Minamiikebukuro+Tokyo',
'Disk+Union+Kichijoji+%2B+Kichijoji+Movie+Store+Tokyo+Japan':'Disk+Union+Kichijoji+PARCO+1-5-1+Kichijoji+Honmachi',
'Disk+Union+Cinema-kan+%2F+Book+Union+Shinjuku+Tokyo+Japan':'Disk+Union+Cinema+Book+Union+3-34-1+Shinjuku+Tokyo'}
for a,b in fixes.items():texts[shops]=texts[shops].replace('query='+a,'query='+b)
# All existing named Maps search destinations, grouped by the note where first found.
seen=set();groups=[]
for name in [main,gems,shops]:
 entries=[]
 for url in re.findall(r'https://www\.google\.com/maps/search/\?[^\s)]+',texts[name]):
  q=parse_qs(urlparse(url).query)['query'][0];key=q.casefold()
  if key in seen:continue
  seen.add(key);entries.append((q,url))
 groups.append((name.removesuffix('.md'),entries))
idx='''# 📍 Japan 2027 — Google Maps index

[[Japan 2027 — Start Here|← Dashboard]] · [[Japan Travel Guide 2027|Full guide]] · [[Japan 2027 — Shops and Cafés|Shops and cafés]] · [[Japan 2027 — Hidden Gems|Hidden gems]]

**Guide audit: 6 October 2026.** This index collects Maps search destinations across the main guide and companion destination notes, plus transport and neighborhood anchors. Repeated places may appear under different branch/address queries. Search links are generated navigation aids, not independently verified place IDs, entrances, hours, or 2027 service guarantees. Choose the exact branch, then use your actual starting point for directions. Chain searches show candidates, not selected restaurants.

**Hotel and booking locations:** no hotels or specific departure terminals are selected. Add the booked address and terminal below after confirmation; no invented hotel pin is supplied.

- First Tokyo hotel / entrance: **TBD**
- Kyoto hotel / entrance: **TBD**
- Final Tokyo hotel / entrance: **TBD**
- Arrival airport terminal: **TBD**
- Departure airport terminal: **TBD**

## 🚉 Transport anchors

'''
idx+='\n'.join('- '+ml(a,q) for a,q in stations)+'\n\n## 🗺️ Neighborhood and area anchors\n\n'
idx+='\n'.join('- '+ml(a,q) for a,q in areas)+'\n\n'
for heading,entries in groups:
 idx+='## '+heading+' — destination searches\n\n'
 idx+='\n'.join('- ['+q.replace(']','')+']('+url+')' for q,url in entries)+'\n\n'
idx+='''## 🧾 Add an exact booking location

- Venue / hotel / branch: …
- Full address: …
- Google Maps link: …
- Required entrance / station exit / floor: …
- Date last checked against the venue’s official information: …

'''
texts['Japan 2027 — Maps.md']=idx
# Put one clear navigation link in every existing companion note, without assigning template destinations.
for name in list(texts):
 if name=='Japan 2027 — Maps.md':continue
 lines=texts[name].splitlines(keepends=True)
 lines.insert(2,'**Maps:** [[Japan 2027 — Maps|📍 All destination, shop, café, and transport searches]]\n\n')
 texts[name]=''.join(lines)
# Booking and daily template fields stay pending until actual venues are chosen.
n='Japan 2027 — Bookings.md';texts[n]=texts[n].replace('- **Address / station / terminal:**','- **Address / station / terminal:**\n- **Google Maps link / actual entrance:**',1)
n='Japan 2027 — Today.md';texts[n]=texts[n].replace('- **Rest stop:** …','- **Rest stop:** …\n- **Food / café Maps links:** …',1)
n='Japan 2027 — Travel Essentials.md';texts[n]=texts[n].replace('| First hotel / address in Japanese | TBD |','| First hotel / address in Japanese | TBD |\n| Hotel entrance Google Maps link | TBD — fill after booking |',1)
# Validate URL syntax and required Google Maps API parameters for every note.
count=0
for name,s in texts.items():
 for url in re.findall(r'https://www\.google\.com/maps/[^\s)]+',s):
  parsed=urlparse(url);params=parse_qs(parsed.query)
  assert parsed.netloc=='www.google.com' and params.get('api')==['1'],(name,url)
  if parsed.path=='/maps/search/':assert params.get('query') and params['query'][0].strip(),(name,url)
  elif parsed.path=='/maps/dir/':assert params.get('origin') and params.get('destination'),(name,url)
  else:raise AssertionError((name,url))
  count+=1
# Validate wikilink file targets, including the new index.
for name,s in texts.items():
 for dest in re.findall(r'\[\[([^\]]+)\]\]',s):
  target=dest.split('|')[0].split('#')[0]
  if target:assert target+'.md' in texts or (v/(target+'.md')).exists(),(name,target)
report={'existing_notes_audited':len(files),'maps_links_before':sum(before.values()),'maps_links_after':count,'index_search_entries':sum(len(e) for _,e in groups)+len(stations)+len(areas),'changed_existing_notes':[n for n in texts if n in before],'new_note':'Japan 2027 — Maps.md','validation':'Maps URL syntax/API parameters and wikilink file targets passed; search results/place pins not independently verified.'}
(work/'audit-report.json').write_text(json.dumps(report,indent=2))
for name,s in texts.items():
 p=v/name
 if p.exists():copy2(p,work/name)
 p.write_text(s)
print(json.dumps(report,indent=2))
