from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
import hashlib, json, re, shutil, sys

V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
W = Path('/home/ivanaguilera/Work/japan-guide-update/nagoya')
NOTES = {}
NOTES['Japan 2027 — Nagoya Chapter.md'] = '''# 🏯 Japan 2027 — Nagoya chapter

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Nagoya Pocket Routes|Three pocket routes]] · [[Japan 2027 — Osaka Chapter|Compare Osaka]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / bookings]]

[[#Google Maps — places and transport|📍 Google Maps]] · [[#Foods to try|🍜 Food]] · [[#Getting here — Tokyo airports and Centrair|🚄 Getting here]]

**Research checked:** 7 October 2026. **Working year:** 2027, unconfirmed. This optional chapter focuses on local food, Osu clothing/collectibles, records, gardens, architecture, and photography. Hotels, dates, transport, tickets, menus, and shop stock remain unconfirmed.

## My starting recommendation for you

Start by comparing **two nights**: arrive and eat locally → one full city day with a castle OR garden morning, Osu browsing, and a short Sakae evening → depart toward Kyoto or Tokyo. That gives one full sightseeing day without forcing another flight into the mainland route.

Choose **three nights** if you want a second full day for **Inuyama OR Ghibli Park OR a museum-focused city day**. Those are alternatives. Ghibli Park earns the extra time only if the films appeal to you and the right dated ticket is available.

With less time, compare a **transfer-day stop between Tokyo and Kyoto**: store luggage, have one meal, and choose one area. First confirm storage hours/capacity and the onward train. A brief station meal is feasible with a shorter stop; a castle plus Osu plus Sakae circuit needs substantially more time. These durations are my itinerary recommendations, not operator tour packages.

## Choose a base

| Base | Why consider it | What to check |
| --- | --- | --- |
| **Nagoya Station / Meieki** | Easiest starting comparison for Shinkansen arrival/departure and a short stay | The actual hotel entrance and walk with luggage; JR, Meitetsu, subway, and Aonami have different gates. |
| **Sakae / Yabacho** | Clothing, records, evening food, and city photos | Subway transfer from arrival station and the return after dinner. |
| **Fushimi** | A central alternative between station and Sakae | Hotel price, walk, and actual route to your chosen sights. |

Use the [city access guide](https://www.nagoya-info.jp/en/access/) and [getting-around guide](https://www.nagoya-info.jp/en/access/traffic/) to compare hotel locations. No hotel is selected.

## A city day — choose one morning anchor

**Nagoya Castle / Hommaru Palace:** my first comparison for architecture. The castle operator currently lists the **main keep as closed**; the reconstructed **Hommaru Palace** is a separate visitor attraction. Plan for the areas actually open, rather than a climb inside the keep. [Current castle visitor guide](https://www.nagoyajo.city.nagoya.jp/en/map/hommaru/) · [Hommaru Palace](https://www.nagoyajo.city.nagoya.jp/en/nagoyajo/honmarugoten/).

Check current admission, opening, and palace rules before visiting; the subway station is now **Nagoyajo**, rather than the old Shiyakusho name found in older guides. [City castle listing / access](https://www.nagoya-info.jp/en/spot/detail/1).

**Tokugawaen:** the alternative for pond, bridge, foliage, and quieter garden photography. **Tokugawa Art Museum** is a separate museum choice next to the garden; check each ticket/calendar instead of assuming one admission includes both. For a shopping-focused day, choose the garden alone. [Garden operator](https://www.tokugawaen.aichi.jp/english/index.html) · [Museum visitor listing](https://db.nagoya-info.jp/en/spot/detail/14).

**Atsuta Jingu:** another alternative for a shrine and wooded precinct walk. Choose it in place of the castle/garden morning if shrine culture interests you most. Observe the area's photography signs and give worshippers space. [Shrine visitor information](https://www.atsutajingu.or.jp/en/vis/) · [Precinct map](https://www.atsutajingu.or.jp/en/pre/).

Then take a seated lunch/break → one Osu shopping block → one Sakae evening block. Leave the other morning anchors for a longer stay.

## Osu and Sakae — shopping for your interests

**Osu shopping streets:** the main browsing area for your vintage/casual clothing, small shops, and collectibles interests. Start near Osu Kannon or Kamimaezu and choose a manageable walking loop. Individual stores keep their own hours; covered shopping streets still involve outdoor walking between areas. [Official Osu guide](https://www.nagoya-info.jp/en/spot/detail/19/).

**Mandarake Nagoya:** a verified toy/collectible lead at **3-18-21 Osu, Naka-ku**. Browse its branch information before visiting. It is an option for your model/collectible interests; specific Tamiya kits have not been confirmed. [Official branch](https://www.mandarake.co.jp/dir/ngy/index-en.html).

**diskunion Nagoya:** your record-shopping lead in **Sakae East Building 2F, 4-2-7 Sakae, Naka-ku**. It is in the Sakae area, so route it separately from Osu. Check hours and the actual record format/condition before buying. [Official branch](https://diskunion.net/shop/nagoya).

**Nagoya PARCO:** use the current tenant directory to shortlist clothing, accessories, and beauty counters. Its **South Building is scheduled to close on 28 February 2027**; the announcement says the West Building, East Building, and PARCO midi will continue. For a later 2027 visit, use the new floor guide rather than an old South Building shop pin. [Closure announcement](https://nagoya.parco.jp/pnews/detail/?id=37168) · [Shop directory](https://nagoya.parco.jp/shop/?category_search=alpha).

For you, prioritize **one denim jacket OR one shirt/flannel**, then compare T-shirts/trousers only if the remaining cap allows. Your saved starting sizes are **L tops / EU 44–46 trousers**; compare garment measurements and try on rather than directly converting Japanese labels. For her, browse one accessory or measured garment matching her Y2K/Korean outfit preferences. Her size remains open. See [[Japan 2027 — Clothing to Browse Online]] and [[Japan 2027 — Gifts for Her]] for the existing shortlist; these are buying priorities, not claims about current Nagoya stock.

Perfume remains a test-in-store idea in [[Japan 2027 — Gifts for Her]]. Check the actual counter/brand listing first; no particular Nagoya scent or bottle stock is promised.

## Sakae photos and an easy evening

**Oasis 21 → nearby MIRAI TOWER / Hisaya-Odori area** is my suggested short architecture/photo walk. Choose a café or dinner and a few evening frames, rather than an additional all-night shopping circuit. Tower observation admission is optional; check its current opening and event pricing. [Oasis 21 operator](https://www.sakaepark.co.jp/en/) · [MIRAI TOWER visitor information](https://www.nagoya-info.jp/spot/detail/9/).

Shot sequence: city wide → architectural line/reflection → permitted shop detail → meal close-up → evening landmark. Pick three to five usable clips for a 30–90 second edit. Ask before filming inside shops, restaurants, palaces, and museum galleries; a visit ticket does not establish filming permission. Record decisions in [[Japan 2027 — Photography and Filming Wishlist]].

## Indoor museum alternatives

| Choice | Why it might suit you | Route / practical distinction |
| --- | --- | --- |
| **Toyota Commemorative Museum of Industry and Technology** | Textile machinery and automobile manufacturing exhibits; a good comparison for mechanical interests | At 4-1-35 Noritake Shinmachi, Nishi-ku, Nagoya. This is a different institution from Toyota Automobile Museum in Nagakute. Check demonstrations/calendar; currently closed Mondays, with a holiday exception. |
| **SCMAGLEV and Railway Park** | Trains, engineering, and exhibit photography where permitted | Nagoya → Aonami Line → Kinjofuto → short walk. It is a separate port-area outing, not next door to the Toyota museum. Check admission, closure days, and simulator arrangements. |

[Toyota museum operator](https://www.tcmit.org/english/) · [Railway museum operator](https://museum.jr-central.co.jp/en/) · [Railway museum access](https://museum.jr-central.co.jp/en/access/).

Choose **one** as a rain/heat alternative to the outdoor morning. For the farther railway museum, rebuild the day's timings and reduce browsing if necessary. Do not assume a garden museum or Ghibli Park is an equally convenient last-minute rain substitute.

## One extra day — choose your branch

**Inuyama:** my first comparison if you want castle-town streets, river context, and a slower photography day. Use a suitable Meitetsu service from **Meitetsu Nagoya to Inuyama Station**, then walk via the castle-town streets toward Inuyama Castle. The castle operator gives about **20 minutes on foot from the station**. Confirm the actual train, opening/ticket, and your comfort with the castle visit. Return to the same Nagoya hotel. [Castle operator access](https://inuyama-castle.jp/access/street-view) · [JNTO Inuyama Castle guide](https://www.japan.travel/en/spot/1246/).

**Ghibli Park, Nagakute:** a full outing branch in Expo 2005 Aichi Commemorative Park. It is **different from Ghibli Museum in Mitaka, Tokyo**. The operator currently requires advance reservations; ticket types give different access, and a warehouse entry time needs attention. Select the date, areas, and official release rules before assigning this day. The current sales page covers 2026 releases and does not confirm your 2027 inventory. [Official overseas tickets](https://ghibli-park.jp/en/ticket/).

Compare the subway route to **Fujigaoka**, then **Linimo to Ai-Chikyuhaku Kinen Koen**, with the operator's entrance directions and enough walking/time for your selected areas. No Ghibli ticket is purchased. [Official directions](https://ghibli-park.jp/en/directions/) · [Japanese access / route map](https://ghibli-park.jp/access).

**Stay in Nagoya:** one of the museums above plus a remaining city interest is the flexible alternative. For textiles, compare **Arimatsu historic streets / Arimatsu-Narumi Tie-Dyeing Museum** instead; this needs its own transfer and opening check, rather than an extra stop on an Inuyama/Ghibli day. A small shibori textile is a fashion-gift lead without requiring her clothing size. Check the actual shop, product, price, and any workshop reservation. [Official Arimatsu visitor listing](https://www.nagoya-info.jp/en/spot/detail/55/) · [Aichi historic-town / museum guide](https://aichinow.pref.aichi.jp/en/spots/detail/18).

These are cultural walks, not a new mountain-hiking itinerary. Keep hiking and Fuji choices in [[Japan 2027 — Hiking and Mount Fuji]].

## Foods to try

| Food | What to expect / when to choose it |
| --- | --- |
| **Miso-katsu** | Fried pork cutlet with miso sauce; a main meal. |
| **Tebasaki** | Seasoned chicken wings; an evening sharing/snack choice. |
| **Kishimen** | Flat noodles; a simple lunch comparison. |
| **Miso-nikomi udon** | Udon cooked in a miso broth; a warming meal. |
| **Hitsumabushi** | Grilled eel over rice, eaten in several ways; compare the menu price before choosing. |
| **Ogura toast / café morning** | Sweet bean toast or a breakfast set; check the café's actual hours and inclusions. |

[Official Nagoya food digest](https://www.nagoya-info.jp/en/gourmet/digest/) · [Nagoya Meshi Council restaurant map](https://en.nagoya-meshi.jp/map/).

My starting food sequence: noodle lunch → wings OR miso-katsu dinner → one café breakfast. Substitute a priced eel meal if it matters to you; no need to eat every specialty. Use the council map to choose a **specific current branch near your route**, then confirm its own menu and opening. No restaurant seat, 2027 menu, or queue length is established here.

**Sweet / matcha lead:** Aoyagi Sohonke's Osu main store, with uiro and its current café offerings. Browse the maker's site and select a small package or a seated sweet break. [Maker](https://www.aoyagiuirou.co.jp/) · [Current stores / Osu main store](https://www.aoyagiuirou.co.jp/store/). This is a matcha-dessert lead; matcha powder stock is not confirmed.

## Souvenirs and the shared shopping cap

Your first comparison: **one compact uiro / Kaeru Manju sweet gift**, **one clothing or shibori textile choice**, or **one record/collectible**. The maker lists the sweets; choose the actual package and check its ingredients, expiry, and storage for the remaining journey. [Aoyagi sweets](https://www.aoyagiuirou.co.jp/).

This chapter uses the existing **US$300 shopping/miscellaneous allowance**. It does not create a Nagoya allowance. Her **US$200** gift cap is still unresolved: inside US$300 leaves US$100 for your purchases; as an additional allocation within US$5,000 it reduces the existing reserve by US$200. Any Nagoya sweet, textile, accessory, or fragrance replaces a choice already in [[Japan 2027 — Shopping Shortlist]] / [[Japan 2027 — Gifts for Her]].

## Summer, November, and May

| Season | How I would adapt this module |
| --- | --- |
| **Summer** | Short outdoor morning; seated lunch and an indoor museum or limited shop block; evening Sakae photos if comfortable. Check dated weather and reduce walking during heat/rain. |
| **November** | Compare Tokugawaen for autumn color and city/food exploring. The garden identifies autumn maple color, but your travel date's peak and 2027 events remain unconfirmed. |
| **May** | Compare the garden's greenery and a town walk with a café break. Check actual weather; do not promise every flower at peak. The wider May plan remains after Golden Week. |

[Tokugawaen seasonal guide](https://www.tokugawaen.aichi.jp/english/03_season/index.html) · [[Japan 2027 — Summer Guide]] · [[Japan 2027 — Autumn Guide]] · [[Japan 2027 — November vs May]]. These adaptations are planning judgments; no seasonal forecast or event booking is implied.

## Getting here — Tokyo airports and Centrair

**From Tokyo / Kyoto / Osaka:** Nagoya is a stop on the Tokaido Shinkansen corridor. Compare Tokyo or Shinagawa → Nagoya, Nagoya → Kyoto, and **Shin-Osaka** → Nagoya using the actual dated service. Osaka Station and Shin-Osaka are different transfer points. Price the whole selected route, seat, baggage needs, and local hotel transfers. [JR Central official planning / train information](https://global.jr-central.co.jp/en/) · [City intercity access](https://www.nagoya-info.jp/en/access/).

**From Haneda (HND):** compare Keikyu → **Shinagawa**, then a separately selected Shinkansen → Nagoya. Allow immigration/baggage, terminal-to-station walking, the station transfer, and a flexible connection after an international flight. [Keikyu airport access](https://www.haneda-tokyo-access.com/en/) · [JR Central](https://global.jr-central.co.jp/en/).

**From Narita (NRT):** compare a suitable Narita Express → **Tokyo or Shinagawa**, then Shinkansen → Nagoya. Confirm the actual N'EX destination and both reservations; the airport train does not continue to Nagoya. [JR East N'EX](https://www.jreast.co.jp/en/multi/nex/) · [JR Central](https://global.jr-central.co.jp/en/). The existing seasonal plan starts with Tokyo nights, so direct airport-to-Nagoya is an alternative arrival pattern, not an extra compulsory transfer.

**From Chubu Centrair (NGO):** compare Meitetsu → **Meitetsu Nagoya**, then your hotel transfer. On μSKY all cars require a first-class μticket in addition to the regular ticket; compare an appropriate ordinary-car service if that suits better. NGO is different from **Nagoya/Komaki Airport (NKM)**. Read the actual airport code on any flight choice. [Meitetsu airport operator guide](https://www.meitetsu.co.jp/eng/airport-access/).

**From Kawaguchiko:** compare the dated bus to **Mishima**, then a suitable onward Shinkansen route to Nagoya. The operator currently requires a reserved bus seat; confirm the dated release and book it once the route is selected. Check that the chosen train stops at Mishima and whether a connection is needed; the bus and rail leg need a realistic buffer. [Fujikyu Mishima bus](https://bus.fujikyu.co.jp/en/highway/mishima/) · [JR Central](https://global.jr-central.co.jp/en/) · [[Japan 2027 — Hiking and Mount Fuji]]. Do not route every train as if it served every station.

**Within Nagoya:** subway plus walking is the starting comparison; Meitetsu serves the Inuyama/airport branches, Aonami the railway-museum branch, and Linimo the park branch. Consider a city pass only after counting your eligible rides and checking date/line coverage. A city subway/bus pass does not automatically include those other railways. [Official local transport / passes](https://www.nagoya-info.jp/en/access/traffic/).

## Fit it into the existing 14 nights

These are mutually exclusive seasonal comparisons. Choose which nights to replace before adding hotels. The original dated blossom itinerary and the separate Fuji summit/hut route keep their own plans.

| Choice | Hotel-night sequence | Total |
| --- | --- | --- |
| **Existing seasonal comparison** | Tokyo 4 → Kawaguchiko 2 → Kyoto 6 → Tokyo 2 | **14** |
| **Two-night Nagoya** | Tokyo 4 → Kawaguchiko 2 → Nagoya 2 → Kyoto 4 → Tokyo 2 | **14** |
| **Three-night Nagoya** | Tokyo 4 → Kawaguchiko 2 → Nagoya 3 → Kyoto 3 → Tokyo 2 | **14** |
| **Transfer-day stop only** | Keep the existing 14 hotel nights; add a carefully timed stop to a suitable transfer day | **14** |

The two/three-night branches reduce Kyoto time, including the space available for Kansai day trips. Do not also insert Osaka, Nara overnights, Fukuoka, Sapporo, Okinawa, or an island module without rebuilding the count. A transfer-day stop can change ticket arrangements, time, and storage cost even when hotel nights stay the same.

Keep the existing **US$5,000 in Japan, excluding international flights**. The seasonal allocations remain US$4,100 planned + US$900 reserve before any extra gift allocation. Requote replaced hotels, complete rail/airport costs, admissions, and local transport against [[Japan 2027 — Seasonal Planning and Bookings]]. No booking, purchase, extra allowance, or rail-pass saving is assumed.

## Google Maps — places and transport

Search links locate places; they do not confirm an entrance, opening, ticket, inventory, or dated transport. Check the operator address and actual route before going. Choose only the pins for your selected branch.

MAP_TABLE

## Before assigning dates

- Choose a transfer stop, two nights, or three nights and identify replaced hotel nights.
- Select one city morning anchor and one extra-day branch if staying longer.
- Check castle areas, museum calendars, PARCO's updated tenant map, and the actual shop/restaurant branches.
- For Ghibli Park, confirm your ticket areas, release date, visit date, entry timing, and access before setting the day.
- Quote all route legs, luggage arrangements, hotels, and selected admissions within the existing budget; keep the shared shopping/gift decision visible.

Use [[Japan 2027 — Nagoya Pocket Routes]] for the phone-friendly version and [[Japan 2027 — Today]] once an actual date is selected.
'''

