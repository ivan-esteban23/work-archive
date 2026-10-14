from pathlib import Path
import hashlib,json,shutil,sys
W=Path(__file__).resolve().parent
V=Path('/home/ivanaguilera/Documents/Obsidian Vault')
S=W/'staged'
SECTION='''## Don Quijote — snacks, small gifts, and practical buys

- [ ] Visit **Don Quijote (Donki), Ginza Honkan**, if it fits the Shinbashi/Ginza shopping block.
- [ ] Choose at most **two food gifts and one useful small item**, within the remaining allowance.

**Suggested slot:** [[Japan 2027 — Pocket 2027-04-07|7 April]], after Tamiya only if time and luggage space allow. Allow **30–45 minutes** as a personal browsing target, plus checkout time. Choose Donki or the optional clothing/café extension rather than adding every stop. If you already choose a Shibuya outing, the existing MEGA Don Quijote Shibuya Honten option can replace this branch.

**Current branch details, checked 7 October 2026:** Ginza Nine #3, 8-10 Ginza, Chuo-ku. Its official page lists **24-hour opening**, no regular holiday, and about **5 minutes on foot from Shinbashi Station**. This is station-to-store guidance, not a measured Tamiya-to-Donki walk. Recheck for 2027; tax-free desk hours may differ. [Official Ginza Honkan branch](https://www.donki.com/en/store/shop_detail.php?shop_id=92) · [Maps search](https://www.google.com/maps/search/?api=1&query=Don+Quijote+Ginza+Honkan+Tokyo) · [Existing Shibuya alternative](https://www.gotokyo.org/en/spot/1879/index.html)

### What I would browse for your interests

| Priority | Candidate | Why I suggest it / what to check |
| --- | --- | --- |
| First | [Shizuoka matcha, 30 g](https://www.donki.com/j-kakaku/product/detail.php?item=3528) | Official listing gives green tea from Shizuoka as the ingredient; a compact tea option. Compare freshness, intended use, and price with your Ippodo choice. It is an alternative tea purchase, not an extra required tin. |
| First | [Two-color sweet-potato chips](https://www.donki.com/j-kakaku/product/detail.php?item=5180) | A different packaged snack to try or take as a small gift. Check ingredients, expiry, bag size, and whether the packaging protects it in luggage. |
| Optional | [Bite-size milk chocolate](https://www.donki.com/j-kakaku/product/detail.php?item=4375) | An easy snack-gift candidate. Check the actual pack and portions, ingredients, and storage needs; no claim that it beats other shops on price. |
| Optional | Matcha-flavored sweets from the shelf | Fits your matcha interest; pick a small pack to taste first. This is a browsing idea, not a verified brand/flavor in stock at Ginza. |
| Practical | [Men’s basics catalog](https://www.donki.com/j-kakaku/product/list.php?cid=3) | Browse an everyday or layering item if needed. Your saved top size is L; compare the actual garment chart and fit. No L/XL branch stock was established. |
| Practical | [Black tapered pants](https://www.donki.com/j-kakaku/product/detail.php?item=5027) | An additional casual-pants lead. Official sizes are M/L/LL/3L, with a listed store maximum of **¥3,299 including tax** at the checked page. Your EU 44–46 requires a waist/hip/inseam comparison; M is not confirmed to fit. |
| Practical | [Bags and small accessories](https://www.donki.com/j-kakaku/product/list.php?cid=5) | Look for a compact item you actually need, such as a small pouch. The category exists; a particular pouch/price was not checked. |

These are product-catalog leads and personal suggestions, **not confirmed Ginza stock or independent quality rankings**. Donki's JONETZ catalog says selection and price vary by store. Save the product's JAN barcode from its page to help staff check the exact item. No specific denim jacket or flannel in your size was verified at Donki; keep the existing [[Japan 2027 — Clothing to Browse Online|clothing links]] for those searches. [Official product catalog](https://www.donki.com/j-kakaku/)

### A small basket within the current budget

My starting suggestion is a **US$20 equivalent limit**, converted using your actual yen rate and fees. This is a spending cap, not a quoted basket price. For souvenir snacks, use the existing souvenir pool and reduce another optional purchase—for example, replace the suggested US$20 record/movie buy. Tea replaces some or all of the tea allocation; clothing uses the existing US$150 clothing cap; a practical item uses its applicable existing gifts/extras category. Record each purchase once. The total shopping/miscellaneous ceiling remains **US$300**.

Snacks consumed during the trip use the meals/drinks allowance; food brought home as gifts uses the souvenir allocation. Check package ingredients and relevant return-home food requirements before choosing food gifts; use the existing [[Japan 2027 — Travel Essentials|travel essentials]] for preparation. Recheck tax-free rules for the 2027 visit before relying on any savings.

### Donki visit checklist

- [ ] Confirm branch, remaining shopping budget, and suitcase space.
- [ ] Save exact product links/JAN codes for the items I want to compare.
- [ ] Check shelf price, pack size, ingredients, and expiry; compare prices only for the same product/quantity.
- [ ] For clothing, compare measurements and applicable fitting/return terms.
- [ ] Record spending and one souvenir story; ask staff before filming inside.

'''

