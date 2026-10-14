from pathlib import Path
import hashlib, shutil, sys
W = Path('/home/ivanaguilera/Work/japan-guide-update/perfume-minis')
V = Path('/home/ivanaguilera/Documents/Obsidian Vault/Japan 2027 — Gifts for Her.md')
SECTION = '''### Preferred plan while her scent preference is unknown

**My pick: two SHIRO eau de parfum minis — Savon and White Lily, 10 mL each.** This gives her a fresh/soapy scent and a floral scent to compare. This is a suggested pairing of two separately sold bottles, not a verified boxed discovery set. [Official mini product page](https://shiro-shiro.jp/ec/pro/disp/1/12737).

| Mini | Brand's scent description | Why I suggest it |
| --- | --- | --- |
| Savon | Citrus/fruity with soft sweetness and a clean, soapy character. | One fresh option to try. |
| White Lily | Lily and magnolia; floral. | A different direction to compare with Savon. |

The [official mini feature](https://shiro-shiro.jp/ec/sp?F=7527) lists **¥1,760 including tax per bottle**: two would be **¥3,520 before any wrapping or delivery costs**, if that price still applies. The freshly fetched product page shows **sold out / awaiting restock** and does not render a numeric price. Variant and branch availability remain unconfirmed; treat this as a shopping target and recheck before the trip. The 40 mL bottle's stock status does not establish mini stock.

Keep perfume and any remaining hand cream inside the existing **US$50 beauty allowance** and the **US$200 gift ceiling**, using the actual payment exchange rate. Ask a fitting branch from the [SHIRO store directory](https://shiro-shiro.jp/ec/ext/shop/index.html) whether both minis and gift wrapping are available before making a detour. Confirm carriage with the booked airline as part of flight preparation.

Her preference is still unknown; these choices are my recommendation, not a guarantee she will like them. If both minis cannot be found, keep the earlier AUX PARADIS 15 mL candidates as alternatives after checking their carriage requirements. No current boxed discovery set was verified and no purchase has been made.

'''
if '--install' in sys.argv:
    assert hashlib.sha256(V.read_bytes()).hexdigest() == (W/'sha256').read_text()
    shutil.copy2(V, W/'backup.md')
    shutil.copy2(W/'staged.md', V)
    assert V.read_bytes() == (W/'staged.md').read_bytes()
    print('Saved and verified preferred two-mini perfume plan; previous note backed up.')
else:
    W.mkdir(exist_ok=True)
    original = V.read_bytes()
    text = original.decode()
    start = text.index('### My starting recommendation\n')
    end = text.index('### Browsing and bringing it home\n', start)
    text = text[:start] + SECTION + text[end:]
    assert text.count('### Preferred plan while her scent preference is unknown') == 1
    (W/'staged.md').write_text(text)
    (W/'sha256').write_text(hashlib.sha256(original).hexdigest())
    print('Prepared preferred Savon + White Lily mini plan, with stock and price limits.')
