from pathlib import Path
import re, hashlib, json
root=Path('/home/ivanaguilera/Work')
source=root/'visual-edit-public/dist/index.html'
s=source.read_text()
original_css=re.search(r'<style>(.*?)</style>',s,re.S).group(1)
fonts='\n'.join(re.findall(r'@font-face\{[^}]+\}',original_css))
css='''
:root{
 color-scheme:light dark;--page:#f4f0e8;--surface:#fcfaf6;--ink:#24211e;--muted:#625b53;
 --line:#c7beb0;--accent:#8b6b3e;--soft:#e9e1d4;--strong:#302923;--focus:#836237;--link:#735332;--on-strong:#fcfaf6;
 --serif:'Instrument Serif',Georgia,serif;--sans:'Source Sans 3',Arial,sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:24px;text-size-adjust:100%}
body{margin:0;background:var(--page);color:var(--ink);font:15px/1.65 var(--sans)}
a{color:inherit;text-underline-offset:4px}
button,input,select{font:inherit;color:inherit}
button,summary,select{touch-action:manipulation}
button{cursor:pointer}
:focus-visible{outline:2px solid var(--focus);outline-offset:4px}
[hidden]{display:none!important}
main{max-width:1440px;margin:auto;padding:0 24px}
h1,h2{font-family:var(--serif);font-weight:400}
h1{font-size:clamp(64px,7.3vw,106px);line-height:.98;letter-spacing:-.03em;margin:22px 0}
h2{font-size:clamp(32px,3.4vw,46px);line-height:1.12;margin:10px 0 16px}
h3{font-size:22px;line-height:1.25;font-weight:550;margin:12px 0}
p{margin:0 0 14px}
.eyebrow,.category,.card-meta,.section-top>span{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.masthead{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:22px 0;border-bottom:1px solid var(--line)}
.masthead>span,.footer-wordmark{font:26px/1.1 var(--serif);letter-spacing:.06em}
.masthead-actions,.language-switch{display:flex;align-items:center;gap:12px;min-width:0}
#language{background:transparent;border:1px solid var(--line);padding:8px;min-height:44px;max-width:132px;font-size:14px}
.hero{position:relative;display:grid;grid-template-columns:minmax(0,1fr);gap:22px;align-items:center;padding:30px 0}
.cover-visual{position:absolute;top:70px;right:0;width:88px}
.hero h1{max-width:calc(100% - 96px);font-size:60px}
.hero>*{min-width:0}
.cover-copy>.eyebrow{font-size:10px}
.cover-line{font:23px/1.3 var(--serif);margin-bottom:16px}
.hero-actions a{white-space:nowrap}
.hero .cover-copy>p:not(.cover-line){max-width:54ch;color:var(--muted);font-size:14px}
.hero .editorial-intro{font-size:12px!important;line-height:1.65}
.cover-kicker{display:flex;gap:8px 18px;flex-wrap:wrap;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-top:20px}
.cover-image{margin:0;padding:6px;border:1px solid var(--line);background:var(--surface)}
.cover-image img{display:block;width:100%;height:auto}
.cover-image figcaption{font-size:9px;color:var(--muted);line-height:1.4;padding-top:8px}
.cover-study{display:none}
.hero-actions{display:flex;gap:20px;align-items:center;margin:22px 0 0;font-size:14px}
.hero-actions a:first-child{background:var(--strong);color:var(--on-strong);padding:12px 18px;text-decoration:none}
.jump{display:flex;gap:4px 22px;flex-wrap:wrap;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:10px 0}
.jump a{font-size:12px;min-height:36px;display:flex;align-items:center;text-decoration:none}
.jump a:hover{text-decoration:underline}
section{padding:40px 0;border-bottom:1px solid var(--line);scroll-margin-top:24px}
.section-top{margin-bottom:24px}
.section-top>p{color:var(--muted);font-size:14px;max-width:70ch}
.directory-tools{padding:20px;background:var(--soft);border:1px solid var(--line)}
.controls{display:flex;gap:10px;margin-bottom:14px}
.controls input{width:100%;min-width:0;flex:1;background:var(--surface);border:1px solid var(--line);font-size:16px;padding:12px}
.controls input::placeholder{color:var(--muted)}
.controls button,.collection-controls button{background:var(--surface);border:1px solid var(--line);padding:10px 12px;min-height:44px;font-size:12px}
.filter-panel{margin:0}
.filter-panel>summary{display:flex;align-items:center;gap:12px;min-height:44px;cursor:pointer;list-style:none;font-size:13px}
summary::-webkit-details-marker{display:none}
#active-filters{font-size:12px;color:var(--muted)}
.panel-symbol{margin-left:auto;font-size:21px}
.filter-panel[open] .panel-symbol{transform:rotate(45deg)}
.filter-panel-body{padding-top:12px}
.region-label{font-size:12px;margin-right:10px}
#region{padding:8px 12px;background:var(--surface);border:1px solid var(--line);min-height:44px;max-width:100%;font-size:16px}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.filters button{background:transparent;border:1px solid var(--line);padding:8px 12px;min-height:44px;font-size:12px;border-radius:2px;text-align:left}
.filters button[aria-pressed=true],.collection-controls button[aria-pressed=true]{background:var(--strong);color:var(--on-strong);border-color:var(--strong)}
.filter-count{margin-left:6px;opacity:.75;font-variant-numeric:tabular-nums}
.collection-controls{display:flex;align-items:center;gap:10px;flex-wrap:wrap;border-top:1px solid var(--line);margin-top:16px;padding-top:16px}
.collection-controls button:disabled{opacity:.5;cursor:default}
#favorites-count{margin-left:8px}
.collection-note,#storage-warning{font-size:11px;line-height:1.5;color:var(--muted);flex-basis:100%;margin:0}
.directory-status{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:14px}
.count{font-size:12px;color:var(--muted);margin:0}
#share-view{border:0;background:transparent;color:var(--link);padding:8px 0;font-size:12px;min-height:44px}
.comparison-key{font-size:11px;line-height:1.6;color:var(--muted);margin:18px 0 24px;max-width:110ch}
.grid{display:grid;grid-template-columns:minmax(0,1fr);gap:16px}
.source{padding:22px;background:var(--surface);border:1px solid var(--line);display:flex;flex-direction:column;min-width:0}
.brand-row{display:flex;align-items:center;gap:14px}
.brand-logo{width:38px;height:38px;object-fit:contain;background:#fff;border:1px solid #d5cdc0;padding:5px;border-radius:4px;flex:none}
.card-meta{display:flex;justify-content:space-between;flex:1;gap:10px;font-size:10px}
.category{margin:20px 0 10px;font-size:10px}
.source h3{margin:0 0 14px}
.source h3 a{display:flex;align-items:center;justify-content:space-between;gap:14px;text-decoration:none;overflow-wrap:anywhere;min-height:30px}
.source h3 a:hover{text-decoration:underline}
.source h3 a>span{font-size:17px;color:var(--link);flex:none}
.source-purpose{font-size:14px;line-height:1.65;margin-bottom:18px;overflow-wrap:anywhere}
.comparison{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:14px 0;margin:0 0 14px}
.comparison div{min-width:0}
.comparison dt{font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.comparison dd{margin:6px 0 0;font-size:12px;overflow-wrap:anywhere}
.comparison div:last-child dd{font-weight:550;color:var(--link)}
.review-date{font-size:11px;color:var(--muted);margin:0 0 10px}
.source-details{margin-top:auto}
.source-details summary{display:flex;justify-content:space-between;align-items:center;min-height:44px;font-size:12px;color:var(--link);cursor:pointer;list-style:none}
.source-details summary span{font-size:21px}
.source-details[open] summary span{transform:rotate(45deg)}
.access{font-size:12px;color:var(--muted);padding:10px 0;border-top:1px solid var(--line)}
.access strong{font-size:10px;letter-spacing:.07em;text-transform:uppercase}
.access p{margin:8px 0}
.context-link{display:inline-flex;align-items:center;min-height:36px}
.favorite-source,.copy-source{display:flex;align-items:center;gap:9px;min-height:44px;background:transparent;border:0;color:var(--link);font-size:12px;padding:8px 0;text-align:left}
.favorite-source>span:first-child{font-size:20px}
.favorite-source[aria-pressed=true]{font-weight:600}
.copy-source{margin-top:2px;border-top:1px solid var(--line)}
.editor-picks,.shortlist,.research-routes,.notes{display:grid;grid-template-columns:minmax(0,1fr);gap:24px}
.editor-pick,.shortlist>div{border-top:1px solid var(--line);padding-top:16px}
.editor-pick h3 a{text-decoration:none}
.editor-pick p,.shortlist p,.workflow p,.notes p,.notes li{font-size:14px}
.shortlist span{font-size:12px;color:var(--muted)}
.research-route{background:var(--surface);border:1px solid var(--line);min-width:0}
.research-route summary{display:flex;align-items:center;gap:14px;padding:18px;cursor:pointer;list-style:none}
.route-num{font-size:12px;color:var(--accent)}
.research-route summary strong{font-size:20px;line-height:1.25;font-weight:550}
.route-sub{display:block;font-size:12px;color:var(--muted);margin-top:6px}
.route-toggle{margin-left:auto;font-size:24px;color:var(--link)}
.research-route[open] .route-toggle{transform:rotate(45deg)}
.route-body{padding:0 18px 18px;font-size:13px}
.route-body ol{padding-left:22px}
.route-body li{margin-bottom:20px}
.route-body h4{margin:10px 0;font-size:14px}
.route-sources{line-height:1.9;color:var(--link)}
.route-result,.record{background:var(--soft);padding:18px}
.workflow{display:grid;grid-template-columns:1fr;gap:16px 36px;padding-left:24px;list-style:decimal-leading-zero}
.workflow li::marker{color:var(--accent)}
.record{white-space:pre-wrap;overflow-wrap:anywhere;border-left:2px solid var(--accent);font-size:12px}
.editorial-footer{padding:36px 0 24px}
.footer-main{display:grid;grid-template-columns:1fr;gap:24px}
.footer-brand p{font-size:14px;color:var(--muted);margin-top:12px}
.footer-nav{display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}
.footer-nav a,.print-guide{min-height:44px;display:flex;align-items:center;font-size:12px;text-decoration:none}
.print-guide{background:transparent;color:var(--link);border:0;padding:0;text-align:left}
.footer-meta{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;border-top:1px solid var(--line);padding-top:20px;margin-top:24px;font-size:10px;letter-spacing:.07em;color:var(--muted)}
.footer-context,.footer-colophon,.translation-note{font-size:11px;color:var(--muted);max-width:100ch;margin:14px 0 0}
.skip-link{position:fixed;top:10px;left:10px;transform:translateY(-180%);z-index:100;background:var(--strong);color:var(--on-strong);padding:12px}
.skip-link:focus{transform:none}
.copy-status{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--strong);color:var(--on-strong);padding:10px 18px;z-index:100;font-size:13px}
.copy-status:empty{display:none}
#copy-dialog{width:min(90vw,520px);background:var(--surface);color:var(--ink);border:1px solid var(--line);padding:24px}
#copy-dialog::backdrop{background:#0008}
#copy-value{width:100%;min-width:0;padding:12px;border:1px solid var(--line);background:var(--page);font-size:16px;margin:10px 0}
#copy-dialog button{background:var(--strong);color:var(--on-strong);border:0;min-height:44px;padding:10px 18px}
html:lang(zh-Hans) h1,html:lang(zh-Hant) h1,html:lang(ja) h1,html:lang(ko) h1{font-family:'Noto Serif CJK SC','Noto Serif CJK TC','Noto Serif JP','Noto Serif KR','Songti SC','Yu Mincho','Batang',serif;font-size:clamp(38px,5vw,64px);line-height:1.2;letter-spacing:0}
html:lang(zh-Hans) h2,html:lang(zh-Hant) h2,html:lang(ja) h2,html:lang(ko) h2,html:lang(zh-Hans) .cover-line,html:lang(zh-Hant) .cover-line,html:lang(ja) .cover-line,html:lang(ko) .cover-line{font-family:'Noto Serif CJK SC','Noto Serif CJK TC','Noto Serif JP','Noto Serif KR','Songti SC','Yu Mincho','Batang',serif;line-height:1.4}
@media(min-width:640px){
 main{padding:0 36px}.cover-visual{position:static;width:auto}.hero h1{max-width:none;font-size:clamp(64px,7.3vw,106px)}.hero{grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:40px;padding:40px 0}
 .hero .cover-copy>p:not(.cover-line){font-size:15px}.cover-image{max-width:280px;margin-left:auto;padding:8px}.cover-image figcaption{font-size:10px}
 .grid,.research-routes,.notes,.workflow{grid-template-columns:repeat(2,minmax(0,1fr))}
 .editor-picks,.shortlist{grid-template-columns:repeat(2,minmax(0,1fr))}
 .filter-panel>summary{display:none}.filter-panel-body{padding-top:0}.collection-note{flex:1;max-width:62ch;margin-left:auto}
 .source-purpose{flex:1}.footer-main{grid-template-columns:1fr 1fr}
}
@media(min-width:1000px){
 main{padding:0 60px}.hero{padding:40px 0;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:64px}
 .cover-image{max-width:340px}.cover-line{font-size:28px}.cover-copy>.eyebrow{font-size:11px}
 .hero .editorial-intro{max-width:65ch}.grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
 .editor-picks,.shortlist{grid-template-columns:repeat(4,minmax(0,1fr))}section{padding:48px 0}
 .source{padding:24px}.directory-tools{padding:22px 24px}.collection-controls{margin-top:20px}
}
@media(prefers-color-scheme:dark){:root{--page:#191715;--surface:#24201d;--ink:#f2ede4;--muted:#c3b8aa;--line:#716459;--accent:#c7a873;--soft:#332d26;--strong:#d9c6a7;--focus:#d9b981;--link:#d9b981;--on-strong:#24201d}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@page{size:A4;margin:14mm}
@media print{
 :root{color-scheme:light;--page:#fff;--surface:#fff;--ink:#20251e;--muted:#4c5849;--line:#b9beaf;--accent:#89412a;--soft:#f0f2ec;--strong:#283b30;--focus:#536747;--link:#3f5847;--on-strong:#fff}
 body{font-size:11px}main{max-width:none;padding:0}.skip-link,.jump,.directory-tools,.hero-actions,.favorite-source,.copy-source,.print-guide,.language-switch,.copy-status,#copy-dialog,#empty,.footer-nav{display:none!important}
 .hero{grid-template-columns:1.5fr 1fr;padding:20px 0;gap:24px}.cover-image{max-width:160px;margin-left:auto}
 .grid,.editor-picks,.shortlist,.workflow{grid-template-columns:1fr 1fr;gap:12px}.source{padding:14px;break-inside:avoid;display:flex!important}
 .source-details summary,.route-toggle{display:none}.source-details>.access,.route-body{display:block!important;content-visibility:visible!important}
 .source h3{font-size:18px}.source-purpose,.comparison dd,.access{font-size:10px}.comparison{gap:6px}.review-date{font-size:9px}
 section{padding:22px 0}.research-route,.editor-pick{break-inside:avoid}.notes,.research-routes{grid-template-columns:1fr}
}
'''
s=re.sub(r'<style>.*?</style>',lambda _: '<style>'+fonts+'\n'+css+'</style>',s,count=1,flags=re.S)
# Move the complete, unchanged directory ahead of the supporting reading sections.
directory=re.search(r'<section id="directory">.*?</section>',s,re.S).group(0)
s=s.replace(directory,'',1).replace('<section id="editors">',directory+'<section id="editors">',1)
# Keep the editorial explanation with the access and context notes.
intro=re.search(r'<p class="editorial-intro">.*?</p>',s,re.S).group(0)
s=s.replace(intro,'',1)
s=s.replace('<section id="notes">','<section id="notes">'+intro,1)
# Surface the existing review-date text without altering it.
def move_review(m):
 card=m.group(0);review=re.search(r'<p class="review-date">.*?</p>',card,re.S).group(0)
 return card.replace(review,'',1).replace('<details class="source-details">',review+'<details class="source-details">',1)
s=re.sub(r'<article class="source".*?</article>',move_review,s,flags=re.S)
s=s.replace('<div class="cover-kicker">','<div class="hero-actions"><a href="#directory">Source directory ↗</a><a href="#shortlist">Asia shortlist ↗</a></div><div class="cover-kicker">',1)
s=s.replace("phone=matchMedia('(max-width:650px)')","phone=matchMedia('(max-width:639px)')")
(root/'visual-edit-design-preview-20261013/index.html').write_text(s)
(root/'visual-edit-design-preview-20261013/source-state.json').write_text(json.dumps({'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'preview_only':True},indent=2))
print('Preview created:',root/'visual-edit-design-preview-20261013/index.html')
print('Cards',s.count('<article class="source"'),'size',len(s.encode()))
