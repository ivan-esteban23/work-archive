from pathlib import Path
import hashlib
import json

ROOT = Path('/home/ivanaguilera/Work/japan-guide-update/preparation-20261008')
VAULT = Path('/home/ivanaguilera/Documents/Obsidian Vault')
STAGED = ROOT / 'staged'
BACKUP = ROOT / 'backup'
BACKUP.mkdir(exist_ok=True)
manifest = {}

def stage(name, transform):
    path = VAULT / name
    data = path.read_bytes()
    result = transform(data.decode())
    assert result != data.decode(), name
    (BACKUP / name).write_bytes(data)
    (STAGED / name).write_text(result)
    manifest[name] = hashlib.sha256(data).hexdigest()

def replace(s, old, new):
    assert s.count(old) == 1, repr(old)
    return s.replace(old, new, 1)

PREP = 'Japan 2027 — Preparation Before Choosing Dates'
RECAP = 'Japan 2027 — Session Recap 2026-10-08'

def dashboard(s):
    s = replace(s, '# 🌸 Japan 2027 — Start Here\n', '# 🌸 Japan 2027 — Start Here\n\n> [!info] Research project · clarified 8 October 2026\n> **Season and month are undecided.** Flight searches were tests. The March–April route and dated pocket cards are one blossom-season example; 2027 remains the research label.\n\n**Prepare before choosing dates:** [[' + PREP + '|Season comparison, preparation checklist, and current official sources]]\n')
    s = replace(s, '**Latest recap:** [[Japan 2027 — Session Recap 2026-10-07|7 October continuation]]', '**Latest recap:** [[' + RECAP + '|8 October — season still open and preparation research]]')
    s = replace(s, '**Resume tomorrow:** [[Japan 2027 — Session Recap 2026-10-06|🌙 Saved session recap and next steps]]', '**Previous recaps:** [[Japan 2027 — Session Recap 2026-10-07|7 October]] · [[Japan 2027 — Session Recap 2026-10-06|6 October]]')
    s = replace(s, '> [!info] Working plan · updated 6 October 2026', '> [!info] Blossom-season example · context clarified 8 October 2026')
    s = replace(s, 'These are proposed dates; the guide records no confirmed bookings. Departing Santiago on 25 March would produce a different stay length.', 'These are example dates for researching sakura, not your selected travel window. The guide records no confirmed bookings. When comparing flights, record Santiago departure and Japan arrival separately.')
    s = replace(s, '- [ ] Confirm traveler count, passport nationality, and whether the US$5,000 in-Japan ceiling is per person.\n- [ ] Compare flight itineraries by **local arrival/departure dates**, baggage, connections, and full price; compare Tokyo return with Osaka KIX departure.\n- [ ] Compare total hotel quotes for the resulting nights, including taxes, room requirements, station walks, and exact cancellation terms.', '- [ ] Compare two seasonal windows in [[' + PREP + '|the preparation note]] using scenery, walking conditions and your interests.\n- [ ] Confirm traveler count, passport nationality, and whether the US$5,000 in-Japan ceiling is per person.\n- [ ] Prepare documents, medicine checks, phone/payment backups and walking/camera routines; compare flights and hotels when useful for a clearly labeled scenario.')
    s = replace(s, '| Dates | 25 March–8 April in Japan | Flight dates and local arrival/departure times |', '| Season and dates | Undecided; 25 March–8 April is a blossom example | Compare seasonal windows, then record local flight dates |')
    s = replace(s, '## 💰 Budget you can use', '## 💰 Blossom-example budget')
    s = replace(s, 'The full guide allocates **US$3,850 planned spending + US$1,150 reserve = US$5,000**, excluding international flights.', 'The blossom example allocates **US$3,850 planned spending + US$1,150 reserve = US$5,000**, excluding international flights. The separate [[Japan 2027 — Seasonal Planning and Bookings|seasonal route example]] uses US$4,100 + US$900 reserve, with different transport/activity allowances. Choose one scenario before comparing totals.')
    s = replace(s, '| Early February 2027, adjusted to the actual departure |', '| At least a month before actual departure; earlier if follow-up is needed |')
    return s

stage('Japan 2027 — Start Here.md', dashboard)

