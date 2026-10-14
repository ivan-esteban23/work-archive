from pathlib import Path
from urllib.parse import urlencode
import hashlib, json, re, shutil, sys

V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
W = Path('/home/ivanaguilera/Work/japan-guide-update/sapporo')
NOTES = {}
NOTES['Japan 2027 — Sapporo Chapter.md'] = '''# 🌿 Japan 2027 — Sapporo chapter

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Sapporo Pocket Routes|Four pocket routes]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and bookings]]

[[#Google Maps — sights shopping and transport|📍 Google Maps]] · [[#Foods to try|🍜 Food]] · [[#Getting here — Haneda Narita and Kansai|🛬 Getting here]]

**Research checked:** 7 October 2026. **Working year:** 2027, unconfirmed. This chapter is an optional Hokkaido module. Dates, hotels, flights, restaurants, stock, and travel-day opening times are not confirmed. Recommendations below reflect your photography, food, clothes, hobby browsing, gifts, and outdoor interests.

## My starting recommendation

Start with **three nights**: arrival and a short central evening → Sapporo city day → Otaru day trip → departure. Choose **four nights** if you also want Jozankei hot springs or a separate Moerenuma photography day. Three nights give two full outing days, not three. Four nights are my preferred summer version if reducing another base feels worthwhile.

Sapporo is a Hokkaido base, substantially separate from your Kansai and Kyushu options. Compare it with [[Japan 2027 — Fukuoka Chapter|Fukuoka]] as another regional choice; do not automatically add both to the same 14 nights. Keep Fuji as its own scenic/summit decision.

## Which season suits your guide?

| Your option | What changes here | My recommendation |
| --- | --- | --- |
| **Summer, especially July / early August** | Park walks, outdoor photography, and longer daylight; temperatures and rain still vary | Best first fit for this chapter. Compare four nights, while retaining breaks and a rain alternative. |
| **Second half of May** | Hokkaido is still in spring; lilacs are a better seasonal lead than assuming Tokyo/Kyoto warmth or cherry blossom timing | Good second choice for city food, Otaru, and spring greenery. Pack layers; check actual flowering. |
| **Mid / late November** | Your proposed Kyoto foliage trip occurs later than Sapporo's usual city foliage window | Choose Sapporo for food and a colder city visit; keep Kyoto time if autumn colors are the main goal. |
| **A future winter trip** | Snow experiences require a separate winter plan and current conditions | Snow Festival is normally early February; it does not belong to the summer/May/November itinerary. |

This ranking is my planning judgment. The [official summer guide](https://visit.sapporo.travel/seasons/summer/) describes summer outdoor options; the [spring guide](https://visit.sapporo.travel/seasons/spring/) places average cherry flowering around late April/early May and lilacs in May. Neither establishes 2027 peak dates or festival dates.

The [official autumn guide](https://visit.sapporo.travel/seasons/autumn/) gives **mid-October to early November** for city foliage. That is a general window, not a forecast or a guarantee that Jozankei and city trees peak together. The [winter guide](https://visit.sapporo.travel/seasons/winter/) describes winter roughly December–March, February's Snow Festival, and illuminations usually beginning in late November. Check future event announcements separately; November does not guarantee established ski conditions or festival snow scenes.

## Explore by area

| Area | Your reason to explore | Suggested use |
| --- | --- | --- |
| **Sapporo Station / Odori** | Arrival convenience, park and city architecture | Base near the station for rail days, or Odori for central walks; compare actual hotel quotes |
| **Tanukikoji / Susukino** | Covered shopping, collectibles, ramen, evening street photos | One shopping block and a selected dinner; no compulsory nightlife crawl |
| **Maruyama / Hokkaido Shrine** | Green spaces and shrine setting | City-day morning; park walking is the default outdoor activity |
| **Nakajima Park** | A quieter park-photo alternative | Substitute for another park when you want a slower day |
| **Hokkaido University** | Tree-lined campus and seasonal photography | Optional station-area walk on public visitor routes; respect teaching/research spaces |
| **Mt. Moiwa** | City panorama | Optional clear-weather ropeway evening, chosen instead of a long extra dinner/shopping circuit |
| **Otaru** | Canal, historic streets, sweets, craft browsing | A separate rail day trip |
| **Jozankei / Moerenuma** | Hot-spring relaxation OR landscape/art photography | Fourth-night extension: choose one outing |

Use the [city's first-visit walking itinerary](https://visit.sapporo.travel/itineraries/02/) for central orientation and the [official attraction directory](https://www.sapporo.travel/en/facility/) to select sights. The table is a suggested grouping, not a promise that every stop fits a single day. [Tanukikoji city listing](https://www.sapporo.travel/spot/facility/tanukikoji_shopping_arcade/).

### Outdoor views and photography

**Mt. Moiwa:** start by comparing a ropeway visit, rather than assign a summit hike without knowing your preferred effort. Check the [operator's current notices](https://mt-moiwa.jp/) and [access map](https://mt-moiwa.jp/access/map/) for the streetcar/shuttle/walking connection, operation, tickets, and final descent. A map pin at the lower station is not a complete ascent. Choose a clear forecast; keep dinner/shop plans flexible.

**Moerenuma Park:** Isamu Noguchi's landscape design, geometric landforms, and the Glass Pyramid make this my strongest optional architecture/photo outing. Reach the park using the operator's described **Toho subway to Kanjodori-Higashi → Chuo Bus to the appropriate park entrance** route, then verify the dated bus timetable and return. Entrance access and facilities change seasonally. Check the actual fountain schedule before planning a fountain shot; the current English page carries operating restrictions. [Park design, transport, and facilities](https://moerenumapark.jp/english/).

**Filming sequence:** a central street establishing shot → park/architecture detail → permitted food preparation or meal close-up → Otaru waterfront movement → city lights. Ask before recording inside shops, restaurants, shrine interiors, or museums. Moerenuma publishes photography/video requirements on its English page; consult those for a planned shoot. A small personal camera does not establish permission for every use.

## Foods to try

My first two priorities are **miso ramen** and **soup curry**, followed by **jingisukan** if grilled lamb appeals to you. Use Otaru for a seafood lunch and a sweet rather than schedule every specialty on arrival.

| Food | What to expect | Where I would put it |
| --- | --- | --- |
| **Sapporo miso ramen** | Ramen with a miso-based broth; toppings vary | Arrival evening or city lunch; Ramen Yokocho is one browsing lead |
| **Soup curry** | Spiced broth with substantial vegetables and optional meat | City-day lunch; choose spice level and ingredients from the actual menu |
| **Jingisukan** | Grilled lamb/mutton | One dinner; compare portions, cooking format, and price before committing |
| **Seafood / kaisendon** | Fish or seafood over rice; ingredients vary | Nijo Market or Otaru lunch after looking at the displayed menu |
| **Sweets and a café break** | Choose a pastry, chocolate, or local dessert you actually want | Otaru sweet stop or Shiroi Koibito Park as an alternative outing |

[Official city food portal](https://quruquru.sapporo.travel/en/list/?id=2%2F) · [City explanation of ramen and soup curry](https://visit.sapporo.travel/seasons/winter/) · [Nijo and Curb Market visitor guide](https://www.sapporo.travel/en/spot/feature/sapporo-nijo-market-curb-market/). Seafood prices and availability vary; this is not a quoted crab/uni meal or a restaurant reservation.

**Sapporo Beer Museum / Beer Garden:** optional history and a separate meal/tasting decision. The museum and nearby restaurant are not one automatic booking, and the actual brewery in Eniwa is a different location. Older guides describe free self-guided admission; the [current Japanese visitor page](https://www.sapporobeer.jp/brewery/s_museum/kengaku/) lists paid admission. Use the [current English operator page](https://www.sapporobeer.jp/english/brewery/s_museum/) and dated booking information before budgeting; do not rely on an old free-entry assumption. No alcohol or museum visit is required for this route.

For an izakaya evening, use **Susukino as an area lead**, then pick a menu, seating arrangement, and total price closer to travel. It is not a verified individual-restaurant shortlist or a new ranking against Osaka/Tokyo.

## Shopping, perfume browsing, and gifts

| Lead | What to browse | Current source / limitation |
| --- | --- | --- |
| **Tanukikoji arcade** | A compact clothing/accessory or practical souvenir browse | [Official city listing](https://www.sapporo.travel/spot/facility/tanukikoji_shopping_arcade/). Area lead; no exact vintage inventory or size confirmed. |
| **Mandarake Sapporo** | Used toys, collectibles, models, discs, and games | **nORBESA 2F, 1-1 Minami 3-jo Nishi 5-chome, Chuo-ku.** [Official branch](https://www.mandarake.co.jp/dir/spr/). Inspect condition and actual stock; no Tamiya item promised. |
| **Sapporo PARCO** | Tees, shirts, trousers, denim or an accessory; compare current tenants | [Official shop list](https://sapporo.parco.jp/shop/?category_search=category). For her, look for Y2K/Korean-inspired pieces she would enjoy; no 2027 trend forecast or size guarantee. |
| **NOSE SHOP at PARCO** | Fragrance testing as a lead for her gift | Listed in the [current first-floor guide](https://sapporo.parco.jp/floor/detail/?f=1f&ft=type1). Confirm branch/brands, available testers, and small formats closer to travel. |
| **Shiroi Koibito Park** | Sweets, shop browsing, café, optional paid experiences | [Operator's English guide](https://www.shiroikoibitopark.jp/en/). An alternative half-day activity; do not force it into the city/Otaru core. |
| **Otaru craft-shopping streets** | One small craft or decorative gift after seeing it in person | [Otaru tourist association](https://otaru.gr.jp/). Treat shop pins and inventories as separate checks. |

Your **L tops / EU 44–46 trousers** are starting references; try on or compare garment measurements. Her size remains unknown, so a small accessory is easier to choose than fitted clothes. Fragrance preferences remain unknown too: test first and compare a small format if offered; a fashion preference does not establish a scent preference. Your Tokyo Tamiya visit remains the specific Tamiya anchor.

### Souvenir shortlist

1. **For her: Shiroi Koibito or another clearly labeled packaged sweet.** Compare a small box at the park/shop, with ingredients, expiry, and storage checked. [Park's official shop overview](https://www.shiroikoibitopark.jp/en/).
2. **For you or her: ROYCE' Pure Chocolate or a packaged alternative.** The [manufacturer's product guide](https://www.royce.com/contents/english_product/) distinguishes storage needs. Pure Chocolate is listed at **25°C or below**; it still needs protection from summer heat. **Nama Chocolate requires 10°C or below**, so choose it only with a workable cold-storage/transport plan. Some varieties contain liquor; choose by the label.
3. **Enjoy LeTAO Double Fromage locally instead of assuming it is a suitcase gift.** The [manufacturer's product page](https://www.letao.jp/category/DOUBLE_FROMAGE/F011.html) lists frozen storage. Check café servings in Otaru; for travel, compare another product whose printed storage instructions suit your journey.
4. **One compact accessory or collectible.** Choose by personal appeal, condition, weight, and price. A new city does not create another shopping allowance.

Her choices remain within the existing **US$200 gift cap**, with the relationship to your **US$300 shopping/miscellaneous allowance** still open. If included in that US$300, up to US$100 remains for your other shopping. If additional within the US$5,000 envelope, the existing planning scenario is US$4,300 planned / US$700 reserve. Count a perfume, sweets, or fashion purchase once. [[Japan 2027 — Gifts for Her|Gift plan]] · [[Japan 2027 — Shopping Shortlist|Personal shortlist]].

## Otaru day trip

**Route:** Sapporo Station → a dated JR service to **Otaru Station** → walk the central area → JR back to Sapporo. Confirm whether your service is direct or needs a change. Use [JR Hokkaido's Sapporo/Otaru service information](https://www.jrhokkaido.co.jp/global/english/travel/airport.html) and the [Otaru tourist association](https://otaru.gr.jp/) for updated visitor information.

My day: **canal and warehouse-area photos → seafood lunch → Sakaimachi-area browsing → one café/sweet → return**. The canal and Sakaimachi shopping area are separate walking blocks; cut shopping if your pace or weather requires. Otaru's historic harbor/warehouse character is described by [Hokkaido's official tourism guide](https://en.visit-hokkaido.jp/adventure-travel/traveltrade-press/destinations/otaru/).

Blue-hour canal photos are optional. Check that the actual return train, shop closures, and dinner plan support a later stay. No canal cruise, glass workshop, music-box purchase, or specific café seat has been booked.

## Jozankei hot springs — fourth-night choice

**Route:** central Sapporo → **Jotetsu Kappa Liner** or another confirmed bus → your selected Jozankei stop → short town/river walk and a selected day-use bath → bus back. Compare the [tourist association's access page](https://jozankei.jp/en/access/) with the [operator's multilingual transport page](https://www.jotetsu.co.jp/bus/global/index.html) for the actual boarding point, timetable, booking requirements, and return. Reserve the Kappa Liner when required; do not substitute an old bus-stop screenshot for a confirmed seat.

Choose the bathing facility first: check day-use admission, last entry, closures, towels, and house rules, then coordinate the bus. Use the [association's hot-spring listings](https://jozankei.jp/en/) to compare options. River walks depend on weather/access. Autumn viewpoints and seasonal shuttles need a dated check; the [official foliage program](https://jozankei.jp/en/godaikoyo/) is a planning lead, not confirmation of 2027 bus operation or peak colors.

This is a separate outing from Otaru. A Jozankei overnight would replace a Sapporo hotel night and change luggage/transfers; it has not been added. Furano/Biei, Hakodate, and Niseko would need their own wider Hokkaido route rather than extra compulsory day trips in this short chapter.

## Getting here — Haneda, Narita, and Kansai

**Default airport: New Chitose (CTS).** Search the exact airport code: Sapporo's **Okadama (OKD)** is a different airport and is not the arrival used in this chapter.

| Starting point | Route to compare | Before choosing |
| --- | --- | --- |
| **Haneda (HND)** | Domestic flight HND → CTS → airport rail to Sapporo → hotel | Same-airport terminal transfer, actual connection time, baggage rules, and check-in deadline |
| **Narita (NRT)** | Compare a direct NRT → CTS flight on your date → rail to Sapporo | Availability, airline/terminal, fare with baggage, and international-to-domestic connection rules; do not assume a transfer to HND is needed |
| **Kyoto / Osaka** | Hotel → selected Kansai airport, such as ITM or KIX → CTS → Sapporo | Compare the full hotel-to-hotel journey; ITM and KIX are different airports |
| **International arrival directly at CTS** | Clear arrival formalities → follow signs toward domestic-terminal airport rail station → Sapporo | Correct terminal walking route and late-arrival train options |
| **Sapporo back to Tokyo** | Sapporo → CTS → selected Tokyo airport → final Tokyo hotel | Retain the planned Tokyo buffer nights; do not attach a day trip before the flight |

Use [JAL's domestic route map/timetables](https://www.jal.co.jp/jp/en/dom/route/index.html) and [Peach's route map](https://www.flypeach.com/en/lm/st/routemap) to compare dated service. These are research tools, not held flights or confirmed 2027 schedules. Avoid a same-day cross-airport transfer without accounting for the entire ground journey and connection rules.

**CTS → city:** [JR Hokkaido's airport guide](https://www.jrhokkaido.co.jp/global/english/travel/airport.html) describes Airport train services to Sapporo and Otaru; select the actual train/destination. The station is reached from the domestic terminal basement, including a terminal walk when arriving internationally. [JR airport terminal map](https://www.jrhokkaido.co.jp/global/pdf/e-chitose.pdf). Do not equate flight landing time with reaching the station platform. Within the city, compare subway/walking connections to your hotel; station-area and Odori bases serve different priorities.

## Fit it into 15 days / 14 nights

These are **alternatives**, not additions to the existing dated cherry-blossom cards or a commitment to three separate trips.

| Alternative | Nights | Tradeoff |
| --- | --- | --- |
| **Three-night Sapporo module** | Tokyo 4 → Kawaguchiko 2 → Kyoto 3 → Sapporo 3 → Tokyo 2 = **14** | City + Otaru; replaces three Kyoto nights in the default seasonal outline. No separate Jozankei day. |
| **Four-night summer preference** | Tokyo 4 → Kawaguchiko 2 → Kyoto 2 → Sapporo 4 → Tokyo 2 = **14** | Adds Jozankei OR Moerenuma, but Kyoto gets only one full non-transfer day. Choose knowingly. |
| **Hokkaido-focused alternative** | Tokyo 4 → Kawaguchiko 2 → Sapporo 6 → Tokyo 2 = **14** | Omits Kyoto/Osaka; permits slower Sapporo and separate day trips. A wider regional circuit still needs fresh routing. |

All versions retain your scenic Fuji option, not an automatic summit climb. For November foliage, my starting choice remains more Kyoto time rather than the four-night Sapporo route. Requote domestic flights, airport ground travel, rail/bus day trips, hotels, and activities within the **US$5,000 in-Japan ceiling**. The US$400 intercity planning allocation is not evidence these flights fit. Compare total trip cost before selecting a route. No new city shopping allowance or hotel quote has been introduced.

## Google Maps — sights, shopping, and transport

Search links below are orientation pins, not saved offline routes, booked transport, or proof of stock/access. Check the actual entrance/address and your dated journey in Maps and with the operator.

MAP_TABLE

## Next booking checks

- [ ] Choose three nights or four; identify exactly which other nights they replace.
- [ ] Choose season and check local forecast, daylight, foliage/flower updates, and event dates.
- [ ] Compare HND/NRT or Kansai → CTS and CTS → Tokyo with baggage and all airport legs included.
- [ ] Choose station-area or Odori hotel by actual quote and cancellation terms.
- [ ] Select city + Otaru; only add Jozankei OR Moerenuma when a fourth night exists.
- [ ] Check ropeway, museum, shops, day-use bath, and dated return transport.
- [ ] Check gift size/preferences, product storage, and the shared shopping cap.

[[Japan 2027 — Sapporo Pocket Routes|Open the compact route cards]] · [[Japan 2027 — Fukuoka Chapter|Compare Fukuoka]] · [[Japan 2027 — Osaka Chapter|Compare Osaka]]
'''

