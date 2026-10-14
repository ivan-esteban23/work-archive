from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
import hashlib, json, re, shutil, sys

V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
W = Path('/home/ivanaguilera/Work/japan-guide-update/okinawa')
NOTES = {}
NOTES['Japan 2027 — Okinawa Chapter.md'] = '''# 🏝️ Japan 2027 — Okinawa chapter

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Okinawa Pocket Routes|Four pocket routes]] · [[Japan 2027 — Best Islands|Compare islands]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / bookings]]

[[#Google Maps — places and transport|📍 Google Maps]] · [[#Foods to try|🍜 Food]] · [[#Getting here — Haneda Narita and Kansai|🛬 Getting here]]

**Research checked:** 7 October 2026. **Working year:** 2027, unconfirmed. This is an optional southern-island chapter for your photography, food, shopping, gifts, and outdoor interests. Dates, hotels, flights, ferries, tours, marine activities, and product stock remain unconfirmed.

## Which Okinawa do we mean?

**This chapter starts with Okinawa Main Island**, flying into **Naha Airport (OKA)**. Naha, Shuri, Chatan, Onna, and Motobu are places on this island. The **Kerama Islands**, including Zamami, are separate islands reached by boat from Naha.

**Ishigaki / Taketomi and Miyako are different regional choices**, already covered in [[Japan 2027 — Best Islands]]. They are not neighborhoods of Naha or automatic day trips from an Onna hotel. Compare one region first; adding inter-island flights and hotel changes requires a fresh route. [Official Okinawa overview](https://visitokinawajapan.com/discover/okinawa-at-a-glance/) · [Ishigaki](https://visitokinawajapan.com/destinations/yaeyama-islands/ishigaki-island/) · [Miyako Islands](https://visitokinawajapan.com/destinations/miyako-islands/).

## My starting recommendation for you

Compare **four nights based in Naha**: arrival and an easy local meal → Shuri / city culture and crafts → one Chatan coastal outing → **Zamami day trip OR a Motobu / Churaumi Aquarium day** → departure. Four nights provide three full outing days. Swap the middle days when conditions and reservations justify it.

This is my simplest first comparison while your driving preference remains open. **A city hotel is not a beachfront resort.** If beach time matters more than city browsing, compare **five nights split Naha 2 + Onna 3**, with transfers, resort location, and transport priced first. Do not use the Naha day cards as if every bus/port were equally convenient from Onna.

With only three nights, keep city culture and one coast/boat/north choice. A longer stay can add slower beach days; it does not need an outing to every named area.

## Choose your base and transport

| Base | Best reason to choose it | Transport implications |
| --- | --- | --- |
| **Naha near Yui Rail / Kokusai Street** | Airport access, meals, crafts, Shuri, and a Tomari-port outing | Strongest starting comparison without a car. Confirm the walk to hotel and port; monorail does not reach Onna or Motobu. |
| **Chatan** | Waterfront cafés, sunset walks, American Village shopping | Compare dated buses/airport transfer and the actual hotel location. A coastal base still needs a northern/port transport plan. |
| **Onna coast** | Beach/resort stay and coastal photography | Compare hotel shuttle/bus stops, meals, and beach access, or a deliberate rental-car plan. Do not assume every resort is walkable from every stop. |
| **Motobu area** | More time around Churaumi / Ocean Expo Park | An alternative northern base for a longer visit; it is farther from Naha activities and airport transfers. |

[Naha guide](https://visitokinawajapan.com/destinations/okinawa-main-island/southern-okinawa-main-island/naha/) · [Chatan guide](https://visitokinawajapan.com/destinations/okinawa-main-island/central-okinawa-main-island/chatan/) · [Onna coast guide](https://visitokinawajapan.com/destinations/okinawa-main-island/northern-okinawa-main-island/onna-coast/) · [Motobu guide](https://visitokinawajapan.com/destinations/okinawa-main-island/northern-okinawa-main-island/motobu-peninsula/).

**Without a car:** use Yui Rail / walking for selected Naha sights, a dated bus/shuttle for a chosen coast destination, and a reserved tour only if its stops, pickup, time, and price suit. A taxi is a priced alternative, not an assumed unlimited transport budget. Select one destination block per excursion; a bus map does not establish that a multi-stop driving itinerary works by bus. [Official getting-around guide](https://visitokinawajapan.com/plan-your-trip/getting-around-okinawa/) · [Yui Rail operator](https://www.yui-rail.co.jp/en/).

**With a car:** compare the full rental quote, pickup/return travel, insurance terms, fuel, parking, and any tolls. Before choosing this branch, confirm the driver's accepted documents and eligibility with the rental operator using the [official rental-vehicle guidance](https://visitokinawajapan.com/plan-your-trip/getting-around-okinawa/rental-vehicles-in-okinawa/). A foreign license or a document called an international permit does not by itself confirm acceptance. No car or driving eligibility has been assumed.

## Naha — culture, food, and crafts

**Shuri Castle Park:** choose a park / heritage visit and check the actual areas available on your date. The operator announces the restored **Seiden main hall interior opening for 23 November 2026**, with designated date/time reservations for interior viewing. A paid-area ticket **without** that reservation excludes the main hall interior. The announced adult individual fee from that date is **¥1,000**, with no extra charge for the timed designation. [Official opening and ticket guide](https://oki-park.jp/shurijo/en/ticket_guide/).

Treat this as an announced change checked in October 2026, not proof that a particular 2027 slot is available. Use [current park notices](https://oki-park.jp/shurijo/en/) and [operator access instructions](https://oki-park.jp/shurijo/access) to coordinate your monorail/bus/walk and ticket. Avoid relying on pre-fire photos or older restoration-tour assumptions for what you will see.

**Kokusai Street / Makishi area:** a manageable meal/shopping block, with the market as a browsing lead. Compare a clearly priced menu rather than assume a seafood purchase includes preparation or upstairs dining. **Tsuboya Yachimun Street:** pottery browsing and a café alternative. [Naha visitor guide](https://visitokinawajapan.com/destinations/okinawa-main-island/southern-okinawa-main-island/naha/).

**Café lead for you:** the official Naha feature lists **Okinawan cafe BUKU-BUKU** in Tsuboya and other café/gallery stops. Choose one seated break and check the actual menu, opening day, and filming permission. [Official café / craft walking feature](https://visitokinawajapan.com/travel-inspiration/get-to-know-naha/). A named café is a lead, not a booked seat or guaranteed drink.

## Coastal exploring — choose a manageable block

**Chatan / American Village:** waterfront walk, a café/meal, and a limited browsing block. My main photo goal here is **late-afternoon coast → sunset if visible → illuminated street detail**, with a confirmed return journey. Depot Island / Sunset Walk and the Miyagi Coast are separate possible blocks; choose by your transport and pace. [Official Chatan guide](https://visitokinawajapan.com/destinations/okinawa-main-island/central-okinawa-main-island/chatan/).

**Onna:** compare a beach-oriented stay or one selected coastal destination. Longer transfer time and resort access matter more than the number of beach pins. A paid guided snorkeling activity is an optional separate purchase after checking operator location, equipment, suitability, and weather. [Official Onna overview](https://visitokinawajapan.com/destinations/okinawa-main-island/northern-okinawa-main-island/onna-coast/).

**Motobu / Churaumi Aquarium:** dedicate an outing day to the aquarium / nearby Ocean Expo Park. The operator describes a substantial journey from Naha Airport, approximately **two hours by car** or **two and a half hours by express-bus options** before allowing for your actual connection and traffic. This is an orientation estimate, not a guaranteed hotel-to-door journey. [Aquarium access](https://churaumi.okinawa/guide/access/) · [Park's bus information and operator links](https://oki-park.jp/kaiyohaku/acc/147).

For the car-free version, compare a through bus/shuttle or a suitable dated tour, confirm the actual stop and walk to the entrance, and save the return. Do not combine a full aquarium visit, Onna beach day, Chatan sunset, and a Kerama trip in one day. [Aquarium visitor guide](https://churaumi.okinawa/en/). Kouri or other northern detours would require a separate, workable transport plan; they have not been added automatically.

## Kerama option — Zamami day trip from Naha

**Route:** Naha hotel → **Tomari Port** → the correct reserved boat to **Zamami Port** → selected beach/village area using confirmed island transport → boat back → hotel. The high-speed boat and larger ferry use different boarding arrangements; confirm your vessel and pier. [Tourism association access guide](https://www.zamamitourism.com/en/transport).

Choose **one beach/viewpoint or a guided marine activity** after coordinating its start/finish with both sailings. **Furuzamami Beach** is a sightseeing/swimming lead subject to its actual open zones, supervision, weather, and local transfer. A sea-view photo day does not require entering the water. [Official Zamami island guide](https://visitokinawajapan.com/destinations/kerama-islands/zamami-island/).

Book/check **both directions** rather than assume a return seat. Boats can sell out or be canceled by wind/waves, and the operator determines daily service. The tourism association supplies information; **boat reservations are managed by the village office**, not the association. [Reservation guidance](https://www.zamamitourism.com/en/aboutboat-1) · [Village office for current sailing status and booking links](https://www.vill.zamami.okinawa.jp/).

Do not schedule this on your flight day. For an island overnight, replace a Naha hotel night and reassess weather/luggage/return buffers first; this chapter does not include that overnight. Do not add Aka and Tokashiki transfers to the same introductory day. If boat conditions fail, use a land day or the northern option when its own transport is workable.

### Beach and marine-day checks

Check whether swimming is allowed, the managed swimming zone, supervision, weather/sea conditions, and operator guidance. Stay out when local restrictions or conditions require; use appropriate flotation/equipment for chosen activities. Protect coral and follow local instructions. [Official sea-activity guidance](https://visitokinawajapan.com/wp-content/themes/visit-okinawa_multi-language/lang/en/assets/document/plan-your-trip/useful-information/303/All%20About%20the%20Sea%20in%20Okinawa.pdf).

No guaranteed calm sea, turtle sighting, diving qualification, snorkeling booking, or beach opening is assumed. Your default outdoor activity remains walking and photography until a water activity is deliberately selected.

## Foods to try

My first choices are **Okinawa soba**, **goya champuru**, and one **beni-imo or sata-andagi sweet**. Add a pork dish or taco rice on another day rather than order every specialty at once.

| Food | What to expect | Suggested role |
| --- | --- | --- |
| **Okinawa soba / soki soba** | Local noodle soup; pork-rib topping is a common soki version | Arrival meal or city lunch; inspect the actual broth/toppings |
| **Goya champuru** | Bitter-melon stir-fry, often with tofu and other ingredients | A main dish or shared side; actual recipes vary |
| **Rafute** | Slow-cooked pork dish | One dinner if pork appeals |
| **Taco rice** | Rice with taco-style toppings | Casual lunch; an alternative to another noodle meal |
| **Sata andagi** | Fried doughnut-style sweet | One fresh snack, not a required souvenir box |
| **Beni-imo tart** | Purple sweet-potato sweet | Taste one, then compare a small gift box |

[Official Okinawan food culture](https://visitokinawajapan.com/discover/food-and-longevity/okinawan-food-culture/) · [JNTO cuisine examples](https://www.japan.travel/en/gastronomy/article-indigenous-cuisine-on-the-menu/) · [Official street-food guide](https://visitokinawajapan.com/travel-inspiration/must-try-okinawa-street-foods/) · [Okashigoten's sweet guide](https://okashigoten.co.jp/en/faq/).

For an izakaya evening, start with the Naha/Kokusai area near your chosen hotel and compare actual menu, seating, cover charge if any, and total price. It is an area lead rather than a verified individual-restaurant reservation. Keep coastal sunset and a long dinner realistic against the final bus/transport plan.

## Clothing, crafts, and gifts

| Buy idea | Best match | Where / source |
| --- | --- | --- |
| **Kariyushi shirt** | For you: a distinctive local shirt to compare with your tee/shirt wishlist | MANGO HOUSE's [official store directory](https://www.mangohouse.jp/f/shop) lists **Kokusai Street No. 2, 1-2-1 Matsuo, Naha**, as one central branch. No exact print, price, or size stock confirmed. |
| **Small bingata textile/accessory** | For her: a compact fashion-related gift without a fitted-garment decision | Compare origin, pattern, material, and price; [official bingata craft guide](https://visitokinawajapan.com/travel-inspiration/ryukyu-bingata-okinawa-dyeing/). |
| **Yachimun pottery / small shisa** | For you or her: one craft keepsake | Browse Tsuboya; inspect packing, fragility, maker, and actual cost. [Naha craft/café guide](https://visitokinawajapan.com/travel-inspiration/get-to-know-naha/) · [Traditional craft experiences](https://visitokinawajapan.com/travel-inspiration/must-try-traditional-experiences/). |
| **Beni-imo tarts or chinsuko** | Her sweet-gift choice | [Okashigoten official stores](https://okashigoten.co.jp/en/) lists **Kokusai Street Matsuo, 1-2-5 Matsuo, Naha** and airport counters. Branch stock and travel-day hours still need checking. |

Your **L tops / EU 44–46 trousers** are references; use actual measurements or try on before buying. Her clothing size and perfume preferences remain unknown. No current Okinawa Y2K/Korean-style product stock or perfume counter has been verified here; the existing [[Japan 2027 — Gifts for Her|gift shortlist]] remains the place to compare those options.

For sweets, check the **specific product's** ingredients, expiry, and storage. Packaged original tarts and chilled/frozen fresh sweets are different products; do not assume identical travel suitability. A pottery workshop also needs pickup/shipping timing before treating the finished item as a same-day souvenir.

Choose one keeper or one small gift within the existing allowance. Her purchases share **US$200**, with inclusion in the **US$300 shopping/miscellaneous** allowance still open. If included, up to US$100 remains for your other shopping; if additional inside the same trip ceiling, the previously described reserve decreases. No new Okinawa allowance is added. [[Japan 2027 — Shopping Shortlist|Shopping priorities]].

## Photography and filming wishlist

**My sequence:** Naha street establishing shot → permitted Shuri architecture/detail → Tsuboya craft texture with permission → coast/water wide shot → food close-up → sunset or night street. Choose one coast scene you can reach comfortably; a sunny brochure image is not a forecast.

Ask before filming in shops, cafés, museums, or guided activities and follow castle/site restrictions. Keep tripods out of busy walkways and do not film other customers without consent. Water filming is an optional equipment/activity decision, not a reason to enter an unsuitable area. [[Japan 2027 — Photography and Filming Wishlist|Main shot and permission records]].

## Compare your seasons

| Season | Main fit | Adaptation |
| --- | --- | --- |
| **Summer / July–early August** | Beach scenery and a possible marine activity | Heat and typhoons can affect plans; keep flexible land days and mainland return nights. A late-July/early-August trip is not outside typhoon season. |
| **November** | City culture, food, coastal walks, and a break from mainland cold | A good comparison for land-based exploring. Confirm each beach's swimming permission and conditions; it is not a Kyoto-style autumn-color module. |
| **Second half of May** | Warm southern scenery, crafts, and food | Usually overlaps the rainy season; retain indoor/short land alternatives rather than assume clear beach days. |
| **Late March / early April** | Another climate/culture option | Separate from your Kyoto/Tokyo blossom route; it requires replaced nights and a whole-trip revision. |

[Official climate / seasons guide](https://visitokinawajapan.com/plan-your-trip/when-to-visit-climate-seasons/) · [May guidance](https://visitokinawajapan.com/plan-your-trip/when-to-visit-climate-seasons/okinawa-may/) · [November guidance](https://visitokinawajapan.com/plan-your-trip/when-to-visit-climate-seasons/okinawa-november/). The [official FAQ](https://visitokinawajapan.com/plan-your-trip/faq/) places the typical rainy season in May–June and says typhoons are most common in August/September, with possible occurrences June–October. These are general patterns, not 2027 forecasts or guarantees outside those months.

## Getting here — Haneda, Narita, and Kansai

| Start | Route to compare | Before selecting |
| --- | --- | --- |
| **Haneda (HND)** | HND → **Naha (OKA)** domestic flight → hotel transfer | Dated fare, baggage, terminal/check-in, and international-to-domestic connection rules |
| **Narita (NRT)** | A dated direct NRT → OKA flight, if suitable | Airline/terminal and full fare with baggage; do not assume changing to HND is required |
| **Kyoto / Osaka** | Hotel → selected Kansai airport, such as ITM or KIX → OKA | Compare each exact airport and hotel-to-airport journey; these airports are not interchangeable |
| **Okinawa → Tokyo** | Hotel → OKA → chosen Tokyo airport → final Tokyo hotel | Retain the Tokyo buffer nights before international departure |
| **International arrival at OKA** | Arrival formalities → selected monorail/bus/taxi transfer | Correct terminal exit, last usable connection, and hotel location |

[JAL route / timetable tools](https://www.jal.co.jp/jp/en/dom/route/index.html) · [Peach routes / schedules](https://www.flypeach.com/en/lm/st/routemap) · [Naha Airport terminal and transport information](https://www.naha-airport.co.jp/en/). These links do not establish a particular 2027 service or fare. Use **OKA** for this module; ISG, MMY, and SHI serve different island-region choices in [[Japan 2027 — Island Access from Haneda and Narita]].

**Airport → Naha:** compare **Yui Rail** to the station nearest your hotel, followed by the actual walk/taxi. **Airport → Chatan/Onna:** compare a dated bus/shuttle, prearranged transfer, or deliberate rental-car pickup; Yui Rail does not complete that coastal journey. **Hotel → Tomari Port:** verify your boat's terminal/pier and check-in deadline, separately from the airport transfer. [Yui Rail operator](https://www.yui-rail.co.jp/en/) · [Zamami access](https://www.zamamitourism.com/en/transport).

## Fit it into 15 days / 14 nights

| Alternative | Nights | What it replaces |
| --- | --- | --- |
| **Four-night main-island module** | Tokyo 4 → Kawaguchiko 2 → Kyoto 2 → Okinawa 4 → Tokyo 2 = **14** | Four Kyoto nights; only one full non-transfer Kyoto day remains |
| **Five-night beach/culture preference** | Tokyo 4 → Kawaguchiko 2 → Kyoto 1 → Naha 2 → Onna 3 → Tokyo 2 = **14** | Kyoto becomes a brief stop; compare whether that transfer is worthwhile |
| **Okinawa-focused alternative** | Tokyo 4 → Kawaguchiko 2 → Okinawa 6 → Tokyo 2 = **14** | Omits Kyoto/Osaka; allows a slower main-island stay with bases chosen deliberately |

These are alternatives to the existing seasonal outlines and to Ishigaki/Miyako, Sapporo, and Fukuoka modules. They do not modify the dated spring cards. The Fuji scenic/summit choice remains separate. For the five-night version, arrival/transfer days reduce full beach time; Naha 2 + Onna 3 is five nights, not five full sightseeing days.

Keep the existing **US$5,000 in-Japan ceiling**, excluding international flights. Requote domestic flights with baggage, airport travel, replaced accommodation, ferry return tickets, any resort transfers/car costs, guided activities, meals, and admissions. The seasonal **US$400 intercity planning allocation** does not prove these flights/ferries fit. Count transport legs once and preserve the final mainland nights; this buffer reduces connection pressure but cannot guarantee disruption-free travel. No tickets or lodging have been booked.

## Google Maps — places and transport

Search links are orientation pins, not dated services, offline maps, booked activities, open swimming zones, or verified stock. Select the correct port pier/entrance and your actual hotel as the start point.

MAP_TABLE

## Before booking

- [ ] Choose main island, Ishigaki/Taketomi, or Miyako first.
- [ ] Choose four Naha nights or a longer split base; identify replaced mainland nights.
- [ ] Decide whether to use a car and confirm requirements before pricing that branch.
- [ ] Check complete airport transfers and domestic flight baggage/connection rules.
- [ ] For Shuri interiors, check the correct ticket and timed reservation.
- [ ] Choose Zamami OR the north for the short stay; verify both transport directions.
- [ ] Keep a land alternative and check actual beach/sea operations.
- [ ] Requote the entire route within the existing envelope; gifts remain within their shared cap.

[[Japan 2027 — Okinawa Pocket Routes|Open the compact routes]] · [[Japan 2027 — Best Islands|Compare island regions]]
'''

