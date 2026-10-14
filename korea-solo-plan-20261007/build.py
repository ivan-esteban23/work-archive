from pathlib import Path
import json,re,hashlib

root=Path('/home/ivanaguilera/Work/korea-solo-plan-20261007')
backup=root/'backup'; staged=root/'staged'
docs={p.name:p.read_text() for p in backup.glob('*.md')}
prefix='Korea 2026 — '
def note(title,body):
    docs[prefix+title+'.md']='---\ncssclasses:\n  - korea-trip\n---\n# '+prefix+title+'\n\n[[Korea 2026 — Start Here|Dashboard]] · [[Korea 2026 — Solo Plan|Solo plan]]\n\n'+body.strip()+'\n'
def insert(title,body):
    name=prefix+title+'.md';s=docs[name]; pos=s.index('\n\n',s.index('# '))+2
    docs[name]=s[:pos]+body.strip()+'\n\n'+s[pos:]

status='**Updated 7 October 2026: one traveler, flexible dates, nothing booked (confirmed by you).** The old 27 October–2 November schedule is a previous draft. Use [[Korea 2026 — Solo Plan]] for the current recommendations; trip length, departure airport, passport and dietary details remain open.'
old='**Reviewed 7 October 2026. Proposed trip: 27 October–2 November 2026, six nights. No reservation confirmation was present in the reviewed notes.**'
for name,s in list(docs.items()):
    if 'Session Recap' in name or 'Review and Sources' in name: continue
    docs[name]=s.replace(old,status)

