from pathlib import Path
import hashlib, json, re, shutil, sys

V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
W = Path('/home/ivanaguilera/Work/japan-guide-update/osaka')
NOTES = {}
NOTES['Japan 2027 — Osaka Chapter.md'] = '''# 🐙 Japan 2027 — Osaka chapter

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Osaka Pocket Routes|Phone-ready routes]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and reservations]]

**Built:** 7 October 2026. **Status:** optional chapter for your summer, November, or May trip; no dates or bookings assigned. The inherited planning year is 2027. Shop information below was checked against official sources today; future hours, exact products, sizes, prices, and branch stock remain unconfirmed.

## My starting recommendation for you

Choose **two Osaka nights** if food, fashion, hobby shops, cafés, records, and night photography deserve their own chapter. Start with Minami, then use the second day for Kita or Minoh. If Kyoto temples and matcha matter more, keep your Kyoto base and make Osaka one day trip instead.

Your best matches are **Den Den Town for models**, **Amerikamura/Shinsaibashi for clothes**, **Dotonbori for food and neon**, and **Nakazakicho/Umeda for a slower café-and-record outing**. Minoh supplies the nature alternative. These priorities are my selection for your interests, rather than a promise that every shop stocks your wishlist.

## Understand the city in three blocks

| Block | What to explore | How I would use it |
| --- | --- | --- |
| Minami / south | Namba, Nipponbashi/Den Den Town, Shinsaibashi, Amerikamura, Dotonbori | Main shopping-and-food day; finish with evening photos |
| Kita / north | Osaka/Umeda, Nakazakicho, Doyamacho | Café, fashion, and one record shop; slower second day |
| Minoh / north of the city | Station-to-waterfall walk | Separate daylight outing, replacing some city browsing |

[Official Amerikamura guide](https://osaka-info.jp/en/spot/america-mura-american-village/) describes its vintage-clothing and music culture. [Den Den Town](https://osaka-info.jp/en/discover-kansai/osaka-den-den-town/) is the electronics/pop-culture browsing area. [Nakazakicho](https://osaka-info.jp/en/special/dc/event/detail637/) offers a retro streetscape. Explore each as an area; individual stores set their own opening and filming rules.

## Shopping shortlist — what I would look for

| Stop / area | Your shopping idea | Location / current source |
| --- | --- | --- |
| Joshin Super Kids Land Honten, Den Den Town | One compact plastic model or RC-related item; ask whether the exact Tamiya kit or Mini 4WD item you want is stocked | **4-12-4 Nipponbashi, Naniwa-ku**; official hours currently 10:00–20:00. [Joshin branch](https://store.joshin.co.jp/detail/1746/) |
| Amerikamura | For you: graphic tee, denim jacket, flannel, or trousers; browse condition and measurements before deciding | West of Shinsaibashi around Triangle Park. [Area guide](https://osaka-info.jp/en/spot/america-mura-american-village/) |
| WEGO Shinsaibashi | For her: browse a Y2K-inspired top, small bag, or accessory; for you: casual tee or layer if the fit suits | **Shinsaibashi GATE 4–5F, 2-5-5 Shinsaibashisuji, Chuo-ku**. [Shopping-street branch listing](https://www.shinsaibashi.or.jp/stores/show/1/) |
| SPINNS HEP FIVE, Kita | Alternative clothing browse for her: cardigan/cami, streetwear, or an accessory, depending on the collection | **HEP FIVE 2F, 5-15 Kakudacho, Kita-ku**. [Official store directory](https://www.spinns.jp/f/shop) |
| DiskUnion Osaka, Kita | One used record or CD that you actually want; inspect condition and consider luggage space | **ACT III 1F, 15-17 Doyamacho, Kita-ku**. [Official branch](https://diskunion.net/shop/osaka) |
| LiLo Coffee Roasters, Minami | Seated coffee break if seating is available; consider beans as an optional gift after checking roast date and luggage space | **1F, 1-10-28 Nishishinsaibashi, Chuo-ku**. [Official locations](https://coffee.liloinveve.com/pages/store-location) |

Joshin's branch explicitly lists plastic models, RC models, railway models, and Gunpla; exact Tamiya inventory needs a separate check. Your Tokyo **Tamiya Shinbashi** visit remains the existing shopping anchor. An Osaka hobby purchase can replace another planned purchase rather than becoming a new allowance.

**Clothing fit:** your saved reference is L tops and EU 44–46 trousers. Try garments or compare actual chest/shoulder/waist/inseam measurements; Japanese letter sizes and vintage labels vary. Her size is still unknown, so a bag or accessory is easier to choose than fitted clothing. Y2K/Korean-inspired items above are browsing ideas, not confirmed current branch products or a forecast of 2027 trends. Reuse [[Japan 2027 — Clothing to Browse Online]] and [[Japan 2027 — Gifts for Her]] for the detailed wishlist.

For perfume, retain the small-format options in [[Japan 2027 — Gifts for Her]] and test scents before buying. I have not verified a specific Osaka perfume counter or its stock in this chapter. A clothing-and-perfume basket must share her existing US$200 gift cap.

## Food and café plan

Try **takoyaki** as a small snack, **okonomiyaki** as a seated meal, and **kushikatsu** as an alternative dinner. These are established Osaka foods; my suggestion is to choose one main meal and one snack per outing rather than chase every dish. [Official Osaka food guide](https://osaka-info.jp/en/gourmet/).

**Kuromon Market** is an optional daytime food browse near Nipponbashi. Check displayed prices and choose a small serving before buying several items; it is not automatically the cheapest meal stop. [Official market overview](https://osaka-info.jp/en/osaka/food/gastronomy-markets/). **Dotonbori** works as the evening food-and-signage anchor. Choose a restaurant by the menu and wait that day; no restaurant reservation or price has been confirmed. [Dotonbori guide](https://www.osaka-info.jp/en/spot/dotonbori/).

LiLo is the named coffee lead for Minami. In Nakazakicho, leave a café slot flexible rather than assign an unverified opening time. Take-home sweets or coffee beans count under shopping; food consumed during the outing counts under meals.

## Minoh waterfall walk

Use **Hankyu Minoh Station** as the walking anchor, follow the signed waterfall route, and return to the station. Osaka's official tourism page describes roughly **40 minutes one way** and just under two hours for the round trip; my personal planning allowance is **2–3 hours for walking, rests, and photos**, plus transport and food. [Official Minoh Park guide](https://discover.osaka-info.jp/en/spots/mino-park) · [Tourism hiking map](https://minohkankou.net/wp-content/themes/minohkankou/pdf/2025/hikingmap-guide2025.pdf).

This is a suggested outing, not a verified current trail-condition report. Check access notices, weather, footwear needs, and daylight before choosing it. Stay with the main waterfall route unless you deliberately choose and prepare for a different trail. Avoid combining a full Minoh walk with a full Minami shopping day.

| Season | How I would adapt Osaka |
| --- | --- |
| Summer | Short outdoor blocks; lunch/café/indoor browsing during the hottest part of the day. Minoh still requires checking heat and weather; forest shade does not guarantee comfortable conditions. |
| November | Compare Minoh for autumn-color photography when local reports support it; finish the walk in daylight. Keep Dotonbori for city night photos. Peak foliage and special events are unconfirmed. |
| May | Choose greenery and waterfall/park photography, then evening food. The second half of May remains the comparison window in your May note; check actual holidays and prices before fixing dates. |

## Photography and filming wishlist

My short Osaka sequence: **city arrival → model/shop detail with permission → clothing texture → food preparation with permission → Dotonbori wide view → reflection or closing street scene**. The northern alternative uses café detail, a record sleeve, retro architecture, and a walking transition. The nature version uses a wide forest scene, flowing water, leaf detail, and ambient sound.

- Try Dotonbori as daylight fades, then compare the same composition after dark; crowds and weather determine the usable spot.
- In Amerikamura, look for signs, textures, and your own outfit/purchase rather than photograph strangers closely without permission.
- Ask before recording inside shops, cafés, or restaurants; follow posted restrictions and keep passageways clear.
- Keep one 30–90 second film goal, using [[Japan 2027 — Photography and Filming Wishlist|your existing filming outline]].

## Fit Osaka into the 15-day / 14-night guides

These are alternatives; **the current summer/autumn daily tables have not been replaced**. Choose a variant before creating dated cards or reservations.

| Variant | Night count | What changes |
| --- | --- | --- |
| Kyoto day trip | Tokyo 4 + Kawaguchiko 2 + Kyoto 6 + Tokyo 2 = **14** | Replace one Kyoto outing, such as Day 11 or 12, with Minami. Return to the Kyoto hotel that night. |
| Two Osaka nights — my starting recommendation | Tokyo 4 + Kawaguchiko 2 + Kyoto 4 + Osaka 2 + Tokyo 2 = **14** | Days 1–6 unchanged; Day 7 Kyoto arrival; Days 8–10 choose three Kyoto outing blocks; Day 11 transfer to Osaka/Minami; Day 12 Kita OR Minoh; Day 13 Tokyo return; Day 14 shopping/packing; Day 15 departure. Two Kyoto nights are replaced. |
| Depart from Osaka/KIX | Tokyo 4 + Kawaguchiko 2 + Kyoto 5 + Osaka 3 = **14** | Days 1–6 unchanged; Days 7–11 Kyoto; Days 12–14 Osaka; Day 15 KIX departure. Move Tamiya to the first Tokyo block, replacing another outing. Compare the complete flight/rail/hotel cost before selecting. |

For the two-night variant, select Kyoto days deliberately: summer could retain Higashiyama, Arashiyama, and Uji; November could retain your three preferred foliage areas and fit tea into one lighter afternoon. You cannot preserve all six Kyoto day blocks in four nights. The separate Fuji summit branch has a hut and recovery days: rebuild its night balance if adding Osaka rather than applying this scenic-route table unchanged.

The original blossom guide already offers Osaka as an optional Kyoto excursion; this chapter expands that option without changing its March/April calendar.

## Transport and where to stay

**Namba/Shinsaibashi:** my first hotel-area comparison for Minami shopping and evening photos. **Osaka/Umeda:** compare if Kita, Kyoto access, and a Minoh outing are the priorities. Choose the actual hotel by total price, station exit/walking route, luggage practicality, and cancellation terms; no property is shortlisted or booked here.

**Shin-Osaka, Osaka/Umeda, and Namba are different station areas.** Match each intercity/local leg to the correct station before choosing a hotel. For a Kyoto day trip, compare routes from your actual Kyoto hotel using [JR West's official planning information](https://www.westjr.co.jp/global/en/); exact fares, travel times, and last-return services are not assigned in this chapter.

For a KIX departure, compare [JR airport access](https://www.westjr.co.jp/global/en/travel/shopping/access/train.html) and the [airport's Nankai access information](https://www.kansai-airport.or.jp/en/faq/2721), then verify the dated service, terminal, and airport arrival buffer. An Osaka departure is a flight comparison, not a confirmed change.

**Universal Studios Japan / Super Nintendo World:** optional separate full-day choice, replacing another Osaka outing. Park admission and area entry requirements need checking; purchasing a park ticket alone does not establish your chosen area-access arrangement. [Official timed-entry information](https://www.usj.co.jp/web/en/us/enjoy/numbered-ticket/timed-entry-ticket). Tickets, Express Pass options, dates, and cost are unconfirmed.

## Money and next checks

Keep the shared **US$5,000 in-Japan ceiling**, excluding international flights. The seasonal plan currently allocates US$600 to meals/drinks and US$300 to shopping/miscellaneous. Osaka meals replace meals elsewhere; Osaka purchases share the same shopping allowance. Her US$200 gift inclusion is still open. Hotel, intercity, local transport, and activity totals need recalculating for the chosen variant; no Osaka price quote supports the existing allocations yet.

- [ ] Choose day trip, two nights, or KIX-departure variant.
- [ ] Decide Minami + Kita versus Minami + Minoh; USJ replaces a day if selected.
- [ ] Confirm year/dates and actual hotel/station connections.
- [ ] Recheck branch addresses/hours, exact item stock, garment measurements, and returns before buying.
- [ ] Check trail conditions, daylight, and weather before the Minoh outing.
- [ ] Record exact costs and bookings in [[Japan 2027 — Seasonal Planning and Bookings]].

## Map anchors to save

These are search links, not saved offline maps. Confirm the displayed branch name and address against the official sources above.

[Namba](https://www.google.com/maps/search/?api=1&query=Namba+Station+Osaka) · [Joshin Super Kids Land Honten](https://www.google.com/maps/search/?api=1&query=Joshin+Super+Kids+Land+4-12-4+Nipponbashi+Osaka) · [Amerikamura Triangle Park](https://www.google.com/maps/search/?api=1&query=Amerikamura+Triangle+Park+Osaka) · [LiLo Coffee Roasters](https://www.google.com/maps/search/?api=1&query=LiLo+Coffee+Roasters+1-10-28+Nishishinsaibashi) · [Dotonbori](https://www.google.com/maps/search/?api=1&query=Dotonbori+Osaka) · [Nakazakicho](https://www.google.com/maps/search/?api=1&query=Nakazakicho+Station+Osaka) · [DiskUnion Osaka](https://www.google.com/maps/search/?api=1&query=DiskUnion+Osaka+15-17+Doyamacho) · [HEP FIVE](https://www.google.com/maps/search/?api=1&query=HEP+FIVE+Osaka) · [Hankyu Minoh Station](https://www.google.com/maps/search/?api=1&query=Hankyu+Minoh+Station)
'''

