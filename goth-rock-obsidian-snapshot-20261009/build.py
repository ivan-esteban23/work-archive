import json, re, html, hashlib, pathlib, urllib.parse, urllib.request, concurrent.futures

ROOT = pathlib.Path(__file__).parent
DATA = json.loads((ROOT / 'source.json').read_text())
OUT = ROOT / 'Goth Rock — Notion Snapshot 2026-10-09'
OUT.mkdir(exist_ok=True)
ASSETS = OUT / 'Attachments'
ASSETS.mkdir(exist_ok=True)
PREFIX = OUT.name
MAIN = 'Goth Rock — Research and Listening'

def clean(s):
    return re.sub(r'[\\/:*?"<>|]', '—', s).strip()

def key(url):
    ids = re.findall(r'[a-f0-9]{32}|[a-f0-9]{8}(?:-[a-f0-9]{4}){3}-[a-f0-9]{12}', url)
    return ids[-1].replace('-', '') if ids else url

def content(p):
    return p['text'].split('<content>\n', 1)[1].rsplit('\n</content>', 1)[0]

mapping = {key(DATA['main']['id']): MAIN}
names = {}
for p in DATA['pages']:
    props = json.loads(p['text'].split('<properties>\n', 1)[1].split('\n</properties>', 1)[0])
    if 'Album' in props: name = 'Album — ' + props['Artist'] + ' — ' + props['Album']
    elif 'Milestone' in props: name = 'Timeline — ' + props['Milestone']
    elif 'Scene' in props: name = 'Scene — ' + props['Scene']
    else: name = 'Original research and preference archive'
    names[p['id']] = clean(name)
    mapping[key(p['id'])] = clean(name)
indexes = {'albums': 'Album Gallery', 'scenes': 'Scene Atlas', 'history': 'History Timeline', 'journal': 'Listening Journal'}
for (k, db), inline in zip(DATA['manifest']['databases'].items(), [None]*4):
    mapping[key(db['url'])] = indexes[k]
    mapping[key(db['ds'])] = indexes[k]
for db in DATA['manifest']['inline']:
    k = next(k for k,v in DATA['manifest']['databases'].items() if v['ds'] == db['ds'])
    mapping[key(db['url'])] = indexes[k]

def wiki(url, label=None):
    name = mapping.get(key(url))
    if name:
        return '[[' + PREFIX + '/' + name + '|' + (label or name).replace('|','—').replace('\\','') + ']]'
    return '[' + (label or 'Open in Notion') + '](' + url + ')'

# Stable references sharing the same attachment ID use one local file.
assets, jobs = {}, {}
for f in DATA['downloads']:
    ref = f['reference']; aid = urllib.parse.urlparse(ref).path.strip('/')
    original = urllib.parse.parse_qs(urllib.parse.urlparse(ref).query).get('name',['image.jpg'])[0]
    filename = hashlib.sha256(aid.encode()).hexdigest()[:10] + '-' + clean(original)
    assets[ref] = filename
    jobs[filename] = f['url']
for p in [DATA['main']] + DATA['pages']:
    for m in re.finditer(r'!\[([^\]]*)\]\((https?://[^)]+)\)', content(p)):
        url = m[2]
        # Match existing uploaded copies by their original filename where possible.
        filename = 'external-' + hashlib.sha256(url.encode()).hexdigest()[:12] + '.jpg'
        assets[url] = filename; jobs[filename] = url

def download(item):
    filename, url = item; dest = ASSETS / filename
    if dest.exists() and dest.stat().st_size > 0: return filename
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = r.read()
        if not r.headers.get('Content-Type','').startswith('image/'):
            raise ValueError('Non-image response for ' + filename)
    dest.write_bytes(payload)
    return filename

def convert(s):
    def table(m):
        rows=[]
        for row in re.findall(r'<tr[^>]*>(.*?)</tr>', m[0], re.S):
            cells = [re.sub(r'\s+', ' ', c).strip().replace('|', '\\|') for c in re.findall(r'<td[^>]*>(.*?)</td>',row,re.S)]
            if cells: rows.append('| ' + ' | '.join(cells) + ' |')
        if not rows: return ''
        n = len(re.findall(r'<td', re.search(r'<tr[^>]*>(.*?)</tr>',m[0],re.S)[1]))
        return '\n\n' + rows[0] + '\n| ' + ' | '.join(['---']*n) + ' |\n' + '\n'.join(rows[1:]) + '\n\n'
    s = re.sub(r'<table\b[^>]*>.*?</table>',table,s,flags=re.S)
    s = re.sub(r'<mention-date\b([^>]*)/>',lambda m: ' → '.join(re.findall(r'(?:start|end)="([^"]+)"',m[1])),s)
    s = re.sub(r'<mention-(?:page|database|data-source)\b[^>]*url="([^"]+)"[^>]*/>',lambda m:wiki(m[1]),s)
    s = re.sub(r'<mention-(?:page|database|data-source)\b[^>]*url="([^"]+)"[^>]*>(.*?)</mention-(?:page|database|data-source)>',lambda m:wiki(m[1],m[2] or None),s,flags=re.S)
    s = re.sub(r'<(?:page|database)\b[^>]*url="([^"]+)"[^>]*>(.*?)</(?:page|database)>',lambda m:'\n'+wiki(m[1],m[2] or None)+'\n',s,flags=re.S)
    s = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',lambda m:'![['+PREFIX+'/Attachments/'+assets[m[2]]+']]\n\n*'+m[1]+'*' if m[2] in assets else m[0],s)
    def details(m):
        title,body=m[1],m[2]
        body='\n'.join(l.lstrip('\t') for l in body.strip().splitlines())
        return '\n> [!note]- '+title+'\n'+'\n'.join('> '+l for l in body.splitlines())+'\n\n'
    s = re.sub(r'<details[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>',details,s,flags=re.S)
    s = re.sub(r'<callout[^>]*>(.*?)</callout>',lambda m:'\n> [!note]\n'+'\n'.join('> '+l.lstrip('\t') for l in m[1].strip().splitlines())+'\n\n',s,flags=re.S)
    s = re.sub(r'</?(?:columns|column)\b[^>]*>', '\n', s)
    s = re.sub(r'\s*\{(?:color|toggle)="[^"\n]+"[^}\n]*\}', '', s)
    s = re.sub(r'<span[^>]*>(.*?)</span>',r'\1',s,flags=re.S)
    s = s.replace('<empty-block/>','\n').replace('<table_of_contents/>','')
    s = '\n'.join(l.lstrip('\t') for l in s.splitlines())
    s = re.sub(r'\n{3,}', '\n\n', s)
    # Separate headings/paragraphs so CommonMark and Obsidian render predictably.
    s = re.sub(r'(?m)^(#{1,6} .+)\n(?!\n)',r'\1\n\n',s)
    return s.strip()+'\n'

