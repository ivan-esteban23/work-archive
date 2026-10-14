from pathlib import Path
import re, json, hashlib
from urllib.parse import quote

ROOT=Path(__file__).parent
BACK=ROOT/'backup'
OUT=ROOT/'staged'
PREFIX='Korea 2026 — '
S={
'pus':('Gimhae Airport rail connections','https://www.airport.co.kr/gimhaeeng/cms/frCon/index.do?CONTENTS_NO=3&MENU_ID=110','Korea Airports Corporation','Undated live airport page','Line 2 transfer at Sasang; not door-to-door journey time.'),
'noodles':('Milmyeon menu on Busan city service','https://menu.busan.go.kr/shop/info/CD_SHP_001154','Busan Metropolitan City multilingual-menu service','Undated live menu','Milmyeon as wheat noodles; no certification of dietary suitability or future pricing.'),
'entry':('K-ETA official application guide','https://www.k-eta.go.kr/portal/guide/viewetaapplication.do','Ministry of Justice','Undated live page','Eligibility, advance approval, fee and processing; individual nationality still needs checking.'),
'arrival':('Official e-Arrival Card guide','https://www.e-arrivalcard.go.kr/portal/guide/eacGuide.do?locale=E','Ministry of Justice','Undated live page','Free declaration, submission window and required information.'),
'exempt':('Arrival-card exemption navigator','https://www.e-arrivalcard.go.kr/portal/guide/navigator.do?locale=E','Ministry of Justice','Undated live page','Valid K-ETA holders are exempt from arrival declarations; this does not establish K-ETA eligibility.'),
'emergency':('Seoul visitor safety','https://english.visitseoul.net/essential-Info-article/Safety/ENN012370','Seoul Tourism Organization','Older standing guidance','119 ambulance/fire; 112 police. Other old information on this page was not adopted.'),
'metro':('Seoul subway fares','https://english.seoul.go.kr/policy/transportation/modes-of-transport/subway/','Seoul Metropolitan Government','Fare effective 2025-06-28','Adult base fares and distance additions; not a quote for every route.'),
'arex':('Airport rail to Seoul','https://english.seoul.go.kr/service/entry/getting-to-seoul-from-incheon-airport/','Seoul Metropolitan Government','Undated live page','Express one-way fare and terminal-specific scheduled journey times.'),
'guard':('Gyeongbokgung guard ceremonies','https://www.kh.or.kr/cms/content/view/824','Korea Heritage Agency','Undated live page','Changing ceremony is distinct from gate-guard performance; schedule subject to cancellation.'),
'park':('Gyeongui Line Forest Park','https://english.seoul.go.kr/gyeongui-line-forest-park/','Seoul Metropolitan Government','2022 article','Mapo linear park geography; not current business hours.'),
'seoullo':('Seoullo 7017','https://english.visitseoul.net/tours/Must-See-Spots-at-Seoullo-7017/ENN022620','Seoul Tourism Organization','Older standing destination article','Elevated park near Seoul Station; not Gyeongui Forest Park.'),
'cable':('Songdo Marine Cable Car','https://visitbusanpass.com/attractions/_detail?id=GO0000000267','Visit Busan Pass','Undated live listing','Songdo–Amnam route; no exact-date operating guarantee.'),
'biennale':('Busan Biennale 2026 city announcement','https://www.busan.go.kr/eng/bsnews01/1752281','Busan Metropolitan City','2026-09-02','2026 dates, three venues, opening schedule and differing admission charges.'),
'bread':('Gyeongju Hwangnam bread','https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=179934','Korea Tourism Organization','Older food reference','Red-bean-filled pastry with egg in the dough; not butter bread.'),
'tax':('Comprehensive tax-refund guide','https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=489&vcontsId=248765','Korea Tourism Organization','Live guide; publication metadata indicates 2025','Qualifying purchases and distinction between immediate and departure refunds.'),
'health':('South Korea traveler health','https://wwwnc.cdc.gov/travel/destinations/traveler/none/south-korea','US CDC','Live destination guidance','Routine and itinerary-specific prevention; clinician must assess individual needs.'),
'medicine':('Controlled medicines brought into Korea','https://www.mfds.go.kr/brd/m_74/view.do?seq=43906','Ministry of Food and Drug Safety','Standing notice, originally 2020','Advance permit requirement for controlled substances; use current application procedure.'),
'drone':('Drone usage regulations','https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=177&vcontsId=1593140','Korea Tourism Organization','2026-09-04','Preflight checks and Drone One-Stop referral; not individual flight authorization.'),
'boan':('BOAN 1942 visitor listing','https://english.visitseoul.net/area/boan-1942/ENPk1cyet','Seoul Tourism Organization','Updated 2026-07-22','Bookshop/café complex in Tongui-dong; address and listed opening hours.'),
'waveon':('Waveon official location','https://m.waveoncoffee.com/layout/info.html','Waveon Coffee','Undated live business page','Gijang address; not a Gwangalli café or verified date-specific booking.'),
'cash':('Korean banknotes','https://www.bok.or.kr/eng/main/contents.do?menuNo=400112','Bank of Korea','Undated currency reference','Current banknote denominations.'),
'weather':('KMA short-range forecasts','https://www.weather.go.kr/neng/forecast/short-term.do','Korea Meteorological Administration','Dynamic forecast page','Where to check near-departure weather; no forecast for 27 October–2 November was verified.'),
'tunnel':('The Third Tunnel','https://ggtour.or.kr/en/?p=11&reqIdx=202311091631104968&viewMode=view','Gyeonggi Tourism Organization','Undated destination listing','Discovered in 1978; does not confirm a particular tour departure.'),
}
def cite(key):
 a=S[key]; return f'[{a[0]}]({a[1]})'
def link(n,label=None): return '[['+PREFIX+n+('|' + label if label else '')+']]'
def put(n,body):
 body='\n'.join(re.sub(r'\[\[([^\]]+)\]\]',lambda m:'[['+m.group(1).replace('|',r'\|')+']]',line) if line.startswith('|') else line for line in body.splitlines())
 (OUT/(PREFIX+n+'.md')).write_text('---\ncssclasses:\n  - korea-trip\n---\n# '+PREFIX+n+'\n\n'+link('Start Here','Dashboard')+' · '+link('Review and Sources 2026-10-07','Review and sources')+'\n\n'+body.strip()+'\n',encoding='utf-8')
status='**Reviewed 7 October 2026. Proposed trip: 27 October–2 November 2026, six nights. No reservation confirmation was present in the reviewed notes.**'