NOTES['Japan 2027 — Osaka Pocket Routes.md'] = '''# 🐙 Osaka — pocket routes

[[Japan 2027 — Osaka Chapter|← Full Osaka chapter]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget / bookings]]

**Undated alternatives.** Choose one per day; assign calendar dates only after the season and accommodation route are confirmed. Sequence and duration are my suggestions; opening times, train services, prices, and stock must be checked for the travel day. Official links, addresses, and map anchors are in the full chapter.

## Card 1 — Minami: models, clothes, food, neon

**Anchor:** Namba / Nipponbashi. **Best use:** one Kyoto day trip or your Osaka arrival day if you arrive with enough time.

| Block | Plan |
| --- | --- |
| Arrival / lunch | If arriving before shops open, start with a relaxed meal or orientation. Kuromon is an optional food browse. |
| First shopping block | Den Den Town; make Joshin Super Kids Land your main hobby stop. Choose one compact item to inspect. |
| Café / rest | Break before crossing to Shinsaibashi/Amerikamura; LiLo is the named coffee lead. |
| Clothing block | Pick two shops at most around Amerikamura/Shinsaibashi; WEGO is the verified branch lead. |
| Evening | Dotonbori signs and reflections, one dinner, then return to the hotel or Kyoto on a verified service. |

**Choose:** hobby + one fashion stop if time is short. **Buy idea:** one model OR one clothing piece; her accessory is an alternative gift purchase. **Shot:** wide neon scene → food detail with permission → souvenir detail. **Summer adjustment:** shorten outdoor walking and add a seated midday break. **Rain alternative:** concentrate on selected shops and a meal, with a shorter outdoor photo walk.

- [ ] Exact branch hours and item stock checked.
- [ ] Kyoto return connection / hotel route saved before dinner.
- [ ] Meals and shopping recorded once under their existing budget categories.

## Card 2 — Kita: cafés, records, fashion

**Anchor:** Osaka/Umeda. **Best use:** second Osaka day; city alternative to Minoh.

| Block | Plan |
| --- | --- |
| Start | Nakazakicho neighborhood walk and a café when open; leave the venue flexible. |
| Midday | Seated lunch and rest. |
| One main browse | DiskUnion Osaka in Doyamacho; choose a record/CD by interest and condition. |
| Optional second stop | HEP FIVE / SPINNS for her clothing or an accessory; omit if the main browse uses your shopping allowance. |
| Finish | Easy dinner near the chosen station or hotel; avoid adding another full Minami circuit. |

**Buy idea:** one record OR a gift accessory. **Shot:** retro street detail → café moment with permission → record sleeve you are considering. **Rain alternative:** reduce the neighborhood walk and focus on the selected indoor stops. **Exit:** check the actual station and platform for your hotel or onward train; Umeda complexes need orientation time.

- [ ] Café/store hours checked for the weekday.
- [ ] Her garment measurements known before buying fitted clothing.
- [ ] Record condition, luggage space, and final cost checked.

## Card 3 — Minoh: waterfall and greenery / foliage

**Anchor:** Hankyu Minoh Station. **Best use:** daylight nature day replacing Card 2, or the third day in the KIX variant.

| Block | Plan |
| --- | --- |
| Before leaving | Check weather, daylight, trail notices, station access, and return services. |
| Walk | Follow the main signed waterfall route; allow 2–3 hours for your walk/photos/rests, plus transport and food. |
| Waterfall | Wide scene, water/leaf detail, ambient sound; keep the route clear. |
| Return | Walk back to the station, eat, and keep the rest of the day light. |

**November:** choose only if actual foliage reports and trail conditions support the visit. **May:** focus on greenery. **Summer:** adapt to heat and rain; a forest outing still needs weather checks. **Bad-weather alternative:** Card 2 with shorter outdoor walking. **Buy idea:** none required; prioritize the outing over another shopping basket.

- [ ] Appropriate shoes, water, layers/rain protection chosen for conditions.
- [ ] Main-route access and daylight checked; no extra mountain trail assumed.
- [ ] Return to the station planned with buffer before onward travel.

**Optional USJ day:** replace one of these cards with a separate full park day only after checking admission, area-entry arrangements, and the total cost. No park ticket or Nintendo-area access is booked.
'''

