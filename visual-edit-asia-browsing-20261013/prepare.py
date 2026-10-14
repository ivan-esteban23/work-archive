from pathlib import Path
import re,json,hashlib,shutil
root=Path(__file__).parent;source=Path('/home/ivanaguilera/Work/visual-edit-public/dist/index.html');s=source.read_text();backup=root/'backup';backup.mkdir(exist_ok=True)
if not (backup/'index.html').exists():shutil.copy2(source,backup/'index.html')
(root/'source.sha256').write_text(hashlib.sha256(source.read_bytes()).hexdigest())
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault/Attachments/Pinterest Alternatives/Pinterest Alternatives — Visual Research and Moodboarding.html')
if not (backup/'vault.html').exists():shutil.copy2(vault,backup/'vault.html')
(root/'vault.sha256').write_text(hashlib.sha256(vault.read_bytes()).hexdigest())
def change(a,b):
 global s
 assert a in s,a[:120]
 s=s.replace(a,b,1)
markets=['China','Japan','South Korea']
buttons=''.join('<button type="button" data-browse-region="'+market+'" aria-pressed="false"><span class="market-name">'+market+'</span><span class="market-count" data-market-count="'+market+'"></span><span class="market-arrow" aria-hidden="true">↗</span></button>' for market in markets)
entry='<nav class="asia-browse" id="asia-browse" aria-labelledby="asia-title"><p class="eyebrow" id="asia-title">Browse Asia</p><div class="asia-markets">'+buttons+'</div><p class="asia-note">Start with one market, then explore the full directory for global tools and archives.</p></nav>'
change('<div class="search-bar">',entry+'<div class="search-bar">')
change('<a href="#shortlist">Asia shortlist ↗</a>','<a href="#asia-browse">Browse Asia ↗</a>')
# Make the existing shortlist useful as another path into matching sources.
section=re.search(r'<section id="shortlist">.*?</section>',s,re.S).group(0);updated=section
for market in markets:
 pattern=r'(<div><span>'+market+r'</span>.*?)(</div>)'
 updated,n=re.subn(pattern,lambda m:m.group(1)+'<button class="browse-market" type="button" data-browse-region="'+market+'">Browse '+market+' ↗</button>'+m.group(2),updated,count=1,flags=re.S);assert n==1
