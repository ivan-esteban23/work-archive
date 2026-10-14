from pathlib import Path
import hashlib, json, re, shutil, urllib.parse, zipfile

BASE = Path(__file__).resolve().parent
VAULT = Path('/home/ivanaguilera/Documents/Obsidian Vault')
STAGE = BASE / 'staged'
PACK = BASE / 'Black Metal ChatGPT Project'
PACK.mkdir(exist_ok=True)
(PACK / 'Sources').mkdir(exist_ok=True)
DATE = '2026-10-08'
names = ['Start Here', 'History Subgenres and Classics', 'Rankings and Listening Journal', 'Releases and New Bands 2026', 'Research and Sources 2026-10-08', 'ChatGPT Project Instructions', 'ChatGPT Project Prompts']
titles = {x: 'Black Metal — ' + x for x in names}
def link(x): return '[[' + titles[x] + ']]'
nav = link('Start Here') + ' · [[Music Prompt Library]]\n\n'
sources = {
 'venom': ('Venom / BMG: In Nomine Satanas anniversary flyer', 'https://venomslegions.com/news/ads-mags-pix/venom-40yearsinsodom-flyer-2019.pdf', 'Artist-hosted 2019 catalog flyer identifies Black Metal as 1982 and the source of the genre name; promotional influence claims are not independent consensus.'),
 'overview': ('MasterClass: Black Metal Music Guide', 'https://www.masterclass.com/articles/black-metal-music-guide', 'Updated 2021-08-03; short first/second-wave overview. Simplifies international development; avoid treating every sonic description as universal.'),
 'taxonomy': ('Wikipedia: Black metal', 'https://en.wikipedia.org/wiki/Black_metal', 'Editable orientation to styles and boundaries; follow its references for deeper claims.'),
 'nineties': ('Dayal Patterson / Metal Hammer: 20 of the best black metal albums from the 1990s', 'https://www.loudersound.com/features/20-of-the-best-black-metal-albums-from-the-1990s', 'Published 2016-07-20. Attributed critical selection and original album years; neither consensus nor the user’s ranking. An inconsistent Mystifier formation claim was excluded.'),
 'darkthrone': ('Peaceville: Darkthrone', 'https://peaceville.com/bands/darkthrone/', 'Responsible label: 1992–1994 catalog years and current hybrid description. Promotional appraisal is not independent criticism.'),
 'bathory': ('Apple Music: Under the Sign of the Black Mark', 'https://music.apple.com/us/album/under-the-sign-of-the-black-mark/290061167', '1987 album metadata; digital edition track counts may differ from the original LP.'),
 'emperor': ('Metal Hammer: Emperor and In the Nightside Eclipse', 'https://www.loudersound.com/features/emperor-band-story-behind-in-the-nightside-eclipse', 'Retrospective history of the 1994 debut; exact release day not asserted here.'),
 'twohunters': ('Wolves in the Throne Room: Two Hunters', 'https://wolvesinthethroneroom.bandcamp.com/album/two-hunters', 'Artist-hosted catalog: released 2007-09-25; atmospheric black metal tags.'),
 'mayhem26': ('Apple Music: Liturgy of Death', 'https://music.apple.com/us/album/liturgy-of-death/1846578494', 'Released 2026-02-06; full album metadata. Artist interview/editorial content does not establish consensus.'),
 'winter': ('Winterfylleth: The Unyielding Season', 'https://winterfylleth.bandcamp.com/album/the-unyielding-season', 'Artist-hosted page: released 2026-03-27; ninth album, atmospheric black metal; established act.'),
 'hieron': ('Hieron: From the Temple to the Grave', 'https://hieron.bandcamp.com/album/from-the-temple-to-the-grave', 'Artist-hosted page: debut album, melodic black metal, Görlitz; released 2026-01-30. Formation year not established.'),
 'nine': ('Nine Spears: Nine Spears', 'https://ninespears.bandcamp.com/album/nine-spears', 'Artist-hosted page: English solo project formed 2024; debut album released 2026-03-07.'),
 'vithial': ('Vithial: Awakened Ancient Spirits', 'https://vithial.bandcamp.com/album/awakened-ancient-spirits', 'Artist-hosted page: debut full-length, melodic black/death, Pensacola; released 2026-06-05. Formation year not established.'),
 'bruul': ('Bruul: Bruul - EP', 'https://bruul.bandcamp.com/album/bruul-ep', 'Artist-hosted page: debut EP released 2026-08-31; black/doom tags. Earlier demo listed September 2025; formation year not established.'),
 'dark26': ('Apple Music: Pre-Historic Metal', 'https://music.apple.com/us/album/pre-historic-metal/1881564845', 'Released 2026-05-08. Cross-check classification with Peaceville rather than treating the platform category as decisive.'),
 'gaerea': ('Apple Music: Loss', 'https://music.apple.com/us/album/loss/1843578156', 'Released 2026-03-20; platform labels it Metal. Album-level subgenre classification remains a research task.'),
 'estuary': ('Wolves in the Throne Room: Estuary (North America Edition)', 'https://wolvesinthethroneroom.bandcamp.com/album/estuary-north-america-edition', 'Preorder page announces 2026-10-23; two advance tracks available at check. Full album still upcoming on 2026-10-08.'),
 'book': ('Cult Never Dies: Black Metal — Evolution of the Cult', 'https://www.cultneverdies.com/books/black-metal-evolution-of-the-cult', 'Publisher page for Dayal Patterson’s book/expanded edition. Reading lead only: the book itself was not read for these notes.'),
}
def cite(key):
    title, url, _ = sources[key]
    return f'[{title}]({url})'

