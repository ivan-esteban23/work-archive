from pathlib import Path
import re,collections
p=Path('visual-edit-public/dist/index.html');s=p.read_text();original=s

def card(m):
 c=m[0]
 header=re.search(r'<div class="brand-row">(<img[^>]+>)(<div class="card-meta">.*?</div>)</div>',c,re.S)
 category=re.search(r'<p class="category">.*?</p>',c,re.S)[0]
 title=re.search(r'<h3>.*?</h3>',c,re.S)[0]
 purpose=re.search(r'<p class="source-purpose">.*?</p>',c,re.S)[0]
 comparison=re.search(r'<dl class="comparison">.*?</dl>',c,re.S)[0]
 review=re.search(r'<p class="review-date">.*?</p>',c,re.S)[0]
 details=re.search(r'<details class="source-details">.*?</details>',c,re.S)[0]
 actions=re.search(r'<div class="source-actions".*?</div>',c,re.S)[0]
 logo=header[1]
 if 'alt=""' in logo:logo=logo.replace('class="brand-logo"','class="brand-logo brand-initials"')
 return c[:c.index('<div class="brand-row">')]+f'<div class="brand-row">{logo}{title}</div>{purpose}<div class="source-metadata">{category}{header[2]}{comparison}{review}</div>{details}{actions}</article>'
s=re.sub(r'<article class="source".*?</article>',card,s,flags=re.S)
# Screen-only card styling; keep existing print declarations.
screen,printcss=s.split('@page',1)
changes={
'--control-radius:2px;':'--control-radius:2px;--card-hover:#FCFAF5;',
'background:var(--surface);border:0;display:flex;flex-direction:column;min-width:0}':'background:var(--surface);border:0;display:flex;flex-direction:column;min-width:0;transition:background-color .18s ease,box-shadow .18s ease}',
'.source:focus-within{outline:1px solid var(--accent);outline-offset:0}':'.source:focus-within{outline:2px solid var(--focus);outline-offset:2px}',
'.brand-row{display:flex;align-items:center;gap:var(--space-2)}':'.brand-row{display:flex;align-items:center;gap:var(--space-2);margin-bottom:var(--space-2);min-height:var(--control-height)}',
'.brand-logo{width:40px;height:40px;object-fit:contain;background:#fff;border:1px solid #d5cdc0;padding:5px;border-radius:4px;flex:none}':'.brand-logo{width:2.5rem;height:2.5rem;object-fit:contain;background:#fff;border:1px solid var(--line);padding:4px;border-radius:2px;flex:none}',
'.country-label{display:grid;gap:2px;text-align:right;max-width:78%;overflow-wrap:anywhere}':'.country-label{display:flex;flex-wrap:wrap;gap:var(--space-1);text-align:left;max-width:100%;overflow-wrap:anywhere}',
'.card-meta{letter-spacing:0;color:var(--muted);display:flex;justify-content:space-between;flex:1;gap:10px;font-size:var(--text-label)}':'.card-meta{letter-spacing:0;color:var(--muted);display:flex;align-items:baseline;gap:var(--space-2);font-size:var(--text-small);margin-bottom:var(--space-2)}',
'.category{letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin:var(--space-3) 0 var(--space-1);font-size:var(--text-label)}':'.category{letter-spacing:0;text-transform:none;color:var(--muted);margin:0 0 var(--space-1);font-size:var(--text-small)}',
'.source h3{font-family:var(--sans);font-weight:550;margin:0 0 var(--space-2);font-size:var(--type-title);line-height:1.3;letter-spacing:0}':'.source h3{flex:1;min-width:0;font-family:var(--sans);font-weight:550;margin:0;font-size:var(--type-title);line-height:1.3;letter-spacing:0}',
'gap:var(--space-2);border-top:1px solid var(--line);border-bottom:0;padding:var(--space-3) 0;margin:0 0 var(--space-2)':'gap:var(--space-2);border-top:0;border-bottom:0;padding:var(--space-2) 0;margin:0 0 var(--space-2)',
'.comparison dd{margin:6px 0 0;font-size:var(--text-small);overflow-wrap:anywhere}':'.comparison dd{margin:4px 0 0;font-size:var(--text-small);color:var(--muted);overflow-wrap:anywhere}',
'.comparison div:last-child dd{display:inline-block;max-width:100%;padding:3px 8px;border:1px solid var(--line);background:var(--soft);font-weight:550;color:var(--link)}':'.comparison div:last-child dd{display:block;max-width:100%;padding:0;border:0;background:transparent;font-weight:400;color:var(--muted)}',
'.source-actions{display:flex;gap:var(--space-2);border-top:1px solid var(--line);padding-top:8px;margin-top:8px}':'.source-actions{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-2);border-top:1px solid var(--line);padding-top:var(--space-1);margin-top:var(--space-2)}',
'--on-strong:#191817}}':'--on-strong:#191817;--card-hover:#282622}}',
'@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}':'@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.source{transition:none}}',
}
for old,new in changes.items():
 assert old in screen,old
 screen=screen.replace(old,new)
i=screen.index('html:lang(zh-Hans)');screen=screen[:i]+".source-metadata{border-top:1px solid var(--line);padding-top:var(--space-3)}\n.card-meta>span:first-child{font-size:var(--text-label);font-variant-numeric:tabular-nums}\n.brand-initials{padding:0;border:0;background:var(--soft)}\n@media(hover:hover) and (pointer:fine){.source:hover{background:var(--card-hover);box-shadow:inset 0 0 0 1px var(--line)}}\n"+screen[i:]
s=screen+'@page'+printcss
assert collections.Counter(re.findall(r'href="([^"]+)"',s))==collections.Counter(re.findall(r'href="([^"]+)"',original))
assert re.findall(r'src="data:[^"]+"',s)==re.findall(r'src="data:[^"]+"',original)
p.write_text(s)
sw=Path('visual-edit-public/dist/sw.js');sw.write_text(re.sub(r"const CACHE='[^']+'","const CACHE='visual-edit-shell-source-cards-20261014-v1'",sw.read_text()))
print('All 58 cards restructured; original URLs and embedded image assets preserved.')
