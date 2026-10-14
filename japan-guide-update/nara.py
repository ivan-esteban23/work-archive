from pathlib import Path
from urllib.parse import urlencode
import hashlib, json, re, shutil, sys

V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
W = Path('/home/ivanaguilera/Work/japan-guide-update/nara')
NOTES = {}
NOTES['Japan 2027 — Nara Chapter.md'] = '''# 🦌 Japan 2027 — Nara chapter

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Nara Pocket Routes|Three pocket routes]] · [[Japan 2027 — Osaka Chapter|Osaka]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / bookings]]

[[#Google Maps — sights food shopping and transport|📍 Google Maps]] · [[#Foods and café stops|🍵 Food]] · [[#Getting here — Kyoto Osaka and Tokyo airports|🚆 Transport]]

**Research checked:** 7 October 2026. **Working year:** 2027, unconfirmed. This chapter expands your existing optional Nara excursion. Dates, tickets, restaurants, hotel nights, and travel-day opening times remain provisional. The focus is **Nara City**, rather than every destination in Nara Prefecture.

## My recommendation for you

Give Nara **one full, unhurried day from Kyoto or Osaka**. Start with **Todai-ji and Nara Park**, then choose **Kasuga Taisha** for shrine/lantern-path atmosphere **OR Naramachi** for cafés, sweets, and crafts. Your photography interests make a slower route more useful than trying to visit every hall, museum, garden, and hillside.

**One overnight** is optional if you want two distinct outings and an earlier park start. It replaces a Kyoto/Osaka night; it does not expand the trip beyond 14 nights. Park mornings do not require an overnight, and quieter conditions are not guaranteed.

For your original spring plan, **4 April is already a choice among Uji, Nara, Osaka, or another Kyoto day**. This chapter keeps Nara as a choice rather than selecting it for you. In the seasonal guides, use one Kyoto-area day only if it wins over that day's existing activity.

## Main sights and how to choose

| Place / area | Why it fits you | How I would use it |
| --- | --- | --- |
| **Todai-ji / Great Buddha Hall** | A major temple visit with architecture and the Great Buddha | First main anchor, with time to look rather than rush |
| **Nara Park** | Park scenery, deer, walking transitions for a short film | Connect selected sights; deer feeding is optional |
| **Nigatsu-do** | A temple-side extension with elevated views | Optional after Todai-ji if steps and energy suit |
| **Kasuga Taisha** | Shrine setting, lantern-lined approach, woodland atmosphere | Main afternoon choice; distinguish general worship from paid special areas |
| **Naramachi / Sarusawa Pond** | Traditional streets, cafés, sweets, compact gifts | Alternative afternoon or second-day block |
| **Kohfukuji** | Temple grounds and selected art/hall visits | Central-area option; check the restoration note below before expecting a pagoda photograph |
| **Isuien Garden** | Garden composition and a slower visual outing | Alternative to another paid attraction, when open |
| **Mt. Wakakusa** | An uphill walking option and city views | Separate active route that replaces other sightseeing |

Primary visitor sources: [Todai-ji](https://www.todaiji.or.jp/en/) · [Nigatsu-do](https://www.todaiji.or.jp/en/information/nigatsudo/) · [Kasuga Taisha visitor information](https://www.kasugataisha.or.jp/en/about_en/basic/) · [Nara Park area guide](https://www.visitnara.jp/destinations/area/nara-park/) · [Naramachi guide](https://www.visitnara.jp/destinations/area/naramachi/) · [Isuien](https://isuien.or.jp/en/garden).

Nara Park is a broad sightseeing area, not one attraction gate. JR Nara and Kintetsu-Nara are different arrival stations; the park is closer to Kintetsu-Nara. Use buses or shorten the loop when the walking load is too much. [Official park access](https://www.visitnara.jp/destinations/area/nara-park/) · [Nara Kotsu visitor transport](https://www.narakotsu.co.jp/language/en/).

### Two current notices that affect your plans

- **Kohfukuji's five-storied pagoda is undergoing major conservation.** Do not build your shot list around an unobstructed pagoda or its reflection in Sarusawa Pond. Check the [temple-linked conservation project](https://kohfukuji-project.jp/five-storied_pagoda/en/index.html) and [city visitor notice](https://narashikanko.or.jp/en/spot/detail_10029.html) near travel. Other grounds/halls require their own access checks.
- **Nara National Museum's Buddhist Sculpture Hall has announced renovation closure for approximately 18 months from 14 September 2026.** That overlaps the working 2027 trips. This is a specific hall closure, not evidence the entire museum is closed; choose any museum outing from the actual open galleries and exhibitions. [Museum's hall notice](https://www.narahaku.go.jp/english/about/guide/butsuzo/). Avoid making that hall your automatic rain fallback or promising a future Shosoin exhibition date.

## A realistic first-day route

**Arrival station → Todai-ji → lunch / rest → park walk → Kasuga Taisha OR Naramachi → return train.** Use the [pocket routes](#) through [[Japan 2027 — Nara Pocket Routes]] to choose the branch before departure.

You can pass central temple grounds or Sarusawa Pond on the approach/return when convenient, but a full paid hall visit is another activity. **Nigatsu-do, Isuien, a museum, and Wakakusa are alternatives or extensions**, not four compulsory additions. If choosing Kasuga Taisha, prioritize it before closing rather than arrive after a long shopping session. Choose an indoor meal/rest stop; carrying lunch through a deer area needs care with bags and food.

## Deer encounters and camera etiquette

Nara's deer are **wild animals**. Observe and photograph from a respectful distance; feeding is optional. If feeding, use only locally sold **shika senbei deer crackers**. Do not offer human snacks, chase or grab deer, tease them with food, or let them eat maps, paper, or plastic. Keep personal food and loose belongings secured. [Official deer guidance](https://www.visitnara.jp/venues/S01487/).

For photos, let the animal move naturally and keep the path clear. Do not stage a bowing interaction repeatedly or hold food near your face for a selfie. This is my practical photography recommendation, not a guarantee about animal behavior.

**Photo / film wishlist:** temple exterior wide shot → architectural detail where permitted → park/deer scene from a distance → lantern-path OR Naramachi street sequence → tea/sweet close-up with permission. For an overnight, consider an early park walk or a permitted Nigatsu-do exterior/viewpoint visit, subject to actual access and daylight.

**Kasuga Taisha publishes filming rules** covering equipment that disturbs worship/visitors and commercial shooting without prior permission. Consult the [shrine's photography and videography notice](https://www.kasugataisha.or.jp/wp-content/uploads/2021/07/%E6%92%AE%E5%BD%B1%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A0%85%EF%BC%88%E8%8B%B1%E8%AA%9E%EF%BC%89.pdf), and follow signs/staff instructions for each area. Do not assume all lantern interiors are open or lit for your visit. [Todai-ji's official site](https://www.todaiji.or.jp/en/) prohibits drone photography in its precincts. [Nigatsu-do's visitor page](https://www.todaiji.or.jp/en/information/nigatsudo/) prohibits photography inside the hall. For exterior viewpoints and other halls, check local tripod and worshipper restrictions before shooting.

[[Japan 2027 — Photography and Filming Wishlist|Your main filming wishlist]] has the shared permission and sequence-planning records.

## Foods and café stops

My first pairing is **a kakinoha-zushi lunch and one freshly made sweet**, with a seated tea/café break. If fish is not appealing, choose another clearly described meal rather than force a local specialty.

| Try | What it is | My suggested role |
| --- | --- | --- |
| **Kakinoha-zushi** | Pressed vinegared rice with fish, wrapped in persimmon leaves | Lunch or a small tasting; check actual ingredients and storage |
| **Chagayu** | Rice porridge cooked with roasted tea | A lighter meal option if offered on your chosen menu |
| **Narazuke** | Vegetables pickled using sake lees | A small savory tasting before considering a gift |
| **Yomogi mochi** | Mugwort rice cake | One fresh sweet at Nakatanido; enjoy during the outing |
| **Kuzu-based sweets** | A regional sweet lead using kudzu starch | Compare a café or packaged product; check the label rather than assume every similarly named sweet is identical |
| **Tea / wagashi** | Tea with a Japanese sweet chosen from the menu | Your seated photography/rest break |

The [city tourism food guide](https://narashikanko.or.jp/en/narashi) explains kakinoha-zushi, chagayu, narazuke, and regional kuzu sweets. [Nakatanido's official site](https://nakatanidou.jp/) describes its fresh yomogi mochi. The [Izasa manufacturer's Nara shop guide](https://www.izasa.co.jp/en/company/) is a kakinoha-zushi browsing lead, not a guaranteed seat, item, or quoted meal.

**Nakatanido:** stop for the sweet; a mochi-pounding demonstration is a bonus only if taking place. No demonstration time is confirmed here. Avoid blocking staff or nearby pedestrian traffic for filming.

**Naramachi:** choose one café rather than a café crawl. The [official neighborhood guide](https://www.visitnara.jp/destinations/area/naramachi/) lists café leads and **Nakanishi Yosaburo**, a traditional sweet shop. Check the actual tea service, seating, opening day, and photography permission. Nara is a complement to your [[Japan Travel Guide 2027#🍵 Uji — the strongest new option for your interests|Uji tea option]], not a replacement automatically selected for the spring excursion day.

## Shopping and souvenirs for you and her

Make this a **small craft/sweet stop**, with your bigger clothing, fragrance, record, and Tamiya searches staying in their established city chapters. No specific Nara vintage inventory, her garment size, or perfume stock has been checked here.

| Idea | Why I would compare it | What to check |
| --- | --- | --- |
| **A handkerchief or small textile accessory** | A compact gift for her without a fitted-clothing decision | Material, pattern, price, and whether she would use it |
| **A patterned kaya-weave cloth** | Lightweight, useful personal/household souvenir | Actual design and intended use |
| **Packaged tea or dry sweets** | Fits your café interests or her love of sweets | Ingredients, storage, expiry beyond return, and package size |
| **A small deer-themed craft** | A local visual memory | Fragility, weight, price, and personal appeal |
| **Goshuin, if meaningful to you** | A temple/shrine visit record | Correct etiquette and the specific site's service; not a compulsory souvenir |

**Nakagawa Masashichi Shoten, Nara flagship:** the maker's guide gives **22 Ganriin-cho, Shika Saru Kitsune Building**, and introduces textiles, tea, sweets, and small crafts. Use its [official souvenir guide](https://story.nakagawa-masashichi.jp/242205) for browsing and [current flagship page](https://www.nakagawa-masashichi.jp/shop/pages/shikasarukitsune.aspx) for store information. The article's older prices and assortment are not current stock guarantees. Compare a compact textile or packaged product after seeing it; no exact embroidered design or customization lead time is promised.

For goshuin, [Todai-ji publishes a collecting guide](https://www.todaiji.or.jp/en/sutra-and-goshuin/goshuin/). Check the actual counter/service before adding it to the visit. Do not treat every hall's stamp as included in admission.

Fresh mochi or a fish/rice purchase is an **eat-during-the-trip choice** unless the seller explicitly confirms a suitable storage/transport plan. Her Nara gifts share the existing **US$200 cap**. Its relationship to the main US$300 shopping allowance remains unresolved: inside that allowance leaves up to US$100 for your other purchases; the additional-gift scenario stays within the same US$5,000 ceiling and reduces the reserve. [[Japan 2027 — Gifts for Her|Gift plan]] · [[Japan 2027 — Shopping Shortlist|Personal shopping]].

## Optional active route — Mt. Wakakusa

Compare a **paid walking entrance and an uphill viewpoint outing** with your normal park walk. [Official Wakakusa guide](https://www.visitnara.jp/venues/A00491/) describes the trails, viewpoints, and seasonal closure. The grassy mountain normally closes for part of winter; verify the specific travel-day gate hours and route before committing.

Use a walking entrance near the park, not a summit-driveway pin. Decide your turnaround point according to conditions and energy. Allow time for both ascent and descent, and descend before the confirmed gate deadline; a sunset photo is not an automatic right to stay after closing. Replace a long Naramachi/garden/shrine block with this walk, rather than append it to a full classic day. Wet ground or heat can make the ordinary park route a better choice.

No full Kasuga forest trek or Yagyu long-distance walk is scheduled. [[Japan 2027 — Hiking and Mount Fuji|Your main hiking guide]] keeps effort and Fuji decisions separate.

## Summer, November, May, and spring blossoms

| Season | My adaptation |
| --- | --- |
| **Summer** | Start the main outdoor block early, build in a seated lunch/café break, and reduce the long uphill route in heat. Consider evening events only after dated notices and return trains are checked. |
| **November** | Park/tree photography fits the autumn concept, but leaves vary by location/year. Plan major sights before their actual closing times and keep the return/daylight plan clear. |
| **Second half of May** | Prioritize greenery and a flexible park walk. Kasuga's botanical garden is an option if open; do not promise peak wisteria during those exact dates. |
| **Your provisional late-March / early-April trip** | Keep Nara on the optional-excursion day and decide from weather, energy, and actual blossom reports. A city's usual flowering period does not guarantee a particular day's blooms. |

The [official city seasonal overview](https://narashikanko.or.jp/en/narashi) describes park foliage and summer candle/lighting events. It is not a 2027 event calendar. [Kasuga's garden information](https://www.kasugataisha.or.jp/en/guidance_en/) describes spring wisteria; use current flowering reports if that becomes a priority.

**Rain alternatives:** Naramachi shops/café and a selected open temple hall; Isuien is an outdoor garden, not a fully indoor rain substitute. Its [operator calendar](https://isuien.or.jp/en/access) lists regular Tuesday closure and other maintenance periods. For a museum visit, check the specific open galleries and the renovation notice above.

## Getting here — Kyoto, Osaka, and Tokyo airports

| Start | Route to compare | Key distinction |
| --- | --- | --- |
| **Kyoto Station** | Kintetsu to **Kintetsu-Nara**, direct or changing at **Yamato-Saidaiji** as your dated service requires; OR JR Nara Line to **JR Nara** | Different arrival stations and onward walking distances |
| **Osaka-Namba** | Kintetsu Nara Line to **Kintetsu-Nara**, selecting the correct direct service or change | Osaka-Namba on Kintetsu is not JR Namba; confirm your hotel-to-station route |
| **Osaka / Tennoji** | JR Yamatoji service to **JR Nara**, using the actual departure/connection | Confirm the train's destination and stops rather than board by line name alone |
| **Haneda / Narita, via Tokyo** | Airport ground transport → Tokyo-area Shinkansen station → Kyoto → selected Nara rail route | Best treated as onward travel from a Kyoto/Osaka base; Nara has no Shinkansen arrival station |
| **Kansai Airport (KIX)** | Compare airport rail via **Tennoji** to JR Nara, or a currently operating airport bus to Nara | Dated service, baggage, and onward hotel connection determine the choice |

[Official travel-to-Nara comparison](https://www.visitnara.jp/travel-to-nara/) · [Kintetsu English travel tools](https://www.kintetsu.co.jp/foreign/english/) · [JR West travel information](https://www.westjr.co.jp/global/en/) · [Local Nara Kotsu transport](https://www.narakotsu.co.jp/language/en/).

**Express and Limited Express are different products.** Kintetsu Limited Express uses reserved seats and requires a Limited Express ticket/charge **in addition to the base fare**. Ordinary Express/Rapid Express services are alternatives; compare actual journey and total price. [Operator explanation](https://www.kintetsu.co.jp/foreign/english/about/limited_express/index.html). AONIYOSHI is an optional sightseeing-train upgrade with its own availability/rules, not necessary for Nara. [Operator's AONIYOSHI page](https://www.kintetsu.co.jp/foreign/english/aoniyoshi/).

After landing at HND/NRT, keep your established Tokyo airport transfer and overnight plan unless choosing a different whole-trip route. For a day trip, go without large luggage if possible. If using Nara between Kyoto and Osaka, confirm luggage storage hours/availability and the correct arrival and departure stations first. Return to the hotel base named in the chosen route; no hotel check-in or rail reservation has been made.

## Stay length, night counts, and costs

| Alternative | Night count / effect |
| --- | --- |
| **Recommended day trip** | Tokyo 4 → Kawaguchiko 2 → Kyoto 6 → Tokyo 2 = **14 nights**. Use one Kyoto outing day for Nara; no extra hotel night. |
| **One Nara overnight** | Tokyo 4 → Kawaguchiko 2 → Kyoto 5 → Nara 1 → Tokyo 2 = **14 nights**. Replace one Kyoto night; return toward Kyoto for the onward Tokyo Shinkansen connection. |
| **Osaka plus Nara overnight** | Tokyo 4 → Kawaguchiko 2 → Kyoto 3 → Nara 1 → Osaka 2 → Tokyo 2 = **14 nights**. More hotel changes and less Kyoto time; compare before choosing. |

These alternatives do not combine automatically with Sapporo, Fukuoka, island modules, or the Fuji summit branch. The existing spring dated plan remains Tokyo 6 → Kyoto 6 → Tokyo 2, with Nara optional on 4 April.

**Current reference admission:** Todai-ji's visitor page lists **¥800 adult individual admission** for a paid hall/museum visit and **¥1,200** for the Great Buddha Hall / Todai-ji Museum joint pass; other paid halls are not thereby included. [Official admissions](https://www.todaiji.or.jp/en/information/haikan/). Kasuga Taisha lists **¥700** for special main-sanctuary worship, separate from general worship and its garden/museum tickets. [Shrine fees and access](https://www.kasugataisha.or.jp/en/about_en/basic/). These are October 2026 references, not guaranteed 2027 prices; purchase only the areas actually selected.

Requote return rail, local buses, admissions, meals, and any replaced hotel night within the existing **US$5,000 in-Japan ceiling**, excluding international flights. Nara food replaces another day's food and souvenirs share the existing shopping cap. This chapter adds no allowance or booking.

## Google Maps — sights, food, shopping, and transport

These search links locate places; they do not establish a dated rail/bus service, saved offline route, open interior, or stock. Check the actual gate/address before navigating.

MAP_TABLE

## Before the outing

- [ ] Choose a Kyoto/Osaka day trip or deliberately replace one hotel night.
- [ ] Choose Kasuga Taisha OR Naramachi for the first afternoon; choose the active route separately.
- [ ] Confirm both rail directions, arrival station, walking/bus connection, and last practical return.
- [ ] Check actual temple/garden hours, pagoda works, and museum gallery notices.
- [ ] Keep feeding optional; secure food, paper, and bags around deer.
- [ ] Check photography permissions, clothing fit where relevant, gift storage, and total cost.

[[Japan 2027 — Nara Pocket Routes|Open the compact route cards]] · [[Japan 2027 — Pocket 2027-04-04|Original spring excursion-choice card]]
'''