PLACES = [
('Airport', 'New Chitose Airport (CTS)', 'New Chitose Airport CTS Hokkaido'),
('Airport rail', 'New Chitose Airport Station', 'New Chitose Airport Station JR Hokkaido'),
('Rail base', 'Sapporo Station', 'Sapporo Station Hokkaido'),
('City transport', 'Odori Station', 'Odori Station Sapporo'),
('Dinner / nightlife area', 'Susukino', 'Susukino Sapporo'),
('Park / city photos', 'Odori Park', 'Odori Park Sapporo'),
('City architecture', 'Sapporo TV Tower', 'Sapporo TV Tower'),
('City architecture', 'Sapporo Clock Tower', 'Sapporo Clock Tower'),
('Park alternative', 'Nakajima Park', 'Nakajima Park Sapporo'),
('Campus / seasonal walk', 'Hokkaido University', 'Hokkaido University Sapporo'),
('Nature', 'Maruyama Park', 'Maruyama Park Sapporo'),
('Shrine', 'Hokkaido Shrine', 'Hokkaido Shrine Sapporo'),
('Panorama access', 'Mt. Moiwa Ropeway lower station', 'Mount Moiwa Ropeway Sanroku Station Sapporo'),
('History / optional tasting', 'Sapporo Beer Museum', 'Sapporo Beer Museum Kita 7 Higashi 9'),
('Food', 'Nijo Market', 'Nijo Market Sapporo'),
('Food', 'Ganso Sapporo Ramen Yokocho', 'Ganso Sapporo Ramen Yokocho Susukino'),
('Shopping', 'Tanukikoji arcade', 'Tanukikoji Shopping Street Sapporo'),
('Collectibles', 'Mandarake Sapporo, nORBESA 2F', 'Mandarake Sapporo nORBESA Minami 3 Nishi 5'),
('Fashion / fragrance browse', 'Sapporo PARCO', 'Sapporo PARCO'),
('Sweets / alternative outing', 'Shiroi Koibito Park', 'Shiroi Koibito Park Sapporo'),
('Art / outdoor outing', 'Moerenuma Park', 'Moerenuma Park Sapporo'),
('Architecture', 'Moerenuma Glass Pyramid', 'Moerenuma Park Glass Pyramid HIDAMARI'),
('Park transport', 'Kanjodori-Higashi Station', 'Kanjodori Higashi Station Sapporo'),
('Otaru rail', 'Otaru Station', 'Otaru Station Hokkaido'),
('Otaru photos', 'Otaru Canal', 'Otaru Canal Hokkaido'),
('Otaru browsing', 'Sakaimachi shopping street', 'Otaru Sakaimachi Street Hokkaido'),
('Onsen outing orientation', 'Jozankei Tourist Information Center', 'Jozankei Tourist Information Center Sapporo'),
]
maps = '| Use | Google Maps location |\n| --- | --- |\n' + '\n'.join(
    '| ' + category + ' | [' + label + '](https://www.google.com/maps/search/?' + urlencode({'api': '1', 'query': query}) + ') |'
    for category, label, query in PLACES)