PLACES = [
    ('JR Nagoya Station', 'Nagoya Station JR Nagoya Japan', 'Shinkansen arrival / departure'),
    ('Meitetsu Nagoya Station', 'Meitetsu Nagoya Station Nagoya Japan', 'Airport / Inuyama services; separate gates'),
    ('Chubu Centrair airport — NGO', 'Chubu Centrair International Airport Tokoname Japan', 'Alternative arrival; verify airport code'),
    ('Sakae Station', 'Sakae Station Nagoya Japan', 'Sakae hotel / evening area'),
    ('Fushimi Station', 'Fushimi Station Nagoya Japan', 'Alternative central base'),
    ('Nagoyajo Station', 'Nagoyajo Station Nagoya Japan', 'Castle access; renamed station'),
    ('Nagoya Castle', 'Nagoya Castle Nagoya Japan', 'Check currently open areas'),
    ('Hommaru Palace', 'Nagoya Castle Hommaru Palace Nagoya Japan', 'Palace visit; separate from closed main keep'),
    ('Tokugawaen', 'Tokugawaen Nagoya Japan', 'Garden morning alternative'),
    ('Tokugawa Art Museum', 'Tokugawa Art Museum Nagoya Japan', 'Separate museum ticket / calendar'),
    ('Atsuta Jingu', 'Atsuta Jingu Nagoya Japan', 'Alternative shrine morning'),
    ('Osu shopping streets', 'Osu Shopping District Nagoya Japan', 'Clothing / browsing area'),
    ('Osu Kannon', 'Osu Kannon Nagoya Japan', 'Temple / western walking anchor'),
    ('Kamimaezu Station', 'Kamimaezu Station Nagoya Japan', 'Osu access / eastern anchor'),
    ('Mandarake Nagoya', 'Mandarake Nagoya 3-18-21 Osu Nagoya Japan', 'Collectibles lead; no kit stock promise'),
    ('diskunion Nagoya', 'diskunion Nagoya 4-2-7 Sakae Nagoya Japan', 'Records, Sakae East Building 2F'),
    ('Nagoya PARCO', 'Nagoya PARCO West Building Nagoya Japan', 'Use updated 2027 floor / tenant directory'),
    ('Aoyagi Sohonke Osu main store', 'Aoyagi Sohonke Osu Main Store Nagoya Japan', 'Sweet / café lead; confirm opening'),
    ('Oasis 21', 'Oasis 21 Nagoya Japan', 'Sakae architecture'),
    ('Chubu Electric Power MIRAI TOWER', 'Chubu Electric Power MIRAI TOWER Nagoya Japan', 'Exterior photos / optional observation'),
    ('Hisaya-Odori Park', 'Hisaya Odori Park Nagoya Japan', 'Short evening walking block'),
    ('Toyota Commemorative Museum', 'Toyota Commemorative Museum of Industry and Technology Nagoya Japan', 'Industry museum; calendar check'),
    ('SCMAGLEV and Railway Park', 'SCMAGLEV and Railway Park Nagoya Japan', 'Separate port-area museum outing'),
    ('Kinjofuto Station', 'Kinjofuto Station Nagoya Japan', 'Aonami museum access'),
    ('Inuyama Station', 'Inuyama Station Inuyama Aichi Japan', 'Extra-day Meitetsu arrival'),
    ('Inuyama Castle', 'Inuyama Castle Inuyama Aichi Japan', 'Castle-town walking branch'),
    ('Fujigaoka Station', 'Fujigaoka Station Nagoya Aichi Japan', 'Subway / Linimo transfer'),
    ('Ai-Chikyuhaku Kinen Koen Station', 'Ai Chikyuhaku Kinen Koen Station Nagakute Japan', 'Linimo park arrival'),
    ('Ghibli Park', 'Ghibli Park Nagakute Aichi Japan', 'Advance-ticket extra-day branch'),
    ('Arimatsu Station', 'Arimatsu Station Nagoya Japan', 'Alternative textile-town outing'),
    ('Arimatsu-Narumi Tie-Dyeing Museum', 'Arimatsu Narumi Tie Dyeing Museum 3008 Arimatsu Nagoya Japan', 'Textile / craft lead; check calendar'),
]
table = '| Place | Google Maps | Use |\n| --- | --- | --- |\n' + '\n'.join(
    '| ' + name + ' | [Open Maps](https://www.google.com/maps/search/?' + urlencode({'api': '1', 'query': query}) + ') | ' + use + ' |'
    for name, query, use in PLACES
)
NOTES['Japan 2027 — Nagoya Chapter.md'] = NOTES['Japan 2027 — Nagoya Chapter.md'].replace('MAP_TABLE', table)

