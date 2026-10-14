from pathlib import Path
from shutil import copy2
p=Path('/home/ivanaguilera/Documents/Obsidian Vault/Japan Travel Guide 2027.md')
s=p.read_text();marker='### 💰 Shopping allowance'
assert marker in s and '### 🛒 More verified tax-free shops' not in s
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Main-before-more-shops.md'))
s=s.replace(marker,'''### 🛒 More verified tax-free shops

**Official branch/service pages checked 6 October 2026.** These expand your choices, not your shopping budget or fixed itinerary. The pages confirm current tax-free participation; old same-day refund instructions on retailer pages may describe the pre-November 2026 system. Use [[#🧾 Tax-free shopping for the 2027 trip|the 2027 refund guidance]] and recheck branch procedures before your visit.

| Shop | Choose it for | Route fit | Verified service / official source | Maps search |
| --- | --- | --- | --- | --- |
| **MUJI Ginza** | Simple clothing, stationery, travel accessories, and small home goods | Existing Ginza café/shopping outing | Exact flagship page lists tax-free service and a dedicated register. [Official branch](https://www.muji.com/jp/ja/shop/detail/046604) | [MUJI Ginza](https://www.google.com/maps/search/?api=1&query=MUJI+Ginza+Tokyo) |
| **GU Ginza** | Compare everyday clothes and casual styles with UNIQLO | Same Ginza block; 5-7-7 Ginza | GU advertises tax-free at its Japan stores and features this exact branch. [Official tax-free page](https://www.gu-global.com/jp/ja/feature/contents/tax-free/all) | [GU Ginza](https://www.google.com/maps/search/?api=1&query=GU+Ginza+5-7-7+Tokyo) |
| **Ginza Loft** | Stationery, notebooks, design gifts, and personal-care items | Alternative or complement to Itoya, if time allows | Exact branch lists tax-free registration and counter hours. Ginza Belvia, 2-4-6 Ginza. [Official branch](https://www.loft.co.jp/ginzaloft/) | [Ginza Loft](https://www.google.com/maps/search/?api=1&query=Ginza+Loft+2-4-6+Tokyo) |
| **Don Quijote Ginza Honkan** | Packaged gifts, snacks, and practical travel items | Optional separate stop toward southern Ginza | Exact branch page displays TAX FREE. Confirm the tax-free desk’s own hours. [Official branch](https://www.donki.com/en/store/shop_detail.php?shop_id=92) | [Ginza Honkan](https://www.google.com/maps/search/?api=1&query=Don+Quijote+Ginza+Honkan+Tokyo) |
| **Hands Kyoto** | Stationery, useful household items, and small gifts | Downtown Kyoto shopping block around Shijo | Kyoto branch explicitly lists Tax Free among its services. [Official branch](https://store.hands.net/kyoto/) | [Hands Kyoto](https://www.google.com/maps/search/?api=1&query=Hands+Kyoto+Japan) |
| **JR Kyoto Isetan** | Compare clothing, craft/home goods, and packaged food gifts | Kyoto Station area; use a suitable flexible block | Official overseas-customer page lists a tax-free counter; currently notes a processing fee and exclusions. Ask about 2027 fees and eligible products. [Official visitor services](https://www.mistore.jp/store/kyoto/foreign_customer.html) | [JR Kyoto Isetan](https://www.google.com/maps/search/?api=1&query=JR+Kyoto+Isetan+Japan) |

**Tea-shopping lead:** Ippodo’s own support page identifies a JR Kyoto Isetan sales location. This gives you another place to ask about packaged tea, but it does not verify matcha stock, purchase limits, or eligibility of a particular item under Isetan’s tax-free procedures. Check those at the counter before paying. [Official Ippodo location reference](https://support.ippodo-tea.co.jp/hc/ja/articles/15721848722831)

**My suggested shortlist:** choose MUJI or GU for clothes, Loft or Hands for stationery, and Isetan if gifts fit a station-area outing. Don Quijote is an optional practical stop. Do not try to visit every shop, and compare the final price after any fees rather than treating the tax-free label as proof of a bargain.

**Before checkout:** ask whether the branch and selected items qualify, which purchases may be combined, how your passport/entry status is checked, and how the refund is delivered. Keep the gross purchase in your budget until the refund arrives. Pack exported food/tea for departure inspection and [[Japan 2027 — Travel Essentials#🎁 Bringing matcha and food souvenirs back to Chile|declare relevant souvenirs to SAG on returning to Chile]]. Map links are searches; verify the selected branch and entrance.

'''+marker,1)
p.write_text(s)
print('Added six officially verified optional tax-free shops, Maps links, route fit, and a qualified Ippodo tea-shopping lead.')