NOTES['Japan 2027 — Sapporo Chapter.md'] = NOTES['Japan 2027 — Sapporo Chapter.md'].replace('MAP_TABLE', maps)

NOTES['Japan 2027 — Sapporo Pocket Routes.md'] = '''# 🌿 Sapporo — pocket routes

[[Japan 2027 — Sapporo Chapter|← Full chapter, sources, transport, and Google Maps]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / reservations]]

**Undated cards:** arrival + two full outing days + departure for three nights. Use Cards 1–3, adapting arrival to the actual flight. Add Card 4 only with a fourth night; choose its A or B outing. These cards do not change the 15 dated spring cards or establish shop opening times.

## Card 1 — arrive, settle in, first Sapporo meal

**Anchor:** CTS → JR airport train → Sapporo Station → selected hotel, or the equivalent confirmed city connection.

| Block | Plan |
| --- | --- |
| Arrival | Correct terminal → baggage/arrival formalities → airport rail → hotel. Confirm luggage/check-in arrangements. |
| If daylight and energy allow | Short Odori or hotel-area walk; do not attempt the whole sightseeing circuit. |
| Dinner | Miso ramen or another nearby meal; Ramen Yokocho only if convenient and open. |
| Optional evening | A short Susukino street-photo walk with a planned return. |

**Food:** one ramen meal. **Shot:** arrival transition → city grid → food close-up with permission. **Buy:** none required. **Late-arrival fallback:** hotel-area dinner and rest.

- [ ] CTS airport code, terminal, final usable train, and hotel connection checked.
- [ ] Tomorrow's weather and city block chosen.

## Card 2 — green Sapporo, soup curry, and shopping

**Anchor:** Maruyama / shrine → central lunch → Tanukikoji / one shop → chosen evening.

| Block | Plan |
| --- | --- |
| Morning | Maruyama Park and permitted Hokkaido Shrine areas; keep it a manageable park walk. |
| Lunch | Soup curry; choose ingredients and spice level. |
| Afternoon | Tanukikoji plus Mandarake OR PARCO. Choose a priority rather than force every shop. |
| Evening | Jingisukan / izakaya-style dinner OR a clear-weather Mt. Moiwa ropeway visit followed by a simpler meal. |

**Shot:** green canopy → shrine exterior → texture/collectible with permission → city lights. **Buy:** one garment/accessory OR collectible within the existing cap. If comparing NOSE SHOP perfumes, test before considering a small format; her preferences remain open.

**Rain alternative:** selected central shopping and a café; Beer Museum only after checking admission/opening. **May adjustment:** layers and actual flower conditions. **November adjustment:** shorter outdoor blocks and actual daylight; no foliage guarantee. **Summer adjustment:** hydration, seated breaks, and shade when needed.

- [ ] Selected shops and dinner menu/price checked; actual measurements before buying clothes.
- [ ] Ropeway operations, access, final descent, and weather checked if chosen.
- [ ] Ask before indoor filming; do not automatically film other diners.

## Card 3 — Otaru, canal photos, seafood, and one sweet

**Route:** Sapporo Station → dated JR train to Otaru Station → central walking blocks → JR return. Confirm direct service or transfer, and final return suitable for your evening.

| Block | Plan |
| --- | --- |
| Morning | Canal / warehouse-area walk and photos. |
| Lunch | Seafood or another suitable meal after checking the menu. |
| Afternoon | Sakaimachi-area craft browsing, then one café/sweet. |
| Return | Train back to Sapporo; a relaxed dinner near the hotel. |

**Shot:** canal wide → warehouse detail → street movement → dessert. **Buy:** one compact craft OR packaged sweet; do not assume a frozen cheesecake can travel unrefrigerated. **Blue hour:** optional only if return transport, weather, and shop closures fit. **Fallback:** shorten walking and use cafés/shops; change to an indoor city day if conditions make the outing unsuitable.

- [ ] Rail route/return and a realistic walking loop checked.
- [ ] Ingredients, expiry, and storage reviewed for edible gifts.
- [ ] No cruise, workshop, café reservation, or craft purchase assumed.

## Card 4 — fourth-night extension: choose A OR B

### A. Jozankei — hot springs and a short river walk

**Route:** selected city boarding point → reserved Kappa Liner when required or a verified alternative bus → correct Jozankei stop → return bus. Confirm both directions before departure.

**Main block:** a short town/river walk → lunch → preselected day-use bath → return. Choose the bathing facility and check access, hours, last entry, towels, and rules before settling the bus plan. No Jozankei overnight is counted.

**Shot:** town/river exterior details; no bath photography. **Buy:** optional compact souvenir only. **Fallback:** an indoor Sapporo day if transport, access, or weather does not work. Autumn-color scenes are conditional, especially in November.

### B. Moerenuma — landscape and architecture

**Route lead:** Toho subway → Kanjodori-Higashi → dated Chuo Bus to the appropriate Moerenuma entrance → return. Consult the park's current access information; check entrance changes and the last workable return.

**Main block:** manageable park loop → geometric landscape / Glass Pyramid if open → break → city return. Check fountain operations before assigning a fountain shot; its schedule is seasonal and can carry restrictions.

**Shot:** wide landform → geometric detail → walking transition → permitted pyramid interior. **Buy:** none required. **Fallback:** central architecture/café/shopping when wind, rain, facility closure, or bus service limits the outing.

- [ ] Choose A or B; do not schedule both with Otaru on one day.
- [ ] Dated transport, facility opening, and total outing cost checked.
- [ ] Planned filming fits facility rules.

**Departure:** hotel → CTS → onward flight, with baggage/check-in buffers. Keep excursions off the flight day. The Tokyo-return route separately retains its two Tokyo nights before international departure.
'''

