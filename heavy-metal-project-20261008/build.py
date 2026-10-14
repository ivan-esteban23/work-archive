from pathlib import Path
import hashlib, json, re, urllib.parse, zipfile

base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
stage=base/'staged'
pack=base/'Heavy Metal ChatGPT Project'
(pack/'Sources').mkdir(parents=True,exist_ok=True)
parts=['Start Here','History Styles and Classics','Rankings and Listening Journal','Releases and New Bands 2026','Research and Sources 2026-10-08','ChatGPT Project Instructions','ChatGPT Project Prompts']
titles={p:'Heavy Metal — '+p for p in parts}
def wiki(p): return '[['+titles[p]+']]'
nav=wiki('Start Here')+' · [[Music Prompt Library]]\n\n'
src={
 'history':('Heavy metal music — Wikipedia','https://en.wikipedia.org/wiki/Heavy_metal_music','Editable broad historical orientation; not sole authority for contested origins.'),
 'revival':('NWOTHM — Wikipedia','https://en.wikipedia.org/wiki/New_wave_of_traditional_heavy_metal','Editable orientation: mid-2000s revival; movement rather than a rigid sonic subgenre.'),
 'paranoid':('Black Sabbath Online — Paranoid','https://www.black-sabbath.com/discography/blacksabbath/paranoid/','Independent specialist fan discography, not the official band site. Lists UK 1970 and US 1971; original year here is 1970.'),
 'heaven':('Black Sabbath Online — Heaven and Hell','https://www.black-sabbath.com/discography/blacksabbath/heavenandhell/','Independent specialist discography: UK original release 1980; reissue dates separate.'),
 'priest':('Judas Priest — official discography','https://judaspriest.com/disc/default.asp','Responsible artist catalog: original album years; remaster bonus tracks must not be mistaken for original track lists.'),
 'maiden':('Iron Maiden — official studio albums','https://www.ironmaiden.com/discography/studio-albums/','Responsible artist catalog for original years; does not establish an independent best-album order.'),
 'dio':('Ronnie James Dio — official discography','https://ronniejamesdio.com/discography/','Official catalog used for Holy Diver (1983). Other entries require their own checks before use.'),
 'saxon':('Chris Dick / Decibel — Wheels of Steel','https://www.decibelmagazine.com/2017/01/04/saxon-wheels-of-steel/','Published 2017-01-04; specialist retrospective identifies 1980. Exact day differs from some databases; only the year is used.'),
 'accept':('Restless and Wild — Wikipedia','https://en.wikipedia.org/wiki/Restless_and_Wild','Original 1982 continental Europe versus 1983 UK/US. Editable secondary metadata; cross-check liner notes before edition-specific claims.'),
 'chariots':('Chariots Overdrive — The End of Antiquity','https://chariotsoverdrive.bandcamp.com/album/the-end-of-antiquity','Artist-hosted page: debut album released 2026-04-03; China-origin band based in Atlanta. Promotional quality claims are not independent appraisal.'),
 'telomyras':('Telomyras — Duskfall','https://telomyras.bandcamp.com/album/duskfall','Artist-hosted page: debut full-length released 2026-05-08; Seattle; describes classic/extreme/progressive crossover. Earlier EP listed February 2023.'),
 'kerrigan':('Kerrigan — Wayfarer','https://kerriganheavymetal.bandcamp.com/album/wayfarer','Artist-hosted page: released 2026-03-27; German traditional-metal act; follows Bloodmoon (2023), so not a debut.'),
}
def cite(k):
 a,b,c=src[k]
 return f'[{a}]({b})'
