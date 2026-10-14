from pathlib import Path
import hashlib,json,re
base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((base/'manifest.json').read_text())
files={p.stem:p for p in vault.glob('*.md')}
files.update({p.stem:p for p in (base/'staged').glob('*.md')})
for name in manifest:
    text=(base/'staged'/name).read_text()
    for target in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',text):
        stem,sep,anchor=target.partition('#')
        assert stem in files,(name,stem)
        if sep:assert anchor in re.findall(r'^#+ (.+)$',files[stem].read_text(),re.M),(name,anchor)
prompt=(base/'staged'/'China — ChatGPT Project Prompts.md').read_text()
numbers=[int(n) for n in re.findall(r'^## (\d+)\.',prompt,re.M)]
assert numbers==list(range(1,18)),numbers
assert prompt.count('```text')==18
assert prompt.count('```')==36
for name,expected in manifest.items():
    target=vault/name
    if expected is None:assert not target.exists(),name
    else:assert hashlib.sha256(target.read_bytes()).hexdigest()==expected,'Changed since backup: '+name
for name,expected in manifest.items():
    target=vault/name
    if expected is None:assert not target.exists(),name
    else:assert hashlib.sha256(target.read_bytes()).hexdigest()==expected,name
    target.write_bytes((base/'staged'/name).read_bytes())
for name in manifest:
    assert (vault/name).read_bytes()==(base/'staged'/name).read_bytes(),name
    print('Saved and read back:',name)
print('Verified 17 numbered prompts, research add-on, code fences, wiki targets, and section anchors.')