put('Practical Info',f'''{status}

## Entry documents

Passport nationality, age and any existing immigration status remain unconfirmed. Visa-free eligibility does **not** automatically mean K-ETA exemption. Check the exact passport and the exemptions applicable on the arrival date before buying nonrefundable travel. Do not use a blanket six-month passport rule: confirm destination, transit-country and airline requirements for the actual route.

Where K-ETA is required, obtain approval before boarding. The official fee is KRW 10,000 plus payment charges; processing is usually within 72 hours but can take longer. An approval is not a visa or a guarantee of admission. {cite('entry')}

The electronic arrival declaration is a separate, free process, submitted within three days before arrival using Korean time. Valid K-ETA holders are exempt from that declaration; other exemptions also exist. Use the official navigator for your circumstances. {cite('arrival')}; {cite('exempt')}

## Emergency and communication

**119: ambulance/fire. 112: police.** Save hotel names and addresses in Korean and keep an offline copy of travel insurance assistance details. Tourism assistance is a separate service and should not replace an emergency call. {cite('emergency')}

Choose a SIM/eSIM after checking phone compatibility, whether the package includes a Korean phone number, and its activation rules. Download maps or screenshots and confirmations before departure; no offline access has been configured by this review.

## Money and tax refunds

Banknotes are KRW 1,000, 5,000, 10,000 and 50,000; there is no KRW 20,000 banknote. Carry some smaller denominations. Foreign-card acceptance and ATM fees depend on your card and the machine: check international-network support and the fee screen. {cite('cash')}

At participating shops, eligible purchases of **KRW 15,000 or more** can qualify for a tourist tax refund. Immediate refunds happen at purchase; airport refunds are a different procedure. The official immediate-refund limits are under KRW 1 million per transaction and up to KRW 5 million in total purchases during the stay. Eligibility, export timing and unused-goods conditions apply. Keep the passport, receipts and goods accessible if departure inspection is needed. {cite('tax')}

No exchange rate in the old guide is a current quote. Record the rate, conversion fees and date alongside USD/CLP comparisons. International postage to Chile needs a separate service/price check; domestic convenience-store parcel services do not establish international delivery availability.

## Local dates and airport connections

All itinerary times are KST (UTC+9). For these proposed dates Santiago is UTC−3, so Korea is **12 hours ahead**. This was checked using the installed IANA time-zone database for America/Santiago and Asia/Seoul on both travel dates. Other parts of Chile may use different zones.

27 October means the proposed **arrival in Korea**, not necessarily departure from Santiago. Flight numbers, terminals, total duration and connecting airports are unconfirmed. Do not interpret a route sketch as an operating nonstop flight or a protected connection. Check through-ticketing, checked bags, transit requirements and any airport change against the actual airline itinerary.

## Respectful visits and navigation

Use the exact Korean name and branch address in a current navigation app. A search link is a search, not a verified entrance. Follow residential access signs, keep voices low and ask before photographing people or private interiors. Verify step-free access for each specific entrance and route rather than assuming that an entire city is accessible or inaccessible.

See {link('Transport')}, {link('Health preparation')} and {link('Korean phrasebook')}.
''')

put('Transport',f'''{status}

## Airport arrival

ICN terminal and arrival time must come from the flight confirmation. Allow immigration, baggage and walking time before choosing a train.

AREX Express to Seoul Station is listed at **KRW 13,000 per person one way**, with scheduled running times of **43 minutes from T1 / 51 minutes from T2**. These exclude waiting and airport formalities. Buy an Express ticket; do not assume a normal transit-card tap reserves an Express seat. The all-stop train is a separate option. {cite('arex')}

Seoul Station connects with subway Lines 1 and 4, AREX and Gyeongui–Jungang services; Line 2 requires a transfer. Choose the hotel route after confirming its address. Seoul's adult subway base fare is **KRW 1,550 by transport card / KRW 1,650 single-journey fare**, with additional distance charges; a refundable single-ticket deposit may be separate. {cite('metro')}

## Intercity legs to price and reserve

| Proposed date | Route | Status |
| --- | --- | --- |
| Fri 30 Oct | Seoul → Gyeongju, morning preferred | Train number, departure and fare unconfirmed |
| Sat 31 Oct | Gyeongju → Busan, afternoon preferred | Train number, departure and fare unconfirmed |

Use [KORAIL](https://www.korail.com/) to obtain current exact-date quotes, station names and seat availability. The old KRW 44,500 / 10,100 figures were not verified and are withdrawn as confirmed fares. Compare point-to-point tickets and a pass **per person**, using the same passenger category, class and travel days. Do not compare one pass against two travelers' tickets. No pass recommendation is final without those quotes.

The high-speed Gyeongju station is outside the historic center. Verify the selected station on the ticket and route it to the actual accommodation; do not navigate to a former downtown station. For planning, leave a generous transfer allowance rather than relying on the old ten-minute taxi promise. Bus number, frequency and fare remain to be checked in a current route planner.

## Busan departure

For a Seomyeon base, the rail route is subway Line 2 to Sasang, then Busan–Gimhae Light Rail to Airport station. The airport confirms the Line 2 connection at Sasang. {cite('pus')} Confirm first/last services and a door-to-door estimate shortly before travel. For planning, allow about 45–60 minutes from Seomyeon including the transfer, plus a disruption margin; this is an allowance, not a verified timetable. The Sasang–airport light-rail leg alone should not be assigned the old unverified 50-minute estimate.

Set hotel departure from the **actual flight time**, the airline's check-in/bag-drop deadline and the international/domestic terminal. A reasonable initial planning target for an international departure is arrival about three hours before the flight, subject to airline instructions. The old 13:00 flight and 11:30 hotel departure were placeholders and must not be used.

## City movement

Group Ikseon-dong/Insadong together; pair Gyeongui Forest Park with Hongdae/Yeonnam. Seochon is west of Gyeongbokgung. Deoksugung is by City Hall. {cite('park')}; {cite('seoullo')}

In Busan, Gamcheon/Nampo and Gwangalli/Millak are separate outings joined by a cross-city transfer. Haedong Yonggungsa belongs to an eastern Busan plan, not a quick extra before Gwangalli sunset. All specific travel times depend on the route, traffic, luggage and mobility.
''')

