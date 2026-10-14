from pathlib import Path
p=Path('visual-edit-public/dist/index.html');s=p.read_text()
css='''
/* Interaction tokens: quiet feedback without hiding content or moving controls. */
:root{--motion-fast:140ms;--motion-ease:ease-out}
button,select,summary,.hero-actions a,.jump a,.footer-nav a,#sections-menu a{transition:background-color var(--motion-fast) var(--motion-ease),border-color var(--motion-fast) var(--motion-ease),color var(--motion-fast) var(--motion-ease),box-shadow var(--motion-fast) var(--motion-ease)}
button,select,input:not([type=hidden]),summary{min-height:var(--control-height)}
button,summary{overflow-wrap:anywhere}
.source-details summary span,.route-toggle{transition:transform var(--motion-fast) var(--motion-ease)}
summary:hover{background:var(--soft)}
:where(button,a,input,select,summary):focus-visible{outline:2px solid var(--focus);outline-offset:4px}
:where(button,select,input,summary,a){scroll-margin-block:var(--search-offset,160px) 7rem}
.mobile-nav button{min-width:0;flex-wrap:wrap;gap:var(--space-1);padding:var(--space-1)}
.sections-heading,.app-heading{gap:var(--space-2);flex-wrap:wrap}
.sections-heading h2,.app-heading h2{min-width:0;flex:1 1 12rem}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
@media(forced-colors:active){:where(button,select,input,summary,a):focus-visible{outline:2px solid Highlight}.filters button.active,.mobile-nav button[aria-pressed=true],select.is-active{outline:2px solid Highlight;outline-offset:-2px}}
'''
i=s.index('@page');s=s[:i]+css+s[i:];p.write_text(s)
p=p.parent/'sw.js';s=p.read_text().replace('visual-edit-shell-editorial-20261014-v1','visual-edit-shell-accessibility-20261014-v1');p.write_text(s)
