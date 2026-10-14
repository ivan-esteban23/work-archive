from pathlib import Path
import re,json,html,collections
root=Path(__file__).parent;rows=json.loads((root/'countries.json').read_text());byid={r['id']:r for r in rows};s=(root/'backup/site.html').read_text()
def change(a,b):
 global s
 assert a in s,a[:130]
 s=s.replace(a,b,1)
def card_edit(m):
 card=m.group(0);num=re.search(r'<div class="card-meta"><span>(.*?)</span>',card).group(1);row=byid[num]
 card=card.replace('data-region="'+row['coverage']+'"','data-region="'+row['coverage']+'" data-country="'+html.escape(row['country'],quote=True)+'"',1)
 card=card.replace('<div class="card-meta"><span>'+num+'</span><span>'+row['coverage']+'</span>', '<div class="card-meta"><span>'+num+'</span><span class="country-label"><span class="metadata-label">Country/base</span><span>'+html.escape(row['country'])+'</span></span>',1)
 card=card.replace('<div class="compare-access">','<div class="compare-coverage"><dt>Coverage</dt><dd>'+row['coverage']+'</dd></div><div class="compare-access">',1)
 card=card.replace('</div></details>', '<p class="country-review">Country check · <time datetime="2026-10-13">2026-10-13</time> · <a class="country-evidence" href="'+html.escape(row['country_source'],quote=True)+'" target="_blank" rel="noopener">Country/base evidence ↗</a></p></div></details>',1)
 return card