notes={}
first='''Let’s start exploring Heavy Metal together. Read the project instructions and uploaded sources so we can continue from the work already prepared.

Give me an overview of its history, main styles, classic albums, and current discoveries. Start with traditional Heavy Metal while explaining its place in the wider metal family. Distinguish verified research, editorial recommendations, and gaps.

Recommend three contrasting albums to begin with, explain what to notice in each, and ask me one useful question about what I already enjoy. Do not assume I have listened to or rated any album.'''
notes['Start Here']=f'''# Heavy Metal — Start Here

Research snapshot: **8 October 2026**. This is a separate research and listening project, built in the same format as Death Metal and Black Metal.

## Scope

Start with **traditional Heavy Metal**, its historical foundations, NWOBHM, epic and melodic approaches, and modern traditional revival. Explain the wider metal family as context, then label neighboring branches and album-specific hybrids. “Heavy metal” can mean both the whole family and a narrower style; clarify which meaning a question uses. This focus is provisional and can broaden at your request.

## Project notes

'''+ '\n'.join('- '+wiki(p) for p in parts[1:])+f'''
- [[Music Prompt Library]]

## Three starting albums

Suggested learning sequence: **Black Sabbath — Paranoid (1970)** → **Judas Priest — Screaming for Vengeance (1982)** → **Iron Maiden — Powerslave (1984)**. Use these to compare riff foundations, concise songs and vocal power, and longer melodic storytelling. Original years and evidence are in the classics note. This is an editorial exploration order; no personal listening or scores are assumed.

## ChatGPT setup

Suggested name: **Heavy Metal — History, Classics & Discovery**. Unzip the project pack, upload the five text files in Sources, paste Project Instructions.txt into project instructions, and send First Message.txt. The pack also contains 15 reusable prompts. Files are snapshots; this does not create a ChatGPT project or synchronize Obsidian.

## First message

```text
{first}
```

## Next steps

Choose a three-album listening batch, a historical chapter, a regional scene, or a year to rank. Your preferences and listening journal remain empty until you share them. Detailed history and most yearly rankings still need research.
'''
albums=[
 ('Black Sabbath','Paranoid',1970,'Riff foundations','paranoid'),
 ('Judas Priest','Sad Wings of Destiny',1976,'Early dramatic approach','priest'),
 ('Black Sabbath','Heaven and Hell',1980,'Different Sabbath vocal era','heaven'),
 ('Judas Priest','British Steel',1980,'Concise songcraft','priest'),
 ('Iron Maiden','Iron Maiden',1980,'Early Maiden identity','maiden'),
 ('Saxon','Wheels of Steel',1980,'NWOBHM contrast','saxon'),
 ('Iron Maiden','The Number of the Beast',1982,'Dickinson-era entry point','maiden'),
 ('Judas Priest','Screaming for Vengeance',1982,'Vocal and guitar focus','priest'),
 ('Accept','Restless and Wild',1982,'German heavy/speed boundary','accept'),
 ('Dio','Holy Diver',1983,'Dramatic melodic entry','dio'),
 ('Iron Maiden','Powerslave',1984,'Longer-form storytelling','maiden'),
 ('Judas Priest','Painkiller',1990,'Heavy/speed intensity','priest'),
]
rows=[]
for a,t,y,c,s in albums:
 q=urllib.parse.quote(a+' '+t,safe='')
 rows.append(f'| {a} — {t} | {y} | {c} | {cite(s)} · [Spotify title search](https://open.spotify.com/search/{q}) |')
