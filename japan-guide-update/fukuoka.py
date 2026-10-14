from pathlib import Path
from urllib.parse import urlencode
import hashlib,json,re,shutil,sys
V=Path('/home/ivanaguilera/Documents/Obsidian Vault')
W=Path('/home/ivanaguilera/Work/japan-guide-update/fukuoka')
NOTES={}
NOTES['Japan 2027 — Fukuoka Chapter.md']='''# 🍜 Japan 2027 — Fukuoka chapter

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Fukuoka Pocket Routes|Three pocket routes]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and bookings]]

[[#Google Maps — sights shopping and transport|📍 Google Maps]] · [[#Foods to try and a yatai evening|🍜 Food]] · [[#Getting here — Haneda Narita and western Japan|🛬 Getting here]]

**Research checked:** 7 October 2026. **Working year:** 2027, unconfirmed. This is an optional city chapter, with no dates, hotels, tickets, or restaurants booked. Routes and stay lengths are my recommendations for your photography, food, tea/cafés, vintage clothes, hobby browsing, and gift interests. Current sources do not confirm 2027 stock, prices, event dates, or travel-day opening times.

## My starting recommendation

Compare **three Fukuoka nights**: arrival and a relaxed Hakata evening → Ohori Park, tea, and Tenjin/Daimyo browsing → **Dazaifu OR Itoshima** → departure. Four nights make room for both excursions or a slower city day. With two nights, prioritize the city and one yatai evening rather than assume two full excursion days fit.

Fukuoka sits on **Kyushu**, west of your Osaka chapter. It earns its place when you want another food-focused city or a gateway to a future Kyushu trip; adding it to 15 days means reducing other bases. It is not scheduled as a casual Kyoto day trip.

## Explore by neighborhood

| Area | Your main reason to visit | How I would use it |
| --- | --- | --- |
| **Hakata Station / Old Town** | Arrival base, food and souvenirs; Kushida Shrine and Tochoji | A manageable history walk on a city day; shorten on arrival |
| **Nakasu / Kawabata** | River views, night photography, yatai | One evening with a selected food stop and river walk |
| **Tenjin / Daimyo** | Vintage clothes, independent shops, collectibles | Your main shopping block, with café breaks |
| **Ohori / Maizuru** | Pond reflections, park walking, art and tea | Main morning outing plus seated tea; one indoor museum option |
| **Dazaifu** | Shrine setting, approach shops, a traditional sweet, museum option | Separate outing; do not combine with the Itoshima coast |
| **Itoshima / Futamigaura** | Coastal scenery and sea-facing torii / rocks | Separate weather-dependent excursion with planned transport |

The city tourism authority identifies Daimyo as a vintage/independent-shopping area and Hakata Station's complex as a food/shopping hub. [Official shopping guide](https://www.gofukuoka.jp/articles/detail/408a917e-7d53-48b8-99ee-e3127e3fdb7b). Use [Hakata's official historic walking course](https://www.gofukuoka.jp/en/route/detail/37ca2359-b761-4c73-8063-f1232dc84ef7) to choose a few stops, rather than treat every temple as compulsory.

## Foods to try and a yatai evening

My first meal is **Hakata tonkotsu ramen**, then one yatai evening and a **mizutaki OR motsunabe** dinner on another night. Taste one sweet during the Dazaifu outing if chosen. Prices, portions, restaurant hours, and dietary preferences are still open.

| Dish | What to expect | My suggested role |
| --- | --- | --- |
| **Hakata tonkotsu ramen** | Pork-bone broth ramen | Arrival/city lunch; choose a menu and queue that suit the day |
| **Mentaiko** | Seasoned pollock roe | Try a small portion with rice or another clearly described dish |
| **Motsunabe** | Offal hot pot with vegetables | One dinner if you enjoy offal; check minimum portions for a solo diner |
| **Mizutaki** | Chicken-and-vegetable hot pot in chicken broth | Dinner alternative if offal is not appealing |
| **Yakitori / skewers** | Grilled skewers; Fukuoka offerings can include pork and vegetables as well as chicken | Choose by ingredients rather than assume every skewer is chicken |
| **Umegaemochi**, Dazaifu | Grilled mochi with sweet red-bean filling | One freshly made sweet on the shrine approach |
| **Yame tea** | Regional tea; compare the actual serving menu | Seated Ohori break, paired with a small meal or dessert if available |

[Official Fukuoka food overview](https://www.gofukuoka.jp/f-food.html) · [Hot-pot explanation](https://www.gofukuoka.jp/en/articles/detail/f8bce646-da5f-4661-8339-8c6764e76a2e) · [Skewer customs](https://gofukuoka.jp/mustdo/) · [Dazaifu sweet explanation](https://www.kyuhaku.jp/en/visit/visit_pguide.html).

### Choose a yatai area

**Yatai are compact food stalls**, a different format from a full indoor izakaya. For you, I would compare **Tenjin** after shopping and **Nakasu** for river/night photos; **Nagahama** is a third option if its location and menus suit your day. Choose one area for dinner rather than schedule a three-district crawl. [Official yatai area comparison](https://gofukuoka.jp/en/articles/detail/ff5d9c6d-860e-4ec5-952f-366c1b2b60fe).

Use the [city's yatai guide](https://gofukuoka.jp/YATAI) and [English stall map](https://gofukuoka.jp/yatai/img/yataimap_eng.pdf) to pick a stall closer to the travel date. The map is an orientation source, not confirmation that every stall will operate that evening. Weather and individual schedules can change the plan.

**My evening plan:** look at the displayed menu/prices → choose one stall with a suitable seat → order a small meal/drink → ask before filming → make room when finished → take your river photos afterward. Keep an indoor restaurant alternative if stalls are closed or queues are unsuitable. [Official yatai dining context and limited-seat etiquette](https://gofukuoka.jp/en/articles/detail/d773d813-d160-4b3f-8092-8f7c2fe5d17d).

Your Osaka izakaya plan remains a separate experience. Fukuoka's first food priority in this chapter is a yatai evening; it does not require buying a guided food tour.

## Tea, shopping, and hobby browsing

| Lead | What I would browse / try | Verified source and location |
| --- | --- | --- |
| **Ohori Terrace / & LOCALS** | Yame tea, a seated café meal, packaged tea/food gift browsing | **1-9 Ohori Koen**, near the Japanese garden. [Current city guide](https://www.gofukuoka.jp/en/articles/detail/f590b215-77b4-4324-8fc8-eb189717744d) |
| **Daimyo** | For you: tee, denim jacket, flannel, or trousers, chosen by condition and fit | Area-level lead; no particular vintage shop inventory confirmed. [Shopping overview](https://www.gofukuoka.jp/articles/detail/408a917e-7d53-48b8-99ee-e3127e3fdb7b) |
| **Tenjin malls / independent shops** | For her: a small accessory or a garment after size confirmation; compare Y2K/Korean-inspired styles if present | Fashion browse, not a verified current product list or 2027 trend forecast. Use the current tenant directory on arrival. |
| **Mandarake Fukuoka** | Used toys/collectibles, manga, CDs/DVDs; choose one item by interest and condition | **Grand Building, 2-9-5 Daimyo, Chuo-ku**; current official hours 12:00–20:00. [Official branch](https://www.mandarake.co.jp/dir/fko/index-en.html) |
| **THE GUNDAM BASE FUKUOKA, Canal City** | Optional Gunpla browse if Gundam models appeal to you | [Current mall branch listing](https://canalcity.co.jp/shop/detail/10210401?tenant_id=10210401). Check access notices and actual item stock. |
| **JR Hakata City / station shopping** | Final packaged sweets and compact gifts | Convenient station-area shopping; check the exact counter and hours for the travel day. [City shopping guide](https://www.gofukuoka.jp/articles/detail/408a917e-7d53-48b8-99ee-e3127e3fdb7b) |

The Canal City Gundam shop and Mandarake are different stops; neither is confirmation of a Tamiya item or a substitute for your Tokyo Tamiya Shinbashi anchor. No Fukuoka record-specific store or perfume counter has been verified in this chapter. For clothing, your L tops / EU 44–46 trousers are size references, not guaranteed Japanese fits. Her size is still needed before choosing fitted garments.

### Souvenirs for you and her

- **Hakata Torimon:** white-bean-filled sweets with a Western-style butter/cream influence; a small box is my first sweet-gift comparison for her. [Manufacturer product description](https://www.meigetsudo.co.jp/info/wp-content/themes/meigetsudo/pdf/202408.pdf). This brochure is dated 2024; use it for the product description, not current prices, pack sizes, or stock.
- **Menbei:** crunchy mentaiko/seafood-flavored crackers; a savory gift alternative. [Manufacturer English product guide](https://www.fukutaro.co.jp/wordpress/wp-content/themes/fukutaro/English.pdf). Older price/tax details in the brochure are not a current purchase quote.
- **Packaged Yame tea:** browse Ohori Terrace's retail selection; confirm tea type, pack size, and price. A good personal/café-memory souvenir without another clothing-size decision.
- **One vintage piece or compact collectible:** replaces another personal shopping choice. Do not add a new city allowance simply because another store is available.

Check food ingredients, storage instructions, and best-before date against your return date. Her purchases share her existing US$200 cap and the unresolved relationship to the main US$300 shopping allowance. [[Japan 2027 — Gifts for Her|Gift wishlist]] · [[Japan 2027 — Shopping Shortlist|Personal shopping]].

## Dazaifu or Itoshima — choose the third-day outing

**Dazaifu:** Nishitetsu Fukuoka (Tenjin) → **Nishitetsu Futsukaichi** → Dazaifu Line → **Dazaifu Station** → shrine approach on foot. Subway Tenjin and Nishitetsu Fukuoka (Tenjin) are distinct stations requiring a walk. [Official heritage access guide](https://www.dazaifu-japan-heritage.jp/en/access/). Plan shrine/approach, lunch, and umegaemochi; add the **Kyushu National Museum** only if its opening calendar and your pace suit. [Museum visitor guide](https://www.kyuhaku.jp/en/visit/visit_pguide.html).

Check [Dazaifu Tenmangu's current official notices](https://www.dazaifutenmangu.or.jp/) before visiting. Shrine restoration/access arrangements have changed; old images of a temporary sanctuary do not establish what will be open in 2027. No specific sanctuary layout, bridge access, or museum exhibition is promised here.

**Itoshima / Sakurai Futamigaura:** choose one coastal area, a meal/café, and your photo walk. [Official prefectural Futamigaura guide](https://www.crossroadfukuoka.jp/fr/spot/12456). Compare **Showa Bus West Coast Liner** from the Hakata/Tenjin area with other dated local options; check the exact boarding point and final return. The operator has published changes affecting the **Futamigaura (Meotoiwa-mae)** stop; the current 2026 timetable uses nearby **PALMBEACH** and **Tsuki-to-Taiyo Itoshima-Sabo** stops. [2026 operator timetable](https://www.showa-bus.jp/wp-content/uploads/2026/03/0_04_westcoastliner_20260401.pdf) · [Operator notices](https://www.showa-bus.jp/2025/08/) · [Operator homepage for updates](https://www.showa-bus.jp/).

Treat those stops as research leads, not 2027 confirmation. Coastal spots are dispersed; a train ride to the Itoshima area does not by itself complete the journey to Futamigaura. A rental car/taxi/tour is an alternative only after a quote and a deliberate choice; driving has not been assumed. A sunset shoot depends on the actual last return transport, so choose an earlier photo session if necessary.

For nature without an excursion, use **Ohori Park and an optional Maizuru walk**. This chapter proposes park/coastal walking, not an unverified mountain-hiking route. Your existing [[Japan 2027 — Hiking and Mount Fuji|hiking chapter]] remains the place for the researched trail options.

## Summer, November, and May

| Season | How I would adapt Fukuoka |
| --- | --- |
| **Summer** | Short park/old-town walks when comfortable, indoor shopping and seated breaks midday, then yatai if operating. Keep the coast weather-dependent; no fireworks or festival has been assigned. |
| **November** | Park/temple photography, a warmer layer for evening stalls, and a hot-pot dinner. Foliage and night events need the actual year's reports; this is not a replacement for Kyoto's foliage plan. |
| **Second half of May** | Park greenery and a coastal outing when conditions suit. Recheck the actual calendar, lodging prices, and excursion transport before choosing dates. |

An example of date-sensitive research is the **2026 Hakata Old Town Lightup Walk**, announced for October 31–November 3. It is **not a 2027 booking opportunity or evidence that mid/late-November dates include the event**. [Current official announcement](https://gofukuoka.jp/events/detail/187d3a5a-4626-457d-9076-3a655f7dc8b8). Keep future events optional until announced.

## Photography and filming

My Fukuoka sequence: **station arrival → old-town architectural detail → tea beside the pond → a clothing/collectible detail with permission → yatai preparation with permission → Nakasu river reflections**. The coast alternative uses a wide sea/torii composition, rock/water detail, and a walking transition. The Dazaifu alternative uses the approach, shrine detail where permitted, and a freshly made sweet.

Use [[Japan 2027 — Photography and Filming Wishlist|your existing 30–90 second outline]]. Ask before recording staff, diners, shop interiors, or food preparation. Follow shrine/museum restrictions and keep walkways and stall seating usable. No drone, tripod placement, or commercial filming permission has been arranged.

## Getting here — Haneda Narita and western Japan

| Starting point | Route to compare | Key checks |
| --- | --- | --- |
| **Haneda (HND)** | Domestic flight HND → Fukuoka Airport **FUK** → Airport Line subway from the domestic terminal to Hakata/Tenjin → hotel | Actual dated flight, baggage, terminal, check-in, and hotel route. If connecting after international arrival, follow the airport/airline arrival-transfer procedures. |
| **Narita (NRT)** | Domestic flight NRT → FUK → subway from the domestic terminal → hotel | Compare the dated same-airport flight and full baggage cost. Do not silently switch the departure to Haneda; changing airports requires its own ground transfer. |
| **Kyoto / Osaka** | Kyoto or Shin-Osaka → Tokaido/Sanyo Shinkansen to **Hakata**, direct or with a change as required → hotel | Hakata is the Fukuoka city Shinkansen anchor; check the actual service, luggage arrangements, and total fare. |
| **Hiroshima / Miyajima module** | Return to Hiroshima Station → Sanyo Shinkansen to Hakata → hotel | This is a western continuation after the island module; preserve its full island day and recount hotel nights. |
| **Tokyo city, rail alternative** | Tokyo/Shinagawa → Tokaido/Sanyo Shinkansen to Hakata, changing if required | Compare total travel time and price against flight plus airport access; it is a substantial transfer day. |

[JAL domestic search](https://www.jal.co.jp/jp/en/dom/reservation/) · [Peach route/schedule search](https://www.flypeach.com/en/lm/st/routemap) · [JR Central](https://global.jr-central.co.jp/en/) · [JR West](https://www.westjr.co.jp/global/en/). These are routes to compare, not verified date-specific flight or train availability.

**At Fukuoka Airport:** the **domestic terminal connects to the subway**. If arriving at the **international terminal**, compare its ground transport or the airport's shuttle to the domestic terminal before taking the subway. [Official airport access](https://www.fukuoka-airport.jp/en/access/). Choose the terminal shown on your itinerary; a pin at the airport is not the whole hotel transfer.

**Where to stay:** compare **Hakata** for rail arrival/departure and station food, or **Tenjin** for Daimyo shopping and the Nishitetsu Dazaifu start. No hotel quote has been obtained. Select the property by actual station exit, room/air-conditioning needs, total price, and cancellation terms. For a late yatai evening, check the last subway or budget a local taxi explicitly.

## Fit Fukuoka into 15 days / 14 nights

These alternatives leave the existing seasonal daily tables unchanged until you choose one. Counts refer to actual accommodation nights.

| Concept | Night count | What you give up / need to compare |
| --- | --- | --- |
| **Tokyo return, Fukuoka module** | Tokyo 4 → Fuji lakes 2 → Kyoto 3 → Fukuoka 3 → Tokyo 2 = **14** | Replaces three Kyoto nights. No Osaka overnight block; an Osaka day trip would replace one of the reduced Kyoto outings. FUK → Tokyo flight/transfer needs pricing. |
| **Osaka plus Fukuoka, departure via FUK** | Tokyo 4 → Fuji lakes 2 → Kyoto 3 → Osaka 2 → Fukuoka 3 = **14** | Reduces Kyoto and removes the final Tokyo return. Move Tamiya into the first Tokyo block. Compare the actual international itinerary from FUK, including connections; no direct long-haul departure is assumed. |

**Tokyo-return outline:** Days 1–6 unchanged Tokyo/Fuji → Day 7 Kyoto arrival → Days 8–9 choose two Kyoto outing blocks → Day 10 travel to Fukuoka / easy Hakata evening → Day 11 Ohori, tea, Tenjin/Daimyo, one yatai area → Day 12 Dazaifu OR Itoshima → Day 13 Tokyo return → Day 14 final shopping/packing → Day 15 international departure. Three Kyoto nights cannot preserve the six-night Kyoto sightseeing table.

If you want **Miyajima, Osaka, Fukuoka, Fuji, and a full Kyoto program**, compare more nights or explicitly remove other blocks; do not stack every chapter's alternative. The separate Fuji summit branch also needs a fresh count that retains its hut and recovery days. [[Japan 2027 — Best Islands|Island options]] · [[Japan 2027 — Osaka Chapter|Osaka alternatives]].

## Money and next decisions

Keep the shared **US$5,000 in-Japan ceiling**, excluding international flights. Requote hotels, the extra long-distance leg/domestic flights, bags, local transfers, and activities for the selected Fukuoka route. No actual Fukuoka quote establishes that it fits the existing allocations. Meals and purchases replace spending elsewhere; no new shopping allowance is added.

- [ ] Choose two, three, or four nights and the accommodation base.
- [ ] Pick Dazaifu versus Itoshima; include both only with enough actual days.
- [ ] Choose Tokyo return versus an international flight itinerary via FUK.
- [ ] Confirm year/dates and replaced Kyoto/Tokyo blocks before dated pocket cards.
- [ ] Check yatai operations, menus, queues, shop stock/measurements, and excursion return services.
- [ ] Record all actual prices and reservations in [[Japan 2027 — Seasonal Planning and Bookings]].

## Google Maps — sights shopping and transport

Tap the searches below and confirm the displayed place/branch before navigating. These are location searches, not saved offline maps, verified Place IDs, or live transport checks. Use operator timetables alongside Maps, particularly for Itoshima.

MAP_TABLE
'''

