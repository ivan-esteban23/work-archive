from pathlib import Path
from shutil import copy2
from urllib.parse import urlencode
v=Path('/home/ivanaguilera/Documents/Obsidian Vault')
p=v/'Japan 2027 — Shops and Cafés.md'
s=p.read_text(); marker='## ⭐ What I would choose'
assert marker in s and '## 🎶 Vinyl, movies, and vintage film finds' not in s
rows=[
('Shibuya','HMV record shop Shibuya','Used vinyl and CDs, with a focus on classic recordings from the 1960s–1990s.','36-2 Udagawacho, Noa Shibuya 1F/2F; choose the record shop rather than HMV&BOOKS in MODI.','https://www.hmv.co.jp/store/SHU/'),
('Shimokitazawa','Disk Union Shimokitazawa','New and used records/CDs across genres, including rock, jazz, soul, and Japanese music.','1-40-6 Kitazawa, Kashiwa Third Building 1F; fits the vintage-clothing outing.','https://diskunion.net/shop/shimokitazawa'),
('Kichijoji','COCONUTS DISK Kichijoji','An independent used-record and CD shop for browsing across genres.','2-22-4 Kichijoji Honmachi; combine with your Kichijoji shops and coffee.','https://coconutsdisk.com/kichijoji/map/'),
('Kichijoji','Disk Union Kichijoji + Kichijoji Movie Store','New/used vinyl, CDs, DVDs and Blu-rays; dedicated movie and jazz sections within the store.','1-5-1 Kichijoji Honmachi, PARCO B1F; my most practical music-and-movies combination.','https://diskunion.net/shop/kichijyoji'),
('Shinjuku','Disk Union Shinjuku Rock Record Store','Especially 1960s–1970s rock vinyl, plus vintage music posters and memorabilia.','3-34-12 Shinjuku, Shimogiku Building 5F; stock ranges from accessible buys to collectible originals.','https://diskunion.net/shop/shinjuku_rockrecord'),
('Shinjuku','Disk Union Cinema-kan / Book Union Shinjuku','Soundtracks, film-music CDs, cinema books and magazines.','3-34-1 Shinjuku, Juraku Twin B Building 2F; its current description confirms film music/books, so prioritize Kichijoji or Ikebukuro for movie discs.','https://diskunion.net/shop/shinjuku_chukokan_bookunion'),
('Ikebukuro','Disk Union Ikebukuro','Records, vintage music/band T-shirts, and movie DVDs/Blu-rays.','Current branch: 2-27-8 Minamiikebukuro, Dai-10 Nohagi Building 9F. Official page announces its August 2026 relocation; avoid old pins.','https://diskunion.net/shop/ikebukuro'),
('Nakano','Mandarake Katsudo Shashin-kan, Nakano Broadway','Japanese movie posters, film/TV scripts, and cinema books; categories include period films, science fiction, kaiju, and tokusatsu.','Ask at Mandarake for the current Katsudo Shashin-kan location. Displayed example stock was photographed in 2016 and is not an availability promise.','https://www.mandarake.co.jp/shop/nkn/katsudo-shashin-kan.html')]
section='''## 🎶 Vinyl, movies, and vintage film finds

**Checked 6 October 2026.** These recommendations focus on physical music, movies, and memorabilia. Used stock changes constantly; a shop’s category listing does not guarantee a specific artist or film. Vintage here describes the merchandise and browsing experience; modern retail interiors may differ. Reconfirm addresses and opening days for 2027. Tax-free participation has not been verified for these additions.

| Area | Shop | What to browse | Route / location notes | Official source | Maps search |
| --- | --- | --- | --- | --- | --- |
'''
for area,name,goods,note,url in rows:
 maps='https://www.google.com/maps/search/?'+urlencode({'api':1,'query':name+' Tokyo Japan'})
 section+=f'| {area} | **{name}** | {goods} | {note} | [Official]({url}) | [Maps]({maps}) |\n'
section+='''
### ☕ A record-listening café

**RECOCO Shimokitazawa** offers a hands-on vinyl-listening café experience at **2-9-2 Kitazawa, ARISTO Shimokitazawa B1F**. It is a café stop; its site does not establish it as a used-record shop. Current rules include an entry charge plus one drink, cashless payment, no seat reservations, and a 90-minute limit when busy. Check the current menu and fees before going. Do not bring your newly purchased records in for listening: its published rules prohibit outside records.

[Official café and rules](https://recoco.cafe/) · [Maps: Shimokitazawa branch](https://www.google.com/maps/search/?api=1&query=RECOCO+Shimokitazawa+Tokyo)

### 🧭 Three optional outings

- **Music + café + thrift:** Shimokitazawa, with Disk Union and either RECOCO or the previously listed LIGHT UP COFFEE. Allow about 3–4 hours on site as a planning estimate; select a few stops.
- **Records + movies + park:** Kichijoji, choosing COCONUTS DISK and/or Disk Union alongside the existing park/coffee option. This is a half-day alternative for 30 March or 7 April, with time to pack afterwards.
- **Vintage film memorabilia:** Nakano Broadway, with Katsudo Shashin-kan as the anchor. Allow 2–3 hours on site as a planning estimate. Nakano is along the Chuo corridor like Koenji and Kichijoji, but adding all three would reduce browsing time; choose the main priority.

Shibuya, Shinjuku, and Ikebukuro shops can fit an outing already in that neighborhood. Recheck the exact entrances and floors, and use a current transit route. See [Mandarake’s current Nakano store guide](https://www.mandarake.co.jp/dir/nkn/index-en.html) for the broader complex.

### 💿 Before buying

- **Vinyl:** ask to inspect the disc and sleeve, understand the shop’s grading, and check missing inserts or an obi strip if completeness matters. Ask whether preview listening is available. Keep records supported and protected from heat or bending in luggage.
- **Movies:** check the exact edition’s region code, audio tracks, and subtitles against your player before paying. Do not assume Japanese releases have English or Spanish subtitles, or that a collector’s edition works on your home player.
- **Posters/scripts:** ask whether the item is original or a reproduction, inspect folds and wear, and request suitable protective packaging. Do not fold a poster simply to fit your suitcase.
- **Budget:** music and film souvenirs share the existing US$300 shopping/miscellaneous allowance. Pick a personal spending cap before browsing; collectible originals can be expensive.

'''
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Shops-and-Cafes-before-music.md'))
p.write_text(s.replace(marker,section+marker,1))
main=v/'Japan Travel Guide 2027.md'; m=main.read_text()
old='These remain optional outings.\n\n### 💰 Shopping allowance'
assert old in m
copy2(main,Path('/home/ivanaguilera/Work/japan-guide-update/Main-before-music.md'))
main.write_text(m.replace(old,'These remain optional outings.\n\nFor records, movie discs, vintage posters, soundtracks, and a listening café, see [[Japan 2027 — Shops and Cafés#🎶 Vinyl, movies, and vintage film finds|music and vintage film shopping]].\n\n### 💰 Shopping allowance',1))
assert all(name in p.read_text() for _,name,_,_,_ in rows)
assert '## 🎶 Vinyl, movies, and vintage film finds' in p.read_text()
print('Added eight music/film shops, a record-listening café, route suggestions, and Maps links; linked from main guide.')
