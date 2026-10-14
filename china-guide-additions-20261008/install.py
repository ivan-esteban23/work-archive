from pathlib import Path
import json,hashlib,re
base=Path('/home/ivanaguilera/Work/china-guide-additions-20261008')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((base/'manifest.json').read_text())
for name,expected in manifest.items():
    p=vault/name
    current=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
    assert current==expected,'Live note changed; stopped: '+name
for name,expected in manifest.items():
    data=(base/'staged'/name).read_bytes()
    p=vault/name
    if expected is None:
        with p.open('xb') as f: f.write(data)
    else:
        assert hashlib.sha256(p.read_bytes()).hexdigest()==expected,name
        p.write_bytes(data)
for name in manifest:
    p=vault/name
    assert p.read_bytes()==(base/'staged'/name).read_bytes()
    for link in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',p.read_text()):
        assert (vault/(link.split('#')[0]+'.md')).exists(),link
    print('Read back and verified:',name)
