from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import uuid

VAULT = Path('/home/ivanaguilera/Documents/Obsidian Vault')
WORK = Path(__file__).parent
STAGED = WORK / 'staged'
STAGED.mkdir(exist_ok=True)
updates = {}
originals = {}

def stage(name, content):
    target = VAULT / name
    originals[name] = target.read_bytes() if target.exists() else None
    updates[name] = content.encode()
    p = STAGED / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(updates[name])

def add_link(name, link):
    text = (VAULT / name).read_text()
    if link not in text:
        first, rest = text.split('\n', 1)
        text = first + '\n\n' + link + '\n' + rest
    stage(name, text)

expense_name = 'Japan 2027 — Expenses.md'
place_name = 'Japan 2027 — Place Inbox.md'
cards_name = 'Japan 2027 — Japanese Flashcards.md'
help_name = 'Japan 2027 — Quick Capture.md'
recap_name = 'Japan 2027 — Session Recap 2026-10-07.md'

stage(expense_name, '''# 💴 Japan 2027 — Expenses

[[Japan 2027 — Start Here|Dashboard]] · [[Japan 2027 — Quick Capture|Capture instructions]] · [[Japan 2027 — Bookings|Reservations]]

Use **Japan — Expense** in the command palette to add a payment. Enter a plain numeric amount and its original currency (JPY, USD, or CLP). Record the spending date, category, item, and payment method. Entries below are actual payments; estimates belong in the planning budget.

Keep currencies separate until you record the conversion rate, date, and fees. A reservation payment already included in Bookings must be counted only once when calculating overall spending. This note does not calculate totals automatically.

## Entries
''')
stage(place_name, '''# 📍 Japan 2027 — Place Inbox

[[Japan 2027 — Start Here|Dashboard]] · [[Japan 2027 — Quick Capture|Capture instructions]] · [[Japan 2027 — Maps|Maps index]]

Use **Japan — Place** to save a discovery. Include the exact branch and a source or Maps URL when available. New entries are research ideas: verify the branch, opening hours, and route before adding them to a day plan or the interactive map.

## Entries
''')

practice = (VAULT / 'Japan 2027 — Japanese Practice.md').read_text()
selected = {
    'Excuse me / sorry', 'Please speak slowly.', 'Could you say that once more?',
    'Sorry, I don’t understand.', 'One of this, please.', 'A matcha latte, please.',
    'What do you recommend?', 'I’ll have it here.', 'To take away, please.',
    'The bill, please.', 'How much is this?', 'May I try this on?',
    'Can I listen to this before buying?', 'May I take a photo?',
    'Can I pay by card?', 'I don’t need a bag.', 'Where is the restroom?',
    'Do I need to change trains?',
}
cards = []
for line in practice.splitlines():
    if not line.startswith('| '):
        continue
    cells = [c.strip() for c in line.strip('|').split('|')]
    if len(cells) == 3 and cells[0] in selected:
        cards.append(f'{cells[0]}::{cells[1]} — {cells[2]}')
assert len(cards) == len(selected)
for japanese, pronunciation, meaning in [
    ('何名様ですか？', 'Nanmei-sama desu ka?', 'How many people?'),
    ('売り切れです。', 'Urikire desu.', 'It’s sold out.'),
    ('少々お待ちください。', 'Shōshō omachi kudasai.', 'Please wait a moment.'),
    ('こちらです。', 'Kochira desu.', 'Here / this way.'),
]:
    assert japanese in practice and pronunciation in practice
    cards.append(f'What does this mean: {japanese}::{meaning} — {pronunciation}')
stage(cards_name, '''# 🗣️ Japan 2027 — Japanese Flashcards

#flashcards/japan2027

[[Japan 2027 — Japanese Practice|Conversations and pronunciation]] · [[Japan 2027 — Today|Today]]

Open the command palette, search **Spaced Repetition**, and choose its flashcard review command. Select the Japan 2027 deck. Say the answer aloud before revealing it; use Again, Hard, Good, or Easy according to recall. Start with five minutes and then practice a conversation from the original note.

These 22 cards use the existing phrase note. Review schedules are created by the plugin as you answer. There is no timed notification or audio attached.

## Say it in Japanese

''' + '\n\n'.join(cards[:18]) + '\n\n## Understand the reply\n\n' + '\n\n'.join(cards[18:]) + '\n')

settings_name = '.obsidian/plugins/quickadd/data.json'
settings = json.loads((VAULT / settings_name).read_text())