note('Solo Plan',r'''
**Research: 7 October 2026. Confirmed: solo traveler; dates flexible; nothing booked.** Autumn 2026 remains a working scenario, not a newly selected season. Passport, departure airport, total budget, available leave and diet are awaiting your answers.

## Recommendation and alternatives

My recommendation is **10 days / 9 nights in Korea: Seoul 4 → Gyeongju 2 → Busan 3**. Two nights in Gyeongju protect one full sightseeing day and two chances at evening photography. Three Busan nights give you two full days without combining every district into one cross-city outing. International travel days are additional.

| Time in Korea | Allocation | Tradeoff |
| --- | --- | --- |
| 7 days / 6 nights | Seoul 4 + Busan 2 | My shorter-trip choice: omit Gyeongju rather than rush three bases. |
| 10 days / 9 nights | Seoul 4 + Gyeongju 2 + Busan 3 | Recommended balance; DMZ is optional. |
| 12 days / 11 nights | Seoul 5 + Gyeongju 2 + Busan 3 + Seoul 1 | More browsing time and a final Seoul night if returning through ICN. |

**Candidate Korean-local window A: 27 October–5 November 2026**, used for the hotel searches only. **Window B: 3–12 November**, a later comparison window, not hotel-priced here. Both are planning choices. KTO recommends spring/autumn for walking and advises autumn layers. Its 8 September 2026 foliage article, crediting Weatheri, forecasts Bukhansan peak around 4 November, with weather-dependent dates; that is not a forecast for individual Seoul streets or Gyeongju trees. [Seasonal guidance](https://english.visitkorea.or.kr/svc/contents/infoBscView.do?vcontsId=140636) · [2026 foliage forecast](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1593230)

Choose dates from the combination of usable nights, flight routing, accommodation totals and leave—not foliage alone. [[Korea 2026 — Flights and Stays]] contains indicative flight research and sample-date hotel results.

## Ten-day route

All times are local. Each day has one main outing and room for a meal/rest break. These are planning judgments, not booked departures or walking-time guarantees.

| Day | Sample date | Main plan | Overnight |
| --- | --- | --- | --- |
| 1 | Tue 27 Oct | ICN arrival; check in; short Insadong/Ikseon-dong walk only if rested | Seoul |
| 2 | Wed 28 Oct | Gyeongbokgung → Seochon / BOAN 1942; optional Euljiro record browse if energy permits | Seoul |
| 3 | Thu 29 Oct | Mangwon listening café → Hongdae/Yeonnam browsing; keep this a west-Seoul day | Seoul |
| 4 | Fri 30 Oct | Optional Third Tunnel DMZ group tour; otherwise Dongmyo + Euljiro | Seoul |
| 5 | Sat 31 Oct | Seoul → Gyeongju; luggage drop; historic center; Wolji around evening light | Gyeongju |
| 6 | Sun 1 Nov | Bulguksa morning; return for tea and an unhurried historic-center walk | Gyeongju |
| 7 | Mon 2 Nov | Gyeongju → Busan; check in; Nampo/Gwangbok-dong, early finish | Busan |
| 8 | Tue 3 Nov | Gamcheon → Nampo; optional Songdo only if you still want another excursion | Busan |
| 9 | Wed 4 Nov | Jeonpo café block → Gwangalli/Millak waterfront for late-day light | Busan |
| 10 | Thu 5 Nov | Depart from PUS only if the eventual flight routing supports it | — |

The eastern Busan alternative is Haedong Yonggungsa + Haeundae, **replacing Day 9**. Waveon is a further Gijang excursion and stays off the default route. The previous Biennale option ends before the sample Busan stay; do not carry it into these dates.

If flights are return ICN, either add a final Seoul night (10 nights total), or replace the third Busan night with Seoul (4 + 2 + 2 + 1 = 9). In that nine-night version, Day 9 becomes a transfer day; drop its Jeonpo/Gwangalli outing or substitute it for Day 8. Compare the additional rail/hotel cost with a protected flight home from PUS. Avoid planning a tight same-day Busan–ICN connection to a separate long-haul ticket.

## Closures and photography

- Gyeongbokgung normally closes Tuesday; holiday exceptions apply. Listed hours are 09:00–18:00 in October and 09:00–17:00 in November, last entry one hour earlier. Standard foreign-adult admission ages 19–64 is listed at KRW 3,000. Recheck notices after choosing dates. [Seoul Tourism Organization](https://english.visitseoul.net/attractions/gyeongbokgung%20palace/ENP000072)
- BOAN's listing closes Monday; Bitgguri's closes Tuesday. Move those blocks when shifting dates; see [[Korea 2026 — Places Shortlist]].
- Gyeongju city lists Wolji at 102 Wonhwa-ro, 09:00–22:00, last entry 21:30. Plan your photography around the selected date's sunset rather than treating closing time as dusk. Two evenings provide a weather fallback. [Gyeongju city route guide](https://www.gyeongju.go.kr/tour/page.do?mnu_uid=4598)
- Keep the camera kit light, ask before interior photography and allow a seated break before evening shooting. Check Bulguksa's current hours before departure; no exact-date access or admission quote was established here.

## DMZ decision — separate Klook shortlist

I would keep one optional group-tour day if modern history is a priority. For a shorter trip, or if you prefer street photography and shopping, use Dongmyo/Euljiro instead. Do not attach a fixed afternoon reservation to a tour day.

| Klook candidate | Displayed search price | What is established / still missing |
| --- | --- | --- |
| [DMZ Tour; NK Defector Meet up & Suspension Bridge options](https://www.klook.com/en-US/activity/216-dmz-tour-gyeonggi-do/) | US$50.75 | Listing describes Third Tunnel, Imjingak and observatory; join-in and private variants coexist. |
| [DMZ Insider Tour: Third Tunnel and optional bridge](https://www.klook.com/en-US/activity/77005-dmz-3rd-invasion-tunnel-suspension-bridge-one-day-tour-from-seoul/) | US$52.75 | Essential half-day and bridge variants; hotel pickup is advertised for groups of 10+, so do not assume solo pickup. |

These are **listing prices, not one-adult checkout totals**: the connector does not expose a reliable passenger-pricing unit here. The directly opened pages displayed US$50.85 / US$52.85, illustrating variation. English and solo-booking filters were requested, but selected-package language, meeting point, duration, one-person acceptance, lunch, passport instructions and cancellation deadline remain to be checked. Final prices and availability depend on date, party size and options.

The first operator lists a different Monday product without the normal tunnel itinerary; choose a non-Monday tunnel departure. JSA access is not established. A third result was excluded because its Cheorwon location conflicted with its Paju/Dora/Third Tunnel description. No tour is booked.

## Next concrete decisions

1. Confirm departure airport, passport, usable leave and budget; choose 6, 9 or 11 nights.
2. Compare protected flight itineraries and verify Korean arrival/departure dates before fixing hotel dates.
3. Quote one room for one adult with cancellation terms; then price the actual train legs.
4. Choose DMZ or the Seoul alternative; finish the checklist in [[Korea 2026 — Departure Checklist]].
''')