notes = {}
notes['Start Here'] = f'''# Black Metal — Start Here

Research snapshot: **8 October 2026**. A separate music project for history, styles, classics, annual album comparisons, emerging artists, and personal listening discovery. This is a researched starter, not a completed history or every-year ranking archive.

## Project notes

- {link('History Subgenres and Classics')}: chronology, style map, 12 classic entry points.
- {link('Rankings and Listening Journal')}: provisional 1994 comparison, annual archive, your blank journal.
- {link('Releases and New Bands 2026')}: released albums, debut leads, EPs, and upcoming material.
- {link('Research and Sources 2026-10-08')}: evidence, limitations, next research steps.
- {link('ChatGPT Project Instructions')}: paste-ready project instructions.
- {link('ChatGPT Project Prompts')}: 15 reusable prompts.
- [[Music Prompt Library]]: shared home for all music projects.

## Three contrasting starting points

My suggested exploration order is **Bathory — Under the Sign of the Black Mark**, **Emperor — In the Nightside Eclipse**, then **Wolves in the Throne Room — Two Hunters**. Compare first-wave roots, an orchestral second-wave approach, and a later atmospheric direction. Original years and sources are in the classics table. This is an editorial learning sequence, not a claim that you have listened or that these are universally the best.

If you want the starker Norwegian route, try **Darkthrone — A Blaze in the Northern Sky** before Emperor. If harsh production is difficult, start with the atmospheric path and return to the early records later.

## Create the ChatGPT project

Suggested name: **Black Metal — History, Classics & Discovery**. The workspace download pack contains five text sources, instructions, prompts, a first message, and a README. Unzip it; upload the five files under Sources and paste the instruction block into project instructions. The pack is a dated snapshot. Creating these files does not create the project inside ChatGPT or synchronize future Obsidian changes.

## Next decisions

Share any bands you already like and whether you prefer raw aggression, melody, atmosphere, or experimentation. Then choose a three-album batch or a year to research. No preferences or personal scores have been assumed.
'''

classics = [
 ('Venom', 'Black Metal', 1982, 'First-wave naming landmark', 'venom'),
 ('Bathory', 'Under the Sign of the Black Mark', 1987, 'Early Scandinavian foundation', 'bathory'),
 ("Master’s Hammer", 'Ritual', 1991, 'Czech bridge between waves', 'nineties'),
 ('Darkthrone', 'A Blaze in the Northern Sky', 1992, 'Norwegian transformation', 'darkthrone'),
 ('Immortal', 'Pure Holocaust', 1993, 'Fast, icy attack', 'nineties'),
 ('Emperor', 'In the Nightside Eclipse', 1994, 'Layered orchestral ambition', 'emperor'),
 ('Mayhem', 'De Mysteriis Dom Sathanas', 1994, 'Distinctive vocal/drum identity', 'nineties'),
 ('Rotting Christ', 'Non Serviam', 1994, 'Greek scene contrast', 'nineties'),
 ('Ulver', 'Bergtatt', 1995, 'Folk and clean-vocal contrast', 'nineties'),
 ('Dissection', "Storm of the Light’s Bane", 1995, 'Melodic black/death boundary', 'nineties'),
 ('Satyricon', 'Nemesis Divina', 1996, 'Norwegian mid-decade contrast', 'nineties'),
 ('Wolves in the Throne Room', 'Two Hunters', 2007, 'Atmospheric American direction', 'twohunters'),
]
rows = []
for artist, album, year, cue, source in classics:
    query = urllib.parse.quote(f'{artist} {album}', safe='')
    rows.append(f'| {artist} — {album} | {year} | {cue} | {cite(source)} · [Spotify title search](https://open.spotify.com/search/{query}) |')
