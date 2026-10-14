from pathlib import Path
from urllib.parse import quote_plus
from datetime import date, timedelta
import hashlib, json, shutil, sys, re

WORK = Path(__file__).resolve().parent
VAULT = Path('/home/ivanaguilera/Documents/Obsidian Vault')
STAGE = WORK / 'staged'
INDEX = 'Japan 2027 — Daily Pocket Cards'
DATA = [
('Arrival in Tokyo', 'Tokyo · night 1', 'Reach the hotel, eat, and recover.', 'Airport → confirmed hotel; choose the terminal and transfer after booking the flight.', 'Dinner near the hotel; skip extra sightseeing after a late arrival.', 'Stay at the hotel or a nearby seated café.', 'Confirm flight arrival, hotel address, check-in cutoff, and luggage storage.', 'Hotel neighborhood Tokyo', 'A short neighborhood walk, only if rested.'),
('Asakusa', 'Tokyo · night 2', 'Senso-ji and an easy Asakusa walk; allow a relaxed 2–3 hours.', 'Hotel → Asakusa → hotel; add Kuramae only if energy allows.', 'Lunch in Asakusa; optional Dandelion Chocolate Kuramae break if taking that extension.', 'Shorten the outdoor walk; use a nearby café or return for jet-lag recovery.', 'Check tomorrow’s blossoms; swap with a photo day if needed.', 'Senso-ji Asakusa Tokyo Japan', 'Sumida Park if blooms and energy make it worthwhile.'),
('Chidorigafuchi photography', 'Tokyo · night 3', 'One 2–3 hour photo block: moat views, blossom branches, reflections.', 'Hotel → Chidorigafuchi → meal nearby → hotel; check the actual entrance and crowd routing.', 'Lunch and a seated café break in the same area.', 'Move the photo block to a clearer day; choose one indoor venue from the guide’s rainy-day list.', 'Check flowering and access; evening illumination remains conditional on the 2027 announcement.', 'Chidorigafuchi Tokyo Japan', 'An evening return only if lighting and access are confirmed.'),
('Shinjuku Gyoen', 'Tokyo · night 4', 'Garden photography for 2–3 hours, then an easy Shinjuku afternoon.', 'Hotel → verified garden entrance → lunch in Shinjuku → hotel.', 'Lunch and a seated café in Shinjuku; keep the afternoon light.', 'A café and indoor browsing; reschedule the garden if rain is sustained.', 'Sunday: verify 2027 cherry-season reservations, visiting hours, and last entry.', 'Shinjuku Gyoen Tokyo Japan', 'City scenes; observatory only if access and visibility suit.'),
('Nakameguro', 'Tokyo · night 5', 'Meguro River photography in the afternoon; protect time for light and crowds.', 'Hotel → Nakameguro river area → nearby dinner → hotel.', 'Café in Nakameguro; IVY PLACE in Daikanyama only if using the optional earlier block.', 'Replace the long river walk with cafés and browsing; save outdoor photos for another day.', 'Follow bridge/crowd directions; check current shop notices and any seasonal lighting.', 'Meguro River Nakameguro Tokyo Japan', 'TRAVELER’S FACTORY; Daikanyama only if it fits without rushing.'),
('Tokyo blossom buffer', 'Tokyo · night 6', 'Choose one: best blossom revisit, Ueno, or Yanaka–Nezu.', 'Hotel → one chosen area → hotel early enough to pack.', 'Lunch and one café in the chosen neighborhood.', 'If choosing Ueno, consider one nearby museum after checking admission; otherwise use café/rest time.', 'Confirm Kyoto ticket, station, baggage, and hotel; pack and back up photos.', 'Ueno Park Tokyo Japan', 'Shopping replaces a photo block; it does not add another district.'),
('Tokyo to Kyoto', 'Kyoto · night 7', 'Transfer comfortably; a short local walk after check-in is enough.', 'Hotel → booked Shinkansen station → Kyoto → hotel. Allow a suggested 30–45 minute station buffer plus hotel travel.', 'Buy food at the departure station; dinner close to the Kyoto hotel.', 'Make this a transfer and recovery day; skip the outdoor walk.', 'Use the actual service, ticket entry method, luggage arrangements, and check-in instructions.', 'Kyoto Station Japan', 'Hotel-neighborhood photos if rested.'),
('Philosopher’s Path', 'Kyoto · night 8', 'A relaxed 2–3 hour canal photo walk in eastern Kyoto.', 'Hotel → chosen end of the path → nearby lunch → hotel; map the start after choosing the hotel.', 'Lunch and a seated café near the walking area.', 'Swap with a suitable indoor Kyoto cultural visit; check opening day and access.', 'Check local bloom reports; swap with Fushimi Inari if blossoms are not ready.', 'Philosophers Path Kyoto Japan', 'At most one nearby temple after checking admission.'),
('Kiyomizu and historic Kyoto', 'Kyoto · night 9', 'Kiyomizu-dera, then historic streets; Yasaka/Gion only if energy allows.', 'Hotel → Kiyomizu-dera → historic streets → optional Yasaka → hotel. Allow for slopes, steps, and crowds.', 'Lunch and a seated break in the historic-streets area.', 'Shorten the slope-heavy walk; use a café or one indoor cultural stop instead.', 'Check daytime hours; follow private-lane and photography signs. Night viewing is conditional.', 'Kiyomizu-dera Kyoto Japan', 'A respectful Gion walk; skip it if tired.'),
('Fushimi Inari', 'Kyoto · night 10', 'A 2–3 hour visit at your pace; reaching the summit is optional.', 'Hotel → Fushimi Inari → lunch nearby → hotel or one chosen afternoon stop.', 'Lunch near the shrine; a hotel-neighborhood café for recovery.', 'Reduce or postpone the uphill walk; choose a checked indoor visit and a rest.', 'Saturday: keep the plan flexible; turn back whenever comfortable.', 'Fushimi Inari Taisha Kyoto Japan', 'One blossom session from current reports, or a quiet afternoon.'),
('Choose one excursion', 'Kyoto · night 11', 'Proposed Uji: Byodoin, one tea stop, and a river walk. Choose the excursion the evening before.', 'Kyoto hotel → chosen destination → Kyoto hotel; confirm outward and return services.', 'For Uji, one tea stop from the existing Uji plan plus lunch nearby.', 'Stay in Kyoto for one indoor visit and a café, or take a recovery day.', 'Uji is optional. Nara, Osaka, or more Kyoto replaces it; check return travel before leaving.', 'Byodoin Uji Japan', 'Nara: park/Todai-ji; Osaka: one city outing; Kyoto: blossoms/rest. Pick one.'),
('Final Kyoto photo day', 'Kyoto · night 12', 'Revisit the strongest blossom area; Arashiyama is the alternative.', 'Hotel → one chosen area → hotel with time to pack; keep nearby stops together.', 'Lunch and a seated café in the chosen area.', 'Indoor culture or central tea browsing from the guide, followed by packing.', 'Confirm tomorrow’s train, departure station, ticket, baggage, and hotel.', 'Arashiyama Kyoto Japan', 'Ohara replaces this outing and needs its own checked transport plan.'),
('Return to Tokyo', 'Tokyo · night 13', 'Return, check in, and have an easy local evening.', 'Kyoto hotel → booked Shinkansen → Tokyo hotel; allow station and check-in buffers.', 'Train-day meal; dinner near the Tokyo hotel.', 'Hotel recovery, photo backup, and a nearby indoor meal.', 'Confirm 8 April airport, terminal, flight time, transfer, and luggage arrangements.', 'Tokyo Station Japan', 'A short nearby outing; avoid an essential timed attraction after the train.'),
('Last Tokyo day', 'Tokyo · night 14', 'One final photo area or shopping neighborhood, then pack.', 'Hotel → one chosen area → hotel early; choose the route after the final hotel is booked.', 'Lunch/café in that area; early dinner near the hotel.', 'Choose one indoor shopping area and a café; protect packing time.', 'Back up photos; confirm airport transfer and airline arrival requirements. Revisit hotel choice for an early flight.', 'Tokyo Japan', 'Choose one shopping area from Shops and Cafés, rather than several.'),
('Departure', 'No hotel night', 'Reach the correct airport terminal with all documents and bags.', 'Hotel → confirmed airport terminal. Work backward from airline arrival requirements; add transfer, station walk, and disruption buffer.', 'Simple breakfast or meal along the confirmed airport route.', 'Allow for travel disruption; skip optional sightseeing.', 'Confirm flight/terminal, transfer service, passport, boarding details, and baggage.', 'Tokyo airport Japan', 'Sightseeing only if the confirmed flight comfortably permits it.'),
]