put('Bookings',f'''{status}

## Booking checklist

These are decisions to make, not reservations. No artificial booking deadline or assumed pickup time is retained.

- [ ] Confirm travelers, passport nationality and travel dates.
- [ ] Choose international flights; check transit rules and connection protection.
- [ ] Seoul: check-in 27 Oct, check-out 30 Oct — three nights.
- [ ] Gyeongju: check-in 30 Oct, check-out 31 Oct — one night.
- [ ] Busan: check-in 31 Oct, check-out 2 Nov — two nights.
- [ ] Quote both KTX legs and record chosen trains.
- [ ] Decide whether to book a DMZ tour; verify tunnel inclusion, passport instructions, pickup, physical requirements and cancellation/refund terms.
- [ ] Confirm dietary needs directly with any chosen restaurant.

## Reservations

| Item | Proposed date | Provider / confirmation | Total / paid / balance | Cancellation deadline with zone |
| --- | --- | --- | --- | --- |
| Flights into Korea | Arrival 27 Oct | — | — | — |
| Seoul, 3 nights | 27–30 Oct | — | — | — |
| DMZ, optional | 29 Oct | — | — | — |
| KTX Seoul → Gyeongju | 30 Oct | — | — | — |
| Gyeongju, 1 night | 30–31 Oct | — | — | — |
| KTX Gyeongju → Busan | 31 Oct | — | — | — |
| Busan, 2 nights | 31 Oct–2 Nov | — | — | — |
| Departure from PUS | 2 Nov | — | — | — |

**Confirmed spending recorded in this guide: none.** Blank cells mean unknown, not proof that nothing has been paid elsewhere. Add actual confirmations before marking anything booked. Record deposits within the total, not on top of it.

## Optional experiences and fallback

Hanbok rental is an optional experience, not a demonstrated saving over a palace admission ticket. Songdo Marine Cable Car is the cable-car option; Yongdusan Park is a separate place. {cite('cable')}

If the DMZ visit is cancelled, use a Seoul museum/café day and the Deoksugung area. The former Baegyangsa/Paju restaurant-and-bookshop route is withdrawn: its location and venue claims were not reliable. No substitute activity is reserved.

Keep confirmation PDFs or email exports linked here. Store passport numbers in an appropriate private location, not in a broadly shared guide export.
''')

amounts=[('Lodging, six nights',721),('Food',750),('Cafés',120),('Records, books, listening room and tea',135),('Intercity rail',79),('Local transit',95),('Optional DMZ tour',100),('Admissions / optional attractions',95),('Contingency reserve',300)]
put('Budget',f'''{status}

## Planning sheet — USD, assumed two travelers

These are the original **allowances**, retained for comparison, not current market quotes. Traveler count, room count and the working ceiling still need confirmation. International flights are excluded.

| Category | Original planned allowance | Actual spending recorded |
| --- | ---: | --- |
'''+''.join(f'| {n} | US${a:,} | — |\n' for n,a in amounts)+f'''
**Total: US$2,395 = US$2,095 allocated + US$300 reserve.** The arithmetic in the original total was correct. A US$2,500 ceiling leaves US$105; a US$3,000 ceiling leaves US$605. Neither ceiling has been newly approved.

## Corrections and gaps

- Actual rail spending and contingency are now blank. An estimate or reserve is not a payment.
- US$750 across seven calendar days is about **US$107.14 per day for the group**, not US$105. Arrival/departure days may be partial days.
- US$721 lodging is an allowance, not a checked six-night quote. The old blanket 5% tax assumption is not a verified property policy.
- The rail allowance of US$79 is **stale and needs repricing**. It is not guaranteed by regulation. Obtain both exact-date KORAIL fares before relying on the total.
- The local-transit allowance needs a new calculation using airport rail, hotel locations and the selected city routes. See {link('Transport')} for the verified AREX and Seoul subway figures.
- Named listening-room prices, a tea class and DMZ package prices in the earlier version were unverified. Request current prices and inclusions before allocating them.
- Clothing has no separate funded line. It must share the US$135 discretionary line or be an explicit additional allowance. The old US$145 and US$295 shopping claims are withdrawn.
- No live foreign-exchange rate was obtained. Keep original-currency quotes and conversion date/fees.

## Manual tracking

The old unbound input fields did not establish a reliable live calculation. This is now a plain table that remains readable in exports. Update it manually after each confirmation.

| Item | Currency | Total cost | Paid | Still owed | USD conversion and date |
| --- | --- | ---: | ---: | ---: | --- |
| Add confirmed item here | | | | | |

Recalculate **committed total + remaining estimates + unspent reserve** after each booking. Paid and outstanding amounts together form the committed total. Shopping decisions: {link('Shopping shortlist')}.
''')

put('Food',f'''{status}

## Dietary assumption to confirm

The old guide assumes **no pork, beef or chicken, but fish is allowed**. This is not the same as vegan or vegetarian. Confirm shellfish, eggs, dairy and any allergies separately before using the card below.

> 저는 돼지고기, 소고기, 닭고기를 먹지 않아요. 고기 육수도 먹지 않아요. 생선은 먹어도 괜찮아요.
>
> I do not eat pork, beef or chicken, or meat broth. Fish is okay.

Ask staff about the **broth, sauce and garnish**, not just visible meat. Removing the meat topping does not change a meat-based stock. An allergy requires a separate, explicit statement and cross-contact discussion.

## Food-name corrections

| Food | What to expect / what to ask |
| --- | --- |
| 밀면 — milmyeon | Busan-style wheat noodles; not radish rice cakes. Broth and toppings may contain meat, so check the actual restaurant recipe. |
| 황남빵 — Hwangnamppang | Gyeongju red-bean-filled pastry; its dough contains egg. Not butter bread. |
| 비빔밥 — bibimbap | Rice with toppings; request without meat and confirm stock/sauce. Egg may be included. |
| 빈대떡 — bindaetteok | Mung-bean pancake; pork may be mixed into the batter. |
| 국밥 / 해장국 — gukbap / haejangguk | Broad soup categories, often meat-based; not safe default vegetarian orders. |
| 쌈밥 — ssambap | Rice and leaf wraps with side dishes; meat and seafood vary by set. |
| 간장 — ganjang | Soy sauce. Ordinary soy sauce is not automatically fish broth; mixed sauces still need checking. |

The Hwangnam bread ingredients are documented by {cite('bread')}; wheat-noodle terminology is also shown on {cite('noodles')}. Other ingredient descriptions are general food explanations, not certification of a specific kitchen.

Kimchi may contain fish sauce or salted seafood. Halal describes a different dietary standard and does not mean meat-free. Temple-style branding alone does not verify a commercial restaurant's current menu.

## Meal planning

Choose one or two suitable restaurants near each day's actual route after checking the current menu and exact address. Keep a simple backup meal available, especially on the DMZ and rail days. The previous named restaurant list contained unsupported dish names, locations and dietary assurances, so none is retained as a verified dietary recommendation.

Research names preserved for identification only: Makdong Toseong, Eonnae Handaxe, Sajae, Jejugo, Sajung, Omma Temple, Ssanggye Sikdang, Hwangnam Gukbap, Sisters Naejangsan and Cactus Basil. Their exact identities, operating status, menus and claimed awards have **not** been established. Do not reserve or navigate using these English labels alone.

The earlier “sarangchae” meal description and the dish names “hobachui,” “maeuntak,” “mulbaegu” and “ganseul” were not reliable ordering advice and are withdrawn. Use an actual menu item and photo instead.

See {link('Korean phrasebook')} for short questions.
''')

