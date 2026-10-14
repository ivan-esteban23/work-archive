from pathlib import Path
import json,hashlib,re
root=Path('/home/ivanaguilera/Work/korea-fitness-flights-20261007')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
staged=root/'staged'; backup=root/'backup'
staged.mkdir(exist_ok=True); backup.mkdir(exist_ok=True)
original={p.name:p.read_text() for p in vault.glob('Korea*.md')}
notes=dict(original)
def key(s): return 'Korea 2026 — '+s+'.md'
def replace(s,a,b):
 n=key(s); assert a in notes[n],(s,a); notes[n]=notes[n].replace(a,b)
def add(s,text):
 n=key(s);assert n not in notes
 notes[n]='---\ncssclasses:\n  - korea-trip\n---\n# Korea 2026 — '+s+'\n\n'+text.strip()+'\n'
profile='Confirmed 7 October 2026: one Chilean traveler from San Fernando, departing SCL; flexible dates, nothing booked; US$2,500 excluding round-trip international airfare; unrestricted diet, no reported food allergies, preference for high-protein meals. Trip length and transit authorizations remain open.'
old='trip length, departure airport, passport and dietary details remain open.'
for n in notes:
 if 'Session Recap' not in n and 'Review and Sources' not in n:
  notes[n]=notes[n].replace(old,'Chilean nationality, San Fernando/SCL origin, US$2,500 excluding international flights, and unrestricted high-protein diet are now confirmed. Dates and trip length remain open.')
