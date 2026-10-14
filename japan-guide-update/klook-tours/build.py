from pathlib import Path
import json
import re
import shutil
import sys

ROOT = Path(__file__).parent
VAULT = Path('/home/ivanaguilera/Documents/Obsidian Vault')
STAGED = ROOT / 'staged'
STAGED.mkdir(exist_ok=True)
data = json.loads((ROOT / 'results.json').read_text())
name = 'Japan 2027 — Klook Tours and Experiences.md'
updates = {}
before = {}

def stage(filename, text):
    p = VAULT / filename
    before[filename] = p.read_bytes() if p.exists() else None
    updates[filename] = text.encode()
    (STAGED / filename).write_text(text)

selections = [
    ('Tokyo — food and a local guide', 'tokyo-food', 188779,
     'A food-led evening through Shinjuku and Kabukicho. The listing describes 15 dishes across four eateries.',
     'Consider one evening during 26–30 March, after a lighter afternoon.',
     'Check the selected package’s exact food/drink inclusions, start time, dietary accommodations, and walking distance.'),
    ('Tokyo — food and a local guide', 'tokyo-food', 188797,
     'Guided introduction to Tsukiji’s outer market, Hongwanji Temple, and food traditions; tasting choices are described as flexible.',
     'Use as the main morning outing during the first Tokyo stay, followed by a nearby café.',
     'Food costs are not clearly included in the returned summary. Check what the displayed price covers; choose this or the next Tsukiji tour.'),
    ('Tokyo — food and a local guide', 'tokyo-food', 126018,
     'Another Tsukiji outer-market walking option, with an English-speaking guide described in the listing.',
     'Alternative to the previous Tsukiji listing, rather than an additional market visit.',
     'Check duration, tastings, meeting point, and the selected package’s language. Do not assume access to an auction or restricted wholesale market.'),
    ('Tokyo — food and a local guide', 'tokyo-personal', 95833,
     'Personalized neighborhoods and local stops: the summary mentions Harajuku, Asakusa/Ueno, Yanaka, cafés, and food.',
     'Consider 30 March’s flexible Tokyo block, or recheck for 7 April if you prefer the final stay.',
     'Ask whether your chosen package can cover vintage shops, records, and cafés. Those specialist shopping stops are not guaranteed by the summary. Confirm duration, transport costs, and whether pricing is per person or group. The 5.0 rating is based on only four reviews.'),
    ('Kyoto — guided walks and history', 'kyoto-walk', 148681,
     'A guided Gion walk emphasizing townhouses, a shrine, local tips, and cultural context.',
     'Use within one Kyoto half-day, 1–5 April, instead of repeating a separate Gion walk.',
     'Two returned searches displayed US$ 13.09 and US$ 16.25 for this same activity. Confirm the price for the exact date/package. Seeing a geiko or maiko is not guaranteed; follow the guide’s access and photography rules.'),
    ('Kyoto — guided walks and history', 'kyoto-walk', 87999,
     'A three-hour evening walk through Gion, traditional streets, and temples/shrines as described by the listing.',
     'Alternative to the daytime Gion tour on an otherwise quiet Kyoto evening.',
     'Check the actual start/end time, meeting point, walking route, and guide language. Treat street encounters as incidental, not a booked performance.'),
    ('Kyoto — guided walks and history', 'kyoto-walk', 148498,
     'Nijo Castle history tour. The summary describes admission included and a group of up to ten.',
     'Possible Kyoto culture block on 3 or 5 April; compare against your planned sightseeing.',
     'Confirm that admission and the stated group size apply to the selected package. Check duration and permitted photography areas.'),
    ('Uji and Kyoto — broader day trips', 'uji', 122392,
     'Combines Kinkaku-ji, Kiyomizu-dera, and Uji; the summary mentions Byodo-in, the river, and matcha desserts.',
     'Possible replacement for the 4 April excursion, if you want a structured multi-stop day.',
     'Check departure city, exact pickup, temple admissions, food costs, and time actually allocated to Uji. Several sights overlap your existing Kyoto plan. This is sightseeing, not a verified hands-on matcha workshop.'),
    ('Uji and Kyoto — broader day trips', 'uji', 156282,
     'Bus-based route advertised with Uji/Byodo-in, Fushimi Inari, and Katsuo-ji; the title lists departure from Osaka and Kyoto.',
     'Another 4 April excursion alternative; select a Kyoto departure if that is your hotel base.',
     'Confirm the departure/return stops and actual itinerary: the product URL also references Minoh Falls, which is not clearly specified in the returned title/summary. Check admissions and Uji free time. It is not a dedicated tea ceremony.'),
    ('Fuji — sightseeing day trips from Tokyo', 'fuji', 93901,
     'Photo-stop itinerary advertised around Fuji, Oshino Hakkai, Lake Kawaguchi, and Fujiyoshida street views, departing from Tokyo Station or Shinjuku.',
     'Weather-dependent alternative for one full Tokyo day, preferably the flexible 30 March block.',
     'The listing offers different meeting-point/private-car packages. Check the selected route, group size, guide language, and time at each photo stop; do not assume every mentioned stop belongs to every package.'),
    ('Fuji — sightseeing day trips from Tokyo', 'fuji', 131149,
     'Scenic outing featuring Arakurayama/Chureito views, Lake Kawaguchi’s Oishi Park, and Oshino Hakkai in the listing.',
     'Alternative to the other Fuji tours for the same full-day slot.',
     'Check the actual stop list, walking/stairs, departure and return time, and whether pickup is included. Promotional upgrade wording in the returned listing is not a confirmed 2027 offer.'),
    ('Fuji — sightseeing day trips from Tokyo', 'fuji', 110632,
     'Fuji sightseeing with a Kawaguchiko ropeway ticket advertised in the title, plus Arakurayama and Oishi Park.',
     'Consider if the ropeway matters more than collecting many street-photo stops.',
     'Confirm the ropeway inclusion and its weather-related contingency. Small-group, regular-tour, pickup, and private-charter options appear in the summary; the displayed price does not establish which option you will receive.'),
    ('Optional Kyoto workshops — souvenirs you make', 'tea-focused', 181896,
     'Make a pair of wooden chopsticks in Gion, with optional personalization.',
     'A possible short cultural stop alongside a Kyoto café/shopping block.',
     'The summary says two wood choices are included; other woods cost JPY 1,000–5,000 extra, and engraving also costs extra. Check duration, language, and the full selected cost.'),
    ('Optional Kyoto workshops — souvenirs you make', 'tea-focused', 202375,
     'Beginner-friendly vintage-coin ring workshop, with the finished ring taken home the same day according to the listing.',
     'Optional alternative to the chopstick workshop if a wearable souvenir appeals more.',
     'Confirm coin/material choices, fitting, duration, guide language, and any upgrades in your chosen package.'),
]
assert len({row[2] for row in selections}) == 14