s=re.sub(r'<article class="source".*?</article>',card_edit,s,flags=re.S)
countries=sorted(set(r['country'] for r in rows));standard=[c for c in countries if not c.startswith('International')];other=[c for c in countries if c.startswith('International')]
options='<option value="All">All</option>'+''.join('<option value="'+c+'">'+c+'</option>' for c in standard)+'<optgroup label="Projects and communities">'+''.join('<option value="'+c+'">'+c+'</option>' for c in other)+'</optgroup>'
change('<div class="filter-panel-body">','<div class="filter-panel-body"><div class="filter-field"><label class="region-label" for="country-filter">Country/base</label><select id="country-filter" aria-label="Filter country">'+options+'</select></div>')
change('for="region">Region</label>','for="region">Coverage</label>')
change('aria-label="Filter region"','aria-label="Filter coverage"')
change('#region,#access-filter{','#region,#access-filter,#country-filter{')
change('.card-meta{','.country-label{display:grid;gap:2px;text-align:right;max-width:78%;overflow-wrap:anywhere}\n.metadata-label{font-size:8px;color:var(--muted);letter-spacing:.07em}\n.card-meta{')
change('.compare-content{grid-column:1/-1;grid-row:2}', '.compare-content{grid-column:1/-1;grid-row:2}\n.compare-coverage{grid-column:1/-1;grid-row:3}')
change('.review-date{','.country-review{font-size:11px;line-height:1.6;color:var(--muted);margin-top:14px}\n.review-date{')
# Make all verified countries browsable while retaining the familiar Asia anchor.
change('id="asia-title">Browse Asia</p>', 'id="asia-title">Browse by country</p>')
change('Start with one market, then explore the full directory for global tools and archives.', 'Country/base identifies the publisher, project team or national edition. Coverage is the directory’s research focus, not an exhaustive list of markets covered.')
s=s.replace('Browse Asia ↗','Browse countries ↗').replace('>Browse Asia</a>','>Browse countries</a>')
entry=re.search(r'<nav class="asia-browse".*?</nav>',s,re.S).group(0);updated=entry.replace('data-browse-region=','data-browse-country=').replace('data-market-count=','data-country-count=')
rest=[c for c in countries if c not in ['China','Japan','South Korea']]
more='<details class="other-countries"><summary>More countries &amp; communities</summary><div class="other-country-grid">'+''.join('<button type="button" data-browse-country="'+c+'" aria-pressed="false"><span>'+c+'</span><span class="country-count" data-country-count="'+c+'"></span></button>' for c in rest)+'</div></details>'
updated=updated.replace('<p class="asia-note">',more+'<p class="asia-note">');change(entry,updated)
change('.asia-note{', '.other-countries{margin-top:12px}\n.other-countries summary{min-height:44px;display:flex;align-items:center;color:var(--link);font-size:13px;cursor:pointer}\n.other-country-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:8px}\n.other-country-grid button{display:flex;flex-direction:column;align-items:flex-start;gap:8px;min-height:72px;min-width:0;padding:12px;border:1px solid var(--line);background:var(--surface);color:var(--ink);text-align:left;font-size:13px;overflow-wrap:anywhere}\n.other-country-grid button[aria-pressed=true]{background:var(--soft);border-color:var(--accent)}\n.country-count{font-size:11px;color:var(--muted)}\n.asia-note{')
change('.asia-markets{gap:14px}', '.other-country-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.asia-markets{gap:14px}')
change('@media(min-width:1000px){', '@media(min-width:1000px){\n .other-country-grid{grid-template-columns:repeat(4,minmax(0,1fr))}')
# Stable values survive translation; new source-country filtering is independent of coverage.
change("accessFilter=document.querySelector('#access-filter'),buttons=", "accessFilter=document.querySelector('#access-filter'),countryFilter=document.querySelector('#country-filter'),buttons=")
change("+(accessFilter.value==='All'?0:1)+(search.value.trim()?1:0)", "+(accessFilter.value==='All'?0:1)+(countryFilter.value==='All'?0:1)+(search.value.trim()?1:0)")
change("&&(accessFilter.value==='All'||accessByCard.get(c)===accessFilter.value)&&c.textContent", "&&(accessFilter.value==='All'||accessByCard.get(c)===accessFilter.value)&&(countryFilter.value==='All'||c.dataset.country===countryFilter.value)&&c.textContent")
change("accessFilter.addEventListener('change',update);", "accessFilter.addEventListener('change',update);countryFilter.addEventListener('change',update);")
s=s.replace("accessFilter.value='All';search.value='';", "accessFilter.value='All';countryFilter.value='All';search.value='';")
s=s.replace("region.value='All';accessFilter.value='All';favoritesOnly=false;", "region.value='All';accessFilter.value='All';countryFilter.value='All';favoritesOnly=false;")
change("if(accessFilter.value!=='All')p.set('access',accessFilter.value);", "if(accessFilter.value!=='All')p.set('access',accessFilter.value);if(countryFilter.value!=='All')p.set('country',countryFilter.value);")
change("accessFilter.value!=='All'||location.hash", "accessFilter.value!=='All'||countryFilter.value!=='All'||location.hash")
change("accessFilter.value=[...accessFilter.options].some(o=>o.value===access)?access:'All';", "accessFilter.value=[...accessFilter.options].some(o=>o.value===access)?access:'All';const country=p.get('country');countryFilter.value=[...countryFilter.options].some(o=>o.value===country)?country:'All';")
change("region.value='All';accessFilter.value='All';}update();", "region.value='All';accessFilter.value='All';countryFilter.value='All';}update();")
change("filters.push(['region',t(region.value)])", "filters.push(['region',t('Coverage')+': '+t(region.value)])")
change("if(accessFilter.value!=='All')filters.push", "if(countryFilter.value!=='All')filters.push(['country',t('Country/base')+': '+t(countryFilter.value)]);if(accessFilter.value!=='All')filters.push")
change("if(key==='access')accessFilter.value='All';", "if(key==='access')accessFilter.value='All';if(key==='country')countryFilter.value='All';")
old=re.search(r'function refreshAsiaBrowse\(\)\{.*?\}\nfunction refreshDynamicLabels',s,re.S).group(0)
new='''function refreshAsiaBrowse(){document.querySelectorAll('[data-browse-country],[data-browse-region]').forEach(button=>{const country=button.dataset.browseCountry;const market=country||button.dataset.browseRegion;const n=cards.filter(c=>country?c.dataset.country===country:c.dataset.region===market).length;button.setAttribute('aria-label',t(country?'Browse {country}: {n} sources':'Explore {country} coverage: {n} sources').replace('{country}',t(market)).replace('{n}',n));button.setAttribute('aria-pressed',String(country?countryFilter.value===country:region.value===market));const count=button.querySelector('[data-country-count]');if(count)count.textContent=t(n===1?'{n} source':'{n} sources').replace('{n}',n);});}
function refreshDynamicLabels'''
change(old,new)
old=re.search(r"document.querySelectorAll\('\[data-browse-region\]'\).forEach\(button=>button.addEventListener\('click'.*?\}\)\);",s,re.S).group(0)
new="document.querySelectorAll('[data-browse-country],[data-browse-region]').forEach(button=>button.addEventListener('click',()=>{const country=button.dataset.browseCountry;region.value=country?'All':button.dataset.browseRegion;countryFilter.value=country||'All';category='All';accessFilter.value='All';search.value='';favoritesOnly=false;update();const first=cards.find(c=>!c.hidden);const target=first||document.querySelector('#directory');target.scrollIntoView({block:'start',behavior:'instant'});if(first)first.querySelector('h3 a').focus({preventScroll:true});else search.focus({preventScroll:true});}));"
change(old,new)
# Include country provenance in exported favorites without changing source review dates.
change("lines.push('- '+t('Region')+': '+t(card.dataset.region));", "lines.push('- '+t('Country/base')+': '+t(card.dataset.country));")
change("if(context)lines.push('['+t('Official context')+']('+context.href+')');lines.push('');", "if(context)lines.push('['+t('Official context')+']('+context.href+')');const evidence=card.querySelector('.country-evidence');lines.push('['+t('Country/base evidence')+']('+evidence.href+')');lines.push('');")
change("document.querySelectorAll('[placeholder],[title],[aria-label],[alt]')", "document.querySelectorAll('[placeholder],[title],[aria-label],[alt],[label]')")
s=s.replace("['placeholder','title','aria-label','alt']", "['placeholder','title','aria-label','alt','label']")
change('.other-countries summary{', '.other-countries summary::after{content:\' +\';margin-left:auto;font-size:20px}\n.other-countries[open] summary::after{content:\' −\'}\n.other-countries summary{')

