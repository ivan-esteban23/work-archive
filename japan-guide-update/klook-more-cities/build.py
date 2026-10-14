from pathlib import Path
import json
import re
import shutil
import sys

ROOT = Path(__file__).parent
V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
S = ROOT / 'staged'
S.mkdir(exist_ok=True)
data = json.loads((ROOT / 'results.json').read_text())
NAME = 'Japan 2027 — Klook More Cities and Islands.md'
STEM = Path(NAME).stem
updates, before = {}, {}

def stage(name, text):
    target = V / name
    before[name] = target.read_bytes() if target.exists() else None
    updates[name] = text.encode()
    (S / name).write_text(text)

groups = [
('Fukuoka', 'Japan 2027 — Fukuoka Chapter', 'Compare the Itoshima coast/café outing with your chapter’s Dazaifu alternative; leave a separate city block for Hakata food and shopping.', [
 ('fukuoka',152315,'Coastal photography, a forest café, Shiraito Falls, and salt-pudding stops, departing from Hakata Station.','Confirm the selected guide language, seasonal substitutions, actual free time, and whether café drinks, pudding, and seafood are included.'),
 ('fukuoka-city',81471,'A Nakasu river cruise for a different view of the riverside city and food-stall area.','This is a cruise ticket, not a guided yatai meal. Check boarding location, duration, timetable, and weather policy; arrange food separately.'),
 ('fukuoka',95611,'A wider Kyushu day-trip option advertising Yufuin, a scenic train segment, and alternative temple/hot-spring stops.','The title bundles several possible routes. Verify which package includes the train, Dazaifu versus Nyoirin-ji, Beppu stops, admissions, and enough time in Yufuin. Not a simple Fukuoka city tour.'),
]),
('Nagoya', 'Japan 2027 — Nagoya Chapter', 'For your interests, compare the private city tour first: it explicitly mentions Osu vintage shops. A Takayama/Shirakawa-go trip needs its own full day.', [
 ('nagoya-more',112500,'A private Nagoya tour covering the Toyota Commemorative Museum, Nagoya Castle, and Osu shopping; the summary mentions an English-speaking guide and a bus/subway day pass.','Check the actual duration, museum/castle admission, pass coverage, and time available for vintage/record shopping. The displayed price’s person/group basis is unconfirmed; no rating was supplied.'),
 ('nagoya-more',176604,'A half-day small-group cultural tour advertised around Nagoya Castle and Hisaya-odori Park.','Only the title and rating were returned, with no detailed summary. Check the full itinerary, duration, group size, language, and admission inclusions.'),
 ('nagoya',138507,'A day trip from Nagoya to Takayama’s old streets and Shirakawa-go, with an optional observation-deck component.','Check transfer time, café/meal costs, viewing-deck access, and whether the selected package includes the optional observatory. This visits other towns and does not replace a Nagoya city day.'),
]),
('Nara', 'Japan 2027 — Nara Chapter', 'Compare the Nara-only private option or afternoon coach tour with your existing self-guided Nara day; avoid repeating Kyoto sights just to reach Nara.', [
 ('nara-more',123473,'A private Nara cultural tour focusing on the Great Buddha, temple sculpture, and deer encounters, with some customization advertised.','Confirm start/end location, language, duration, actual temple list, admissions, and person/group pricing. Check whether it starts in Nara or includes transfers; do not assume Kyoto pickup.'),
 ('nara-more',625,'An afternoon coach tour from Kyoto or Osaka, advertised with Todai-ji, Nara Park, Kasuga Taisha, and a licensed English-speaking guide.','Verify your departure city, exact return time, admissions, and whether the advertised special sanctuary visit belongs to the selected package.'),
 ('nara-more',140553,'A combined Nara/Uji day outing listing Byodo-in, the Genji museum, hot spring, and Nara sights.','Confirm exact pickup, group size, included admissions, the hot-spring option, and time in each city. The rating snapshot is 4.0 from 16 reviews. This is a broader alternative to either a Nara-only or Uji-only day.'),
]),
('Osaka', 'Japan 2027 — Osaka Chapter', 'Pick one food tour for a relaxed Osaka evening, or the walking/cruise option if scenery is the priority. Account for your return to Kyoto or stay overnight.', [
 ('osaka',149852,'A guided food outing advertised with 12 dishes and two drinks, local bars, and Osaka food culture.','Check dietary substitutions, alcoholic/nonalcoholic drink options, exact inclusions, neighborhood, and start/end times.'),
 ('osaka',89990,'A Shinsekai night food tour visiting several local eateries.','The title advertises 15 dishes and three drinks, while the summary says 13 dishes and two drinks. Confirm the selected package’s actual inclusions before choosing; these counts are inconsistent in the returned data.'),
 ('osaka',213593,'A guided walk advertised with a Dotonbori river cruise, backstreets, billboards, and street-food stops.','Confirm cruise inclusion and weather contingency, walking duration, and whether food is included or purchased separately.'),
]),
('Sapporo and Otaru', 'Japan 2027 — Sapporo Chapter', 'These require an actual Hokkaido stay and travel days. The autumn outing below belongs to a seasonal alternative, not the provisional spring route.', [
 ('sapporo',148089,'A Sapporo-area cultural outing advertised around Jozankei and the Hill of the Buddha; the summary also mentions shrine, market, factory, and museum possibilities.','Confirm the exact selected route. Do not assume every location in the general summary is included. Check onsen admission, food, transport, and time actually available for bathing.'),
 ('sapporo',135910,'A Sapporo-departure day trip titled with Cape Kamui, Otaru, and Shiroi Koibito Park; the summary mentions the Otaru canal and shopping streets.','The URL references a snowland itinerary while the title describes a coastal itinerary. Verify season, exact route, Cape Kamui access, shopping free time, and included admissions.'),
 ('sapporo',174200,'An autumn-focused Jozankei/Yuni Garden outing describing valley, lake, dam, and foliage stops.','Seasonal research only: the listing describes autumn foliage. Verify operating dates and the exact route for your chosen year; it is not evidence of a March/April or November departure, or peak leaf color.'),
]),
('Okinawa and Kerama', 'Japan 2027 — Okinawa Chapter', 'Use these only with a Naha/main-island stay. Kerama Tokashiki, Ishigaki, Taketomi, and Miyako are different islands with separate access plans.', [
 ('okinawa',142932,'A Naha-departure sightseeing bus offering northern and southern route packages, with aquarium, coast, and shopping stops.','Choose north OR south: the combined title is not a promise to visit every attraction in one day. Check aquarium tickets, audio-guide language, pickup/drop-off, and actual route.'),
 ('okinawa',1555,'A glass-bottom boat experience for seeing marine life without snorkeling; the summary describes a one-hour outing.','Confirm the actual port, transfer from Naha, departure time, visibility/weather policy, and facilities. The result does not establish Naha pickup.'),
 ('okinawa',12454,'A Tokashiki/Aharen Beach swimming and optional snorkeling outing, with return boat transfer from Tomarin described.','The returned summary explicitly calls this summertime-only. Check seasonal dates, ferry versus fast-boat package, snorkeling and lunch inclusions, health/age conditions, equipment, and weather cancellation; do not place it in the spring route automatically.'),
]),
('Kamakura and Enoshima', 'Japan 2027 — Best Islands', 'A full-day alternative from Tokyo combining temples, coastal views, and Enoden scenery. Choose one outing instead of adding it to a blossom-photo day.', [
 ('kamakura',149592,'A Tokyo-departure Kamakura/Enoshima outing advertised with the Great Buddha, shrines, and an Enoden ticket.','Confirm the precise stop list, temple admissions, Enoden segment, guide language, walking/stairs, and Tokyo meeting point.'),
 ('kamakura',196721,'A bus day trip advertising an Enoden ride and separate Kamakura Highlights or Kamakura/Yokohama route choices.','Select the actual route: the title does not guarantee Kamakura, Enoshima, and Yokohama all in one package. Check where free time, admissions, and transfers fit.'),
]),
('Hiroshima and Miyajima', 'Japan 2027 — Best Islands', 'A separate western-Japan route module. Compare a Hiroshima base with an actual rail-inclusive package rather than assuming a low listing price covers long-distance trains.', [
 ('miyajima',76852,'A Hiroshima/Miyajima bus outing describing an English-speaking guide, a scenic ferry, okonomiyaki lunch, and island free time.','Confirm the departure city, ferry route, shrine/museum tickets, lunch package, and actual time on Miyajima. Allow enough time for photography within the tour schedule.'),
 ('miyajima',140942,'A Hiroshima/Miyajima outing advertising ferry travel, English–Spanish guiding, and optional return Shinkansen from other cities.','The displayed price does not confirm the rail-inclusive package. Check Hiroshima start versus Tokyo/Kyoto/Osaka origin, rail tickets, departure/return times, admissions, and whether Spanish guiding is offered on your date.'),
]),
('Naoshima', 'Japan 2027 — Best Islands', 'Compare guided art exploration only after choosing your port, museum priorities, and island stay. The returned private options have substantial displayed prices and unclear pricing units.', [
 ('naoshima',134492,'A private custom Naoshima tour with a local guide.','The generic summary also refers to Kagawa/Takamatsu, so confirm that the itinerary is actually on Naoshima. Check meeting port, ferry/transport, art admissions, duration, person/group price, and customization. No rating supplied.'),
 ('naoshima',76836,'A day tour from Uno or Takamatsu advertising an English-speaking private guide, cycling or public bus, and selected art admissions.','The summary describes about seven hours, Benesse House/Art House admissions included, and Chichu excluded. Confirm all current inclusions and the dated Chichu supplement rather than relying on the summary’s fee; also verify ferries, bicycle availability, and price unit. Only two reviews underpin the 5.0 rating.'),
]),
('Shodoshima', 'Japan 2027 — Best Islands', 'An island bus option if you select a Shodoshima module. Coordinate ferries before choosing a tour date.', [
 ('shodoshima-retry',116307,'A sightseeing bus departing and returning to Tonosho Port, with four island stops and a smartphone audio guide advertised in English and other languages.','Check the exact four stops, bus times, ferry connection buffer, admissions, and mobile audio requirements. The returned summary does not identify every stop or establish Angel Road tide timing.'),
]),
('Yakushima', 'Japan 2027 — Best Islands', 'Choose the actual hiking route and enough island time before booking. These options differ in origin and should not be treated as interchangeable short walks.', [
 ('yakushima',150846,'A small-group Yakushima hiking listing advertising forest scenery, rental equipment on request, and up to six participants.','The summary mentions Taiko Rock and Jomon Cedar together without a clear route distinction. Confirm which course you are booking, start time, distance, elevation, fitness needs, equipment, transfers, and weather policy. The 5.0 rating has only three reviews.'),
 ('yakushima',146665,'A Kagoshima-origin option advertising a high-speed jetfoil and an English-guided Shiratani Unsuikyo forest hike.','Confirm jetfoil tickets, sailing schedule, hike duration, guide language, equipment, return buffer, and the plan if weather disrupts the boat. Only five reviews underpin the 5.0 rating.'),
]),
('Ishigaki', 'Japan 2027 — Best Islands', 'These need an Ishigaki base; an Okinawa/Naha stay alone does not put you at the departure point. Choose a night nature walk or a sea outing according to your interests.', [
 ('ishigaki',120934,'An Ishigaki jungle night outing with possible stargazing when conditions allow.','Confirm pickup zone, guide language, actual duration, walking conditions, and weather policy. A clear sky or particular wildlife sighting is not guaranteed.'),
 ('ishigaki',123808,'A half-day Hamajima landing and boat-snorkeling outing advertising equipment, photo data, showers, and pickup.','Confirm exact pickup area, sea/weather conditions, physical/health requirements, equipment and photo delivery. Hamajima is not Taketomi: this does not satisfy a Taketomi village excursion.'),
]),
('Miyako Island', 'Japan 2027 — Best Islands', 'Treat this as a separate Miyako stay with flights and a local base; decide between a night walk and snorkeling.', [
 ('miyako',153008,'A jungle night walk advertising English-speaking guides, possible star photos, and pickup options around Miyako and connected islands.','The summary says a cloudy outing may still proceed as a jungle walk. Confirm language, pickup eligibility, actual weather policy, duration, and walking conditions.'),
 ('miyako',179115,'Beach-entry snorkeling advertised around turtles, coral, fish, equipment, and photo delivery.','Turtle sightings are not guaranteed. Confirm guide language, health/age suitability, pickup package, and equipment charges. The summary quotes optional wetsuit/prescription-mask supplements of JPY 1,000 each; verify the selected date/package and on-site payment requirements.'),
]),
]

