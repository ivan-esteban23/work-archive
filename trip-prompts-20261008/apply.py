from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((root/'manifest.json').read_text())
for name,expected in manifest.items():
    p=vault/name
    actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
    assert actual==expected,'Changed since staging: '+name
for name in manifest:
    data=(root/'staged'/name).read_bytes()
    (vault/name).write_bytes(data)
    assert (vault/name).read_bytes()==data
note=(vault/'Trip Planning Prompt Library.md').read_text()
for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',note):
    assert (vault/(target+'.md')).exists(),target
assert note.count('```')%2==0
for name in manifest:
    assert 'Trip Planning Prompt Library' in (vault/name).read_text()
print('Saved and read back prompt library and both dashboard links; wiki targets and prompt blocks verified.')
