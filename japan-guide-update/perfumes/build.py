from pathlib import Path
import hashlib, json, shutil, sys
W = Path(__file__).resolve().parent
V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
NAME = 'Japan 2027 — Gifts for Her.md'
SECTION = '''
## Perfumes for her — options to smell in Japan

**Checked 7 October 2026.** Her scent preference is not yet recorded. Enjoying sweets does not establish that she likes sweet perfume; Y2K/Korean clothing preferences also do not determine fragrance taste. Scent descriptions below come from the brands, not personal testing.

| Perfume | Scent direction | Bottle / reference price | Availability evidence |
| --- | --- | --- | --- |
| [SHIRO Savon eau de parfum](https://shiro-shiro.jp/ec/pro/disp/1/12702) | Fruity and clean/soapy: citrus and blackcurrant with soft sweetness. | **40 mL**; the [official Savon catalog](https://shiro-shiro.jp/ec/Facet?category_0=11aa1100000) lists **¥4,180 incl. tax**. The freshly fetched product page did not render a numeric price, so confirm price before buying. | Product page displays **sold out / awaiting restock online**; physical branch stock unconfirmed. |
| [AUX PARADIS Fleur eau de parfum](https://www.auxparadis.com/products/210116.html) | Floral with lemon/bergamot, neroli, and amber/musk notes. | **15 mL ¥3,300** or **30 mL ¥4,400** on the current official product page. | Catalogued with size selection; exact size/branch stock not verified. |
| [AUX PARADIS Savon eau de parfum](https://www.auxparadis.com/products/210117.html) | Lavender-led and soft/soapy. | **15 mL ¥3,300** or **30 mL ¥4,400** on the current official product page. | Catalogued; exact size/branch stock not verified. |

The two brands' perfumes named Savon are different products. These are fragrance candidates to compare; no claim of universal appeal, quality ranking, or popularity among Korean fashion fans is intended.

### My starting recommendation

For a fresh/clean preference, smell **SHIRO Savon** and **AUX PARADIS Savon** side by side. For a floral preference, begin with **Fleur**. I suggest a **15 mL AUX PARADIS spray** if she likes the scent and you prefer a smaller gift. Ask for the full spray bottle: the separately sold replacement nozzle is not a perfume bottle, and the 60 mL AUX PARADIS version is a dropper refill.

Use the existing **US$50 beauty cap inside the US$200 gift ceiling**. Choose perfume instead of some or all of the hand-cream/blotting-paper bundle; if buying both, their combined converted cost must fit that cap. Yen prices are references, not confirmed dollar totals; include payment-rate fees and wrapping when deciding.

### Browsing and bringing it home

[SHIRO official store directory](https://shiro-shiro.jp/ec/ext/shop/index.html) · [AUX PARADIS official store directory](https://www.auxparadis.com/shoplist.html)

Choose a branch that fits an existing shopping outing, and confirm tester and bottle availability before a detour. Try a paper tester first; if testing on skin, allow the scent to develop before deciding. Knowing one perfume she already enjoys would help narrow these choices.

AUX PARADIS's product pages explicitly say the perfume is over 80% alcohol, cannot be shipped by air, and cannot be forwarded overseas. **Do not arrange overseas forwarding.** Before purchasing it to bring home yourself, confirm passenger-baggage acceptance for the exact product with the operating airline; a shipping restriction alone does not settle passenger carriage. Use [[Japan 2027 — Travel Essentials|the flight preparation checklist]] for the booked flights and connections. Keep the bottle closed, protected, and separate from clothes to contain any leak.

- [ ] Her favorite existing perfume / preferred scent family: …
- [ ] Compare tester, full bottle size, shelf price, and remaining beauty budget.
- [ ] Confirm exact branch stock and applicable flight carriage rules before buying.
- [ ] Record purchase and keep packaging/receipt.

Recheck prices, stock, and travel requirements near the March/April 2027 trip. No perfume has been purchased or reserved.
'''

def prepare():
    W.mkdir(parents=True, exist_ok=True)
    original = (V / NAME).read_bytes()
    assert '## Perfumes for her' not in original.decode()
    (W / 'staged.md').write_text(original.decode() + SECTION)
    (W / 'manifest.json').write_text(json.dumps({'sha256': hashlib.sha256(original).hexdigest()}))
    print('Prepared 3 perfume options with prices, stock limits, and beauty-budget integration.')

def install():
    target = V / NAME
    assert hashlib.sha256(target.read_bytes()).hexdigest() == json.loads((W / 'manifest.json').read_text())['sha256']
    shutil.copy2(target, W / 'backup.md')
    shutil.copy2(W / 'staged.md', target)
    assert target.read_bytes() == (W / 'staged.md').read_bytes()
    print('Saved and verified perfume section in Gifts for Her; existing note backed up.')

if __name__ == '__main__':
    install() if '--install' in sys.argv else prepare()
