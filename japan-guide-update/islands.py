from pathlib import Path
import hashlib, json, re, shutil, sys

V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
W = Path('/home/ivanaguilera/Work/japan-guide-update/islands')
NAME = 'Japan 2027 — Best Islands.md'
CHAPTER = '''# 🏝️ Japan — best islands for your trip

[[Japan 2027 — Seasonal Guides|← Seasonal guides]] · [[Japan 2027 — Osaka Chapter|Osaka chapter]] · [[Japan 2027 — Seasonal Planning and Bookings|Budget and reservations]]

**Research checked:** 7 October 2026. **Working year:** 2027, still unconfirmed. This is a selection chapter for your photography/filming, hiking, cafés, food, and gift interests. Recommendations and suggested stay lengths are my judgment; they are not an official island ranking. No island has been added to the dated itinerary or booked.

## My shortlist for you

**Start with Miyajima** for the strongest mix of shrine scenery, a possible hike, food, and a manageable western-Japan detour. **Choose Naoshima instead** if art and architecture are the main reason to visit. **Yakushima** deserves a larger hiking-focused route, and **Ishigaki with Taketomi** works as a dedicated beach-and-village stay. **Enoshima** is the simplest island outing to compare from Tokyo.

Japan's four main islands are major travel regions; this chapter concentrates on smaller island outings rather than treating all of Honshu or Hokkaido as a single stop.

| Island | Best reason to choose it | My suggested time | Fit with your existing route |
| --- | --- | --- | --- |
| **Miyajima / Itsukushima** | Shrine waterfront, views, walking, November foliage | One full day from Hiroshima; compare 1–2 nights in the area | Strong first choice for a western-Japan module |
| **Naoshima** | Contemporary art, architecture, coastal compositions | One full island day; preferably a two-night regional block | Good alternative to Miyajima, with timed museum planning |
| **Shodoshima** | Coastal scenery, olive/soy-sauce culture, gorge greenery or foliage | Two island nights | Slower Setouchi alternative; local transport matters |
| **Yakushima** | Mossy forest, cedars, substantial hiking possibilities | 3–4 island nights plus access/buffer planning | A larger route change; prioritize if hiking becomes the trip's focus |
| **Ishigaki** | Ocean views, guided marine activities, stargazing, island base | Four nights as a starting comparison | Domestic-flight module replacing mainland nights |
| **Taketomi** | Red-roof village streets, crafts, relaxed photography | Day trip from Ishigaki, or a deliberately chosen overnight | Pair with Ishigaki; not an independent mainland detour |
| **Miyako Island** | Beaches and ocean scenery across bridge-linked islands | 3–4 nights | Compare against Ishigaki rather than automatically visit both |
| **Enoshima** | Coastal walk, shrine, viewpoint, an easy change of scene | One Tokyo day outing | Least disruption; no extra hotel base needed |
| **Sado** | Historic port streets, rice terraces, coastal scenery, music culture | 2–3 island nights plus access | Better for a northern-Japan route than your current Kansai emphasis |

The suggested nights include room to slow down, not a guarantee against weather disruption. Flight/ferry days consume part of the stay. Actual connections, hours, fares, trail conditions, and 2027 events need checking after dates are chosen.

## 1. Miyajima — my first choice for this guide

Explore the Itsukushima Shrine waterfront, the town, and a selected temple/park walk. Add **Mount Misen** only if your chosen trail, effort, daylight, and weather suit; a ropeway option still requires checking how much walking remains. In November, **Momijidani Park** is the foliage lead, with actual color timing checked locally. [Miyajima Tourist Association](https://miyajima.or.jp/english/) · [Official Momijidani guide](https://www.miyajima.or.jp/english/spot/spot_momiji.html).

**Photo idea:** compare the waterfront at different tide stages; look up the actual tide times rather than assume one arrival gives both views. Choose shrine/waterfront photography OR a longer Misen outing as the main block. For food, oysters are a regional lead if you enjoy them; decide from the actual menu. [JNTO oyster information](https://www.japan.travel/national-parks/parks/setonaikai/see-and-do/sightseeing-cruise-and-gourmet-oyster-experience/).

**Access:** plan mainland rail to the Hiroshima area, then local travel to Miyajimaguchi and a ferry. A Hiroshima base simplifies luggage and offers a full island day; staying on Miyajima is an alternative if quieter early/late photography is worth the hotel choice. [Official ferry operator](https://miyajima-matsudai.co.jp/en/ticket.html). Exact dated services and any admission/visitor charges remain unquoted.

## 2. Naoshima — art and architecture

Choose a small set of art sites rather than race through every museum: **Chichu Art Museum**, **Benesse House Museum**, and a Honmura/Art House Project block are starting leads. Build the day around ticket availability, then fit coastal walking and lunch around those slots. Chichu and some other facilities currently use dated/timed admission. [Official tickets and facilities](https://benesse-artsite.jp/en/general-information.html).

**Access:** compare **Uno Port**, reached via the Okayama area, with **Takamatsu Port**. Decide your accommodation base before matching ferry arrivals to museum tickets. The official access page contains mixed-year notices, so check the linked operator's actual travel-date timetable. [Benesse access](https://www.benesse-artsite.jp/en/access/index.html).

**Photo idea:** coastline, architectural lines, and permitted outdoor art. Check each facility's photography/filming rules; do not build your film around unrestricted museum interiors. **Teshima** is a possible second island day only if you replace other activities and verify its museum slot and ferries. No art festival has been assumed for 2027.

## 3. Shodoshima — slower scenery and food culture

My two-day split is **Olive Park / food-culture browsing** on one day and **Kankakei Gorge** on another. Add **Angel Road** only when the tide and local access information support the visit; it is a tidal sandbar, not a guaranteed all-day walkway. The island is known for olives, soy sauce, and somen, with gorge greenery and autumn foliage offering different photo subjects. [JNTO Shodoshima guide](https://www.japan.travel/en/sg/jbyj-blog/shodoshima/).

**Gift idea:** a small olive-based product or packaged local food, chosen within the existing shopping cap and checked for your luggage/import needs. **Access planning:** identify the exact ferry port, accommodation, and onward local bus/taxi/rental plan before booking. Widely separated stops should not be treated as one compact walking route. [Local tourism association](https://shodoshima.or.jp/).

**Photo idea:** sea and grove textures in May; gorge color in November when reports support it. Prefer this over Naoshima when scenery and food culture matter more than museums.

## 4. Yakushima — the hiking-focused choice

Start by comparing a **Shiratani Unsuikyo** forest route with the shorter walking options at **Yakusugi Land**. Select an actual mapped course by effort; these names cover different lengths and terrain. A Jomon Sugi outing is a separate strenuous planning decision, not a casual extra after a forest stroll. [Town trail access information](https://www.town.yakushima.kagoshima.jp/soshiki/kanko_machizukuri/kankosushin/kankosite_English/2/756.html) · [Official hiking guidance](https://www.yakushima.or.jp/assets/file/guidance/tozan_guide_en.pdf).

**Photo idea:** moss detail, cedar scale, flowing water, and forest sound. Rain protection for you and the camera matters; check the actual trail/weather notices, particularly for higher routes. A wet island forecast is not a reason to assume every forest trail remains suitable.

**Access:** investigate air connections and sea access via Kagoshima for the chosen dates; match the actual arrival point to your accommodation and trail transport. [JNTO island-access overview](https://faq.japan-travel.jnto.go.jp/en/guide/island-hopping/). I would reserve 3–4 island nights plus mainland/connection buffer as a starting comparison. Rebuild the 14-night route around it instead of stacking it onto Fuji, Kyoto, Osaka, and another island module.

## 5–6. Ishigaki and Taketomi — beach base plus village day

**Ishigaki:** compare staying near the southern town/port for meals and ferry access with a quieter coastal base that needs a more deliberate transport plan. Starting leads are **Kabira Bay scenery**, one coastal viewpoint, and a guided marine outing suited to your experience. **Swimming/snorkeling from Kabira Bay's beach is not permitted**; sightseeing there and an operator-approved marine trip elsewhere are different activities. [Official Ishigaki guide](https://visitokinawajapan.com/destinations/yaeyama-islands/ishigaki-island/).

**Taketomi:** use a separate ferry day for the red-tiled village, streets, crafts, and shore views. The island's minsah weaving is a gift-browsing lead; inspect the actual product and price. Respect residential areas when filming. [Official Taketomi guide](https://visitokinawajapan.com/destinations/yaeyama-islands/taketomi-island/).

**My four-night starting outline:** arrival/orientation → Ishigaki coastal day → Taketomi village day → guided marine outing OR weather-flexible land day → departure. Swap the middle days when operators and conditions justify it. This includes only one neighboring island, not a promise that every ferry excursion runs.

**Access and season:** compare actual flights to Ishigaki, local airport/port travel, and dated ferry services. Warm southern-island scenery does not guarantee beach conditions in May or November. Check wind, waves, and operator advice before choosing water activities. Weather can interrupt flight/ferry plans; leave a mainland buffer before an international departure. [Official Okinawa sea guidance](https://visitokinawajapan.com/wp-content/themes/visit-okinawa_multi-language/lang/en/assets/document/plan-your-trip/useful-information/303/All%20About%20the%20Sea%20in%20Okinawa.pdf).

## 7. Miyako Island — compare if beaches are the priority

Miyako is my alternative to Ishigaki when the trip's purpose is beach scenery and a relaxed coastal stay. Nearby islands connected by bridges add different viewpoints without making each outing a ferry day. Ishigaki is my first comparison if the Taketomi village visit and ferry-based exploration matter more. [Official Miyako Islands guide](https://visitokinawajapan.com/destinations/miyako-islands/) · [JNTO Miyako overview](https://www.japan.travel/en/destinations/okinawa/Okinawa/miyako-island/).

**Plan:** choose one coastal area per day and compare rental car, taxi, bus, or a tour against your actual accommodation location. No car or driving eligibility has been assumed. Follow current beach notices and operator advice for swimming. **Photo idea:** a wide water-color scene, coastal detail, and a permitted viewpoint; do not stop on a bridge roadway for a shot. Give this 3–4 nights before deciding whether the travel cost is worthwhile.

## 8. Enoshima — simplest from Tokyo

Use a Tokyo outing for the shrine area, coast, and **Sea Candle** viewpoint if operating. Choose a manageable island walk with breaks; stairs and an optional cave visit can change the effort. A full Kamakura sightseeing circuit plus every Enoshima stop would make a different, busier day. [Official Fujisawa access and attractions](https://discover-fujisawa.jp/en/access/).

**Photo idea:** coastal layers and later light when weather and your return plan suit. A Fuji view is a bonus, not a guarantee or a replacement for your planned Fuji-lakes visit. Check [official night-event notices](https://discover-fujisawa.jp/en/special/night-event/) before relying on an illumination; current events are not confirmation for 2027.

**Route fit:** replace one Tokyo outdoor block, such as the optional Takao day, and return to the same hotel. This is the easiest first island choice when you want to preserve all 14 nights and the Kansai plan.

## 9. Sado — save for a northern route

Explore **Shukunegi's historic port streets**, coastal scenery, and selected rice-terrace or cultural stops. Taiko culture is another reason to investigate it; a future festival date or performance requires its own confirmation. [JNTO Sado guide](https://www.japan.travel/en/destinations/hokuriku-shinetsu/niigata/sado-island/).

**Access:** compare travel to Niigata and the actual ferry route, then establish local transport. A car can help with dispersed sights, but has not been assumed; check a workable bus/taxi/tour alternative if you are not driving. Suggested time is 2–3 island nights plus connections. For your present Tokyo–Fuji–Kansai focus I would put Miyajima or Naoshima ahead of Sado. [Sado tourism](https://www.visitsado.com/).

## Summer versus November versus May

These are my selection priorities, not weather forecasts or guaranteed foliage/swimming windows.

| Season | First comparisons | What changes the decision |
| --- | --- | --- |
| Summer | Ishigaki/Taketomi or Miyako for a dedicated coastal stay; Yakushima if forest hiking dominates | Heat, rain, sea conditions, transport disruption, and actual activity availability; marine wildlife sightings are never assured |
| November | Miyajima; Shodoshima if gorge scenery matters; Naoshima for art | Current foliage reports, daylight, museum opening calendars, and sea-access conditions |
| Second half of May | Miyajima, Naoshima, or Shodoshima for scenery; Yakushima for mapped forest routes | Actual weather, holiday demand, trail access, and the balance of green landscapes versus city time |
| Any of your three concepts | Enoshima as one Tokyo outing | Travel-day weather, attraction access, and a verified return connection |

## Fit one island module into 15 days / 14 nights

The existing summer/autumn daily tables remain the base concept. Choose one module before creating a revised calendar. The following night counts are deliberate alternatives, not additions to a booked trip.

| Alternative | Nights | Concrete tradeoff |
| --- | --- | --- |
| Enoshima outing | Existing Tokyo 4 → Fuji lakes 2 → Kyoto 6 → Tokyo 2 = **14** | Replace one Tokyo outing; no new hotel base |
| Miyajima module, Tokyo return | Tokyo 4 → Fuji lakes 2 → Kyoto 4 → Hiroshima area 2 → Tokyo 2 = **14** | Two Kyoto nights replaced; use a full Hiroshima-based day for Miyajima. Osaka can remain an optional Kyoto day trip, replacing another outing. |
| Art-island module, Tokyo return | Tokyo 4 → Fuji lakes 2 → Kyoto 4 → Uno/Naoshima area 2 → Tokyo 2 = **14** | Two Kyoto nights replaced; one full Naoshima day. Choose the actual lodging base and ferry before tickets. |
| Miyajima plus Osaka, KIX departure | Tokyo 4 → Fuji lakes 2 → Kyoto 3 → Hiroshima area 2 → Osaka 3 = **14** | Reduces Kyoto to three nights and removes the Tokyo return; move Tamiya into the first Tokyo block. Requires comparing actual international flights. |

**Two-night Miyajima module in the Tokyo-return variant:** Days 1–6 Tokyo/Fuji as before; Day 7 Kyoto arrival; Days 8–10 your three selected Kyoto outings; Day 11 travel to Hiroshima-area accommodation; Day 12 Miyajima; Day 13 Tokyo transfer; Day 14 final shopping/packing; Day 15 departure. Hiroshima city sightseeing needs its own time allocation rather than being implied by the accommodation base. Rail legs and luggage arrangements need quotes.

Yakushima, Sado, and the Okinawa islands deserve a fresh route comparison once selected. The Fuji summit itinerary also needs a separate rebuild: preserve its hut, descent, and recovery blocks instead of borrowing nights invisibly.

## Budget, filming, and final checks

The current ceiling remains **US$5,000 in Japan, excluding international flights**. Island accommodation replaces accommodation elsewhere. Record domestic flights/ferries, local transfers, rental/tour costs, baggage, museums, and chosen activities; no actual island quote proves that a module fits the existing category allocations. Souvenirs share your shopping allowance, and her gifts still share the US$200 gift cap. Track everything in [[Japan 2027 — Seasonal Planning and Bookings]].

My film outline is **arrival crossing → wide island scene → one cultural/nature detail → meal/craft with permission → closing coast/forest scene**. Use [[Japan 2027 — Photography and Filming Wishlist]] and respect museum, shrine, shop, and residential restrictions.

- [ ] Select one island module and the main purpose: scenery, art, hiking, or beaches.
- [ ] Confirm year/dates, departure airport, and which mainland nights/outings it replaces.
- [ ] Match timed admissions to the exact dated ferry/local-transfer plan.
- [ ] Check tides for tidal viewpoints, and current trail or sea conditions for the activity chosen.
- [ ] Compare full costs, cancellation terms, luggage arrangements, and a weather fallback.
- [ ] Save your return connection and avoid relying on a same-day remote-island transfer before the international flight.

**My next comparison for you:** Miyajima versus Naoshima. Choose Miyajima for shrine/coastal/nature photographs; choose Naoshima for art and architecture. Enoshima can remain a separate Tokyo outing if another city activity is replaced.
'''