# Translate country labels and the new interface terms; existing dictionaries remain intact.
prefix,tail=s.split('const translations=',1);dictionary,n=json.JSONDecoder().raw_decode(tail)
country_translations={
'United States':['Estados Unidos','美国','美國','アメリカ合衆国','미국'],
'United Kingdom':['Reino Unido','英国','英國','イギリス','영국'],
'France':['Francia','法国','法國','フランス','프랑스'],
'Taiwan':['Taiwán','台湾','臺灣','台湾','대만'],
'Bulgaria':['Bulgaria','保加利亚','保加利亞','ブルガリア','불가리아'],
'Canada':['Canadá','加拿大','加拿大','カナダ','캐나다'],
'Australia':['Australia','澳大利亚','澳大利亞','オーストラリア','호주'],
'Sweden':['Suecia','瑞典','瑞典','スウェーデン','스웨덴'],
'Kazakhstan':['Kazajistán','哈萨克斯坦','哈薩克斯坦','カザフスタン','카자흐스탄'],
'Italy':['Italia','意大利','義大利','イタリア','이탈리아'],
'Germany':['Alemania','德国','德國','ドイツ','독일'],
'Spain':['España','西班牙','西班牙','スペイン','스페인'],
'Netherlands':['Países Bajos','荷兰','荷蘭','オランダ','네덜란드'],
'International project':['Proyecto internacional','国际项目','國際專案','国際プロジェクト','국제 프로젝트'],
'International community':['Comunidad internacional','国际社区','國際社群','国際コミュニティ','국제 커뮤니티']}
ui={
'{n} source':['{n} fuente','{n} 个来源','{n} 個來源','{n} 件のソース','자료 {n}개'],
'Country/base':['País/base','国家／所在地','國家／所在地','国／拠点','국가/기반'],
'Coverage':['Cobertura','报道范围','報導範圍','対象地域','다루는 지역'],
'Filter country':['Filtrar país','按国家筛选','依國家篩選','国で絞り込む','국가 필터'],
'Filter coverage':['Filtrar cobertura','按报道范围筛选','依報導範圍篩選','対象地域で絞り込む','다루는 지역 필터'],
'Projects and communities':['Proyectos y comunidades','项目和社区','專案與社群','プロジェクトとコミュニティ','프로젝트 및 커뮤니티'],
'Browse by country':['Explorar por país','按国家浏览','依國家瀏覽','国別に探す','국가별 둘러보기'],
'Browse countries':['Explorar países','浏览国家','瀏覽國家','国別に探す','국가 둘러보기'],
'Browse countries ↗':['Explorar países ↗','浏览国家 ↗','瀏覽國家 ↗','国別に探す ↗','국가 둘러보기 ↗'],
'More countries & communities':['Más países y comunidades','更多国家和社区','更多國家與社群','その他の国とコミュニティ','더 많은 국가와 커뮤니티'],
'Country check':['Revisión del país','国家信息核查','國家資訊核查','国情報の確認','국가 정보 확인'],
'Country/base evidence ↗':['Fuente del país/base ↗','国家／所在地依据 ↗','國家／所在地依據 ↗','国／拠点の出典 ↗','국가/기반 출처 ↗'],
'Country/base evidence':['Fuente del país/base','国家／所在地依据','國家／所在地依據','国／拠点の出典','국가/기반 출처'],
'Explore {country} coverage: {n} sources':['Explorar la cobertura de {country}: {n} fuentes','探索{country}的报道范围：{n} 个来源','探索{country}的報導範圍：{n} 個來源','{country}の対象ソース：{n} 件','{country} 관련 자료: {n}개'],
'Country/base identifies the publisher, project team or national edition. Coverage is the directory’s research focus, not an exhaustive list of markets covered.':['País/base identifica al editor, equipo del proyecto o edición nacional. Cobertura indica el enfoque de investigación del directorio, no una lista exhaustiva de los mercados tratados.','国家／所在地指出版方、项目团队或国家版本。报道范围表示本目录的研究重点，并非来源涵盖市场的完整列表。','國家／所在地指出版方、專案團隊或國家版本。報導範圍表示本目錄的研究重點，並非來源涵蓋市場的完整清單。','国／拠点は出版社、プロジェクトチーム、または各国版を指します。対象地域はこの一覧での研究上の重点であり、扱う市場のすべてを示すものではありません。','국가/기반은 발행사, 프로젝트 팀 또는 국가별 판을 뜻합니다. 다루는 지역은 이 목록의 연구 초점이며, 모든 시장을 나열한 것은 아닙니다.']}
for key,values in {**country_translations,**ui}.items():
 for locale,value in zip(['es','zh-Hans','zh-Hant','ja','ko'],values):dictionary[locale][key]=value
