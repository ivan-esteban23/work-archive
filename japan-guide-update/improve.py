from pathlib import Path
import re

v = Path('/home/ivanaguilera/Documents/Obsidian Vault')
main = v / 'Japan Travel Guide 2027.md'
s = main.read_text()
assert '[[Japan 2027 — Start Here' not in s
s = s.replace('Updated: 6 October 2026\n', '''Updated: 6 October 2026

> [!tip] Start here
> Open [[Japan 2027 — Start Here|the planning dashboard]] for the next decisions, budget overview, and links to your daily notes. Keep this guide as the detailed reference.

''', 1)
s = s.replace('**Optional discoveries:**', '**Travel essentials:** [[Japan 2027 — Travel Essentials|🧳 Entry, luggage, arrival, and useful contacts]] — current official guidance and fields to complete before departure.\n\n**Optional discoveries:**', 1)
s = s.replace('The sushi name mentioned may be **Sushiro (スシロー)**, the Japanese sushi chain; this is a likely interpretation, not a confirmed identification.', 'Your selected sushi chain is **Sushiro (スシロー)**, as recorded above in this guide.')
s = s.replace('- Whether Osaka or Nara should be included.', '- Which excursion to choose for 4 April: Uji, Nara, Osaka, or another Kyoto day.')
s = s.replace('**Notion:** import the file using its Markdown import option. This guide uses ordinary headings, tables, links, and checkboxes rather than Obsidian-only features.', '**Notion or another app:** standard Markdown headings, tables, and checkboxes can be imported, but this guide also uses Obsidian wikilinks and callouts. Convert those links and callouts before sharing outside Obsidian; companion notes need exporting separately.')
s = s.replace('Keep this guide as the planning record, then replace TBD values with actual quotes and update the checked date as arrangements become confirmed.', 'Use [[Japan 2027 — Start Here]] to navigate, this guide for itinerary research and budget assumptions, [[Japan 2027 — Bookings]] for confirmed reservations and exact deadlines, and [[Japan 2027 — Today]] for the day’s route. Replace TBD values with actual quotes; update the checked date only for information you rechecked.')
main.write_text(s)