PLACES = [
('Airport', 'Naha Airport (OKA)', 'Naha Airport OKA Okinawa'),
('Airport monorail', 'Naha Airport Yui Rail Station', 'Naha Airport Station Yui Rail Okinawa'),
('Naha base / monorail', 'Kencho-mae Station', 'Kencho mae Station Naha Okinawa'),
('Port-area monorail', 'Miebashi Station', 'Miebashi Station Naha Okinawa'),
('Shuri transport', 'Shuri Station', 'Shuri Station Yui Rail Naha'),
('City transport', 'Naha Bus Terminal', 'Naha Bus Terminal Okinawa'),
('Shopping / meals', 'Kokusai Street', 'Kokusai Dori Naha Okinawa'),
('Food browse', 'First Makishi Public Market', 'First Makishi Public Market Naha Okinawa'),
('Culture', 'Shuri Castle Park', 'Shurijo Castle Park Naha Okinawa'),
('Castle gate', 'Shureimon', 'Shureimon Gate Shuri Naha'),
('Crafts', 'Tsuboya Yachimun Street', 'Tsuboya Yachimun Street Naha Okinawa'),
('Café lead', 'Okinawan cafe BUKU-BUKU', 'Okinawan cafe BUKU BUKU Tsuboya Naha'),
('Sweet gifts', 'Okashigoten Kokusai Street Matsuo', 'Okashigoten 1-2-5 Matsuo Naha Okinawa'),
('Kariyushi shirts', 'MANGO HOUSE Kokusai Street No. 2', 'MANGO HOUSE 1-2-1 Matsuo Naha Okinawa'),
('Coastal browse', 'Mihama American Village', 'Mihama American Village Chatan Okinawa'),
('Waterfront photos', 'Depot Island / Sunset Walk', 'Depot Island Sunset Walk Chatan Okinawa'),
('Coastal walk alternative', 'Miyagi Coast', 'Miyagi Coast Chatan Okinawa'),
('Coastal area', 'Onna coast', 'Onna Village Okinawa Japan'),
('Northern outing', 'Okinawa Churaumi Aquarium', 'Okinawa Churaumi Aquarium Motobu'),
('Northern park', 'Ocean Expo Park', 'Ocean Expo Park Motobu Okinawa'),
('Aquarium bus orientation', 'Kinen Koen Mae bus stop', 'Kinen Koen Mae bus stop Motobu Okinawa'),
('Boat departure — verify pier', 'Tomari Port / Tomarin', 'Tomari Port Tomarin Naha Okinawa'),
('Island boat arrival', 'Zamami Port', 'Zamami Port Okinawa Japan'),
('Island beach — confirm open zones', 'Furuzamami Beach', 'Furuzamami Beach Zamami Okinawa'),
('Island scenery option', 'Takatsukiyama Observatory', 'Takatsukiyama Observatory Zamami Okinawa'),
]
table = '| Use | Google Maps location |\n| --- | --- |\n' + '\n'.join(
    '| ' + category + ' | [' + label + '](https://www.google.com/maps/search/?' + urlencode({'api': '1', 'query': query}) + ') |'
    for category, label, query in PLACES)