notes['History Styles and Classics']=nav+f'''# Heavy Metal — History, Styles and Classics

Checked **2026-10-08**. This is a starter outline and editorial listening map, not a complete genre history or a claim of direct listening by the assistant.

## Historical outline

**Late 1960s–1970s:** hard rock and blues-derived amplification, riffs, and performance helped form the early metal vocabulary; Black Sabbath, Led Zeppelin, and Deep Purple recur in historical accounts. Their roles and the category’s boundaries are debated. **Late 1970s–1980s:** NWOBHM brought a new British generation alongside older pioneers; international scenes and neighboring branches diversified. **1990s onward:** the wider family continued branching while traditional approaches persisted. Orientation: {cite('history')}.

**Modern revival:** NWOTHM describes a revival movement associated with classic 1970s/1980s sounds from the mid-2000s onward. It overlaps traditional, speed, power, and hard-rock approaches rather than defining one exact sound. Orientation: {cite('revival')}.

Develop later chapters with interviews, specialist histories, and responsible catalog sources: foundations; Priest and Sabbath transformations; NWOBHM beyond Maiden; Germany and continental Europe; US epic/power traditions; Latin America including Chile; Japan and other Asian scenes; women’s contributions; independent labels and modern revival. This chapter plan identifies research work, not completed findings.

## Styles, movements, and neighbors

Working listening cues are a synthesis, not a definitive taxonomy. General orientation: {cite('history')} and {cite('revival')}. Verify labels album by album.

| Category | How to explore it |
| --- | --- |
| Traditional Heavy Metal | Riffs, hooks, expressive vocals, leads |
| NWOBHM | Historical movement with varied sounds |
| NWOTHM | Modern traditional revival |
| Epic heavy metal | Extended dramatic storytelling |
| Melodic approaches | Guitar/vocal melody as a focus |
| Heavy/speed hybrids | Greater pace and attack |
| Heavy/doom hybrids | Weight, space, slower movement |
| US power-related approaches | Compare heavier and epic traditions |
| European power metal | Neighboring branch; define eligibility |
| Progressive approaches | Structural and rhythmic exploration |
| Hard rock / glam overlap | Discuss album-specific boundaries |
| Thrash metal | Related branch, separate core rankings |
| Death / Black Metal | Separate projects; compare hybrids explicitly |

Clean vocals, leather imagery, nationality, or a release date alone do not settle genre classification. NWOBHM is not a synonym for all British metal; older pioneers can influence a movement without belonging to its new generation.

## Twelve classic entry points

This selection is intentionally manageable and UK-heavy; it needs later-decade and geographical expansion. Inclusion is an editorial recommendation, not a measured consensus. Use earliest original release year for annual comparisons. For Accept, 1982 Europe precedes the UK/US 1983 issue; Paranoid similarly predates its US issue.

| Artist / album | Original year | Exploration cue | Evidence / listening |
| --- | --- | --- | --- |
'''+ '\n'.join(rows)+'''

Spotify links are title searches, not verified album objects. Confirm artist, edition, original sequence, bonus tracks, and regional availability before playing.

## Listening paths

**Chronological:** Paranoid → Sad Wings of Destiny → British Steel / Iron Maiden / Wheels of Steel → The Number of the Beast → Holy Diver → Powerslave → Painkiller. Take two or three records at a time.

**By contrast:** compare Priest and Maiden for song structure and guitar roles; Sabbath and Dio for different dramatic settings; Saxon and Accept for another route through early-1980s metal. These are exploration suggestions rather than exclusive labels.

Listen for how riffs connect sections, what bass and drums contribute, how vocal phrases shape hooks, and whether production serves the songs. Historical importance and personal enjoyment should be recorded separately.
'''
pool=[('Judas Priest — British Steel','Concise-song entry point','priest'),('Black Sabbath — Heaven and Hell','A contrasting vocal-era entry','heaven'),('Iron Maiden — Iron Maiden','Early Maiden comparison','maiden'),('Saxon — Wheels of Steel','Broadens the British candidate pool','saxon')]
notes['Rankings and Listening Journal']=nav+'''# Heavy Metal — Rankings and Listening Journal

## Method

Keep editorial recommendations, attributed published lists, and your personal favorites separate. Default scope: traditional Heavy Metal studio full-lengths, first publicly released in the selected year, with hybrids labeled. Broader umbrella rankings require an explicit scope change. Separate EPs, demos, live albums, compilations, and reissues.

Discussion rubric: songwriting/riffs 35%, identity/coherence 25%, performance 20%, production serving the music 20%. This is not a calculated score. Discuss historical influence separately; technical difficulty, sales, and heaviness do not automatically make an album better. Explain pool size, sources, omissions, and uncertainty.

## 1980 starter comparison

Provisional editorial exploration order checked 2026-10-08, limited to four sourced candidates. It is neither a complete best-of-1980 ranking nor a published critic’s list or your rating. The order is intended to introduce contrasts, not imply direct listening by the assistant. Add candidates and independent appraisal before drawing stronger quality conclusions.

| Order | Album | Why explore it | Year evidence |
| --- | --- | --- | --- |
'''+ '\n'.join(f'| {i} | {a} | {r} | {cite(s)} |' for i,(a,r,s) in enumerate(pool,1))+'''

## Annual research archive

1970 is a practical starting point anchored to the classics selection, not an uncontested invention date. Thin pools should have fewer entries rather than padded lists. Future years roll forward with the actual date.

| Year | Status |
| --- | --- |
'''+ '\n'.join(f'| {y} | {"Four-candidate comparison; wider pool pending" if y==1980 else "Discovery snapshot; best-so-far ranking pending" if y==2026 else "Candidate pool and ranking pending"} |' for y in range(1970,2027))+'''

## Personal listening journal

No listens or ratings have been recorded. Preserve your words and leave missing fields blank when you report feedback.

| Date | Artist / album / edition | Full listen or sample | Your reaction / favorite moments | Optional enjoyment score |
| --- | --- | --- | --- | --- |

## Your annual favorites

Empty until you choose them. Personal favorites can differ from classic reputation or editorial recommendations.
'''
notes['Releases and New Bands 2026']=nav+f'''# Heavy Metal — Releases and New Bands 2026

**Checked through 8 October 2026.** A small discovery shortlist, not a comprehensive release census or quality ranking. Responsible artist pages support identity, format, date, and self-description; their promotional praise does not establish independent acclaim.

## Released full-lengths

| Artist | Album | Release date | Discovery category | Evidence / listening |
| --- | --- | --- | --- | --- |
| Chariots Overdrive | The End of Antiquity | 2026-04-03 | Debut album; traditional/epic-power influences | {cite('chariots')} |
| Telomyras | Duskfall | 2026-05-08 | Debut full-length; traditional/progressive/extreme crossover | {cite('telomyras')} |
| Kerrigan | Wayfarer | 2026-03-27 | Modern traditional act; follows Bloodmoon (2023) | {cite('kerrigan')} |

## Emerging bands

Here emerging means **debut/early-discography**, not verified rising popularity. Chariots Overdrive and Telomyras are debut-album leads; formation years have not been established in this starter. Chariots Overdrive describes Chinese origins and a current Atlanta base, with Chinese historical/mythic themes. Telomyras is based in Seattle and has an earlier 2023 EP. Both have source pages above; experienced-member backgrounds need further research.

Kerrigan is a contemporary discovery rather than a debut lead. The artist page lists an earlier full-length, Bloodmoon, in 2023. Exact career history and independent reviews remain to be developed.

## Where to begin

Try Chariots Overdrive for the project’s traditional/epic route, Kerrigan for another modern traditional comparison, and Telomyras for a labeled hybrid contrast. This is an editorial exploration sequence based on scope and metadata, not a claim that any is the best release or that either of us listened.

## Upcoming, EPs, and reissues

No verified upcoming release has been entered yet. The shortlist’s empty upcoming section does not prove there are none. No 2026 EP or reissue has been entered; keep those formats separate as research expands. A historical record newly appearing on Bandcamp is not automatically an original 2026 album.

## Refresh procedure

Use the actual current year and cutoff date. Reopen responsible pages, confirm full release rather than preorder/advance tracks, verify original-versus-edition dates, and add independent appraisal. Expand geography and smaller-label coverage before preparing a best-so-far ranking. No monitoring or release alerts are configured.
'''
notes['Research and Sources 2026-10-08']=nav+'''# Heavy Metal — Research and Sources 2026-10-08

## Session recap

Created seven project notes, 12 classic entry points, a working historical/style outline, four-candidate 1980 comparison, pending annual archive, blank listening journal, and three verified 2026 full-length discovery leads. Added instructions and 15 prompts under Music Prompts and linked the shared index. Prepared five ChatGPT upload sources, setup files, and a first chat message. No app project was created, uploads made, music played, or playlist saved.

## Source register

All pages below were opened on **2026-10-08**. This register states uses and limits; artist pages support their own catalog metadata, while specialist criticism supports attributed interpretation.

| Source | Use / limits |
| --- | --- |
'''+ '\n'.join(f'| [{a}]({u}) | {l} |' for a,u,l in src.values())+'''

## Evidence gaps and next session

- Scope defaults to traditional Heavy Metal; broaden only with an explicit eligibility discussion.
- History and style map are starter outlines. Detailed chapters, disputed origin accounts, and album-specific boundary examples need more responsible sources.
- The classics pool favors the UK and early decades. Add more countries and modern recordings, including Chile and Japan, with verified catalog evidence.
- Annual rankings remain research tasks; the 1980 order is only a small exploration comparison.
- The 2026 shortlist has three records; it does not establish the year’s best albums or bands. Broaden the pool and consult independent reviews.
- Sabbath metadata uses an independent specialist site, not the band’s official site. Accept metadata is provisional secondary-source evidence; edition-specific claims need further checking.
- Formation years for emerging leads remain unknown. Do not equate new albums with new bands or publicity with critical consensus.
- Sources in ChatGPT are snapshots. Replace them after substantive vault changes; no automatic synchronization exists.

Next useful work: collect your initial preferences; compare three classics; develop the 1970s-to-NWOBHM history; or build a broader annual pool before ranking it.
'''
instructions='''You are my Heavy Metal research and listening partner. Help me explore history, styles, classics, overlooked records, current releases, annual rankings, and emerging artists. Build my taste from explicit feedback without inventing preferences, listens, or scores.

Read 01_Project_Context_and_Method.txt first. Initial research was checked 8 October 2026; my latest decisions override older snapshots. Keep this project’s listening history and preferences separate from Death Metal, Black Metal, other music, and travel. Obsidian and uploaded sources do not automatically synchronize. Prepare named Markdown updates and replacement snapshots when asked; never claim saves or uploads without evidence.

Default scope is traditional Heavy Metal and its historical foundations, with wider metal history for context. The name also describes an umbrella family: clarify which meaning a question uses. Discuss NWOBHM and NWOTHM as movements, epic and melodic approaches as overlapping descriptors, and heavy/speed, heavy/doom, US power-related and progressive hybrids with album-specific evidence. Explain hard rock, glam, European power, thrash, death, black, and other neighboring branches without placing every metal album in a core traditional ranking. Broaden scope when I ask. Do not claim a fixed complete taxonomy or treat imagery, clean singing, geography, and platform tags as sufficient classification.

Build chronological chapters from late-1960s precursors and 1970s foundations through late-1970s/1980s NWOBHM, international development, subsequent decades, and the modern traditional revival. Include riffs, vocal approaches, bass/drum roles, guitar harmony, composition, production, labels, artwork, touring, distribution, and cultural context. Cover the UK, continental Europe, US/Canada, Latin America including Chile, Japan and other Asian scenes, and other documented regions. Investigate women’s contributions and overlooked artists. Distinguish pioneers influencing a movement from its younger generation. Compare disputed origin accounts rather than declaring an uncontested inventor; avoid assuming regional uniformity.

Explain music in accessible language, then deepen analysis as useful. Separate historical significance from musical appeal and my enjoyment. For metadata prefer artist/label catalogs, liner notes, and responsible discographies. Use named specialist reviews, interviews, and historical research for reputation and interpretation. Open sources before relying on them. Link near claims, date current checks, label promotional copy, and cross-check material conflicts. Independent fan sites and editable databases can help but are not official sources. Never imply a whole book was read when only a publisher page was consulted. Do not invent quotations, tracks, credits, dates, awards, metrics, or consensus.

For this year use the actual current calendar year and state the cutoff; initially 2026. Verify original release identity, format, and full-release status. Separate studio full-lengths, upcoming announcements, EPs/demos/splits, singles, live records, compilations, and reissues/remasters. A preorder with previews is not a released full album. Do not rank an unavailable record as though heard. Current-year orders are best so far, not final year-end lists. Historical rankings use earliest original public release years, explaining regional dates and edition differences rather than using a streaming reissue date.

Maintain three ranking types: your editorial recommendation, attributed published critic/community lists, and my personal favorites. State eligibility, candidate pool, criteria, evidence, and omissions. Default pool is traditional Heavy Metal original studio full-lengths first released in the chosen year; label hybrids and offer core-only alternatives. Wider umbrella rankings require explicit scope. Work through annual pools from 1970 onward without padding thin years or presenting an unresearched archive as complete. Discussion rubric: songwriting/riffs 35%, identity/coherence 25%, performance 20%, production serving the music 20%. Historical impact is separate. Avoid invented precision, incompatible rating averages, and claims that sales, heaviness, speed, or technical difficulty automatically measure quality. Explain provisional placements and alternatives.

Define new bands each time: newly formed, debut/early-discography, rising, or new to me. Default to debut/early-discography with evidence; experienced musicians in a new project may qualify but should be labeled. Formation and debut dates can differ. New albums by established acts do not make new bands. Keep emerging projects and established contemporary discoveries separate. Use geographic/style variety without inventing formation dates, popularity thresholds, or praise.

Recommend three to five albums at a time with exact artist/title, original year, reason, practical listening cues, evidence, and links. Distinguish direct verified album links from clearly labeled title searches. Confirm edition and availability where relevant. Do not claim direct listening without supported audio access; use cited analysis and my supplied reactions. Summarize themes without reproducing full lyrics. Do not purchase, publish, modify my library, save playlists, configure alerts, or claim playback unless asked and a tool succeeds.

Keep the journal empty until I report listening. Preserve my words, date if supplied, exact album/edition, full listen versus sample, favorite moments, response to riffs/vocals/melody/rhythm/production, and optional score. Leave missing fields blank. Ask one useful preference question at a time and recommend two close matches plus one contrasting experiment. Avoid gatekeeping and let personal favorites differ from accepted classics.

Respond in the language I use. Lead with a useful recommendation and explain it. Use compact comparison tables when helpful. After substantial research state what is verified, editorial interpretation, and still unresolved; suggest the next listening or research step. Build gradually without calling a starter survey the whole history or a completed annual ranking archive.
'''
assert len(instructions)<8000
notes['ChatGPT Project Instructions']=nav+'# Heavy Metal — ChatGPT Project Instructions\n\nPaste the complete block into project instructions.\n\n```text\n'+instructions+'```\n'
prompts=[
 ('Start the project',first),
 ('History in chapters','Create a sourced chapter plan for Heavy Metal from precursors through the 1970s, NWOBHM, international scenes, later decades, and traditional revival. Start the first chapter. Compare disputed origins and explain music, labels, production, distribution, and cultural context. Do not present an outline as the whole history.'),
 ('Map styles and neighbors','Explain traditional Heavy Metal, NWOBHM, NWOTHM, epic/melodic approaches, and neighboring speed, doom, power, progressive, hard rock/glam, thrash, death, and black branches. Distinguish style, movement, scene, and descriptor. Give two sourced album examples where supported and label disputed boundaries.'),
 ('Classic albums','Recommend five classic or overlooked albums for [era/style], with original years, edition notes, historical role, musical appeal, and sourced listening links. Include varied artists rather than only Maiden and Priest. Distinguish reputation from my enjoyment.'),
 ('NWOBHM beyond famous names','Research NWOBHM beyond Iron Maiden. Explain the scene and discover lesser-known recordings with verified years, roles, and sources. Distinguish older influences from the new generation and do not assume all British metal is NWOBHM.'),
 ('Modern traditional revival','Explain NWOTHM and recommend contrasting contemporary entry albums with verified dates. Compare revival, influence, and originality through attributed criticism. Keep established acts separate from debut projects.'),
 ('Regional scene','Research Heavy Metal in [country/region, for example Chile, Japan, Germany, or the US]. Develop sourced local history, classic albums, modern artists, and stylistic variety without treating a nation as one sound. Identify remaining gaps.'),
 ('Rank one year','Build a top [five/ten] for [year]. Start with traditional Heavy Metal original studio albums; state candidate pool, hybrid eligibility, original years, criteria, evidence, and omissions. Separate editorial order, published lists, and my favorites. Do not invent scores or pad thin pools.'),
 ('Develop annual archive','Research [year range] one year at a time. Verify candidates before ranking, use original rather than reissue years, and track gaps and confidence. Compare named published lists without inventing consensus. Prepare Markdown updates for the annual archive.'),
 ('Current releases','Search the actual current calendar year through today. State cutoff and scope, verify responsible artist/label pages, and separate released full albums, upcoming announcements, EPs/demos/splits, and reissues. Include smaller acts and varied scenes. Recommend three priorities without ranking an unavailable album.'),
 ('Emerging bands','Find promising debut/early-discography Heavy Metal projects for [year/style/region]. Verify debut and formation details where possible, label experienced-member projects and unknown dates, and give entry albums plus independent appraisal where available. Do not call established acts new because of a new album.'),
 ('Compare albums','Compare [album A] and [album B] on songwriting, identity, performance, production, and context. Verify original years and editions, use cited analysis and my feedback, and do not claim direct listening. Explain the best reason to try each.'),
 ('Record my feedback','I listened to [artist/album/edition], [full album/sample]. My reaction: [feedback]. Optional date/score: [details]. Preserve my words in the journal and leave missing fields blank. Recommend two close matches and one contrasting experiment, with one useful follow-up question.'),
 ('Listening sequence','Plan a [length]-track or [number]-album sequence for [era/style/mood]. Verify identities, link official recordings or label title searches, and explain the progression. Do not claim playback or save a playlist unless I ask and the action succeeds.'),
 ('Continue and refresh notes','Summarize verified research, editorial recommendations, my explicit feedback/decisions, and remaining gaps. Prepare named Markdown updates for the relevant notes and identify uploaded snapshots to replace. Do not claim automatic Obsidian synchronization, saves, or uploads.'),
]
notes['ChatGPT Project Prompts']=nav+'# Heavy Metal — ChatGPT Project Prompts\n\nCopy one prompt into this project and replace bracketed fields.\n\n## Research add-on\n\n```text\nBrowse as of today and open sources. Verify album identity, original year, edition, format, release status, and scope. Cite sources near claims. Separate fact, promotion, classification, editorial recommendation, and my reactions. Do not invent listening, scores, or consensus.\n```\n\n'+'\n'.join(f'## {i}. {t}\n\n```text\n{p}\n```\n' for i,(t,p) in enumerate(prompts,1))
manifest=[]
for part,content in notes.items():
 rel=Path('Music Prompts')/(titles[part]+'.md') if part.startswith('ChatGPT') else Path(titles[part]+'.md')
 assert not (vault/rel).exists(),rel
 target=stage/rel
 target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(content,encoding='utf-8')
 manifest.append({'relative':str(rel),'expected':None})
