from pathlib import Path
from shutil import copy2
from urllib.parse import urlencode
v=Path('/home/ivanaguilera/Documents/Obsidian Vault')
def link(label,query):
 return '['+label+'](https://www.google.com/maps/search/?'+urlencode({'api':1,'query':query})+')'
p=v/'Japan 2027 — Shops and Cafés.md';s=p.read_text()
marker='## 🎶 Vinyl, movies, and vintage film finds'
assert marker in s and '## 📍 Additional Maps links' not in s
section='## 📍 Additional Maps links for the neighborhood shortlist\n\nThese provide individual search links for the other named stops. Check the result and entrance; these are not independently verified Google place pins.\n\n| Area | Individual destinations |\n| --- | --- |\n'
safari=' · '.join(link('SAFARI '+x,'SAFARI '+x+' Koenji Tokyo') for x in ['1号店','2号店','3号店','4号店','5号店','1PLUS'])
rows=[('Koenji',safari),('Kichijoji',link('SAFARI Nanaibashi','SAFARI なない橋店 吉祥寺')+' · '+link('SAFARI Nakamichi-dori','SAFARI 中道通り店 吉祥寺')+' · '+link('Inokashira Park','Inokashira Park Tokyo Japan')),('Shimokitazawa',link('Reload','reload Shimokitazawa Tokyo')+' · '+link('2nd STREET','2nd STREET Shimokitazawa 2-30-13 Kitazawa Tokyo')),('Daikanyama',link('IVY PLACE','IVY PLACE Daikanyama Tokyo')+' · '+link('TSUTAYA BOOKS','Daikanyama Tsutaya Books Tokyo')),('Nakameguro',link('Meguro River','Meguro River Nakameguro Tokyo'))]
for area,links in rows:section+='| '+area+' | '+links+' |\n'
section+='\n'
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Shops-before-maps-complete.md'))
p.write_text(s.replace(marker,section+marker,1))
main=v/'Japan Travel Guide 2027.md';m=main.read_text()
old='[City listing](https://www.city.kamakura.kanagawa.jp/shoukou/omise2006/data/0219.html)'
assert old in m
copy2(main,Path('/home/ivanaguilera/Work/japan-guide-update/Main-before-maps-complete.md'))
m=m.replace(old,old+' · '+link('Maps: Kimamaya (confirm before visiting)','Kimamaya 3-8-11 Hase Kamakura'),1)
old2='[Official directory](https://ikebukuro.parco.jp/taxfree/)'
assert old2 in m
m=m.replace(old2,old2+' · '+link('Maps: Onitsuka Tiger','Onitsuka Tiger Ikebukuro PARCO')+' · '+link('Maps: POP MART','POP MART Ikebukuro PARCO')+' · '+link('Maps: EVANGELION STORE','EVANGELION STORE TOKYO-01 Ikebukuro PARCO'),1)
main.write_text(m)
assert 'Maps: IVY' not in '' # completed write verified below
print('Filled missing Maps links for thrift branches, café, parks, Reload, and additional tax-free leads.')