def capture(name, target, fmt, heading=''):
    result = dict(
        id=str(uuid.uuid5(uuid.NAMESPACE_URL, 'japan2027/' + name)),
        name=name, type='Capture', command=True, onePageInput='always',
        appendLink=False, copyLinkToClipboard=False,
        captureTo=target, captureToActiveFile=False, captureToCanvasNodeId='',
        activeFileWritePosition='cursor',
        createFileIfItDoesntExist=dict(enabled=False, createWithTemplate=False, template=''),
        format=dict(enabled=True, format=fmt),
        insertAfter=dict(enabled=bool(heading), after=heading, insertAtEnd=True,
                         considerSubsections=True, createIfNotFound=False,
                         createIfNotFoundLocation='bottom', inline=False,
                         replaceExisting=False, blankLineAfterMatchMode='auto', promptHeading=False),
        insertBefore=dict(enabled=False, before='', createIfNotFound=False, createIfNotFoundLocation='top'),
        newLineCapture=dict(enabled=False, direction='below'),
        prepend=False, task=False, openFile=False,
        fileOpening=dict(location='tab', direction='vertical', mode='default', focus=True),
        templater=dict(afterCapture='none'),
    )
    return result

choices = [
    capture('Japan — Expense', expense_name,
            '\n### {{VDATE:Spending date,YYYY-MM-DD}} — {{VALUE:Item}}\n'
            '- Amount: {{VALUE:Amount numeric}}\n- Currency: {{VALUE:Currency JPY USD or CLP}}\n'
            '- Category: {{VALUE:Category}}\n- Payment method: {{VALUE:Payment method}}\n'
            '- Notes or receipt: {{VALUE:Notes or receipt}}\n'),
    capture('Japan — Place', place_name,
            '\n### {{VALUE:Exact place or branch}}\n'
            '- Saved: {{DATE:YYYY-MM-DD HH:mm}}\n- City / area: {{VALUE:City or area}}\n'
            '- Source / Maps URL: {{VALUE:Source or Maps URL}}\n'
            '- Why visit: {{VALUE:Why visit}}\n- Status: To verify\n'),
    capture('Japan — Memory', 'Japan 2027 — Memories.md',
            '\n### {{VDATE:Memory date,YYYY-MM-DD}} — {{VALUE:Place}}\n'
            '- The moment: {{VALUE:Moment to remember}}\n'
            '- Favorite photo / clip: {{VALUE:Photo or clip filename or link}}\n',
            '## My entries'),
]
existing_ids = {c['id'] for c in settings['choices']}
assert not existing_ids.intersection(c['id'] for c in choices), 'Already configured'
settings['choices'].extend(choices)
stage(settings_name, json.dumps(settings, ensure_ascii=False, indent=2) + '\n')

stage(help_name, '''# ✍️ Japan 2027 — Quick Capture

[[Japan 2027 — Start Here|Dashboard]] · [[Japan 2027 — Today|Today]]

## Save something quickly

1. Reload Obsidian once after this setup so QuickAdd loads the new choices.
2. Open the command palette with **Ctrl+P**, search **Japan**, and choose a capture. You can also run **QuickAdd: Run** and select it there.
3. Fill in the form, then submit. Cancel to leave without saving. Enter `—` for an unused notes or photo field.

| Capture | Saves to | What to enter |
| --- | --- | --- |
| Japan — Expense | [[Japan 2027 — Expenses]] | Spending date, item, numeric amount, original currency, category, payment method, notes/receipt |
| Japan — Place | [[Japan 2027 — Place Inbox]] | Exact place or branch, area, source/Maps URL, why you want to visit |
| Japan — Memory | [[Japan 2027 — Memories#My entries]] | Memory date, place, moment, photo/clip filename or link |

Dates accept today or a specific date; check the saved date when recording an older entry. Amounts and URLs are text fields: check them before submitting. Captures append entries and do not update budgets, bookings, map pins, or the memory summary table automatically.

## Japanese review

Open [[Japan 2027 — Japanese Flashcards|your 22-card Japanese deck]] and use the Spaced Repetition flashcard review command. Keep the five-minute conversation practice in [[Japan 2027 — Japanese Practice]].

## Setup reference

The choices use QuickAdd's [capture formats](https://quickadd.obsidian.guide/docs/Choices/CaptureChoice/) and [one-page forms](https://quickadd.obsidian.guide/docs/Advanced/onePageInputs/). The deck uses Spaced Repetition's [question-and-answer cards](https://stephenmwangi.com/obsidian-spaced-repetition/flashcards/q-and-a-cards/).

Configuration and note links were checked. Interactive form submission and review still need a check inside Obsidian. The existing plugin privacy settings and reminder settings were preserved.
''')