note('Places Shortlist',r'''
**Checked 7 October 2026.** A compact shortlist for the flexible solo route. Listed hours may change; menu prices are displayed listings, not future quotes. The saved no-meat/fish-allowed preference remains unconfirmed; these plant-based candidates keep options open.

## Seoul

| Stop | Location and fit | Verified detail and limits |
| --- | --- | --- |
| **BOAN 1942 / Boan Books** | 33 Hyoja-ro, Jongno-gu; after the palace on Day 2 | Cultural complex with bookstore/café. Listed Tue–Sun 12:00–18:00; check the specific business within the complex. [City listing](https://english.visitseoul.net/area/boan-1942/ENPk1cyet), updated 22 July 2026. |
| **House of Vinyl, Mangwon** | 1F, 23 Heeujeong-ro 16-gil, Mapo-gu; anchor Day 3 | LP listening café, listed daily 11:00–22:00; 90-minute limit when full. No current minimum spend verified. My pick for a relaxed solo music hour. [City listing](https://english.visitseoul.net/area/houseofvinyl-mangwon/ENPcq5rwf). |
| **Clique Records** | 301ho, 8 Eulji-ro 12-gil, Jung-gu; optional Day 2 or non-DMZ Day 4 | Operator lists Tue–Fri 14:00–20:00, Sat–Sun 13:00–20:00. Monday hours not listed. Use the ABOUT address; its separate CONTACT page contains inconsistent template information. No album stock or price guaranteed. [Operator](https://cliquerecords.kr/about). |
| **Dongmyo Flea Market** | Around Dongmyo shrine, Sungin-dong; Day 4 alternative | Sourced vintage/secondhand district, not a promise about a particular stall. Browse in daylight; inspect fit/condition and compare prices. Do not budget using the city's old bargain-price examples. [City listing](https://english.visitseoul.net/dongdaemunarea/Dongmyo-Flea-Market-EN/ENP009646), updated 7 August 2026. |
| **Ohsaegyehyang / 오세계향** | 14-5 Insadong 12-gil; arrival-day meal candidate or Day 2 | Vegetarian restaurant; listing updated 3 June 2026 gives 11:30–16:00 / 17:00–21:00, closed Thursday. Prefer this newer listing over older city articles with different hours. Confirm ingredients/allergies and single-person service. [City listing](https://english.visitseoul.net/PalaceArea/Ohsaegyehyang/ENP001670). |

Hongdae/Yeonnam remains a browsing block rather than a list of unverified shops. Choose a few shops encountered along the walk; do not cross the city for one of the unresolved old English names. If DMZ wins Day 4, keep Dongmyo optional or extend Seoul by a night.

## Gyeongju

| Stop | Location and fit | Verified detail and limits |
| --- | --- | --- |
| **Bitgguri / 빛꾸리** | 16-1 Sonhyoja-gil; historic-center tea break on Day 5 or 6 | KTO lists rice cakes and tangerine-ginger tea, floor seating, Wed–Mon 11:00–20:00; closed Tuesday. No tea class or price verified. [KTO](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=174235). |
| **YELLA** | 17 Taejong-ro 791beon-gil; downtown meal candidate | Visit Gyeongju's 24 September 2025 article identifies it as vegan. Current hours, prices and one-person menu need checking; do not assume continued daily operation. [Destination food guide](https://visitgyeongju.or.kr/tema/view/535f404004030a440a490342455140414b). |
| **El Rato Gyeongju** | 1045 Poseok-ro; convenient alternative around Hwangnidan-gil | The same guide lists vegetarian options and single seating. Mexican food offers variety; ask about the selected dish's ingredients. [Destination food guide](https://visitgyeongju.or.kr/tema/view/535f404004030a440a490342455140414b). |

For a Korean meal, check a nearby actual menu for a one-person bibimbap or tofu dish compatible with your diet. Tofu does not establish meat-free broth. Keep a simple backup meal on rail days. Do not make the more distant vegetarian-course restaurants obligatory for a solo trip.

## Busan

**Jeonpo Café Street** is the daytime Day 9 browsing area, around 92 Dongcheon-ro, Busanjin-gu. KTO identifies the district; hours vary by business. Pick one café on arrival rather than inventing a reservation or a walkable cluster from the old inbox. [KTO district guide](https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=&vcontsId=192977)

**Vegenarang / 베지나랑** is a conditional meal candidate for the Gwangalli/Millak outing. Busan's municipal menu lists textured-soy cutlet at **KRW 12,000 per listed dish**, spicy vegetable soup **KRW 11,500**, and avocado roll **KRW 12,500**. The lotus-leaf set explicitly requires **two or more people**, so prefer checking individual dishes for solo dining. Prices have no visible update date and need reconfirmation. [Municipal menu](https://menu.busan.go.kr/shop/info/CD_SHP_000774)

Address evidence is weaker: Restaurant Guru lists **9F, Noble Sky, 9-32 Gwanganhaebyeon-ro 370beon-gil**, but its hours and recent review text differ on kitchen closing time. The city tourism page and operator Instagram could not be read. **Recheck branch/address, last order and one-person ordering before making a special journey.** This remains conditional, not a timed meal booking. [Secondary address listing](https://restaurantguru.com/%EB%B2%A0%EC%A7%80%EB%82%98%EB%9E%91-Busan)

## Shopping and meal rules

- Suggested shopping envelope: **US$150 total**, shared by clothing, records, books and gifts; an allowance awaiting your budget, not a spending target. Café/listening consumption belongs to the separate café allowance.
- Buy one well-fitting vintage item before adding several speculative purchases. Keep record sleeves protected and leave luggage space.
- Ask for one-person ordering before sitting down at a set-menu restaurant. Confirm broth, sauces and garnishes; establish allergies separately.
- [[Korea 2026 — Food]] retains the dietary questions and Korean card. [[Korea 2026 — Cafés and Shops]] retains unresolved leads; a name in that inbox is not a verified recommendation.
''')

