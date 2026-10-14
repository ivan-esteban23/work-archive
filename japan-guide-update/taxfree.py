from pathlib import Path
from shutil import copy2
v=Path('/home/ivanaguilera/Documents/Obsidian Vault');b=Path('/home/ivanaguilera/Work/japan-guide-update')
p=v/'Japan Travel Guide 2027.md';s=p.read_text();marker='### 💰 Shopping allowance'
assert marker in s and '### 🧾 Tax-free shopping for the 2027 trip' not in s
copy2(p,b/'Main-before-taxfree.md')
s=s.replace(marker,'''### 🧾 Tax-free shopping for the 2027 trip

**Checked 6 October 2026.** These existing stops currently advertise tax-free service; recheck branch participation and procedures before your 2027 visit.

| Existing stop | Verified current status | Official source |
| --- | --- | --- |
| UNIQLO Ginza | UNIQLO advertises tax-free shopping at all Japan stores and specifically features Ginza | [UNIQLO tax-free page](https://www.uniqlo.com/jp/ja/special-feature/tax-free) |
| 2nd STREET Shimokitazawa · 2-30-13 Kitazawa | The exact branch page lists Tax-free and confirms the service | [Branch listing](https://www.2ndstreet.jp/shop/details?shopsId=31139) |
| 2nd STREET Shijo Kawaramachi · 538-1 Nakanocho | The exact branch page lists Tax-free and confirms the service | [Branch listing](https://www.2ndstreet.jp/shop/details?shopsId=30860) |

**Not established in this check:** the guide’s exact Ginza Itoya, RAGTAG Kyoto, Musubi, Ippodo, and Marukyu Koyamaen branches. Ask the chosen shop; unverified does not mean unavailable. Nakamise and Shimokitazawa are areas with multiple independent shops, not one tax-free retailer.

**Your trip falls under the new refund system starting 1 November 2026:** pay the tax-inclusive amount at the participating store, register the eligible purchase, then obtain customs confirmation that the goods are leaving Japan within **90 days of purchase**. The retailer/operator refunds the tax after confirmation. The revised minimum eligible purchase is **¥5,000 before tax**. Ask the shop about aggregation rules, refund method, timing, and any fees. [Official NTA reform leaflet](https://www.nta.go.jp/publication/pamph/shohi/menzei/202506/pdf/0025006-106.pdf)

- [ ] Bring the actual passport and confirm visitor eligibility with the shop before payment.
- [ ] Complete the tax-free purchase registration at checkout; an ordinary receipt alone is not the full procedure.
- [ ] Keep receipts and the purchased goods available for departure customs checks. Check the airport process before handing over checked baggage containing the goods.
- [ ] Record the full amount paid in the budget; record a refund only when received.

Restaurant meals, café drinks consumed during the trip, and hotel stays are not exported shopping goods. Do not budget them as tax-free purchases. [JNTO tax-free shopping overview](https://www.japan.travel/en/plan/japans-tax-exemption/)

'''+marker,1);p.write_text(s)
p=v/'Japan 2027 — Travel Essentials.md';s=p.read_text();copy2(p,b/'Essentials-before-taxfree.md');marker='## ✈️ The evening before leaving Japan';assert marker in s
s=s.replace(marker,'## 🧾 Tax-free purchases before departure\n\nSee [[Japan Travel Guide 2027#🧾 Tax-free shopping for the 2027 trip|verified shops and the new refund process]]. Complete the required customs confirmation before checking in any baggage containing goods that may need inspection; confirm the actual airport procedure. Track refunds separately from money already paid.\n\n'+marker,1);p.write_text(s)
print('Added verified tax-free shop shortlist and 2027 refund guidance; linked departure checklist.')
