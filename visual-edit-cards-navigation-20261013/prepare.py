from pathlib import Path
import re,json,hashlib,shutil
root=Path(__file__).parent;source=Path('/home/ivanaguilera/Work/visual-edit-public/dist/index.html');s=source.read_text();backup=root/'backup';backup.mkdir(exist_ok=True)
if not (backup/'index.html').exists():shutil.copy2(source,backup/'index.html')
(root/'source.sha256').write_text(hashlib.sha256(source.read_bytes()).hexdigest())
def change(a,b):
 global s
 assert a in s,a[:120]
 s=s.replace(a,b,1)
# Retain each source's complete research fields and existing button hooks.
def card_edit(m):
 card=m.group(0)
 for key in ['Language','Content','Access']:
  card=card.replace('<div><dt>'+key+'</dt>','<div class="compare-'+key.lower()+'"><dt>'+key+'</dt>',1)
 actions=re.search(r'<button class="favorite-source".*?</button><button class="copy-source".*?</button>',card,re.S).group(0)
 card=card.replace(actions,'<div class="source-actions" role="group" aria-label="Source actions">'+actions.replace('Copy source link ↗</button>','Copy link ↗</button>')+'</div>',1)
 return card
s=re.sub(r'<article class="source".*?</article>',card_edit,s,flags=re.S)
change('<p class="comparison-key">','<div class="collection-view" role="region" aria-labelledby="collection-title" hidden><div><h3 id="collection-title" tabindex="-1">Your collection</h3><p id="collection-summary" aria-live="polite"></p><p>Saved in this browser only. Export your selection to keep a copy in Obsidian. Shared view links do not include your private favorites.</p></div><button id="show-all-saved" type="button">Show all saved sources</button></div><p class="comparison-key">')
links=re.search(r'<nav class="jump".*?</nav>',s,re.S).group(0);links=re.search(r'>(.*?)</nav>',links,re.S).group(1)
mobile='<nav class="mobile-nav" aria-label="Mobile navigation"><button id="mobile-directory" type="button" aria-pressed="true">Directory</button><button id="mobile-saved" type="button" aria-pressed="false"><span>Saved</span><span id="mobile-saved-count">0</span></button><button id="mobile-sections" type="button" aria-haspopup="dialog" aria-controls="sections-menu">Sections</button></nav><dialog id="sections-menu" aria-labelledby="sections-title"><div class="sections-heading"><h2 id="sections-title">Explore sections</h2><form method="dialog"><button type="submit">Close</button></form></div><nav aria-label="Sections">'+links+'</nav></dialog>'
change('</main><p id="copy-status"','</main>'+mobile+'<p id="copy-status"')
# Edit existing rules and put new components beside their related rules.
change('scroll-padding-top:var(--search-offset,100px);', 'scroll-padding-top:var(--search-offset,100px);scroll-padding-bottom:calc(90px + env(safe-area-inset-bottom));')
change('body{margin:0;', 'body{padding-bottom:calc(76px + env(safe-area-inset-bottom));margin:0;')
change('.source h3{margin:0 0 14px}', '.source h3{margin:0 0 14px;font-size:24px;line-height:1.2}')
change('.comparison{display:grid;grid-template-columns:1fr 1fr 1fr;', '.comparison{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);')
change('.comparison div{min-width:0}', '.comparison div{min-width:0}\n.compare-content{grid-column:1/-1;grid-row:2}\n.compare-access{grid-column:2;grid-row:1}')
change('.comparison div:last-child dd{font-weight:550;color:var(--link)}', '.comparison div:last-child dd{display:inline-block;max-width:100%;padding:3px 8px;border:1px solid var(--line);background:var(--soft);font-weight:550;color:var(--link)}')
change('.favorite-source{display:flex;', '.source-actions{display:flex;gap:14px;border-top:1px solid var(--line);padding-top:8px;margin-top:8px}\n.favorite-source{flex:1;min-width:0;display:flex;')
change('.copy-source{display:flex;align-items:center;gap:9px;min-height:44px;background:transparent;border:0;border-top:1px solid var(--line);color:var(--link);font-size:12px;padding:8px 0;text-align:left;margin-top:2px}', '.copy-source{flex:1;min-width:0;display:flex;justify-content:flex-end;align-items:center;gap:9px;min-height:44px;background:transparent;border:0;color:var(--link);font-size:12px;padding:8px 0;text-align:right}')
change('.collection-controls button:disabled{','.collection-controls button:disabled,#show-all-saved:disabled{')
change('.collection-controls{', '.collection-view{display:flex;gap:20px;align-items:center;justify-content:space-between;border:1px solid var(--line);border-left:2px solid var(--accent);background:var(--surface);padding:20px;margin:24px 0;flex-wrap:wrap}\n.collection-view h3{margin:0 0 8px}\n.collection-view p{font-size:12px;color:var(--muted);max-width:72ch;margin:6px 0}\n#show-all-saved{min-height:44px;padding:10px 14px;border:1px solid var(--line);background:var(--soft);color:var(--link);font-size:13px}\n.collection-controls{')
change('.copy-status{position:fixed;bottom:20px;', '.copy-status{position:fixed;bottom:calc(90px + env(safe-area-inset-bottom));')
change('#copy-dialog{', '''.mobile-nav{position:fixed;bottom:0;left:0;right:0;z-index:30;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px;border-top:1px solid var(--line);background:var(--surface);padding:8px max(12px,env(safe-area-inset-left)) max(8px,env(safe-area-inset-bottom));}
.mobile-nav button{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border:0;background:transparent;color:var(--muted);font-size:13px}
.mobile-nav button[aria-pressed=true]{color:var(--ink);background:var(--soft)}
#mobile-saved-count{font-size:11px;font-variant-numeric:tabular-nums}
#sections-menu{width:min(92vw,520px);max-height:80dvh;overflow:auto;padding:24px;border:1px solid var(--line);background:var(--surface);color:var(--ink)}
#sections-menu::backdrop{background:#0008}
.sections-heading{display:flex;align-items:start;justify-content:space-between;gap:18px;margin-bottom:18px}
.sections-heading h2{font-size:32px;margin:0}
.sections-heading button{min-height:44px;padding:8px 12px;border:1px solid var(--line);background:transparent;color:var(--link);font-size:13px}
#sections-menu nav{display:grid}
#sections-menu a{display:flex;align-items:center;min-height:48px;border-top:1px solid var(--line);font-size:14px;text-decoration:none}
#copy-dialog{''')
change('@media(min-width:640px){', '@media(min-width:640px){\n body{padding-bottom:0}html{scroll-padding-bottom:20px}.mobile-nav{display:none}.copy-status{bottom:20px}')
change('body{font-size:11px}main{','body{font-size:11px;padding-bottom:0}main{')
change('.language-switch,.copy-status,#copy-dialog,#empty,.footer-nav{', '.language-switch,.copy-status,#copy-dialog,#empty,.footer-nav,.mobile-nav,#sections-menu,.collection-view,.source-actions{')
# Measure the sticky row immediately after chips change, before navigation scrolls.
change("new ResizeObserver(()=>{document.documentElement.style.setProperty('--search-offset',(searchBar.getBoundingClientRect().height+16)+'px');}).observe(searchBar);", "function updateSearchOffset(){document.documentElement.style.setProperty('--search-offset',(searchBar.getBoundingClientRect().height+16)+'px');}new ResizeObserver(updateSearchOffset).observe(searchBar);")
change("holder.append(button);});}\nfunction viewHash", "holder.append(button);});updateSearchOffset();}\nfunction viewHash")

