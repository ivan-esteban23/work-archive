from pathlib import Path
import re,json,shutil,hashlib
root=Path(__file__).parent;source=Path('/home/ivanaguilera/Work/visual-edit-public/dist/index.html');s=source.read_text();backup=root/'backup';backup.mkdir(exist_ok=True)
if not (backup/'index.html').exists():shutil.copy2(source,backup/'index.html')
(root/'source.sha256').write_text(hashlib.sha256(source.read_bytes()).hexdigest())
def change(a,b):
 global s
 assert a in s,a[:120]
 s=s.replace(a,b,1)
controls=re.search(r'<div class="controls">.*?</div>',s,re.S).group(0)
reset='<button id="reset" type="button">Reset filters</button>'
newcontrols=controls.replace(reset,'<button id="filter-toggle" type="button" aria-controls="filter-panel" aria-expanded="false">Filters</button>').replace('Search sources, silhouettes, tools…','Search sources…')
change('<div class="directory-tools">'+controls,'<div class="search-bar">'+newcontrols+'<div id="filter-chips" aria-label="Active filters" hidden></div></div><div class="directory-tools">')
change('<details class="filter-panel" open>','<details class="filter-panel" id="filter-panel" open>')
change('<div class="filters" aria-label="Filter category">','<label class="region-label" for="access-filter">Access</label><select id="access-filter" aria-label="Filter access"><option value="All">All</option>'+''.join('<option value="'+x+'">'+x+'</option>' for x in ['Open','Partial','Paid','Not verified'])+'</select>'+reset+'<div class="filters" aria-label="Filter category">')
change('scroll-padding-top:24px','scroll-padding-top:var(--search-offset,100px)')
change('scroll-margin-top:24px','scroll-margin-top:var(--search-offset,100px)')
change('.controls{display:flex;gap:10px;margin-bottom:14px}', '''.search-bar{position:sticky;top:0;z-index:20;background:var(--page);padding:10px 0;border-bottom:1px solid var(--line)}
.controls{display:flex;gap:10px;margin:0}
#filter-chips{display:flex;gap:8px;overflow-x:auto;padding-top:8px;scrollbar-width:thin}
.filter-chip{flex:none;display:flex;align-items:center;gap:10px;max-width:85vw;min-height:44px;padding:8px 12px;background:var(--soft);color:var(--link);border:1px solid var(--line);font-size:12px}
.filter-chip>span:first-child{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}''')
change('.controls button,.collection-controls button{','.controls button,.collection-controls button,#reset{')
s=re.sub(r'<label class="region-label" for="(?:region|access-filter)">.*?</select>',lambda m:'<div class="filter-field">'+m.group(0)+'</div>',s,flags=re.S)
change('.region-label{font-size:12px;margin-right:10px}', '.filter-field{display:grid;gap:6px;flex:1 1 120px;max-width:220px;min-width:0}\n.region-label{font-size:12px}')
change('padding:8px 12px;background:var(--surface);border:1px solid var(--line);min-height:44px;max-width:100%;font-size:16px}', 'padding:8px 12px;background:var(--surface);border:1px solid var(--line);min-height:44px;width:100%;min-width:0;max-width:100%;font-size:16px}')
change('.filter-panel{margin:0}', '.filter-panel{margin:0;scroll-margin-top:var(--search-offset,100px)}')
change('.filter-panel-body{padding-top:12px}', '.filter-panel-body{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-top:12px}')
change('#region{', '#region,#access-filter{')
change('.filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}', '.filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px;flex-basis:100%}')
change('.skip-link,.jump,.directory-tools,.hero-actions', '.skip-link,.jump,.directory-tools,.search-bar,.hero-actions')
# Expand the existing translation dictionary only for new controls.
prefix,rest=s.split('const translations=',1);dictionary,n=json.JSONDecoder().raw_decode(rest)
additions={
'es':['Todos los niveles de acceso','Filtrar acceso','Filtros activos','Quitar el filtro {filter}','Buscar','Buscar fuentes…'],
'zh-Hans':['所有访问级别','按访问权限筛选','当前筛选条件','移除筛选条件：{filter}','搜索','搜索来源…'],
'zh-Hant':['所有存取層級','依存取權限篩選','目前篩選條件','移除篩選條件：{filter}','搜尋','搜尋來源…'],
'ja':['すべてのアクセス区分','アクセスで絞り込む','適用中の条件','「{filter}」の条件を解除','検索','ソースを検索…'],
'ko':['모든 접근 유형','접근 유형 필터','적용된 필터','{filter} 필터 제거','검색','자료 검색…']}
keys=['All access levels','Filter access','Active filters','Remove {filter} filter','Search','Search sources…']
for locale,values in additions.items():dictionary[locale].update(zip(keys,values))
s=prefix+'const translations='+json.dumps(dictionary,ensure_ascii=False)+rest[n:]
change("const search=document.querySelector('#search'),region=document.querySelector('#region'),buttons=", "const search=document.querySelector('#search'),region=document.querySelector('#region'),accessFilter=document.querySelector('#access-filter'),buttons=")
change("function update(){let n=0;", "const accessByCard=new Map(cards.map(c=>[c,c.querySelector('.comparison div:last-child dd').textContent.trim()]));function activeFilterCount(){return (category==='All'?0:1)+(region.value==='All'?0:1)+(accessFilter.value==='All'?0:1)+(search.value.trim()?1:0)+(favoritesOnly?1:0);}function update(){let n=0;")
change("&&(region.value==='All'||c.dataset.region===region.value)&&c.textContent", "&&(region.value==='All'||c.dataset.region===region.value)&&(accessFilter.value==='All'||accessByCard.get(c)===accessFilter.value)&&c.textContent")
s=s.replace("const active=(category==='All'?0:1)+(region.value==='All'?0:1);", "const active=activeFilterCount();")
change("region.addEventListener('change',update);", "region.addEventListener('change',update);accessFilter.addEventListener('change',update);")
change("category='All';search.value='';region.value='All';favoritesOnly=false;", "category='All';search.value='';region.value='All';accessFilter.value='All';favoritesOnly=false;")
change("if(region.value!=='All')p.set('region',region.value);", "if(region.value!=='All')p.set('region',region.value);if(accessFilter.value!=='All')p.set('access',accessFilter.value);")
change("category!=='All'||region.value!=='All'||location.hash", "category!=='All'||region.value!=='All'||accessFilter.value!=='All'||location.hash")
change("region.value=[...region.options].some(o=>o.value===reg)?reg:'All';", "region.value=[...region.options].some(o=>o.value===reg)?reg:'All';const access=p.get('access');accessFilter.value=[...accessFilter.options].some(o=>o.value===access)?access:'All';")
change("}else{category='All';search.value='';region.value='All';}update();", "}else{category='All';search.value='';region.value='All';accessFilter.value='All';}update();")
change("function adaptFilters(){panel.open=phone.matches?mobileOpen:true;}", "function adaptFilters(){panel.open=phone.matches?mobileOpen:true;document.querySelector('#filter-toggle').setAttribute('aria-expanded',String(panel.open));}")
change("panel.addEventListener('toggle',()=>{if(phone.matches)mobileOpen=panel.open;});", "panel.addEventListener('toggle',()=>{if(phone.matches)mobileOpen=panel.open;document.querySelector('#filter-toggle').setAttribute('aria-expanded',String(panel.open));});")
change("adaptFilters();\nfunction viewHash", '''adaptFilters();
document.querySelector('#filter-toggle').addEventListener('click',()=>{const bar=document.querySelector('.search-bar');const near=panel.getBoundingClientRect().top>=bar.getBoundingClientRect().bottom&&panel.getBoundingClientRect().top<innerHeight;if(phone.matches&&panel.open&&near){panel.open=false;}else{panel.open=true;panel.scrollIntoView({block:'start',behavior:'instant'});region.focus({preventScroll:true});}});
const searchBar=document.querySelector('.search-bar');new ResizeObserver(()=>{document.documentElement.style.setProperty('--search-offset',(searchBar.getBoundingClientRect().height+16)+'px');}).observe(searchBar);
function renderFilterChips(){const holder=document.querySelector('#filter-chips');const filters=[];if(search.value.trim())filters.push(['search',t('Search')+': '+search.value.trim()]);if(category!=='All')filters.push(['category',t(category)]);if(region.value!=='All')filters.push(['region',t(region.value)]);if(accessFilter.value!=='All')filters.push(['access',t('Access')+': '+t(accessFilter.value)]);if(favoritesOnly)filters.push(['favorites',t('Favorites')]);holder.replaceChildren();holder.hidden=!filters.length;filters.forEach(([key,label],index)=>{const button=document.createElement('button');button.type='button';button.className='filter-chip';button.dataset.removeFilter=key;button.setAttribute('aria-label',t('Remove {filter} filter').replace('{filter}',label));const text=document.createElement('span');text.textContent=label;const icon=document.createElement('span');icon.textContent='×';icon.setAttribute('aria-hidden','true');button.append(text,icon);button.addEventListener('click',()=>{if(key==='search')search.value='';if(key==='category')category='All';if(key==='region')region.value='All';if(key==='access')accessFilter.value='All';if(key==='favorites')favoritesOnly=false;update();const next=holder.children[Math.min(index,holder.children.length-1)];(next||search).focus({preventScroll:true});});holder.append(button);});}
function viewHash''')
change("script,style,#language,h3 a", "script,style,#language,#filter-chips,h3 a")
change("function refreshDynamicLabels(){", "function refreshDynamicLabels(){renderFilterChips();")
# The access values stay stable when option labels are translated.
(root/'index.html').write_text(s)
assert re.findall(r'<article class="source".*?</article>',source.read_text(),re.S)==re.findall(r'<article class="source".*?</article>',s,re.S)
print('Working copy ready; all 52 source cards unchanged.')
