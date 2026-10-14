from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
import json,re

ROOT=Path(__file__).parent
OUT=ROOT/'logos';OUT.mkdir(exist_ok=True)
class Icons(HTMLParser):
    def __init__(self):super().__init__();self.items=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and 'icon' in a.get('rel','').lower() and a.get('href'):
            rel=a.get('rel','').lower()
            score=300 if 'apple-touch' in rel else 200 if 'svg' in a.get('type','') else 100
            sizes=re.findall(r'\d+',a.get('sizes',''))
            if sizes:score+=min(int(sizes[0]),512)
            self.items.append((score,a['href']))
def get(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; VisualResearchDirectory/1.0)'}),timeout=12) as res:
        return res.read(4_000_000),res.headers.get_content_type(),res.url
def save_asset(data,mime,slug):
    if data.startswith(b'\x89PNG\r\n\x1a\n'):ext='png';mime='image/png'
    elif data.startswith(b'\x00\x00\x01\x00'):ext='ico';mime='image/x-icon'
    elif data.startswith(b'\xff\xd8\xff'):ext='jpg';mime='image/jpeg'
    elif data[:4]==b'RIFF' and data[8:12]==b'WEBP':ext='webp';mime='image/webp'
    elif b'<svg' in data[:1000] and b'<script' not in data.lower():ext='svg';mime='image/svg+xml'
    elif data.startswith((b'GIF87a',b'GIF89a')):ext='gif';mime='image/gif'
    else:raise ValueError('Not a supported image')
    filename=f'{slug}.{ext}';(OUT/filename).write_bytes(data)
    return filename,mime
def fetch(row):
    name=row['name'];slug=re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')
    page=row['url'];host=urlparse(page).netloc
    # Shaarli's project mark, rather than GitHub's platform favicon.
    explicit={'Shaarli':['https://raw.githubusercontent.com/shaarli/Shaarli/master/doc/md/images/shaarli-logo.png']}
    candidates=explicit.get(name,[])
    errors=[]
    try:
        body,_,final=get(page);parser=Icons();parser.feed(body.decode('utf-8',errors='replace'))
        candidates += [urljoin(final,h) for _,h in sorted(parser.items,reverse=True)]
    except Exception as e:errors.append(type(e).__name__)
    if name!='Shaarli':candidates += [f'https://{host}/favicon.ico',f'https://{host}/favicon.png']
    for url in dict.fromkeys(candidates):
        try:
            data,mime,final=get(url);filename,mime=save_asset(data,mime,slug)
            print(name+': saved '+filename,flush=True)
            return dict(name=name,file=filename,mime=mime,source_url=final,site_url=page,kind='Official website icon / brand asset',retrieved='2026-10-13')
        except Exception as e:errors.append(type(e).__name__)
    print(name+': unresolved',flush=True)
    return dict(name=name,site_url=page,error=', '.join(errors[-3:]),candidates=candidates)
if __name__=='__main__':
    rows=json.loads((ROOT/'sources.json').read_text())
    with ThreadPoolExecutor(max_workers=8) as pool:results=list(pool.map(fetch,rows))
    (ROOT/'logos-manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
    print(f"Saved {sum('file' in r for r in results)}/{len(rows)} icons.")