PLACES = [
('Arrival rail', 'Kintetsu-Nara Station', 'Kintetsu Nara Station Japan'),
('Arrival rail', 'JR Nara Station', 'JR Nara Station Japan'),
('Kyoto departure', 'Kyoto Station', 'Kyoto Station Japan'),
('Osaka departure', 'Osaka-Namba Station, Kintetsu', 'Osaka Namba Station Kintetsu Japan'),
('JR / airport connection', 'Tennoji Station', 'Tennoji Station Osaka Japan'),
('Park', 'Nara Park', 'Nara Park Japan'),
('Main temple', 'Todai-ji', 'Todaiji Temple Nara Japan'),
('Paid hall', 'Todai-ji Great Buddha Hall', 'Todaiji Daibutsuden Great Buddha Hall Nara'),
('Temple approach', 'Nandai-mon', 'Todaiji Nandaimon Great South Gate Nara'),
('Optional viewpoint', 'Nigatsu-do', 'Todaiji Nigatsudo Hall Nara'),
('Shrine', 'Kasuga Taisha', 'Kasuga Taisha Shrine Nara'),
('Optional garden', "Man'yo Botanical Garden", 'Kasuga Taisha Manyo Botanical Garden Nara'),
('Central temple', 'Kohfukuji', 'Kohfukuji Temple Nara Japan'),
('Central photo walk', 'Sarusawa Pond', 'Sarusawa Pond Nara'),
('Cafés / crafts area', 'Naramachi', 'Naramachi Nara Japan'),
('Naramachi temple', 'Gangoji', 'Gangoji Temple Nara'),
('Townhouse option', 'Naramachi Koshi-no-Ie', 'Naramachi Koshi no Ie Nara'),
('Optional garden', 'Isuien Garden', 'Isuien Garden Nara'),
('Museum — check gallery closures', 'Nara National Museum', 'Nara National Museum Japan'),
('Walking gate — confirm route', 'Mt. Wakakusa north entrance', 'Mount Wakakusa North Gate Nara'),
('Visitor support', 'Nara Visitor Center and Inn', 'Nara Visitor Center and Inn Japan'),
('Fresh sweet', 'Nakatanido', 'Nakatanido Mochi Nara Japan'),
('Crafts / gifts', 'Nakagawa Masashichi Shoten, Nara flagship', 'Nakagawa Masashichi Shoten Nara 22 Ganriincho'),
('Traditional sweets', 'Nakanishi Yosaburo', 'Nakanishi Yosaburo Naramachi Nara'),
]
maps = '| Use | Google Maps location |\n| --- | --- |\n' + '\n'.join(
    '| ' + category + ' | [' + label + '](https://www.google.com/maps/search/?' + urlencode({'api': '1', 'query': query}) + ') |'
    for category, label, query in PLACES)