(v / 'Japan 2027 — Start Here.md').write_text('''# 🌸 Japan 2027 — Start Here

[[Japan Travel Guide 2027|📖 Full guide]] · [[Japan 2027 — Bookings|🎟️ Bookings]] · [[Japan 2027 — Today|📱 Today]]

> [!info] Working plan · updated 6 October 2026
> **Arrive in Japan 25 March → depart Japan 8 April 2027: 14 nights.** Tokyo 6 nights → Kyoto 6 nights → Tokyo 2 nights. These are proposed dates; the guide records no confirmed bookings. Departing Santiago on 25 March would produce a different stay length.

## ✅ Your next three actions

- [ ] Confirm traveler count, passport nationality, and whether the US$5,000 in-Japan ceiling is per person.
- [ ] Compare flight itineraries by **local arrival/departure dates**, baggage, connections, and full price; compare Tokyo return with Osaka KIX departure.
- [ ] Compare total hotel quotes for the resulting nights, including taxes, room requirements, station walks, and exact cancellation terms.

Record confirmed choices in the full guide and actual reservations in [[Japan 2027 — Bookings]]. A research idea becomes a commitment only after you choose and book it.

## 🧭 Open decisions in the order they matter

| Decision | Current working assumption | What to record next |
| --- | --- | --- |
| Travelers and rooms | Budget example assumes one traveler | Actual traveler count, rooms, dietary or mobility needs |
| Dates | 25 March–8 April in Japan | Flight dates and local arrival/departure times |
| Return route | Return to Tokyo on 6 April | Compare total cost of KIX departure, including transfers and changed hotel nights |
| Spending ceiling | US$5,000 in Japan; flights separate | Personal ceiling in CLP, currency conversion date and fees |
| Hotel bases | Tokyo → Kyoto → Tokyo | Hotels, full-stay totals, check-in/out, cancellation cutoffs |
| 4 April excursion | Uji, Nara, Osaka, or Kyoto | Choose one; Uji is the guide’s proposed matcha-focused option |
| Paid experiences | Optional; no purchases recorded | Choose only priorities that fit the route and budget |

## 💰 Budget you can use

The full guide allocates **US$3,850 planned spending + US$1,150 reserve = US$5,000**, excluding international flights. This assumes one traveler, 14 nights, and up to 15 calendar days; it is an estimate, not a quote.

- **Accommodation target:** US$2,100 total, averaging US$150 per night including applicable taxes and fees.
- **Meals/drinks target:** US$600 across 15 days.
- **Other planned costs:** US$1,150 for rail, local/airport transport, experiences, connectivity/insurance, shopping, and miscellaneous.
- **Separate costs:** international flights and the guide’s separate equipment purchases.

[[Japan Travel Guide 2027#💵 US$5,000 budget and affordable food plan|Open the category budget]] · [[Japan 2027 — Bookings#💰 Payment summary|Open actual booked commitments]]

Before payment, compare **already committed costs + remaining estimated costs** with the ceiling. Include outstanding balances once; paid amounts are part of the reservation total. Convert each foreign-currency amount using a recorded rate and date, then allow for fees. Keep the reserve visible rather than assigning it to optional shopping.

## 📅 When to revisit the plan

| Trigger | Action | Where to record it |
| --- | --- | --- |
| Flights chosen | Rebuild hotel dates, transfer days, airports, and night count | Full guide and Bookings |
| Each reservation | Save confirmation; record payment and exact cancellation time zone; set a calendar reminder | Bookings |
| Early 2027 | Recheck blossom forecasts, attraction access, and seasonal event announcements | Full guide’s official schedule check |
| Rail purchase | Confirm actual booking window, fare terms, baggage space, and ticket entry method | Bookings and Travel Essentials |
| One week before departing Santiago | Recheck entry/transit requirements, connectivity, offline documents, and first hotel transfer | Travel Essentials |
| Each evening in Japan | Choose tomorrow’s anchor, nearby meal, weather backup, and return plan | Today |

This note does not send reminders. Dates calculated from current ticket rules remain provisional until the provider confirms the 2027 rule.

## 📱 Open the right note

| What you need | Note |
| --- | --- |
| Detailed routes, cafés, shopping, and equipment research | [[Japan Travel Guide 2027]] |
| Reservations, balances, and cancellation deadlines | [[Japan 2027 — Bookings]] |
| Entry preparation, luggage, arrival, and contacts | [[Japan 2027 — Travel Essentials]] |
| One practical day’s plan | [[Japan 2027 — Today]] |
| The experiences that matter most | [[Japan 2027 — My Five Things]] |
| Optional quieter outings | [[Japan 2027 — Hidden Gems]] |
| Memories and favorite photographs | [[Japan 2027 — Memories]] |

## 🌸 Keep the itinerary flexible

Choose **one main outing per half-day**, with a nearby meal and a stop you can skip. Swap outdoor photo blocks using live weather and blossom reports while respecting reservations and hotel dates. The existing flexible days are 30 March, 3/5 April, and 7 April; protect packing time before transfers and departure.

If matcha becomes the priority for 4 April, use [[Japan Travel Guide 2027#🍵 Uji — the strongest new option for your interests|the Uji route]] instead of the Nara/Osaka alternatives. Keep optional discoveries in [[Japan 2027 — Hidden Gems]] until you choose one.
''')