s=prefix+'const translations='+json.dumps(dictionary,ensure_ascii=False)+tail[n:]
(root/'index.html').write_text(s)
assert s.count('<article class="source"')==52
# Create a cited audit and align the source table in the existing Obsidian note.
counts=collections.Counter(r['country'] for r in rows)
report='''---\ntags: [visual-research, sources, country-audit]\nupdated: 2026-10-13\n---\n\n# The Visual Edit — Country Audit 2026-10-13\n\nCountry/base records the source operator, posted editorial base, project team or linked national edition. It does not describe owner nationality, the countries of individual contributors, or everywhere a tool can be used. Coverage retains the directory’s existing research-focus grouping and is not an exhaustive geography of published content.\n\n**50 sources have country labels across 16 countries.** Shaarli and r/femalefashionadvice are explicitly classified as an international project and an international community. Their hosting providers’ countries are not substituted for a publisher location.\n\nCountry evidence was checked on 2026-10-13. Existing source-review dates and access labels are preserved; this country audit does not claim fresh verification of subscriptions or logged-in features. Official contact/legal/about pages are preferred. Company-authored GitHub, app-store and LinkedIn profiles are identified in the notes; Vestoj uses an industry editorial biography corroborated by a university-hosted event biography.\n\n## Counts\n\n| Country/base | Sources |\n| --- | ---: |\n'''
report+=''.join('| '+country+' | '+str(count)+' |\n' for country,count in sorted(counts.items()))
report+='\n## Source-by-source evidence\n\n| No. | Source | Country/base | Coverage / research focus | Country evidence | Basis / limits |\n| --- | --- | --- | --- | --- | --- |\n'
for row in rows:report+='| '+row['id']+' | ['+row['name']+']('+row['url']+') | '+row['country']+' | '+row['coverage']+' | [Evidence]('+row['country_source']+') | '+row['country_note']+' |\n'
report+='\n## Additional corroboration\n\n- [Eagle developer identifies OGDESIGN](https://en.eagle.cool/lizhi-reseller). Unrelated Eagle engineering and hardware businesses were excluded.\n- [Printed Matter’s official art-book-fair FAQ](https://printedmatterartbookfairs.org/faq) identifies its Chelsea NYC store.\n- [Vestoj founder event biography hosted by the School of Visual Arts](https://sva.edu/events/anja-aronowsky-cronberg-thinking-critically-about-fashion-an-introduction-to-vestoj) corroborates the Paris editorial connection; it is historical context rather than a current registered-office record.\n\n## Navigation behavior\n\nCountry tiles and the Country/base filter use the new country classification. Thus the China tile has four sources; Jing Daily is available under United States and under China coverage. The Asia shortlist continues to explore coverage (five China-focused sources, four Japan-focused sources, three Korea-focused sources). Country and coverage filters can be combined. Favorites exports include both fields and a country-evidence link.\n'
(root/'The Visual Edit — Country Audit 2026-10-13.md').write_text(report)
md=(root/'backup/note.md').read_text();urlmap={r['url']:r for r in rows};newlines=[];matched=0
for line in md.splitlines():
 if line.startswith('| Logo | Source | Region |'):
  line=line.replace('| Region |','| Country/base | Coverage |',1)
 elif line.startswith('| ![['):
  row=next((r for url,r in urlmap.items() if ']('+url+')' in line),None)
  if row:
   old=' | '+row['coverage']+' | ';new=' | '+row['country']+' | '+row['coverage']+' | ';assert old in line;line=line.replace(old,new,1);matched+=1
 elif line.startswith('| --- |') and newlines and '| Country/base | Coverage |' in newlines[-1]:
  line=line.replace('| --- |','| --- | --- |',1)
 newlines.append(line)
assert matched==52,matched
md='\n'.join(newlines)+'\n'
marker='[[Attachments/Pinterest Alternatives/Pinterest Alternatives — Visual Research and Moodboarding.html|Open the designed HTML directory]]'
assert marker in md
md=md.replace(marker,marker+' · [[The Visual Edit — Country Audit 2026-10-13|Country/base audit and evidence]]',1)
(root/'vault-note.md').write_text(md)
print('Prepared HTML, 52-row country audit, and updated Obsidian source table.')
