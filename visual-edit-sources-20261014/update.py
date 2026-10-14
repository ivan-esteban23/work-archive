from pathlib import Path
import re,json,html,base64,collections
root=Path('/home/ivanaguilera/Work');p=root/'visual-edit-public/dist/index.html';s=p.read_text()
rows=[
('Booooooom','https://www.booooooom.com/','Canada','Design & art direction','English','Design editorial','Partial','Find emerging photographers and artists for portrait and mood references.','Browsing is open; membership and submission features are separate. Follow artist credits.','https://www.booooooom.com/about/','https://www.booooooom.com/about/','BO'),
('Colossal','https://www.thisiscolossal.com/','United States','Design & art direction','English','Design editorial','Open','Explore art, craft and photography for color, texture and material ideas.','Public articles are readable. Image rights remain with the credited creators.','https://www.thisiscolossal.com/about/','https://www.thisiscolossal.com/about/','CO'),
('IGNANT','https://www.ignant.com/','Germany','Design & art direction','English','Design editorial','Open','Study editorial photography, interiors and art for composition and lighting.','Use individual project credits to find original creators; browsing does not grant image rights.','https://www.ignant.com/about/','https://www.ignant.com/imprint/','IG'),
('Frieze','https://www.frieze.com/','United Kingdom','Independent magazines','English / Korean','Design editorial','Partial','Read contemporary art criticism and artist interviews to develop visual concepts.','Membership and paid features were not tested. Country/base follows the London contact address.','https://www.frieze.com/about','https://www.frieze.com/legals','FR'),
('The Met Collection','https://www.metmuseum.org/art/collection','United States','Archives & textiles','English','Historical archive','Open','Research costume, textiles, portraits and prints using museum object records.','Check each object date, credit and Open Access designation before reusing an image.','https://www.metmuseum.org/art/collection','https://www.metmuseum.org/art/collection','ME'),
('Rijksmuseum Collection','https://www.rijksmuseum.nl/en/collection','Netherlands','Archives & textiles','English / Dutch','Historical archive','Open','Study historical portraits, costume details and color palettes in collection records.','Visitor stories are separate from museum records. Check each image and its usage terms.','https://www.rijksmuseum.nl/en/collection','https://www.rijksmuseum.nl/en/collection','RI')]
(root/'visual-edit-sources-20261014/sources.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
card_pattern=r'<article class="source".*?</article>';old=re.findall(card_pattern,s,re.S);template=old[0]
def E(x):return html.escape(x,quote=True)
new=[]
for n,(name,url,country,category,language,content,access,purpose,note,context,evidence,initials) in enumerate(rows,53):
 c=template
 c=re.sub(r'data-category="[^"]+"',f'data-category="{E(category)}"',c,1);c=re.sub(r'data-country="[^"]+"',f'data-country="{E(country)}"',c,1)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48"><rect width="48" height="48" rx="6" fill="#eee9e1"/><text x="24" y="30" text-anchor="middle" font-family="sans-serif" font-size="18" fill="#302c28">{initials}</text></svg>'
 img=f'<img class="brand-logo" src="data:image/svg+xml;base64,{base64.b64encode(svg.encode()).decode()}" alt="" width="48" height="48">'
 c=re.sub(r'<img class="brand-logo"[^>]+>',lambda _:img,c,1)
 c=re.sub(r'<div class="card-meta">.*?</div>',f'<div class="card-meta"><span>{n:02}</span><span class="country-label"><span class="metadata-label">Country/base</span><span>{E(country)}</span></span></div>',c,count=1)
 c=re.sub(r'<p class="category">.*?</p>',f'<p class="category">{E(category)}</p>',c,count=1)
 c=re.sub(r'<h3>.*?</h3>',f'<h3><a href="{E(url)}" target="_blank" rel="noopener">{E(name)} <span aria-hidden="true">↗</span></a></h3>',c,count=1)
 c=re.sub(r'<p class="source-purpose">.*?</p>',f'<p class="source-purpose">{E(purpose)}</p>',c,count=1)
 for cls,value in [('compare-language',language),('compare-content',content),('compare-access',access)]:c=re.sub(r'(<div class="'+cls+r'"><dt>.*?</dt><dd>).*?(</dd>)',lambda m:m[1]+E(value)+m[2],c,count=1)
 c=c.replace('2026-10-13','2026-10-14')
 c=re.sub(r'(<strong>Before you use it</strong><p>).*?(</p>)',lambda m:m[1]+E(note)+m[2],c,count=1)
 c=re.sub(r'(class="context-link" href=")[^"]+',lambda m:m[1]+E(context),c,count=1);c=re.sub(r'(class="country-evidence" href=")[^"]+',lambda m:m[1]+E(evidence),c,count=1)
 c=c.replace('https://www.are.na/',url).replace('Copy source link for Are.na',f'Copy source link for {E(name)}')
 new.append(c)
# Insert additions beside their existing category; retain existing stable source numbers.
for category in dict.fromkeys(r[3] for r in rows):
 current=re.findall(card_pattern,s,re.S);last=[c for c in current if f'data-category="{E(category)}"' in c][-1]
 additions=''.join(c for c in new if f'data-category="{E(category)}"' in c)
 s=s.replace(last,last+additions,1)
# Update visible counts and their existing translations without touching source 52.
s=s.replace('52 sources','58 sources').replace('52 SOURCES','58 SOURCES')
for x in ['52 fuentes','52 FUENTES','52 个来源','52 個來源','52 來源','52のソース','52 出典','52개 소스'] :s=s.replace(x,x.replace('52','58'))
s=s.replace('RESEARCH EDITION / 2026-10-13','RESEARCH EDITION / 2026-10-14')
for prefix in ['EDICIÓN DE INVESTIGACIÓN /','研究版 /','연구 에디션 /']:s=s.replace(prefix+' 2026-10-13',prefix+' 2026-10-14')
counts=collections.Counter(html.unescape(re.search(r'data-category="([^"]+)"',c)[1]) for c in re.findall(card_pattern,s,re.S))
def count_button(m):
 b=m[0];cat=html.unescape(re.search(r'data-filter="([^"]+)"',b)[1]);return re.sub(r'(class="filter-count"[^>]*>)\d+',lambda z:z[1]+str(58 if cat=='All' else counts[cat]),b)
s=re.sub(r'<button[^>]*data-filter[^>]*>.*?</button>',count_button,s)
# Keep translations for short metadata labels; longer new descriptions get translated below.
m=re.search(r'const translations=(.*?);let activeLocale=',s,re.S);translations=json.loads(m[1])
extra={
'English / Dutch':['Inglés / neerlandés','英语 / 荷兰语','英語 / 荷蘭語','英語 / オランダ語','영어 / 네덜란드어'],
'English / Korean':['Inglés / coreano','英语 / 韩语','英語 / 韓語','英語 / 韓国語','영어 / 한국어']}
for key,values in extra.items():
 for locale,value in zip(['es','zh-Hans','zh-Hant','ja','ko'],values):translations[locale][key]=value
s=s[:m.start(1)]+json.dumps(translations,ensure_ascii=False)+s[m.end(1):]
p.write_text(s)
sw=root/'visual-edit-public/dist/sw.js';w=sw.read_text();w=re.sub(r"const CACHE='[^']+'", "const CACHE='visual-edit-shell-sources-20261014-v1'",w);sw.write_text(w)
assert len(re.findall(card_pattern,s,re.S))==58
assert all(c in s for c in old), 'Existing cards changed'
print('Added six cards; all 52 existing cards preserved byte-for-byte.')