count = sum(len(g[3]) for g in groups)
assert count == 31
text = '''# 🗾 Japan 2027 — Klook more cities and islands

[[Japan 2027 — Start Here|Dashboard]] · [[Japan 2027 — Klook Tours and Experiences|Tokyo, Kyoto, Uji and Fuji shortlist]] · [[Japan 2027 — Bookings|Booking records]]

**Research checked: 7 October 2026.** Added **31 tour/experience options** across the other city chapters and relevant island modules. Fukuoka, Nagoya, Nara, and Osaka appear first, followed by the guide’s other destinations.

These searches did **not** apply travel dates: the extra chapters have no assigned dates. The inherited working year is 2027, but a returned listing does not confirm a departure or package for that year. Use the spring, summer, May, or autumn route only after choosing the actual dates and transport. These destinations are alternatives that replace nights or outings; they do not all fit alongside the Tokyo → Kyoto → Tokyo 14-night plan.

**Prices and ratings:** USD prices below are exactly as returned by Klook. They are snapshots, not confirmed 2027 quotes. Final prices and availability depend on dates, party size, package options, and inventory. Check pricing unit (person/group), inclusions, and cancellation terms on each linked activity. A private listing’s price is not automatically a group total. Ratings reflect the returned review counts, including small samples.

## Start with these comparisons

- **Fukuoka:** Itoshima for coastal photos and cafés; Nakasu cruise for a shorter city experience. A yatai meal is separate from the cruise.
- **Nagoya:** the private city tour explicitly mentions Osu vintage shops; compare the half-day cultural walk if you prefer more independent shopping time.
- **Nara:** the Nara-only private outing or afternoon tour could fit better than repeating several Kyoto sights on a combined bus trip.
- **Osaka:** choose one food tour or a walking/cruise outing. Check the return journey before selecting a late evening while based in Kyoto.
- **Other cities/islands:** choose the destination module first, then the local tour. Keep seasonal and marine options attached to suitable dates and conditions.

## Destinations

'''
for title, chapter, advice, entries in groups:
    text += f'- [[{STEM}#{title}|{title}]]\n'