notes['History Subgenres and Classics'] = nav + f'''# Black Metal — History, Subgenres and Classics

Checked {DATE}. The listening routes and cues below are editorial suggestions grounded in the cited sources, not claims of direct audio listening.

## Historical outline

**1980s roots:** Venom, Bathory, and Hellhammer helped shape the first wave. **Early 1990s Norway:** Mayhem, Darkthrone, Emperor, Burzum, Immortal, and others sharpened the sound around an interconnected underground. Murder and church burnings were part of that scene’s history, but do not explain every musical development or international artist. This outline uses {cite('overview')}.

**Beyond Norway:** Czech, Greek, Swedish, and Finnish records offer parallel listening routes. The 1990s selection below makes those contrasts visible; it is not an origin census. See {cite('nineties')}.

**Later expansion:** use Two Hunters (2007) as one American atmospheric entry point, not the invention of that style. Artist catalog: {cite('twohunters')}. Subsequent research should develop the 2000s–2020s in separate sourced chapters.

History chapters still needed: precursors and tape trading; independent labels; Norwegian events with corroborated chronology; Greece/Finland/Sweden; Central/Eastern Europe; US/Canada; Latin America including Chile; Asia and other documented scenes; digital distribution and modern crossover. Regional membership does not imply every band shares a sound or ideology.

## Working style map

These practical cues are a provisional synthesis, not a fixed universal taxonomy. Orientation: {cite('taxonomy')} and {cite('overview')}. Album-specific examples and boundaries should be researched before expanding each branch.

| Style / descriptor | Listening cue |
| --- | --- |
| Traditional / second-wave | Tremolo riffs, harsh vocals |
| Raw | Abrasive, sparse recording |
| Melodic | Foregrounded guitar melody |
| Symphonic | Orchestral/keyboard layers |
| Atmospheric | Long immersive structures |
| Ambient black metal | Ambient textures alongside metal |
| Folk / pagan-associated | Folk material; thematic overlap |
| Black/doom | Doom weight and pacing |
| Depressive / DSBM | Despair-centered expressive approach |
| Black/death | Death-metal hybrid vocabulary |
| War metal / bestial | Dense black/death extremity |
| Black/thrash | Thrash-driven attack |
| Black ’n’ roll | Rock-oriented rhythmic drive |
| Industrial | Electronic/mechanical textures |
| Avant-garde / dissonant | Unconventional harmony/structure |
| Post-black / blackgaze | Post-rock/shoegaze crossover |

Raw is often a production description; Hellenic is a regional label; pagan can describe themes; Viking metal and dungeon synth are neighboring categories with overlapping personnel. NSBM and RABM concern ideology, not a distinctive sonic recipe. Never infer affiliations from imagery or geography alone. Cite reliable evidence when a specific artist’s politics matter to a question.

## Twelve classic entry points

Original years are used; title searches may return reissues, covers, or unrelated editions. Confirm the artist and version before playing. A search link is not a verified album URI or proof of availability in your region.

| Artist / album | Original year | Why include it | Evidence / listening |
| --- | --- | --- | --- |
''' + '\n'.join(rows) + '''

## Listening routes

**Chronological:** Venom → Bathory → Master’s Hammer → Darkthrone → Emperor/Mayhem → Ulver → Two Hunters. Take two or three at a time.

**By sound:** compare Darkthrone/Mayhem for starkness and identity; Emperor for layering; Rotting Christ/Dissection for contrasting melodic approaches; Ulver/Two Hunters for folk and atmosphere. These groupings are navigation aids, not exclusive labels.

For each album note how riffs change, whether repetition creates momentum or immersion, how vocals sit in the mix, and whether production supports the music. A classic’s historical importance and your enjoyment can differ.
'''