def main(s):
    s = replace(s, '# Japan Travel Guide 2027\n', '# Japan Travel Guide 2027\n\n> [!info] Research context · 8 October 2026\n> Your season and month are undecided. Existing March–April dates illustrate a blossom trip, and past flight searches were tests. Start with [[' + PREP + '|preparation and seasonal comparison]]; 2027, 14 nights and the budget remain comparison assumptions.\n')
    s = replace(s, '- Economy round trip, Santiago to Tokyo, 25 March–8 April 2027.', '- Exploratory economy round-trip search, Santiago to Tokyo, 25 March–8 April 2027. You clarified on 8 October that flight searches were tests and no season/month has been chosen. These departure-based search dates need not reproduce the separate sample arrival-based itinerary.')
    return s
stage('Japan Travel Guide 2027.md', main)

stage('Japan 2027 — Seasonal Guides.md', lambda s: replace(s, '# 🗾 Japan — seasonal travel guides\n', '# 🗾 Japan — seasonal travel guides\n\n**Current context · 8 October 2026:** season/month undecided; previous flight searches were tests. [[' + PREP + '|Prepare now and compare seasons using current official sources]].\n'))

def essentials(s):
    s = replace(s, '# 🧳 Japan 2027 — Travel Essentials\n', '# 🧳 Japan 2027 — Travel Essentials\n\n**Before choosing dates:** [[' + PREP + '|Season-neutral preparation and new source checks · 8 October 2026]]. Season/month remain undecided; older dated examples do not set your departure.\n')
    s = replace(s, 'Aim for early February 2027, adjusted to your actual departure and clinical needs.', 'Arrange the consultation relative to your actual departure, ideally at least a month before travel and earlier if clinical follow-up is needed; no travel month has been selected.')
    return s
stage('Japan 2027 — Travel Essentials.md', essentials)

stage('Japan 2027 — Health.md', lambda s: replace(s, '- [ ] Aim for **early February 2027**, allowing time for follow-up before the actual Santiago departure date.', '- [ ] Arrange a pre-travel consultation **at least a month before actual departure**, earlier if follow-up is needed. Season/month are undecided as clarified 8 October 2026; the earlier February example does not set the appointment date.'))

recap = '''# Japan — session recap · 8 October 2026

[[Japan 2027 — Start Here|Dashboard]] · [[Japan 2027 — Session Recap 2026-10-07|Previous recap]]

## User clarification

The travel season and month have not been selected. Earlier flight searches were exploratory tests to learn how to prepare. March–April 2027 is a blossom-itinerary example; the research year, 14-night comparison and budget are provisional.

## Work completed

- Reviewed the latest saved essay and Klook research; saved the audit in `/home/ivanaguilera/Work/japan-guide-update/audit-20261008/Japan research audit.md`.
- Corrected the audit interpretation of the flight searches: differing test dates are not evidence of a travel-planning error. Local dates must agree when a scenario becomes an actual itinerary.
- Added [[Japan 2027 — Preparation Before Choosing Dates]] with current official sources for seasons, regional climate, 2027 holidays, medicine imports, luggage, insurance, arrival procedures and tax changes.
- Updated the dashboard, main-guide context, seasonal index, essentials and health appointment wording to reflect the open season/month.
- Distinguished the blossom budget (US$3,850 + US$1,150 reserve) from the seasonal route model (US$4,100 + US$900 reserve). Both use the same US$5,000 in-Japan envelope, with different allocations.
- Updated the local essay's planning context and rail-pass purchase-channel qualification. It remains a local file for manual upload, not a synchronized ChatGPT-project source.
- Backups and staged files are under `/home/ivanaguilera/Work/japan-guide-update/preparation-20261008/`.

## Pick up next

1. Compare two seasonal windows by scenery, walking comfort and priority experiences; no need to choose immediately.
2. Confirm travelers, passports, rooms and whether the budget is per person before interpreting personalized quotes or entry eligibility.
3. Choose one regional module to develop for each comparison route; quote transport/hotel totals once dates become useful.
4. Recheck remaining Klook packages if selected: exact dates, departure, language, pricing unit, inclusions and cancellation terms remain open.
5. Replace dated pocket cards after choosing a season and arrival date.

Future weather, blooms, exact-year Fuji openings and activity availability remain unconfirmed. No booking, payment, provider contact, account setup or project upload occurred.
'''
(STAGED / (RECAP + '.md')).write_text(recap)

for name in [PREP + '.md', RECAP + '.md']:
    assert not (VAULT / name).exists(), name
    manifest[name] = None

(ROOT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
print('Staged', len(manifest), 'vault notes; backed up', sum(x is not None for x in manifest.values()))
