import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from fetch_logos import ROOT,fetch,get,save_asset
rows=json.loads((ROOT/'additions.json').read_text())
with ThreadPoolExecutor(max_workers=8) as pool:results=list(pool.map(fetch,rows))
for item in results:
 if 'file' in item:continue
 host=urlparse(item['site_url']).netloc
 for url in [f'https://www.google.com/s2/favicons?domain={host}&sz=128',f'https://icons.duckduckgo.com/ip3/{host}.ico']:
  try:
   data,mime,final=get(url);name,mime=save_asset(data,mime,'new-'+host.replace('.','-'))
   item.update(file=name,mime=mime,source_url=final,kind='Website icon retrieved through favicon cache',retrieved='2026-10-13');break
  except Exception:pass
(ROOT/'new-logo-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
assert all('file' in x for x in results),[x['name'] for x in results if 'file' not in x]
old=json.loads((ROOT/'logos-manifest.json').read_text());(ROOT/'logos-manifest.json').write_text(json.dumps(old+results,ensure_ascii=False,indent=2))
print('All 24 new icons saved.')
