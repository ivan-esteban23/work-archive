from pathlib import Path
import hashlib, json, re
base=Path('/home/ivanaguilera/Work/china-guide-additions-20261008')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
names=['China — Start Here.md','China Travel Guide.md','China — Preparation Before Choosing Dates.md','China — Research and Sources 2026-10-08.md','China — Session Recap 2026-10-08.md']
manifest={}
for name in names:
    data=(vault/name).read_bytes()
    (base/'backup'/name).write_bytes(data)
    (base/'staged'/name).write_bytes(data)
    manifest[name]=hashlib.sha256(data).hexdigest()
newname='China — Places and Experiences Shortlist.md'
assert not (vault/newname).exists()
manifest[newname]=None
(base/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
content='''# China — Places and Experiences Shortlist

[[China — Start Here|Dashboard]] · [[China Travel Guide|Main route]] · [[China — Budget|Budget]]

**Research date: 8 October 2026.** A shortlist for the proposed Beijing → Xi’an → Shanghai route. These are candidates, not reserved activities. Chinese text below is for place searches; identify the exact entrance/branch before saving a pin. Opening hours, prices, menus, filming permissions, and future availability need a final check.

## Beijing: art, old streets, and tea

| Candidate / search text | Why I would include it | What to check |
| --- | --- | --- |
| Palace Museum / 故宫博物院 | Main historic anchor; photograph architecture where allowed | Advance tickets; normally closed Mondays; camera rules and exact entrance |
| Mutianyu Great Wall / 慕田峪长城 | Dedicated landscape and architecture outing | Round-trip transport, weather, walking demands, separate lift/extras |
| Yangmeizhu Xiejie / 杨梅竹斜街 | Old-alley texture, books, creative browsing | Individual shops and privacy; keep it an unhurried walk |
| 798 Art District / 798艺术区 | Contemporary art, industrial architecture, design, cafés | Gallery tickets/exhibitions and photography rules; give it a separate outing |
| Maliandao / 马连道 | Tea shopping and a chance to explore Chinese tea beyond the Japan matcha plan | A specific shop, tasting language/price, quantity and total purchase cost |

The municipal government describes Yangmeizhu Xiejie as an old hutong with cultural and commercial uses and 798 as an art/design district with creative retail and cafés. Those two are particularly good additions for your browsing and photography interests. [Beijing tourism/leisure zones, 4 September 2025](https://english.beijing.gov.cn/latest/news/202509/t20250904_4191116.html).

Maliandao is listed by Beijing’s tourism portal as a tea-shopping area on Maliandao Road, Xicheng. Its article dates from 2017: use it to identify the district, not to assume historic shop counts or a particular business is still operating. [Visit Beijing — Maliandao](https://english.visitbeijing.com.cn/article/47ONpUjZFzR). I would make it optional unless tea becomes a major interest; a market visit is not automatically a hosted tasting.

The Palace Museum’s own page says it normally opens Tuesday–Sunday, with national-holiday exceptions, and does **not sell same-day tickets**. Foreign online reservations require passport numbers. The listed standard admission is **CNY 60/person for 1 April–31 October** and **CNY 40/person for 1 November–31 March**, with some galleries extra. These are published tariffs checked today, not dated availability. [Official visitor page](https://intl.dpm.org.cn/visit.html?l=en).

Mutianyu remains the researched Great Wall candidate from the main guide. [Official overview](https://english.beijing.gov.cn/travellinginbeijing/attractions/202603/t20260325_4566115.html).

## Xi’an: city-wall views and a food evening

| Candidate / search text | Why I would include it | What to check |
| --- | --- | --- |
| Xi’an City Wall / 西安城墙 | Architecture and city views; a useful outdoor photo block | Exact entrance, admission, weather, and current cycling rules if wanted |
| Muslim Quarter / 回民街 | Food streets and local cultural context | Specific vendors, ingredients, portions and permission before close-up filming |
| Terracotta Warriors / 秦始皇帝陵博物院 | The main reason for this stop | Reserved slot, original passport, transport and equipment restrictions |

Xi’an’s municipal overview identifies the wall as a place to walk or cycle with city views and the Muslim Quarter as a collection of food streets. It highlights lamb soup with bread and roujiamo. Treat the quarter as a neighborhood to explore rather than assuming one tourist street contains every worthwhile meal. [Xi’an municipal landmark guide](https://en.xa.gov.cn/MediaCenter/News/1691691491099529217.html).

My food priorities would be **yangrou paomo (羊肉泡馍)**, **roujiamo (肉夹馍)**, and a noodle meal. Confirm the meat/filling at the selected shop; versions vary, and a dish name does not establish dietary suitability. The bread-and-lamb-soup and meat-sandwich descriptions are supported by the municipal guide. Exact restaurants and protein quantities remain unresearched.

Keep the wall visit and food exploration flexible around the reserved museum day. [Terracotta Warriors visitor instructions](https://www.bmy.com.cn/jingtai/bmyweb/ticketing.html) remain the source for ticket/ID checks; the ambiguous filming wording is still unresolved.

## Shanghai: art, lane shopping, and repeated riverfront visits

| Candidate / search text | Why I would include it | What to check |
| --- | --- | --- |
| The Bund / 外滩 | Architecture and skyline photography under different light | Weather, access and camera/tripod rules; no guaranteed lighting show |
| M50 Creative Park / M50创意园 | Industrial buildings and a visual-art outing | Specific gallery access and exhibits; Putuo district/Moganshan Road search area |
| Tianzifang / 田子坊 | Lane-scale browsing, crafts, gifts, cafés | Exact shops, crowd levels and privacy around residences |
| Xintiandi / 新天地 | Another architecture, shopping and café option | Choose it if the businesses interest you; it need not duplicate Tianzifang |

Shanghai’s tourism listing describes M50 as a visual-art district retaining industrial-building character. Individual galleries can have their own hours even when the wider complex is listed as open year-round. [Official M50 listing](https://www.meet-in-shanghai.net/cn/industry-tours/m50-creative-park-137682/).

The official shopping guide identifies Tianzifang with crafts, boutiques and cafés, and Xintiandi with shikumen architecture, retail and dining. These are browsing areas, not verified vintage/record-shop lists. [Shanghai shopping districts](https://www.meet-in-shanghai.net/en/guide/shopping-in-shanghai-a-selection-of-the-best-neighborhoods-to-find-treasures-726529/). For the riverfront, see the [official Bund overview](https://www.meet-in-shanghai.net/en/nighttime-culture/bund-sightseeing-area-026252/).

### Named food and café candidates

| Place | Provider-listed location | Research reason |
| --- | --- | --- |
| Jia Jia Tang Bao | 127 Huanghe Road, Huangpu | Soup dumplings |
| Da Hu Chun | 136 Sichuan Middle Road, Huangpu | Shengjian buns |
| O.P.S. CAFE, Taiyuan Road branch | No. 1, Lane 177 Taiyuan Road, Xuhui | Seasonal coffee drinks |
| Manner Coffee, North Bund / Guoke Binjiang branch | Taiping Road, 60 m south of SIPG Tower, Hongkou | Riverside coffee |

All four appear in the official tourism guide dated **21 July 2026**, checked today. Locations are candidates for verification; hours, menu prices, availability and filming access were not established. [Shanghai food and coffee guide](https://www.meet-in-shanghai.net/en/guide/taste-your-way-through-shanghai-food-coffee-and-vibrant-neighborhoods-907063/). Search the exact branch, not just the chain name.

## Make it personal without filling every day

My suggested five priorities are: one Great Wall outing, one major historic museum, a Xi’an food evening, one art-district outing, and repeat Shanghai riverfront photography. You have not selected these yet. Tea browsing and a café block can replace shopping or another attraction if they appeal more.

For photography, choose one establishing image, one detail, and a short ambient clip per outing where permitted. Old lanes offer doors, textures, and signs; art districts offer industrial forms; the wall and riverfront offer wider compositions. Those are creative suggestions, not permission to film people or inside galleries. Ask staff before using substantial equipment.

Before accepting a tasting or guided experience, establish the price, language, duration, inclusions, and whether buying products is optional. For tea/gifts, record package weight and total, keep receipts, and check Chile’s current import rules before bringing food or plant products home. No import eligibility is asserted here.

A relaxed day can have one fixed attraction, one nearby meal, and a flexible walk or café. Keep M50, 798, and Maliandao as separate location decisions until actual transit is checked. If the trip is solo, verify small portions/half-duck options rather than budgeting a group-sized meal as one-person dining.
'''
(base/'staged'/newname).write_text(content)

def edit(name,old,new):
    p=base/'staged'/name
    s=p.read_text()
    assert old in s,name
    p.write_text(s.replace(old,new,1))
edit('China — Start Here.md','## First route to compare','**Places and experiences:** [[China — Places and Experiences Shortlist|Art districts, tea, Chinese place names, food and café candidates]]\n\n## First route to compare')
edit('China Travel Guide.md','## The kind of trip worth building','**New shortlist:** [[China — Places and Experiences Shortlist|Beijing art/tea, Xi’an food and city wall, Shanghai cafés and browsing]].\n\n## The kind of trip worth building')
edit('China Travel Guide.md','The exact museum booking procedure and opening days need checking before these become timed plans.','The Palace Museum normally closes Mondays (national-holiday exceptions) and sells no same-day tickets; foreign online reservations require passport numbers. Recheck the actual date before making a timed plan. [Official visitor page](https://intl.dpm.org.cn/visit.html?l=en).')
edit('China — Preparation Before Choosing Dates.md','## Tickets and photography','## Tickets and photography\n\nThe Palace Museum normally closes on Mondays, with national-holiday exceptions, and does not sell same-day tickets. Foreign online bookings require passport numbers. Plan around that before assigning your Beijing museum day. [Official visitor instructions](https://intl.dpm.org.cn/visit.html?l=en), checked 8 October 2026.')
p=base/'staged'/'China — Research and Sources 2026-10-08.md'
p.write_text(p.read_text()+'''\n## Follow-up: places and experiences\n\nAdded [[China — Places and Experiences Shortlist]] on 8 October 2026. The following pages were opened and read for this addition.\n\n| Source | Page date | Supports / limits |\n| --- | --- | --- |\n| [Beijing municipal leisure zones](https://english.beijing.gov.cn/latest/news/202509/t20250904_4191116.html) | 4 Sep 2025 | Yangmeizhu cultural browsing and 798 art/design/cafés; individual businesses need checking |\n| [Visit Beijing — Maliandao](https://english.visitbeijing.com.cn/article/47ONpUjZFzR) | 19 Jun 2017 | Tea-shopping district; historic counts and business access not adopted |\n| [Palace Museum visitor page](https://intl.dpm.org.cn/visit.html?l=en) | Live page, no update date shown | Monday closure exceptions, no same-day sales, passport booking, seasonal standard tariffs; exact-date access not checked |\n| [Xi’an municipal landmark guide](https://en.xa.gov.cn/MediaCenter/News/1691691491099529217.html) | Not recorded | City-wall views, food streets and dish descriptions; current fares/vendors not checked |\n| [Shanghai official M50 listing](https://www.meet-in-shanghai.net/cn/industry-tours/m50-creative-park-137682/) | No update date shown | Industrial/visual-art character; gallery hours vary |\n| [Shanghai shopping guide](https://www.meet-in-shanghai.net/en/guide/shopping-in-shanghai-a-selection-of-the-best-neighborhoods-to-find-treasures-726529/) | No exact date recorded | Tianzifang/Xintiandi browsing; no individual store guarantees |\n| [Shanghai food and coffee guide](https://www.meet-in-shanghai.net/en/guide/taste-your-way-through-shanghai-food-coffee-and-vibrant-neighborhoods-907063/) | 21 Jul 2026 | Four named food/café candidates and listed addresses; no hours, prices or current operational test |\n\nOther pages read but not relied on for new facts included Shanghai’s Shaanxi travel feature and Beijing’s February 2025 food overview. A February 2026 Beijing magazine PDF could not be retrieved; it is not used as supporting evidence. No tour provider or business was contacted. Chinese search names are navigation aids, not saved/verified map pins.\n''')
p=base/'staged'/'China — Session Recap 2026-10-08.md'
p.write_text(p.read_text()+'''\n## Follow-up additions — same day\n\nFollowing “anything else to add,” created [[China — Places and Experiences Shortlist]] with art districts, old lanes, tea-shopping context, city-wall/riverfront photo ideas, Chinese search names, and four Shanghai food/café candidates. Linked it from the dashboard and full guide. Added Palace Museum Monday/same-day ticket constraints to the guide and preparation note and extended the source register. Dates, budget, travelers, and route remain open.\n\nBackups and staged files for the follow-up: `/home/ivanaguilera/Work/china-guide-additions-20261008/`. Businesses’ hours/prices, actual map pins, gallery access, and future attraction availability remain unverified. No bookings or app setup occurred.\n''')
all_stems={p.stem for p in vault.glob('*.md')}|{p.stem for p in (base/'staged').glob('*.md')}
for p in (base/'staged').glob('*.md'):
    for link in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',p.read_text()):
        assert link.split('#')[0] in all_stems,(p.name,link)
print('Prepared 1 new note, 5 focused updates; backed up current notes and checked wiki targets.')
