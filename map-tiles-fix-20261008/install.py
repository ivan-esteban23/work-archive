from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent
live=Path('/home/ivanaguilera/Documents/Obsidian Vault/.obsidian/plugins/obsidian-map-view/data.json')
assert hashlib.sha256(live.read_bytes()).hexdigest()==(base/'expected-sha.txt').read_text(),'Settings changed during preparation'
new=(base/'data.updated.json').read_bytes()
live.write_bytes(new)
assert live.read_bytes()==new
assert json.loads(new)['mapSources'][0]['urlLight']=='https://tile.openstreetmap.org/{z}/{x}/{y}.png'
print('Saved and read back OpenStreetMap Standard tile source. No live rendering test or app restart performed.')