PLACES=[
('Arrival','Fukuoka Airport — domestic terminal','Fukuoka Airport Domestic Terminal'),
('Arrival','Fukuoka Airport — international terminal','Fukuoka Airport International Terminal'),
('Base','Hakata Station','Hakata Station Fukuoka'),
('Base','Tenjin subway station','Tenjin Subway Station Fukuoka'),
('Dazaifu rail','Nishitetsu Fukuoka (Tenjin)','Nishitetsu Fukuoka Tenjin Station'),
('Hakata history','Kushida Shrine','Kushida Shrine Fukuoka'),
('Hakata history','Tochoji Temple','Tochoji Temple Fukuoka'),
('Night photos','Nakasu river area','Nakasu Fukuoka'),
('Yatai area','Tenjin','Tenjin Yatai Fukuoka'),
('Yatai area','Nagahama','Nagahama Yatai Fukuoka'),
('Nature','Ohori Park','Ohori Park Fukuoka'),
('Nature','Maizuru Park','Maizuru Park Fukuoka'),
('Tea','Ohori Terrace / & LOCALS','Ohori Terrace AND LOCALS 1-9 Ohori Koen Fukuoka'),
('Indoor alternative','Fukuoka Art Museum','Fukuoka Art Museum Ohori'),
('Vintage area','Daimyo','Daimyo Fukuoka'),
('Collectibles','Mandarake Fukuoka','Mandarake Fukuoka 2-9-5 Daimyo'),
('Hobby shopping','THE GUNDAM BASE FUKUOKA, Canal City','THE GUNDAM BASE FUKUOKA Canal City Hakata'),
('Shopping','JR Hakata City','JR Hakata City Fukuoka'),
('Shopping','Canal City Hakata','Canal City Hakata Fukuoka'),
('Dazaifu outing','Dazaifu Station','Dazaifu Station Fukuoka'),
('Dazaifu outing','Dazaifu Tenmangu','Dazaifu Tenmangu Shrine'),
('Dazaifu outing','Kyushu National Museum','Kyushu National Museum Dazaifu'),
('Coastal outing','Sakurai Futamigaura','Sakurai Futamigaura Itoshima Fukuoka'),
('Coastal bus lead','Futamigaura PALMBEACH-mae','Futamigaura PALMBEACH bus stop Fukuoka'),
]
maps='| Use | Google Maps location |\n| --- | --- |\n'+'\n'.join('| '+category+' | ['+label+'](https://www.google.com/maps/search/?'+urlencode({'api':'1','query':query})+') |' for category,label,query in PLACES)
NOTES['Japan 2027 — Fukuoka Chapter.md']=NOTES['Japan 2027 — Fukuoka Chapter.md'].replace('MAP_TABLE',maps)

