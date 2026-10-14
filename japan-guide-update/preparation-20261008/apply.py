from pathlib import Path
import hashlib
import json
import os
import re

root = Path('/home/ivanaguilera/Work/japan-guide-update/preparation-20261008')
vault = Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest = json.loads((root / 'manifest.json').read_text())

# Read every destination immediately before writing and refuse stale prepared edits.
for name, expected in manifest.items():
    p = vault / name
    if expected is None:
        assert not p.exists(), 'New note appeared: ' + name
    else:
        assert hashlib.sha256(p.read_bytes()).hexdigest() == expected, 'Changed while working: ' + name

for name in manifest:
    content = (root / 'staged' / name).read_bytes()
    target = vault / name
    temp = vault / ('.' + name + '.preparation-tmp')
    temp.write_bytes(content)
    os.replace(temp, target)
    assert target.read_bytes() == content

for name in manifest:
    text = (vault / name).read_text()
    # Validate all links in new notes and the new links added to existing notes.
    for raw in re.findall(r'\[\[([^\]]+)\]\]', text):
        dest = raw.split('|')[0].split('#')[0]
        if not dest:
            continue
        if name.startswith('Japan 2027 — Preparation') or name.endswith('2026-10-08.md') or dest in ['Japan 2027 — Preparation Before Choosing Dates', 'Japan 2027 — Session Recap 2026-10-08']:
            assert (vault / (dest + '.md')).exists(), (name, dest)
print('Saved and read back 7 notes; verified new wiki-link targets.')