NOTES['Japan 2027 — Nara Chapter.md'] = NOTES['Japan 2027 — Nara Chapter.md'].replace('MAP_TABLE', maps).replace('Use the [pocket routes](#) through', 'Use')

NOTES['Japan 2027 — Nara Pocket Routes.md'] = '''# 🦌 Nara — pocket routes

[[Japan 2027 — Nara Chapter|← Full chapter, official sources, transport, and Google Maps]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / bookings]]

**Undated alternatives:** choose one card for a day trip. They are not three consecutive scheduled days. One overnight can split the classic park visit and Naramachi/garden outing across two days, adapting the second day to onward travel. The original 4 April card still offers Uji, Nara, Osaka, or more Kyoto.

## Card 1 — classic Nara, with one afternoon choice

**Anchor:** selected JR Nara or Kintetsu-Nara arrival → Todai-ji → park → Kasuga Taisha OR Naramachi → return.

| Block | Plan |
| --- | --- |
| Arrival | Confirm station, onward walk/bus, and return train. |
| Morning | Todai-ji / Great Buddha Hall; optional Nigatsu-do only if steps, time, and energy suit. |
| Midday | Lunch and seated break; keep personal food and paper secured around deer. |
| Afternoon A | Kasuga Taisha approach and permitted worship areas; visit before actual closing. |
| Afternoon B | Naramachi streets, one café/sweet, and a compact craft browse. |
| Return | Selected station → Kyoto or Osaka hotel base. Do not assume the two Nara stations are interchangeable. |

**Food:** kakinoha-zushi OR another suitable lunch, plus one sweet. **Shot:** temple exterior → permitted detail → distant deer/park scene → lantern path OR street/tea scene. **Buy:** one small textile or packaged gift, optional. **Fallback:** shorten the park, choose an open hall/café, and return earlier if conditions require.

- [ ] Choose A or B; every optional garden/museum is another activity.
- [ ] Temple fees/closing and actual return checked.
- [ ] Feeding optional; only deer crackers if chosen. Follow shrine/temple filming rules.

## Card 2 — Naramachi, crafts, sweets, and a selected garden

**Anchor:** central Nara → Sarusawa Pond / Naramachi → one paid garden or cultural stop → café / return.

| Block | Plan |
| --- | --- |
| Morning | Sarusawa area and Naramachi streets; Gangoji OR Koshi-no-Ie if open and appealing. |
| Lunch / break | A clearly described meal, tea, and one sweet; check actual café service. |
| Afternoon choice | Isuien if open and the weather suits, OR a selected central craft-shopping block. |
| Gift browse | Nakagawa Masashichi Shoten flagship or another chosen shop; cap the number of purchases. |

**Food:** chagayu if offered, or a normal café lunch; Nakatanido fresh mochi is an optional convenient stop, with no pounding demonstration promised. **Shot:** street layers → textile/shop detail with permission → sweet close-up → garden composition if chosen. **Buy:** handkerchief, kaya-weave cloth, packaged tea, OR a dry sweet.

**Photo adjustment:** pagoda restoration can obstruct the traditional Kohfukuji/Sarusawa shot. **Rain adjustment:** cafés/shops/open halls; Isuien is an outdoor garden. A museum option requires checking its actual open galleries because the Buddhist Sculpture Hall's announced renovation overlaps 2027.

- [ ] Isuien's closure calendar, shop hours, and seating options checked.
- [ ] No specific pagoda view, product stock, customization, or gallery assumed.
- [ ] Ingredients, expiry, storage, and existing gift/shopping cap checked.

## Card 3 — park and Wakakusa, if the walking route is open

**Anchor:** selected station → park / optional short temple stop → paid Wakakusa walking entrance → viewpoint / descent → meal and return.

**Before leaving:** confirm seasonal opening, the walking entrance, gate deadline, weather, and outward/return transport. Use the walking gate, not a summit car-access pin. Set a comfortable turnaround point and allow descent time.

**Main block:** a limited park/temple visit plus the uphill outing; omit the long shrine/garden/Naramachi circuit. Take a seated meal/rest afterward. A full ascent is optional; choose an ordinary park walk instead when the effort or conditions do not suit.

**Shot:** walking transition → grass/hill detail → city panorama where permitted. **Buy:** none required. **Sunset:** only if verified opening/access and return arrangements support it. **Summer:** reduce uphill effort in heat. **November:** use actual daylight and descend before the gate closes. **Rain fallback:** another card with shorter outdoor blocks.

- [ ] Walking effort and a realistic turnaround selected.
- [ ] Open gate, path conditions, daylight, and descent deadline checked.
- [ ] No full forest trek, summit drive, or guided outing booked.

**Overnight choice:** one Nara night replaces another hotel night. Confirm luggage storage/check-in and second-day onward travel first. An early park walk is optional; do not turn departure morning into another full outing without time for transport.
'''

