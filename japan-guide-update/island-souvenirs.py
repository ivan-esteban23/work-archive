from pathlib import Path
import hashlib,json,shutil,sys
V=Path('/home/ivanaguilera/Documents/Obsidian Vault')
W=Path('/home/ivanaguilera/Work/japan-guide-update/island-souvenirs')
NAME='Japan 2027 — Best Islands.md'
BLOCK='''## Souvenirs — small keepsakes and gifts

**Checked:** 7 October 2026. My best matches are **an art keepsake for you from Naoshima**, **a minsa textile accessory for her from Ishigaki/Taketomi**, and **a small momiji-manju box from Miyajima**. Choose souvenirs from the islands you actually visit; this is an alternative shortlist, not a basket to buy in full. Specific variants, prices, stock, and 2027 opening times are unconfirmed.

| Island | What I would browse | Why it fits / what to check | Official source |
| --- | --- | --- | --- |
| **Miyajima** | Small **shakushi rice scoop**, **momiji manju** | A compact traditional keepsake for your kitchen, or sweets for her. Check whether the scoop is intended for cooking or decoration; check the cakes' expiry/storage instructions. | [Local souvenir guide](https://www.miyajima.or.jp/english/souvenir/souvenir.html) |
| **Naoshima** | Small art goods or a slim art book | Fits your photography/art interests. Pick from the actual museum-shop selection; postcard/stationery formats are worth asking for but their stock is not verified. The separate Benesse House Shop welcomes non-guests. | [Benesse shops](https://benesse-artsite.jp/en/stay/benessehouse/shop.html) |
| **Shodoshima** | **Mini olive hand cream**, small olive skincare product, dried somen | Beauty gift or a cooking souvenir. The Olive Park catalog lists a mini hand cream; check ingredients, fragrance, actual price, and current stock before choosing. | [Olive Park cosmetics catalog](https://story.olive-pk.jp/ja/category/gr13/) · [Local food products](https://www.kagawa-culture-compass.net/en/spot/052.html) |
| **Yakushima** | Small **yakusugi craft** or packaged island tea | Ask to see a compact wood item, or choose tea for easier packing. Check material/maker and item-care instructions rather than assume every wood souvenir is locally made. | [Yakushima Town souvenirs](https://www.town.yakushima.kagoshima.jp/kanko/English/3/2473.html) |
| **Ishigaki** | **Minsa woven accessory**, optional small **Ishigaki-yaki pottery** | Textile accessories fit her fashion interests without needing a garment size. The blue-glazed pottery is a separate fragile keepsake option; inspect packing and the price. | [Official crafts guide](https://visitokinawajapan.com/travel-inspiration/ishigaki-traditions-inspired-by-the-sea/) |
| **Taketomi** | Minsa textile accessory if locally available | Browse the village craft offerings; confirm maker/origin. You can also compare at Ishigaki's Minsah Kogei Kan, so the same gift need not be purchased twice. | [Regional minsa craft information](https://visitokinawajapan.com/travel-inspiration/ishigaki-traditions-inspired-by-the-sea/) |
| **Miyako** | Small locally made woven/craft item, or packaged brown sugar | Compare a craft workshop/shop with a simple food gift. A finished handmade item requires confirming pickup time; do not assume pottery can be fired and collected immediately. | [Official craft and brown-sugar ideas](https://visitokinawajapan.com/plan-your-trip/recommended-trips/three-days-miyako-island/) |
| **Enoshima** | **Shirasu rice crackers**, packaged traditional sweets | A food gift lead from the local cuisine list; choose an actual sealed product with a suitable expiry date. | [Official local specialties](https://discover-fujisawa.jp/en/sightseeing/cuisine/) |
| **Sado** | Small packaged local-rice product; optional local sake | Ask what is available at your actual stop. Sado is known for its rice and sake; a small food format suits luggage better than a large bag or bottle. No specific retail item is confirmed. | [JNTO Sado guide](https://www.japan.travel/en/destinations/hokuriku-shinetsu/niigata/sado-island/) |

### Shopping locations — Google Maps

These are location searches for browsing leads, not confirmation that a particular item is available.

- **Miyajima rice-scoop browsing:** [Shakushi-no-ji Miyazato — Google Maps](https://www.google.com/maps/search/?api=1&query=Shakushi+no+Ji+Miyazato+Miyajima+Hiroshima). The tourism association identifies it as a rice-scoop specialty shop in its [shopping map](https://www.miyajima.or.jp/english/map/img/map_omotesando.pdf).
- **Naoshima art gifts:** [Benesse House Shop — Google Maps](https://www.google.com/maps/search/?api=1&query=Benesse+House+Shop+Naoshima). The shop adjacent to the Park and the Museum Shop inside the museum are separate locations; check access to the one you want.
- **Shodoshima beauty/food gifts:** [Olive Park — Google Maps](https://www.google.com/maps/search/?api=1&query=Shodoshima+Olive+Park+Kagawa).
- **Ishigaki textiles:** [Minsah Kogei Kan — Google Maps](https://www.google.com/maps/search/?api=1&query=Minsah+Kogei+Kan+Ishigaki+Okinawa).
- **Ishigaki pottery:** [Ishigaki-yaki Pottery Studio — Google Maps](https://www.google.com/maps/search/?api=1&query=Ishigaki+yaki+Pottery+Studio+Okinawa).
- **Miyako craft browsing:** [Miyakojima Traditional Crafts Village — Google Maps](https://www.google.com/maps/search/?api=1&query=Miyakojima+Traditional+Crafts+Village+Okinawa).

### Your spending and packing plan

My suggested **island souvenir target is up to US$30–50**, carved out of the existing shopping allowance. This is a planning limit, not a claim that any specific craft costs that amount. Choose one keeper and one small gift; compare actual prices before deciding.

Her souvenir, beauty product, or sweets share the existing **US$200 gift cap**. If that cap stays inside your US$300 shopping allowance, only US$100 remains for all your other purchases, including Tamiya and clothing. An island accessory replaces another planned fashion gift; olive cream replaces another beauty gift. The earlier decision about whether her gift cap is inside the main allowance remains open.

For food, check the label, storage needs, expiry against your return date, and applicable import requirements. For ceramics, ask for protective packaging. Liquid beauty products and bottles need packing according to the actual airline/airport rules; no baggage or customs entitlement is assumed here. Keep receipts and record the purchase once in [[Japan 2027 — Shopping Shortlist]] or [[Japan 2027 — Gifts for Her]], as appropriate.

'''

