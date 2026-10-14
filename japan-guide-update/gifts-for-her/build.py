from pathlib import Path
import hashlib, json, shutil, sys
W = Path(__file__).resolve().parent
V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
S = W / 'staged'
NAME = 'Japan 2027 — Gifts for Her.md'
NOTE = '''# 🎁 Japan 2027 — Gifts for her

[[Japan 2027 — Shopping Shortlist|← Shopping shortlist]] · [[Japan 2027 — Start Here|Dashboard]]

**Her interests:** sweets, fashion, and beauty. **Your gift ceiling: US$200.** Saved 7 October 2026. Her sizes, favorite colors, scents, and dietary preferences are not yet recorded.

## My suggested gift bundle

One patterned accessory, one small beauty bundle, and one boxed sweet gives her something to wear/use and something to enjoy. These are personal suggestions based on her interests.

| Category | Spending cap | What to browse |
| --- | --- | --- |
| Fashion | US$80 | An AYANOKOJI patterned kiss-lock pouch from Kyoto. Choose a pattern she would use. |
| Beauty | US$50 | Yojiya hand cream plus blotting papers; choose her preferred scent. |
| Sweets | US$50 | A Yoku Moku assorted cookie box; one smaller snack can fit the same cap. |
| Wrapping / flexible reserve | US$20 | Gift wrapping or a little extra toward her favorite item. |
| Total maximum | **US$200** | Caps are planning limits, not quoted product costs or a target to spend in full. |

## Fashion — a Kyoto pouch

**First choice:** [AYANOKOJI brocade flat kiss-lock pouch](https://ayanokoji.jp/c/00/144/597/162/p-6hira-kr). The checked page lists **¥3,465 including tax** for the old-hardware version. It offers several patterns; the yellow Marutakara pattern is marked sold out. Treat this exact model as an example: its design, price, and availability may change before 2027. [Official shop directory](https://ayanokoji.jp/shop-list/).

I suggest a pouch because her garment measurements are unknown. Inspect the opening, lining, dimensions, and pattern in person. Her clothing size cannot be inferred from your saved L / EU 44–46 sizes. If choosing a shirt instead, get her measurements and compare the exact garment chart first.

## Beauty — a small Yojiya bundle

- [Mayugomori hand cream, 30 g](https://www.yojiyacosme.com/c/handcream/gd672): checked price **¥900 including tax**. The brand describes its fragrance as including white lily, lavender, and jasmine.
- [Other Yojiya hand creams](https://www.yojiyacosme.com/c/handcream): the catalog lists Hanahonoka at **¥900** and Yuzutsuyaya at **¥950**, including tax. Choose a scent she likes rather than collecting every version.
- [Yojiya blotting papers](https://www.yojiyacosme.com/c/skincare/aburatorigami): browse one small pack to pair with the cream. Exact pack price and branch stock have not been checked.

Check ingredients against her known preferences and sensitivities, and try the scent if a tester is available. Shade-dependent makeup is easier to choose once her preferred shade is known. These are gift suggestions, not tested performance rankings.

## Sweets — one boxed assortment

**First choice:** [Yoku Moku Petit Cinq Délices, 5 varieties / 27 pieces](https://yokumoku.co.jp/products/1010011409100). The [official collection](https://yokumoku.co.jp/collections/cigareplain) lists **¥2,700 including tax** at this check. Choose it if she enjoys butter cookies. Check the exact box's ingredient/allergen label, best-before date, and storage instructions before buying; her dietary preferences are unknown.

**Extra browsing option:** a small packaged Japanese sweet from [[Japan 2027 — Shopping Shortlist#Don Quijote — snacks, small gifts, and practical buys|Donki]]. Matcha flavor is an option if she enjoys it; it is your recorded interest, not a confirmed preference of hers. Keep extras inside the sweets cap.

## Where this fits the trip

- Kyoto: browse the pouch and beauty gifts during an existing central shopping break. [[Japan 2027 — Pocket 2027-04-05|5 April]] is an option if you choose a central outing; select branches and check opening hours before adding a route.
- Tokyo: buy boxed sweets late in the trip. [[Japan 2027 — Pocket 2027-04-07|7 April]] is a possible shopping day; choose which optional shopping stops fit alongside Tamiya and packing time.
- Save these product links before departure and recheck prices, variants, and store stock. Online listings do not establish stock in a particular branch or availability in March/April 2027.

## How the US$200 fits the wider budget

The **US$200 gift ceiling is confirmed**. Whether it is included in the existing **US$300 shopping/miscellaneous allowance** or additional to it remains open.

| Budget treatment | Result |
| --- | --- |
| Gifts included in US$300 | Up to US$200 for her leaves US$100 for your other shopping/miscellaneous purchases; revise the earlier category caps before buying. |
| Gifts additional to US$300 | Shopping/miscellaneous becomes US$500; the provisional in-Japan plan rises from US$3,850 to US$4,050, leaving US$950 of the US$5,000 envelope. Flights remain excluded. |

These are scenarios; the main guide's budget has not been revised. Convert the caps using the actual payment exchange rate and fees; record every purchase once.

## Before buying

- [ ] Favorite colors/patterns: …
- [ ] Preferred beauty scent and any ingredient exclusions: …
- [ ] Sweet flavors and dietary needs: …
- [ ] Decide which wider-budget scenario applies.
- [ ] Check exact item, shelf price, expiry where relevant, gift wrapping, and packing space.
- [ ] Record purchase, yen cost, converted spend, and where it came from.

Prices are official website reference prices checked 7 October 2026, not locked-in trip prices. No purchase or reservation has been made.
'''

def prepare():
    S.mkdir(parents=True, exist_ok=True)
    assert not (V / NAME).exists()
    (S / NAME).write_text(NOTE)
    manifest = {NAME: None}
    for filename in ['Japan 2027 — Shopping Shortlist.md', 'Japan 2027 — Start Here.md', 'Japan Travel Guide 2027.md']:
        p = V / filename
        manifest[filename] = hashlib.sha256(p.read_bytes()).hexdigest()
        text = p.read_text()
        assert '[[Japan 2027 — Gifts for Her' not in text
        first = text.index('\n') + 1
        text = text[:first] + '\n**Gifts for her:** [[Japan 2027 — Gifts for Her|Sweets, fashion, and beauty — US$200 gift plan]]\n' + text[first:]
        (S / filename).write_text(text)
    (W / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    validate(S)
    print('Prepared gift note and links in 3 guide notes.')

def validate(root):
    assert (root / NAME).read_text() == NOTE
    for filename in json.loads((W / 'manifest.json').read_text()):
        if filename != NAME:
            assert (root / filename).read_text().count('[[Japan 2027 — Gifts for Her|') == 1

def install():
    manifest = json.loads((W / 'manifest.json').read_text())
    for filename, digest in manifest.items():
        p = V / filename
        assert not p.exists() if digest is None else hashlib.sha256(p.read_bytes()).hexdigest() == digest
    backup = W / 'backup'
    backup.mkdir(exist_ok=True)
    for filename, digest in manifest.items():
        if digest is not None:
            shutil.copy2(V / filename, backup / filename)
    for filename in manifest:
        shutil.copy2(S / filename, V / filename)
    validate(V)
    print('Saved and verified gift note and 3 guide links; existing notes backed up.')

if __name__ == '__main__':
    install() if '--install' in sys.argv else prepare()
