from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
import subprocess
import sys

vault = Path('/home/ivanaguilera/Documents/Obsidian Vault')
out = Path(__file__).parent
stamp = datetime.now(ZoneInfo('America/Santiago')).isoformat(timespec='seconds')
notes = sorted(vault.glob('Japan*.md'), key=lambda p: p.name.casefold())
priority = ['Japan 2027 — Start Here.md', 'Japan 2027 — Session Recap 2026-10-07.md',
            'Japan Travel Guide 2027.md', 'Japan 2027 — Klook Tours and Experiences.md',
            'Japan 2027 — Klook More Cities and Islands.md']
notes.sort(key=lambda p: (priority.index(p.name) if p.name in priority else len(priority), p.name.casefold()))
maps = sorted(p for p in (vault / 'Attachments/Japan 2027 Maps').glob('*') if p.suffix in {'.csv','.kml'})
sources = notes + maps
assert len(notes) == 64
assert len({p.name for p in sources}) == len(sources)

intro = f'''JAPAN 2027 — COMPLETE TRAVEL GUIDE PROJECT SOURCE

Exported: {stamp}
Source: live local Obsidian Japan guide
Included: {len(notes)} Japan Markdown notes and {len(maps)} text map exports.

This is a snapshot for a ChatGPT project, not a live connection to Obsidian.
Later vault edits require a refreshed export. The current dashboard and latest
session recap appear first. The full guide follows, then Klook shortlists and
all remaining Japan notes. Historical recaps are included as history; newer
notes and the user's latest instructions take precedence.

All source note content and external URLs are preserved. Obsidian [[wiki links]]
refer to other named source notes in this file; they are not public web links.
No Korea notes, plugin settings, account credentials, or backup copies are included.
Map exports contain search queries and starter coordinates; do not assume every
query is a verified venue or every coordinate is an entrance.

Existing dates, budgets, destinations, shopping ideas, and tour shortlists retain
their original provisional status. An activity appearing here is not a booking,
and displayed prices are not confirmed 2027 quotes. Follow the user’s current
choices and verify time-sensitive information before making recommendations.

SOURCE INDEX
'''
intro += '\n'.join(f'{i}. {p.relative_to(vault).as_posix()}' for i,p in enumerate(sources,1)) + '\n'
chunks = [intro]
manifest = []
for i,p in enumerate(sources,1):
    original = p.read_bytes()
    content = original.decode('utf-8')
    marker = f'BEGIN SOURCE {i}: {p.relative_to(vault).as_posix()}'
    chunks.append('\n\n' + '='*78 + '\n' + marker + '\n' + '='*78 + '\n\n' + content + '\n\n' + f'END SOURCE {i}\n')
    manifest.append({'source':p.relative_to(vault).as_posix(), 'bytes':len(original), 'sha256':hashlib.sha256(original).hexdigest()})
bundle = out / 'Japan 2027 — Complete Guide for ChatGPT.txt'
bundle.write_text(''.join(chunks))
result = bundle.read_text()
for i,p in enumerate(sources,1):
    assert result.count(f'BEGIN SOURCE {i}: {p.relative_to(vault).as_posix()}') == 1
    assert p.read_text() in result
assert len(result.encode()) < 2_000_000
(out / 'manifest.json').write_text(json.dumps({'exported_at':stamp,'source_count':len(sources),'files':manifest},ensure_ascii=False,indent=2))

instructions = '''Help me plan my Japan trip using the attached complete guide. Read the Start Here note and latest dated session recap first. Preserve my interests in photography/filming, matcha, cafés, food, vintage clothing, vinyl records, hobby browsing, and gifts.

Treat dates, budget allocations, optional destinations, and Klook lists as research assumptions until I confirm them. Confirm traveler count, rooms, and budget scope before comparing booking totals. Distinguish Santiago departure dates from arrival dates in Japan. Optional cities replace itinerary nights or excursions; do not add all of them to the same 14-night trip.

Use current official/provider information and available plugins for time-sensitive research. Preserve source links, currencies, package details, research dates, and uncertainties. Exclude geographically mismatched search results. Do not invent availability, bookings, cancellation terms, or price inclusions. Keep proposed options separate from confirmed reservations.

The upload is an Obsidian snapshot. Ask for an updated export when newer vault information is needed. Do not claim you changed the local vault unless an available tool actually saved and verified that change. Do not book, pay, cancel, or contact businesses without my explicit request. Give concise, practical comparisons and state what remains unresolved.

Never paste passport numbers, booking confirmation codes, or payment details into the chat — summarize bookings as facts instead (dates, totals, cancellation deadlines).
'''
(out / 'Project instructions.txt').write_text(instructions)
(out / 'README.md').write_text('''# Add the Japan guide to ChatGPT Projects

1. In the menu shown in your screenshot, select **New project** and name it **Japan 2027**.
2. Open the project's **Sources** section and upload these seven files from this folder (not the big Complete Guide file):
   - `Japan 2027 — Dashboard and Decisions.txt`
   - `Japan 2027 — Itinerary and Pocket Cards.txt`
   - `Japan 2027 — City Chapters and Regions.txt`
   - `Japan 2027 — Shopping Food and Experiences.txt`
   - `Japan 2027 — Planning Essentials and Seasons.txt`
   - `Japan 2027 — Maps and Routes.txt`
   - `Japan 2027 — Confirmed Decisions.txt` (update this one by hand after each chat where something gets decided)
3. Add the contents of `Project instructions.txt` to the project's instructions if that option is offered.
4. Start a chat inside the project: “Read my Japan guide and latest recap, then help me compare flights and hotel bases.”

The six guide files hold 64 Japan notes and two map exports, including both Klook shortlists. Everything is a snapshot, so rerun `export.py` when the Obsidian guide changes and replace the old project sources. This folder prepares the upload; it does not create a cloud project or upload anything automatically. The `Japan 2027 — Complete Guide for ChatGPT.txt` file is kept only as the intermediate step the split is built from — do not upload it alongside the six, or everything counts twice.

Refresh triggers: any vault edit, any booking, the January 2027 rail timetable, and the February 2027 blossom forecasts.

Official reference: [Projects and chats](https://learn.chatgpt.com/docs/projects?surface=app).
''')
print(f'Created and verified {bundle}: {len(notes)} notes, {len(maps)} map exports, {bundle.stat().st_size:,} bytes.')
print('Project instructions and import steps saved alongside it. No ChatGPT project has been created or modified.')

# One-command refresh: split the bundle into the six topical project files.
# split-guide.py reads the Complete Guide file written above and overwrites the six.
splitter = out / 'split-guide.py'
r = subprocess.run([sys.executable, str(splitter)], capture_output=True, text=True)
print(r.stdout, end='')
if r.returncode != 0:
    print(r.stderr, file=sys.stderr)
    raise SystemExit(f'split-guide.py failed with exit code {r.returncode}')
print('Refresh complete: bundle, six project files, manifest, instructions and README are all current.')