LINKS = {
 'Japan 2027 — Start Here.md': '**Island chapter:** [[Japan 2027 — Best Islands|Best islands for your interests, seasonal comparisons, and route choices]].',
 'Japan 2027 — Seasonal Guides.md': '**Island options:** [[Japan 2027 — Best Islands|Miyajima, Naoshima, Yakushima, Okinawa islands, and more]] — compare one module before changing the itinerary.',
 'Japan 2027 — Summer Guide.md': '**Island alternatives:** [[Japan 2027 — Best Islands]] compares beach stays, forest hiking, art islands, and an Enoshima Tokyo outing. Multi-night islands replace existing bases; the daily outline remains unchanged.',
 'Japan 2027 — Autumn Guide.md': '**Island alternatives:** [[Japan 2027 — Best Islands]] includes Miyajima and Shodoshima foliage leads and a Naoshima art option; actual color timing and travel-day access need checking.',
 'Japan 2027 — November vs May.md': '**Island scenery comparison:** [[Japan 2027 — Best Islands]] adds November foliage and May greenery choices, with suggested stays and explicit mainland-night tradeoffs.',
 'Japan 2027 — Osaka Chapter.md': '**Continue west / island alternatives:** [[Japan 2027 — Best Islands]] includes Miyajima and Naoshima modules and a 14-night Miyajima-plus-Osaka concept with KIX departure, subject to flight comparison.',
 'Japan 2027 — Seasonal Planning and Bookings.md': '**Island decision:** [[Japan 2027 — Best Islands|Choose one island module]] before revising hotel nights, transport, and activities. Requote the entire route within the current ceiling; no island reservation or extra allowance has been added.',
 'Japan Travel Guide 2027.md': '**Island research chapter:** [[Japan 2027 — Best Islands|Island shortlist, season comparison, and route alternatives]]. Optional research; no dated blossom days have been reassigned.',
}