rankrows = [
 ('Emperor — In the Nightside Eclipse', 'A strong first comparison for layering and ambition.', 'emperor'),
 ('Mayhem — De Mysteriis Dom Sathanas', 'A contrasting reference for vocal and rhythmic identity.', 'nineties'),
 ('Darkthrone — Transilvanian Hunger', 'An austere counterpoint to elaborate arrangements.', 'darkthrone'),
 ('Rotting Christ — Non Serviam', 'Broadens the pool beyond Norway.', 'nineties'),
 ('Gorgoroth — Pentagram', 'Adds another early Norwegian comparison.', 'nineties'),
]
notes['Rankings and Listening Journal'] = nav + '''# Black Metal — Rankings and Listening Journal

## Ranking method

Keep **editorial recommendations**, **attributed published lists**, and **your personal favorites** separate. Default eligibility: original studio full-lengths first publicly released in the year, with hybrids labeled. Keep demos, EPs, splits, compilations, live records, and reissues separate. Research original dates independently of streaming-edition dates.

Suggested discussion rubric: songwriting/riffs 35%, atmosphere/identity/coherence 25%, performance 20%, production serving the music 20%. It is a framework, not calculated scores. Rawness, technical difficulty, sales, and historical importance do not automatically mean higher quality. Explain criteria and gaps; do not fabricate scores or listening.

## 1994 starter comparison

Provisional editorial exploration order checked 2026-10-08, limited to the five candidates below. It is not an exhaustive best-of-1994 judgment, a published critic’s order, or a personal rating. Placements reflect useful contrasts and documented reputation rather than direct listening by the assistant. Expand the candidate pool before producing a definitive annual recommendation.

| Order | Album | Editorial reason | Year evidence |
| --- | --- | --- | --- |
''' + '\n'.join(f'| {i} | {a} | {reason} | {cite(s)} |' for i,(a,reason,s) in enumerate(rankrows,1)) + '''

## Annual archive

1982 is an organizational starting point anchored to Venom’s title, not a claim that every year has an adequate core-black-metal album pool. Future years should roll forward with the actual calendar year. Each row is research status, not an empty personal ranking.

| Year | Status |
| --- | --- |
''' + '\n'.join(f'| {y} | {"Five-candidate comparison above; broader research pending" if y == 1994 else "2026 discovery snapshot; best-so-far ranking pending" if y == 2026 else "Candidate pool and ranking pending"} |' for y in range(1982,2027)) + '''

## Personal listening journal

No listens, scores, or favorites have been recorded. Add entries only from your feedback.

| Date | Artist / album / edition | Full listen or sample | Your reaction / favorite moments | Optional enjoyment score |
| --- | --- | --- | --- | --- |

## Your annual favorites

Empty until you choose them. A personally loved album need not top the historical or editorial list.
'''