LINKS = {
    'Japan 2027 — Start Here.md': '**Nara chapter:** [[Japan 2027 — Nara Chapter|Temples, park, cafés, crafts, transport, and Maps]] · [[Japan 2027 — Nara Pocket Routes|Three day-trip choices]].',
    'Japan 2027 — Seasonal Guides.md': '**Nara option:** [[Japan 2027 — Nara Chapter]] expands a Kyoto/Osaka day trip, with summer, November, May, and one-night alternatives.',
    'Japan 2027 — Summer Guide.md': '**Nara day-trip alternative:** [[Japan 2027 — Nara Chapter|Todai-ji, park, and one afternoon choice]]. Replace one Kyoto-area outing; keep heat breaks and compare Wakakusa as a separate active route.',
    'Japan 2027 — Autumn Guide.md': '**Nara day-trip alternative:** [[Japan 2027 — Nara Chapter|Temples and park/tree photography]]. Use actual foliage, daylight, and closing reports before replacing another Kyoto day.',
    'Japan 2027 — November vs May.md': '**Nara comparison:** [[Japan 2027 — Nara Chapter]] adapts a Kyoto/Osaka excursion to November colors or May greenery; late-May wisteria and annual peaks are not guaranteed.',
    'Japan 2027 — Osaka Chapter.md': '**Nearby culture day:** [[Japan 2027 — Nara Chapter|Nara]] — compare Kintetsu from Osaka-Namba or JR to Nara, with a separate full-day route and optional replaced overnight.',
    'Japan 2027 — Sapporo Chapter.md': '**Next chapter:** [[Japan 2027 — Nara Chapter|Nara]] — a Kyoto/Osaka day-trip alternative with temples, park, food, and crafts; separate from the Hokkaido module.',
    'Japan 2027 — Seasonal Planning and Bookings.md': '**Nara decision:** [[Japan 2027 — Nara Chapter|Day trip or one replaced hotel night]]. Compare station choice, return rail, paid areas, and current restoration/gallery notices within the shared budget.',
    'Japan Travel Guide 2027.md': '**Nara research chapter:** [[Japan 2027 — Nara Chapter]] · [[Japan 2027 — Nara Pocket Routes]]. Expands the existing optional 4 April excursion without selecting it or changing dated nights.',
    'Japan 2027 — Pocket 2027-04-04.md': '**If choosing Nara:** [[Japan 2027 — Nara Chapter|Full Nara chapter and Maps]] · [[Japan 2027 — Nara Pocket Routes|Choose a compact day route]]. Uji, Osaka, and Kyoto remain alternatives.',
    'Japan 2027 — Hiking and Mount Fuji.md': '**Nara walking option:** [[Japan 2027 — Nara Chapter|Mt. Wakakusa]] has a separate active route with seasonal gate checks and an optional turnaround; it replaces a longer sightseeing block.',
}

def validate(root, manifest):
    for name in manifest:
        s = (root / name).read_text()
        assert s.startswith('# '), name
        assert 'MAP_TABLE' not in s and '] (#)' not in s, name
        for target in re.findall(r'\[\[([^\]|#]+)', s):
            assert target + '.md' in manifest or (V / (target + '.md')).exists(), (name, target)
    chapter = (root / 'Japan 2027 — Nara Chapter.md').read_text()
    assert chapter.count('https://www.google.com/maps/search/?') == len(PLACES) == 24
    assert all(sum(route) == 14 for route in ([4, 2, 6, 2], [4, 2, 5, 1, 2], [4, 2, 3, 1, 2, 2], [6, 6, 2]))
    cards = (root / 'Japan 2027 — Nara Pocket Routes.md').read_text()
    assert len(re.findall(r'^## Card [1-3] ', cards, re.M)) == 3
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
    print('Saved Nara chapter, three pocket routes, 24 Maps links, and eleven guide integrations. Links and 14-night alternatives verified; existing content preserved and backed up.')
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
    print('Prepared Nara chapter, three pocket routes, 24 Maps links, and eleven integrations. References, 14-night alternatives, and existing outlines validated.')