LINKS = {
    'Japan 2027 — Start Here.md': '**Sapporo chapter:** [[Japan 2027 — Sapporo Chapter|Food, parks, shopping, Otaru/Jozankei, airport access, and Maps]] · [[Japan 2027 — Sapporo Pocket Routes|Four flexible pocket routes]].',
    'Japan 2027 — Seasonal Guides.md': '**Sapporo option:** [[Japan 2027 — Sapporo Chapter]] compares three/four nights, with summer, May spring, and November tradeoffs plus explicit 14-night alternatives.',
    'Japan 2027 — Summer Guide.md': '**Sapporo alternative:** [[Japan 2027 — Sapporo Chapter|Summer parks, food, Otaru, and an optional fourth-night outing]]. Compare replaced nights and domestic flight costs before selecting it.',
    'Japan 2027 — Autumn Guide.md': '**Sapporo comparison:** [[Japan 2027 — Sapporo Chapter|Hokkaido city food and seasonal timing]]. Usual city foliage is mid-October to early November; a mid/late-November module trades away Kyoto time without guaranteeing northern colors.',
    'Japan 2027 — November vs May.md': '**Sapporo comparison:** [[Japan 2027 — Sapporo Chapter]] treats late May as Hokkaido spring and mid/late November as a colder city-food option; flowering and foliage need local dated checks.',
    'Japan 2027 — Fukuoka Chapter.md': '**Next regional comparison:** [[Japan 2027 — Sapporo Chapter|Sapporo / Hokkaido]] — summer parks, Otaru, and optional hot springs. Choose regional nights deliberately before combining Kyushu and Hokkaido.',
    'Japan 2027 — Seasonal Planning and Bookings.md': '**Sapporo route decision:** [[Japan 2027 — Sapporo Chapter|Three-night, four-night, or Hokkaido-focused alternatives]]. Requote CTS flights, airport legs, day trips, and replaced hotel nights within the existing budget.',
    'Japan Travel Guide 2027.md': '**Sapporo research chapter:** [[Japan 2027 — Sapporo Chapter]] · [[Japan 2027 — Sapporo Pocket Routes]]. An optional Hokkaido module; existing dated blossom days remain the original route.',
}