(v / 'Japan 2027 — Travel Essentials.md').write_text('''# 🧳 Japan 2027 — Travel Essentials

[[Japan 2027 — Start Here|← Dashboard]] · [[Japan Travel Guide 2027|Full guide]] · [[Japan 2027 — Bookings|Bookings]]

**New official-source checks: 6 October 2026.** These are current rules and preparation steps, not confirmed 2027 requirements. Recheck before paying for flights and before departure. Fill in personal fields after selecting the route.

## 🛂 Entry and arrival preparation

- [ ] Check the requirements for each traveler’s actual passport; departing from Chile does not establish nationality.
- [ ] Check transit-country requirements for the selected connections, including any airport changes or separate tickets.
- [ ] After booking, prepare Visit Japan Web using the actual arrival flight and accommodation details.
- [ ] Save essential travel documents securely offline and confirm how to display the arrival code before departure.

**Passport-specific starting point:** Japan’s current short-stay exemption list includes Chile, with a usual landing-permission period of 90 days for listed countries without a shorter stated period. Use this only if the traveler holds the relevant passport and meets the applicable conditions; nationality is still unconfirmed in your plan. [MOFA short-stay exemption list](https://www.mofa.go.jp/j_info/visit/visa/short/novisa.html) · [Embassy of Japan in Chile](https://www.cl.emb-japan.go.jp/itpr_ja/procedimientodevisado.html)

**Visit Japan Web:** the Digital Agency provides online arrival procedures for immigration and customs. Access it through the official agency page. Completing the form does not replace checking visa eligibility. [Official Visit Japan Web information and access](https://www.digital.go.jp/en/policies/visit_japan_web)

## 🛬 Arrival card — complete after booking

| Detail | Actual value |
| --- | --- |
| Arrival airport / terminal | TBD |
| Arrival date / local time | TBD |
| First hotel / address in Japanese | TBD |
| Hotel phone / check-in window | TBD |
| Preferred airport-to-hotel route | TBD |
| Final usable departure for that route | TBD — check the actual operating day |
| Late-arrival backup and cost limit | TBD |
| Mobile data activation / backup | TBD |

Choose the transfer after checking the actual hotel entrance, station exit, and luggage needs. Save directions offline. If delayed, check the next operating service and inform the hotel before its check-in cutoff. The guide already has [[Japan Travel Guide 2027#🛬 First-day checklist|a first-day checklist]].

## 🧳 Tokyo–Kyoto luggage decision

Measure **length + width + height**, including protruding handles and wheels, before buying the train ticket.

| Suitcase total dimensions | Current JR Central guidance for ordinary luggage |
| --- | --- |
| Up to 160 cm | Oversized-baggage reservation is not required by size; storage must suit the bag and available space |
| Over 160 cm and up to 250 cm | Reserve a seat with an oversized baggage area |
| Over 250 cm | Cannot be brought aboard under these rules; arrange another solution |

JR Central’s summary distinguishes these size bands. Selecting an ordinary reserved seat does not automatically reserve the oversized area. Recheck the current operator rules and any special-item exceptions before booking. [Official JR Central luggage guidance](https://global.jr-central.co.jp/en/info/oversized-baggage/) · [SmartEX baggage booking steps](https://smart-ex.jp/en/entraining/oversized-baggage/)

- **My suitcase measurements / total:** TBD.
- **Carry or forward:** TBD.
- **Train seat and baggage arrangement:** record in [[Japan 2027 — Bookings]].
- **If forwarding:** confirm both hotels accept it, delivery date, full price, and pickup cutoff. Keep essentials with you until confirmed delivery; do not assume same-day service between Tokyo and Kyoto.

## 📞 Contacts to save offline

| Need | Number / information |
| --- | --- |
| Urgent police help in Japan | **110** |
| Ambulance / fire in Japan | **119** |
| JNTO visitor assistance | **050-3816-2787** in Japan; **+81-50-3816-2787** from overseas |
| Travel insurer assistance / policy | TBD |
| Current hotel / address | TBD |
| Personal contact | TBD |

JNTO lists the visitor hotline as available 24 hours daily in English, Chinese, and Korean. Keep urgent police and ambulance numbers separate from general visitor assistance. [Official JNTO hotline and emergency numbers](https://www.japan.travel/en/plan/hotline/)

## 🎒 One week before leaving Santiago

- [ ] Confirm flights, local dates, hotel nights, and airport transfers agree.
- [ ] Recheck passport and transit requirements using official sources for the actual traveler.
- [ ] Prepare arrival procedures and secure offline confirmations.
- [ ] Test mobile data setup, maps, payment cards, and charging adapters.
- [ ] Confirm suitcase dimensions and any train baggage reservation.
- [ ] Save hotel addresses, insurance contact, and useful numbers offline.
- [ ] Choose the first easy meal and keep arrival-day sightseeing optional.

Use [[Japan 2027 — Today]] for live weather, opening hours, and the route each day. Keep private passport scans and complete booking references out of any publicly shared copy.
''')

today=v/'Japan 2027 — Today.md'
s=today.read_text().replace('[[Japan Travel Guide 2027|← Full travel guide]]', '[[Japan 2027 — Start Here|← Dashboard]] · [[Japan Travel Guide 2027|Full guide]] · [[Japan 2027 — Travel Essentials#📞 Contacts to save offline|📞 Contacts]]', 1)
s=s.replace('- **Return route / last practical service:** …', '- **Return route / last practical service:** …\n- **Must keep today:** reservation time, hotel check-in cutoff, or transfer: …')
today.write_text(s)
print('Updated main guide and Today; added Start Here and Travel Essentials.')