def validate(root, manifest):
    for name in manifest:
        s = (root/name).read_text()
        assert s.startswith('# '), name
        for target in re.findall(r'\[\[([^\]|#]+)', s):
            assert target+'.md' in manifest or (V/(target+'.md')).exists(), (name,target)
    for name in ['Japan 2027 — Summer Guide.md','Japan 2027 — Autumn Guide.md']:
        s = (root/name).read_text()
        assert all(re.search(r'\| '+str(day)+r' /',s) for day in range(1,16))
    assert sum([4,2,4,2,2]) == 14 and sum([4,2,3,2,3]) == 14
    assert 'US$5,000' in (root/NAME).read_text()

if '--install' in sys.argv:
    manifest = json.loads((W/'manifest.json').read_text())
    for name,h in manifest.items():
        p = V/name
        assert (not p.exists()) if h is None else hashlib.sha256(p.read_bytes()).hexdigest() == h, name
    validate(W/'staged',manifest)
    (W/'backup').mkdir(exist_ok=True)
    for name,h in manifest.items():
        if h is not None: shutil.copy2(V/name,W/'backup'/name)
        shutil.copy2(W/'staged'/name,V/name)
    validate(V,manifest)
    assert all((V/name).read_bytes() == (W/'staged'/name).read_bytes() for name in manifest)
    print('Saved and verified island chapter covering nine islands, seasonal comparison, four route alternatives, and links in eight guide notes. Originals backed up.')
else:
    (W/'staged').mkdir(parents=True,exist_ok=True)
    assert not (V/NAME).exists()
    (W/'staged'/NAME).write_text(CHAPTER)
    manifest = {NAME:None}
    for name,addition in LINKS.items():
        original = (V/name).read_bytes()
        manifest[name] = hashlib.sha256(original).hexdigest()
        s = original.decode(); i = s.index('\n')+1
        (W/'staged'/name).write_text(s[:i]+'\n'+addition+'\n'+s[i:])
    (W/'manifest.json').write_text(json.dumps(manifest))
    validate(W/'staged',manifest)
    print('Prepared island chapter and eight integrations; wiki links, existing 15-day outlines, and 14-night variants checked.')