def validate(root, manifest):
    for name in manifest:
        s = (root / name).read_text()
        assert s.startswith('# '), name
        assert 'MAP_TABLE' not in s, name
        for target in re.findall(r'\[\[([^\]|#]+)', s):
            assert target + '.md' in manifest or (V / (target + '.md')).exists(), (name, target)
    chapter = (root / 'Japan 2027 — Sapporo Chapter.md').read_text()
    assert chapter.count('https://www.google.com/maps/search/?') == len(PLACES) == 27
    assert all(sum(route) == 14 for route in ([4, 2, 3, 3, 2], [4, 2, 2, 4, 2], [4, 2, 6, 2]))
    cards = (root / 'Japan 2027 — Sapporo Pocket Routes.md').read_text()
    assert len(re.findall(r'^## Card [1-4] ', cards, re.M)) == 4
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
    print('Saved Sapporo chapter, four pocket routes, 27 Maps links, and eight integrations. Links, 14-night counts, and existing 15-day outlines verified; originals backed up.')
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
        (W / 'staged' / name).write_text(s[:i] + '\n' + line + '\n' + s[i:])
    (W / 'manifest.json').write_text(json.dumps(manifest))
    validate(W / 'staged', manifest)
    print('Prepared Sapporo chapter, four pocket routes, 27 Maps links, and eight integrations. References, 14-night alternatives, and existing outlines validated.')