released = [
 ('Mayhem', 'Liturgy of Death', '2026-02-06', 'Established Norwegian act', 'mayhem26'),
 ('Winterfylleth', 'The Unyielding Season', '2026-03-27', 'Established atmospheric act; ninth album', 'winter'),
 ('Hieron', 'From the Temple to the Grave', '2026-01-30', 'Debut album; melodic black metal; Germany', 'hieron'),
 ('Nine Spears', 'Nine Spears', '2026-03-07', 'Debut album; English solo project formed 2024', 'nine'),
 ('Vithial', 'Awakened Ancient Spirits', '2026-06-05', 'Debut full-length; melodic black/death; US', 'vithial'),
]
notes['Releases and New Bands 2026'] = nav + f'''# Black Metal — Releases and New Bands 2026

**Checked through {DATE}; discovery shortlist, not a year-end ranking.** Release metadata and artist classifications were checked; these notes do not claim the assistant or you heard the albums. Artist tags and promotional statements are starting evidence rather than independent quality judgments. This small pool is not comprehensive.

## Released full-lengths

| Artist | Album | Release date | Category / status | Source and listening |
| --- | --- | --- | --- | --- |
''' + '\n'.join(f'| {a} | {b} | {d} | {desc} | {cite(s)} |' for a,b,d,desc,s in released) + f'''

## Emerging project leads

Here **emerging** means debut/early-discography, not a verified claim of growing popularity. Hieron, Nine Spears, and Vithial qualify as debut-album leads according to their own pages. Only Nine Spears’ formation year was established. Debut projects can include experienced musicians; biographies and reviews need further research. Mayhem and Winterfylleth belong in the established list.

To explore variety, try Hieron, Nine Spears, and Vithial before choosing favorites. This is an editorial discovery suggestion based on scope and metadata, not a best-new-bands verdict. Add independent appraisal and your reactions next.

## EPs and early-discography leads

**Bruul — Bruul - EP**, released **31 August 2026**: debut EP, English black/doom tags. A September 2025 demo is also listed; formation year remains unknown. Keep the EP outside full-length rankings. {cite('bruul')}.

## Established acts and album-boundary checks

- **Darkthrone — Pre-Historic Metal**, **8 May 2026**: released full album. Peaceville describes a mixture of thrash, black, heavy, and doom metal. Include it in a broad discovery list; decide album eligibility explicitly for a core Black Metal ranking. {cite('dark26')}; {cite('darkthrone')}.
- **Gaerea — Loss**, **20 March 2026**: released full album. Apple Music’s generic Metal label verifies identity/date but does not settle its precise style. Keep album-level classification and review research pending before assigning a core ranking. {cite('gaerea')}.

## Announced / upcoming

**Wolves in the Throne Room — Estuary**, announced for **23 October 2026**. The North America edition page still offers a preorder and two advance tracks as of the cutoff. Recheck on release; do not rank the unavailable full album yet. {cite('estuary')}.

## Update procedure

On the next refresh, use the actual date/year. Reopen responsible sources; record postponements and original-versus-reissue identity. Add distinct sections for full-lengths, EPs/demos/splits, and reissues. Review current-year rankings only as best so far, with a named candidate pool and corroborated criticism. No release alert or ongoing monitoring has been configured.
'''

notes['Research and Sources 2026-10-08'] = nav + '''# Black Metal — Research and Sources 2026-10-08

## Session recap

Created a separate Black Metal starter project: seven notes, 12 classic entry points, a working style map, a five-candidate 1994 comparison, an annual research archive, a blank personal journal, and a 2026 release/discovery snapshot. Prompts and instructions live in Music Prompts and are linked from its shared index. The upload pack contains five source snapshots plus instructions and 15 prompts. No ChatGPT app project was created, uploads performed, playlists saved, or audio played.

## Source register

All pages below were opened and checked **2026-10-08**. The rows state what was actually consulted and its limits. Facts use the responsible catalog where available; reputation uses attributed criticism. No full books were consulted.

| Source | Use / limitations |
| --- | --- |
''' + '\n'.join(f'| [{title}]({url}) | {limit} |' for title,url,limit in sources.values()) + '''

## Limits and unresolved work

- The history is an outline; detailed chapters and corroborated contested-event accounts remain to be researched.
- The style map is provisional. Build album-specific examples and cross-check boundaries instead of claiming all subgenres are complete.
- The classic selection is an editorial sample, heavily weighted toward the 1990s. Add later decades and geographically broader candidates.
- Annual rankings are pending apart from a limited 1994 comparison; 2026 is a shortlist, not a best-of list.
- Formation dates for several debut projects are unverified. Artist publicity alone does not establish quality or rising popularity.
- Political affiliations require specific reliable evidence; neither pagan imagery nor nationality proves an affiliation. Ideology is distinct from sonic classification.
- Spotify links in the classics note are labeled searches, not verified album objects. Streaming availability and preferred editions need checking.
- Listening history remains empty; uploads are static snapshots, not vault synchronization.

## Next session

Choose one: develop the 1980s/early-1990s history with more responsible sources; research a broader 1994 or 1995 album pool; explore a regional scene including Chile; or collect feedback on three contrasting albums. Refresh the upload sources after substantive local changes.
'''