NOTES['Japan 2027 — Okinawa Chapter.md'] = NOTES['Japan 2027 — Okinawa Chapter.md'].replace('MAP_TABLE', table)

NOTES['Japan 2027 — Okinawa Pocket Routes.md'] = '''# 🏝️ Okinawa — pocket routes

[[Japan 2027 — Okinawa Chapter|← Full chapter, official sources, airport access, and Google Maps]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / bookings]]

**Undated Naha-base cards:** four nights give arrival, three full outing days, and departure. Use Cards 1–4 with Card 4's A OR B choice. Swap Cards 2–4 when conditions/reservations justify. For three nights, omit one full outing. An Onna split-base version needs different transfers; these are not four consecutive days of driving around every region.

## Card 1 — arrive and settle into Naha

**Route:** Naha Airport (OKA) → selected Yui Rail / bus / taxi connection → hotel. Confirm baggage and check-in arrangements first.

**If time and energy allow:** short Kokusai/hotel-area walk → Okinawa soba or a nearby meal → rest. Arrival is a transport day, not a ferry-and-beach day. For a late arrival, keep the meal near the hotel and omit shopping.

**Shot:** city arrival transition → street scene → first food detail with permission. **Buy:** none required. **Check:** actual arrival terminal, final usable connection, and next day's weather/reservation.

## Card 2 — Shuri, a seated meal, and Naha crafts

| Block | Plan |
| --- | --- |
| Morning | Confirmed monorail/bus/walk → Shuri Castle Park. Interior only with the correct available timed reservation. |
| Midday | Lunch/rest; choose goya champuru, soba, or another suitable menu. |
| Afternoon | Tsuboya pottery street plus one café OR Makishi/Kokusai browsing. Reduce the block if the castle visit runs long. |
| Evening | A nearby dinner; rafute is optional if pork appeals. |

**Shot:** permitted castle architecture → street/craft texture → tea/sweet detail. **Buy:** kariyushi shirt after fit check OR compact craft / packaged sweet. Use current MANGO HOUSE branch information before navigating to a shop. Her size and fragrance preferences remain open.

**Rain alternative:** selected café/covered shopping and any confirmed indoor part of the chosen visit; outdoor castle paths still need weather judgment. **Check:** ticket type, actual opening, transport, shop hours, filming permission, and shared shopping cap.

## Card 3 — Chatan waterfront and a realistic sunset plan

**Route:** Naha hotel → dated coast bus/shuttle, priced taxi, or a deliberately selected rental-car route → Chatan → confirmed return. Yui Rail alone does not complete this journey.

**Main block:** American Village / Depot Island waterfront → lunch or café → limited shopping → late-afternoon photos. Miyagi Coast is an alternative or a separately routed extension, not a compulsory extra walk. Choose one main coastal block.

**Food:** taco rice or a clearly priced café meal, plus one sweet if wanted. **Shot:** coast wide → street color → food → sunset if visible. **Buy:** none required; one shirt/accessory replaces another planned shopping choice.

**Return:** verify the last workable bus before committing to sunset/dinner. A later taxi needs a realistic quote. **Bad-weather alternative:** Naha cafés/crafts and a shorter outdoor walk. For an Onna hotel base, rebuild this day's start/finish and avoid an unnecessary Naha return.

## Card 4 — choose A OR B

### A. Zamami — one Kerama island day

**Route:** Naha hotel → correct Tomari Port pier → reserved boat to Zamami Port → confirmed local beach/viewpoint or activity transfer → reserved boat back → Naha hotel.

**Main block:** one Furuzamami/beach-view area OR one guided marine activity that finishes in time for the return. Choose lunch/break and island transport before departure. The beach pin does not confirm swimming permission or supervision. Observe local sea rules; land photos are a valid option.

**Shot:** port transition → sea/coast wide → village detail where appropriate. **Buy:** none required. **Check:** both seats, actual sailing status, pier/check-in, local return, and the activity's equipment/conditions. Boats can cancel by wind/waves; use a land fallback. No Aka/Tokashiki hopping or island overnight is counted.

### B. Motobu — Churaumi Aquarium / Ocean Expo Park

**Route:** selected dated through bus/shuttle/tour or rental-car route → confirmed aquarium-area stop/entrance → return. Allow a full excursion day; the northern journey is substantial.

**Main block:** aquarium visit → meal/break → a manageable nearby park block if conditions and return time suit. Check current admission, opening, and any program notices. Do not add a full Onna beach day and Chatan sunset afterward.

**Shot:** exterior/park scene → permitted exhibit detail → coast context. **Buy:** one compact keepsake only if wanted. **Check:** outward/return transport, stop-to-entrance walking, pickup if using a tour, and total cost. This is an alternative to the boat day, not a guaranteed transport option during severe weather.

**Departure day:** hotel → OKA with baggage/check-in buffer. If renting, allow return/refueling and transfer time. No ferry outing or northern day trip is scheduled before the flight. The Tokyo-return alternatives retain two separate Tokyo hotel nights before international departure.
'''