def prepare():
    S.mkdir(parents=True,exist_ok=True);manifest={}
    def save(filename,fn):
        p=V/filename;manifest[filename]=hashlib.sha256(p.read_bytes()).hexdigest();(S/filename).write_text(fn(p.read_text()))
    def shortlist(s):
        assert '## Don Quijote' not in s and '## Keep the existing shopping ceiling' in s
        return s.replace('## Keep the existing shopping ceiling',SECTION+'## Keep the existing shopping ceiling',1)
    save('Japan 2027 — Shopping Shortlist.md',shortlist)
    link='[[Japan 2027 — Shopping Shortlist#Don Quijote — snacks, small gifts, and practical buys|Donki buying ideas and visit checklist]]'
    save('Japan 2027 — Shops and Cafés.md',lambda s:s+'\n## 🛒 Donki practical shopping stop\n\n'+link+' — Ginza Honkan is a proposed short extension to the Shinbashi/Tamiya day. Product links, branch details, stock limits, and a basket cap are in the shortlist.\n')
    save('Japan 2027 — Clothing to Browse Online.md',lambda s:s+'\n## Donki clothing alternatives\n\n'+link+' includes the official men’s catalog and black tapered pants. Your saved sizes remain L tops and EU 44–46 trousers. Donki’s pants list M/L/LL/3L; waist measurements and fit must be checked before choosing a size. Branch stock is unconfirmed.\n')
    def main(s):
        pos=s.index('\n')+1
        return s[:pos]+'\n**Don Quijote:** '+link+'\n'+s[pos:]
    save('Japan Travel Guide 2027.md',main)
    def pocket(s):
        assert '**Rain backup:**' in s
        return s.replace('**Rain backup:**','**Donki option:** Ginza Honkan for a short snack/gift stop after Tamiya if time allows; choose this or the other shopping extension. '+link+'\n\n**Rain backup:**',1)
    save('Japan 2027 — Pocket 2027-04-07.md',pocket)
    (W/'manifest.json').write_text(json.dumps(manifest,indent=2));validate(S)
    print('Prepared Donki shortlist with verified catalog links, branch details, and 4 guide integrations.')

def validate(root):
    s=(root/'Japan 2027 — Shopping Shortlist.md').read_text()
    assert s.count('## Don Quijote — snacks, small gifts, and practical buys')==1
    assert all(x in s for x in ['item=3528','item=5180','item=4375','item=5027','US$300'])
    for staged in S.glob('*.md'):
        if staged.name!='Japan 2027 — Shopping Shortlist.md': assert '#Don Quijote — snacks, small gifts, and practical buys|' in (root/staged.name).read_text()

def install():
    manifest=json.loads((W/'manifest.json').read_text())
    for filename,h in manifest.items(): assert hashlib.sha256((V/filename).read_bytes()).hexdigest()==h,filename
    backup=W/'backup';backup.mkdir(exist_ok=True)
    for filename in manifest: shutil.copy2(V/filename,backup/filename)
    for p in S.glob('*.md'): shutil.copy2(p,V/p.name)
    validate(V);assert all(p.read_bytes()==(V/p.name).read_bytes() for p in S.glob('*.md'))
    print('Saved and verified Donki addition in 5 notes; existing notes backed up.')

if __name__=='__main__': install() if '--install' in sys.argv else prepare()