def write(name, body):
    (OUT/(name+'.md')).write_text(body)

header = '> [!info] Notion snapshot · 9 October 2026\n> This is a local copy with downloaded images. Notion galleries are linked notes and tables here; this copy does not synchronize automatically.\n\n'
write(MAIN, '# '+MAIN+'\n\n'+header+convert(content(DATA['main'])))
for p in DATA['pages']:
    name=names[p['id']]
    props=json.loads(p['text'].split('<properties>\n',1)[1].split('\n</properties>',1)[0])
    metadata=[]
    for k,v in props.items():
        if k in {'Artwork','url','title'} or v is None: continue
        if isinstance(v,list): v=', '.join(map(str,v))
        metadata.append('- **'+k+':** '+str(v))
    write(name, '# '+name+'\n\n[Original Notion page]('+p['url']+')\n\n'+ '\n'.join(metadata)+'\n\n'+convert(content(p)))

for k, name in indexes.items():
    rows=DATA['rows'][k]
    text='# '+name+'\n\n'+wiki(DATA['main']['url'],MAIN)+'\n\n'
    if k=='albums':
        rows=sorted(rows,key=lambda r:r.get('Order',0))
        for shelf in ['Next listens','Stated favorite','Historical reference','Atmospheric detour']:
            text+='## '+shelf+'\n\n'
            text+='| Album dossier | Artist | Year | Entry track |\n| --- | --- | --- | --- |\n'
            for row in rows:
                if row['Shelf']==shelf:
                    text+='| '+wiki(row['url'],row['Album']).replace('|','\\|')+' | '+row['Artist']+' | '+str(row['Original year'])+' | '+row['Entry track']+' |\n'
            text+='\n'
    elif k=='history':
        text+='Year spans preserve the source precision; January 1 is not an asserted release day.\n\n| Year | Milestone | Scene | Precision |\n| --- | --- | --- | --- |\n'
        for row in sorted(rows,key=lambda r:r['Year']):
            text+='| '+str(row['Year'])+' | '+wiki(row['url'],row['Milestone']).replace('|','\\|')+' | '+row['Scene']+' | '+row['Date precision']+' |\n'
    elif k=='scenes':
        for row in sorted(rows,key=lambda r:r['Region']): text+='- '+wiki(row['url'],row['Scene'])+' — '+row['Region']+' · '+row['Evidence']+'\n'
    elif k=='journal':
        assert not rows, 'Journal now has entries; export those before continuing'
        text+='No listening sessions were recorded in the Notion database at export.\n\n## Listening entry template\n\nCopy this section for each session.\n\n- **Date:**\n- **Artist / album:**\n- **Exact edition / format:**\n- **Sample or full listen:**\n- **Memorable track / timestamp:**\n- **Atmosphere:**\n- **Rhythm and guitar/bass weight:**\n- **Your reaction:**\n- **Optional personal score:**\n- **Next listen:**\n- **Bandcamp / source link:**\n'
    write(name,text)

def verify():
    allnames={p.stem for p in OUT.glob('*.md')}
    missing=[]
    for p in OUT.glob('*.md'):
        s=p.read_text()
        assert not re.search(r'notion-file-block://|file-upload://|<database\b|<mention-',s),p.name
        for target in re.findall(r'!?\[\[([^\]|]+)',s):
            target = target.rstrip('\\')
            if '/Attachments/' in target:
                f=OUT/target.split(PREFIX+'/',1)[1]
                if not f.exists() or not f.stat().st_size: missing.append(str(f))
            elif target.split('/')[-1] not in allnames: missing.append(target)
    assert not missing, missing
    print(json.dumps({'notes':len(allnames),'images':len(list(ASSETS.iterdir())),'output':str(OUT),'broken_links':0}))

if __name__=='__main__':
    failures=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        fs={pool.submit(download,j):j[0] for j in jobs.items()}
        for f in concurrent.futures.as_completed(fs):
            try: f.result()
            except Exception as e: failures.append({'file':fs[f],'error':str(e)})
    if failures: print(json.dumps(failures)); raise SystemExit(1)
    verify()
