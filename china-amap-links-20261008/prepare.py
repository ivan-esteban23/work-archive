from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
import hashlib,json,re
base=Path('/home/ivanaguilera/Work/china-amap-links-20261008')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
names=['China — Places and Experiences Shortlist.md','China — Preparation Before Choosing Dates.md','China — Start Here.md','China — Research and Sources 2026-10-08.md','China — Session Recap 2026-10-08.md']
manifest={}
for name in names:
    data=(vault/name).read_bytes()
    (base/'backup'/name).write_bytes(data)
    (base/'staged'/name).write_bytes(data)
    manifest[name]=hashlib.sha256(data).hexdigest()
(base/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False))
places={
'Palace Museum / 故宫博物院':('故宫博物院','北京'),
'Mutianyu Great Wall / 慕田峪长城':('慕田峪长城','北京'),
'Yangmeizhu Xiejie / 杨梅竹斜街':('杨梅竹斜街','北京'),
'798 Art District / 798艺术区':('798艺术区','北京'),
'Maliandao / 马连道':('马连道','北京'),
'Xi’an City Wall / 西安城墙':('西安城墙','西安'),
'Muslim Quarter / 回民街':('回民街','西安'),
'Terracotta Warriors / 秦始皇帝陵博物院':('秦始皇帝陵博物院 兵马俑','西安'),
'The Bund / 外滩':('外滩','上海'),
'M50 Creative Park / M50创意园':('M50创意园','上海'),
'Tianzifang / 田子坊':('田子坊','上海'),
'Xintiandi / 新天地':('新天地','上海'),
'Jia Jia Tang Bao':('佳家汤包 黄河路127号','上海'),
'Da Hu Chun':('大壶春 四川中路136号','上海'),
'O.P.S. CAFE, Taiyuan Road branch':('O.P.S. CAFE 太原路177弄1号','上海'),
'Manner Coffee, North Bund / Guoke Binjiang branch':('MANNER 太平路','上海'),
}
p=base/'staged'/names[0]
s=p.read_text()
lines=[]
found=set()
links=[]
for line in s.splitlines():
    if line.startswith('| Candidate / search text |') or line.startswith('| Place | Provider-listed location |'):
        line=line+' Amap link (iPhone / Android) |'
    elif line=='| --- | --- | --- |':
        line=line+' --- |'
    elif line.startswith('| '):
        label=line.split('|')[1].strip()
        if label in places:
            keyword,city=places[label]
            url='https://uri.amap.com/search?'+urlencode({'keyword':keyword,'city':city,'view':'list','src':'china_trip_guide','callnative':'1'})
            line=line+f' [Search in Amap]({url}) |'
            found.add(label)
            links.append((url,keyword,city))
    lines.append(line)