rel=Path('Music Prompts/Music Prompt Library.md')
raw=(vault/rel).read_bytes()
text=raw.decode()
assert '| Heavy Metal |' not in text
lines=text.splitlines(keepends=True)
i=next(i for i,l in enumerate(lines) if l.startswith('| Black Metal |'))+1
lines.insert(i,'| Heavy Metal | [[Heavy Metal — ChatGPT Project Prompts|15 project prompts]] | [[Heavy Metal — ChatGPT Project Instructions|Paste-ready instructions]] | [[Heavy Metal — Start Here]] |\n')
(stage/rel).write_text(''.join(lines),encoding='utf-8')
backup=base/'backup'/rel
backup.parent.mkdir(parents=True,exist_ok=True)
backup.write_bytes(raw)
manifest.append({'relative':str(rel),'expected':hashlib.sha256(raw).hexdigest()})
(base/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
slugs=['Project_Context_and_Method','History_Styles_and_Classics','Rankings_and_Listening_Journal','Releases_and_New_Bands_2026','Research_and_Sources_2026-10-08']
exports={p:f'{i:02d}_{s}.txt' for i,(p,s) in enumerate(zip(parts[:5],slugs),1)}
def plain(content):
 def replace(m):
  name=m.group(1).split('|')[0]
  for k,t in titles.items():
   if name==t: return name+' [see '+(exports[k] if k in exports else 'project setup files')+']'
  return name+' [vault navigation]'
 return re.sub(r'\[\[([^\]]+)\]\]',replace,content)
for p,f in exports.items(): (pack/'Sources'/f).write_text(plain(notes[p]),encoding='utf-8')
(pack/'Project Instructions.txt').write_text(instructions,encoding='utf-8')
(pack/'Project Prompts.txt').write_text(plain(notes['ChatGPT Project Prompts']),encoding='utf-8')
(pack/'First Message.txt').write_text(first+'\n',encoding='utf-8')
(pack/'README.md').write_text('''# Heavy Metal ChatGPT Project

Snapshot checked 8 October 2026. Suggested name: Heavy Metal — History, Classics & Discovery.

1. Create a separate project in ChatGPT.
2. Unzip this pack and upload the five text files under Sources.
3. Paste Project Instructions.txt into project instructions.
4. Send First Message.txt to begin chatting, then use Project Prompts.txt.

Default scope is traditional Heavy Metal, with the broader family as context. The pack contains original summarized notes and source links, not copied full articles. It includes 12 classics, a four-candidate 1980 comparison, a pending annual archive, and three 2026 discovery albums. Detailed history and yearly rankings still need development. Personal listening is empty.

These files do not create an app project, upload themselves, configure alerts, or synchronize with Obsidian. Refresh source snapshots after changes and recheck time-sensitive information.
''',encoding='utf-8')
with zipfile.ZipFile(base/'Heavy Metal — ChatGPT Project Pack.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(pack.rglob('*')):
  if p.is_file(): z.write(p,Path(pack.name)/p.relative_to(pack))
print(f'Staged seven notes and index update; {len(prompts)} prompts; instructions {len(instructions)} characters; ZIP ready.')