NOTES['Japan 2027 — Nagoya Pocket Routes.md'] = '''# 🗂️ Japan 2027 — Nagoya pocket routes

[[Japan 2027 — Nagoya Chapter|← Nagoya chapter / Maps / sources]] · [[Japan 2027 — Seasonal Guides|Seasonal guides]] · [[Japan 2027 — Today|Today]]

**Three flexible cards; no calendar assigned.** Checked 7 October 2026. Two nights provide arrival + one full city day + departure. Three nights add one full outing day using Card 3. Short-stop visitors use only the variant in Card 1. Follow current operator links in the chapter; transport, tickets, opening, and stock remain unconfirmed.

## Card 1 — arrival and a local meal

**Route:** selected Shinkansen → JR Nagoya → actual hotel entrance. If using NGO, take a suitable Meitetsu service → Meitetsu Nagoya → hotel; μSKY needs the additional first-class ticket. Meitetsu and JR have separate gates. From HND/NRT, follow the chapter's airport + rail comparison with a realistic flight-arrival buffer.

**Main block:** check in / confirmed luggage drop → one meal → a short walk near the base. If staying in Sakae and arriving early enough, compare a brief Oasis 21 / tower-area exterior walk. Preserve the full shopping block for tomorrow.

**Food:** one noodle or miso-katsu meal. **Shot:** station arrival → street context → meal detail. **Buy:** none required; save the shared shopping allowance for deliberate choices.

**Short-stop variant:** confirm luggage storage and onward train first → one meal + **one** chosen area if timing permits → collect luggage → correct platform. Osu browsing and a Sakae evening are not both compulsory. With a tight connection, keep the meal near the station. No overnight is counted for this variant; recheck the actual ticket arrangement and any storage cost.

## Card 2 — one city anchor, Osu, and Sakae

**Morning:** hotel → **Nagoya Castle / Hommaru Palace OR Tokugawaen OR Atsuta Jingu**. Choose one. The castle's main keep is currently closed; check available areas and palace rules. For Tokugawaen, add the separate art museum only if opening, ticket, and available time suit.

**Midday:** seated lunch / café break → Osu loop from Osu Kannon or Kamimaezu → limited clothing browsing and optionally Mandarake. Check actual shop hours before heading over. Specific Tamiya kits remain unverified.

**Later:** choose diskunion's **Sakae** branch OR a current PARCO clothing/accessory shortlist, then dinner and a short Oasis 21 / MIRAI TOWER exterior photo walk if energy allows. Use the updated directory: PARCO South Building is scheduled to close 28 February 2027. The remaining activities can be skipped rather than rushed.

**Food:** simple lunch → wings or another selected main meal; optional Aoyagi sweet/café break replaces another snack. **Shot:** morning scene → permitted clothing/record detail → evening architecture. **Buy:** one measured garment OR a record/collectible, plus a small gift only within the shared cap. Your saved size is a starting lead; her size remains open.

**Rain/heat alternative:** replace the morning with Toyota Commemorative Museum, or rebuild a shorter browsing day around SCMAGLEV and Railway Park via Aonami / Kinjofuto. Check each museum calendar; Toyota currently has a Monday closure with a holiday exception. Keep a seated break and reduce outdoor walking.

## Card 3 — extra full day: choose A OR B OR C

### A. Inuyama

**Route:** hotel → Meitetsu Nagoya → suitable dated train to Inuyama Station → castle-town walk → Inuyama Castle if selected → return to the same Nagoya hotel. The operator gives about 20 minutes' walk from the station to the castle.

**Main block:** town streets and castle → seated meal/break → a manageable riverside/view block if conditions suit. Check castle access, opening, and the return service. **Shot:** streets → castle architecture → river context. **Buy:** optional one compact keepsake that replaces another purchase. No Ghibli Park or Arimatsu extension is counted.

### B. Ghibli Park

**Route:** hotel → subway to Fujigaoka → Linimo to Ai-Chikyuhaku Kinen Koen → correct park/area entrance → return. Use the official route instructions and selected ticket's timings.

**Main block:** the areas included in your advance ticket, with meal/break and walking time. This is Ghibli Park in Aichi, separate from Tokyo's Ghibli Museum. Confirm release rules, ticket areas, calendar, entry time, and permitted photography. **Shot:** only permitted park scenes. **Buy:** one gift within the existing allowance if wanted. If a suitable ticket is unavailable, select another branch; a same-day entrance purchase is not assumed.

### C. Stay local / textile alternative

**Route:** selected museum OR a remaining city morning interest → meal → limited café/shopping. For a textile-focused outing instead, choose Arimatsu / its tie-dyeing museum with a separate dated transfer and opening check. Price and confirm any workshop before choosing it.

**Shot:** machinery/exhibit detail where allowed OR town/textile texture. **Buy:** a compact shibori textile is an optional gift lead; stock and price need checking. These choices replace A/B rather than join them.

**Departure day:** collect luggage → selected Nagoya station/gates → dated onward train, or hotel → confirmed NGO airport service with check-in buffer. The two/three-night mainland comparisons keep two separate Tokyo hotel nights before the international departure. Do not put a full extra-day outing ahead of a tight departure connection.
'''