put('Korean phrasebook','''**Reviewed 7 October 2026.** Show the Hangul if pronunciation is difficult. Dietary phrases express the guide's provisional fish-allowed preference, not an allergy declaration.

| Korean | Meaning |
| --- | --- |
| 안녕하세요. | Hello. |
| 감사합니다. | Thank you. |
| 죄송합니다. | Sorry / excuse me. |
| 영어 하세요? | Do you speak English? |
| 천천히 말씀해 주세요. | Please speak slowly. |
| 화장실이 어디예요? | Where is the toilet? |
| 이거 얼마예요? | How much is this? |
| 카드로 결제할 수 있어요? | Can I pay by card? |
| 따로 계산해 주세요. | Please charge us separately. |
| 같이 계산해 주세요. | Please put these on one bill. |
| 여기서 먹을게요. | I will eat here. |
| 포장해 주세요. | Please pack it to take away. |
| 돼지고기, 소고기, 닭고기는 빼 주세요. | Please leave out pork, beef and chicken. |
| 고기 육수가 들어가요? | Does it contain meat broth? |
| 생선은 먹어도 괜찮아요. | Fish is okay for me to eat. |
| 물 주세요. | Water, please. |
| 예약했어요. | I have a reservation. Use only after actually booking. |
| 이 주소로 가 주세요. | Please take me to this address. |
| 여기서 세워 주세요. | Please stop here. |
| 괜찮아요. 감사합니다. | No, thank you / I am okay, thank you. |
| 좀 지나갈게요. | Excuse me, I am coming through. |
| 도와주세요! | Please help! |
| 구급차를 불러 주세요. | Please call an ambulance. |
| 경찰을 불러 주세요. | Please call the police. |
| 병원에 가야 해요. | I need to go to a hospital. |

## Useful words

생선 fish as food · 해산물 seafood · 문어 octopus · 갑오징어 cuttlefish · 육수 broth · 고기 meat · 병원 hospital · 약국 pharmacy · 의사 doctor.

여기서요? means “here?”; it is not “where?” 세탁 is washing/laundry; 드라이클리닝 specifically means dry cleaning. 간선 is not a word for pollock.

## Prices

천 원 = KRW 1,000 · 천오백 원 = KRW 1,500 · 오천 원 = KRW 5,000 · 만 원 = KRW 10,000 · 이만 원 = KRW 20,000 (an amount, not a banknote denomination).

Use digits on the phone to confirm a price. Regional speech and noisy rooms can make spoken numbers difficult; do not rely on the old invented pronunciation shortcuts.
''')

put('Health preparation',f'''{status}

## Before departure

- [ ] Review routine vaccines and itinerary-specific advice with a travel-health clinician; take the actual route, including the optional DMZ visit.
- [ ] Check travel insurance coverage, assistance contact and relevant medical exclusions.
- [ ] Carry medication in original packaging with prescriptions or a clinician's letter where appropriate.
- [ ] Check every medication's active ingredient against Korean import requirements.

CDC advice is individualized by exposure and destination within Korea; do not read this short city itinerary as automatically requiring or excluding malaria prevention or other travel vaccines. {cite('health')}

Controlled medicines can require **advance MFDS permission regardless of nationality**. A foreign prescription alone does not establish import permission. Use the current MFDS process and confirm the medicine and quantity rather than copying old processing-time promises. {cite('medicine')}

## During travel

Keep essential medication in hand luggage. On a long flight, move periodically when safe and follow any personal medical advice. Adjust sleep to the actual itinerary; the former precise jet-lag schedule and assumed total flight duration were not supported.

Pack comfortable shoes, layers, a small first-aid kit appropriate to you, and usual prescriptions. Ask a pharmacist or clinician about medicines unfamiliar to you rather than using a generic travel checklist as dosing advice.

## Food and access

Use {link('Food')} and confirm allergies separately. Fish-allowed eating does not establish shellfish tolerance. Consider steep paths, steps and confined-space walking when deciding on Gamcheon, temple visits and the tunnel; ask the operator about the specific route and assistance available.

## If you need help

**Ambulance/fire: 119. Police: 112.** Provide your location and keep the Korean hotel address available. For nonurgent illness, your insurer or accommodation can help locate an appropriate clinic; that does not guarantee language support or coverage. {cite('emergency')}
''')

put('Weather and Packing',f'''{status}

## Weather status

**No exact-date weather forecast for this trip was verified on 7 October.** The previous daily temperatures and guaranteed dry-weather claims were removed. Seasonal expectations are not a forecast. Check Seoul, Gyeongju and Busan separately in the days before each visit. {cite('weather')}

For planning, prepare for cool evenings, daytime temperature changes and wind by the coast, with rain possible. Do not assume zero typhoon risk or that October is Seoul's driest month. Check official alerts before outdoor or marine activities.

## Packing checklist

- [ ] Light layers plus a warm outer layer for evenings.
- [ ] Rain shell or compact umbrella and a camera rain cover.
- [ ] Comfortable walking shoes with grip; socks and a spare dry layer.
- [ ] Phone charger, compatible adapter, power bank and cables.
- [ ] Camera batteries/cards; check airline battery limits for the actual flight.
- [ ] Passport, entry documents, insurance and offline confirmations.
- [ ] Medication and any required import permit.
- [ ] A small day bag; leave luggage capacity for planned purchases.

Check laundry availability at the chosen accommodation. Do not assume every property offers next-day service. Protect a reserve rather than packing or purchasing for a precise forecast that does not yet exist.

## Rain and low-energy alternatives

Seoul: a museum or confirmed café near the hotel. Gyeongju: a museum/café block, subject to current opening details. Busan: the Biennale is a possible indoor replacement during its verified dates, but the venues are spread out and admissions differ; see {link('Itinerary')}. Cable cars are not a guaranteed bad-weather alternative.
''')