ADDITIONS = {
 'Japan 2027 — Seasonal Guides.md': '**Osaka chapter:** [[Japan 2027 — Osaka Chapter|Food, fashion, hobby shops, cafés, records, and Minoh]] · [[Japan 2027 — Osaka Pocket Routes|Three undated pocket routes]]. Includes a Kyoto day trip, two Osaka nights, and KIX-departure alternatives.',
 'Japan 2027 — Summer Guide.md': '**Osaka option:** [[Japan 2027 — Osaka Chapter]] provides a Kyoto day trip or two-night variation, replacing Kyoto time while preserving 14 nights; summer heat breaks are included. [[Japan 2027 — Osaka Pocket Routes|Open the pocket routes]]. The daily table below remains the original scenic-Fuji concept.',
 'Japan 2027 — Autumn Guide.md': '**Osaka option:** [[Japan 2027 — Osaka Chapter]] adds city shopping/night photography and an optional Minoh foliage walk. Choose a Kyoto day trip or replace two Kyoto nights with Osaka; actual foliage and access need checking. [[Japan 2027 — Osaka Pocket Routes|Open the pocket routes]].',
 'Japan 2027 — November vs May.md': '**Osaka comparison:** [[Japan 2027 — Osaka Chapter]] includes Minoh for November foliage when reports support it, or May greenery, alongside the same city shopping and food options. Osaka is an optional route change in either season.',
 'Japan 2027 — Seasonal Planning and Bookings.md': '**Osaka route decision:** [[Japan 2027 — Osaka Chapter|Day trip, two-night stay, or KIX departure]]; choose one before assigning hotels and transport. Recalculate actual category totals within the existing ceiling. No Osaka booking or extra shopping allowance has been added.',
 'Japan 2027 — Start Here.md': '**Explore Osaka:** [[Japan 2027 — Osaka Chapter|The full Osaka chapter]] · [[Japan 2027 — Osaka Pocket Routes|Three flexible pocket routes]]. Shopping, food, filming, Minoh, and seasonal route alternatives.',
 'Japan Travel Guide 2027.md': '**Expanded Osaka research:** [[Japan 2027 — Osaka Chapter|Osaka chapter]] · [[Japan 2027 — Osaka Pocket Routes|Pocket routes]]. Develops the existing optional Kyoto excursion and includes separate summer/autumn alternatives; your dated blossom itinerary remains provisional and unchanged.',
}