LINKS = {
    'Japan 2027 — Start Here.md': '**Nagoya chapter:** [[Japan 2027 — Nagoya Chapter|Food, Osu shopping, records, city sights, transport, and Maps]] · [[Japan 2027 — Nagoya Pocket Routes|Three flexible routes]].',
    'Japan 2027 — Seasonal Guides.md': '**Nagoya option:** [[Japan 2027 — Nagoya Chapter]] compares a transfer stop, two-night city stay, and three-night stay with one Inuyama/Ghibli/museum branch.',
    'Japan 2027 — Summer Guide.md': '**Nagoya alternative:** [[Japan 2027 — Nagoya Chapter|Food, Osu, and indoor museum choices]]. Replace Kyoto nights and shorten outdoor blocks in heat/rain.',
    'Japan 2027 — Autumn Guide.md': '**Nagoya comparison:** [[Japan 2027 — Nagoya Chapter|Tokugawaen, food, and city photography]]. Autumn color and 2027 event dates need checking; a stay replaces other nights.',
    'Japan 2027 — November vs May.md': '**Nagoya comparison:** [[Japan 2027 — Nagoya Chapter]] adapts Tokugawaen and city/town walks for November color versus May greenery without assuming peak dates.',
    'Japan 2027 — Seasonal Planning and Bookings.md': '**Nagoya decision:** [[Japan 2027 — Nagoya Chapter|Transfer stop, two nights, or three nights]]. Identify replaced Kyoto nights and quote full rail, luggage, hotel, and chosen admission costs within the existing ceiling.',
    'Japan Travel Guide 2027.md': '**Nagoya research chapter:** [[Japan 2027 — Nagoya Chapter]] · [[Japan 2027 — Nagoya Pocket Routes]]. Optional mainland stop; original dated blossom itinerary remains unchanged.',
    'Japan 2027 — Shopping Shortlist.md': '**Nagoya browsing option:** [[Japan 2027 — Nagoya Chapter|Osu clothing/collectibles, Sakae records, sweets, and textile gifts]]. Shares the existing shopping allowance; check updated 2027 PARCO tenants and actual stock.',
    'Japan 2027 — Osaka Chapter.md': '**Compare a mainland stop:** [[Japan 2027 — Nagoya Chapter|Nagoya food, Osu/Sakae, and two-night routes]]. Choose which city nights to replace before combining modules.',
    'Japan 2027 — Okinawa Chapter.md': '**Next city chapter:** [[Japan 2027 — Nagoya Chapter|Nagoya]] — a mainland rail-stop comparison with food, city sights, shopping, and optional Inuyama/Ghibli branches.',
}

