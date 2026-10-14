from pathlib import Path
import hashlib,json,re,shutil,sys
W=Path('/home/ivanaguilera/Work/japan-guide-update/seasonal-guides')
V=Path('/home/ivanaguilera/Documents/Obsidian Vault')
NOTES={}
NOTES['Japan 2027 — Seasonal Guides.md']='''# 🗾 Japan — seasonal travel guides

**Working year: 2027**, inherited from your existing trip research; actual year/dates remain unconfirmed. Built 7 October 2026. All three concepts are alternatives for one trip, unless you later choose multiple visits.

| Open | Purpose |
| --- | --- |
| [[Japan 2027 — Summer Guide]] | Summer cities, Fuji lakes, hiking choices, and festival planning |
| [[Japan 2027 — Summer Fuji Climb Option]] | Optional summit branch requiring its own preparation and reservations |
| [[Japan 2027 — Autumn Guide]] | November foliage, Kyoto/Tokyo photography, and low-elevation hiking |
| [[Japan 2027 — November vs May]] | Compare November autumn colors with May greenery, including a May route adaptation |
| [[Japan 2027 — Seasonal Planning and Bookings]] | Shared budget, decisions, reservation records, and checks |
| [[Japan 2027 — Start Here|Existing cherry-blossom guide]] | Your March/April concept |

**My suggested order:** review summer → decide Fuji scenic visit or summit → compare November and May → choose a season before assigning calendar dates or buying tickets. Fifteen-day outlines are included in the summer and autumn guides; dated daily pocket cards should follow the chosen arrival date.
'''
NOTES['Japan 2027 — Summer Guide.md']='''# ☀️ Japan 2027 — Summer Guide

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and reservations]] · [[Japan 2027 — Autumn Guide|Autumn alternative]]

**Status:** planning guide; no dates, hotels, transport, festival tickets, or climbs booked. **Working length:** 15 days / 14 nights, one traveler as a budgeting assumption. **Your interests:** photography/filming, hiking, Fuji, cafés and matcha, vintage clothes, Tamiya, records, and gifts.

## Best starting window

My first window to compare is **late July into early August**, before the main mid-August Obon travel period. Early July can overlap the rainy season; July/August city sightseeing requires planning for heat and humidity. This is a seasonal recommendation, not a forecast or a promise of lower prices. [JNTO July](https://www.japan.travel/en/guide/july/) · [JNTO August](https://www.japan.travel/en/guide/august/).

If Gion Matsuri is a priority, choose the Kyoto nights around the festival rather than preserving the order below. Kyoto's official guide identifies **July 17 and 24** as procession highlights within the July festival; the exact **2027 arrangements, access, and paid seats need checking**. [Kyoto festival information](https://global.kyoto.travel/en/faq/detail.php?faq_id=2025). No firework date or seasonal event has been assigned to this itinerary.

## Route and accommodation count

**Tokyo 4 nights → Kawaguchiko 2 → Kyoto 6 → Tokyo 2 = 14 nights.** This scenic-Fuji route is the default. Choose air-conditioned rooms with practical station access and cancellable terms where possible; lake-view lodging is an optional upgrade, not a requirement. Compare a Tokyo return flight against departing Osaka/KIX before fixing the last two nights.

Tokyo → Kawaguchiko: compare [direct highway bus](https://bus.fujikyu.co.jp/en/lp/en-shinjuku-kawaguchiko/) and [FUJI EXCURSION rail](https://e.fujikyu-railway.jp/fujikaiyuu/). Kawaguchiko → Kyoto: check the [Mishima–Kawaguchiko liner](https://bus.fujikyu.co.jp/en/highway/mishima/) in the required direction, then the [Tokaido Shinkansen](https://global.jr-central.co.jp/en/). Allow a connection buffer for road delays. If that dated connection is unsuitable, compare returning through Tokyo before Kyoto. Fares and schedules are unconfirmed.

## Fifteen-day outline

These are my proposed outing blocks, not attraction opening times. Choose one main outdoor block per day and use lunch/cafés/indoor browsing to break up the heat. Swap adjacent days when weather or opening notices justify it.

| Day / night | Main plan | Flexible or bad-weather alternative | Photo/film prompt |
| --- | --- | --- | --- |
| 1 / Tokyo 1 | Arrive, hotel transfer, food, rest | Nearby indoor meal | First neighborhood scene |
| 2 / Tokyo 2 | Asakusa early; café and indoor browsing later | Shorten walking and stay near transport | Temple detail / river scene |
| 3 / Tokyo 3 | Kichijoji: choose park, vintage, coffee, and one record shop | LOFT or record browsing with breaks | Pond reflection / shop entrance |
| 4 / Tokyo 4 | Choose an early Takao walk if conditions suit; otherwise a Tokyo park | Shops/café day; full hike is optional | Forest/temple detail |
| 5 / Kawaguchiko 1 | Travel to the Fuji lakes; hotel and lakeside walk | Café and local orientation | Wide lake-and-mountain view if visible |
| 6 / Kawaguchiko 2 | Choose two: lakeside/Oishi Park, Chureito viewpoint, or ropeway | Keep local; no mountain outing in poor weather | One wide frame and one detail |
| 7 / Kyoto 1 | Transfer via a verified connection; easy dinner | Treat as a travel/rest day | Evening arrival atmosphere |
| 8 / Kyoto 2 | Higashiyama early, then seated lunch/café and one indoor stop | Reduce temple count | Street layers / architectural detail |
| 9 / Kyoto 3 | Arashiyama early, then lunch and return | Nearby café / indoor browsing | River, greenery, bamboo detail |
| 10 / Kyoto 4 | Uji matcha-focused outing | Central Kyoto tea/café alternative | Tea preparation with permission |
| 11 / Kyoto 5 | Central Kyoto markets, shops, and gift browsing | Keep the day mostly indoors | One purchase and its story |
| 12 / Kyoto 6 | Optional early Daimonji walk OR Kurama–Kibune if conditions and effort suit | Festival only if dates fit, or relaxed city day | Hill panorama or forest sequence |
| 13 / Tokyo 5 | Return to Tokyo; hotel and easy evening | Rest and laundry | Travel transition |
| 14 / Tokyo 6 | Tamiya in Shinbashi; choose Donki or clothing/gift stop, then pack | Limit to the main purchase | Souvenir detail; ask before shop filming |
| 15 / — | Airport transfer and departure | Leave a reliable transfer buffer | Optional final scene |

Night labels count actual nights in each base: Tokyo's final block is its fifth/sixth nights. Arrival/departure times can change what is realistic on Days 1 and 15. The guide's [existing Fuji viewpoints](https://www.mtfujiropeway.jp/en/) include weather-dependent operations; keep a second opportunity for a view during the two-night stay. Summer visibility is not guaranteed.

## Hiking choices

- **Scenic Fuji lakes:** default, with Chureito's stairs an optional effort. [[Japan 2027 — Hiking and Mount Fuji|Existing hiking research]] supplies viewpoint and trail links; its March/April date suggestions do not apply here.
- **Takao Trail 1:** a possible Tokyo hike, shortened with cable-car assistance if operating. Use the [operator's map](https://www.takaotozan.co.jp/course/img/course_map_english.pdf) and current access notices. A summer city visit does not require a full summit walk.
- **Daimonji or Kurama–Kibune:** choose one Kyoto outdoor block; rain, heat, and trail notices can replace it with city activities. Your preferred effort is still unknown.
- **Fuji summit:** open the separate [[Japan 2027 — Summer Fuji Climb Option|climb option]]. The default two-night lake stay does not provide the climb, descent, and recovery block by itself.
- **Kamikochi nature variation:** if alpine-valley scenery matters more than six Kyoto nights, compare **Tokyo 4 → Fuji lakes 2 → Matsumoto 2 → Kyoto 4 → Tokyo 2 = 14 nights**. Use Matsumoto as the access base and spend a full day on a low valley walking route, with current transfers checked. This replaces Kyoto days rather than adding nights. [Official walking routes](https://www.kamikochi.org/thingstodo/walking) · [Access](https://www.kamikochi.org/access). Valley walks do not imply readiness for the high alpine summits. This variant is not scheduled in the default daily table.

## Cafés, shopping, and her gifts

Use [[Japan 2027 — Kichijoji Shopping and Exploring|Kichijoji]] for vintage/records/coffee and [[Japan 2027 — Shopping Shortlist|the shopping research]] for Tamiya and Donki. Kyoto/Uji provide the matcha focus. Choose one clothing piece or compact hobby purchase before optional records/stationery; check actual garment measurements and luggage space.

[[Japan 2027 — Clothing to Browse Online|Your clothing links]] and [[Japan 2027 — Gifts for Her|her clothing, beauty, perfume, and sweets]] remain browsing leads checked in October 2026. Earlier flannels/faux-fur hoodies may be autumn/winter products; summer trip stock, variants, and sizes are unconfirmed. Choose suitable garments for use at home rather than assuming every shop carries them year-round. Record consumption during the trip under meals and take-home food gifts under shopping.

## Phone-ready day rhythm and checklist

**Morning:** main outdoor block when access allows → **midday:** lunch, seated break, café or indoor activity → **later:** short photo walk or one shop → **evening:** dinner, photos backed up, next-day weather/transport checked. This is a flexible rhythm, not an assertion that every attraction opens early.

- [ ] Confirm year, arrival/departure dates, traveler count, hiking effort, and scenic Fuji versus summit.
- [ ] Check hotel air-conditioning, full-stay price, station access, and cancellation deadline.
- [ ] Save dated transport and return connections; verify festival arrangements only after choosing dates.
- [ ] Carry water, sun/rain protection, light city clothing, and grip footwear; use proper mountain layers if hiking.
- [ ] Replace outdoor plans when local heat/weather/access notices make them unsuitable.
- [ ] Compare all actual prices with [[Japan 2027 — Seasonal Planning and Bookings|the seasonal budget]] before purchase.

International flights, dated transport fares, event access, and accommodation remain unquoted. This guide is ready for choosing a route; it is not a confirmed travel schedule.
'''
NOTES['Japan 2027 — Summer Fuji Climb Option.md']='''# 🗻 Summer Fuji — optional summit branch

[[Japan 2027 — Summer Guide|← Summer guide]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and booking records]]

**Decision still open:** you requested hiking and a Fuji visit; a summit climb has not been selected. Your hiking experience and preferred effort are not recorded. Scenic lake/viewpoint visits remain the default summer route.

The [official climbing site](https://www.fujisan-climb.jp/en/) publishes trail openings, reservations, fees, preparation, and notices. Summer opening differs by trail and year; **2026 information is background, not confirmation of the 2027 season**. Do not apply old fee, gate-hour, or booking-opening details to a future purchase.

## How the climb changes the itinerary

Compare this **14-night alternative** only if you choose the summit:

**Tokyo 4 → Kawaguchiko 1 → mountain hut 1 → Kawaguchiko 2 → Kyoto 4 → Tokyo 2 = 14 nights.**

| Day | Proposed block | Night |
| --- | --- | --- |
| 1–4 | Same Tokyo block as the summer guide | Tokyo 4 |
| 5 | Transfer to Kawaguchiko; organize equipment and next day's verified access | Kawaguchiko |
| 6 | Travel to the chosen trailhead, acclimatize, climb to a reserved hut | Mountain hut |
| 7 | Optional summit attempt if appropriate, descend on the correct trail, return and rest | Kawaguchiko |
| 8 | Recovery / local lake day; no long intercity transfer planned | Kawaguchiko |
| 9 | Transfer to Kyoto on a verified connection | Kyoto |
| 10–12 | Kyoto highlights, reduced to fit the climb branch | Kyoto 3 further nights |
| 13–14 | Tokyo return, shopping, packing | Tokyo 2 |
| 15 | Departure | — |

**Day 8 is a recovery day.** If a weather delay shifts the climb, replace further Kyoto time or extend the trip explicitly before changing reservations. Buffer time does not guarantee a delayed hut or transport reservation can be moved.

The hut replaces a hotel night; it is not an extra uncounted night. Luggage storage/forwarding and transport after descent require confirmation. A sunrise summit is optional, not a reason to climb through the night without rest. The official [Yoshida model plan](https://www.fujisan-climb.jp/en/modelplan-yoshida/) provides a starting reference for a hut-based climb; a guide/operator should settle the route, pace, and suitability if selected.

## What to verify before selecting this branch

- [ ] Prior mountain experience, usual walking hours, and readiness for a strenuous high-altitude outing.
- [ ] Exact trail, opening period, current access rules, admission/reservation requirements, and current fee.
- [ ] Mountain hut: confirmed night, location on the selected trail, meals, bedding, arrival requirements, cancellation terms.
- [ ] Guide/operator if wanted: actual quote, inclusions, equipment, weather/turnaround policy, and meeting point.
- [ ] Proper clothing/footwear, waterproofs, headlamp, food/water, and the official preparation guidance; summer city clothing alone is insufficient.
- [ ] Trailhead transport both ways, descent route, return accommodation, and itinerary recovery time.
- [ ] Weather/trail notices and an agreed turnaround plan; the summit remains optional.
- [ ] Actual total for hut, access, transport, guide, and equipment, with reductions elsewhere if required to stay inside the cap.

**Cost status:** no hut, guide, equipment-rental, or admission quote. No summit reservation has been made. Do not add these costs invisibly to the scenic-route budget. If you choose scenic Fuji, retain the summer guide's two lake nights and skip this branch.
'''
NOTES['Japan 2027 — Autumn Guide.md']='''# 🍁 Japan 2027 — Autumn Guide

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — November vs May|November versus May]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and reservations]]

**Concept:** November photography, Fuji lakes, low-elevation hikes, matcha/cafés, and your existing shopping interests. **Working length:** 15 days / 14 nights. **Dates/year:** unconfirmed; 2027 is the inherited planning year. No bookings recorded.

## Window to compare

My first window is **mid-to-late November**, positioning Kyoto later in the trip for foliage. JNTO describes November's brisk weather and notes that Kyoto's autumn color season starts around mid-November; actual timing varies by year, site, and elevation. Use annual local foliage reports before assigning temple days. [JNTO November](https://www.japan.travel/en/guide/november/).

This guide plans low-elevation walking. Mountain weather/access need separate checks, and November is outside Fuji's normal summit season. Fuji viewpoints remain weather-dependent. There is no guaranteed peak-color or clear-sky date.

## Route

**Tokyo 4 nights → Kawaguchiko 2 → Kyoto 6 → Tokyo 2 = 14 nights.** Same base pattern as scenic summer, making the seasons easier to compare. Choose Kyoto dates around the actual foliage window; compare a KIX departure before committing the final Tokyo return.

Use the summer guide's operator links for Tokyo–Kawaguchiko, the possible Mishima connection to Kyoto, and the Tokyo return. Recheck the November timetable and connection buffer. Kyoto foliage demand can affect hotel availability; compare real quotes rather than assuming this is a cheaper season.

## Fifteen-day autumn outline

These are proposed blocks. Swap foliage days according to local reports and weather; do not stack every temple into one outing. Confirm admission/photography rules separately for each visit.

| Day / night | Main plan | Alternative / evening | Photography focus |
| --- | --- | --- | --- |
| 1 / Tokyo 1 | Arrive, hotel, dinner, rest | Nearby walk only if energy allows | First autumn city scene |
| 2 / Tokyo 2 | Asakusa and a riverside walk | Café and indoor browsing | Architecture / city layers |
| 3 / Tokyo 3 | Kichijoji park, vintage, coffee, and one record shop | LOFT or gift browsing | Water reflections / leaves if present |
| 4 / Tokyo 4 | Takao Trail 1 if open and conditions suit | Tokyo garden and café alternative | Woodland / temple detail |
| 5 / Kawaguchiko 1 | Transfer; lakeside orientation | Local dinner and early rest | Fuji view if visible |
| 6 / Kawaguchiko 2 | Choose lakeside/Oishi Park plus Chureito OR ropeway | Keep a flexible local weather day | Wide mountain / reflection detail |
| 7 / Kyoto 1 | Transfer on a verified connection; easy evening | Rest | Arrival atmosphere |
| 8 / Kyoto 2 | Nanzen-ji / Eikando area: choose manageable visits | Café; illumination only if announced and booked where needed | Maple/architecture detail |
| 9 / Kyoto 3 | Arashiyama riverside and one chosen temple | Lunch, return, short neighborhood walk | River and hillside color |
| 10 / Kyoto 4 | Tofuku-ji-focused morning; optional Fushimi area later | Reduce walking if queues are long | One autumn composition |
| 11 / Kyoto 5 | Uji tea/matcha outing | Central Kyoto tea/gifts alternative | Tea story / riverside |
| 12 / Kyoto 6 | Daimonji viewpoint OR Kurama–Kibune if access/daylight suit | Flexible foliage catch-up and cafés | Panorama or forest |
| 13 / Tokyo 5 | Return to Tokyo | Easy evening / laundry | Travel transition |
| 14 / Tokyo 6 | Tamiya plus one gift/clothing stop; packing | Donki or earlier shopping lead as time allows | Souvenir story |
| 15 / — | Airport and departure | Protect transfer buffer | Optional final frame |

Kyoto's official [green-maple/foliage spot list](https://global.kyoto.travel/en/faq/detail.php?faq_id=1034) identifies Nanzen-ji, Eikando, Tofuku-ji, and Arashiyama as maple destinations; the route above is my selection from those areas. Specific 2027 illumination periods, night admission, and tickets are unconfirmed. [Arashiyama area guide](https://www.kyoto.travel/en/areas/saga-arashiyama/).

## Walking, clothing, and photo rhythm

[[Japan 2027 — Hiking and Mount Fuji|Existing trail research]] gives Takao, Daimonji, and Kurama–Kibune options. Its spring dates are not autumn reservations. Finish hikes in daylight, check access notices, and adapt to wet/icy ground. Choose a city walk if conditions or your preferred effort make the hike unsuitable.

Pack layers, a warmer outer layer for evenings/lakes, rain protection, and shoes with grip. Plan one main outdoor area and a café break rather than crossing Kyoto repeatedly. My shot sequence: wide scene → leaf/architectural detail → person-scale walking shot with permission → ambient sound. Keep a weather/daylight note in the daily plan once dates are fixed.

## Buying and eating

Autumn is a useful context for browsing your flannel, denim-jacket, and trousers wishlist, but exact stock and size availability still need checking. Use [[Japan 2027 — Clothing to Browse Online]], [[Japan 2027 — Shopping Shortlist]], [[Japan 2027 — Kichijoji Shopping and Exploring]], and [[Japan 2027 — Gifts for Her]] as research references. Old March/April visit dates and October 2026 product stock do not transfer to this itinerary.

Keep matcha/cafés in Uji and central Kyoto, choose one vintage/record outing in Tokyo, and keep Tamiya as the last Tokyo shopping anchor. Her gifts remain capped at US$200 if retained; budget inclusion is handled in [[Japan 2027 — Seasonal Planning and Bookings|the planning note]]. No restaurant or shopping appointment is booked.

## Next decisions

- [ ] Confirm year, local arrival/departure dates, traveler count, and 14-night length.
- [ ] Decide November versus [[Japan 2027 — November vs May|May]] using scenery and weather preferences.
- [ ] Check lodging quotes for the actual foliage dates and total route cost.
- [ ] Check foliage updates, dated temple admission/illumination notices, trail access, and Fuji visibility.
- [ ] Reserve transport/paid experiences only after the dated route is set.
- [ ] Generate dated pocket cards and update calendar-day hours before departure.

This is a complete route concept with flexible daily blocks; seasonal conditions, prices, and bookings remain open.
'''
NOTES['Japan 2027 — November vs May.md']='''# 🍁🌿 Japan — November versus May

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Autumn Guide|November route]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and decisions]]

**Purpose:** choose between November autumn colors and May greenery/warmer days after reviewing summer. Working year 2027; no dates selected. My comparison uses the same **15 days / 14 nights** and **Tokyo 4 → Fuji lakes 2 → Kyoto 6 → Tokyo 2** route to isolate seasonal differences.

| Dimension | November | May, after Golden Week |
| --- | --- | --- |
| Main scenery | Autumn color in Kyoto/Tokyo; exact timing varies | Fresh greenery, green maples, and other spring flowers; not a Tokyo/Kyoto blossom trip |
| Walking feel | Cooler days and colder evenings; plan earlier hike finishes | Generally warmer conditions for city walks; heat/rain remain possible |
| Photography | My pick for leaves, temple contrasts, reflections, and possible evening light-ups | My pick for green forest scenes, gardens, and brighter spring landscapes |
| Hiking | Low-elevation options; high mountains may have winter conditions | Low-elevation options; verify high-mountain conditions rather than treating May as summer |
| Fuji | Lake/viewpoint visit; summit climb outside normal season | Lake/viewpoint visit; summit climb outside normal season |
| Crowds | Popular foliage locations can be busy; compare real lodging quotes | Golden Week is especially busy; compare the calmer second half of May |
| Clothing/shopping | Browse outerwear and layers if useful at home | Browse lighter pieces if useful at home; exact seasonal stock varies |
| What to verify | Foliage progress, night-visit announcements, daylight, trail access | Holiday dates, garden/flower conditions, rain forecasts, trail access |

[JNTO November](https://www.japan.travel/en/guide/november/) · [JNTO May](https://www.japan.travel/en/guide/may/) · [National parks seasons and climate](https://faq.japan-travel.jnto.jp/national-parks/plan-your-visit/seasons-and-climate/) · [Fuji season](https://www.fujisan-climb.jp/en/season/).

May's second half is my starting window for warmer walking and greenery. JNTO notes that Tokyo/Kyoto's cherry blossoms have generally finished by May; later northern blossom travel requires a different regional route. Neither season guarantees sun or a clear Fuji view, and no claim that either is always cheaper is supported without dated quotes.

## May adaptation of the autumn itinerary

Keep the same hotels/base count provisionally and make these changes:

| Days | May version |
| --- | --- |
| 1–4 | Tokyo arrival, Asakusa, Kichijoji, and Takao or a garden; photograph greenery rather than chasing leaf color. |
| 5–6 | Fuji lakes, choosing two manageable viewpoints and keeping weather flexibility. |
| 7 | Kyoto transfer; rest and easy dinner. |
| 8 | Nanzen-ji/Eikando area for green maples and architecture; no autumn illumination assumed. |
| 9 | Arashiyama river/greenery and one chosen temple. |
| 10 | Tofuku-ji for green-maple scenery, or a lighter central Kyoto day. |
| 11 | Uji matcha/café outing. |
| 12 | Daimonji OR Kurama–Kibune if conditions suit; a city fallback remains available. |
| 13–15 | Tokyo return, Tamiya plus selected gifts/clothing, packing, departure. |

Kyoto confirms that its well-known autumn maple sites are also green-maple destinations. [Official green-maple suggestions](https://global.kyoto.travel/en/faq/detail.php?faq_id=1034). Admission, opening days, and trail access require the actual May dates.

## How I would choose for you

- **November:** first choice if the trip centers on seasonal photography and Kyoto temple scenery.
- **May:** first choice if warmer walking days and greenery matter more than autumn color.
- **Summer:** the season to investigate a Fuji summit climb, plus festival possibilities, while adapting city days to heat.

These are personal recommendations based on your interests. All three retain cafés, matcha, vintage clothes, records, Tamiya, and her gifts; those interests do not require a particular season.

## Decision record

Preferred season: … · year: … · arrival/departure: … · main scenery goal: … · preferred hike effort: … · Fuji scenic visit/summit: …

Before choosing, compare full hotel/transport quotes for the same night count, flight arrival/departure dates, and cancellation terms. Save the result in the seasonal planning note. The summer, November, and May concepts are alternatives; their budgets are not added together.
'''
NOTES['Japan 2027 — Seasonal Planning and Bookings.md']='''# 🧭 Seasonal planning, budget, and bookings

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Summer Guide|Summer]] · [[Japan 2027 — Autumn Guide|November]] · [[Japan 2027 — November vs May|May comparison]]

## Assumptions and decisions

Inherited research: **2027**, **15 calendar days / 14 nights**, one traveler for the budget example, **US$5,000 in Japan excluding international flights**. These are working assumptions for comparing the new guides, not newly confirmed dates or spending authorization. Existing flights/hotels remain unconfirmed.

| Decision | Working plan | Final choice |
| --- | --- | --- |
| Season / year | Summer first, then November versus May | … |
| Length / travelers / rooms | 14 nights, one-person budget example | … |
| Arrival and departure | Tokyo return; compare KIX departure | … |
| Summer Fuji | Scenic two-night lake stay; summit branch separate | … |
| Hiking | Choose one accessible outing; effort unconfirmed | … |
| Regional variation | Kamikochi only by replacing Kyoto nights | … |
| Gifts | Up to US$200 for her; relationship to US$300 shopping remains open | … |

## Provisional cost ceilings for comparison

These are my planning allocations, **not quoted prices**. They replace the blossom guide's category example for evaluating each seasonal alternative; they do not change that guide's budget or create three trip commitments.

| Category | US$ planning amount | Before booking |
| --- | --- | --- |
| Accommodation | 2,100 | 14-night total, taxes/fees included; average target US$150/night |
| Meals and drinks | 600 | Up to 15 calendar days, US$40/day target |
| Intercity transport | 400 | Fuji access and Kyoto/Tokyo travel quotes; record legs once |
| Local and airport transport | 250 | Hotel/airport routes and day-trip local legs |
| Admissions / activities | 300 | Exact temples, viewpoints, cable cars/ropeways, and selected events |
| Connectivity / insurance | 150 | Actual cover and connection choice |
| Shopping / miscellaneous | 300 | Your purchases and gifts according to the chosen scenario |
| Planned subtotal | **4,100** | Rebuild from actual quotes |
| Unassigned reserve | **900** | Maintain visibly until costs are known |
| Total in-Japan envelope | **5,000** | International flights excluded |

**Gift scenarios:** if her US$200 is inside shopping/miscellaneous, it leaves up to US$100 for your other purchases; revise prior personal category caps accordingly. If additional, planned spending becomes **US$4,300**, reserve **US$700**, inside the same US$5,000 ceiling. This scenario does not confirm extra spending. Her suggested US$80 fashion / US$50 beauty / US$50 sweets / US$20 flexible reserve total US$200; count each purchase once.

**Fuji summit branch:** hut, guide, equipment, admission, and extra transport need actual quotes. Replace the relevant accommodation/transport/activities amounts, then reassess the reserve and route. Do not treat the US$300 activities allocation as proof that a guided climb fits. Gear bought separately and international flights need explicit separate tracking.

Use the actual yen/payment exchange rate and fees. Compare **committed reservation totals + remaining estimates** with the ceiling; deposits are part of the full reservation cost, not an additional cost. No seasonal rate or exact airfare has been checked.

## Reservation record — empty until booked

| Item / route | Dates | Full total / currency | Paid / due | Cancellation deadline and time zone | Confirmation / source |
| --- | --- | --- | --- | --- | --- |
| International flights | TBD | TBD | — | TBD | — |
| Tokyo first block | TBD | TBD | — | TBD | — |
| Kawaguchiko lodging | TBD | TBD | — | TBD | — |
| Kyoto lodging | TBD | TBD | — | TBD | — |
| Tokyo final block | TBD | TBD | — | TBD | — |
| Intercity transport | TBD | TBD | — | TBD | — |
| Selected paid experience | TBD | TBD | — | TBD | — |
| Fuji hut / guide, only if chosen | TBD | TBD | — | TBD | — |

No reservation, payment, or hold has been made. A dated shortlist is not a booking confirmation.

## Checks at the useful time

1. **Before setting dates:** choose year/season, hiking level, Fuji goal, traveler count, and airports; compare full route quotes.
2. **Before each booking:** verify the dated official timetable/access notice, exact price, luggage/inclusions, cancellation terms, and running total.
3. **When annual announcements appear:** update festival arrangements, Fuji openings/fees/reservation rules, autumn illuminations, and relevant transport booking windows. Current 2026 details are not 2027 confirmation.
4. **Close to departure:** recheck entry/transit requirements for your actual nationality/route, attraction/trail access, and local conditions; use [[Japan 2027 — Travel Essentials|the existing essentials]] as a checklist reference and refresh date-sensitive facts.
5. **Once dates are chosen:** create seasonal dated pocket cards, actual station-to-hotel routes, and calendar-specific opening checks. Do not reuse the blossom cards' dates.
6. **Each evening:** back up photos, record spending, and settle next day's main stop and fallback.

## Reusable research

[[Japan 2027 — Shopping Shortlist]] · [[Japan 2027 — Clothing to Browse Online]] · [[Japan 2027 — Gifts for Her]] · [[Japan 2027 — Kichijoji Shopping and Exploring]] · [[Japan 2027 — Photography and Filming Wishlist]]

These notes supply interests, links, size references, and purchase ideas. Their date-specific March/April routes and October 2026 stock claims must be rechecked for the chosen season. Map exports from the blossom route need updating if destinations change.
'''