NOTES['Japan 2027 — Fukuoka Pocket Routes.md']='''# 🍜 Fukuoka — pocket routes

[[Japan 2027 — Fukuoka Chapter|← Full chapter, official sources, and Google Maps]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / reservations]]

**Undated cards:** proposed outing blocks, not calendar bookings or opening times. A three-night stay has an arrival day, two main outing days, and departure. Use Cards 1–3 in that order if arrival allows, reducing Card 1 when needed. Four nights can accommodate both Card 3 alternatives; with two nights, reduce the program.

## Card 1 — arrival, Hakata, and a relaxed evening

**Anchor:** hotel near Hakata or your selected city base.

| Block | Plan |
| --- | --- |
| Arrival | Airport → correct terminal transport/subway → hotel; or Hakata rail arrival → hotel. Confirm luggage arrangements. |
| If daylight and energy allow | Choose Kushida Shrine OR a short old-town walk; leave closed interiors for another day. |
| Optional browse | Canal City / Gundam Base only if enough time and current access suit; otherwise omit. |
| Dinner | Hakata ramen or another nearby meal. Nakasu photos are optional if you have energy and a return plan. |

**Food goal:** one ramen meal. **Shot:** station transition → architecture detail → first food scene. **Buy idea:** none required on arrival. **Fallback:** food, rest, and a short hotel-area walk. Do not force a late-arrival temple/shopping/yatai circuit.

- [ ] Arrival terminal/station, hotel route, and late check-in confirmed.
- [ ] No extra luggage-carrying sightseeing assumed before hotel arrangements.
- [ ] Tomorrow's main block and weather checked.

## Card 2 — Ohori tea, Daimyo shopping, and yatai

**Anchor:** Ohori Park → Tenjin/Daimyo → one dinner area.

| Block | Plan |
| --- | --- |
| Morning | Manageable Ohori pond walk; optional Maizuru extension if energy/weather suit. |
| Break | Ohori Terrace / & LOCALS tea or meal if open; use an alternative café when needed. |
| Afternoon | Daimyo clothes browsing plus Mandarake if collectibles matter; choose two browsing stops rather than shop everything. |
| Evening | Tenjin yatai for convenience OR Nakasu for river atmosphere. Confirm stall operations and check the menu/prices. |

**Food goal:** Yame tea and one yatai meal. **Buy idea:** one vintage garment OR collectible; packaged tea is an alternative gift. **Shot:** pond reflection → tea detail → clothing texture with permission → night street/river. **Rain alternative:** Fukuoka Art Museum if open, selected shopping, and an indoor dinner. **Summer adjustment:** shorten park walking and use seated/indoor breaks.

- [ ] Shop hours, condition, actual size, and total cost checked.
- [ ] Ask before filming inside the café/shop/stall.
- [ ] Last subway or paid taxi alternative settled before dinner.

## Card 3 — choose Dazaifu OR Itoshima

### A. Dazaifu — culture and a sweet

**Route:** Nishitetsu Fukuoka (Tenjin) → Nishitetsu Futsukaichi → Dazaifu Station → walk the approach. Allow for the walk between subway Tenjin and the Nishitetsu station if arriving by subway.

**Main block:** shrine approach and Dazaifu Tenmangu → lunch → freshly made umegaemochi. **Optional:** Kyushu National Museum if open and enough time remains. Check the shrine's current access notices; do not rely on old temporary-sanctuary photos. **Return:** verified Nishitetsu service, then hotel; hot-pot dinner optional after checking portion requirements and price.

**Shot:** approach wide view → permitted shrine detail → sweet close-up. **Buy idea:** one small packaged gift only after checking expiry/storage. **Rain adjustment:** museum plus a shorter shrine/approach visit when conditions suit, or replace with an indoor city day.

### B. Itoshima — coast and photography

**Route:** verify a Showa Bus West Coast Liner or another workable dated route to the Futamigaura area and back. Confirm your actual boarding/alighting stop; older Meotoiwa-mae listings may not match current service. Maps pins alone do not establish a bus journey.

**Main block:** one Futamigaura coastal area → meal/café → a short photo walk → return to the city. **Shot:** sea/torii wide scene → rock/water detail → walking transition. **Buy idea:** none required. **Sunset:** optional only when an actual return service or separately arranged ride supports it. **Bad-weather alternative:** city cafés/art/shopping or Dazaifu when appropriate.

- [ ] Pick A or B; do not combine them in one day.
- [ ] Opening/access notices and actual outward/return connections checked.
- [ ] Daylight/weather and meal options fit the chosen transport.
- [ ] Any taxi, tour, car, museum, or shopping cost fits the shared budget.

**Departure day:** hotel → Hakata or the correct Fukuoka Airport terminal with a reliable buffer. No last-minute excursion is scheduled before the onward train/flight. For Tokyo-return routes, the separate Tokyo hotel nights remain part of the 14-night count.
'''

