import json,re,html,urllib.request,concurrent.futures
from pathlib import Path
root=Path(__file__).parent;rows=json.loads((root/'records.json').read_text());out=root/'Attachments';out.mkdir(exist_ok=True)
def fetch(item):
 i,r=item;url=r['source']
 # Only single-album pages; shared discographies/press pages do not identify one cover.
 if url in {'https://themissionukband.com/albums','https://media.rhino.com/press-release/joy-divisions-studio-albums-and-essential-compilations','https://www.cherryred.co.uk/skeletal-family-eternal-singles-albums-rarities-bbc-sessions-live-demos-19822015','https://www.thecure.com/news/2025/11/the-show-of-a-lost-world/'}:return i,None
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  s=urllib.request.urlopen(req,timeout=25).read().decode('utf-8',errors='replace')
  (root/f'source-{i}.html').write_text(s)
  tags=re.findall(r'<meta\b[^>]+>',s,re.I);images=[]
  for tag in tags:
   if re.search(r'(?:property|name)=[\"\']og:image[\"\']',tag):
    m=re.search(r'content=[\"\']([^\"\']+)',tag)
    if m:images.append(html.unescape(m[1]))
  if not images:return i,{'error':'No album-specific image selected yet'}
  image=images[0];image=urllib.parse.urljoin(url,image)
  req=urllib.request.Request(image,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=25) as f:
   b=f.read();ct=f.headers.get('Content-Type','');assert ct.startswith('image/'),ct
  fn=f'album-{i:02d}.jpg';(out/fn).write_bytes(b)
  return i,{'url':image,'file':fn,'source':url}
 except Exception as e:return i,{'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 results=dict(ex.map(fetch,enumerate(rows)))
(root/'covers.json').write_text(json.dumps(results,indent=2))
print(json.dumps({i:v for i,v in results.items() if v},indent=2))