change(section,updated)
# Add a menu link without removing the existing shortlist.
s=s.replace('<a href="#shortlist">Asia shortlist</a>','<a href="#asia-browse">Browse Asia</a><a href="#shortlist">Asia shortlist</a>')
change('.search-bar{', '''.asia-browse{margin:24px 0;scroll-margin-top:var(--search-offset,100px)}
.asia-browse>.eyebrow{margin-bottom:12px}
.asia-markets{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.asia-markets button{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px 4px;padding:14px 10px;border:1px solid var(--line);background:var(--surface);color:var(--ink);text-align:left;min-width:0;min-height:108px}
.asia-markets button[aria-pressed=true]{border-color:var(--accent);background:var(--soft)}
.market-name{font-size:18px;font-weight:550;line-height:1.25;min-height:2.5em;overflow-wrap:anywhere}
.market-count{grid-column:1/-1;font-size:11px;color:var(--muted);align-self:end}
.market-arrow{grid-column:2;grid-row:1;color:var(--link)}
.asia-note{font-size:12px;color:var(--muted);margin:12px 0 0;max-width:80ch}
.search-bar{''')
change('.shortlist span{', '.browse-market{display:inline-flex;align-items:center;min-height:44px;padding:8px 0;border:0;background:transparent;color:var(--link);font-size:13px}\n.shortlist span{')
change('body{padding-bottom:0}html{scroll-padding-bottom:20px}', 'body{padding-bottom:0}html{scroll-padding-bottom:20px}.asia-markets{gap:14px}.asia-markets button{padding:18px 20px;min-height:92px}.market-name{min-height:0}')
change('.mobile-nav,#sections-menu,.collection-view,.source-actions{', '.mobile-nav,#sections-menu,.collection-view,.source-actions,.asia-browse,.browse-market{')
# Translate only the new interface copy, retaining all existing dictionaries.
prefix,rest=s.split('const translations=',1);dictionary,n=json.JSONDecoder().raw_decode(rest)
keys=['Browse Asia','Browse Asia ↗','Start with one market, then explore the full directory for global tools and archives.','{n} sources','Browse {country}: {n} sources','Browse China ↗','Browse Japan ↗','Browse South Korea ↗']
values={
'es':['Explorar Asia','Explorar Asia ↗','Empieza por un mercado y explora después el directorio completo para encontrar herramientas globales y archivos.','{n} fuentes','Explorar {country}: {n} fuentes','Explorar China ↗','Explorar Japón ↗','Explorar Corea del Sur ↗'],
'zh-Hans':['探索亚洲','探索亚洲 ↗','先从一个市场开始，再浏览完整目录中的全球工具和档案。','{n} 个来源','浏览{country}：{n} 个来源','浏览中国 ↗','浏览日本 ↗','浏览韩国 ↗'],
'zh-Hant':['探索亞洲','探索亞洲 ↗','先從一個市場開始，再瀏覽完整目錄中的全球工具與檔案。','{n} 個來源','瀏覽{country}：{n} 個來源','瀏覽中國 ↗','瀏覽日本 ↗','瀏覽韓國 ↗'],
'ja':['アジアを探す','アジアを探す ↗','まず一つの市場を選び、続いて全体の一覧から世界のツールやアーカイブを探しましょう。','{n} 件のソース','{country}を探す：{n} 件のソース','中国を探す ↗','日本を探す ↗','韓国を探す ↗'],
'ko':['아시아 둘러보기','아시아 둘러보기 ↗','한 시장부터 시작한 뒤 전체 목록에서 글로벌 도구와 아카이브를 살펴보세요.','자료 {n}개','{country} 둘러보기: 자료 {n}개','중국 둘러보기 ↗','일본 둘러보기 ↗','한국 둘러보기 ↗']}
for locale,v in values.items():dictionary[locale].update(zip(keys,v))
s=prefix+'const translations='+json.dumps(dictionary,ensure_ascii=False)+rest[n:]
change('function refreshDynamicLabels(){renderFilterChips();', '''function refreshAsiaBrowse(){document.querySelectorAll('[data-browse-region]').forEach(button=>{const market=button.dataset.browseRegion;const n=cards.filter(c=>c.dataset.region===market).length;button.setAttribute('aria-label',t('Browse {country}: {n} sources').replace('{country}',t(market)).replace('{n}',n));button.setAttribute('aria-pressed',String(region.value===market));const count=button.querySelector('.market-count');if(count)count.textContent=t('{n} sources').replace('{n}',n);});}
function refreshDynamicLabels(){renderFilterChips();refreshAsiaBrowse();''')
change('function navigateDirectory(saved){', '''document.querySelectorAll('[data-browse-region]').forEach(button=>button.addEventListener('click',()=>{region.value=button.dataset.browseRegion;category='All';accessFilter.value='All';search.value='';favoritesOnly=false;update();const first=cards.find(c=>!c.hidden);const target=first||document.querySelector('#directory');target.scrollIntoView({block:'start',behavior:'instant'});if(first)first.querySelector('h3 a').focus({preventScroll:true});else search.focus({preventScroll:true});}));
function navigateDirectory(saved){''')
(root/'index.html').write_text(s)
assert re.findall(r'<article class="source".*?</article>',source.read_text(),re.S)==re.findall(r'<article class="source".*?</article>',s,re.S)
assert re.findall(r'@font-face\{[^}]+\}',source.read_text())==re.findall(r'@font-face\{[^}]+\}',s)
print('Asia entry points added; cards and embedded fonts unchanged.')
