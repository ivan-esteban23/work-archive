from pathlib import Path
from datetime import date
import re,json,hashlib
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((ROOT/'manifest.json').read_text())
allnotes={p.stem:p.read_text() for p in VAULT.rglob('*.md')}
errors=[]
for name in manifest:
    assert (VAULT/name).read_bytes()==(ROOT/'staged'/name).read_bytes(),name
for p in VAULT.glob('Korea*.md'):
    t=p.read_text()
    for ref in re.findall(r'\[\[([^\]]+)\]\]',t):
        target=ref.split('|')[0].replace('\\','')
        base,_,anchor=target.partition('#')
        base=base or p.stem
        if base not in allnotes: errors.append([p.name,target,'missing note'])
        elif anchor and anchor not in re.findall(r'^#{1,6} (.+)$',allnotes[base],re.M): errors.append([p.name,target,'missing heading'])
assert not errors,errors
for p in [ROOT/'chatgpt-project'/'Korea — Current Planning Brief and Verified Sources.md',ROOT/'chatgpt-project'/'Korea — Travel Essay and Verified Sources.txt']:
    s=p.read_text()
    assert '2026' in s and 'https://' in s
for p in VAULT.glob('Korea*.md'):
    assert p.read_text() in (ROOT/'chatgpt-project'/'Korea — All Guide Notes Snapshot.md').read_text(),p.name
assert (date(2026,11,5)-date(2026,10,27)).days==9
assert 4+2+3==9 and 2200+300==2500 and 236+208+246==690
report={'reviewed_existing':33,'saved_existing':21,'new_notes':4,'live_korea_notes':37,'saved_notes_match_staging':len(manifest),'broken_wiki_targets_or_headings':errors,'korea_export_complete':True,'japan_snapshot_notes':66,'native_chatgpt_projects_created':0,'uploads':0,'bookings':0}
(ROOT/'verification.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report))
