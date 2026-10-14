from pathlib import Path
from urllib.parse import urlencode, urlparse
import hashlib,json,re

base=Path('/home/ivanaguilera/Work/china-more-ideas-20261008')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
def amap(name,city):
    return 'https://uri.amap.com/search?'+urlencode(dict(keyword=name,city=city,view='list',src='china_trip_guide',callnative=1))
sources={
 'jingshan':'https://english.beijing.gov.cn/foreignersinbeijing/beijingthroughforeignerslens/202401/t20240105_3526514.html',
 'market':'https://english.beijing.gov.cn/consuminginbeijing/onedayinbeijing/sleeplessinbeijing/updatesofnighttimeconsumption/202504/t20250428_4076854.html',
 'walk':'https://english.shanghai.gov.cn/en-FAQs-StudyinShanghai/20251124/9f1658ae899240d19c52784bddfed782.html',
 'suzhou':'https://english.shanghai.gov.cn/en-TravelAcrossChina/20250521/2cd76b748ca1433c98044118867371c5.html',
 'gardens':'https://whc.unesco.org/en/list/813/',
 'hangzhou':'https://english.shanghai.gov.cn/en-TravelAcrossChina/20250515/fc5c158cf2b141dc8bbc8e7e2fb63256.html',
 'water':'https://english.shanghai.gov.cn/en-HeritageZones/20240827/66903de4b44047a5aeb1284a2148fc09.html',
 'chengdu':'https://english.shanghai.gov.cn/en-TravelAcrossChina/20250421/fa4666cf783d46f48fc6edd4cf9dcf95.html',
 'chongqing':'https://english.shanghai.gov.cn/en-TravelAcrossChina/20250514/0a8f03830bcc493190c6b6025e4898b5.html',
 'nature':'https://whc.unesco.org/en/list/640/'
}
rows=[
 ('Jingshan Park / 景山公园','北京','jingshan','Architecture photography looking toward the Palace Museum; pair with the palace day if energy and entry hours allow.'),
 ('Panjiayuan market / 潘家园','北京','market','Crafts, objects, and browsing; ask about materials and provenance before buying. Current vendor and night-market schedules need checking.'),
 ('Wukang Road / 武康路','上海','walk','An unhurried architecture and café walk; choose a small walking area rather than crossing the whole city.'),
 ('Anfu Road / 安福路','上海','walk','Fashion, design, and café browsing; combine with Wukang Road in one neighborhood block.'),
 ('Duozhuayu / 多抓鱼 安福路','上海','walk','Bookshop browsing candidate mentioned in the official city walk. Confirm the current Anfu branch, address, and hours.'),
 ("Humble Administrator’s Garden / 拙政园",'苏州','gardens','Choose one main Suzhou garden for framed views, water, and architecture; check ticket dates and camera rules.'),
 ('Pingjiang Road / 平江路','苏州','suzhou','Canal-side walk to pair with the garden; leave time for a meal instead of adding several far-apart attractions.'),
 ('West Lake / 西湖','杭州','hangzhou','Lake walks and landscape photography; reserve a flexible block for good light rather than promising a sunset.'),
 ('Longjing village / 龙井村','杭州','hangzhou','Tea terraces, tasting, and learning about Chinese green tea. A picking workshop depends on the chosen date and package.'),
 ('Zhujiajiao ancient town / 朱家角古镇','上海','water','Water-town lanes and bridges as an alternative Shanghai excursion; choose this or Suzhou before filling every free day.'),
 ('Jinli / 锦里','成都','chengdu','A Chengdu food-and-street-life starting point. Kuanzhai lanes and the panda base are other research candidates for this new base.'),
 ('Hongyadong / 洪崖洞','重庆','chongqing','A Chongqing night-photography starting point. Liziba, the riverfront, and a hotpot meal could form a separate city chapter.'),
 ('Wulingyuan / 武陵源','张家界','nature','Sandstone pillars and ravines for a landscape-focused route; park entrances, walking demands, and transport need dedicated planning.')
]
ideas='''# China — More Ideas and Route Choices

[[China — Start Here|Dashboard]] · [[China — Places and Experiences Shortlist|Original shortlist]] · [[China — Klook Experience Research 2026-10-08|Paid experience research]]

**Researched 8 October 2026.** These are optional ideas for an undated trip. Routes below are planning judgments; no transport, hotels, or activities are booked.

## My strongest additions for your interests

I would first add **a Shanghai dumpling-making class**, **one Suzhou garden followed by Pingjiang Road**, and **a Wukang–Anfu neighborhood walk**. They build on your food, photography, cafés, and browsing interests without adding another hotel base. Jingshan is a useful Beijing photography candidate to compare with the existing palace day.

If tea becomes a main interest, **two nights in Hangzhou** are my strongest route expansion: one lake block and one Longjing village block, with room for transfers. That recommendation is about pace and your interests; it is not a checked train itinerary. The municipal feature describes West Lake and Longjing village, including tea terraces and tea culture. [Hangzhou overview](SOURCE_HANGZHOU).

## Places to compare

The Amap links use the same city-scoped search format as your original shortlist, for both iPhone and Android. They are **searches, not checked POI pins**; confirm the entrance or shop branch. Phone handoff and current search results remain untested. [[China — Places and Experiences Shortlist#Open these places in Amap|Downloads and instructions]].

| Idea / Chinese search | Why it might fit / next check | Amap for either phone | Evidence |
| --- | --- | --- | --- |
'''.replace('SOURCE_HANGZHOU',sources['hangzhou'])
for title,city,key,why in rows:
    chinese=title.split(' / ')[1]
    ideas+=f'| {title} | {why} | [Search in Amap]({amap(chinese,city)}) | [Source]({sources[key]}) |\n'
