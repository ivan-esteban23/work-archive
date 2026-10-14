from pathlib import Path
import hashlib,json,re,zipfile

base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
groups={
 '01_Trip_Context_and_Status.txt':['China — Start Here','China — Budget','China — Bookings','China — Session Recap 2026-10-08'],
 '02_Current_Travel_Guide.txt':['China Travel Guide'],
 '03_Places_and_Route_Ideas.txt':['China — Places and Experiences Shortlist','China — More Ideas and Route Choices'],
 '04_Practical_Preparation.txt':['China — Preparation Before Choosing Dates'],
 '05_Evidence_and_Experience_Research.txt':['China — Research and Sources 2026-10-08','China — Klook Experience Research 2026-10-08']
}
mapping={stem:filename for filename,stems in groups.items() for stem in stems}
raw={stem:(vault/(stem+'.md')).read_bytes() for stem in mapping}
titles={
 '01_Trip_Context_and_Status.txt':'China Trip — Context, Decisions, Budget, and Reservations',
 '02_Current_Travel_Guide.txt':'China Trip — Current Travel Guide',
 '03_Places_and_Route_Ideas.txt':'China Trip — Places, Amap Links, and Route Choices',
 '04_Practical_Preparation.txt':'China Trip — Practical Preparation',
 '05_Evidence_and_Experience_Research.txt':'China Trip — Evidence and Paid Experience Research'
}
def convert(data):
    def ref(match):
        target,sep,label=match.group(1).partition('|')
        stem,has_anchor,anchor=target.partition('#')
        assert stem in mapping,stem
        display=label if sep else (anchor if has_anchor else stem)
        return f'{display} [source: {mapping[stem]}; note: {stem}'+(f'; section: {anchor}' if has_anchor else '')+']'
    text=re.sub(r'\[\[([^]]+)\]\]',ref,data)
    text=re.sub(r'`/home/ivanaguilera/Work/[^`]+`','(local preparation workspace; not part of these uploads)',text)
    return text

for filename,stems in groups.items():
    content=f'# {titles[filename]}\n\nSnapshot: 8 October 2026. Exported from the China Obsidian notes. Internal source references point to other uploaded files, not live links. External source and Amap URLs are retained. Research dates describe when claims were checked; this export does not refresh provider facts.\n\n'
    if filename.startswith('01'):
        content+='''## Quick orientation for a new project chat

This is a separate China trip. The user wants continuing research and planning, with useful location links. They use both iPhone and Android and plan to test Amap later; phone opening and live place matches remain untested. Interests drawn from other guides include photography/filming, food, cafés, tea, vintage clothing, vinyl, hobby browsing, and meaningful gifts; confirm priorities as needed.

Beijing 5 + Xi’an 3 + Shanghai 6 is a proposed 14-night / 15-local-day route. No year, travel dates, length, traveler/room count, budget, or final route has been selected. Chilean nationality and San Fernando/SCL origin are provisional carryover context; confirm the actual passport before applying entry/transit rules. There are no confirmed China bookings in this snapshot. Korea/Japan budgets are not China budgets.

Latest research added Hangzhou/Longjing tea, Suzhou gardens/canals, Shanghai cooking and neighborhood walks, and Chengdu/Chongqing/Zhangjiajie alternatives. There are 29 city-scoped Amap searches across the two location notes. None establishes a verified POI pin or tested handset handoff. Four Klook products are exploratory; pricing units and dated totals are unresolved.

Read the source notes below for details. Recommendations do not constitute the user’s choices. Later explicit user decisions or actual confirmations supersede this snapshot.

'''
    for stem in stems:
        content+=f'\n---\n\nOriginal note: {stem}.md\n\n'+convert(raw[stem].decode())+'\n'
    (base/'sources'/filename).write_text(content)

all_original='\n'.join(data.decode() for data in raw.values())
all_exported='\n'.join(p.read_text() for p in (base/'sources').glob('*.txt'))
url_pattern=r'\]\((https?://[^)]+)\)'
assert sorted(re.findall(url_pattern,all_original))==sorted(re.findall(url_pattern,all_exported)), 'An external URL changed or disappeared'
assert all_exported.count('[Search in Amap](')==29
assert '[[' not in all_exported
assert '/home/ivanaguilera/' not in all_exported
for filename in groups:
    assert (base/'sources'/filename).stat().st_size>0
for stem,data in raw.items():
    assert (vault/(stem+'.md')).read_bytes()==data,'Vault changed during export: '+stem
manifest={'snapshot_date':'2026-10-08','sources':{},'outputs':{}}
for filename,stems in groups.items():
    for stem in stems:
        manifest['sources'][stem+'.md']={'sha256':hashlib.sha256(raw[stem]).hexdigest(),'exported_to':filename}
for p in [*(base/'sources').glob('*.txt'),base/'project-instructions.txt',base/'first-message.txt',base/'README.md']:
    manifest['outputs'][str(p.relative_to(base))]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
(base/'export-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
archive=base/'China-ChatGPT-Project-2026-10-08.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for rel in [*manifest['outputs'],'export-manifest.json']:
        z.write(base/rel,rel)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for rel in [*manifest['outputs'],'export-manifest.json']:
        assert z.read(rel)==(base/rel).read_bytes(),rel
print('Created five source files covering all ten live China notes.')
print('Verified all external URL occurrences, 29 Amap searches, internal references, unchanged vault, output hashes, and ZIP readback.')
print('Project instructions:',len((base/'project-instructions.txt').read_text()),'characters')
print('Bundle:',archive)
