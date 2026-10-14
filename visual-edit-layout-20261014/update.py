from pathlib import Path
import re
p=Path('visual-edit-public/dist/index.html');s=p.read_text();screen,printcss=s.split('@page',1)
screen=screen.replace('--control-height:48px;','--space-1:.5rem;--space-2:1rem;--space-3:1.5rem;--space-4:2rem;--space-6:3rem;--space-8:4rem;--space-12:6rem;--content-width:90rem;--gutter:var(--space-2);--control-height:48px;',1)
# Edit existing declarations; leave compact print rules intact.
replacements={
'main{max-width:1440px;margin:auto;padding:0 20px}':'main{max-width:var(--content-width);margin:auto;padding:0 var(--gutter)}',
'margin:22px 0}':'margin:var(--space-3) 0}',
'margin:10px 0 16px}':'margin:var(--space-2) 0 var(--space-3)}',
'p{margin:0 0 14px}':'p{margin:0 0 var(--space-2)}',
'gap:12px 16px;padding:22px 0;':'gap:var(--space-2);padding:var(--space-4) 0;',
'.masthead-actions,.language-switch{display:flex;align-items:center;gap:12px;':'.masthead-actions,.language-switch{display:flex;align-items:center;gap:var(--space-2);',
'gap:22px;align-items:center;padding:30px 0':'gap:var(--space-4);align-items:center;padding:var(--space-6) 0',
'gap:8px 18px;flex-wrap:wrap;':'gap:var(--space-1) var(--space-3);flex-wrap:wrap;',
'margin-top:20px}':'margin-top:var(--space-3)}',
'.cover-image{margin:0;padding:6px;border:1px solid var(--line);background:var(--surface)}':'.cover-image{margin:0;padding:0;border:0;background:transparent}',
'.hero-actions{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin:22px 0 0;':'.hero-actions{display:flex;flex-wrap:wrap;gap:var(--space-2) var(--space-3);align-items:center;margin:var(--space-4) 0 0;',
'.jump{display:flex;gap:4px 22px;flex-wrap:wrap;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:10px 0}':'.jump{display:flex;gap:var(--space-1) var(--space-3);flex-wrap:wrap;border-top:1px solid var(--line);border-bottom:0;padding:var(--space-2) 0}',
'section{padding:40px 0;border-bottom:1px solid var(--line);':'section{padding:var(--space-8) 0;border-bottom:0;',
'.section-top{margin-bottom:24px}':'.section-top{margin-bottom:var(--space-4)}',
'.directory-tools{padding:20px;background:var(--soft);border:1px solid var(--line)}':'.directory-tools{padding:var(--space-3) 0;background:transparent;border:0;border-block:1px solid var(--line)}',
'.asia-browse{margin:24px 0;':'.asia-browse{margin:var(--space-4) 0;',
'.search-bar{position:sticky;top:0;z-index:20;background:var(--page);padding:10px 0;':'.search-bar{position:sticky;top:0;z-index:20;background:var(--page);padding:var(--space-2) 0;',
'.controls{display:flex;gap:10px;':'.controls{display:flex;gap:var(--space-1);',
'.filter-panel-body{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-top:12px}':'.filter-panel-body{display:flex;align-items:center;gap:var(--space-2);flex-wrap:wrap;padding-top:var(--space-2)}',
'gap:20px;align-items:center;justify-content:space-between;border:1px solid var(--line);border-left:2px solid var(--accent);background:var(--surface);padding:20px;margin:24px 0;':'gap:var(--space-3);align-items:center;justify-content:space-between;border:0;border-left:2px solid var(--accent);background:var(--surface);padding:var(--space-3);margin:var(--space-4) 0;',
'.comparison-key{font-size:var(--text-label);line-height:1.6;color:var(--muted);margin:18px 0 24px;':'.comparison-key{font-size:var(--text-label);line-height:1.6;color:var(--muted);margin:var(--space-3) 0 var(--space-4);',
'.grid{display:grid;grid-template-columns:minmax(0,1fr);gap:16px}':'.grid{display:grid;grid-template-columns:minmax(0,1fr);gap:var(--space-3)}',
'.source{padding:20px;background:var(--surface);border:1px solid var(--line);':'.source{padding:var(--space-3);background:var(--surface);border:0;',
'.source:focus-within{border-color:var(--accent)}':'.source:focus-within{outline:1px solid var(--accent);outline-offset:0}',
'.brand-row{display:flex;align-items:center;gap:14px}':'.brand-row{display:flex;align-items:center;gap:var(--space-2)}',
'margin:20px 0 10px;':'margin:var(--space-3) 0 var(--space-1);',
'margin:0 0 14px;font-size:var(--type-title)':'margin:0 0 var(--space-2);font-size:var(--type-title)',
'max-width:58ch;margin-bottom:18px;':'max-width:58ch;margin-bottom:var(--space-3);',
'gap:12px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:14px 0;margin:0 0 14px':'gap:var(--space-2);border-top:1px solid var(--line);border-bottom:0;padding:var(--space-3) 0;margin:0 0 var(--space-2)',
'.source-actions{display:flex;gap:14px;':'.source-actions{display:flex;gap:var(--space-2);',
'grid-template-columns:minmax(0,1fr);gap:24px}':'grid-template-columns:minmax(0,1fr);gap:var(--space-4)}',
'.editor-pick{display:flex;flex-direction:column;min-width:0;padding:20px;border:1px solid var(--line);background:var(--surface)}':'.editor-pick{display:flex;flex-direction:column;min-width:0;padding:var(--space-3) 0;border:0;border-top:1px solid var(--line);background:transparent}',
'gap:12px;margin-bottom:18px}':'gap:var(--space-2);margin-bottom:var(--space-3)}',
'.research-route{background:var(--surface);border:1px solid var(--line);min-width:0}':'.research-route{background:transparent;border:0;border-top:1px solid var(--line);min-width:0}',
'gap:12px;padding:20px;cursor:pointer;':'gap:var(--space-2);padding:var(--space-3) 0;cursor:pointer;',
'.route-body{padding:0 20px 20px;':'.route-body{padding:0 0 var(--space-3);',
'.workflow{display:grid;grid-template-columns:minmax(0,1fr);gap:24px 40px;max-width:1080px;':'.workflow{display:grid;grid-template-columns:minmax(0,1fr);gap:var(--space-4) var(--space-6);max-width:none;',
'.editorial-footer{padding:36px 0 24px}':'.editorial-footer{padding:var(--space-8) 0 var(--space-4)}',
'.footer-main{display:grid;grid-template-columns:1fr;gap:24px}':'.footer-main{display:grid;grid-template-columns:1fr;gap:var(--space-4)}',
'main{padding:0 36px}':':root{--gutter:var(--space-4)}',
'gap:40px;padding:40px 0':'gap:var(--space-6);padding:var(--space-8) 0',
'margin-left:auto;padding:8px}':'margin-left:auto;padding:0}',
'@media(min-width:1000px)':'@media(min-width:1200px)',
'.notes{grid-template-columns:repeat(2,minmax(0,1fr));gap:40px}.editor-pick{padding:24px}':'.notes{grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-8)}',
'main{padding:0 60px}.hero{padding:40px 0;':':root{--gutter:var(--space-6)}.hero{padding:var(--space-12) 0;',
'gap:64px}':'gap:var(--space-8)}',
'.grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}':'.grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--space-4)}',
'.editor-picks,.shortlist{grid-template-columns:repeat(4,minmax(0,1fr))}section{padding:48px 0}':'.editor-picks,.shortlist{grid-template-columns:repeat(3,minmax(0,1fr))}section{padding:var(--space-12) 0}.section-top{margin-bottom:var(--space-6)}',
'.source{padding:24px}.directory-tools{padding:22px 24px}.collection-controls{margin-top:var(--space-3)}':'.source{padding:var(--space-4)}.directory-tools{padding:var(--space-4) 0}.collection-controls{margin-top:var(--space-3)}',
}
for old,new in replacements.items():
 if old not in screen:print('No match:',old)
 screen=screen.replace(old,new)
# Selected occasional section rules; emphasize direct access to the directory.
i=screen.index('html:lang(zh-Hans)');screen=screen[:i]+"#directory,#notes{border-bottom:1px solid var(--line)}\n.jump a[href='#directory']{font-weight:600;color:var(--ink)}\n"+screen[i:]
p.write_text(screen+'@page'+printcss)
sw=Path('visual-edit-public/dist/sw.js');sw.write_text(re.sub(r"const CACHE='[^']+'","const CACHE='visual-edit-shell-layout-20261014-v1'",sw.read_text()))
print('Layout tokens, responsive grids, spacing and lighter section/card boundaries applied.')