note('Flights and Stays',r'''
**Research date: 7 October 2026. One traveler; hotel searches specify one adult / one room.** Dates below are comparison scenarios. Santiago is an unconfirmed working origin; do not use these flight results if your departure airport differs.

## Flights — indicative date research

Separate October and November return searches for **SCL–ICN** were made using [Skyscanner](https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data), USD / Chile market. These are indicative route prices, not checked one-adult booking totals. The tool has no passenger-count input. All examples below are indirect; individual legs, baggage, connection protection, refund rules and Korean arrival times were not provided.

| SCL outbound date | ICN return-departure date | Displayed indicative USD | Use |
| --- | --- | ---: | --- |
| 23 Oct 2026 | 30 Oct 2026 | $1,860 | Too short to assume nine Korean nights; comparison only. |
| 23 Oct 2026 | 31 Oct 2026 | $1,912 | Eight days between departure dates is not eight nights in Korea. |
| 2 Nov 2026 | 11 Nov 2026 | $1,435 | Later price lead; likely needs extension for the full route, depending on arrival. |
| 2 Nov 2026 | 18 Nov 2026 | $1,435 | Longer price lead; compare a 10–14-night itinerary after seeing actual flights. |

**Inference:** early November deserves a detailed comparison because these returned examples cost less than the October examples. Different durations and undisclosed routes mean this is not proof that November is always cheaper. Some returned carrier labels were inconsistent; those entries were excluded rather than reconstructed. Exact-date live itineraries and a PUS return have not been obtained.

Search next for a protected multi-city itinerary into ICN and home from PUS, against return ICN plus a final Seoul night. Record each flight number, local departure/arrival date, layover airport, baggage allowance, airport change and whether separate tickets are involved. Do not assume a nonstop SCL–Korea flight or infer transit eligibility from residence in Chile. Personal transit advice needs your passport and chosen airports.

## Where I would stay

- **Seoul:** Jongno/Insadong for the palace, books and central walks. Hongdae is an alternative if late evenings and west-Seoul browsing dominate; use one base.
- **Gyeongju:** historic-center/Sajeong-dong area for evening walks; avoid choosing a Bomun/Bulguksa resort solely because it appears in a city search.
- **Busan:** Seomyeon for a balanced city base, or Busan Station for simpler rail luggage days and the western outings. Gwangalli is a waterfront alternative with different transfer costs.

These are route-fit judgments, not property quality guarantees.

## Tripadvisor sample-date accommodation shortlist

Searches used Seoul **27–31 October (4 nights)**, Gyeongju **31 October–2 November (2)** and Busan **2–5 November (3)**. All 2026. Each is **one adult, one room**. The connector states nightly room prices, mandatory fees included, taxes excluded; it also displays a separate taxes/fees field. That combination is insufficient to certify full-stay totals. We preserve the fields separately and do not add them blindly.

| Candidate / route fit | Displayed nightly USD | Separate tax/fee display | Base × nights, excluding unresolved taxes | Tripadvisor guest score |
| --- | ---: | ---: | ---: | --- |
| [Mini Hotel Insa, Seoul](https://www.tripadvisor.com/Hotel_Review-g294197-d1236995-Reviews-Mini_Hotel_Insa-Seoul.html) — Insadong | $59 | $7 | $236 / 4 nights | 4.3/5, 35 reviews |
| [Trip to Gyeongju](https://www.tripadvisor.com/Hotel_Review-g297888-d10513754-Reviews-Trip_to_Gyeongju-Gyeongju_Gyeongsangbuk_do.html) — Sajeong-ro | $104 | $10 | $208 / 2 nights | 4.9/5, 10 reviews |
| [Bee House Hostel](https://www.tripadvisor.com/Hotel_Review-g297888-d17563778-Reviews-Bee_House_Hostel-Gyeongju_Gyeongsangbuk_do.html) — central alternative | $75 | $8 | $150 / 2 nights | 4.3/5, 16 reviews |
| [Asti Hotel Busan Station](https://www.tripadvisor.com/Hotel_Review-g297884-d14789559-Reviews-Asti_Hotel_Busan_Station-Busan.html) — rail-first alternative | $115 | $12 | $345 / 3 nights | 4.6/5, 417 reviews |
| [Hotel Aqua Palace](https://www.tripadvisor.com/Hotel_Review-g297884-d1162841-Reviews-Hotel_Aqua_Palace-Busan.html) — Gwangalli alternative | $63 | $7 | $189 / 3 nights | 4.7/5, 452 reviews |

Guest scores are **review ratings, not hotel star classifications**. The arithmetic columns are estimates from rounded displayed nightly rates, not checkout totals. Room categories and private bathrooms are not established for the displayed offers; particularly do not assume a hostel listing means a private room. No accommodation is selected or reserved.

My first comparison would be Mini Hotel Insa + Trip to Gyeongju + Asti: **$789 base-only arithmetic** for nine nights. Request final tax-inclusive totals before judging value. Keep roughly **$900 as a lodging allowance**, not a guaranteed sufficient amount. The initial Gyeongju resort results were set aside for location mismatch; a Seomyeon search returned citywide results, so none is mislabeled as being in Seomyeon.

### Details worth checking before choosing

Tripadvisor detail results list Mini Hotel Insa at **26 Insadong 14-gil**, with baggage storage and laundry service; Trip to Gyeongju at **47-1 Sajeong-ro**, with baggage storage; Asti at **7-8 Jungang-daero 214beon-gil**. Verify these services for your arrival time and room. The Gyeongju review sample is small and the supplied reviews are old; its high score alone is weak evidence of current quality.

Displayed cancellation summaries: Mini's Booking.com offer says refundable before **24 October**; Trip to Gyeongju's Booking.com offer before **27 October** (Agoda before 28 October); Asti detail offers before **30 October**. **Times, time zones and complete conditions were not returned.** They are provider summaries, not deadlines for a booking you hold. Asti's detail offers varied from **$103–$116 per night**, confirming that provider/package results can change from the search table. Use the selected offer's full terms at checkout.

## Trains and airport legs

For the sample route, price **Seoul → Gyeongju on 31 October** and **Gyeongju → Busan on 2 November**, one adult, standard class. Add Busan → Seoul if choosing return ICN. Compare point-to-point tickets first; a rail pass is not presumed cheaper.

[KORAIL's English booking page](https://www.korail.com/global/eng) opened only as a script shell here, so no timetable, fare or available seat was verified. Exact-date rail quotes remain open. Use the high-speed Gyeongju station on the chosen ticket and allow a separate transfer to town. The old two-person rail allowance is not a usable quote.

[[Korea 2026 — Transport]] contains the previously sourced airport/local-transit guidance. Recheck the hotel-specific route and first/last services after flight selection. Plan station arrival with luggage margin; do not reserve an early intercity train immediately after an unconfirmed international arrival.
''')