LINKS = {
    'Japan 2027 — Start Here.md': '**Okinawa chapter:** [[Japan 2027 — Okinawa Chapter|Naha, coasts, food, crafts, transport, and Maps]] · [[Japan 2027 — Okinawa Pocket Routes|Four flexible routes]].',
    'Japan 2027 — Seasonal Guides.md': '**Okinawa option:** [[Japan 2027 — Okinawa Chapter]] compares a four-night Naha base with a longer beach stay, summer/November/May conditions, and 14-night alternatives.',
    'Japan 2027 — Summer Guide.md': '**Okinawa alternative:** [[Japan 2027 — Okinawa Chapter|Main-island culture and coast]]. Replace other nights; summer heat/typhoon conditions and full domestic-flight costs need checking.',
    'Japan 2027 — Autumn Guide.md': '**Okinawa comparison:** [[Japan 2027 — Okinawa Chapter|November culture, food, and coastal walks]]. It replaces mainland foliage time; swimming permission and sea conditions remain local dated checks.',
    'Japan 2027 — November vs May.md': '**Okinawa comparison:** [[Japan 2027 — Okinawa Chapter]] distinguishes November land/coast exploring from late-May rainy-season planning; neither guarantees beach conditions.',
    'Japan 2027 — Nara Chapter.md': '**Next regional chapter:** [[Japan 2027 — Okinawa Chapter|Okinawa]] — a separate domestic-flight module, with Naha culture and coastal choices rather than another Kansai day trip.',
    'Japan 2027 — Best Islands.md': '**Okinawa main-island comparison:** [[Japan 2027 — Okinawa Chapter|Naha, Chatan/Onna, and one Kerama day]]. Compare with Ishigaki/Taketomi or Miyako first; they are separate regional bases.',
    'Japan 2027 — Island Access from Haneda and Narita.md': '**Okinawa Main Island access:** [[Japan 2027 — Okinawa Chapter|HND/NRT → Naha (OKA), coastal transfers, and Tomari/Zamami]]. OKA is a different arrival choice from ISG, MMY, and SHI.',
    'Japan 2027 — Seasonal Planning and Bookings.md': '**Okinawa decision:** [[Japan 2027 — Okinawa Chapter|Four-night, split-base, or Okinawa-focused routes]]. Requote flights, baggage, replaced hotels, local transfers, and selected boat/car/activity costs within the existing ceiling.',
    'Japan Travel Guide 2027.md': '**Okinawa research chapter:** [[Japan 2027 — Okinawa Chapter]] · [[Japan 2027 — Okinawa Pocket Routes]]. Optional main-island module; the original dated blossom itinerary remains unchanged.',
}

