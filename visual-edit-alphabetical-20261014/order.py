from pathlib import Path
import re,html,unicodedata,collections
p=Path('visual-edit-public/dist/index.html');s=p.read_text();original=s

def text(v):return html.unescape(re.sub('<[^>]+>','',v)).replace('↗','').strip()
def key(v):return unicodedata.normalize('NFKD',text(v)).casefold()
def reorder(pattern,sortkey,renumber=None):
 global s
 blocks=re.findall(pattern,s,re.S)
 ordered=sorted(blocks,key=sortkey)
 if renumber:
  ordered=[re.sub(renumber,lambda m:m[1]+f'{i:02}'+m[2],b,count=1) for i,b in enumerate(ordered,1)]
 it=iter(ordered);s=re.sub(pattern,lambda _:next(it),s,flags=re.S)
reorder(r'<article class="source".*?</article>',lambda c:key(re.search(r'<h3>.*?</h3>',c,re.S)[0]),r'(<div class="card-meta"><span>)\d+(</span>)')
reorder(r'<article class="editor-pick".*?</article>',lambda c:key(re.search(r'<h3>.*?</h3>',c,re.S)[0]),r'(<span class="pick-num">)\d+(</span>)')
reorder(r'<details class="research-route">.*?</details>',lambda c:key(re.search(r'<strong>.*?</strong>',c,re.S)[0]),r'(<span class="route-num">)\d+(</span>)')
# Each route's list of source links is also alphabetical.
def route_links(m):
 block=m[0]; links=re.findall(r'<a\b.*?</a>',block,re.S);it=iter(sorted(links,key=key));return re.sub(r'<a\b.*?</a>',lambda _:next(it),block,flags=re.S)
s=re.sub(r'<p class="route-sources">.*?</p>',route_links,s,flags=re.S)
reorder(r'<button[^>]*data-filter[^>]*>.*?</button>',lambda c:(0 if 'data-filter="All"' in c else 1,key(re.search(r'data-filter="([^"]+)"',c)[1])))
# Keep All first; sort choices inside existing groups (preserving country group headings).
def select(m):
 c=m[0]
 if 'id="language"' in c:return c
 def group(g):
  opts=re.findall(r'<option\b.*?</option>',g,re.S);it=iter(sorted(opts,key=lambda o:(0 if text(o)=='All' else 1,key(o))));return re.sub(r'<option\b.*?</option>',lambda _:next(it),g,flags=re.S)
 parts=re.split(r'(<optgroup\b.*?</optgroup>)',c,flags=re.S)
 return ''.join(group(x) for x in parts)
s=re.sub(r'<select\b.*?</select>',select,s,flags=re.S)
# Sort section links in desktop, footer, and mobile menus; retain utility buttons.
def nav(m):
 c=m[0]
 if 'aria-label="Sections"' not in c and 'aria-label="Footer navigation"' not in c:return c
 links=re.findall(r'<a\b.*?</a>',c,re.S);it=iter(sorted(links,key=key));return re.sub(r'<a\b.*?</a>',lambda _:next(it),c,flags=re.S)
s=re.sub(r'<nav\b.*?</nav>',nav,s,flags=re.S)
# Alphabetize the independent reading-practice topics, retaining sequential workflow instructions.
m=re.search(r'(<section id="landscape">.*?<ol class="workflow">)(.*?)(</ol>)',s,re.S)
items=re.findall(r'<li>.*?</li>',m[2],re.S);ordered=''.join(sorted(items,key=lambda c:key(re.search(r'<h3>.*?</h3>',c,re.S)[0])))
s=s[:m.start(2)]+ordered+s[m.end(2):]
p.write_text(s)
sw=Path('visual-edit-public/dist/sw.js');sw.write_text(re.sub(r"const CACHE='[^']+'","const CACHE='visual-edit-shell-alphabetical-20261014-v1'",sw.read_text()))
# Content/link preservation, except visible list numbers.
assert collections.Counter(re.findall(r'href="([^"]+)"',s))==collections.Counter(re.findall(r'href="([^"]+)"',original))
assert len(re.findall(r'<article class="source"',s))==58
print('Alphabetized 58 source cards, editor picks, routes, route links, category/coverage/access filters, navigation, and reading topics. All URLs preserved.')