selected_ids = set()
for title, chapter, advice, entries in groups:
    text += f'\n## {title}\n\n[[{chapter}|Open the guide chapter]]\n\n{advice}\n'
    for key, ident, description, checks in entries:
        item = next(x for x in data[key]['activity_data'] if x['vertical_id'] == ident)
        assert ident not in selected_ids
        selected_ids.add(ident)
        assert item['deep_link'].startswith('https://www.klook.com/')
        r = item['review']
        rating = f"{r['star']}/5 · {r['count']}" if r.get('star') else 'No rating supplied'
        text += f"\n### [{item['title']}]({item['deep_link']})\n\n"
        text += f"**Displayed price:** {item['price']['selling_price']} · **Klook rating:** {rating}\n\n"
        text += description + '\n\n**Check:** ' + checks + '\n'

text += '''
## Checked, but no matching island tour established

- **Taketomi:** two searches returned main-island Okinawa/Kerama and Ishigaki/Hamajima activities, not a verified Taketomi village or water-buffalo-cart tour. Those are different islands, so no substitute was labeled Taketomi. Keep the self-guided ferry/village research in [[Japan 2027 — Best Islands]].
- **Sado:** both searches returned mainland Niigata/Yuzawa activities. No matching Sado island guided option was established in this search; this is not a claim that none exists.
- **Shodoshima:** the first search returned unrelated Itoshima products; a refined search returned the Tonosho-port island bus listed above.

## Turn a choice into a reservation

Choose the destination and dates first. On the linked activity page, compare the exact package, traveler count, language, start/end point, duration, included costs, and cancellation deadline. Fit one main outing into the day and protect transport and hotel check-in time. Record a purchase in [[Japan 2027 — Bookings]] with its actual total, confirmation, and cancellation deadline.

No reservations, payments, flight changes, hotel changes, or dated itinerary additions were made during this research.
'''
stage(NAME, text)

