from pathlib import Path
import re
root=Path(__file__).parent;s=(root/'backup/site.html').read_text();css=re.search(r'<style>(.*?)</style>',s,re.S).group(1)
base,rest=css.split('@media(min-width:640px){',1)
def replace(a,b):
 global base
 assert a in base,a[:100]
 base=base.replace(a,b,1)
replace("--serif:'Instrument Serif',Georgia,serif;--sans:'Source Sans 3',Arial,sans-serif;", "--serif:'Instrument Serif',Georgia,serif;--sans:'Source Sans 3',Arial,sans-serif;\n --text-body:16px;--text-small:14px;--text-label:12px;--control-height:48px;--control-radius:2px;")
replace('font:15px/1.65 var(--sans)', 'font:var(--text-body)/1.7 var(--sans)')
replace('input{font:inherit;color:inherit}', 'input{font:inherit;color:inherit;border-radius:var(--control-radius)}')
replace('button{font:inherit;color:inherit;touch-action:manipulation;cursor:pointer}', 'button{font:inherit;color:inherit;border-radius:var(--control-radius);touch-action:manipulation;cursor:pointer}')
replace('select{font:inherit;color:inherit;touch-action:manipulation}', 'select{font:inherit;color:inherit;border-radius:var(--control-radius);touch-action:manipulation}')
replace('main{max-width:1440px;margin:auto;padding:0 24px}', 'main{max-width:1440px;margin:auto;padding:0 20px}')
replace('.masthead{display:flex;align-items:center;justify-content:space-between;gap:12px;', '.masthead{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px 16px;')
replace('#language{background:transparent;border:1px solid var(--line);padding:8px;min-height:44px;max-width:132px;font-size:14px}', '#language{background:var(--surface);border:1px solid var(--line);padding:10px 12px;min-height:var(--control-height);max-width:150px;font-size:var(--text-body)}')
replace('.hero-actions a{white-space:nowrap}', '.hero-actions a{display:inline-flex;align-items:center;min-height:var(--control-height);white-space:nowrap}')
replace('.hero-actions{display:flex;gap:20px;', '.hero-actions{display:flex;flex-wrap:wrap;gap:12px 20px;')
replace('.hero-actions a:first-child{background:', '.hero-actions a:first-child{display:inline-flex;align-items:center;min-height:var(--control-height);border-radius:var(--control-radius);background:')
replace('.filter-field{display:grid;gap:6px;flex:1 1 120px;max-width:220px;min-width:0}', '.filter-field{display:grid;gap:8px;flex:1 1 100%;max-width:none;min-width:0}')
replace('.region-label{font-size:12px}', '.region-label{font-size:var(--text-small);font-weight:550}')
replace('.source{padding:22px;', '.source{padding:20px;')
replace('width:38px;height:38px;', 'width:40px;height:40px;')
replace('min-height:30px', 'min-height:var(--control-height)')
replace('font-size:8px', 'font-size:var(--text-label)')
replace('.card-meta{letter-spacing:.1em;', '.card-meta{letter-spacing:.06em;')
replace('.category{letter-spacing:.1em;', '.category{letter-spacing:.07em;')
replace('.source-purpose{font-size:14px;line-height:1.65;', '.source-purpose{font-size:var(--text-body);line-height:1.7;')
replace('.editor-pick p,.shortlist p,.workflow p,.notes p,.notes li{font-size:14px}', '.editor-pick p,.shortlist p,.workflow p,.notes p,.notes li{font-size:var(--text-body)}')
replace('.hero .cover-copy>p:not(.cover-line){max-width:54ch;color:var(--muted);font-size:14px}', '.hero .cover-copy>p:not(.cover-line){max-width:54ch;color:var(--muted);font-size:var(--text-body)}')
replace('.section-top>p{color:var(--muted);font-size:14px;', '.section-top>p{color:var(--muted);font-size:var(--text-body);')
replace('.comparison dd{margin:6px 0 0;font-size:12px;', '.comparison dd{margin:6px 0 0;font-size:var(--text-small);')
replace('.access{font-size:12px;', '.access{font-size:var(--text-small);')
replace('.source-details summary{display:flex;justify-content:space-between;align-items:center;min-height:44px;font-size:12px;', '.source-details summary{display:flex;justify-content:space-between;align-items:center;min-height:var(--control-height);font-size:var(--text-small);')
replace('.context-link{display:inline-flex;align-items:center;min-height:36px}', '.context-link,.country-evidence{display:inline-flex;align-items:center;min-height:var(--control-height)}')
replace('.jump a{font-size:12px;min-height:36px;', '.jump a{font-size:var(--text-small);min-height:var(--control-height);')
replace('.collection-view p{font-size:12px;', '.collection-view p{font-size:var(--text-small);')
replace('.route-body{padding:0 18px 18px;font-size:13px}', '.route-body{padding:0 20px 20px;font-size:var(--text-small)}')
replace('gap:14px;padding:18px;cursor:pointer;', 'gap:16px;padding:20px;cursor:pointer;')
replace('padding:8px 12px;background:var(--surface);border:1px solid var(--line);', 'padding:12px;background:var(--surface);border:1px solid var(--line);')
# One readable metadata scale and one control height across existing component rules.
base=re.sub(r'font-size:(?:9|10|11)px', 'font-size:var(--text-label)',base)
base=base.replace('min-height:44px','min-height:var(--control-height)')
# Enlarge interactive labels while keeping supporting metadata at 12px.
for selector in ['.controls button,.collection-controls button,#reset','.filters button','.filter-chip','.favorite-source','.copy-source','#share-view','.footer-nav a','.print-guide','.mobile-nav button','.sections-heading button','.other-countries summary','.other-country-grid button','.browse-market']:
 pattern=re.escape(selector)+r'\{([^}]*)\}'
 m=re.search(pattern,base);assert m,selector
 rule=m.group(0);new=re.sub(r'font-size:(?:12|13)px','font-size:var(--text-small)',rule)
 base=base.replace(rule,new,1)