stage(recap_name, '''# 🌙 Japan 2027 — Session recap · 7 October 2026

[[Japan 2027 — Start Here|Dashboard]] · [[Japan 2027 — Session Recap 2026-10-06|Previous recap]]

Resumed from the 6 October recap and inspected the current vault. Since that recap, the guide gained daily pocket cards, photo/film priorities, shopping and gift lists, seasonal comparisons, island research, and Osaka, Fukuoka, Sapporo, Nara, Okinawa, and Nagoya chapters. These remain options rather than confirmed additions to the route.

## This continuation

- Configured three QuickAdd capture forms: expenses, places, and memories. Instructions: [[Japan 2027 — Quick Capture]].
- Added [[Japan 2027 — Expenses]] and [[Japan 2027 — Place Inbox]]; memories append under the existing journal's My entries heading.
- Added [[Japan 2027 — Japanese Flashcards|22 Japanese flashcards]] from the current Japanese Practice note.
- Checked note links, capture targets, configuration structure, and the deck's match to the installed card separator/tag settings. Live form submission and card review have not been tested inside Obsidian.
- Preserved the earlier recap, existing notes, unrelated plugin settings, and current itinerary assumptions. A backup of changed files is in the workspace's `resume-20261007/backup` folder.

## Pick up next time

1. Reload Obsidian and try a capture; review a few Japanese cards.
2. Confirm passport nationality, traveler count, and whether the US$5,000 ceiling is per person before narrowing flight/hotel plans.
3. Choose a seasonal route and excursion; the main working stay is still provisionally 25 March–8 April 2027, Tokyo → Kyoto → Tokyo.
4. Verify precise shop/café branches before extending the interactive maps. Add hotel pins after choosing hotels.
5. Download the required offline areas on your iPhone using [[Japan 2027 — Saved Maps]].

Tracker and Meta Bind remain available for later configuration. No reservations, payments, or notifications were created.
''')
add_link('Japan 2027 — Start Here.md',
         '**Latest recap:** [[Japan 2027 — Session Recap 2026-10-07|7 October continuation]] · **Capture and review:** [[Japan 2027 — Quick Capture|Expense, place, memory forms and Japanese flashcards]]')
add_link('Japan 2027 — Today.md',
         '**Quick capture:** [[Japan 2027 — Quick Capture|Save expenses, places, and memories]] · [[Japan 2027 — Japanese Flashcards|Japanese review]]')
add_link('Japan 2027 — Japanese Practice.md',
         '**Flashcards:** [[Japan 2027 — Japanese Flashcards|Review 22 phrases with Spaced Repetition]]')

def verify():
    all_notes = {p.relative_to(VAULT).as_posix() for p in VAULT.rglob('*.md')} | set(updates)
    for name, data in updates.items():
        if not name.endswith('.md'):
            continue
        for link in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', data.decode()):
            target = link.split('#', 1)[0]
            assert not target or target + '.md' in all_notes, (name, target)
    for choice in choices:
        target = choice['captureTo']
        assert target in all_notes
        if choice['insertAfter']['enabled']:
            assert choice['insertAfter']['after'] in (VAULT / target).read_text()
    assert sum('::' in line for line in updates[cards_name].decode().splitlines()) == 22
    sr = json.loads((VAULT / '.obsidian/plugins/obsidian-spaced-repetition/data.json').read_text())['settings']
    assert sr['singleLineCardSeparator'] == '::' and '#flashcards' in sr['flashcardTags']
    preserved = json.loads((VAULT / settings_name).read_text())
    expected = dict(settings)
    expected['choices'] = expected['choices'][:-3]
    assert expected == preserved

verify()
manifest = {name: dict(before=hashlib.sha256(originals[name]).hexdigest() if originals[name] is not None else None,
                       after=hashlib.sha256(data).hexdigest()) for name, data in updates.items()}
(WORK / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))

if argparse.ArgumentParser().parse_known_args()[1] == ['--apply']:
    for name, before in originals.items():
        p = VAULT / name
        assert (p.read_bytes() if p.exists() else None) == before, f'Changed during staging: {name}'
    for name, data in updates.items():
        target = VAULT / name
        if originals[name] is not None:
            backup = WORK / 'backup' / name
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup)
        target.write_bytes(data)
        assert target.read_bytes() == data
    print(f'Applied and read back {len(updates)} files; 3 captures and 22 cards.')
else:
    print(f'Staged and checked {len(updates)} files; 3 captures and 22 cards.')
