from pathlib import Path
import json,urllib.request,urllib.parse,re,time
from concurrent.futures import ThreadPoolExecutor,as_completed
R=Path(__file__).parent;strings=json.loads((R/'locale-strings.json').read_text());chunks=[];current=[];size=0
for s in strings:
 if size+len(s)>2200 and current:chunks.append(current);current=[];size=0
 current.append(s);size+=len(s)+12
if current:chunks.append(current)
locales={'es':'es','zh-Hans':'zh-CN','zh-Hant':'zh-TW','ja':'ja','ko':'ko'}
result={locale:{} for locale in locales}
brands=sorted({x['name'] for x in json.loads((R/'sources.json').read_text())}|{'Pinterest','Obsidian','The Portrait Edit','The Visual Edit','Instrument Serif','Source Sans 3'},key=len,reverse=True)
brand_re=re.compile('|'.join(re.escape(x) for x in brands))
def protect(text):return brand_re.sub(lambda m:'ZXBRAND'+str(brands.index(m.group())).zfill(3)+'ZX',text)
def unprotect(text):return re.sub(r'ZXBRAND(\d{3})ZX',lambda m:brands[int(m.group(1))],text)
def translate(job):
 locale,chunk=job;q='\n'.join(f'⟦{i:03}⟧\n{protect(s)}' for i,s in enumerate(chunk));url='https://clients5.google.com/translate_a/t?'+urllib.parse.urlencode({'client':'dict-chrome-ex','sl':'en','tl':locales[locale],'q':q})
 for attempt in range(3):
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as response:data=json.load(response)
   text=data[0];parts=re.split(r'⟦\s*(\d{3})\s*⟧\s*',text);pairs={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)}
   assert set(pairs)==set(range(len(chunk))),str(parts)[:150]
   return locale,{s:unprotect(pairs[i]) for i,s in enumerate(chunk)}
  except Exception:
   if attempt==2:raise
   time.sleep(1+attempt)
with ThreadPoolExecutor(max_workers=4) as pool:
 futures=[pool.submit(translate,(locale,chunk)) for locale in locales for chunk in chunks]
 for count,f in enumerate(as_completed(futures),1):
  locale,entries=f.result();result[locale].update(entries)
  (R/'translations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
  if count%10==0:print(f'Translated {count}/{len(futures)} batches',flush=True)
assert all(len(v)==len(strings) for v in result.values());print('All five translation dictionaries complete.',flush=True)
