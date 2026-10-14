from pathlib import Path
from shutil import copy2
p=Path('/home/ivanaguilera/Documents/Obsidian Vault/Japan 2027 — Travel Essentials.md')
s=p.read_text();marker='## 🎒 One week before leaving Santiago'
assert marker in s and '## 📱 Phone and payment backups' not in s
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Travel Essentials-before-backups.md'))
s=s.replace(marker,'''## 📱 Phone and payment backups

These are practical preparation suggestions; test them with your actual devices, bank, and mobile provider.

- [ ] Confirm the phone is unlocked and supports the selected eSIM/SIM; check activation timing, data allowance, and hotspot terms before paying.
- [ ] Decide how to receive bank verification codes abroad; a data-only travel eSIM may not receive calls or SMS sent to your home number. Check roaming charges with your home carrier.
- [ ] Carry a backup physical payment card separately from the main wallet, plus some yen. Confirm overseas use and know the card-freezing procedure.
- [ ] Save hotel addresses in Japanese, confirmations, key contacts, and a simple route offline. Do not rely entirely on live maps or a phone wallet.
- [ ] Prepare secure account-recovery access if the phone is lost; keep recovery codes private and separate from the device.

**If the phone or wallet is lost:** contact the venue/transport operator and local police as appropriate; freeze affected cards and use the device’s lost-mode controls from a trusted device. Use the hotel and [[#📞 Contacts to save offline|contacts card]] for assistance.

## 🌏 Earthquake and weather alerts

- [ ] Install **Safety tips** through JNTO’s official guidance and enable relevant alerts before traveling.
- [ ] On hotel arrival, identify the emergency exits and ask staff about evacuation arrangements.
- [ ] Follow official alerts and staff instructions if a disruption occurs; recheck transport before continuing the itinerary.

JNTO recommends Safety tips among its visitor information tools for natural disasters. [Official JNTO safety guidance and app links](https://faq.japan-travel.jnto.go.jp/en/plan/emergencies/)

## 🗣️ A small offline language kit

- [ ] Download the translation app’s Japanese language pack if supported and test it without mobile data.
- [ ] Save the hotel name/address in Japanese and the names of your next stations.
- [ ] Prepare any food-allergy statement with reliable translation; ask about ingredients and cross-contact. Camera translation alone does not establish that a meal is safe for an allergy.

The main guide already includes [[Japan Travel Guide 2027#🗣️ Useful Japanese phrases|useful Japanese phrases]]. Keep the essentials accessible without searching the full guide.

## 🎁 Bringing matcha and food souvenirs back to Chile

**Official guidance checked 6 October 2026; recheck before returning in 2027.** SAG requires declaration of plant- and animal-origin products carried into Chile. Declare tea/matcha and relevant food souvenirs; commercial or sealed packaging does not remove the declaration obligation. An inspector determines whether entry is permitted. [SAG traveler declaration guidance](https://www.sag.gob.cl/tramites/declaracion-jurada-sag-sobre-ingreso-de-productos-de-origen-vegetal-o-animal-chile) · [SAG entry rules](https://www.sag.gob.cl/ambitos-de-accion/ingreso-chile)

- [ ] Check the specific products with SAG before buying anything whose admission is uncertain.
- [ ] Keep tea and food in original labeled packaging and accessible for inspection.
- [ ] Prepare the required declaration through [SAG’s official portal](https://dj.sag.gob.cl/) or the accepted arrival procedure; do not guess the opening window for 2027.

## ✈️ The evening before leaving Japan

- [ ] Confirm departure airport, terminal, airline check-in deadline, and baggage allowance from the actual ticket.
- [ ] Calculate hotel → airport travel for the real departure day, with time for check-in/security and a disruption buffer; save a backup route.
- [ ] Check checkout time, luggage storage, and any Wi-Fi rental return instructions.
- [ ] Back up photos and pack passport, medicines, payment cards, and flight documents where accessible.
- [ ] Review souvenir declarations for Chile and any requirements at connection airports.

'''+marker,1)
p.write_text(s)
print('Added phone/payment backups, alerts, language preparation, Chile souvenir declarations, and departure checklist.')