note('Departure Checklist',r'''
**Prepared 7 October 2026 for one traveler and flexible dates.** This is a preparation plan; no application, booking, insurance purchase, download or reminder has been completed.

## Before selecting nonrefundable travel

- [ ] Confirm passport nationality, departure airport, leave available and total budget. Only nationality is needed for preliminary entry research; do not put passport numbers in this guide.
- [ ] Determine visa/K-ETA eligibility for that passport and arrival date. Living in Chile does not establish citizenship or exemption. Verify every transit airport and any landside/airport-change requirement against the actual itinerary.
- [ ] If K-ETA is required, use the official process and allow more than the typical 72-hour assessment period. The current application guide lists KRW 10,000 plus payment charges. No personal eligibility determination is made here. [K-ETA](https://www.k-eta.go.kr/portal/guide/viewetaapplication.do)
- [ ] Check passport validity against Korea, transit countries and airline requirements; do not use an invented universal six-month rule.
- [ ] Compare total travel time and protected connections alongside fare. Decide PUS departure versus return ICN before fixing hotels.

## Once dates and flights are chosen

- [ ] Reserve one room for one adult only after checking bed type, private/shared bathroom, access stairs/lift, late check-in, luggage storage, tax-inclusive full total and cancellation deadline with time zone.
- [ ] Price/reserve the actual train legs; verify station, departure date, ticket name and cancellation policy.
- [ ] Decide DMZ or city day. Check meeting point, one-person participation, English language, Third Tunnel access/physical demands, passport instructions, photography restrictions and operator cancellation terms.
- [ ] Choose travel insurance with appropriate medical assistance and any camera-equipment cover you need; record deductibles and exclusions.
- [ ] Review routine and itinerary-specific health preparation with a clinician, including any northern rural/DMZ exposure. [CDC South Korea](https://wwwnc.cdc.gov/travel/destinations/traveler/none/south-korea)
- [ ] Check medication active ingredients and quantities; controlled medicines may need advance MFDS permission. Carry original packaging and relevant documentation. [MFDS guidance](https://www.mfds.go.kr/brd/m_74/view.do?seq=43906)
- [ ] Confirm diet, shellfish/egg/dairy preferences and allergies. Save a suitable Korean food card only after it matches your actual needs.

## Week before departure

- [ ] Check Seoul, Gyeongju and Busan forecasts separately; adjust the outdoor days. [KMA](https://www.weather.go.kr/neng/forecast/short-term.do)
- [ ] Pack walking shoes, layers, warm evening layer, rain shell, compact day bag, camera protection, chargers and adapter. Check device input ratings and the airline's actual battery rules.
- [ ] Check eSIM compatibility/unlocked status, activation timing, coverage, validity and whether a local number is included; no plan has been purchased.
- [ ] Save Korean hotel addresses, tickets, insurer assistance and a trusted contact offline. Test access without mobile data yourself; this guide does not establish that an app's maps work offline.
- [ ] Arrange a simple check-in plan with a trusted person. Keep a second payment method separate and save your bank's lost-card contact.
- [ ] Recheck opening days, meal last orders and selected business addresses. For solo set menus, ask about minimum portions.

## Within the official arrival-declaration window

If your circumstances require an e-Arrival Card, it is free and filing opens **three days before arrival, based on Korean time**. It is separate from K-ETA. Use the official eligibility navigator; valid K-ETA holders are among the exempt groups. Enter the actual flight and lodging details, not the sample itinerary. [Official guide](https://www.e-arrivalcard.go.kr/portal/guide/eacGuide.do?locale=E) · [Navigator](https://www.e-arrivalcard.go.kr/portal/guide/navigator.do?locale=E)

## During the trip and before flying home

Emergency: **119 ambulance/fire; 112 police**. Save the hotel address in Korean so you can state your location. [Seoul visitor safety](https://english.visitseoul.net/essential-Info-article/Safety/ENN012370)

Keep the first day light, protect meal/rest time and leave a taxi reserve after evening photography. Recheck the final airport route, terminal and airline bag-drop deadline. If separate transport brings you to ICN from Busan, a final Seoul night gives recovery margin. Record actual spending only after payment; keep research offers out of [[Korea 2026 — Bookings]].
''')