def add_top(name, link):
    s = (V / name).read_text()
    if link not in s:
        head, rest = s.split('\n', 1)
        s = head + '\n\n' + link + '\n' + rest
    stage(name, s)

add_top('Japan 2027 — Klook Tours and Experiences.md', f'**More destinations:** [[{STEM}|31 options for Fukuoka, Nagoya, Nara, Osaka, Sapporo, Okinawa, and the island chapters]]')
add_top('Japan 2027 — Start Here.md', f'**Klook for other cities:** [[{STEM}|Fukuoka, Nagoya, Nara, Osaka and more — 31 tour/experience options]]')
for city in ['Fukuoka','Nagoya','Nara','Osaka']:
    add_top(f'Japan 2027 — {city} Chapter.md', f'**Klook tours to compare:** [[{STEM}#{city}|{city} tour and experience options]]')
add_top('Japan 2027 — Sapporo Chapter.md', f'**Klook tours to compare:** [[{STEM}#Sapporo and Otaru|Sapporo, Otaru, and Jozankei options]]')
add_top('Japan 2027 — Okinawa Chapter.md', f'**Klook tours to compare:** [[{STEM}#Okinawa and Kerama|Main-island and Kerama options]]')
add_top('Japan 2027 — Best Islands.md', f'**Klook island tours:** [[{STEM}|Island options and the Taketomi/Sado search gaps]]')