put('Autumn Foliage',f'''{status}

## What is established

Late October and early November are the proposed autumn travel window. **This review did not establish a reliable 2026 peak-foliage forecast for the individual stops.** The earlier exact peak dates and promises that particular trees would remain green are withdrawn. Tree species, elevation, recent temperatures, wind and rain can change what is visible.

Use current local photographs and official weather information close to the visit. {cite('weather')} provides weather checks, not a foliage guarantee.

## Flexible viewing choices

| Base | Possible place | Planning condition |
| --- | --- | --- |
| Seoul | Gyeongbokgung / Seochon, Deoksugung surroundings | Fit the existing city days; check opening and access rules. |
| Seoul | Seoul Forest / Seongsu | Optional replacement block, not an extra squeezed into the DMZ day. |
| Gyeongju | Historic center and Bulguksa | Keep architectural and historical interest even if color is limited. |
| Busan | Temple or park visit | Choose by observed conditions and route, not a claimed later guaranteed peak. |

Gyeongui Line Forest Park is a ground-level former railway corridor in Mapo, useful with Hongdae/Yeonnam. Seoullo 7017 is the elevated park near Seoul Station. They are different places. {cite('park')}; {cite('seoullo')}

## Limits on extra excursions

Do not add distant mountain trips to a six-night itinerary just to chase an unverified forecast. The old Baegyangsa/Paju fallback is withdrawn. Seoraksan is in Gangwon, not a southern mountain near Busan. Tongiljeon is not part of the compact Hwangnidan-gil café walk.

Moving arrival from 17 to 27 October is a **ten-day** change. It does not by itself establish better leaf color. Any festival needs a separately confirmed 2026 schedule; the proposed Jeongdong event dates were not verified.
''')

put('Photography and Filming',f'''{status}

## Creative priorities

Keep the original interests: autumn details, Wolji reflections, street scenes, books/records and a short travel film. These are suggested subjects, not reasons to rush a transfer or ignore access restrictions.

| Day | Suggested subject | Practical adjustment |
| --- | --- | --- |
| 27 Oct | Ikseon-dong / Insadong details | Keep arrival afternoon flexible; avoid photographing private interiors without consent. |
| 28 Oct | Palace scale, Seochon textures, Hongdae browsing | Separate palace morning from the western shopping district. |
| 29 Oct | DMZ permitted areas; Deoksugung surroundings later | Ask the guide where cameras may be used; no interior tunnel shooting plan. |
| 30 Oct | Historic Gyeongju and Wolji reflections | Arrive before the desired evening light; 20:30 is night, not dusk. |
| 31 Oct | Bulguksa exterior and Nampo street scenes | Leave station/luggage margin; Seokguram is not a rushed mandatory addition. |
| 1 Nov | Gamcheon details and Gwangalli waterfront | Allow a cross-city transfer; be at the waterfront before sunset. |
| 2 Nov | A few departure details | Airport timing takes priority. |

Exact sunrise/sunset and venue lighting times have not been verified. Look them up for the date and location shortly before the outing. Gwangalli faces the Gwangan Bridge; do not label it “Haeundae Bridge.”

## Small kit

Carry the camera you will actually use, a versatile lens, charged spare batteries and cards, a cleaning cloth and weather protection. A fast lens can help with evening scenes. A tripod is optional and only useful where permitted; do not block paths or rest equipment on fragile heritage surfaces.

## Access and photography

Respect posted restrictions and staff instructions at temples, museums, military sites and businesses. Remove the former Seokguram interior/Buddha-face shot instruction; plan exterior photography and verify restrictions on site. Do not presume a tourist ticket grants permission for professional filming, tripods, lighting or drones.

Drone registration, pilot qualifications, airspace permission and filming restrictions are different checks. This guide does not authorize flight or give a blanket weight-based exemption. Use [Drone One-Stop](https://drone.onestop.go.kr/) and check the exact coordinates, aircraft and intended activity; the old unsupported penalty amounts and airspace percentages are withdrawn. {cite('drone')}

## Simple film sequence

For each day, aim for one wide establishing view, two medium scenes and two small details. Record a little ambient sound where appropriate, and write the location/date before forgetting. Photograph people respectfully and ask before a close portrait. Back up files when practical; no backup has been configured by this review.
''')

put('Shopping shortlist',f'''{status}

## Set one total

The budget has **US$135 total for records, books, listening-room visits and tea**. Clothing is not separately funded. Either share that line, reduce another line or explicitly increase the trip budget. Do not combine the old contradictory US$145, US$150 and US$295 ceilings.

Priorities retained from the draft: one vintage garment if a good fit, one record, one book, and small meaningful gifts. These are optional interests, not confirmed purchases or minimum spend.

## Before buying

- Inspect condition, measurements and any damage; second-hand does not mean guaranteed mint condition.
- For records, inspect the disc and sleeve and ask to listen where possible.
- Check the book's language and whether you actually want it.
- Compare full cost, luggage space/weight and the return policy.
- Verify the shop/branch and hours before crossing the city; see {link('Cafés and Shops')}.

Do not count a possible tax refund until the transaction qualifies. Current rules are in {link('Practical Info')}. International postage availability and pricing are unverified; a domestic courier estimate is not a Chile shipping quote.

## Purchase record

| Date | Item / shop | Original currency and amount | Refund, if received | Budget category |
| --- | --- | --- | --- | --- |
| | | | | |

No purchases were recorded in the source note.
''')

# Preserve each named shop idea, but not unsupported operating claims or fake ratings.
names=[]
for line in (BACK/(PREFIX+'Cafés and Shops.md')).read_text().splitlines():
 if line.startswith('|'):
  cell=line.split('|')[1].strip()
  if cell.startswith('**'):
   names.append(cell.replace('**','').replace('⭐','').strip())
