from pathlib import Path
import re,json
root=Path(__file__).parent;s=(root/'backup/site.html').read_text();original=s
roles=[]
def editor_edit(m):
 card=m.group(0);label=re.search(r'<span class="eyebrow">(.*?)</span>',card).group(1);num,purpose=label.split(' / ',1);roles.append((label,purpose))
 return card.replace('<span class="eyebrow">'+label+'</span>', '<div class="pick-role"><span class="pick-num">'+num+'</span><span class="pick-purpose">'+purpose+'</span></div>',1)
s=re.sub(r'<article class="editor-pick">.*?</article>',editor_edit,s,flags=re.S)
def route_edit(m):
 route=m.group(0);route=route.replace('</span><span class="route-toggle"', '<span class="route-outline">3 steps</span></span><span class="route-toggle"',1)
 outcome=re.search(r'<p class="route-result">.*?</p>',route,re.S).group(0);route=route.replace(outcome,'',1).replace('<div class="route-body">','<div class="route-body">'+outcome,1)
 def step_edit(m):
  step=m.group(0);sources=re.search(r'<p class="route-sources">.*?</p>',step,re.S).group(0);step=step.replace(sources,'',1);sources=sources.replace('<p class="route-sources">','<p class="route-sources"><span class="route-source-label">Sources</span>',1)
  return step.replace('</li>',sources+'</li>',1)
 return re.sub(r'<li>.*?</li>',step_edit,route,flags=re.S)
s=re.sub(r'<details class="research-route">.*?</details>',route_edit,s,flags=re.S)
intro=re.search(r'<section id="notes">(<p class="editorial-intro">.*?</p>)',s,re.S).group(1)
s=s.replace('<section id="notes">'+intro,'<section id="notes">',1)
s=s.replace('<h2>Keep the context.</h2></div>','<h2>Keep the context.</h2>'+intro+'</div>',1)
css=re.search(r'<style>(.*?)</style>',s,re.S).group(1)
def change(a,b):
 global css
 assert a in css,a[:120]
 css=css.replace(a,b,1)
