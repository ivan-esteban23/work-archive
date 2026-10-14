from pathlib import Path
from shutil import copy2
from urllib.parse import urlencode
p=Path('/home/ivanaguilera/Documents/Obsidian Vault/Japan Travel Guide 2027.md')
s=p.read_text()
marker='### 💰 Shopping allowance'
assert marker in s and '### 🗺️ Tax-free options by Tokyo area' not in s
rows=[
('Shinjuku','Isetan Shinjuku','Department-store fashion and gifts','Main building currently lists a 6F tax-free counter; ask about eligible purchases and fees.','https://www.mistore.jp/store/shinjuku/service.html'),
('Shinjuku','BOOKOFF PLUS Shinjuku-eki Nishi-guchi','Secondhand fashion, books, music, toys and cards','Exact branch confirms tax-free service; 4F–6F, 1-10-2 Nishishinjuku.','https://www.bookoff.co.jp/inbound/shop20472.html'),
('Shibuya','Shibuya Loft','Stationery, notebooks and small design gifts','Official directory lists tax-free procedures for this branch; 21-1 Udagawacho.','https://www.loft.co.jp/shop_list/?trflg=1'),
('Shibuya','MEGA Don Quijote Shibuya Honten','Packaged snacks, matcha sweets and practical souvenirs','GO TOKYO confirms tax-free shopping for this exact store.','https://www.gotokyo.org/en/spot/1879/index.html'),
('Akihabara','BIC CAMERA AKIBA','Compare electronics and camera accessories','Local shopping district cooperative lists the branch as tax-free; 4-1-1 Soto-Kanda.','https://e-akihabara.jp/e/dutyfree/'),
('Akihabara','BOOKOFF Akihabara Eki-mae','Books, music, trading cards and secondhand electronics','Exact branch confirms tax-free service; 1-6-4 Kanda Sakumacho.','https://www.bookoff.co.jp/inbound/shop20396.html'),
('Ikebukuro','BOOKOFF Ikebukuro Sunshine 60-dori','Books, music, trading cards and toys','Exact branch confirms tax-free service; 1-22-10 Higashiikebukuro.','https://www.bookoff.co.jp/inbound/shop20422.html'),
('Ikebukuro','CAPCOM STORE IKEBUKURO at Ikebukuro PARCO','Character merchandise','PARCO tax-free directory lists this B2F shop. Procedures are per shop, with no shared tax-free counter.','https://ikebukuro.parco.jp/taxfree/'),
('Kamakura (Kanagawa)','BOOKOFF Kamakura Tehiro','Books, music, trading cards and toys','Exact branch confirms tax-free service; 6-2-14 Tehiro. Separate stop from central Kamakura sightseeing.','https://www.bookoff.co.jp/inbound/shop10731.html')]
section='''### 🗺️ Tax-free options by Tokyo area — and Kamakura

**Checked 6 October 2026.** Optional choices for areas you may visit; these do not add fixed itinerary stops. Kamakura is in Kanagawa, outside Tokyo. Current participation is confirmed by the retailer, mall, or official local tourism/shopping organization; recheck for March–April 2027 and use [[#🧾 Tax-free shopping for the 2027 trip|the 2027 refund guidance]].

| Area | Shop | Choose it for | Confirmation / location | Maps search |
| --- | --- | --- | --- | --- |
'''
for area,name,goods,note,url in rows:
 maps='https://www.google.com/maps/search/?'+urlencode({'api':1,'query':name+' Japan'})
 section+=f'| {area} | **{name}** | {goods} | {note} [Source]({url}) | [Maps]({maps}) |\n'
section+='''
**Best fit for your interests:** Shibuya Loft for stationery and gifts; BOOKOFF PLUS in Shinjuku for secondhand fashion; Don Quijote for packaged souvenirs. Akihabara electronics purchases need a model-by-model comparison of price, language settings, voltage, and warranty coverage in Chile.

**Ikebukuro alternatives:** PARCO’s official tax-free list also includes Onitsuka Tiger, POP MART, and EVANGELION STORE TOKYO-01. Check each tenant’s own procedure and current floor before visiting; tax-free participation does not apply automatically to every shop in the mall. [Official directory](https://ikebukuro.parco.jp/taxfree/)

**Kamakura sightseeing lead, confirmation pending:** the city’s official Kimamaya listing at 3-8-11 Hase displays a Japan Tax-free Shop image and describes gifts/vintage items. It provides no current hours or detailed tax-free procedure, so call +81 467-24-4578 before treating it as a shopping stop. Café purchases do not qualify as exported goods. [City listing](https://www.city.kamakura.kanagawa.jp/shoukou/omise2006/data/0219.html)

Bring your passport, ask which items qualify and how the 2027 refund is processed, and check counter hours separately from store hours. Maps links are searches; verify the exact branch. Keep the existing shopping budget and pick a shop that fits a planned outing.

'''
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Main-before-area-shops.md'))
p.write_text(s.replace(marker,section+marker,1))
assert all(name in p.read_text() for _,name,_,_,_ in rows)
print('Added nine confirmed area-specific options and one qualified Kamakura lead.')