put('Cafés and Shops',f'''{status}

## Sources checked

**BOAN 1942 / Boan Books, Seoul:** the official city visitor listing identifies the cultural complex, bookstore and café at **33 Hyoja-ro, Jongno-gu**, in Tongui-dong/Seochon. It lists **12:00–18:00, closed Mondays** (listing updated 22 July 2026). This is a useful candidate for 28 October after the palace; confirm the specific bookshop's hours before travel. {cite('boan')}

**Waveon Coffee, Busan:** the operator lists **286 Haemaji-ro, Jangan-eup, Gijang-gun**. It is an eastern coastal excursion, not a vintage villa next to Gwangalli. Keep it off the default Gamcheon–Gwangalli day. No current price or trip-date opening guarantee was verified. {cite('waveon')}

## Research inbox — identification and availability still needed

The following names are retained from the old guide so useful leads are not lost. **This list does not verify existence under that spelling, exact branch, location, price, menu, hours, accessibility or rating.** None should anchor a journey until matched to a current operator listing and Korean address. Some old names may be mistranscriptions or conflations.

'''+ '\n'.join('- '+n for n in names if n not in ['Boan Books','Waveon Coffee'])+f'''

The previous Millak cluster was not established as a walkable group. Check each address independently; Millak-dong is **민락동**. Brand spellings can differ from district spellings. The proposed tea class at Bitgguri was not verified. An English title such as “Music Complex” must be matched to an actual branch before use.

## How to promote a candidate into the itinerary

Record the exact Korean/business name, street address, operator URL, date checked, opening day/hours, any minimum spend, and reservation requirements. Then add it to the day's existing neighborhood block. A search result or a Google search link alone is not evidence that the old price and description were correct.

All original descriptions and search links are preserved in the review backup outside the active vault; the review note gives its location.
''')

days=[
('2026-10-27','Tue','Seoul arrival','Seoul','Arrive at ICN, clear formalities and travel to the confirmed hotel. Leave bags or check in according to property policy. If energy permits, keep the afternoon to Insadong, Ikseon-dong and a short Cheonggyecheon walk. Eat nearby and rest.','Airport terminal, flight time and hotel remain unconfirmed. Skip extra districts after a delayed arrival. Gyeongui Forest Park belongs to the Hongdae day, not this walk.'),
('2026-10-28','Wed','Palace, Seochon and Hongdae','Seoul','Start with Gyeongbokgung, then lunch and a Seochon bookshop/café block. BOAN 1942 is a sourced candidate, subject to rechecking. Rest or transfer west for Hongdae/Yeonnam and the Gyeongui Forest Park area. Limit shopping to a few confirmed places.','The guard-changing ceremony is listed at 10:00 and 14:00; confirm cancellation notices. Do not confuse it with other guard performances. Deoksugung is a separate City Hall visit, moved to the next day.'),
('2026-10-29','Thu','Optional DMZ and central Seoul','Seoul','If booked, follow the tour operator’s actual meeting time and passport instructions. Keep the afternoon flexible because access and return timing can change. After resting, consider Deoksugung and its surrounding streets, subject to palace hours.','No tour is booked. Confirm Third Tunnel inclusion and walking demands; do not assume JSA access. If cancelled, use a Seoul museum/café day. No Jeongdong festival is assumed.'),
('2026-10-30','Fri','Seoul to Gyeongju','Gyeongju','Take a confirmed morning train, transfer from the high-speed station and leave luggage at the accommodation by arrangement. Walk a compact historic-center route: Hwangnidan-gil, Daereungwon surroundings and Cheomseongdae as time permits. Make Wolji the evening priority.','Train time and admission details need confirmation. Get to Wolji before your desired evening light and verify last entry. The former 20:30 “dusk” description was wrong. Keep the museum optional rather than forcing every site into the afternoon.'),
('2026-10-31','Sat','Bulguksa and onward to Busan','Busan','Visit Bulguksa only if current opening times and the selected afternoon train leave adequate margin. Otherwise enjoy the historic center. Collect luggage, travel to Busan and check in. If time allows, explore Nampo/Gwangbok-dong and Yongdusan Park.','Seokguram is an optional alternative requiring extra travel time, not a quick obligatory add-on. Songdo’s cable car is a separate excursion. Neither is called “Yongdusan cable car.” Avoid assuming Halloween crowd conditions.'),
('2026-11-01','Sun','Gamcheon and Gwangalli','Busan','Visit Gamcheon in the morning, then lunch/rest around Nampo or the accommodation. Allow a substantial cross-city transfer to Millak/Gwangalli in time for the waterfront before sunset. Choose at most one café with a verified address.','Haedong Yonggungsa/Haeundae would be an alternative eastern Busan day, replacing Gamcheon. A Biennale visit is another replacement, not an extra full block. No ten-minute Gamcheon-to-Millak transfer is assumed.'),
('2026-11-02','Mon','Departure from Busan','—','Check out and travel to Gimhae Airport according to the actual flight confirmation. Keep shopping or coffee local and optional only after airport timing is established. Retain receipts and allow time for any applicable tax-refund process.','Flight time and terminal are unknown. Work backward from airline deadlines; do not use the earlier 13:00 departure or 11:30 hotel-leaving placeholder. Confirm baggage, connections and transit documents.')]
it=f'''{status}

## Route and assumptions

Seoul **3 nights** (27–29 Oct) → Gyeongju **1 night** (30 Oct) → Busan **2 nights** (31 Oct–1 Nov), departure 2 Nov. Two travelers and the fish-allowed/no-meat diet remain draft assumptions awaiting confirmation. Activities and timings below are planning suggestions, not reservations.

| Date | Day | Plan | Overnight |
| --- | --- | --- | --- |
'''
for date,dow,title,night,plan,condition in days:
 it+=f'| {date} | {dow} | {link("Pocket "+date,title)} | {night} |\n'
for i,(date,dow,title,night,plan,condition) in enumerate(days,1):
 it+=f'\n## Day {i} — {date}: {title}\n\n{plan}\n\n**Keep flexible:** {condition}\n'
it+=f'''
## Verified anchors and sources

Gyeongbokgung guard-changing schedule: {cite('guard')}. BOAN 1942 address and listed hours: {cite('boan')}. Correct park geography: {cite('park')} and {cite('seoullo')}. Songdo cable-car identity: {cite('cable')}.

**Busan Biennale option:** the city announces 29 August–1 November 2026, normally 10:00–18:00 except Mondays, at Busan Museum of Contemporary Art, Space OneZ and the former Busan Nam High School. The museum adult admission is KRW 16,000; the other two venues are free. Choose a venue and check last-entry/transport details. It could replace part of 31 October or 1 November, not 2 November. {cite('biennale')}

Palace admission waivers, night events, Gyeongju opening times and exact-date train/tour availability still need current operator confirmation. Hanbok rental should be chosen for the experience, not described as cheaper than paying normal palace admission. No exact foliage peak or travel-date forecast is guaranteed.

See {link('Bookings')} before treating any item as committed, and {link('Budget')} for allowances awaiting quotes.
'''
put('Itinerary',it)
for i,(date,dow,title,night,plan,condition) in enumerate(days,1):
 put('Pocket '+date,f'''**Day {i} · {dow} {date} · {title}**

Proposed plan, reviewed 7 October 2026. Overnight: **{night}**. Reservation details must be taken from {link('Bookings')}.

## Main plan

{plan}

## Before leaving

{condition}

- [ ] Check weather, route and current opening/access notices.
- [ ] Save the exact hotel and destination addresses.
- [ ] Carry payment options, charged phone, layers and applicable travel documents.

**119 ambulance/fire · 112 police.** {cite('emergency')}

Diet card: {link('Food')} · route details: {link('Itinerary')} · transport: {link('Transport')}.
''')
put('Daily Pocket Cards','**Proposed daily plans, reviewed 7 October 2026.** These cards summarize the corrected itinerary; flight, hotel and tour times remain unconfirmed.\n\n'+ '\n'.join('- '+link('Pocket '+d,f'{d} ({w}) — {t}') for d,w,t,*_ in days)+'\n\nOpen each card and save a local/offline copy if needed. No device download or reminder was configured.\n')

