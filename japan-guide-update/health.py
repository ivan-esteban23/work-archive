from pathlib import Path
from shutil import copy2
v=Path('/home/ivanaguilera/Documents/Obsidian Vault')
b=Path('/home/ivanaguilera/Work/japan-guide-update/health-backup');b.mkdir(exist_ok=True)
for name in ['Japan 2027 — Start Here.md','Japan 2027 — Travel Essentials.md']:
 copy2(v/name,b/name)
p=v/'Japan 2027 — Health.md'
assert not p.exists(), 'Health note already exists; review before replacing'
p.write_text('''# 🩺 Japan 2027 — Health preparation

[[Japan 2027 — Start Here|← Dashboard]] · [[Japan 2027 — Travel Essentials|Travel essentials]]

**Official guidance checked: 6 October 2026.** General preparation for the proposed two-week Tokyo–Kyoto trip; personalize it with a clinician and recheck guidance in 2027. These steps reduce risk but cannot guarantee you will avoid illness.

## 📅 Book a pre-travel appointment

- [ ] Aim for **early February 2027**, allowing time for follow-up before the actual Santiago departure date.
- [ ] Bring vaccine records, medication names/doses, allergies, and the itinerary, including transit countries and any rural outings.
- [ ] Discuss ongoing conditions, recent symptoms, walking demands, and long-flight suitability.
- [ ] Ask which examination or tests are appropriate for your history; do not assume a broad blood-test package is necessary.
- [ ] Plan any overdue dental care early enough to recover before travel.

CDC recommends a consultation at least a month before visiting Japan. Earlier review helps if vaccine series or an existing condition need attention. [CDC Japan guidance](https://wwwnc.cdc.gov/travel/destinations/traveler/none/japan) · [Pre-travel consultation framework](https://www.cdc.gov/yellow-book/hcp/preparing-international-travelers/the-pre-travel-consultation.html)

## 💉 Review vaccines with your clinician

- [ ] Check routine protection, especially **measles/MMR**, tetanus-containing vaccines, and seasonal influenza; review current COVID-19 recommendations for your age and health.
- [ ] Discuss **hepatitis A and B** based on prior vaccination, health, age, and activities.
- [ ] Reassess if the itinerary changes to longer rural stays, camping, or higher-risk activities.

CDC does not recommend Japanese encephalitis vaccination for short trips limited to urban areas. Rural exposure can change that assessment. Recommendations are individualized and differ from border-entry requirements. [Current CDC Japan vaccine recommendations](https://wwwnc.cdc.gov/travel/destinations/traveler/none/japan)

## 😷 Reduce respiratory infections

Keep vaccinations current, wash hands regularly, favor well-ventilated spaces, and consider a well-fitting high-filtration mask in crowded indoor places, airports, and public transport. If sick, reduce contact with others and seek advice promptly if you are at higher risk of severe illness. [CDC respiratory-illness prevention](https://www.cdc.gov/respiratory-viruses/prevention/index.html)

## ✈️ Prepare for the long flights

Move your legs and do calf exercises while seated; walk periodically when safe. If you have a previous clot, recent surgery, pregnancy, or another clot-risk factor, ask your clinician about tailored prevention and whether compression stockings are appropriate. Do not start aspirin or blood thinners for a flight on your own. [CDC long-distance travel and blood clots](https://www.cdc.gov/yellow-book/hcp/travel-air-sea/deep-vein-thrombosis-and-pulmonary-embolism.html)

Keep arrival day light, allow sleep and regular meals, and build walking tolerance before the trip. Comfortable, already-tested shoes and breaks fit the guide’s photography days better than an ambitious first-day schedule.

## 🍱 Food, outdoors, and allergies

Wash hands before eating; choose food prepared and stored safely. If pregnant, immunocompromised, or otherwise vulnerable to foodborne illness, discuss avoiding raw or undercooked foods with your clinician. Use sun protection and prevent insect bites during outdoor outings. [CDC Japan health precautions](https://wwwnc.cdc.gov/travel/destinations/traveler/none/japan)

If you have seasonal allergies or asthma, agree on a symptom plan before departure. Record food allergies in Japanese and ask restaurants about ingredients and cross-contact rather than assuming a dish is suitable.

## 💊 Medicines and a small travel kit

- [ ] Check **each active ingredient**, quantity, and any required permission against Japan’s medicine-import rules before packing, including over-the-counter products.
- [ ] Keep regular medicines in labeled original packaging in hand luggage, with a prescription/clinician letter and a supply covering the full journey and foreseeable delays, within permitted limits.
- [ ] Ask a pharmacist about suitable pain/fever relief, any allergy treatment, and oral rehydration sachets; pack plasters/blister dressings, a thermometer, masks, and hand sanitizer.
- [ ] Confirm insurance medical coverage, exclusions for existing conditions, and the assistance number.

Japan allows up to a month’s supply of many ordinary prescription medicines without Import Confirmation, but controlled or prohibited ingredients have separate rules. A foreign prescription alone does not establish permission. [Official Japanese medicine-import guidance](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iyakuhin/kojinyunyu/topics/tp010401-1_00001.html)

## 📞 If you become unwell

Use [[Japan 2027 — Travel Essentials#📞 Contacts to save offline|the contacts card]] and your insurer to find suitable care. Severe breathing difficulty, chest pain, fainting, or a severe allergic reaction needs urgent assessment; in Japan call **119** for an ambulance. Tell clinicians about recent international travel. [JNTO emergency contacts](https://www.japan.travel/en/plan/hotline/)

## 📝 Personal checklist — complete privately

- **Appointment date / clinic:** TBD.
- **Vaccine review and follow-up:** TBD.
- **Medication import check completed:** TBD.
- **Allergy / ongoing-condition plan:** TBD.
- **Insurance assistance / coverage checked:** TBD.

Keep detailed diagnoses, prescriptions, and personal medical records in a private note if sharing the travel guide.
''')
p=v/'Japan 2027 — Start Here.md';s=p.read_text();s=s.replace('| Entry preparation, luggage, arrival, and contacts | [[Japan 2027 — Travel Essentials]] |','| Entry preparation, luggage, arrival, and contacts | [[Japan 2027 — Travel Essentials]] |\n| Pre-travel appointment, vaccines, and staying well | [[Japan 2027 — Health]] |');s=s.replace('| Early 2027 | Recheck blossom forecasts, attraction access, and seasonal event announcements | Full guide’s official schedule check |','| Early 2027 | Recheck blossom forecasts, attraction access, and seasonal event announcements | Full guide’s official schedule check |\n| Early February 2027, adjusted to the actual departure | Pre-travel consultation; review vaccines, medicines, and any health needs | Health |');p.write_text(s)
p=v/'Japan 2027 — Travel Essentials.md';s=p.read_text();s=s.replace('## 🎒 One week before leaving Santiago','## 🩺 Health preparation\n\nOpen [[Japan 2027 — Health]] for the pre-travel appointment, vaccine review, medicine-import checks, and illness-prevention checklist. Aim for early February 2027, adjusted to your actual departure and clinical needs.\n\n## 🎒 One week before leaving Santiago');p.write_text(s)
print('Added linked Health note; existing modified notes backed up.')