ideas+='''
## Excursion or new base?

**Suzhou:** my first excursion candidate from Shanghai for gardens and canal photography. Choose the Humble Administrator’s Garden or research the Lingering Garden as an alternative; UNESCO lists both within the classical-gardens property. One garden, Pingjiang Road, and a meal are a more useful starting plan than buying a package covering several gardens, temples, hills, and a second water town. Compare the actual rail stations, local transfers, admission reservations, and return connection once dates are set. [UNESCO gardens](SOURCE_GARDENS) · [Suzhou overview](SOURCE_SUZHOU).

**Zhujiajiao:** another water-town option within Shanghai, with riverside buildings and Fangsheng Bridge. Compare it with Suzhou on the scenery you want and the complete travel day. I would select one initially and keep the other optional. Boat rides and attraction tickets require separate inclusion checks; a town visit does not establish that every site or boat is included. [Shanghai heritage overview](SOURCE_WATER).

**Hangzhou:** allow an arrival/lake block, a Longjing tea block, and an onward-transfer block if staying two nights. Keep tea purchasing separate from workshop fees and ask for the quantity and full purchase price. A provider offers picking, hand-frying, and tasting, but future picking conditions, dates, and language availability remain to be checked in [[China — Klook Experience Research 2026-10-08]].

**Chengdu:** a route replacement for food, lanes, and an optional panda-base visit. The municipal Sichuan feature identifies Jinli, Kuanzhai, and the Chengdu panda base. Begin with one food/neighborhood day and research the panda outing separately; admission does not guarantee close animal encounters. Specific tea houses and restaurants still need verification. [Sichuan overview](SOURCE_CHENGDU).

**Chongqing:** a route replacement if urban night photography and hotpot matter more than Xi’an history. Hongyadong and Liziba are starting points from the official overview, not a finished walking route. Check actual viewpoints, crowd conditions, hills/stairs, river crossings, and hotel access before choosing a base. Do not assume every camera viewpoint is public or every skyline light operates nightly. [Chongqing overview](SOURCE_CHONGQING).

**Zhangjiajie / Wulingyuan:** the strongest landscape alternative in this round. UNESCO describes a landscape of sandstone pillars and ravines. Treat it as a dedicated city/park chapter, with weather flexibility and a checked entrance plan. Any Tianmen Mountain or glass-bridge ticket would require its own location and inclusion research; this Wulingyuan source does not verify those products. [UNESCO Wulingyuan](SOURCE_NATURE).

## Route choices with the same 14-night allowance

| Priority | Illustrative nights | What changes |
| --- | --- | --- |
| Keep the history route | Beijing 5 + Xi’an 3 + Shanghai 6 = 14 | Add Shanghai activities and choose one excursion within the existing stay |
| Add a tea chapter | Beijing 5 + Xi’an 3 + Hangzhou 2 + Shanghai 4 = 14 | Four bases and three internal transfer days; reduces Shanghai time and adds packing/transport |
| Regional food | Beijing 4 + Chengdu 4 + Shanghai 6 = 14 | Replaces Xi’an; gives up the Terracotta Warriors |
| Urban night photography | Beijing 4 + Chongqing 4 + Shanghai 6 = 14 | Replaces Xi’an; prioritizes river-city scenery and food |
| Landscapes | Beijing 4 + Zhangjiajie 4 + Shanghai 6 = 14 | Replaces Xi’an; connections, weather, and park access determine feasibility |

These are **14 nights / 15 local calendar days**, excluding international travel time from Chile. Route order and transfer feasibility have not been established. Chengdu, Chongqing, and Zhangjiajie are alternatives to choose among for this allowance.

## What deserves another research round

Verify a small list of current vintage shops, vinyl stores, and film-related shops with exact branches; this search did not establish enough store-level evidence to recommend names. Develop a food list around the selected neighborhoods and dietary preferences. After the route and month are chosen, check seasonal suitability, holidays, dated transport, admission, filming rules, and complete hotel totals.
'''
for key,url in sources.items(): ideas=ideas.replace('SOURCE_'+key.upper(),url)
new={'China — More Ideas and Route Choices.md':ideas}
existing=['China — Start Here.md','China Travel Guide.md','China — Places and Experiences Shortlist.md','China — Research and Sources 2026-10-08.md','China — Session Recap 2026-10-08.md']
manifest={}
for name in existing:
    data=(vault/name).read_bytes()
    (base/'backup'/name).write_bytes(data)
    manifest[name]=hashlib.sha256(data).hexdigest()
    content=data.decode()
    if name=='China — Start Here.md':
        content=content.replace('## First route to compare','**More ideas:** [[China — More Ideas and Route Choices|Tea, gardens, cooking, and route choices]] · [[China — Klook Experience Research 2026-10-08|Four paid experience candidates and exploratory prices]]\n\n## First route to compare')
    elif name=='China Travel Guide.md':
        content+='\n## More ideas to compare\n\nSee [[China — More Ideas and Route Choices]] for 13 new location searches, Hangzhou tea, Suzhou gardens, and Chengdu/Chongqing/Zhangjiajie route choices. [[China — Klook Experience Research 2026-10-08]] holds four exploratory paid experiences; availability, package units, and final totals need dates. The base itinerary remains a proposal.\n'
    elif name=='China — Places and Experiences Shortlist.md':
        content+='\n## Further ideas\n\nContinue with [[China — More Ideas and Route Choices]] for additional Beijing/Shanghai stops, Suzhou and Hangzhou, and alternative bases, with 13 more Amap searches. See [[China — Klook Experience Research 2026-10-08]] for tea, food, cooking, and water-town experience research.\n'
    elif name=='China — Research and Sources 2026-10-08.md':
        content+='\n## Further ideas — 8 October 2026\n\nCreated [[China — More Ideas and Route Choices]] using these opened pages. Older tourism features supply place context; no historical transport times, visa advice, or future operating schedules were adopted. Specific venues, ticket dates, and entrances still require checks.\n\n'
        for key,url in sources.items(): content+=f'- [{key.title()} source]({url}): place descriptions supporting the new idea note.\n'
        content+='\nKlook searches in USD and provider-page reads are documented separately in [[China — Klook Experience Research 2026-10-08]]. Search prices and page displays differed; no dates or quantities were selected. Several ambiguous titles/summaries were excluded.\n'
    else:
        content+='\n## Further ideas — same day\n\nUser will test Amap later and requested more trip research. Added [[China — More Ideas and Route Choices]] with 13 new city-scoped Amap searches and flexible 14-night comparisons, including a two-night Hangzhou tea chapter. Added [[China — Klook Experience Research 2026-10-08]] with four candidates, displayed USD search amounts, provider checks, price discrepancies, and unresolved package terms. Linked both from dashboard, guide, shortlist, and evidence note.\n\nBackups and staged files: `/home/ivanaguilera/Work/china-more-ideas-20261008/`. Next: choose priorities/month, verify current shops and selected experience packages, then compare dated transport and hotel totals. Dates, travelers, budget, and route remain open; no bookings or phone tests performed.\n'
    (base/'staged'/name).write_text(content)
for name,content in new.items():
    assert not (vault/name).exists(),name
    manifest[name]=None
    (base/'staged'/name).write_text(content)
(base/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Prepared 13 place searches and five focused updates; backups saved.')