LINKS={
 'Japan 2027 — Start Here.md':'**Fukuoka chapter:** [[Japan 2027 — Fukuoka Chapter|Food, yatai, shopping, sightseeing, airport access, and Maps]] · [[Japan 2027 — Fukuoka Pocket Routes|Three flexible pocket routes]].',
 'Japan 2027 — Seasonal Guides.md':'**Fukuoka option:** [[Japan 2027 — Fukuoka Chapter]] compares a three-night Kyushu-city module, with summer/November/May adaptations and explicit 14-night route alternatives.',
 'Japan 2027 — Summer Guide.md':'**Fukuoka alternative:** [[Japan 2027 — Fukuoka Chapter|Yatai, tea, vintage browsing, and coast/culture choices]]. Adding the city replaces other nights; the current summer outline remains unchanged.',
 'Japan 2027 — Autumn Guide.md':'**Fukuoka alternative:** [[Japan 2027 — Fukuoka Chapter|City food, park photography, and hot-pot dinners]]. Compare its route tradeoffs before reducing Kyoto foliage time; future events and colors remain unconfirmed.',
 'Japan 2027 — November vs May.md':'**Fukuoka comparison:** [[Japan 2027 — Fukuoka Chapter]] adapts city walks, food, and a Dazaifu/coastal outing to November or May without assuming annual conditions or events.',
 'Japan 2027 — Osaka Chapter.md':'**Next city to compare:** [[Japan 2027 — Fukuoka Chapter|Fukuoka]] — rail onward to Hakata, three-night food/culture option, and explicit route changes.',
 'Japan 2027 — Seasonal Planning and Bookings.md':'**Fukuoka route decision:** [[Japan 2027 — Fukuoka Chapter|Tokyo-return versus departure-via-FUK alternatives]]. Requote transport/hotels and identify replaced nights before booking; no extra allowance or reservation added.',
 'Japan Travel Guide 2027.md':'**Fukuoka research chapter:** [[Japan 2027 — Fukuoka Chapter]] · [[Japan 2027 — Fukuoka Pocket Routes]]. A separate regional option; no dated blossom days have been changed.',
}

