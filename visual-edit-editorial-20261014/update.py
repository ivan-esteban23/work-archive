from pathlib import Path
import re,shutil
p=Path('visual-edit-public/dist/index.html');t=Path('visual-edit-editorial-20261014');(t/'backup').mkdir(exist_ok=True)
for name in ['index.html','sw.js']:shutil.copyfile(p.parent/name,t/'backup'/name)
s=p.read_text()
# Keep exact content and source order while putting the source name first in reading order.
s,n=re.subn(r'(<article class="editor-pick">)(<div class="pick-role">.*?</div>)(<h3>.*?</h3>)',r'\1\3\2',s,flags=re.S);assert n==8
css='''
/* Shared editorial surfaces and hierarchy. */
.editor-pick,.shortlist>div,.research-route{background:var(--surface);border:0;padding:var(--space-3);min-width:0}
.editor-pick,.research-route{transition:background-color .18s ease,box-shadow .18s ease}
.editor-pick:hover,.research-route:hover{background:var(--card-hover);box-shadow:inset 0 0 0 1px var(--line)}
.editor-pick:focus-within,.research-route:focus-within{outline:2px solid var(--focus);outline-offset:2px}
.editor-pick h3,.shortlist h3{font:550 var(--type-title)/1.3 var(--sans);letter-spacing:0;margin:0 0 var(--space-2)}
.editor-pick h3 a{color:var(--ink)}
.pick-role{gap:var(--space-1);margin:0 0 var(--space-2);color:var(--muted)}
.pick-purpose{font-size:var(--text-small);font-weight:400}
.pick-num{color:var(--muted);padding-top:.125rem}
.editor-pick p,.shortlist p{margin:0;line-height:1.75;max-width:56ch}
.shortlist>div{display:flex;flex-direction:column;gap:var(--space-2)}
.shortlist>div>span{font:400 var(--text-small)/1.5 var(--sans);letter-spacing:0;text-transform:none;color:var(--muted)}
.shortlist h3{margin:0}
.shortlist .browse-market{align-self:flex-start;margin-top:auto}
.research-routes{align-items:start}
.research-route summary{grid-template-columns:24px minmax(0,1fr) 24px;gap:var(--space-2);padding:0;min-height:var(--control-height)}
.route-num{border:0;justify-content:flex-start;color:var(--muted);min-height:32px}
.route-outline{font-size:var(--text-small);letter-spacing:0;text-transform:none;margin-top:var(--space-1)}
.route-sub{margin-top:var(--space-1)}
.route-body{padding:var(--space-3) 0 0}
.route-result{padding:var(--space-2);border:0;font-size:var(--text-body)}
.route-result strong{color:var(--muted);font-weight:400}
.route-body ol{margin:var(--space-3) 0 0;padding-left:var(--space-3)}
.route-body li{padding:var(--space-3) 0 0 var(--space-1);margin:0 0 var(--space-3)}
.route-body li:last-child{margin-bottom:0}
.route-body h4{margin:0 0 var(--space-1)}
.route-body p{line-height:1.75;max-width:56ch}
.route-sources{margin:var(--space-2) 0 0}
.route-sources a{font-size:var(--type-title);font-weight:550;line-height:1.4;color:var(--ink)}
.route-source-label{font-size:var(--text-small);letter-spacing:0;text-transform:none}
.workflow{margin:0;padding-left:var(--space-3)}
.workflow li{padding:var(--space-3) 0 0 var(--space-1)}
.workflow h3{margin-bottom:var(--space-2)}
.workflow p{line-height:1.75}
.notes h3{margin:0 0 var(--space-2)}
.notes p,.notes li{line-height:1.75;max-width:64ch}
.record{padding:var(--space-3);border:0;margin:var(--space-3) 0;background:var(--surface)}
.footer-brand p,.footer-context,.footer-colophon,.translation-note{font-size:var(--text-small);line-height:1.75;max-width:72ch;margin-top:var(--space-2)}
.footer-meta{font-size:var(--text-small);letter-spacing:0;line-height:1.6;gap:var(--space-2);padding-top:var(--space-3);margin-top:var(--space-4)}
.footer-nav{gap:var(--space-1) var(--space-3)}
#copy-dialog,#app-dialog,#sections-menu{box-sizing:border-box;width:min(calc(100% - 2 * var(--gutter)),36rem);max-height:85dvh;padding:var(--space-3);padding-bottom:max(var(--space-3),env(safe-area-inset-bottom));background:var(--surface);border:1px solid var(--control-line);color:var(--ink)}
#copy-dialog h2,#app-dialog h2,#sections-menu h2{font:400 var(--type-section)/1.15 var(--serif);margin:0 0 var(--space-3);overflow-wrap:anywhere}
#copy-dialog p,#app-dialog p{font-size:var(--text-body);line-height:1.75;max-width:56ch}
#sections-menu :where(a,.app-entry){font-size:var(--text-body)}
#copy-value{box-sizing:border-box;width:100%;min-width:0;min-height:var(--control-height);font:inherit;background:var(--page);color:var(--ink);border:1px solid var(--control-line);padding:var(--space-1);margin:var(--space-1) 0 var(--space-3)}
@media(min-width:640px){.editor-pick,.shortlist>div,.research-route{padding:var(--space-4)}#copy-dialog,#app-dialog,#sections-menu{padding:var(--space-4)}}
@media(prefers-reduced-motion:reduce){.editor-pick,.research-route{transition:none}}
'''
pos=s.index('@page');s=s[:pos]+css+s[pos:];p.write_text(s)
p=p.parent/'sw.js';s=p.read_text();s=re.sub(r"visual-edit-shell-navigation-20261014-v1","visual-edit-shell-editorial-20261014-v1",s);p.write_text(s)
print('Updated eight editor picks and shared editorial styles; all copy retained.')