# New UI strings are translated; source names and research text stay unchanged.
prefix,rest=s.split('const translations=',1);dictionary,n=json.JSONDecoder().raw_decode(rest)
keys=['Source actions','Copy link ↗','Save','Saved','Your collection','Show all saved sources','Mobile navigation','Directory','Sections','Explore sections','{visible} of {saved} saved sources shown.','No saved sources match these filters. Show all saved sources to broaden your selection.']
values={
'es':['Acciones de la fuente','Copiar enlace ↗','Guardar','Guardado','Tu colección','Mostrar todas las fuentes guardadas','Navegación móvil','Directorio','Secciones','Explorar secciones','Se muestran {visible} de {saved} fuentes guardadas.','Ninguna fuente guardada coincide con estos filtros. Muestra todas las fuentes guardadas para ampliar la selección.'],
'zh-Hans':['来源操作','复制链接 ↗','收藏','已收藏','你的收藏','显示所有已收藏来源','移动导航','目录','章节','浏览章节','显示 {saved} 个已收藏来源中的 {visible} 个。','没有已收藏来源符合这些筛选条件。显示所有已收藏来源以扩大选择范围。'],
'zh-Hant':['來源操作','複製連結 ↗','收藏','已收藏','你的收藏','顯示所有已收藏來源','行動導覽','目錄','章節','瀏覽章節','顯示 {saved} 個已收藏來源中的 {visible} 個。','沒有已收藏來源符合這些篩選條件。顯示所有已收藏來源以擴大選擇範圍。'],
'ja':['ソースの操作','リンクをコピー ↗','保存','保存済み','あなたのコレクション','保存済みソースをすべて表示','モバイルナビゲーション','一覧','セクション','セクションを探す','保存済み {saved} 件中 {visible} 件を表示。','条件に一致する保存済みソースはありません。保存済みソースをすべて表示して選択範囲を広げてください。'],
'ko':['자료 작업','링크 복사 ↗','저장','저장됨','내 컬렉션','저장한 자료 모두 보기','모바일 탐색','목록','섹션','섹션 둘러보기','저장한 자료 {saved}개 중 {visible}개 표시.','이 필터에 맞는 저장 자료가 없습니다. 저장한 자료를 모두 표시하여 선택 범위를 넓히세요.']}
for locale,v in values.items():dictionary[locale].update(zip(keys,v))
s=prefix+'const translations='+json.dumps(dictionary,ensure_ascii=False)+rest[n:]
change("t(saved?'Saved source':'Save source')", "t(saved?'Saved':'Save')")
change("'No favorites match these filters. Reset filters to see all sources.'", "'No saved sources match these filters. Show all saved sources to broaden your selection.'")
change("document.querySelector('#favorites-count').textContent=favoriteKeys.size;", "document.querySelector('#favorites-count').textContent=favoriteKeys.size;document.querySelector('#mobile-saved-count').textContent=favoriteKeys.size;document.querySelector('#mobile-saved').setAttribute('aria-pressed',String(favoritesOnly));document.querySelector('#mobile-directory').setAttribute('aria-pressed',String(!favoritesOnly));document.querySelector('.collection-view').hidden=!favoritesOnly;document.querySelector('#collection-summary').textContent=t('{visible} of {saved} saved sources shown.').replace('{visible}',cards.filter(c=>!c.hidden).length).replace('{saved}',favoriteKeys.size);document.querySelector('#show-all-saved').disabled=!favoriteKeys.size;")
change("saveFavorites();update();}));document.querySelector('#favorites-view')", "saveFavorites();update();if(favoritesOnly&&b.closest('.source').hidden){const next=cards.find(c=>!c.hidden)?.querySelector('.favorite-source');(next||document.querySelector('#collection-title')).focus({preventScroll:true});}}));document.querySelector('#favorites-view')")
change("function saveFavorites(){", '''document.querySelector('#show-all-saved').addEventListener('click',()=>{category='All';region.value='All';accessFilter.value='All';search.value='';favoritesOnly=true;update();document.querySelector('#collection-title').focus({preventScroll:true});});
function navigateDirectory(saved){favoritesOnly=saved;update();const target=document.querySelector(saved?'#collection-title':'#directory');target.scrollIntoView({block:'start',behavior:'instant'});target.setAttribute('tabindex','-1');target.focus({preventScroll:true});}
document.querySelector('#mobile-directory').addEventListener('click',()=>navigateDirectory(false));document.querySelector('#mobile-saved').addEventListener('click',()=>navigateDirectory(true));
const sectionsMenu=document.querySelector('#sections-menu');document.querySelector('#mobile-sections').addEventListener('click',()=>{document.querySelector('#mobile-sections').focus({preventScroll:true});sectionsMenu.showModal();});sectionsMenu.querySelectorAll('a').forEach(a=>a.addEventListener('click',event=>{event.preventDefault();sectionsMenu.close();const target=document.querySelector(a.getAttribute('href'));if(a.getAttribute('href')==='#directory'){favoritesOnly=false;update();}target.scrollIntoView({block:'start',behavior:'instant'});target.setAttribute('tabindex','-1');target.focus({preventScroll:true});}));
function saveFavorites(){''')
(root/'index.html').write_text(s)
assert re.findall(r'@font-face\{[^}]+\}',source.read_text())==re.findall(r'@font-face\{[^}]+\}',s)
print('Working copy ready: 52 cards, navigation, and collection view.')
