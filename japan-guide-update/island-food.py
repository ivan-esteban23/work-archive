from pathlib import Path
import hashlib,json,re,shutil,sys
V=Path('/home/ivanaguilera/Documents/Obsidian Vault')
W=Path('/home/ivanaguilera/Work/japan-guide-update/island-food')
NAME='Japan 2027 — Best Islands.md'
BLOCK='''## Foods to try — island shortlist

**Added / checked:** 7 October 2026. These are local dish ideas, not confirmed travel-date menus or restaurant bookings. My first three for you are **anago-meshi on Miyajima**, **Shodoshima somen**, and **Yaeyama soba on Ishigaki/Taketomi**. Choose one main meal and one small sweet per island day; an Ishigaki beef meal can be a deliberate splurge after checking its price.

| Island | What to try | What it is / how I would order | Source |
| --- | --- | --- | --- |
| **Miyajima** | **Anago-meshi**, oysters, **momiji manju** | Grilled conger eel over rice as your main meal; cooked oysters as an alternative or small plate. Finish with a maple-leaf-shaped cake; fillings can include red bean, custard, chocolate, or matcha. | [Local savory dishes](https://www.miyajima.or.jp/english/gourmet/gourmet.html) · [Sweets and fillings](https://visit-miyajima-japan.com/en/culture-and-heritage/culinary-heritage.html) |
| **Naoshima** | Udon lunch | A practical Kagawa noodle lunch between art visits; Kinosaki Udon is a named lead. This is a regional food choice, not a claim that udon is unique to Naoshima. | [Official tourism restaurant listing](https://naoshima.net/ja/foodsen/kinosaki-udon/) |
| **Shodoshima** | **Hand-stretched somen**, local soy sauce / olive products | Thin wheat noodles; try fresh/unprocessed somen if on the menu. Browse a small soy-sauce or olive product as a gift rather than buy a heavy basket. | [Official somen guide](https://www.my-kagawa.jp/en/see-and-do/10126) · [Local products](https://www.kagawa-culture-compass.net/en/spot/052.html) |
| **Yakushima** | **Tobiuo — flying fish** | Ask for the restaurant's cooked flying-fish dish or set meal; preparation and availability depend on the menu. A prearranged bento is practical for a chosen hike. | [JNTO Yakushima food guide](https://www.japan.travel/en/spot/ma_229/) |
| **Ishigaki** | **Yaeyama soba**, **Ishigaki beef** | Regional noodles in broth for one lunch; compare a clearly priced beef portion or set meal for your special dinner. Check the actual toppings and broth if you avoid an ingredient. | [Regional soba explanation — MAFF](https://www.maff.go.jp/e/policies/market/k_ryouri/search_menu/5566/index.html) · [Okinawa beef brands](https://visitokinawajapan.com/discover/food-and-longevity/taste-okinawa/tender-tasty-premium-meats/) |
| **Taketomi** | Yaeyama soba | The same regional noodle family makes a sensible village-day lunch. Choose an open café/restaurant and leave enough time for the ferry; no named venue or stock is confirmed here. | [Official regional cuisine guide](https://www.maff.go.jp/e/policies/market/k_ryouri/search_menu/5566/index.html) |
| **Miyako** | **Miyako soba**, mango dessert, optional Miyako beef | Noodle soup first; mango shaved ice or juice if available. The official guide lists fresh local mango season as June–August, so May/November availability should not be assumed. | [Official Miyako food guide](https://visitokinawajapan.com/destinations/miyako-islands/miyako-island/) |
| **Enoshima** | **Shirasu-don**, shirasu croquette or crackers | Rice topped with tiny whitebait fish; ask for the cooked version if that suits you. Raw whitebait depends on the day's catch. A croquette is an alternative snack. | [Official Fujisawa local cuisine](https://discover-fujisawa.jp/en/sightseeing/cuisine/) |
| **Sado** | **Buri katsudon**, local rice and seafood | Deep-fried amberjack over rice; choose a local rice/seafood meal if that dish is unavailable. | [JNTO Sado food information](https://www.japan.travel/en/destinations/hokuriku-shinetsu/niigata/sado-island/) |

### Food stops with Google Maps links

These are Google Maps searches for verified browsing leads or named food areas; check the displayed island/branch and current menu before visiting. No travel-day hours, prices, reservations, or opening status have been confirmed.

- **Miyajima — Momiji-do Head Shop:** an age-momiji (deep-fried momiji manju) snack lead. [Google Maps](https://www.google.com/maps/search/?api=1&query=Momijido+Head+Shop+Miyajima+Hiroshima) · [Tourism association's food/shop map](https://www.miyajima.or.jp/english/map/img/map_omotesando.pdf).
- **Miyajima — Yakigaki-no-Hayashi:** oyster/conger-eel meal lead. [Google Maps](https://www.google.com/maps/search/?api=1&query=Yakigaki+no+Hayashi+Miyajima+Hiroshima) · [Same official shop map](https://www.miyajima.or.jp/english/map/img/map_omotesando.pdf).
- **Naoshima — Kinosaki Udon:** noodle-lunch lead. [Google Maps](https://www.google.com/maps/search/?api=1&query=Kinosaki+Udon+Naoshima+2071-4) · [Official tourism listing](https://naoshima.net/ja/foodsen/kinosaki-udon/).
- **Shodoshima — Nakabuan:** somen/food-culture lead; factory experiences require checking reservations separately from a meal. [Google Maps](https://www.google.com/maps/search/?api=1&query=Nakabuan+Shodoshima+Kagawa) · [Official somen-experience information](https://www.my-kagawa.jp/en/see-and-do/10126).

### Sweets and gifts for her

**My first pick is a small momiji-manju box** if you visit Miyajima. Taste one before deciding on the filling, then check the package's best-before date and storage instructions against your return date. Keep fresh desserts as something to enjoy on the island; a packaged gift needs its own shelf-life check. Shodoshima's small olive-food products or dried somen are alternatives for someone who enjoys cooking.

Take-home gifts count under shopping and her existing US$200 cap; meals/snacks eaten during the trip count under meals. They share your existing allowances rather than creating another food-gift budget. Link back to [[Japan 2027 — Gifts for Her|her gift shortlist]] when recording a purchase.

**Photography idea:** a wide meal scene → one food texture → preparation only with staff permission. Check your meal options before the island return connection; don't assume a late ferry arrival leaves dinner venues open. Food preferences and allergies have not been supplied, so the shortlist is flexible.

'''