insert('Budget',r'''
## Current solo planning allowance — 9 nights / 10 days

**This supersedes the old two-traveler worksheet below.** All amounts are proposed USD spending envelopes, not market quotes or your approved ceiling. International flights are separate. A private room is paid by you alone; do not halve an old two-person lodging total.

| Category | Solo allowance | Basis |
| --- | ---: | --- |
| Lodging | $900 | Nine nights; sample hotel base arithmetic is $789 before unresolved taxes/room conditions. |
| Meals | $300 | $30 × 10 calendar days; can include partial flight days. |
| Cafés / listening-café consumption | $100 | Separate from retail shopping. |
| Clothes, records, books and gifts | $150 | One shared optional shopping envelope. |
| Intercity trains | $90 | Placeholder for two legs; not a KORAIL quote. |
| Airport/local transport and taxi margin | $110 | Route-dependent allowance. |
| Optional DMZ | $85 | Package/baggage/meal needs unpriced; listing price is not checkout. |
| Other admissions | $60 | Excludes the DMZ line to avoid double counting. |
| Mobile data | $25 | No product selected. |
| Travel insurance | $80 | Placeholder, not a personal premium quote. |
| Subtotal | **$1,900** | Proposed on-ground allocation. |
| Contingency, 15% | **$285** | Reserve, not spending. |
| Total excluding international flights | **$2,185** | Recalculate after exact quotes and your budget. |

As a deliberately conservative planning exercise, reserving another $1,800–$2,400 for international flights gives **$3,985–$4,585 overall**. That flight envelope is my budgeting judgment, not the price of an available itinerary. [[Korea 2026 — Flights and Stays]] keeps Skyscanner's lower indicative examples separate because routing, baggage and usable nights are unresolved. Add any visa/transit authorizations, extra Seoul night/rail leg or purchases above the cap; no current CLP conversion is asserted.

To trim the plan, first remove DMZ and reduce shopping, then compare room types/neighborhoods and a two-city route. Do not cut needed connection margins to fit the old budget. Reprice all hotels if dates change.

## Historical worksheet — retained for comparison only
''')
note('Bookings',r'''
**7 October 2026: you confirmed that nothing is booked. One traveler; dates are flexible.** Provider search results and suggested dates live in [[Korea 2026 — Flights and Stays]], not this ledger.

## Decisions before booking

- [ ] Confirm origin, passport, duration, diet and budget.
- [ ] Select flights with actual local arrival/departure dates and checked transit requirements.
- [ ] Choose one room for one adult in each base; record full totals and cancellation time zones.
- [ ] Select actual KORAIL departures and any return-to-Seoul leg.
- [ ] Choose optional DMZ package or Seoul alternative.

## Confirmed reservations

| Item | Actual dates | Provider / confirmation | Currency / full total | Paid / balance | Cancellation deadline and zone |
| --- | --- | --- | --- | --- | --- |
| None confirmed | — | — | — | — | — |

Do not add sample-price hotels as reservations. When you choose an option, keep selection status distinct from a paid/issued confirmation. Deposits are part of the total, not additional cost. Keep passport numbers and payment details outside broadly shared guide exports.
''')