replace('.source{padding:20px;background:var(--surface);border:1px solid var(--line);display:flex;flex-direction:column;min-width:0}', '.source{padding:20px;background:var(--surface);border:1px solid var(--line);display:flex;flex-direction:column;min-width:0}\n.source:focus-within{border-color:var(--accent)}')
# Keep responsive variants in their existing media block; leave embedded fonts and print sizes intact.
rest=rest.replace('body{padding-bottom:0}', 'body{padding-bottom:0}.filter-field{flex:1 1 160px;max-width:220px}',1)
rest=rest.replace('.hero .cover-copy>p:not(.cover-line){font-size:15px}', '.hero .cover-copy>p:not(.cover-line){font-size:var(--text-body)}',1)
rest=rest.replace('.cover-image figcaption{font-size:10px}', '.cover-image figcaption{font-size:var(--text-label)}',1)
hover='''@media(hover:hover) and (pointer:fine){
 :where(.controls button,.filters button,.collection-controls button,#reset,#show-all-saved,.filter-chip,.favorite-source,.copy-source,.mobile-nav button,.sections-heading button,.other-country-grid button,.asia-markets button,.browse-market,.print-guide,#share-view):not(:disabled):hover{background:var(--soft);border-color:var(--accent)}
}
'''
rest=rest.replace('@media(prefers-color-scheme:dark){',hover+'@media(prefers-color-scheme:dark){',1)
rest=rest.replace('section{padding:22px 0}.research-route', '.context-link,.country-evidence{min-height:0;display:inline}.source h3 a{min-height:0}section{padding:22px 0}.research-route',1)
newcss=base+'@media(min-width:640px){'+rest
s=s.replace(css,newcss,1);(root/'index.html').write_text(s)
old=(root/'backup/site.html').read_text();assert re.findall(r'<script>(.*?)</script>',old,re.S)==re.findall(r'<script>(.*?)</script>',s,re.S)
assert old.split('<body>',1)[1]==s.split('<body>',1)[1]
assert re.findall(r'@font-face\{[^}]+\}',old)==re.findall(r'@font-face\{[^}]+\}',s)
print('CSS-only polish staged; HTML, source content, scripts, and embedded fonts unchanged.')