if '--install' in sys.argv:
    h=json.loads((W/'manifest.json').read_text())['original_sha256']
    assert hashlib.sha256((V/NAME).read_bytes()).hexdigest()==h
    shutil.copy2(V/NAME,W/'backup.md')
    shutil.copy2(W/'staged.md',V/NAME)
    assert (V/NAME).read_bytes()==(W/'staged.md').read_bytes()
    print('Saved and verified nine-island food shortlist, four food-stop Maps links, sweet-gift ideas, and budget notes. Chapter backed up.')
else:
    W.mkdir(parents=True,exist_ok=True)
    original=(V/NAME).read_bytes();s=original.decode()
    assert '## Foods to try — island shortlist' not in s
    anchor='## Summer versus November versus May'
    assert anchor in s
    s=s.replace(anchor,BLOCK+anchor,1)
    i=s.index('\n')+1
    s=s[:i]+'\n[[#Foods to try — island shortlist|🍽️ Island foods and food-stop Maps links]]\n'+s[i:]
    assert s.count('https://www.google.com/maps/search/?')==41
    assert all('| **'+n+'** |' in BLOCK for n in ['Miyajima','Naoshima','Shodoshima','Yakushima','Ishigaki','Taketomi','Miyako','Enoshima','Sado'])
    (W/'staged.md').write_text(s)
    (W/'manifest.json').write_text(json.dumps({'original_sha256':hashlib.sha256(original).hexdigest()}))
    print('Prepared foods for nine islands, four Google Maps food leads, and gift notes; existing Maps/access content preserved.')