def name(i):
    return f'Japan 2027 — Pocket {(date(2027, 3, 25) + timedelta(days=i)).isoformat()}'

def maps(query):
    return 'https://www.google.com/maps/search/?api=1&query=' + quote_plus(query)

def prepare():
    STAGE.mkdir(parents=True, exist_ok=True)
    original = {}
    for i, (title, base, main, route, food, rain, check, query, optional) in enumerate(DATA):
        d = date(2027, 3, 25) + timedelta(days=i)
        nav = []
        if i: nav.append(f'[[{name(i-1)}|← Previous]]')
        nav.append(f'[[{INDEX}|All days]]')
        if i < 14: nav.append(f'[[{name(i+1)}|Next →]]')
        budget = '**Spend target:** US$40 meals/drinks; transport and admission amounts to fill after checking the route.'
        if i in (6, 12): budget += ' Train fare comes from the US$250 intercity pool.'
        if i in (0, 14): budget += ' Airport transfer comes from the US$200 local/airport pool.'
        card = f'''# {d.strftime('%d %B %Y')} · {title}

{' · '.join(nav)}

**Base:** {base} · **Hotel:** TBD · **Plan:** provisional

**Main stop:** {main}

**Route:** {route}

[Main-stop Maps search]({maps(query)}) · [[Japan 2027 — Maps|Other stops]]

**Food / café:** {food}

**Optional:** {optional}

**Rain backup:** {rain}

{budget}

- [ ] **Before leaving:** {check}
- [ ] Phone/camera charged; payment, water, layers, and rain protection ready.
- [ ] **Tonight:** back up photos, record **actual ¥…**, and check tomorrow’s weather/bookings.

[[Japan 2027 — Today|Fill today’s exact times, route, and spending]] · [[Japan 2027 — Bookings|Reservations]] · [[Japan Travel Guide 2027#🧭 Detailed daily itinerary|Full itinerary]]
'''
        (STAGE / (name(i)+'.md')).write_text(card)
    rows = '\n'.join(f'- [[{name(i)}|{(date(2027,3,25)+timedelta(days=i)).strftime("%d %b")} · {item[0]}]]' for i,item in enumerate(DATA))
    index = f'''# 📱 Japan 2027 — Daily pocket cards

[[Japan 2027 — Start Here|← Dashboard]] · [[Japan 2027 — Today|Today’s editable plan]] · [[Japan Travel Guide 2027|Full guide]]

Open one card on your phone; fill exact times and routes in Today the evening before. These 15 cards follow the proposed **25 March–8 April 2027** itinerary: Tokyo 6 nights → Kyoto 6 nights → Tokyo 2 nights. Swap outdoor outings within a city as weather and blossoms change, keeping transfers and reservations intact.

## Choose your day

{rows}

## Spending targets

The **US$40 daily food/drinks target × 15 dates = US$600** already in the guide. It is a personal allocation, not a menu quote or total daily trip cost. Record actual purchases in yen and convert using your actual rate/fees.

Transport, admissions, and shopping vary by day: use the existing trip pools of **US$200 local/airport transport**, **US$250 intercity rail**, **US$250 attractions/experiences**, and **US$300 shopping/miscellaneous**. Hotel, connectivity/insurance, and reserve stay in the full budget. These cards add no new budget allowance. Replace estimates with actual quotes in [[Japan 2027 — Bookings]].

## Before travel

Hotel addresses, flight terminals, exact routes, fares, hours, and 2027 seasonal access remain to be confirmed. Map links are destination searches; select the correct place and entrance. On buffer days, replace the suggested search with your chosen area. The 4 April card keeps Uji optional alongside Nara, Osaka, or staying in Kyoto.

Prepared 7 October 2026 from the existing guide and its Shops and Cafés note. No new venue availability or 2027 timetable verification was performed.
'''
    (STAGE / (INDEX+'.md')).write_text(index)
    link = f'**Daily pocket cards:** [[{INDEX}|📱 Open a compact plan for each travel date]]'
    for filename in ['Japan 2027 — Start Here.md', 'Japan 2027 — Today.md', 'Japan Travel Guide 2027.md']:
        src = VAULT / filename
        s = src.read_text()
        original[filename] = hashlib.sha256(src.read_bytes()).hexdigest()
        if link not in s:
            pos = s.index('\n')+1
            s = s[:pos]+'\n'+link+'\n'+s[pos:]
        (STAGE / filename).write_text(s)
    (WORK / 'manifest.json').write_text(json.dumps(original, indent=2))
    validate(STAGE)