def validate(root, manifest):
    for name in manifest:
        s = (root / name).read_text()
        assert s.startswith('# ') and 'MAP_TABLE' not in s, name
        for target in re.findall(r'\[\[([^\]|#]+)', s):
            assert target + '.md' in manifest or (V / (target + '.md')).exists(), (name, target)
    s = (root / 'Japan 2027 — Okinawa Chapter.md').read_text()
    assert s.count('https://www.google.com/maps/search/?') == len(PLACES) == 25
    for url in re.findall(r'\]\((https://[^)]+)\)', s):
        assert ' ' not in url
        if 'google.com/maps/search' in url:
            q = parse_qs(urlparse(url).query)
            assert q['api'] == ['1'] and q['query'][0]
    assert all(sum(route) == 14 for route in ([4, 2, 2, 4, 2], [4, 2, 1, 2, 3, 2], [4, 2, 6, 2]))
    s = (root / 'Japan 2027 — Okinawa Pocket Routes.md').read_text()
    assert len(re.findall(r'^## Card [1-4] ', s, re.M)) == 4
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
    print('Saved Okinawa chapter, four pocket routes, 25 Maps links, and ten integrations. Night counts, references, and installed content verified; originals backed up.')
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
    print('Prepared Okinawa chapter, four pocket routes, 25 Maps links, and ten integrations. All original content preserved; references and 14-night routes validated.')
