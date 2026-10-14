from pathlib import Path
import json,re,zipfile,hashlib
base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((base/'manifest.json').read_text())
def check():
    files={p.stem:p for p in vault.glob('*.md')}
    files.update({p.stem:p for p in (base/'staged').glob('*.md')})
    for p in (base/'staged').glob('*.md'):
        text=p.read_text()
        for link in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',text):
            stem,sep,anchor=link.partition('#')
            assert stem in files,(p.name,stem)
            if sep:assert anchor in re.findall(r'^#+ (.+)$',files[stem].read_text(),re.M),(p.name,anchor)
        assert text.count('```')%2==0,p.name
        for table in re.findall(r'(?m)^\|.*(?:\n\|.*)+',text):
            assert len({line.count('|') for line in table.splitlines()})==1,p.name
    prompts=(base/'staged'/'Death Metal — ChatGPT Project Prompts.md').read_text()
    assert [int(n) for n in re.findall(r'^## (\d+)\.',prompts,re.M)]==list(range(1,16))
    assert prompts.count('```text')==16
    instructions=(base/'project-instructions.txt').read_text()
    assert instructions in (base/'staged'/'Death Metal — ChatGPT Project Instructions.md').read_text()
    expected={u for p in (base/'staged').glob('*.md') if p.name!='Death Metal — ChatGPT Project Instructions.md' for u in re.findall(r'\]\((https?://[^)]+)\)',p.read_text())}
    exports=list((base/'sources').glob('*.txt'))
    assert len(exports)==5
    exported='\n'.join(p.read_text() for p in exports)
    assert '[[' not in exported
    assert expected==set(re.findall(r'\]\((https?://[^)]+)\)',exported))
    with zipfile.ZipFile(base/'Death-Metal-ChatGPT-Project-2026-10-08.zip') as z:
        assert z.testzip() is None
        for name in z.namelist():assert z.read(name)==(base/name).read_bytes(),name
check()
for name,expected in manifest.items():assert expected is None and not (vault/name).exists(),name
for name in manifest:
    assert not (vault/name).exists(),name
    (vault/name).write_bytes((base/'staged'/name).read_bytes())
for name in manifest:
    assert (vault/name).read_bytes()==(base/'staged'/name).read_bytes(),name
    print('Saved and read back:',name)
check()
(base/'saved-hashes.json').write_text(json.dumps({name:hashlib.sha256((vault/name).read_bytes()).hexdigest() for name in manifest},ensure_ascii=False,indent=2))
print('Verified wiki targets, tables, fences, 15 prompts, instruction copy, source URL preservation, and ZIP readback.')
