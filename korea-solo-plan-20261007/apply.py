from pathlib import Path
import hashlib,json

root=Path('/home/ivanaguilera/Work/korea-solo-plan-20261007')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
expected=json.loads((root/'original-hashes.json').read_text())
files=sorted((root/'staged').glob('*.md'))
def digest(data):return hashlib.sha256(data).hexdigest()
for f in files:
    target=vault/f.name
    if f.name in expected:
        if not target.exists() or digest(target.read_bytes())!=expected[f.name]:
            raise SystemExit('Live note changed; refusing to overwrite: '+f.name)
    elif target.exists():
        raise SystemExit('New note already exists; refusing to overwrite: '+f.name)
written={}
for f in files:
    target=vault/f.name
    if f.name in expected and digest(target.read_bytes())!=expected[f.name]:
        raise SystemExit('Live note changed immediately before write: '+f.name)
    data=f.read_bytes()
    if f.name in expected:target.write_bytes(data)
    else:
        with target.open('xb') as stream:stream.write(data)
    actual=target.read_bytes()
    if actual!=data:raise SystemExit('Readback mismatch: '+f.name)
    written[f.name]=digest(actual)
(root/'applied-hashes.json').write_text(json.dumps(written,indent=2,ensure_ascii=False))
print('Saved and read back',len(written),'Korea notes. Existing notes backed up; new notes created without overwriting.')