recap = 'Japan 2027 — Session Recap 2026-10-07.md'
s = (V / recap).read_text()
heading = '## Klook — additional cities and islands'
assert heading not in s
stage(recap, s.rstrip() + f'\n\n{heading}\n\nAdded [[{STEM}|31 additional tour/experience options]] for Fukuoka, Nagoya, Nara, Osaka, Sapporo/Otaru, Okinawa/Kerama, Kamakura/Enoshima, Hiroshima/Miyajima, Naoshima, Shodoshima, Yakushima, Ishigaki, and Miyako. Each has a Klook link, displayed USD price, rating snapshot, and package checks. No travel dates were applied to these searches; seasonal options were marked. Taketomi/Sado searches did not establish matching island tours. Linked the note from the original shortlist, dashboard, and relevant chapters. No booking, payment, or dated-route change was made.\n')

available = {p.stem for p in V.glob('*.md')} | {Path(p).stem for p in updates}
for name, content in updates.items():
    for link in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', content.decode()):
        target = link.split('#',1)[0]
        assert not target or target in available, (name,target)
    if name != NAME:
        old = before[name].decode()
        assert old.split('\n',1)[1] in content.decode() or name == recap
assert text.count('### [') == 31
for title, _, _, _ in groups:
    assert '\n## ' + title + '\n' in text

if '--apply' in sys.argv:
    for name, old in before.items():
        target = V / name
        assert (target.read_bytes() if target.exists() else None) == old, name
    for name, content in updates.items():
        target = V / name
        if before[name] is not None:
            backup = ROOT / 'backup' / name
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup)
        target.write_bytes(content)
        assert target.read_bytes() == content
    print(f'Saved 31 options; read back {len(updates)} files; links and source prices checked; backups retained.')
else:
    print(f'Prepared 31 options in {len(updates)} files; links and source prices checked.')