put('My Five Things',f'''**Proposed priorities retained from the original draft; these have not been newly confirmed by the traveler.** Use them to choose between optional activities, rather than treating all five as obligations.

## 1. Wolji reflections

Protect some evening time in Gyeongju on 30 October, subject to entry and lighting details. Lodging near the historic center helps, but an exact address is needed to judge the return walk.

- [ ] Done
- Photo / one sentence: _______________

## 2. An hour listening to music

Choose a verified listening room and current price from the research leads in {link('Cafés and Shops')}. No venue or time is reserved. Use a restful city block instead of adding a long detour.

- [ ] Done
- Record played / memory: _______________

## 3. One vintage piece

Browse during the Hongdae block if energy allows. Buy for fit and condition, within the single ceiling in {link('Shopping shortlist')}. There is no obligation to buy.

- [ ] Done
- Item / shop: _______________

## 4. The Third Tunnel, if the tour operates

This is an optional tour decision. The tunnel was **discovered in 1978**; the old claim that it was constructed that year and “cut north from North Korea” was inaccurate. Confirm physical access requirements and permitted photography with the operator. {cite('tunnel')}

- [ ] Done
- One sentence: _______________

## 5. A memorable meal

Pick a real current menu compatible with the confirmed diet. The earlier restaurant and dish claims do not establish a safe or available meal. Use {link('Food')} to ask about ingredients.

- [ ] Done
- Restaurant / dish / memory: _______________

## If plans compete

Choose the experience that matters most that day and leave adequate travel/rest time. Good light, a closed shop or fatigue may reasonably change these priorities. Keep Korea memories here rather than recording them in the Japan guide.
''')

# Preserve map configuration and inherited coordinates, correcting unsupported verification claims.
mv=(BACK/(PREFIX+'Map View.md')).read_text()
blocks=re.findall(r'```mapview\n(.*?)\n```',mv,re.S)
pins=mv.split('## 📍 Pin directory',1)[1].split('## ⚠️',1)[0]
pins=re.sub(r'Each line.*?\n','Each location below is inherited from the old guide and is an approximate orientation pin, not a re-surveyed entrance.\n',pins,count=1)
pins=re.sub(r' ✓ (?:~)?[\d,]+ m','',pins)
pins=pins.replace(' ~ single source',' (inherited reference)')
pins=pins.replace('Hongik University Station — Hongdae vintage loop','Hongik University campus — not the subway station')
pins=pins.replace('query=천문대+경주','query=첨성대+경주')
pins=pins.replace('query=월지연못+경주','query=동궁과월지+경주')
put('Map View','''**Reviewed 7 October 2026.** Existing map blocks and coordinates are retained for orientation. The prior claim that every point had been checked against two independent sources is not substantiated by this review and has been removed. No live Obsidian rendering or offline tiles were tested.

A coordinate may mark a campus, park or airport center, not its entrance. Confirm the name and address in a current route planner. The Hongik point is the university campus, not Hongik University Station. Gyeongju station requires special care because of the former downtown station.

'''+ '\n\n'.join('## '+n+'\n\n```mapview\n'+b+'\n```' for n,b in zip(['Seoul','Gyeongju','Busan','Airports and rail'],blocks))+'\n\n## Pin directory\n'+pins)

places={'Seoul':[('Gyeongbokgung','경복궁 서울'),('Seochon / BOAN 1942','보안1942 효자로33'),('Deoksugung','덕수궁 서울'),('Ikseon-dong','익선동 서울'),('Insadong','인사동 서울'),('Gyeongui Forest Park, Yeonnam section','경의선숲길 연남동'),('Seoullo 7017','서울로7017'),('Hongik University Station','홍대입구역'),('Seoul Forest','서울숲'),('Seoul Station','서울역')],
'Gyeongju':[('Gyeongju high-speed station — verify ticket','경주역 건천읍'),('Hwangnidan-gil','황리단길 경주'),('Daereungwon','대릉원 경주'),('Cheomseongdae','첨성대 경주'),('Donggung Palace and Wolji Pond','동궁과월지 경주'),('Woljeongyo','월정교 경주'),('Bulguksa','불국사 경주'),('Seokguram, optional','석굴암 경주')],
'Busan':[('Busan Station','부산역'),('Gamcheon Culture Village','감천문화마을 부산'),('Nampo / Gwangbok-dong','광복동 부산'),('Yongdusan Park','용두산공원 부산'),('Songdo Marine Cable Car, separate outing','송도해상케이블카 부산'),('Gwangalli Beach','광안리해수욕장'),('Millak-dong','민락동 부산 수영구'),('Jeonpo-dong','전포동 부산'),('Haedong Yonggungsa, alternative eastern day','해동용궁사 부산'),('Waveon, separate Gijang trip','웨이브온커피 부산 기장군 해맞이로286'),('Gimhae Airport','김해국제공항')],
'Optional DMZ tour area':[('Imjingak','임진각 파주'),('Freedom Bridge','자유의다리 파주 임진각'),('Dora Observatory','도라전망대 파주')]}
maps='**Reviewed 7 October 2026.** These links perform name searches. They do not verify a business, entrance, operating hours or unrestricted access. Compare Korean names and street addresses before following directions. DMZ stops depend on the selected authorized tour.\n'
for region,rows in places.items():
 maps+='\n## '+region+'\n\n'
 for title,q in rows: maps+=f'- [{title}](https://www.google.com/maps/search/?api=1&query={quote(q)}) — {q}\n'
maps+='\nUnverified restaurant and shop search pins were removed from the active directory; the leads remain in '+link('Cafés and Shops')+'. See '+link('Map View')+' for inherited orientation coordinates.\n'
put('Maps',maps)