if '--install' in sys.argv:
    manifest=json.loads((W/'manifest.json').read_text())
    for name,h in manifest.items():assert hashlib.sha256((V/name).read_bytes()).hexdigest()==h,name
    (W/'backup').mkdir(exist_ok=True)
    for name in manifest:
        shutil.copy2(V/name,W/'backup'/name)
        shutil.copy2(W/'staged'/name,V/name)
    assert all((V/name).read_bytes()==(W/'staged'/name).read_bytes() for name in manifest)
    print('Saved island souvenirs for nine islands, six shopping Maps links, and references in personal/gift shortlists; originals backed up and bytes verified.')
else:
    (W/'staged').mkdir(parents=True,exist_ok=True)
    manifest={}
    for name in [NAME,'Japan 2027 — Shopping Shortlist.md','Japan 2027 — Gifts for Her.md']:
        original=(V/name).read_bytes();manifest[name]=hashlib.sha256(original).hexdigest();s=original.decode()
        if name==NAME:
            assert '## Souvenirs — small keepsakes and gifts' not in s
            anchor='## Summer versus November versus May';assert anchor in s
            s=s.replace(anchor,BLOCK+anchor,1)
            i=s.index('\n')+1;s=s[:i]+'\n[[#Souvenirs — small keepsakes and gifts|🎁 Island souvenirs and shopping Maps links]]\n'+s[i:]
            assert s.count('https://www.google.com/maps/search/?')==47
        else:
            i=s.index('\n')+1
            line='**Island gift alternatives:** [[Japan 2027 — Best Islands#Souvenirs — small keepsakes and gifts|Minsa accessories, olive beauty products, sweets, and island keepsakes]]. Use the existing shopping/gift limits; these replace other choices rather than add an allowance.'
            s=s[:i]+'\n'+line+'\n'+s[i:]
        (W/'staged'/name).write_text(s)
    (W/'manifest.json').write_text(json.dumps(manifest))
    print('Prepared nine-island souvenirs, six Maps shopping leads, and two shortlist references; existing 41 Maps links preserved.')