text = '''# 🎟️ Japan 2027 — Klook tours and experiences

[[Japan 2027 — Start Here|Dashboard]] · [[Japan Travel Guide 2027|Full guide]] · [[Japan 2027 — Bookings|Booking records]]

Researched on **7 October 2026** using Klook search. **12 tours plus two optional craft workshops**, chosen around your interest in food, matcha, cafés, shopping, cultural walks, photography, and meaningful souvenirs.

Searches used the provisional Tokyo window **26–30 March 2027**, Kyoto **31 March–6 April 2027**, and Uji **4 April 2027**. Returned listings do not establish that a 2027 departure or package is available. The suggested slots below are planning judgments, not reservations. Nothing here has been booked.

**Prices:** amounts below are exactly as displayed in the returned Klook results, in USD. They are not confirmed trip-date quotes or trip totals. Final price and availability depend on dates, party size, package options, and inventory; check each linked activity. Taxes, inclusions, pricing unit (person/group), and cancellation terms still need confirmation where not specified.

## Where I would start

- **A memorable meal:** compare the Shinjuku food tour with one Tsukiji tour; choose the meal style you prefer.
- **Kyoto context without a full bus day:** compare the two Gion walks and select one, or choose Nijo Castle for history.
- **Shopping/cafés:** the personalized Tokyo walk could fit your interests if the host agrees to the requested neighborhoods and stops.
- **Your matcha priority:** the returned Uji tours are broader sightseeing routes. Compare their actual Uji free time with [[Japan Travel Guide 2027|your existing self-guided Uji plan]]. The tea-ceremony searches did not return a clearly described dedicated ceremony, so none is presented as confirmed here.
- **Fuji photography:** pick at most one Fuji outing. These are sightseeing tours, not summit climbs or guaranteed photography instruction. Views and blossoms depend on conditions; compare the exact route and cancellation terms before committing.

## Compare the shortlist

| Tour / experience | Displayed price | Klook rating / reviews |
| --- | --- | --- |
'''
items = []
for section, key, ident, fit, slot, check in selections:
    matches = [x for x in data[key]['activity_data'] if x['vertical_id'] == ident]
    assert len(matches) == 1
    item = matches[0]
    assert item['deep_link'].startswith('https://www.klook.com/')
    review = item['review']
    rating = f"{review['star']}/5 · {review['count']}" if review.get('star') else 'Not supplied'
    title = item['title'].replace('|', '—')
    text += f"| [{title}]({item['deep_link']}) | {item['price']['selling_price']} | {rating} |\n"
    items.append((section, item, fit, slot, check, rating))