change('.editor-pick,.shortlist>div{border-top:1px solid var(--line);padding-top:16px}', '''.editor-pick{display:flex;flex-direction:column;min-width:0;padding:20px;border:1px solid var(--line);background:var(--surface)}
.pick-role{display:flex;align-items:flex-start;gap:12px;margin-bottom:18px}
.pick-num{flex:none;min-width:24px;color:var(--accent);font-size:var(--text-label);font-variant-numeric:tabular-nums}
.pick-purpose{font-size:var(--text-small);line-height:1.5;font-weight:550}
.editor-pick h3{margin:0 0 12px;line-height:1.25}
.shortlist>div{border-top:1px solid var(--line);padding-top:16px}''')
change('.source h3 a:hover{text-decoration:underline}', '.source h3 a:hover{text-decoration:underline}\n.editor-pick h3 a:hover{text-decoration:underline}\n.editor-pick:focus-within{border-color:var(--accent)}')
change('.editor-pick h3 a{text-decoration:none}', '.editor-pick h3 a{display:inline-flex;align-items:center;min-height:var(--control-height);text-decoration:none;overflow-wrap:anywhere}')
change('.editor-pick p,.shortlist p,.workflow p,.notes p,.notes li{font-size:var(--text-body)}', '.editor-pick p,.shortlist p,.notes p,.notes li{font-size:var(--text-body)}')
change('.research-route summary{display:flex;align-items:center;gap:16px;padding:20px;cursor:pointer;list-style:none}', '.research-route summary{display:grid;grid-template-columns:32px minmax(0,1fr) 24px;align-items:start;gap:12px;padding:20px;cursor:pointer;list-style:none}')
change('.route-num{font-size:12px;color:var(--accent)}', '.route-num{display:flex;align-items:center;justify-content:center;min-height:32px;border:1px solid var(--line);font-size:var(--text-label);color:var(--accent);font-variant-numeric:tabular-nums}')
change('.research-route summary strong{font-size:20px;', '.research-route summary strong{font-size:22px;')
change('.route-sub{display:block;font-size:12px;color:var(--muted);margin-top:6px}', '.route-sub{display:block;font-size:var(--text-small);line-height:1.6;color:var(--muted);margin-top:8px;max-width:52ch}\n.route-outline{display:block;font-size:var(--text-label);color:var(--muted);letter-spacing:.07em;text-transform:uppercase;margin-top:12px}')
change('.route-toggle{margin-left:auto;font-size:24px;color:var(--link)}', '.route-toggle{margin-left:auto;font-size:24px;line-height:32px;color:var(--link)}')
change('.route-body{padding:0 20px 20px;font-size:var(--text-small)}', '.route-body{padding:0 20px 20px;font-size:var(--text-body)}')
change('.route-body ol{padding-left:22px}', '.route-body ol{padding-left:28px;margin:24px 0 0;list-style:decimal-leading-zero}')
change('.route-body li{margin-bottom:20px}', '.route-body li{padding:18px 0 0 8px;margin:0 0 24px;border-top:1px solid var(--line);min-width:0}\n.route-body li::marker{font-size:var(--text-label);font-weight:550;color:var(--accent)}')
change('.route-body h4{margin:10px 0;font-size:14px}', '.route-body h4{margin:0 0 10px;font-size:var(--text-body);font-weight:550;line-height:1.4}')
change('.route-sources{line-height:1.9;color:var(--link)}', '.route-sources{font-size:var(--text-small);line-height:1.7;color:var(--link);margin:16px 0 0}\n.route-source-label{display:block;font-size:var(--text-label);color:var(--muted);letter-spacing:.07em;text-transform:uppercase}\n.route-sources a{display:inline-flex;align-items:center;min-height:var(--control-height);overflow-wrap:anywhere}')
change('.route-result{background:var(--soft);padding:18px}', '.route-result{background:var(--soft);padding:18px;border-left:2px solid var(--accent);margin:0;font-size:var(--text-small);line-height:1.7}\n.route-result strong{font-size:var(--text-label);letter-spacing:.07em;text-transform:uppercase;color:var(--link)}')
change('.workflow{display:grid;grid-template-columns:1fr;gap:16px 36px;padding-left:24px;list-style:decimal-leading-zero}', '.workflow{display:grid;grid-template-columns:minmax(0,1fr);gap:24px 40px;max-width:1080px;padding-left:28px;list-style:decimal-leading-zero}')
change('.workflow li::marker{color:var(--accent)}', '.workflow li{min-width:0;padding:18px 0 0 8px;border-top:1px solid var(--line)}\n.workflow li::marker{color:var(--accent);font-size:var(--text-small);font-weight:550}\n.workflow h3{margin:0 0 12px;max-width:44ch}\n.workflow p{font-size:var(--text-body);line-height:1.8;margin:0;max-width:56ch}')
change('.record{background:var(--soft);padding:18px;white-space:pre-wrap;overflow-wrap:anywhere;border-left:2px solid var(--accent);font-size:12px}', '.record{background:var(--soft);padding:20px;white-space:pre-wrap;overflow-wrap:anywhere;border-left:2px solid var(--accent);font-size:var(--text-small);line-height:1.8}\n.notes p{max-width:65ch;line-height:1.8}\n.notes h3{margin:24px 0 12px}\n.notes h3:first-child{margin-top:0}\n#notes .editorial-intro{max-width:68ch;color:var(--muted);font-size:var(--text-small);line-height:1.8}\n#landscape>p{max-width:68ch;line-height:1.8}')
# Remove grouped-selector repetition introduced by the more specific reading rule.
change('.editor-pick p,.shortlist p,.notes p,.notes li{', '.editor-pick p,.shortlist p,.notes li{')
change('.notes p{max-width:65ch;', '.notes p{font-size:var(--text-body);max-width:65ch;')
change('.grid,.research-routes,.notes,.workflow{grid-template-columns:repeat(2,minmax(0,1fr))}', '.grid,.research-routes,.workflow{grid-template-columns:repeat(2,minmax(0,1fr))}')
change('@media(min-width:1000px){', '@media(min-width:1000px){\n .notes{grid-template-columns:repeat(2,minmax(0,1fr));gap:40px}.editor-pick{padding:24px}')
# Keep printing compact and disclosure contents readable on paper.
change('.research-route,.editor-pick{break-inside:avoid}', '.research-route{break-inside:avoid}.editor-pick{break-inside:avoid;padding:14px}')
change('.source-details>.access,.route-body{display:block!important;content-visibility:visible!important}', '.source-details>.access{display:block!important;content-visibility:visible!important}\n.route-body{display:block!important;content-visibility:visible!important;font-size:11px}')
change('.context-link,.country-evidence{min-height:0;display:inline}', '.context-link,.country-evidence,.route-sources a,.editor-pick h3 a{min-height:0;display:inline}')
change('.source h3{font-size:18px}', '.workflow p,.notes p{font-size:11px}.route-result,.route-sources{font-size:10px}.route-outline,.route-source-label{font-size:9px}.source h3{font-size:18px}')
s=re.sub(r'<style>.*?</style>',lambda _:'<style>'+css+'</style>',s,count=1,flags=re.S)
prefix,tail=s.split('const translations=',1);dictionary,n=json.JSONDecoder().raw_decode(tail)
for full,purpose in roles:
 for locale,values in dictionary.items():
  translated=values[full];match=re.match(r'^\d+\s*/\s*(.*)$',translated);assert match,(locale,translated);values[purpose]=match.group(1)
for locale,steps,sources in [('es','3 pasos','Fuentes'),('zh-Hans','3 个步骤','来源'),('zh-Hant','3 個步驟','來源'),('ja','3 ステップ','ソース'),('ko','3단계','자료')]:dictionary[locale].update({'3 steps':steps,'Sources':sources})
s=prefix+'const translations='+json.dumps(dictionary,ensure_ascii=False)+tail[n:]
(root/'index.html').write_text(s)
assert re.findall(r'<article class="source".*?</article>',original,re.S)==re.findall(r'<article class="source".*?</article>',s,re.S)
assert re.findall(r'@font-face\{[^}]+\}',original)==re.findall(r'@font-face\{[^}]+\}',s)
print('Editorial cards, outcome-first routes, and reading layouts staged; all 52 source cards unchanged.')