insert('Itinerary','## Current route supersedes the dated draft\n\n'+status+'\n\nRecommended: **Seoul 4 nights → Gyeongju 2 → Busan 3**, with a separate return-ICN variant. Read [[Korea 2026 — Solo Plan#Ten-day route|the flexible ten-day route]].\n\n## Previous six-night draft — reference only')
docs[prefix+'Itinerary.md']=docs[prefix+'Itinerary.md'].replace('Two travelers and the fish-allowed/no-meat diet remain draft assumptions awaiting confirmation.','This previous version used two travelers; you have now confirmed solo travel. The dietary assumption remains unconfirmed.')
insert('Cafés and Shops','## Current researched shortlist\n\nUse [[Korea 2026 — Places Shortlist]] for House of Vinyl, Clique Records, BOAN, Dongmyo, Bitgguri and meal candidates. The inbox below preserves older leads; promoted entries now have evidence in that shortlist.')
insert('Food','## Current meal candidates\n\nSee [[Korea 2026 — Places Shortlist]] for Ohsaegyehyang in Seoul, YELLA/El Rato in Gyeongju and a conditional Vegenarang option in Busan. Vegenarang’s lotus-leaf set requires two or more people; check its individual dishes for solo ordering. Your dietary preference remains to be confirmed.')
docs[prefix+'Shopping shortlist.md']=docs[prefix+'Shopping shortlist.md'].replace('The budget has **US$135 total for records, books, listening-room visits and tea**. Clothing is not separately funded. Either share that line, reduce another line or explicitly increase the trip budget. Do not combine the old contradictory US$145, US$150 and US$295 ceilings.','The new solo budget proposes **US$150 total for clothing, records, books and gifts**, awaiting your budget ceiling. Café/listening consumption is separate. This replaces the old US$135 discretionary line; do not add the two together. See [[Korea 2026 — Budget]] and [[Korea 2026 — Places Shortlist]].')
insert('Transport','## Current solo transport plan\n\nThe dated table below belongs to the previous six-night draft. The nine-night sample uses **31 October: Seoul → Gyeongju; 2 November: Gyeongju → Busan**. Actual dates remain flexible. Add Busan → Seoul if flights return through ICN; see [[Korea 2026 — Flights and Stays#Trains and airport legs]].')
for title in ['Practical Info','Health preparation','Weather and Packing']:
    insert(title,'For the current solo preparation sequence, use [[Korea 2026 — Departure Checklist]]. Any dates below refer to the earlier example; recheck date-dependent rules once the trip is chosen.')
