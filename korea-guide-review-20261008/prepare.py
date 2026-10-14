from pathlib import Path
import hashlib,json,re,shutil
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
files=sorted(VAULT.glob('Korea*.md'))
original={p.name:p.read_text() for p in files}
notes=original.copy()
manifest={}
for p in files:
    shutil.copy2(p,ROOT/'backup'/p.name)
    manifest[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
def replace(name,old,new):
    name='Korea 2026 — '+name+'.md'
    assert old in notes[name],(name,old)
    notes[name]=notes[name].replace(old,new)
def intro(name,text):
    name='Korea 2026 — '+name+'.md'
    pos=notes[name].index('\n',notes[name].index('# '))+1
    notes[name]=notes[name][:pos]+'\n'+text+'\n'+notes[name][pos:]
replace('Places Shortlist','**US$150 total**, shared by clothing, records, books and gifts; an allowance awaiting your budget, not a spending target.','**US$80 total**, shared by clothing, records, books and gifts, within the confirmed US$2,500 solo ceiling. This supersedes the earlier US$150 proposal; it is an allocation, not a spending target.')
replace('Shopping shortlist','**US$150 total for clothing, records, books and gifts**, awaiting your budget ceiling.','**US$80 total for clothing, records, books and gifts**, within your confirmed US$2,500 ceiling. This supersedes the US$150 proposal.')
replace('Health preparation','Use [[Korea 2026 — Food]] and confirm allergies separately. Fish-allowed eating does not establish shellfish tolerance.','Use [[Korea 2026 — Food]]: your current profile is an unrestricted diet with no reported food allergies and a preference for high-protein meals. Update the guide if that changes.')
replace('Health preparation','https://www.mfds.go.kr/brd/m_74/view.do?seq=43906','https://www.mfds.go.kr/eng/brd/m_60/view.do?seq=72497')
intro('Health preparation','**8 October procedure update:** MFDS now provides an online application and multilingual manuals for controlled medicines; its notice states online applications began 27 December 2024. Use the current [MFDS permit manual](https://www.mfds.go.kr/eng/brd/m_60/view.do?seq=72497) and [Drug Safety portal](https://nedrug.mfds.go.kr/eng/index). Check the exact active ingredient and current lead time before travel. No medication or permit has been assessed or submitted for you.')
replace('Korean phrasebook',"Dietary phrases express the guide's provisional fish-allowed preference, not an allergy declaration.",'Updated 8 October: your diet is unrestricted, with no reported food allergies. The old meat-exclusion phrases have been replaced with solo-ordering and gym questions.')
replace('Korean phrasebook','| 돼지고기, 소고기, 닭고기는 빼 주세요. | Please leave out pork, beef and chicken. |\n| 고기 육수가 들어가요? | Does it contain meat broth? |\n| 생선은 먹어도 괜찮아요. | Fish is okay for me to eat. |','| 혼자 왔어요. | I am here alone. |\n| 일 인분만 주문할 수 있어요? | Can I order just one serving? |\n| 계란을 추가할 수 있어요? | Can I add an egg? |\n| 일일 이용권이 있어요? | Do you have a day pass? |')
replace('My Five Things','Protect some evening time in Gyeongju on 30 October, subject to entry and lighting details.','Protect one evening in Gyeongju, subject to entry and lighting details. In the nine-night test route, this is 31 October or 1 November; neither date is chosen.')
replace('Bookings','- [ ] Confirm origin, passport, duration, diet and budget.','- [x] Confirmed profile: one Chilean traveler, San Fernando/SCL, unrestricted diet, no reported food allergies, US$2,500 excluding international airfare.\n- [ ] Choose season, year, month and trip length; verify passport validity and route-specific transit authorization.')
replace('Budget','Traveler count, room count and the working ceiling still need confirmation.','Those were unresolved in the original draft. The current confirmed solo profile and ceiling above supersede them; the final room choice remains open.')
replace('Budget','- Clothing has no separate funded line. It must share the US$135 discretionary line or be an explicit additional allowance.','- In this historical worksheet, clothing shared the US$135 discretionary line. In the current solo allocation, all shopping and gifts share US$80.')
replace('Transport','## Intercity legs to price and reserve','## Historical intercity table — previous six-night draft')
replace('Practical Info','Other parts of Chile may use different zones.','Other parts of Chile may use different zones. Because your month is undecided, 12 hours is only the October/November example: when Santiago is UTC−4, Korea is 13 hours ahead. Recalculate both local dates and the offset for the chosen flights.')
replace('Weather and Packing','For planning, prepare for cool evenings,','For the autumn sample only, prepare for cool evenings,')
replace('Weather and Packing','## Packing checklist','## Autumn example packing checklist')
replace('Weather and Packing','Busan: the Biennale is a possible indoor replacement during its verified dates, but the venues are spread out and admissions differ;','Busan: use a museum or a checked café near the chosen base. The 2026 Biennale ends 1 November and cannot serve as a fallback for the current 2–5 November test stay; for another trip within its dates, the venues are spread out and admissions differ;')
intro('Weather and Packing','**Season remains open.** Use [[Korea 2026 — Preparation Before Choosing Dates]] to compare seasonal conditions; adapt this autumn packing example once the month is chosen.')
replace('Photography and Filming','| Day | Suggested subject | Practical adjustment |','## Historical six-night photo outline — reference only\n\nThese dates follow the older route. Use [[Korea 2026 — Solo Plan]] for the current nine-night example and assign these subjects to its city blocks after choosing dates. Autumn subjects apply only if an autumn trip is selected.\n\n| Day | Suggested subject | Practical adjustment |')
replace('Cafés and Shops','None should anchor a journey until matched to a current operator listing and Korean address.','For entries promoted into [[Korea 2026 — Places Shortlist]], use that note\'s evidence and caveats. The remaining names should not anchor a journey until matched to a current operator listing and Korean address.')
for name in list(notes):
    if ' — Pocket ' in name:
        notes[name]=notes[name].replace('Diet card:', 'Food and protein choices:')
intro('Fitness and Protein','**Verification limits, 8 October:** Shilla Stay Mapo\'s operator page still confirms the listed equipment and 06:00–23:00 hours, with guest access from age 16. SpoAny\'s readable branch page confirms the address and equipment, but its earlier price figures could not be reproduced in today\'s readable page; retain them as 7 October research snapshots pending confirmation. Hotel nightly prices and all gym fees below remain search/listing snapshots, not chosen-date checkout totals.')
intro('Practical Info','**Entry recheck, 8 October:** [Chile\'s consular guidance](https://www.consulado.gob.cl/chilenas-os-que-viajan-fuera-de-chile) still directs Chilean tourists to K-ETA. A [KTO notice](https://spanish.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=177&vcontsId=251932) extends temporary exemptions through 31 December 2026 only for the included nationalities; it does not establish Chilean exemption or any 2027 rule. Check age, passport and actual date in the official eligibility tool. Today the K-ETA and e-Arrival portals displayed maintenance (8 October 18:00–9 October 03:00 KST); the fee/processing details below were not freshly accessible. A valid K-ETA and an exemption from needing K-ETA are different cases for arrival declarations. See [[Korea 2026 — Review and Sources 2026-10-08]].')
intro('Start Here','**8 October continuation:** [[Korea 2026 — Review and Sources 2026-10-08|Full 33-note audit and dated sources]] · [[Korea 2026 — Preparation Before Choosing Dates|Prepare before choosing a season]] · [[Korea 2026 — ChatGPT Project Sources|ChatGPT source package]] · [[Korea 2026 — Session Recap 2026-10-08|Latest recap]]. The year in existing note names is a project label, not a confirmed travel year. Flight dates are test searches.')
replace('Start Here','The corrected local notes and [[Korea 2026 — Session Recap 2026-10-07]] are the continuation point.','Use [[Korea 2026 — Session Recap 2026-10-08]] as the latest continuation point; the 7 October recap remains historical context.')
def new(title,body):
    name='Korea 2026 — '+title+'.md'
    assert not (VAULT/name).exists(),name
    notes[name]='---\ncssclasses:\n  - korea-trip\n---\n# Korea 2026 — '+title+'\n\n'+body.strip()+'\n'
new('Preparation Before Choosing Dates','''[[Korea 2026 — Start Here|Dashboard]] · [[Korea 2026 — Review and Sources 2026-10-08|Review and sources]]

Research checked 8 October 2026. Your season, month, year and trip length remain open. The flight searches are tests. One Chilean traveler, San Fernando–SCL, US$2,500 excluding international round-trip airfare, unrestricted diet with high-protein preferences, nothing booked.

## Choose timing by what matters

| Season | Planning implication |
| --- | --- |
| Spring | Compare walking and photography conditions with autumn. Blossoms depend on city and year; do not schedule around an unissued forecast. |
| Summer | Plan for heat, humidity and rain; KTO places the rainy-season overlap around late June–late July and typhoon season broadly June–October. Coastal activities need weather alternatives. |
| Autumn | Layers suit changing temperatures. The current late-October/early-November route is an example; foliage timing is a separate, weather-dependent forecast. |
| Winter | Replace the autumn kit with adequate cold-weather clothing and shorter outdoor blocks; check conditions for each city. |

These are seasonal patterns from [KTO Climate & Seasons](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140636), not a forecast for your visit. Compare spring and autumn first as a planning judgment for your walking/photography interests, then price equal-duration scenarios. The [2026 foliage forecast](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=1593230), published 8 September, places Bukhansan's peak around 4 November. It is not a promise for Seoul streets, Gyeongju, Busan or another year.

## Prepare in a useful order

1. Choose usable leave and a 9–10-night starting scenario. The nine-night model is Seoul 4 + Gyeongju 2 + Busan 3. A final Seoul night adds one night unless you replace a Busan night. [[Korea 2026 — Solo Plan]]
2. Check passport validity, age-dependent Korean entry requirements and transit eligibility for each candidate hub. US authorization remains unknown. Today's official entry portals displayed maintenance; recheck before buying. [[Korea 2026 — Practical Info]]
3. Compare flights with the same traveler count, baggage and approximate trip length. Record SCL departure and Korean arrival separately, total journey time, airport changes, ticket protection and transit documentation. [[Korea 2026 — Flight Routes from Chile]]
4. Quote one room for one adult, exact check-in/out, room category, taxes, full-stay total and timed cancellation deadline. Compare commercial gym visits against the whole hotel premium. [[Korea 2026 — Flights and Stays]] · [[Korea 2026 — Fitness and Protein]]
5. Price actual KORAIL legs, including any return to Seoul. Then fit insurance, Chile ground travel, meals/data and optional activities within the US$2,200 allocation plus US$300 reserve. [[Korea 2026 — Budget]]
6. Review medicines and route-specific health needs. The current [MFDS manual](https://www.mfds.go.kr/eng/brd/m_60/view.do?seq=72497) provides the online controlled-medicine procedure; [CDC's destination page](https://wwwnc.cdc.gov/travel/destinations/traveler/none/south-korea) includes DMZ-region malaria advice for clinical assessment. [[Korea 2026 — Health preparation]]
7. Near departure, refresh opening days, weather alerts, airport services and any selected tour's pickup, language, inclusions and cancellation policy. Prepare offline copies yourself; none have been downloaded or tested by this review.

## Protect the route

Keep cafés, records and shopping inside existing neighborhood blocks. House of Vinyl belongs to Mangwon; BOAN to Seochon; Clique to Euljiro. Gyeongju needs an evening and realistic transfers to its high-speed station. Busan's western sights and eastern coast are separate days. The 2026 Biennale ends 1 November, before the 2–5 November test stay. No optional tour, gym pass or venue is booked.
''')

# Source register and essay are maintained as workspace artifacts and copied into new notes below.
source_text=(ROOT/'source-register.md').read_text()
new('Review and Sources 2026-10-08',source_text)
new('ChatGPT Project Sources','''[[Korea 2026 — Start Here|Dashboard]] · [[Korea 2026 — Review and Sources 2026-10-08|Audit and sources]]

Prepared locally 8 October 2026 for a separate **South Korea Trip** ChatGPT project. No native project was created and no file was uploaded: available tools do not expose those actions.

[Open package instructions](/home/ivanaguilera/Work/korea-guide-review-20261008/chatgpt-project/README.md)

- `Korea — Current Planning Brief and Verified Sources.md`: current facts, open decisions, route, budget and dated evidence.
- `Korea — Travel Essay and Verified Sources.txt`: connected explanation of the trip and preparation choices.
- `Project Instructions.txt`: suggested project instructions.
- `Korea — All Guide Notes Snapshot.md`: complete reviewed notes, with historical content explicitly subordinated to the current brief.

Add the brief and essay to the project's Sources section; paste the instructions into its project instructions. The snapshot is optional detailed context. Local vault changes do not automatically update uploaded files. [Official ChatGPT project guidance](https://learn.chatgpt.com/docs/projects)

Keep Japan in its own project. Its existing essay and today's preparation note are accompanied by a separate [Japan upload package](/home/ivanaguilera/Work/japan-guide-update/chatgpt-project/README.md).
''')
new('Session Recap 2026-10-08','''[[Korea 2026 — Start Here|Dashboard]] · [[Korea 2026 — Review and Sources 2026-10-08|Audit and sources]]

## Completed

Read all 33 existing Korea Markdown notes, including maps and seven historical pocket cards. Backed them up in `/home/ivanaguilera/Work/korea-guide-review-20261008/backup/`. Corrected active US$150 shopping text to the current US$80 allocation, removed superseded meat restrictions from the phrasebook/health guidance, corrected the fixed Wolji date and completed-profile checkbox, and clarified old rail/photo tables and autumn-only packing. Pocket cards now link to food/protein choices rather than a withdrawn diet card. Historical recaps and filenames are preserved.

Rechecked important official sources. Added the current MFDS online medication-permit procedure, flexible-season preparation note, dated source register and local ChatGPT source package. Entry portals displayed maintenance; retained previous fee/timing details with a recheck caveat. SpoAny fees could not be reproduced in today's readable page. No prices were turned into reservations.

The budget arithmetic is US$2,200 allocation + US$300 reserve = US$2,500, excluding international round-trip airfare. The nine-night route is 4+2+3; adding a final Seoul night makes ten unless a Busan night is replaced. Flight searches remain tests, season/year/month/length undecided.

## Next decisions

Choose timing and usable leave; establish existing US transit authorization; compare equal-duration flight scenarios; quote one-adult rooms including taxes; select return airport, actual rail legs and optional DMZ/gym access. Refresh prices, closures and entry rules for the chosen dates.

The native ChatGPT project and uploads remain a manual step because no suitable creation/upload tool is available. The package instructions provide the source files and suggested project instructions. Obsidian rendering/offline maps and business access were not tested.
''')

changes={n:t for n,t in notes.items() if original.get(n)!=t}
for n,t in changes.items(): (ROOT/'staged'/n).write_text(t)
(ROOT/'manifest.json').write_text(json.dumps({n:manifest.get(n) for n in changes},ensure_ascii=False,indent=2))
(ROOT/'inventory.json').write_text(json.dumps({'reviewed':list(original),'changed':list(changes)},ensure_ascii=False,indent=2))
# Check note targets/section anchors against the complete proposed vault.
allnotes={p.stem:p.read_text() for p in VAULT.rglob('*.md')}
allnotes.update({Path(n).stem:t for n,t in notes.items()})
errors=[]
for n,t in notes.items():
    for ref in re.findall(r'\[\[([^\]]+)\]\]',t):
        target=ref.split('|')[0].replace('\\','')
        base,_,anchor=target.partition('#')
        base=base or Path(n).stem
        if base not in allnotes: errors.append((n,target,'missing note'))
        elif anchor and anchor not in re.findall(r'^#{1,6} (.+)$',allnotes[base],re.M): errors.append((n,target,'missing heading'))
assert not errors,errors
assert sum([1000,350,70,80,140,110,100,100,85,40,25,70,30])==2200
print(json.dumps({'reviewed':len(original),'changed_existing':len(changes)-4,'new_notes':4,'wiki_errors':errors},ensure_ascii=False))