instructions = '''You are my Black Metal research and listening partner. Help me explore its history, styles, classics, overlooked recordings, annual album rankings, current releases, and emerging bands. Develop my taste from my feedback without inventing preferences or assuming expertise.

Read 01_Project_Context_and_Method.txt first, then other uploaded sources as needed. Initial research was checked 8 October 2026. My latest explicit decisions override snapshots. Keep this project’s listening history and preferences separate from Death Metal, other music projects, and travel. Obsidian and ChatGPT uploads do not automatically synchronize; prepare named Markdown updates or refreshed files when asked, and never claim a save or upload without evidence.

Teach in plain language: riffs, tremolo picking, blast beats, vocal approaches, repetition, harmony, keyboards, production, atmosphere, and composition. Distinguish style, era, regional scene, hybrid, production descriptor, lyrical theme, and ideology. Cover traditional/second-wave, raw, melodic, symphonic, atmospheric, ambient, folk/pagan-related, black/doom and depressive approaches, black/death and war/bestial, black/thrash, black ’n’ roll, industrial, avant-garde/dissonant, post-black/blackgaze, and other supported labels. Discuss Viking metal, dungeon synth, death metal, doom, and shoegaze as neighboring or overlapping traditions. Classification can change between albums. Do not claim a final universally complete taxonomy or use platform tags as definitive evidence.

Develop sourced chronological chapters from precursors and the first wave through the Norwegian second wave and international parallel scenes, then later decades. Include tape trading, labels, recording, artwork, distribution, and cultural context. Cover Norway, Sweden, Finland, Greece, Czech/Central and Eastern European scenes, UK, US/Canada, Latin America including Chile, Asia, and other documented scenes without inventing regional uniformity. Compare disputed origins rather than declaring an uncontested inventor. Do not equate the whole genre with Norway or reduce its musical history to crimes. Address documented violence, ideology, and controversies where relevant, distinguishing verified events, individual statements, allegations, and scene mythology. NSBM and RABM are ideological descriptions, not automatic sonic categories. Never infer an artist’s politics from symbols, nationality, pagan themes, or association alone. If I request ideological filters, clarify the criterion and use specific reliable evidence.

For metadata prefer artist/label pages, liner notes, and responsible discography sources. For interpretation and reputation use attributed specialist reviews, interviews, and historical research. Open sources before relying on them; place direct links near claims and date current checks. Cross-check conflicts in original years, editions, formation/debut details, and contested historical claims. Distinguish promotional copy from independent criticism and polls from objective quality. Do not imply an entire book was read from its publisher page. Never invent quotations, credits, tracks, dates, metrics, listening, or consensus.

For this year use the actual current calendar year and a stated cutoff; initially 2026. Verify full release status from responsible pages. Separate released albums, upcoming announcements, EPs/demos/splits, singles, live releases, compilations, and reissues/remasters. A preorder with preview tracks is not a released full album. Do not rank an unavailable album as if it had been heard. Current-year orders are best so far, not final year-end lists. Historical rankings use original studio release years, not digital reissue dates.

Keep three ranking types separate: your reasoned editorial order, named published critic/community lists, and my personal favorites. State year, scope, eligibility, candidate pool, criteria, and gaps. Default eligibility is original studio full-lengths first publicly released in the chosen year, with hybrid boundaries labeled; offer a core-only alternative when appropriate. Research annual pools from 1982 onward without padding sparse early years or presenting an unresearched archive as finished. A discussion rubric is songwriting/riffs 35%, atmosphere/identity/coherence 25%, performance 20%, production serving the music 20%. Historical importance is separate. Raw production, speed, sales, and technical complexity do not automatically mean quality. Prefer explained provisional placements to invented numerical precision. Do not average incompatible rating scales or claim consensus from one list. Explain overlooked alternatives and how broader research might change the order.

Define new bands each time: newly formed, debut/early-discography, gaining attention, or simply new to me. Default to debut/early-discography with verified evidence. A new album by an established act does not make it a new band. New projects may involve experienced musicians; label that when known. Keep independent release discovery and established acts separate. Include geographic and stylistic variety without inventing popularity thresholds, formation dates, or critical acclaim.

Recommend manageable batches of three to five albums, with exact artist/title, original year, why to explore them, listening cues, sources, and links. Distinguish historical significance from enjoyment. Use artist Bandcamp, official artist/label video, or verified streaming album links; label title searches honestly. Confirm exact editions and region availability where relevant. Never claim you listened without supported audio access; use cited analysis and my supplied reactions. Summarize lyrics/themes rather than reproducing full lyrics. Do not purchase, publish, save playlists, alter my library, or configure alerts unless asked and the action succeeds.

Keep my journal empty until I report listening. Preserve my words, date if supplied, exact recording/edition, full listen versus sample, favorite moments, reaction to vocals/riffs/melody/atmosphere/production, and optional score. Leave missing fields blank. Ask one useful preference question at a time. Suggest two close matches and one contrasting experiment; avoid gatekeeping and allow my favorites to differ from established classics.

Respond in the language I use. Lead with a useful recommendation, explain it clearly, and use compact tables when comparing. After substantial work, state what was verified, what is editorial interpretation or a gap, and the next useful listening/research step. Build deeper chapters gradually and do not represent a starter survey as the whole history.
'''
assert len(instructions) < 8000
notes['ChatGPT Project Instructions'] = nav + '# Black Metal — ChatGPT Project Instructions\n\nPaste the complete block into project instructions.\n\n```text\n' + instructions + '```\n'
prompts = [
 ('Start the project', 'Read the uploaded sources and summarize the project’s scope and gaps. Offer chronological and sound-based listening paths, then three contrasting albums. Ask what I already enjoy; do not assume listens or scores.'),
 ('Whole history, in chapters', 'Build a sourced chapter plan from precursors/first wave through Norwegian second wave, international parallel scenes, and the 2000s–present. Explain musical changes, labels, production, distribution, and cultural context. Start with the first chapter, not a claim that a short overview is the whole history. Compare disputed accounts.'),
 ('Styles and listening cues', 'Map the major Black Metal styles and hybrids with practical sonic cues, two verified representative albums per style, and boundary discussions. Separate scene, theme, raw production, and ideological labels from sonic branches. Explain neighboring Viking metal, dungeon synth, war metal, and blackgaze.'),
 ('Classic albums', 'Recommend five classic or overlooked albums for [era/style]. Verify original years and editions, explain historical importance separately from musical appeal, and give direct sources plus official listening links or clearly labeled searches. Include contrasts rather than only famous Norwegian records.'),
 ('First versus second wave', 'Compare first-wave recordings with the early-1990s second wave. Explain changes in riffs, vocals, drums, composition, production, and distribution through three album pairs with sourced original years. Distinguish influence claims from disputed origin stories.'),
 ('Regional scene', 'Research [country/region, for example Chile, Greece, Finland, Czechia, or Japan]. Explain documented local history, key recordings, distinctive approaches where supported, and contemporary discoveries. Do not assume every local band shares one sound or ideology.'),
 ('Rank one year', 'Build a reasoned top [five/ten] Black Metal album list for [year]. Verify original studio-full-length eligibility and state the candidate pool, hybrid policy, criteria, sources, and gaps. Separate editorial order, published rankings, and my favorites. Do not pad thin pools, invent scores, or rank reissues as new originals.'),
 ('Develop the annual archive', 'Work through [year range] one year at a time. Build verified candidate pools before ordering albums; compare published lists by named author/audience. Track research status and missing scenes. Provide concise Markdown for the annual archive and explain why each provisional placement could change.'),
 ('Current-year releases', 'Search the actual current calendar year through today and state the cutoff. Verify responsible artist/label dates and released-full-album status. Separate full-lengths, upcoming records, EPs/demos/splits, and reissues. Include independent releases and varied scenes. Recommend three discovery priorities without ranking an unavailable album.'),
 ('Emerging bands', 'Find debut/early-discography Black Metal projects in [year/region/style]. Verify debut and formation information where possible. Distinguish new projects with experienced members from established acts. Give entry recordings, evidence, and independent appraisal where available; label unknown details and promotional claims.'),
 ('Compare two albums', 'Compare [album A] and [album B] on songwriting, atmosphere/identity, performance, production, and context. Verify original dates and editions. Use cited analysis and my feedback without claiming direct listening. Explain which offers the more useful next contrast for me.'),
 ('Add my listening feedback', 'I listened to [artist/album/edition]; [full album/sample]; my reaction was [feedback]; optional date/score [details]. Preserve my words in the journal, leave missing fields blank, and recommend two close matches plus one contrasting experiment. Ask one useful follow-up question.'),
 ('Listening sequence', 'Plan a [length]-track or [number]-album exploration sequence for [style/mood/era]. Verify artist/title/album matches and links; explain the progression. Clearly label search links. Provide a plan without claiming playback or a saved playlist.'),
 ('Death Metal versus Black Metal', 'Explain musical differences and overlaps between Death Metal and Black Metal using verified contrasting albums and labeled hybrids. Discuss riffs, vocals, rhythm, production, and composition without reducing genres to lyrical stereotypes. Keep this project’s preferences separate from my Death Metal project.'),
 ('Continue and refresh sources', 'Summarize verified research, my explicit reactions/decisions, editorial recommendations, and unresolved gaps. Prepare named Markdown updates for the relevant Obsidian notes and identify upload snapshots that need replacing. Do not claim automatic synchronization, saves, or uploads.'),
]
notes['ChatGPT Project Prompts'] = nav + '# Black Metal — ChatGPT Project Prompts\n\nCopy one prompt into the Black Metal project and replace bracketed fields.\n\n## Research add-on\n\n```text\nBrowse as of today; open sources before relying on them. Verify identity, original year, edition, format, and release status. Cite direct sources near claims. Distinguish fact, classification, promotional copy, editorial recommendation, and my listening feedback. Do not invent listening, scores, consensus, or artist affiliations.\n```\n\n' + '\n'.join(f'## {i}. {title}\n\n```text\n{body}\n```\n' for i,(title,body) in enumerate(prompts,1))