insert('Autumn Foliage','## New evidence from the solo-plan research\n\nA KTO article published 8 September 2026, opened 7 October, now supplies a Weatheri forecast: Bukhansan peak around 4 November. It is weather-dependent and does not establish peak dates for the individual city stops. The earlier review statement below records what that review had established at the time. [2026 KTO foliage forecast](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1593230)\n\nDates remain flexible; use [[Korea 2026 — Solo Plan]] and keep foliage as one factor rather than a guarantee.')
for name in list(docs):
    if 'Pocket 2026-' in name or name==prefix+'Daily Pocket Cards.md':
        insert(name[len(prefix):-3],'**Previous dated draft:** these cards retain the old six-night sequence and are not the current travel calendar. You are traveling alone with dates open. Follow [[Korea 2026 — Solo Plan#Ten-day route]] until flights and dates are selected.')
insert('My Five Things','**Solo-plan update:** the five interests below are retained, but dates are flexible. House of Vinyl is now the sourced music-hour candidate; see [[Korea 2026 — Places Shortlist]]. Wolji moves to Day 5/6 of the recommended route rather than a fixed 30 October.')

insert('Start Here',r'''
## Current continuation — solo and flexible

**Confirmed by you on 7 October 2026: traveling alone; nothing booked; dates can change.** This supersedes the two-traveler assumptions and fixed dates below.

1. [[Korea 2026 — Solo Plan|Route and date options]] — recommended 10 days / 9 nights, Seoul 4 + Gyeongju 2 + Busan 3; DMZ decision and return-ICN variant.
2. [[Korea 2026 — Places Shortlist|Cafés, music, vintage shopping and meals]] — checked locations, closing days and solo-ordering caveats.
3. [[Korea 2026 — Flights and Stays|Flights, hotels and trains]] — indicative flight comparisons and one-adult hotel searches; [[Korea 2026 — Budget|solo budget]].
4. [[Korea 2026 — Departure Checklist|Departure preparation]] — documents, health, packing and practical setup.

Still needed: passport nationality, departure airport, usable trip length/season, budget and diet. **27 October–5 November is a hotel-search example only.** The suggested solo on-ground envelope is $2,185 excluding international flights, not an approved ceiling or booking quote.

## Previous dashboard planning context — reference only
''')
docs[prefix+'Start Here.md']=docs[prefix+'Start Here.md'].replace('Two travelers and no meat but fish allowed are inherited assumptions awaiting confirmation.','The earlier two-traveler assumption is superseded by solo travel; the no-meat/fish-allowed preference still needs confirmation.').replace('- Confirm dates, traveler count, passport nationality and dietary details.','- Choose dates and confirm passport nationality, origin and dietary details; traveler count is now one.')

docs[prefix+'Session Recap 2026-10-07.md']+=r'''

## Continuation — solo flexible plan

User explicitly confirmed solo travel, flexible dates and nothing booked, and requested all four next steps: route, places, transport/lodging/budget and departure preparation. Added Solo Plan, Places Shortlist, Flights and Stays, and Departure Checklist, linked from Start Here and relevant chapters. Recommended nine nights (4 Seoul + 2 Gyeongju + 3 Busan); 27 October–5 November is only a hotel-search scenario. Preserved the previous dated route/cards as marked reference material.

Connected Klook, Skyscanner and Tripadvisor searches succeeded (first Seoul hotel request timed out; a refined search succeeded). Saved indicative SCL–ICN October/November prices with unconfirmed origin, solo-occupancy sample hotel offers, provider limitations and a separate DMZ shortlist. No exact-date rail fares, flight connection details, full hotel checkout totals or chosen-package tour terms were established. KTO's 2026 foliage forecast is now sourced, without city-tree guarantees.

New solo planning allowance: $1,900 + $285 reserve = $2,185 excluding international flights, not user-approved. Passport, origin, available leave/season, budget and dietary answers remain pending. Need those answers before personal entry/transit determination and final quote selection. No bookings, payments, business messages, downloads, reminders, plugin changes or Japan edits were made.

Backup/staging and compact provider evidence: `/home/ivanaguilera/Work/korea-solo-plan-20261007/`. Source links and limitations are adjacent to the claims in the four new notes.
'''

for name,s in docs.items():
    if not (backup/name).exists() or s!=(backup/name).read_text(): (staged/name).write_text(s)
print('Staged',len(list(staged.glob('*.md'))),'notes')
