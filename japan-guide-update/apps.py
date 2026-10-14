from pathlib import Path
from shutil import copy2
v=Path('/home/ivanaguilera/Documents/Obsidian Vault');p=v/'Japan 2027 — Travel Essentials.md';s=p.read_text();marker='## 📱 Phone and payment backups'
assert marker in s and '## 📲 Apps to prepare on your iPhone' not in s
section='''## 📲 Apps to prepare on your iPhone

**Official sources checked 6 October 2026.** Recommended for your Tokyo–Kyoto trip using an iPhone and a Chilean account. This is a practical shortlist, not a ranking of app usage among Japanese residents. Recheck App Store region availability, phone requirements, fees, and 2027 features before departure. Use the developer’s official page for download links.

| Priority | App / service | How you will use it | Setup / official link |
| --- | --- | --- | --- |
| Essential | **Google Maps** | Open the guide’s saved shops, cafés, sightseeing stops, and transport locations; plan the next journey online | Download your Tokyo/Kyoto areas if available, and save important route screenshots. Offline Maps does not provide walking or public-transport directions. [Google’s iPhone guidance](https://support.google.com/maps/answer/6291838?co=GENIE.Platform%3DiOS&hl=en) · [[Japan 2027 — Maps|Your Maps index]] |
| Essential | **Google Translate** (or Apple Translate) | Read signs and menus, type a question, or help with a short conversation | Download Japanese and Spanish in Google Translate before leaving, then test in airplane mode. Available offline functions vary; do not assume every feature works offline. [Google iPhone language downloads](https://support.google.com/translate/answer/6142473?co=GENIE.Platform%3DiOS&hl=en) · [Apple alternative](https://support.apple.com/en-ae/guide/iphone/-iphd74cb450f/ios) |
| Essential setup | **Apple Wallet + Suica** | Tap for supported local transport and purchases | Wallet is built in; create Suica there rather than installing the separate Japanese Suica app for basic use. Test a small top-up using your own card; Apple Pay enrollment alone does not confirm that every Chilean debit card can fund Suica. Keep backup cash/card. [Apple setup instructions](https://support.apple.com/ja-jp/108772) |
| Essential preparation | **Safety tips** | Receive earthquake, tsunami, and special weather warnings, and access disaster guidance | Set the language, locations, and notification permissions before travel. This is the visitor-focused tool supervised by Japan’s Tourism Agency. [Official agency guidance](https://www.mlit.go.jp/kankocho/seisaku_seido/kihonkeikaku/jizoku_kankochi/anzenkakuho/inbound/tool.html) |
| Useful addition | **Japan Travel by NAVITIME** | A second tool for rail/transit route planning, plus nearby stations and ATMs | Choose the visitor version named Japan Travel by NAVITIME. Check which current features are free or require payment before subscribing. [Official app page](https://static.japan.travel.navitime.com/app-lp/en/index.html) |
| Useful taxi backup | **GO** | Request a taxi when tired, carrying luggage, or unable to use the planned train | Register and test phone verification before leaving. Official visitor guidance supports non-Japanese phone numbers and international cards/Apple Pay. Confirm your actual card and the fare plus fees. Short-term foreign visitors currently incur an International Service Charge; check the booking screen. [Official visitor app page](https://go.goinc.jp/en) · [Fee explanation](https://support.go.goinc.jp/hc/en-us/articles/46695032643737-What-is-the-International-Service-Charge) |
| Useful for food | **Tabelog multilingual app** | Find nearby restaurants/cafés, photos, and available reservations | Use the multilingual version. Browsing can start without signup; online reservations require an account and acceptance of the restaurant’s conditions. If unavailable in the Chilean App Store, use its English website. [Official multilingual app](https://tabelog.com/en/tabelog-multilingual-app/) · [FAQ](https://tabelog.com/en/help) |
| Optional social tool | **LINE** | Communicate when a local contact or business specifically uses LINE | Install only if you will use it. For residents of Chile, current account creation uses Continue with Apple or Google; select the country you actually live in. It is not required to ride trains or shop. [Official signup instructions](https://help.line.me/?contentId=20001192) |
| Keep ready | **Your chosen eSIM app, bank apps, airline app, and Obsidian** | Manage data, approve payments, access the actual flight booking, and read your guide | Pick the eSIM after comparing its plan. Test bank verification abroad and ensure your vault/confirmations are available offline before leaving; this note does not install apps or configure your phone. |

### 🌐 Bookmark these instead of relying on another app

- **Visit Japan Web:** open the official service through Safari and optionally add its shortcut to the Home Screen. Complete the actual arrival details and save the code backup. [Official access](https://services.digital.go.jp/en/visit-japan-web/)
- **SmartEX:** use the official English website for Tokyo–Kyoto bookings. Chile is absent from the currently published list of countries/regions where its international app can be downloaded; do not rely on finding it in your Chilean App Store. [Official app-region FAQ](https://smart-ex.jp/en/faq/category/detail/?id=582) · [English booking service](https://smart-ex.jp/en/)

### 💴 Local payment app you can skip for this holiday

**PayPay:** its official signup requirements exclude overseas phone numbers and require a Japanese mobile number capable of SMS verification. A data-only travel eSIM does not supply that. Use your planned Suica, supported debit-card payments, and cash rather than building your payment plan around a PayPay account. [Official requirements](https://paypay.ne.jp/help/c0032/)

### ✅ Before leaving Chile

- [ ] Update the chosen apps and complete needed signups while phone verification is easy.
- [ ] Download translation languages and available map areas; save essential route screenshots separately.
- [ ] Add/test Suica and keep a backup payment method.
- [ ] Enable Safety tips alerts for your destinations.
- [ ] Test GO registration if you want a taxi fallback; review current visitor fees.
- [ ] Bookmark Visit Japan Web and SmartEX in Safari.
- [ ] Test offline access to Obsidian, flight/hotel confirmations, and the contacts card.
- [ ] Confirm how your Chilean phone number receives bank/SMS codes abroad without unexpected roaming costs.

'''
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Essentials-before-apps.md'))
p.write_text(s.replace(marker,section+marker,1))
main=v/'Japan Travel Guide 2027.md';m=main.read_text();needle='**Travel essentials:** [[Japan 2027 — Travel Essentials|🧳 Entry, luggage, arrival, and useful contacts]] — current official guidance and fields to complete before departure.'
assert needle in m
copy2(main,Path('/home/ivanaguilera/Work/japan-guide-update/Main-before-apps.md'))
main.write_text(m.replace(needle,needle+'\n\n**Phone setup:** [[Japan 2027 — Travel Essentials#📲 Apps to prepare on your iPhone|📲 Travel apps and local services]] — install priorities, signup limitations, and browser shortcuts.',1))
assert '## 📲 Apps to prepare on your iPhone' in p.read_text()
print('Added sourced iPhone app shortlist, Chile-specific signup limits, and predeparture setup checklist; linked from main guide.')