manifest = []
for name, content in notes.items():
    rel = Path('Music Prompts') / (titles[name]+'.md') if name.startswith('ChatGPT') else Path(titles[name]+'.md')
    assert not (VAULT / rel).exists(), f'Existing note: {rel}'
    dest = STAGE / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding='utf-8')
    manifest.append({'relative':str(rel), 'expected':None})
indexrel = Path('Music Prompts/Music Prompt Library.md')
original = (VAULT/indexrel).read_bytes()
index = original.decode('utf-8')
assert '| Black Metal |' not in index
row = '| Black Metal | [[Black Metal — ChatGPT Project Prompts|15 project prompts]] | [[Black Metal — ChatGPT Project Instructions|Paste-ready instructions]] | [[Black Metal — Start Here]] |\n'
lines = index.splitlines(keepends=True)
position = next(i for i,x in enumerate(lines) if x.startswith('| Death Metal |')) + 1
lines.insert(position, row)
(STAGE/indexrel).write_text(''.join(lines),encoding='utf-8')
backup = BASE / 'backup' / indexrel
backup.parent.mkdir(parents=True,exist_ok=True)
backup.write_bytes(original)
manifest.append({'relative':str(indexrel),'expected':hashlib.sha256(original).hexdigest()})
(BASE/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))