current = None
for section, item, fit, slot, check, rating in items:
    if section != current:
        text += '\n## ' + section + '\n'
        current = section
    text += f"\n### [{item['title']}]({item['deep_link']})\n\n"
    text += f"**Displayed price:** {item['price']['selling_price']} · **Klook rating:** {rating}\n\n"
    text += f"{fit}\n\n**How it could fit:** {slot}\n\n**Check before selecting:** {check}\n"

text += '''
## Choose and book

Keep this as a shortlist. Select one main activity for a half-day or one full-day excursion, accounting for travel, breaks, and your existing route. Gion tours are alternatives to each other; Tsukiji tours are alternatives to each other; Fuji tours are alternatives to each other. A Uji bus tour replaces an excursion rather than adding another city day.

On the linked Klook page, choose the exact date, party size, package, language, and meeting point. Read the itinerary, inclusions/exclusions, mobility requirements, and cancellation cutoff. Record an actual purchase in [[Japan 2027 — Bookings]], including its total currency, confirmation, and cancellation deadline. Avoid counting included food or transport twice in your budget.

Ratings and review counts are snapshots from these searches. Your guide's dates remain provisional. The original detailed routes and daily cards remain available for deciding which activity to choose.
'''
stage(name, text)

def add_top(filename, link):
    s = (VAULT / filename).read_text()
    if link not in s:
        first, rest = s.split('\n', 1)
        s = first + '\n\n' + link + '\n' + rest
    stage(filename, s)

add_top('Japan 2027 — Start Here.md', '**Klook shortlist:** [[Japan 2027 — Klook Tours and Experiences|12 tours and two craft workshops — prices, fit, and booking links]]')
add_top('Japan Travel Guide 2027.md', '**Tours to compare:** [[Japan 2027 — Klook Tours and Experiences|Klook food, cultural walks, Uji/Fuji day tours, and craft experiences]]')
add_top('Japan 2027 — Bookings.md', '**Research shortlist:** [[Japan 2027 — Klook Tours and Experiences|Klook tours and experiences]] — record here only after choosing and booking.')
recap = 'Japan 2027 — Session Recap 2026-10-07.md'
s = (VAULT / recap).read_text()
addition = '''\n## Klook continuation\n\nSearched Klook and added [[Japan 2027 — Klook Tours and Experiences|12 tour options and two craft workshops]] with displayed USD prices, rating snapshots, activity links, route-fit notes, and package checks. Linked the shortlist from Start Here, the full guide, and Bookings. These are research options; 2027 availability and final package pricing are unconfirmed. Dedicated tea-ceremony searches did not produce a clearly described ceremony. No booking or payment was made.\n'''
assert '## Klook continuation' not in s
stage(recap, s.rstrip() + '\n' + addition)

available = {p.stem for p in VAULT.glob('*.md')} | {Path(p).stem for p in updates}
for filename, contents in updates.items():
    for link in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', contents.decode()):
        target = link.split('#', 1)[0]
        assert not target or target in available, (filename, target)
assert text.count('### [') == 14

if '--apply' in sys.argv:
    for filename, old in before.items():
        target = VAULT / filename
        assert (target.read_bytes() if target.exists() else None) == old, f'Changed during preparation: {filename}'
    for filename, contents in updates.items():
        target = VAULT / filename
        if before[filename] is not None:
            backup = ROOT / 'backup' / filename
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup)
        target.write_bytes(contents)
        assert target.read_bytes() == contents
    print('Saved 12 tours and 2 workshops; verified all 5 files and note links. Backups retained.')
else:
    print('Prepared 12 tours and 2 workshops; checked prices, source links, and all 5 files.')
