from pathlib import Path
import re,json,html
p=Path('visual-edit-public/dist/index.html');s=p.read_text()
# Collapse secondary section navigation while keeping the primary hero directory link.
s=re.sub(r'(<nav class="jump".*?</nav>)',r'<details class="section-navigation"><summary>Explore sections</summary>\1</details>',s,count=1,flags=re.S)
country=re.search(r'<nav class="asia-browse".*?</nav>',s,re.S)[0];s=s.replace(country,'',1)
start=s.index('<div class="search-bar">');end=s.index('<div class="collection-view"',start)
old=s[start:end]
fields=re.findall(r'<div class="filter-field">.*?</div>',old,re.S)
buttons=re.findall(r'<button[^>]*data-filter[^>]*>.*?</button>',old,re.S)
options=''.join('<option value="'+m+'">'+('All sources' if m=='All' else m)+'</option>' for b in buttons for m in [re.search(r'data-filter="([^"]+)"',b)[1]])
category='<div class="category-field"><label class="region-label" for="category-filter">Category</label><select id="category-filter" aria-label="Filter category">'+options+'</select><div class="filters" role="group" aria-label="Filter category">'+''.join(buttons)+'</div></div>'
collection=re.search(r'<div class="collection-controls">.*?</div>',old,re.S)[0]
share=re.search(r'<button id="share-view".*?</button>',old,re.S)[0]
collection=collection.replace('<p class="collection-note">',share+'<p class="collection-note">',1)
new='''<div class="search-bar"><label class="search-label" for="search">Search sources</label><div class="controls"><input id="search" type="search" aria-label="Search sources" placeholder="Search sources…"><button id="filter-toggle" type="button" aria-controls="filter-panel" aria-expanded="false">Filters</button></div><div class="search-status"><p id="count" class="count" role="status" aria-live="polite" aria-atomic="true">58 sources</p><button id="reset" type="button">Reset filters</button></div></div><div class="directory-tools"><div id="filter-chips" aria-label="Active filters" hidden></div><details class="filter-panel" id="filter-panel" open><summary>Filters <span id="active-filters">All sources</span><span class="panel-symbol" aria-hidden="true">+</span></summary><div class="filter-panel-body">'''+category+''.join(fields)+'</div></details>'+collection+'</div><details class="country-shortcuts"><summary>Browse countries</summary>'+country+'</details>'
s=s[:start]+new+s[end:]
# Search and metadata controls retain stable IDs / share-link values.
s=s.replace("function update(){let n=0;","function update(){document.querySelector('#category-filter').value=category;document.querySelector('#reset').disabled=activeFilterCount()===0;[countryFilter,region,accessFilter].forEach(el=>el.classList.toggle('is-active',el.value!=='All'));document.querySelector('#category-filter').classList.toggle('is-active',category!=='All');let n=0;",1)
s=s.replace("search.addEventListener('input',update);","search.addEventListener('input',update);document.querySelector('#category-filter').addEventListener('change',e=>{category=e.target.value;update();});",1)
s=s.replace("region.focus({preventScroll:true});}});","document.querySelector('#category-filter').focus({preventScroll:true});}});",1)
a="if(region.value!=='All')filters.push(['region',t('Coverage')+': '+t(region.value)]);if(countryFilter.value!=='All')filters.push(['country',t('Country/base')+': '+t(countryFilter.value)]);"
b="if(countryFilter.value!=='All')filters.push(['country',t('Country/base')+': '+t(countryFilter.value)]);if(region.value!=='All')filters.push(['region',t('Coverage')+': '+t(region.value)]);"
assert a in s;s=s.replace(a,b,1)
# Focus visibility and hash access to collapsed country shortcuts.
marker="const searchBar=document.querySelector('.search-bar');"
extra="""document.addEventListener('focusin',event=>{const target=event.target;if(!(target instanceof HTMLElement)||target.closest('dialog,.search-bar'))return;requestAnimationFrame(()=>{const rect=target.getBoundingClientRect(),bar=document.querySelector('.search-bar'),br=bar.getBoundingClientRect(),sticky=getComputedStyle(bar).position==='sticky'&&br.top<=1;const top=sticky?br.bottom+8:8;const nav=document.querySelector('.mobile-nav'),nr=nav.getBoundingClientRect();const bottom=getComputedStyle(nav).display!=='none'?nr.top-8:innerHeight-8;if(rect.top<top)window.scrollBy({top:rect.top-top,behavior:'instant'});else if(rect.bottom>bottom)window.scrollBy({top:rect.bottom-bottom,behavior:'instant'});});});
document.addEventListener('click',event=>{const link=event.target.closest?.('a[href="#asia-browse"]');if(link){document.querySelector('.country-shortcuts').open=true;}},true);
function revealCountryShortcuts(){if(location.hash==='#asia-browse'){document.querySelector('.country-shortcuts').open=true;requestAnimationFrame(()=>document.querySelector('#asia-browse').scrollIntoView({block:'start',behavior:'instant'}));}}window.addEventListener('hashchange',revealCountryShortcuts);revealCountryShortcuts();
"""
s=s.replace(marker,extra+marker,1)
# Add translations for the new visible Category label.
m=re.search(r'const translations=(.*?);let activeLocale=',s,re.S);t=json.loads(m[1])
for locale,value in zip(['es','zh-Hans','zh-Hant','ja','ko'],['Categoría','类别','類別','カテゴリー','카테고리']):t[locale]['Category']=value
s=s[:m.start(1)]+json.dumps(t,ensure_ascii=False)+s[m.end(1):]
# Update existing styles and add a small, scoped navigation block.
screen,printcss=s.split('@page',1)
screen=screen.replace('.directory-tools{padding:var(--space-3) 0;background:transparent;border:0;border-block:1px solid var(--line)}','.directory-tools{padding:var(--space-3) 0;background:transparent;border:0}')
screen=screen.replace('.filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px;flex-basis:100%}', '.filters{display:none;flex-wrap:wrap;gap:8px;margin-top:var(--space-1)}')
screen=screen.replace('.filter-field{flex:1 1 160px;max-width:220px}', '.filter-field{flex:1 1 160px;max-width:none}')
screen=screen.replace('.filter-panel>summary{display:none}.filter-panel-body{padding-top:0}', '.filter-panel>summary{display:none}.filter-panel-body{padding-top:0}.filters{display:flex}#category-filter,#filter-toggle{display:none}')
screen=screen.replace(".jump a[href='#directory']{font-weight:600;color:var(--ink)}", ".jump a[href='#directory']{font-weight:600;color:var(--ink)}")
newcss='''
.section-navigation{border-top:1px solid var(--line);padding:var(--space-1) 0}
.section-navigation>summary,.country-shortcuts>summary{display:flex;align-items:center;justify-content:space-between;min-height:var(--control-height);font-size:var(--text-small);cursor:pointer;list-style:none}
.section-navigation>summary::after,.country-shortcuts>summary::after{content:'+';color:var(--link);font-size:1.25rem}
.section-navigation[open]>summary::after,.country-shortcuts[open]>summary::after{content:'−'}
.section-navigation .jump{border:0;padding:var(--space-1) 0}
.search-label{display:block;font-size:var(--text-small);font-weight:550;margin-bottom:var(--space-1)}
.search-status{display:flex;align-items:center;justify-content:space-between;gap:var(--space-2);margin-top:var(--space-1)}
.search-status #reset{flex:none;background:transparent;border:0;padding:var(--space-1);color:var(--link);text-decoration:underline}
.search-status #reset:disabled{color:var(--muted);opacity:.55;cursor:default;text-decoration:none}
.search-status .count{font-size:var(--text-small);color:var(--ink)}
.category-field{flex-basis:100%;min-width:0;display:grid;gap:var(--space-1)}
#category-filter{font:inherit;width:100%;min-width:0;min-height:var(--control-height);padding:12px;border:1px solid var(--control-line);background:var(--surface);color:var(--ink);border-radius:var(--control-radius)}
.filter-field select.is-active,#category-filter.is-active{border-color:var(--accent);box-shadow:inset 3px 0 var(--accent);background:var(--soft)}
#filter-chips{padding-top:0;padding-bottom:var(--space-2)}
.country-shortcuts{border-block:1px solid var(--line);margin:0 0 var(--space-3)}
.country-shortcuts .asia-browse{margin:var(--space-2) 0 var(--space-3)}
.country-shortcuts .asia-browse>.eyebrow{display:none}
.source,.directory-tools :where(button,select,summary),.source :where(a,button,summary){scroll-margin-top:var(--search-offset,160px);scroll-margin-bottom:6rem}
@media(max-width:639px){.filter-panel>summary{display:none}.filter-panel-body{padding-top:0;gap:var(--space-2)}.directory-tools{padding-top:var(--space-2)}.collection-controls{gap:var(--space-1)}.collection-note{max-width:54ch}.search-bar{padding:var(--space-1) 0}.search-label{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}}
@media(max-height:480px){.search-bar{position:static}html{scroll-padding-top:1rem}.source,.filter-panel,.directory-tools :where(button,select,summary),.source :where(a,button,summary){scroll-margin-top:1rem}}
'''
i=screen.index('@page') if '@page' in screen else len(screen);screen+=newcss
printcss=printcss.replace('.skip-link,.jump,','.skip-link,.section-navigation,.country-shortcuts,.jump,',1)
p.write_text(screen+'@page'+printcss)
sw=Path('visual-edit-public/dist/sw.js');sw.write_text(re.sub(r"const CACHE='[^']+'","const CACHE='visual-edit-shell-navigation-20261014-v1'",sw.read_text()))
print('Navigation, search-first controls, mobile category selection, reset/results, and focus visibility updated.')
