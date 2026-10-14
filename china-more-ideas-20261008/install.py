from pathlib import Path
from urllib.parse import urlparse,parse_qs
import json,hashlib,re
base=Path('/home/ivanaguilera/Work/china-more-ideas-20261008')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest=json.loads((base/'manifest.json').read_text())
manifest['China — Klook Experience Research 2026-10-08.md']=None
def validate():
    files={p.stem:p for p in vault.glob('*.md')}
    files.update({p.stem:p for p in (base/'staged').glob('*.md')})
    for p in (base/'staged').glob('*.md'):
        text=p.read_text()
        assert 'SOURCE_' not in text,p
        for link in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',text):
            stem,_,anchor=link.partition('#')
            assert stem in files,(p.name,link)
            if anchor:
                assert anchor in re.findall(r'^#+ (.+)$',files[stem].read_text(),re.M),(p.name,anchor)
        for table in re.findall(r'(?m)^\|.*(?:\n\|.*)+',text):
            assert len({line.count('|') for line in table.splitlines()})==1,p.name
        for url in re.findall(r'\]\((https?://[^)]+)\)',text):
            assert urlparse(url).netloc,url
    ideas=(base/'staged'/'China — More Ideas and Route Choices.md').read_text()
    urls=re.findall(r'\[Search in Amap\]\(([^)]+)\)',ideas)
    assert len(urls)==13
    for url in urls:
        q=parse_qs(urlparse(url).query)
        assert q['keyword'] and q['city'] and q['callnative']==['1'],url
    shortlist=(base/'staged'/'China — Places and Experiences Shortlist.md').read_text()
    assert shortlist.count('[Search in Amap](')==16
validate()
for name,expected in manifest.items():
    target=vault/name
    if expected is None: assert not target.exists(),name
    else: assert hashlib.sha256(target.read_bytes()).hexdigest()==expected,'Changed since backup: '+name
for name,expected in manifest.items():
    target=vault/name
    if expected is None: assert not target.exists(),name
    else: assert hashlib.sha256(target.read_bytes()).hexdigest()==expected,name
    target.write_bytes((base/'staged'/name).read_bytes())
for name in manifest:
    assert (vault/name).read_bytes()==(base/'staged'/name).read_bytes(),name
    print('Saved and read back:',name)
validate()
print('Verified wiki targets/anchors, tables, 13 new Amap searches, and 16 preserved original searches.')