allnames=[p.stem[len(PREFIX):] for p in BACK.glob('*.md')]
put('Start Here',f'''{status}

The review corrected practical errors and removed unsupported precision. **Read {link('Review and Sources 2026-10-07','the review and source register')} for what changed and what still needs checking.** All 25 original notes were backed up before editing.

## Proposed route

| Base | Check-in | Check-out | Nights |
| --- | --- | --- | ---: |
| Seoul | 27 Oct | 30 Oct | 3 |
| Gyeongju | 30 Oct | 31 Oct | 1 |
| Busan | 31 Oct | 2 Nov | 2 |

Total: **six nights / seven calendar days**. These are Korean local dates. Flights and arrival/departure times remain unknown. Two travelers and no meat but fish allowed are inherited assumptions awaiting confirmation.

## Next decisions

- Confirm dates, traveler count, passport nationality and dietary details.
- Resolve entry/transit requirements and choose flights.
- Quote the six nights and both rail legs; decide whether the optional DMZ visit matters enough to book.
- Reprice the US$2,395 original allowance before treating it as a realistic current total.
- Verify any shop, restaurant or event before assigning it a timed slot.

## Guide index

'''+ '\n'.join('- '+link(n) for n in allnames if n!='Start Here' and not n.startswith('Pocket '))+f'''

## Status and provenance

No booking, payment, business contact, account change or ChatGPT Project upload was made by this review. The corrected local notes and {link('Session Recap 2026-10-07')} are the continuation point. Weather/foliage forecasts, exact-date tickets and individual shop availability remain separate checks.
''')

review=f'''**Audit date: 7 October 2026. Scope: all 25 existing Korea 2026 notes, including seven pocket cards and both map notes.**

## Main corrections

| Area | Correction |
| --- | --- |
| Emergency | Medical/fire number corrected to 119; police remains 112. |
| Entry | Removed blanket K-ETA exemption and universal six-month passport claim; separated arrival declaration from travel authorization. Passport-specific decision remains open. |
| Airport/transit | AREX and Seoul metro base fares updated; unverified KTX prices and false pass comparison withdrawn. Flight times and implausibly short transfers no longer presented as facts. |
| Geography | Seoullo separated from Gyeongui Forest Park; Seochon/Deoksugung routes corrected; Songdo cable car separated from Yongdusan; Waveon placed in Gijang. |
| Itinerary | Rebalanced Seoul neighborhoods and Busan east/west travel. Removed unsupported festival assumptions, false booked labels, and the unreliable DMZ fallback. |
| Budget | US$2,395 total confirmed arithmetically. Removed estimates from actual spending; reconciled discretionary allowance and marked stale prices. |
| Food/language | Corrected mistranslations, dietary assumptions and dish descriptions; withdrew unsupported restaurant/dietary claims. |
| Weather/foliage | Removed fabricated daily precision and guaranteed leaf-color claims. |
| Safety/photography | Replaced unsupported medicine/drone rules with scoped official guidance; removed inappropriate interior/tunnel shooting instructions. |
| Maps | Fixed Hongik campus-versus-station label and Korean search terms; removed unsupported coordinate-verification badges. Existing coordinates remain approximate and were not all re-surveyed. |

## What remains unverified

Dates/traveler count/diet are retained as **assumptions** because the clarification is unanswered. Passport nationality is needed for a personal entry determination. Current KTX prices, lodging totals, tour availability, individual shops/menus and Gyeongju admissions/hours are not confirmed. No 2026 spot-specific foliage forecast, Jeongdong festival date, JSA access or return-flight itinerary was established.

Some official palace and Gyeongju pages returned navigation without the relevant facts in readable text; other Korea Tourism Organization destination pages and the airport-light-rail PDF failed to open. Those search snippets were not promoted to confirmed prices or opening hours. K-ETA exemption notices on certain embassy sites failed to load; no country exemption was inferred from them.

The shop inbox preserves candidate names, with unsupported descriptive details removed. Lack of verification does not prove that a business does not exist. Dynamic transport/venue details should be checked again close to travel.

## Source register

All sources below were opened during this audit on **2026-10-07**. Publication dates are reported only where identifiable; search crawl dates are not treated as publication dates. Official pages may change after this review.

| Source | Publisher | Publication/update context | Supported claim and limit |
| --- | --- | --- | --- |
'''
for k,(title,url,pub,dated,claim) in S.items(): review+=f'| [{title}]({url}) | {pub} | {dated} | {claim} |\n'
review+=f'''
## Local calculations and planning judgments

The night count and weekdays were checked against the 2026 calendar. Budget lines sum to 2,395; excluding the reserve gives 2,095. The Santiago/Korea offset was calculated with the installed IANA time-zone database. Proposed neighborhood grouping, rest periods and airport buffers are planning judgments, not operator guarantees.

## Backup and audit trail

Original notes: `/home/ivanaguilera/Work/korea-guide-review-20261007/backup/`.

Original SHA-256 manifest: `/home/ivanaguilera/Work/korea-guide-review-20261007/original-hashes.json`.

Prepared revisions and source metadata: `/home/ivanaguilera/Work/korea-guide-review-20261007/`.

The original files were preserved outside the active vault so unsupported old advice is not mixed into the corrected guide. Filenames and the Korea styling class were retained. Map configuration was retained; no Obsidian settings were changed. No reservations were changed.
'''
put('Review and Sources 2026-10-07',review)
put('Session Recap 2026-10-07',f'''User requested factual review, web research and corrections to the South Korea guide.

Reviewed 25 existing notes and prepared corrected versions plus the review/source note and this recap. The route remains provisional: Seoul 3 nights, Gyeongju 1, Busan 2, 27 October–2 November 2026. No confirmations or completed journal entries were present in the reviewed notes. Full originals are preserved in the task backup.

Start with {link('Review and Sources 2026-10-07')} and {link('Start Here')}. The next dependencies are traveler/passport/diet confirmation, actual flights and lodging, exact-date KTX quotes, a DMZ decision, and checking selected shops. Do not restore old prices, weather predictions or bookings from archived text.

No account, plugin setting or Japan guide was changed. No booking, payment or external upload was made. Existing map coordinates were retained as approximate; rendering in Obsidian was not tested.
''')

(ROOT/'sources.json').write_text(json.dumps({k:dict(title=v[0],url=v[1],publisher=v[2],date_context=v[3],supports=v[4],checked='2026-10-07') for k,v in S.items()},ensure_ascii=False,indent=2))
assert len(list(OUT.glob('*.md')))==27
assert sum(x[1] for x in amounts)==2395
print('Prepared',len(list(OUT.glob('*.md'))),'notes; source records:',len(S))
