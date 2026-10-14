from pathlib import Path
import hashlib
import json
import os

root = Path(__file__).parent
vault = Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest = json.loads((root / 'manifest.json').read_text())

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

# Check every original before saving any file.
for item in manifest:
    assert digest(vault / item['relative']) == item['before_sha256'], f"Live note changed: {item['relative']}"
    assert digest(root / 'staged' / item['relative']) == item['after_sha256'], f"Staged note changed: {item['relative']}"

for item in manifest:
    destination = vault / item['relative']
    assert digest(destination) == item['before_sha256'], f"Live note changed: {item['relative']}"
    temporary = destination.with_name(destination.name + '.music-prompts-update.tmp')
    try:
        with temporary.open('xb') as stream:
            stream.write((root / 'staged' / item['relative']).read_bytes())
        os.chmod(temporary, destination.stat().st_mode & 0o777)
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()
    assert digest(destination) == item['after_sha256'], f"Read-back mismatch: {item['relative']}"
    print(f"Saved and read back: {item['relative']}")

print('Completed: 50 new prompts, five libraries with 25 prompts each, shared index and five dashboards updated.')