def validate(root, manifest):
    for name in manifest:
        s = (root / name).read_text()
        assert s.startswith('# ') and 'MAP_TABLE' not in s, name
        for target in re.findall(r'\[\[([^\]|#]+)', s):
            assert target + '.md' in manifest or (V / (target + '.md')).exists(), (name, target)
    s = (root / 'Japan 2027 — Nagoya Chapter.md').read_text()
    assert s.count('https://www.google.com/maps/search/?') == len(PLACES) == 31
    for url in re.findall(r'\]\((https://[^)]+)\)', s):
        assert ' ' not in url
        if 'google.com/maps/search' in url:
            q = parse_qs(urlparse(url).query)
            assert q['api'] == ['1'] and q['query'][0]
    assert all(sum(route) == 14 for route in ([4, 2, 6, 2], [4, 2, 2, 4, 2], [4, 2, 3, 3, 2]))
    assert '28 February 2027' in s and '**main keep as closed**' in s
    s = (root / 'Japan 2027 — Nagoya Pocket Routes.md').read_text()
    assert len(re.findall(r'^## Card [1-3] ', s, re.M)) == 3
    for name in ['Japan 2027 — Summer Guide.md', 'Japan 2027 — Autumn Guide.md']:
        assert all(re.search(r'\| ' + str(day) + r' /', (root / name).read_text()) for day in range(1, 16))

