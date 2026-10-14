from pathlib import Path
import re,json
p=Path('visual-edit-public/dist/index.html');s=p.read_text()
old="color-scheme:light dark;--page:#f4f0e8;--surface:#fcfaf6;--ink:#24211e;--muted:#625b53;\n --line:#c7beb0;--accent:#8b6b3e;--soft:#e9e1d4;--strong:#302923;--focus:#836237;--link:#735332;--on-strong:#fcfaf6;"
new="color-scheme:light dark;--page:#F7F4EE;--surface:#FFFDF9;--ink:#232323;--muted:#615B54;\n --line:#DCD5CB;--control-line:#8D8274;--accent:#80623D;--soft:#EEE9E1;--strong:#232323;--focus:#80623D;--link:#80623D;--on-strong:#FFFDF9;"
assert old in s;s=s.replace(old,new,1)
old_dark="--page:#191715;--surface:#24201d;--ink:#f2ede4;--muted:#c3b8aa;--line:#716459;--accent:#c7a873;--soft:#332d26;--strong:#d9c6a7;--focus:#d9b981;--link:#d9b981;--on-strong:#24201d"
new_dark="--page:#191817;--surface:#22211F;--ink:#F7F4EE;--muted:#C2BBB0;--line:#49443D;--control-line:#8D8274;--accent:#BFA27A;--soft:#2C2925;--strong:#F7F4EE;--focus:#BFA27A;--link:#BFA27A;--on-strong:#191817"
assert old_dark in s;s=s.replace(old_dark,new_dark,1)
# Distinguish essential control boundaries from decorative dividers.
controls="""
:where(#language,.controls input,.controls button,.collection-controls button,#reset,#show-all-saved,.filter-chip,#region,#access-filter,#country-filter,.filters button,.other-country-grid button,.asia-markets button,.sections-heading button,#copy-value){border-color:var(--control-line)}
.filters button[aria-pressed=true],.collection-controls button[aria-pressed=true]{background:var(--accent);border-color:var(--accent);color:var(--on-strong)}
"""
pos=s.index('@media(hover:hover)');s=s[:pos]+controls+s[pos:]
s=s.replace('content="#f4f0e8" media="(prefers-color-scheme: light)"','content="#F7F4EE" media="(prefers-color-scheme: light)"').replace('content="#191715" media="(prefers-color-scheme: dark)"','content="#191817" media="(prefers-color-scheme: dark)"')
p.write_text(s)
p=Path('visual-edit-public/dist/sw.js');p.write_text(re.sub(r"const CACHE='[^']+'","const CACHE='visual-edit-shell-palette-20261014-v1'",p.read_text()))
p=Path('visual-edit-public/dist/manifest.webmanifest');m=json.loads(p.read_text());m['theme_color']='#F7F4EE';m['background_color']='#F7F4EE';p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print('Light/dark palette and essential control boundaries updated.')
