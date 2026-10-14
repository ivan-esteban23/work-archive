from pathlib import Path
import hashlib, json, os, re

root = Path(__file__).parent
vault = Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest = json.loads((root/'original-hashes.json').read_text())
files = sorted((root/'staged').glob('*.md'))
assert len(manifest) == 25 and len(files) == 27
hashof = lambda b: hashlib.sha256(b).hexdigest()

# Validate every original before writing anything. Never overwrite intervening edits.
for name, expected in manifest.items():
    assert hashof((vault/name).read_bytes()) == expected, f'Live note changed: {name}'
    assert hashof((root/'backup'/name).read_bytes()) == expected, f'Backup mismatch: {name}'
for path in files:
    assert path.name.startswith('Korea 2026 — ')
    if path.name not in manifest:
        assert not (vault/path.name).exists(), f'New note already exists: {path.name}'

names = {p.stem for p in files} | {p.stem for p in vault.glob('*.md')}
for path in files:
    text = path.read_text()
    assert text.startswith('---\ncssclasses:\n  - korea-trip\n')
    assert text.count('```') % 2 == 0
    for raw in re.findall(r'\[\[([^\]]+)\]\]', text):
        target = raw.replace('\\|', '|').split('|')[0].split('#')[0]
        assert target in names, (path.name, raw)
    for block in re.findall(r'```mapview\n(.*?)\n```', text, re.S):
        json.loads(block)

written = {}
for path in files:
    target = vault/path.name
    # Repeat immediately before this individual replacement.
    if path.name in manifest:
        assert hashof(target.read_bytes()) == manifest[path.name], f'Live note changed: {path.name}'
    else:
        assert not target.exists()
    data = path.read_bytes()
    temporary = vault/(path.name+'.review-tmp')
    with temporary.open('xb') as handle:
        handle.write(data)
    os.replace(temporary, target)
    assert target.read_bytes() == data, f'Readback mismatch: {path.name}'
    written[path.name] = hashof(data)

(root/'applied-hashes.json').write_text(json.dumps(written, ensure_ascii=False, indent=2))
print(f'Saved and read back {len(written)} notes: 25 revised, 2 new. Backups and original hashes verified.')