add('Fitness and Protein',r'''
[[Korea 2026 — Start Here|Dashboard]] · [[Korea 2026 — Budget|Budget]] · [[Korea 2026 — Flights and Stays|Hotel research]]

**Checked 7 October 2026.** Solo traveler, unrestricted diet and no reported food allergies. The aim is to maintain normal training and eat enough while enjoying the trip. All hotel dates are examples; nothing is reserved.

## Hotels with fitness facilities

Prices below came from Tripadvisor for **one adult, one room**, in USD per night. Mandatory fees are included according to the connector; taxes are excluded. A separate tax/fee field is retained where returned and is not blindly added, because it may overlap with included fees. Multiplication gives base arithmetic, not a verified full-stay checkout total. Rooms, gym charges and cancellation terms still need final confirmation.

| Hotel | Gym evidence | Example stay / lowest returned nightly offer | Base arithmetic |
| --- | --- | --- | ---: |
| [Shilla Stay Mapo, Seoul](https://www.tripadvisor.com/Hotel_Review-g294197-d8118189-Reviews-Shilla_Stay_Mapo-Seoul.html) | Officially lists dumbbells, three types of strength machines, three treadmills, two bikes and a cross trainer; 26F, 06:00–23:00. Maximum weights/rack not established. | 27–31 Oct 2026: $208; 3–7 Nov: $181 | $832 or $724 / 4 nights, taxes extra |
| [NineTree Premier Hotel Insadong, Seoul](https://www.tripadvisor.com/Hotel_Review-g294197-d18185180-Reviews-Nine_Tree_Premier_Hotel_Insadong-Seoul.html) | Guest fitness access free, 07:00–22:00; equipment/weight limits not established. | 27–31 Oct: $262; 3–7 Nov: $236 | $1,048 or $944 / 4 nights, taxes extra |
| [Ramada Encore by Wyndham Busan Station](https://www.tripadvisor.com/Hotel_Review-g297884-d477913-Reviews-Ramada_Encore_by_Wyndham_Busan_Station-Busan.html) | Wyndham confirms a fitness center. Hours, weights and access fee not verified. | 2–5 Nov: $82; separate tax/fee display $8 | $246 / 3 nights, taxes unresolved |
| [Asti Hotel Busan Station](https://www.tripadvisor.com/Hotel_Review-g297884-d14789559-Reviews-Asti_Hotel_Busan_Station-Busan.html) | Tripadvisor lists fitness facilities; official fitness page could not be retrieved. Verify equipment, hours and fee. | 2–5 Nov: $116; separate tax/fee display $12 | $348 / 3 nights, taxes unresolved |
| [Orakai Insadong Suites, Seoul](https://insa.orakaihotels.com/eng/about/facilities_fitness.asp) | Official gym: 2F, 06:00–23:00; hotel FAQ says guest facilities are complimentary. | Price request timed out; no reliable quote | Unpriced |

Facility sources: [Shilla Stay Mapo](https://www.shillahotels.com/en/shillastay/mapo/facilities/fitnessCenter.do), [NineTree guest guide](https://atoz.ninetreehotels.com/INSADONG/hotel), [Wyndham Busan Station](https://www.wyndhamhotels.com/en-uk/ramada/busan-south-korea/ramada-encore-busan-station/overview), [Orakai FAQ](https://insa.orakaihotels.com/eng/customer/faq.asp?mCode=10). Access and equipment have not been tested in person. A fitness-center label does not establish a full weight room.

**My budget preference:** modest central lodging in Seoul plus commercial gym visits; compare Ramada with Asti in Busan. Mini Hotel Insa's earlier 27–31 October listing was $59/night, with a separate $7 tax/fee field; a gym was not established. Against Shilla's same-date $208, the four-night base difference is $596, much more than a few day passes. Gyeongju can be two recovery/walking days; no suitable central hotel gym has yet been verified. Avoid moving to a distant resort solely for gym access.

## Commercial gym prices

These are access passes, not private personal-training sessions. Keep the original KRW prices; USD equivalents below use an **illustrative planning rate of ₩1,400 per US$1**, not a live exchange quote.

| Gym / location | Listed access price | Practical limitation |
| --- | --- | --- |
| [SpoAny Seoul City Hall PRO](https://m.spoany.com/branch/branch_detail.html?base_seq=ODU%3D), 124 Seosomun-ro, Jung-gu | Day ₩25,000 (~$18), VAT and workout-clothes rental included; month ₩110,000 (~$79), clothes ₩11,000 extra | Page separately mentions first-join fee ₩30,000 before VAT. Confirm whether a day visitor pays it and whether a foreign visitor can register without a Korean number. |
| [Boy Gym, Gwangbok branch, Busan — Hoppin partner listing](https://www.hoppin.life/257a0a27-37f8-805c-b016-dcdcda493456) | Regular day ₩22,000 (~$16); month ₩124,000 (~$89), clothes included in monthly listing | Partner-listed regular prices, not a direct checkout quote. ₩20,000/₩100,000 discounts are only for Hoppin participants; not assumed available to you. |

SpoAny lists weekdays 06:00–00:00, Saturday 06:00–23:00, Sunday/holidays 10:00–18:00. Busan's partner listing gives weekdays 06:00–00:00 and weekends 10:00–21:00. Recheck holiday closures, towel/shower access, registration fees and payment before traveling there.

**Plan ₩88,000–100,000 for four visits** at those day rates (~$63–71 at the illustrative rate); the budget allocates $100 to leave room for fees and currency movement. A month in each city makes little sense for two Seoul and two Busan sessions. Suggested slots for the nine-night route: two Seoul sessions, Gyeongju recovery, two Busan sessions, adjusted for fatigue and opening hours. If “private gym” means a trainer, SpoAny separately lists ₩80,000–100,000 per session **before VAT**; that is outside this gym-access allowance.

## Eating enough protein while traveling

Korean dishes vary: choose a protein portion deliberately instead of assuming every meal is high in protein. Keep rice/noodles, vegetables and enough overall food for walking and training. General sports-nutrition guidance for healthy exercising adults is **1.4–2.0 g protein/kg/day**, often distributed across meals of roughly **20–40 g**. Your body weight and usual targets are unknown, so this is context rather than a personalized prescription. [ISSN position stand, 2017](https://link.springer.com/article/10.1186/s12970-017-0177-8)

| Meal | Practical choices | Check |
| --- | --- | --- |
| Breakfast | Eggs with yogurt/milk or soy milk, plus fruit and bread/rice | A pastry and coffee alone may need a protein addition. |
| Lunch | Grilled fish set (생선구이), bulgogi set (불고기 정식), or tofu stew with egg/meat/seafood (순두부찌개) | Actual portion size; tofu stew is not automatically a large protein serving. |
| Dinner | Chicken, fish, lean beef/pork, or tofu with rice and vegetables | BBQ often has minimum portions; choose individual set meals when solo. |
| Rail/DMZ backup | Packaged chicken breast (닭가슴살), boiled eggs, yogurt, milk/soy drink or a protein drink | Read 단백질 (protein), grams per package and storage instructions. Buy chilled foods close to eating. |

These are food categories, not verified restaurant menus or claimed gram counts. The meal envelope is **$350 across ten days ($35/day)**, including protein snacks; cafés are separate. No supplements or restrictive diet are necessary assumptions. Existing vegetarian restaurants remain optional for variety.

Useful phrases: **혼자 왔어요. 1인분 주문할 수 있나요?** — I'm alone; can I order one serving? **계란을 추가할 수 있나요?** — Can I add an egg? **일일권 있나요?** — Do you have a gym day pass?
''')
add('Flight Routes from Chile',r'''
[[Korea 2026 — Start Here|Dashboard]] · [[Korea 2026 — Flights and Stays|Hotel and rail research]] · [[Korea 2026 — Budget|Budget]]

**Checked 7 October 2026.** Chilean traveler, home San Fernando, departure **SCL**. One traveler; dates flexible; airfare is separate from the US$2,500 travel budget. “Dallas” means the DFW connecting airport, generally an American Airlines option. Airline names: Korean Air and Air France.

## Flexible-date fare leads

[Skyscanner](https://skyscanner.net/g/referrals/v1/flights/home?mediaPartnerId=2850210&utm_term=skyscanner_chatgpt_app_data) indicative return searches: SCL–ICN, USD, Chile market, November/December 2026 and March 2027. The tool has no passenger-count input. **These are displayed indicative return prices, not verified one-adult booking totals.** Carrier labels identify the returned quote, not every operating leg or a confirmed routing. Inconsistent carrier records were excluded.

| Leave SCL | Leave ICN for home | Displayed USD return | Returned carrier labels, outbound / return |
| --- | --- | ---: | --- |
| 2 Nov 2026 | 18 Nov 2026 | $1,435 | LATAM / Asiana |
| 2 Dec 2026 | 15 Dec 2026 | $1,762 | Air Canada / Air Canada |
| 9 Mar 2027 | 24 Mar 2027 | $1,631 | LATAM / Cathay Pacific |
| 2 Mar 2027 | 16 Mar 2027 | $1,705 | Air France / Air France |
| 11 Mar 2027 | 26 Mar 2027 | $1,721 | Qatar Airways / Qatar Airways |

These date pairs have different durations and unknown Korean arrival dates, so they are not equal-stay comparisons. November is the first price lead; March is a preparation-time alternative, not a selected season or a blossom forecast. December deserves a look if its exact itinerary is better. A $270 difference between the November and Air France March examples is meaningful, but does not establish value until baggage, usable nights and connections are known. Existing note names remain unchanged even if 2027 is eventually chosen.

## Airline and connection comparison

The route patterns below are **search candidates**, not confirmed bookable itineraries. One ticket with protected connections is preferable for this solo trip; a marketed airline name does not guarantee all flights are operated by it.

| Candidate | Connection pattern to investigate | Decision |
| --- | --- | --- |
| Air France | SCL–CDG–ICN, one stop | First Europe comparison; March fare lead above does not itself prove these legs. Check airside connection, terminals and total time. |
| Iberia / partner | SCL–MAD–ICN, if through-ticketed with an onward carrier; otherwise another stop | Iberia markets Santiago–Seoul, but that is not proof of an Iberia-operated Madrid–Seoul leg. Check baggage transfer and protection. |
| American / DFW | SCL–DFW–ICN when seasonal SCL–DFW operates; otherwise possibly another US stop | Do not assume a one-stop November schedule. US transit authorization is a prerequisite. |
| LATAM + Korean Air / partner | A US or other partner hub connecting to ICN | Compare the complete itinerary. LATAM and Korean Air both market Santiago–Seoul; neither marketing page proves nonstop service. |
| Qatar Airways + feeder | SCL–GRU–DOH–ICN, two stops, subject to a through fare | Qatar publishes São Paulo–Seoul via Doha. Add the SCL feeder explicitly; compare total hours and current operating conditions. |
| Japan Airlines + partner | SCL–US hub–Tokyo–Seoul, a potential two-stop construction | Santiago is in JAL's codeshare network. Do not infer a direct JAL departure from Chile. Avoid NRT/HND airport changes; check whether Seoul arrival is GMP or ICN. |
| Air Canada | SCL–YYZ–ICN if available on the chosen dates | December price lead; verify Canadian transit documentation for a Chilean passport and each leg. |

Official airline references: [Iberia Santiago–Seoul](https://www.iberia.com/cl/vuelos-baratos/Santiago-de-Chile-Seul/), [LATAM Santiago–Seoul](https://www.latamairlines.com/cl/es/destinos/corea-del-sur/vuelos-desde-santiago-a-seul), [Korean Air Santiago–Seoul](https://www.koreanair.com/flights/en/flights-from-santiago-to-seoul), [Qatar São Paulo–Seoul](https://www.qatarairways.com/en-kr/destinations/flights-to-seoul/from-sao-paulo.html), [JAL network](https://www.jal.com/en-jp/about/air/route.html). These establish marketed routes/network context, not protected connections, future inventory or equal baggage allowances. No comparable exact-date Iberia, American or JAL fare was obtained; no invented fare is assigned to them.

## Flight time versus total journey time

Secondary [FlightConnections route overview](https://www.flightconnections.com/flights-from-scl-to-icn) lists combined flying times, **excluding layovers**: Madrid 25h40, DFW 25h50, Toronto 25h55, Paris 26h20. It marks SCL–DFW seasonal December–March and has inconsistent seasonal labels elsewhere, so this is orientation, not a timetable. For example, Paris 26h20 plus a hypothetical 3–5-hour connection gives **29h20–31h20 airport-to-airport**, before travel to SCL/check-in. No actual flight numbers, departure hours or connection lengths were verified.

My search preference is a protected one-stop itinerary with sensible connection time; compare two stops when the savings justify the extra travel. Keep first Korean day light. Budget **roughly 14–16 calendar days away from home for about 9–11 Korean nights** as a planning margin, then calculate from actual local flight dates. Do not turn the fare-table departure-date gaps into hotel nights.

## San Fernando to SCL

Plan San Fernando → Santiago by intercity bus or available train, then transfer to the airport. Exact San Fernando services, fare and journey time have not yet been quoted. Match the actual Santiago arrival terminal to the airport-bus boarding point.

[Turbus airport service](https://www.turbus.cl/en/traslados) publishes **CLP 2,000 general one-way fare**, Terminal Alameda platforms 22/23 → airport, daily **04:30–00:00**, every **10–15 minutes**; airport → Alameda **05:30–00:00**. This is the Santiago airport leg, not a San Fernando through fare. Recheck the timetable before departure.

For an early SCL flight, compare sleeping in Santiago the night before; for an afternoon/evening departure, same-day travel may work once actual services and buffers are checked. Aim to reach SCL about three hours before an international departure, subject to the airline's instructions, with additional road-delay margin. The budget reserves $100 for return Chile ground travel/contingency; an overnight stay or private car may require reallocating other lines.

## Entry and transit checklist

Chile's official [consular guidance](https://www.consulado.gob.cl/chilenas-os-que-viajan-fuera-de-chile) tells Chilean tourists to obtain **K-ETA for South Korea** and flags **ESTA for US transit**. Use the [official K-ETA application](https://k-eta.go.kr/portal/newapply/index.do?locale=ES), checking arrival-date and age/status exemptions. For the US, confirm valid ESTA eligibility/approval or an appropriate existing visa before choosing DFW, LAX or another US hub; no authorization is assumed. A valid visa can change the required process.

Canada, Japan, France/Spain and any other transit country must be checked against the actual itinerary, passport and airside/landside requirements. Airport changes or separate tickets can change entry requirements. No application has been made. Next unresolved inputs: available leave/season and existing US authorization; then obtain full one-adult fares, bags, local times, connection protection and refund terms before selecting hotels.
''')
replace('Start Here','Still needed: passport nationality, departure airport, usable trip length/season, budget and diet. **27 October–5 November is a hotel-search example only.** The suggested solo on-ground envelope is $2,185 excluding international flights, not an approved ceiling or booking quote.',profile+'\n\nNew research: [[Korea 2026 — Flight Routes from Chile|Airline/date comparisons and San Fernando–SCL]] · [[Korea 2026 — Fitness and Protein|Hotel gyms, gym passes and high-protein meals]]. The revised budget allocates $2,200 plus $300 reserve. **27 October–5 November remains a hotel-search example only.**')
replace('Start Here','the no-meat/fish-allowed preference still needs confirmation.','the old no-meat restriction is superseded by your unrestricted diet.')
replace('Start Here','- Choose dates and confirm passport nationality, origin and dietary details; traveler count is now one.','- Choose dates/usable leave and check existing US transit authorization; personal profile is now confirmed.')
replace('Start Here','- Quote the six nights and both rail legs; decide whether the optional DMZ visit matters enough to book.','- Quote the chosen 9–11-night variant and all rail legs; decide whether the optional DMZ visit matters enough to book.')
replace('Start Here','- Reprice the US$2,395 original allowance before treating it as a realistic current total.','- Keep exact quotes within the confirmed US$2,500 cap, excluding round-trip international airfare.')
replace('Solo Plan','Passport, departure airport, total budget, available leave and diet are awaiting your answers.',profile+' See [[Korea 2026 — Flight Routes from Chile]] and [[Korea 2026 — Fitness and Protein]].')
replace('Solo Plan','Confirm departure airport, passport, usable leave and budget; choose 6, 9 or 11 nights.','Confirm usable leave/season and transit authorization; choose 9 or 11 nights within the $2,500 non-airfare cap.')
replace('Flights and Stays','Santiago is an unconfirmed working origin; do not use these flight results if your departure airport differs.','SCL is now confirmed: home is San Fernando, nationality Chilean. Use [[Korea 2026 — Flight Routes from Chile]] for the latest November/December/March comparison and Chile airport approach; [[Korea 2026 — Fitness and Protein]] compares hotel gyms and commercial passes.')
replace('Flights and Stays','Personal transit advice needs your passport and chosen airports.','Chilean nationality is confirmed; transit requirements still depend on chosen airports and existing authorizations.')
replace('Flights and Stays','Keep roughly **$900 as a lodging allowance**, not a guaranteed sufficient amount.','The revised [[Korea 2026 — Budget]] reserves **$1,000 for lodging**, not a guaranteed sufficient amount.')
budget=r'''## Current confirmed ceiling — US$2,500 excluding international flights

**Updated 7 October 2026.** One Chilean traveler from San Fernando via SCL, unrestricted high-protein diet, nothing booked. These are spending allocations, not prices or reservations. Round-trip international airfare is separate. This replaces the previous $2,185 proposal.

| Category | USD allowance | Basis |
| --- | ---: | --- |
| Lodging | $1,000 | Aim for 9–10 nights, tax-inclusive total; about $100–111/night average. |
| Meals and protein snacks | $350 | $35 × 10 days; extend/reallocate for a longer stay. |
| Cafés | $70 | Separate from meals and shopping. |
| Shopping and gifts | $80 | Optional shared envelope. |
| Korea intercity rail | $140 | Includes margin for final return toward Seoul; exact fares pending. |
| Korea airport/local transport | $110 | Public transport plus modest taxi margin. |
| Commercial gym access | $100 | Around four visits plus fee/FX margin; reduce if hotel gym suffices. |
| San Fernando–SCL return ground travel | $100 | Planning reserve, not a bus/private-transfer quote. |
| Optional DMZ | $85 | Selected package still unpriced. |
| Other admissions | $40 | Separate from DMZ. |
| Data | $25 | Product not chosen. |
| Insurance | $70 | Personal premium not quoted. |
| Entry/transit paperwork allowance | $30 | Placeholder; may be insufficient for the selected route. |
| Allocated subtotal | **$2,200** | Estimates only. |
| Unspent contingency | **$300** | Keep available for uncertainty. |
| Total ceiling | **$2,500** | International round-trip tickets excluded. |

Keep original-currency quotes. No live exchange rate is asserted; the gym chapter uses a clearly marked ₩1,400/USD illustration. Add card/FX fees to actual checkout totals. A required transit permit, Santiago overnight, costlier insurance or extra Korean nights must fit by reallocating optional spending before using emergency reserve.

**Recommended starting point:** nine Korean nights, or ten if adding a final Seoul night before ICN departure. The sample Mini Hotel Insa + Trip to Gyeongju + Ramada Busan combination is $236 + $208 + $246 = **$690 base-only** for 4+2+3 nights in the 27 Oct–5 Nov scenario; taxes/room categories remain unresolved. This is evidence for comparing modest rooms, not a guaranteed $690 stay. A hotel with an expensive gym premium can consume the savings quickly. See [[Korea 2026 — Fitness and Protein]].

Longer stays need a fresh calculation: an extra day adds lodging, meals and transport even if the return airfare is unchanged. Fund extra nights first by reducing shopping, optional DMZ/cafés, or choosing cheaper verified rooms. The indicative 2–18 November flight pair must not automatically become a 16-night itinerary. [[Korea 2026 — Flight Routes from Chile]] separates flight dates from Korean nights.

'''
n=key('Budget');a=notes[n].index('## Current solo');b=notes[n].index('## Historical worksheet')
notes[n]=notes[n][:a]+budget+notes[n][b:]
replace('Budget','Neither ceiling has been newly approved.','Historical note: the user subsequently confirmed a US$2,500 solo ceiling, excluding international round-trip airfare; use the current allocation above.')
n=key('Food'); a=notes[n].index('## Dietary assumption');b=notes[n].index('## Food-name corrections')
notes[n]=notes[n][:a]+'''## Confirmed food preferences

You eat all foods and report no food allergies. Prefer protein at each main meal to support your regular exercise. The old no-pork/beef/chicken restriction and its Korean card are withdrawn; originals are preserved in the workspace backup. Use [[Korea 2026 — Fitness and Protein]] for practical meals, snacks, solo ordering phrases and the $35/day food allowance.

'''+notes[n][b:]
replace('Food','Your dietary preference remains to be confirmed.','These plant-based venues are optional variety; you now confirm an unrestricted diet with a high-protein preference.')
replace('Food','Rice with toppings; request without meat and confirm stock/sauce. Egg may be included.','Rice with toppings; choose beef/egg/tofu as available and check the protein portion. Egg may be included.')
replace('Places Shortlist','The saved no-meat/fish-allowed preference remains unconfirmed; these plant-based candidates keep options open.','You now confirm an unrestricted diet and no food allergies; these plant-based venues remain optional, with protein-focused meal guidance in [[Korea 2026 — Fitness and Protein]].')
replace('Places Shortlist','[[Korea 2026 — Food]] retains the dietary questions and Korean card.','[[Korea 2026 — Food]] records your confirmed unrestricted diet; the old restrictive Korean card has been withdrawn.')
replace('Departure Checklist','- [ ] Confirm passport nationality, departure airport, leave available and total budget. Only nationality is needed for preliminary entry research; do not put passport numbers in this guide.','- [x] Confirmed: Chilean, San Fernando → SCL, solo, $2,500 excluding round-trip international flights.\n- [ ] Choose leave/season and actual Korean nights; check US ESTA/visa status if considering a US transit. See [[Korea 2026 — Flight Routes from Chile]].')
replace('Departure Checklist','Living in Chile does not establish citizenship or exemption.','Chilean nationality is confirmed; Chile’s consular guidance currently says tourists need K-ETA, subject to applicable exemptions.')
replace('Departure Checklist','- [ ] Confirm diet, shellfish/egg/dairy preferences and allergies. Save a suitable Korean food card only after it matches your actual needs.','- [x] Diet confirmed: unrestricted, no reported food allergies, preference for high-protein meals.\n- [ ] Verify gym day-pass registration/fees or hotel equipment and hours; pack workout shoes. See [[Korea 2026 — Fitness and Protein]].')
replace('Practical Info','Passport nationality, age and any existing immigration status remain unconfirmed.','Chilean nationality is confirmed; age and existing authorizations remain unconfirmed. Chile’s [consular guidance](https://www.consulado.gob.cl/chilenas-os-que-viajan-fuera-de-chile) says Chilean tourists need K-ETA. See [[Korea 2026 — Flight Routes from Chile]] for transit-dependent checks.')
notes[key('Transport')]+='\n## Journey from home\n\nHome is San Fernando, Chile; departure airport SCL. See [[Korea 2026 — Flight Routes from Chile]] for airline comparisons, the Turbus airport leg and buffers before international departure. The revised budget includes a separate Chile ground-travel allowance.\n'
if 'The dietary assumption remains unconfirmed.' in notes[key('Itinerary')]: notes[key('Itinerary')]=notes[key('Itinerary')].replace('The dietary assumption remains unconfirmed.','The old dietary restriction is superseded by your unrestricted, high-protein preference.')
notes[key('Session Recap 2026-10-07')]+='''
## Continuation — Chilean profile, flights, gyms and protein

Confirmed by user: Chilean nationality, San Fernando residence, SCL departure, solo travel with flexible dates and nothing booked; US$2,500 excluding round-trip international airfare; unrestricted diet, no food allergies, high-protein preference. Earlier unanswered-profile statements in historical recaps describe the earlier state only.

Added Flight Routes from Chile and Fitness and Protein; linked dashboard, hotel research, food, transport and preparation. Compared indicative November/December 2026 and March 2027 Skyscanner fare leads, with carrier/route limitations; added San Fernando–SCL approach, Turbus airport fare, Chilean K-ETA guidance and conditional US transit checks. Compared five hotel fitness facilities (Asti provider-listed, others official), date-specific hotel listing prices, SpoAny City Hall and Busan commercial gym prices. Removed the active no-meat card; added practical protein meal choices. Revised budget to $2,200 allocated + $300 contingency = $2,500, including gym and Chile ground travel.

Still unresolved: usable leave/season, US authorization, exact flight legs/times/bags/protection, Korean arrival/night count, full hotel tax-inclusive totals and weight equipment, gym foreign-visitor registration/first-join fee, San Fernando service, exact trains and personal insurance/permit costs. No reservation, purchase, application, business message, plugin setting or Japan note changed. Notes retain their 2026 names pending date selection.

Research, backups, staging and provider evidence: `/home/ivanaguilera/Work/korea-fitness-flights-20261007/`. Provider prices checked 7 October 2026; future availability remains unconfirmed.
'''
manifest={}
for n,t in notes.items():
 if t==original.get(n): continue
 if n in original:
  (backup/n).write_text(original[n]); manifest[n]=hashlib.sha256(original[n].encode()).hexdigest()
 else: manifest[n]=None
 (staged/n).write_text(t)
(root/'original-hashes.json').write_text(json.dumps(manifest,indent=2))
sources=[]
for title in ['Fitness and Protein','Flight Routes from Chile']:
 for label,url in re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)',notes[key(title)]):
  sources.append({'publisher_or_page':label,'url':url,'checked':'2026-10-07','publication_date':'2017' if 's12970' in url else 'undated live page or provider response','supports':'See adjacent claim and limitations in '+key(title)})
(root/'source-index.json').write_text(json.dumps(sources,indent=2,ensure_ascii=False))
assert sum([1000,350,70,80,140,110,100,100,85,40,25,70,30])==2200
for n,t in notes.items():
 if n not in manifest: continue
 for target in re.findall(r'\[\[([^\]|#]+)',t):
  target=target.rstrip('\\')
  assert target+'.md' in notes or (vault/(target+'.md')).exists(),(n,target)
print('Staged',len(manifest),'notes; budget and wiki-link targets checked.')