assert found==set(places),(found,set(places))
s='\n'.join(lines)+'\n'
intro='''## Open these places in Amap

**AMap Global:** [iPhone — App Store (Chile)](https://apps.apple.com/cl/app/amap-global/id461703208) · [Android — Google Play](https://play.google.com/store/apps/details?id=com.autonavi.minimap).

The same **Search in Amap** links below are intended for both phones. They use Amap’s documented mobile/web search format and request opening the installed app where supported. These are city-scoped searches, not verified pins or saved favorites. Tap a result, confirm the address/branch or visitor entrance, then save it inside Amap. [Official Amap link documentation](https://lbs.amap.com/api/uri-api/guide/search/search?type=spa), checked 8 October 2026.

If the link opens a browser or does not hand off from Obsidian, open it in your phone’s browser or copy the place name into Amap. Device-specific app opening and search results have not been tested on your iPhone or Android. Keep Chinese names and essential route screenshots as a backup; saved favorites do not establish offline routing.

For **Manner**, the search is deliberately broad: select the North Bund / Guoke Binjiang branch matching the listed Taiping Road/SIPG Tower location. For **Terracotta Warriors**, verify the museum visitor entrance rather than navigating to the mausoleum mound.

'''
s=s.replace('## Beijing: art, old streets, and tea',intro+'## Beijing: art, old streets, and tea',1)
p.write_text(s)
p=base/'staged'/names[1]
s=p.read_text()
old='- [ ] Choose a mapping app and save Chinese names, addresses, and screenshots.'
new='''**Navigation choice: AMap Global / Gaode Maps (高德地图).** [Download for iPhone](https://apps.apple.com/cl/app/amap-global/id461703208) · [Download for Android](https://play.google.com/store/apps/details?id=com.autonavi.minimap). Install before departure and test language settings and routes on each phone. [[China — Places and Experiences Shortlist#Open these places in Amap|Open the 16 location searches]].

- [ ] Install AMap Global on the phone(s) you will use, then save the correct places and essential screenshots.'''
assert old in s
p.write_text(s.replace(old,new,1))
p=base/'staged'/names[2]
s=p.read_text()
old='**Places and experiences:** [[China — Places and Experiences Shortlist|Art districts, tea, Chinese place names, food and café candidates]]'
new='**Places and experiences:** [[China — Places and Experiences Shortlist|Art districts, tea, food and cafés — 16 Amap location searches]] · [[China — Places and Experiences Shortlist#Open these places in Amap|Amap downloads for iPhone and Android]]'
assert old in s
p.write_text(s.replace(old,new,1))
p=base/'staged'/names[3]
p.write_text(p.read_text()+'''\n## Amap links — 8 October 2026\n\nAdded 16 city-scoped Amap search links beside all shortlist locations, plus iPhone/Android app-store links in the shortlist and preparation note. The user reports using both platforms.\n\n- [Amap URI search documentation](https://lbs.amap.com/api/uri-api/guide/search/search?type=spa), updated 20 August 2024, opened today: HTTPS search endpoint, keyword/city parameters, mobile/PC support, and optional mobile app handoff.\n- [AMap Global — Chile App Store](https://apps.apple.com/cl/app/amap-global/id461703208), opened today: app identity and iPhone distribution.\n- [AMap Global — Google Play](https://play.google.com/store/apps/details?id=com.autonavi.minimap), official listing opened during the Amap discussion: Android distribution.\n\nValidated every generated URL’s host, parameters, encoding, keyword, and city. These links are constructed searches, not fetched Amap POI/share IDs. A representative Bund search could not be retrieved by the web research tool. No phone/browser-to-app handoff, live search result, saved favorite, or offline feature was tested. Manner’s search requires matching the exact branch to the listed location; museum searches require choosing the visitor entrance.\n''')
p=base/'staged'/names[4]
p.write_text(p.read_text()+'''\n## Amap navigation links — same day\n\nUser asked to add Amap links for the trip’s locations and supports both iPhone and Android. Added 16 Amap search links directly to the shortlist tables, plus official download links and navigation instructions. Linked this section from Start Here and preparation. Used the documented HTTPS URI format with city/keyword scope and optional app handoff. Search links require checking the branch/entrance; they are not verified POI pins.\n\nBackups and staged updates: `/home/ivanaguilera/Work/china-amap-links-20261008/`. Both-platform handset opening, live POI matches, favorites and offline navigation remain untested.\n''')
for url,keyword,city in links:
    parsed=urlparse(url)
    params=parse_qs(parsed.query)
    assert parsed.scheme=='https' and parsed.netloc=='uri.amap.com' and parsed.path=='/search'
    assert params['keyword']==[keyword] and params['city']==[city] and params['callnative']==['1']
assert len(links)==16
for p in (base/'staged').glob('*.md'):
    for target in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',p.read_text()):
        name,_,anchor=target.partition('#')
        dest=base/'staged'/(name+'.md')
        if not dest.exists(): dest=vault/(name+'.md')
        assert dest.exists(),target
        if anchor: assert any(x.lstrip('# ').strip()==anchor for x in dest.read_text().splitlines() if x.startswith('#')),target
print('Prepared 16 Amap searches; verified URL parameters, wiki links and anchors; backed up 5 notes.')