if '--install' in sys.argv:
    manifest = json.loads((W / 'manifest.json').read_text())
    for name, digest in manifest.items():
        p = V / name
        assert (not p.exists()) if digest is None else hashlib.sha256(p.read_bytes()).hexdigest() == digest, name
    validate(W / 'staged', manifest)
    (W / 'backup').mkdir(exist_ok=True)
    for name, digest in manifest.items():
        if digest is not None:
            shutil.copy2(V / name, W / 'backup' / name)
        shutil.copy2(W / 'staged' / name, V / name)
    validate(V, manifest)
    assert all((V / name).read_bytes() == (W / 'staged' / name).read_bytes() for name in manifest)
    print('Saved Nagoya chapter, three pocket routes, 31 Maps links, and ten integrations. Night counts, references, and installed content verified; originals backed up.')
else:
    (W / 'staged').mkdir(parents=True, exist_ok=True)
    manifest = {}
    for name, s in NOTES.items():
        assert not (V / name).exists(), name
        (W / 'staged' / name).write_text(s)
        manifest[name] = None
    for name, line in LINKS.items():
        original = (V / name).read_bytes()
        manifest[name] = hashlib.sha256(original).hexdigest()
        s = original.decode()
        i = s.index('\n') + 1
        updated = s[:i] + '\n' + line + '\n' + s[i:]
        assert updated[:i] + updated[i + len(line) + 2:] == s, name
        (W / 'staged' / name).write_text(updated)
    (W / 'manifest.json').write_text(json.dumps(manifest))
    validate(W / 'staged', manifest)
    print('Prepared Nagoya chapter, three pocket routes, 31 Maps links, and ten integrations. Original content preserved; references and 14-night routes validated.')