def validate(root,manifest):
    for name in manifest:
        s=(root/name).read_text();assert s.startswith('# '),name
        for target in re.findall(r'\[\[([^\]|#]+)',s):
            assert target+'.md' in manifest or (V/(target+'.md')).exists(),(name,target)
    assert (root/'Japan 2027 — Fukuoka Chapter.md').read_text().count('https://www.google.com/maps/search/?')==24
    assert sum([4,2,3,3,2])==14 and sum([4,2,3,2,3])==14
    for name in ['Japan 2027 — Summer Guide.md','Japan 2027 — Autumn Guide.md']:
        assert all(re.search(r'\| '+str(day)+r' /',(root/name).read_text()) for day in range(1,16))

if '--install' in sys.argv:
    manifest=json.loads((W/'manifest.json').read_text())
    for name,h in manifest.items():
        p=V/name;assert not p.exists() if h is None else hashlib.sha256(p.read_bytes()).hexdigest()==h,name
    validate(W/'staged',manifest)
    (W/'backup').mkdir(exist_ok=True)
    for name,h in manifest.items():
        if h is not None:shutil.copy2(V/name,W/'backup'/name)
        shutil.copy2(W/'staged'/name,V/name)
    validate(V,manifest)
    assert all((V/name).read_bytes()==(W/'staged'/name).read_bytes() for name in manifest)
    print('Saved Fukuoka chapter, three pocket routes, 24 Maps links, airport/rail access, and eight guide integrations; links, night counts, and existing 15-day outlines verified. Originals backed up.')
else:
    (W/'staged').mkdir(parents=True,exist_ok=True);manifest={}
    for name,s in NOTES.items():
        assert not (V/name).exists(),name
        (W/'staged'/name).write_text(s);manifest[name]=None
    for name,line in LINKS.items():
        original=(V/name).read_bytes();manifest[name]=hashlib.sha256(original).hexdigest()
        s=original.decode();i=s.index('\n')+1
        (W/'staged'/name).write_text(s[:i]+'\n'+line+'\n'+s[i:])
    (W/'manifest.json').write_text(json.dumps(manifest));validate(W/'staged',manifest)
    print('Prepared Fukuoka chapter, three pocket routes, 24 Maps links, and eight integrations; references, 14-night alternatives, and existing outlines validated.')