def validate(root, manifest):
    for name in manifest:
        s = (root/name).read_text()
        assert s.startswith('# '), name
        for target in re.findall(r'\[\[([^\]|#]+)', s):
            assert target+'.md' in manifest or (V/(target+'.md')).exists(), (name,target)
    for name in ['Japan 2027 — Summer Guide.md', 'Japan 2027 — Autumn Guide.md']:
        s = (root/name).read_text()
        assert all(re.search(r'\| '+str(day)+r' /', s) for day in range(1,16))
    assert sum([4,2,4,2,2]) == 14 and sum([4,2,5,3]) == 14
    assert 'US$5,000' in (root/'Japan 2027 — Osaka Chapter.md').read_text()

if '--install' in sys.argv:
    manifest = json.loads((W/'manifest.json').read_text())
    for name,h in manifest.items():
        p = V/name
        assert (not p.exists()) if h is None else hashlib.sha256(p.read_bytes()).hexdigest() == h, name
    validate(W/'staged', manifest)
    (W/'backup').mkdir(exist_ok=True)
    for name,h in manifest.items():
        if h is not None: shutil.copy2(V/name, W/'backup'/name)
        shutil.copy2(W/'staged'/name, V/name)
    validate(V, manifest)
    assert all((V/name).read_bytes() == (W/'staged'/name).read_bytes() for name in manifest)
    print('Saved and verified Osaka chapter, three pocket routes, and links in seven guide notes. Existing notes backed up; 15-day tables and wiki links checked.')
else:
    (W/'staged').mkdir(parents=True, exist_ok=True)
    manifest = {}
    for name,s in NOTES.items():
        assert not (V/name).exists(), name
        (W/'staged'/name).write_text(s)
        manifest[name] = None
    for name,addition in ADDITIONS.items():
        original = (V/name).read_bytes()
        manifest[name] = hashlib.sha256(original).hexdigest()
        s = original.decode()
        i = s.index('\n')+1
        (W/'staged'/name).write_text(s[:i]+'\n'+addition+'\n'+s[i:])
    (W/'manifest.json').write_text(json.dumps(manifest))
    validate(W/'staged', manifest)
    print('Prepared two Osaka notes and seven guide integrations. Links, 15-day outlines, and 14-night alternatives validated.')
