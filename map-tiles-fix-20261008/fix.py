from pathlib import Path
import json,hashlib,os

base=Path(__file__).resolve().parent
live=Path('/home/ivanaguilera/Documents/Obsidian Vault/.obsidian/plugins/obsidian-map-view/data.json')
raw=live.read_bytes()
old=json.loads(raw)
new=json.loads(raw)
assert new['mapSources'][0]['name']=='CartoDB'
new['mapSources'][0]={'name':'OpenStreetMap Standard','urlLight':'https://tile.openstreetmap.org/{z}/{x}/{y}.png','preset':False}
assert {k:v for k,v in old.items() if k!='mapSources'}=={k:v for k,v in new.items() if k!='mapSources'}
backup=base/'data.before.json'
backup.write_bytes(raw);backup.chmod(0o600)
staged=base/'data.updated.json'
staged.write_text(json.dumps(new,ensure_ascii=False,indent=2));staged.chmod(0o600)
(base/'expected-sha.txt').write_text(hashlib.sha256(raw).hexdigest())
print('Prepared tile source replacement; all other settings preserved. Private backup saved.')
