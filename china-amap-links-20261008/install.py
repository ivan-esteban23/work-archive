from pathlib import Path
import hashlib,json,re
base=Path('/home/ivanaguilera/Work/china-amap-links-20261008')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((base/'manifest.json').read_text())
for name,expected in manifest.items():
    assert hashlib.sha256((vault/name).read_bytes()).hexdigest()==expected,'Changed since backup: '+name
for name,expected in manifest.items():
    target=vault/name
    assert hashlib.sha256(target.read_bytes()).hexdigest()==expected,name
    target.write_bytes((base/'staged'/name).read_bytes())
for name in manifest:
    data=(vault/name).read_bytes()
    assert data==(base/'staged'/name).read_bytes(),name
    print('Saved and read back:',name)
shortlist=(vault/'China — Places and Experiences Shortlist.md').read_text()
assert shortlist.count('[Search in Amap](')==16
for table in re.findall(r'(?m)^\|.*(?:\n\|.*)+',shortlist):
    counts={line.count('|') for line in table.splitlines()}
    assert counts=={5},counts
print('Verified all 16 links and four table column counts.')