exports = {name: f'{i:02d}_'+slug+'.txt' for i,(name,slug) in enumerate(zip(names[:5], ['Project_Context_and_Method','History_Subgenres_and_Classics','Rankings_and_Listening_Journal','Releases_and_New_Bands_2026','Research_and_Sources_2026-10-08']),1)}
def plain(content):
    def replace(match):
        target = match.group(1).split('|')[0]
        for key,value in titles.items():
            if target == value: return f'{target} [see {exports[key]}]' if key in exports else f'{target} [see project setup files]'
        return target + ' [vault navigation]'
    return re.sub(r'\[\[([^\]]+)\]\]',replace,content)
for name,filename in exports.items():
    (PACK/'Sources'/filename).write_text(plain(notes[name]),encoding='utf-8')
(PACK/'Project Instructions.txt').write_text(instructions,encoding='utf-8')
(PACK/'Project Prompts.txt').write_text(plain(notes['ChatGPT Project Prompts']),encoding='utf-8')
(PACK/'First Message.txt').write_text(prompts[0][1]+'\n',encoding='utf-8')
(PACK/'README.md').write_text('''# Black Metal ChatGPT Project

Snapshot checked 8 October 2026. Suggested project name: Black Metal — History, Classics & Discovery.

1. Create a separate project in ChatGPT.
2. Upload the five text files in Sources (unzip this pack first).
3. Paste Project Instructions.txt into project instructions.
4. Send First Message.txt, then use Project Prompts.txt for later exploration.

Sources are original summarized notes with direct citations, not copied articles or full books. The starter has 12 classic entry points, a provisional 1994 comparison, a pending annual archive, and a dated 2026 shortlist. It is not a finished history or comprehensive ranking. No personal listens have been invented.

These files do not create the app project, perform uploads, configure alerts, or synchronize with Obsidian. Replace uploaded snapshots after local changes; verify current release information again when requesting updates.
''',encoding='utf-8')
with zipfile.ZipFile(BASE/'Black Metal — ChatGPT Project Pack.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(PACK.rglob('*')):
        if path.is_file(): archive.write(path,Path(PACK.name)/path.relative_to(PACK))
print(f'Staged {len(notes)} new notes and shared index update; instructions {len(instructions)} characters; {len(prompts)} prompts; pack ready.')