def validate(root):
    planned=set(NOTES)
    for name in planned:
        s=(root/name).read_text()
        assert s.startswith('# ') and len(s)>400
        for target in re.findall(r'\[\[([^\]|#]+)',s):
            filename=target+'.md'
            assert filename in planned or (V/filename).exists(), (name,target)
    budget=(root/'Japan 2027 — Seasonal Planning and Bookings.md').read_text()
    assert '4,100' in budget and '900' in budget and sum([2100,600,400,250,300,150,300,900])==5000
    for name in ['Japan 2027 — Summer Guide.md','Japan 2027 — Autumn Guide.md']:
        s=(root/name).read_text()
        assert all(re.search(r'\| '+str(day)+r' /',s) for day in range(1,16))

if '--install' in sys.argv:
    manifest=json.loads((W/'manifest.json').read_text())
    for name,h in manifest.items():
        p=V/name
        assert not p.exists() if h is None else hashlib.sha256(p.read_bytes()).hexdigest()==h
    (W/'backup').mkdir(exist_ok=True)
    for name,h in manifest.items():
        if h is not None: shutil.copy2(V/name,W/'backup'/name)
        shutil.copy2(W/'staged'/name,V/name)
    validate(V)
    assert all((V/name).read_bytes()==(W/'staged'/name).read_bytes() for name in manifest)
    print('Saved and verified 6 seasonal notes and dashboard link; original dashboard backed up.')
else:
    (W/'staged').mkdir(parents=True,exist_ok=True)
    manifest={}
    for name,s in NOTES.items():
        assert not (V/name).exists(),name
        (W/'staged'/name).write_text(s);manifest[name]=None
    name='Japan 2027 — Start Here.md';original=(V/name).read_bytes()
    manifest[name]=hashlib.sha256(original).hexdigest()
    s=original.decode();i=s.index('\n')+1
    s=s[:i]+'\n**Other seasons:** [[Japan 2027 — Seasonal Guides|Summer guide, November autumn guide, and November-versus-May comparison]]\n'+s[i:]
    (W/'staged'/name).write_text(s)
    (W/'manifest.json').write_text(json.dumps(manifest))
    validate(W/'staged')
    print('Prepared 6 seasonal notes, two 15-day routes, summit alternative, comparison, budget/booking records, and dashboard link; links and counts checked.')
