from pathlib import Path
import hashlib, json, shutil, sys
W = Path(__file__).resolve().parent
V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
NAME = 'Japan 2027 — Gifts for Her.md'
SECTION = '''
## Clothing for her — Y2K and Korean-inspired wishlist

**Her additional preferences:** Y2K fashion and Korean outfits. Research checked **7 October 2026**; outfit suggestions below are my interpretation of current Japanese retailers' styling. They describe options to browse in Japan, not a nationwide Korean trend ranking or a prediction for spring 2027.

### Current directions worth browsing

- **Y2K / Heisei-gal:** rhinestone logos, graphic fitted tops, zip hoodies, and flared denim. [SPINNS style directory](https://www.spinns.jp/c/taste) and [September 2026 outfit ideas](https://www.spinns.jp/women_s/) show these combinations.
- **Korean-inspired feminine styling:** cardigan-and-camisole layers, ribbons, dots, and pleated skirts. [SPINNS current collection](https://www.spinns.jp/c/taste/girly) and [WEGO Korean-inspired collection](https://wego.jp/collections/f-cts-kr-fashion-girly) are useful visual references.
- **Streetwear crossover:** a fitted top with a loose bottom, or a statement zip hoodie over a simple outfit. [WEGO's Y2K-tagged hoodie](https://wego.jp/products/di25wn11-l0015) is a concrete example.

These Japanese shops sell Korean-inspired styles; that label does not establish that every item is a Korean brand or made in Korea.

### Shortlist to browse online

| Candidate | Website reference price | Size / stock evidence | My suggested use |
| --- | --- | --- | --- |
| [WEGO / dispark rhinestone-logo faux-fur zip hoodie](https://wego.jp/products/di25wn11-l0015), DI25WN11-L0015 | **¥3,000 incl. tax online promotion**; previous displayed ¥6,929. The promotion is web-only, so check store price. | Black **F** marked low online stock on the fetched page; selected stores only. | First Y2K option if she likes statement hoodies. Compare chest, shoulder, sleeve, and length measurements. |
| [SPINNS knit cardigan + dotted camisole set](https://www.spinns.jp/c/taste/girly), search セットアイテム/ニットカーディガン+ドットキャミソール | **¥4,389 incl. tax** on the collection page. | Exact garment measurements and color/size stock not established; individual product page could not be fetched. | First Korean-inspired option; I would browse this before committing to a pouch. |
| [SPINNS fitted striped zip hoodie](https://www.spinns.jp/c/taste/girly), search タイトジップパーカー/ボーダー | **¥4,389 incl. tax** on the collection page. | Exact measurements and variant stock not established; individual page could not be fetched. | A simpler layering option if she prefers stripes to rhinestones. |
| [SPINNS flared denim](https://www.spinns.jp/c/taste?page=5&sort=latest), search デニムフレアパンツ/ヒゲ | **¥5,489 incl. tax** on the checked listing. | Listing advertises two sizes; waist, rise, hip, inseam, and exact stock require checking. | Strong Y2K outfit lead once her measurements are available. |
| [WEGO / dispark logo-and-lace wide sweatpants](https://wego.jp/products/di26as07-l0013), DI26AS07-L0013 | **¥6,929 incl. tax** sale display; previous displayed ¥8,909. | Black **F is marked out of stock online**; branch availability unconfirmed. | Keep as a style reference or a restock candidate, not a currently available pick. |

Collection links remain useful if an individual model sells out. Copy the Japanese product name into the site's search. Prices and online status are a snapshot, and none of these items has confirmed March/April 2027 branch stock.

### What I would buy first

Choose **one cardigan-and-camisole set OR one rhinestone hoodie**, after checking her measurements and favorite colors. Flared jeans are a second option once fit is clear. Outfit idea: cardigan/camisole with her own jeans for the feminine look; rhinestone hoodie with her own flares for Y2K. These are styling suggestions, not additional required purchases.

Clothing uses the existing **US$80 fashion cap within the US$200 gift ceiling**, replacing some or all of the pouch allocation. If a second garment would exceed that cap, reduce another gift category explicitly before purchase. Keep the US$20 flexible reserve available for wrapping or exchange-rate differences.

### Fit and shopping checks

- [ ] Her usual top / bottom size: …; height: …
- [ ] Compare a garment she already likes: chest width, shoulder, sleeve, length; bottom waist, hip, rise, and inseam: …
- [ ] Favorite colors and whether she likes cropped, fitted, oversized, or low-rise cuts: …
- [ ] Check the item's own measurement chart. **F/free size describes one offered size, not universal fit.** Your saved clothing sizes belong to you.
- [ ] Save her preferred product photos and exact item codes; confirm store stock and store price before making a detour.
- [ ] Check gift exchange/return terms and keep tags and receipts.

Browse during an existing Tokyo clothing outing; choose a branch using the retailer's directory before changing the daily route. A dedicated store stop and travel time have not been added yet.
'''

def prepare():
    W.mkdir(parents=True, exist_ok=True)
    original = (V / NAME).read_bytes()
    assert '## Clothing for her' not in original.decode()
    (W / 'staged.md').write_text(original.decode() + SECTION)
    (W / 'manifest.json').write_text(json.dumps({'sha256': hashlib.sha256(original).hexdigest()}))
    print('Prepared 5 clothing leads, current styling references, fit checks, and budget integration.')

def install():
    target = V / NAME
    assert hashlib.sha256(target.read_bytes()).hexdigest() == json.loads((W / 'manifest.json').read_text())['sha256']
    shutil.copy2(target, W / 'backup.md')
    shutil.copy2(W / 'staged.md', target)
    assert target.read_bytes() == (W / 'staged.md').read_bytes()
    print('Saved and verified clothing wishlist in Gifts for Her; original note backed up.')

if __name__ == '__main__':
    install() if '--install' in sys.argv else prepare()