def validate(root):
    cards = list(root.glob('Japan 2027 — Pocket *.md'))
    assert len(cards) == 15
    for i in range(15):
        s = (root/(name(i)+'.md')).read_text()
        for field in ['**Main stop:**', '**Route:**', '**Food / café:**', '**Rain backup:**', '**Spend target:**']:
            assert field in s, (name(i),field)
        assert len(s.split()) < 300
    index = (root/(INDEX+'.md')).read_text()
    assert all(f'[[{name(i)}|' in index for i in range(15))
    for path in root.glob('*.md'):
        if path.name in ['Japan Travel Guide 2027.md', 'Japan 2027 — Start Here.md', 'Japan 2027 — Today.md']:
            assert f'[[{INDEX}|' in path.read_text()
        if path.name.startswith('Japan 2027 — Pocket') or path.stem == INDEX:
            for target in re.findall(r'\[\[([^\]|]+)',path.read_text()):
                target = target.split('#')[0]
                assert (root/(target+'.md')).exists() or (VAULT/(target+'.md')).exists(), target

def install():
    original = json.loads((WORK/'manifest.json').read_text())
    files = sorted(STAGE.glob('*.md'))
    for filename, expected in original.items():
        assert hashlib.sha256((VAULT/filename).read_bytes()).hexdigest() == expected, f'Changed since preparation: {filename}'
    for p in files:
        if p.name not in original:
            assert not (VAULT/p.name).exists(), f'Already exists: {p.name}'
    backup = WORK/'backup'
    backup.mkdir(exist_ok=True)
    for filename in original:
        shutil.copy2(VAULT/filename, backup/filename)
    for p in files:
        shutil.copy2(p, VAULT/p.name)
    validate(VAULT)
    assert all(p.read_bytes() == (VAULT/p.name).read_bytes() for p in files)
    print(f'Installed and verified {len(DATA)} pocket cards, an index, and 3 navigation links. Backups: {backup}')

if __name__ == '__main__':
    if '--install' in sys.argv: install()
    else:
        prepare()
        print('Prepared and verified 15 pocket cards, an index, and links in 3 existing notes.')
