from pathlib import Path
import hashlib,json,re
base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
actions=json.loads((base/'manifest.json').read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files={p.stem:p for p in vault.rglob('*.md') if '.obsidian' not in p.parts}
for a in actions:
    target=Path(a['target'])
    if target!=Path('/home/ivanaguilera/Work/AGENTS.md'):files[target.stem]=base/'staged'/a['staged']
for a in actions:
    staged=base/'staged'/a['staged']
    text=staged.read_text()
    for link in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',text):
        stem,sep,anchor=link.partition('#')
        assert stem in files,(staged.name,stem)
        if sep:assert anchor in re.findall(r'^#+ (.+)$',files[stem].read_text(),re.M),(stem,anchor)
    assert text.count('```')%2==0,staged.name
    if 'Music Prompt Library.md' in staged.name:
        assert [int(x) for x in re.findall(r'^## (\d+)\.',text,re.M)]==list(range(1,12))
for a in actions:
    source,target=Path(a['source']),Path(a['target'])
    if a['expected'] is None:assert not source.exists(),source
    else:assert digest(source)==a['expected'],'Changed since backup: '+str(source)
    if a['move']:assert not target.exists(),target
for a in actions:
    source,target=Path(a['source']),Path(a['target'])
    if a['expected'] is None:assert not source.exists(),source
    else:assert digest(source)==a['expected'],source
    if a['move']:assert not target.exists(),target
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes((base/'staged'/a['staged']).read_bytes())
for a in actions:
    target=Path(a['target'])
    assert target.read_bytes()==(base/'staged'/a['staged']).read_bytes(),target
for a in actions:
    if a['move']:
        source=Path(a['source'])
        assert digest(source)==a['expected'],source
        assert Path(a['target']).read_bytes()==(base/'staged'/a['staged']).read_bytes()
        source.unlink()
for a in actions:
    target=Path(a['target'])
    assert target.read_bytes()==(base/'staged'/a['staged']).read_bytes(),target
    if a['move']:assert not Path(a['source']).exists()
    print('Saved and read back:',target.name)
for a in actions:
    if a['move']:
        matches=[p for p in vault.rglob(Path(a['target']).name) if '.obsidian' not in p.parts]
        assert matches==[Path(a['target'])],matches
print('Verified links/anchors, fences, eleven shared prompts, unique moved-note names, preserved backups, and folder readback.')
