from pathlib import Path
from urllib.parse import quote
import json,hashlib,re,zipfile
base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
notes={}
def add(title,text):notes[title+'.md']=text.strip()+'\n'
H='https://www.musicradar.com/news/guitars/a-history-of-death-metal-249395'
L='https://loudwire.com/heavy-metal-101-history-of-death-metal/'
W='https://en.wikipedia.org/wiki/Death_metal'
K='https://www.kerrang.com/the-15-greatest-death-metal-albums-of-the-90s'
D='https://deathdoom.com/death-metal/'
B='https://www.bazillionpoints.com/books/preorder-choosing-death-the-improbable-history-of-death-metal-grindcore-by-albert-mudrian/'
S='https://www.bazillionpoints.com/books/swedish-death-metal-book-by-daniel-ekeroth/'
P='https://www.loudersound.com/features/possessed-the-band-that-invented-death-metal'
def search(artist,album):return 'https://open.spotify.com/search/'+quote(artist+' '+album,safe='')
add('Death Metal — Start Here','''
---
tags: [music, death-metal]
created: 2026-10-08
---
# Death Metal — Start Here

A music-learning and discovery project: understand the history, explore the styles, hear the classics, follow new releases, compare albums by year, and discover emerging bands. This project is separate from travel planning.

**Learn:** [[Death Metal — History Subgenres and Classics]] · **Rank and record:** [[Death Metal — Rankings and Listening Journal]] · **New music:** [[Death Metal — Releases and New Bands 2026]] · **Evidence:** [[Death Metal — Research and Sources 2026-10-08]]

**ChatGPT:** [[Death Metal — ChatGPT Project Instructions]] · [[Death Metal — ChatGPT Project Prompts]]

## Start listening

Begin with Death’s *Human*, then Obituary’s *Cause of Death*, Entombed’s *Left Hand Path*, and Carcass’s *Heartwork*. This is a suggested learning order, not your personal ranking. Use the classics note for verified years and listening searches. Try one whole album, then record what catches your ear: riffs, atmosphere, vocals, rhythm, melody, and production. Your taste and prior listening are not yet recorded.

Alternate history with new music: after a classic, try one of the verified 2026 releases. Learning order and difficulty are editorial judgments; you can start anywhere.

## What the project contains

- A historical overview and a map of major styles, hybrids, and disputed tags.
- Twelve classic album starting points and a suggested four-stage listening path.
- A transparent ranking method, a first 1991 editorial ranking, and an annual research archive covering 1985–2026.
- Five released 2026 full-length candidates and one announced October debut, with primary-source links.
- A debut-band discovery shortlist, an empty personal listening journal, project instructions, and reusable prompts.

The annual archive is a research programme, not a completed ranking of every year. The 2026 list is a checked starter selection, not a comprehensive release census or final year-end verdict. No listening sessions, ratings, playlist creation, Spotify saves, or automatic monitoring have been performed.

## Next decisions

1. Tell the project which bands/albums you already know and what you like about them.
2. Choose chronological exploration or a tour of contrasting styles.
3. Build one researched annual top five at a time, starting with 1991 or a year you choose.

“This year” currently means **2026**, with research checked **8 October 2026**. In later chats, use the actual current year unless you request a specific one. The uploaded ChatGPT pack and this vault are separate snapshots; synchronize decisions through explicit updates.
''')
history=f'''# Death Metal — History, Subgenres, and Classics

[[Death Metal — Start Here|Dashboard]] · [[Death Metal — Rankings and Listening Journal|Rankings]]

**Research checked: 8 October 2026.** This is a starter synthesis and learning map; detailed scene histories remain topics for the project. Genre boundaries are debated and bands can change style between albums.

## Historical overview

Death metal developed from the increasingly extreme thrash and early extreme-metal underground of the 1980s. Possessed and Death are central to the origin story. Possessed’s *Seven Churches* (1985) precedes Death’s *Scream Bloody Gore* (1987), but “first death metal album” depends partly on how a listener draws the death/thrash boundary. An interview that credits one founder is evidence of that perspective, not a settled universal verdict. [Possessed interview]({P}) · [Historical overview]({H}).

The late 1980s and early 1990s brought a dense network of bands, labels, recording studios, demos, and tape trading. Florida became an important centre around Death, Morbid Angel, Obituary, and Deicide; New York and Sweden also developed distinctive approaches. Grindcore grew alongside death metal and exchanged ideas with it. [MusicRadar history]({H}) · [Loudwire history]({L}).

During the 1990s, the genre branched into melody, technical and progressive composition, brutality, and slower hybrids. Carcass’s *Heartwork* illustrates the melodic turn; Suffocation and the jazz/progressive explorations of Atheist and Cynic point in different directions. These developments overlap rather than forming a single line of progress. [MusicRadar history]({H}).

The longer story includes regional scenes beyond the US and Sweden. South American history deserves its own chapter, including Brazil and Chile; the latter’s research leads include Pentagram, Atomic Aggressor, and Sadism. UK, Finnish, Dutch, Polish, Canadian, and Asian scenes should be investigated on their own evidence rather than folded into one US-centred narrative. [Loudwire regional overview]({L}).

For the 2000s–2020s, investigate the growth of technical styles, changing production, internet discovery, old-school revival, progressive/psychedelic approaches, and genre crossings. Treat these as research chapters to develop; this overview does not establish a complete recent history. The current-release note supplies a verified foothold in 2026.

## A practical style map

These are listening cues, not strict tests. “All subgenres” has no universally fixed list: styles, regional sounds, hybrids, and descriptive tags overlap. This map makes room to add less common terms with evidence.

| Style or label | Listening cue | Representative starting names |
| --- | --- | --- |
| Traditional / old-school death metal | Riff-led extremity | Death, Obituary |
| Swedish chainsaw sound | Abrasive guitar texture; regional sound | Entombed, Dismember |
| Melodic death metal | Prominent melody | Carcass, At the Gates |
| Technical death metal | Instrumental complexity | Necrophagist, Nile |
| Progressive death metal | Expanding arrangements | Atheist, Cynic, Opeth |
| Brutal death metal | Dense, forceful attack | Suffocation, Cryptopsy |
| Slam | Groove-centred brutal branch | Devourment |
| Death-doom | Death/doom fusion | Asphyx |
| Blackened death metal | Black/death fusion | Behemoth |
| Death-thrash | Thrash/death intersection | Pestilence, Possessed |
| Deathgrind | Death/grind intersection | Misery Index, Exhumed |
| Death ’n’ roll | Rock groove | Entombed’s later work |
| Symphonic death metal | Orchestral integration | Septicflesh, Fleshgod Apocalypse |
| Dissonant / avant-garde | Unconventional harmony and form | Gorguts |
| Psychedelic / atmospheric | Texture and atmosphere tags | Blood Incantation |
| Industrial death metal | Mechanical/electronic elements | Investigate album by album |

Classification references: [broad taxonomy]({W}), [musician’s guide]({D}), [historical styles]({H}). The table is an editorial learning map. Modern tags such as “cavernous” and “cosmic” are useful descriptions without necessarily constituting independent lineages.

**Adjacent families:** grindcore and goregrind have their own histories; deathcore crosses into metalcore; funeral doom and war metal also warrant separate boundary discussions. Include them in comparisons with labels rather than treating every extreme-metal record as core death metal. [Taxonomy]({W}) · [Musician’s guide]({D}).

## Twelve classics to start with

Years below refer to original albums, not current reissues. Spotify links are title searches, not verified album IDs; confirm the artist, edition, and original programme. No platform playback has been tested.

| Album | Original year | Learning focus | Listening search / evidence |
| --- | --- | --- | --- |
'''
classics=[('Possessed','Seven Churches',1985,'Origins and boundaries',P),('Death','Scream Bloody Gore',1987,'Early language',H),('Morbid Angel','Altars of Madness',1989,'Classic intensity',H),('Obituary','Cause of Death',1990,'Groove and atmosphere',K),('Entombed','Left Hand Path',1990,'Swedish sound',K),('Death','Human',1991,'Technical/progressive bridge','https://death.bandcamp.com/album/human-deluxe-reissue'),('Suffocation','Effigy of the Forgotten',1991,'Brutal/technical foundation',K),('Atheist','Unquestionable Presence',1991,'Progressive exploration','https://www.alternativenation.net/top-10-death-metal-albums-1991/'),('Carcass','Heartwork',1993,'Melodic bridge',H),('At the Gates','Slaughter of the Soul',1995,'Melodic branch',D),('Cryptopsy','None So Vile',1996,'Brutal branch',K),('Gorguts','Obscura',1998,'Experimental branch',K)]
for a,b,y,f,s in classics:history+=f'| {a} — *{b}* | {y} | {f} | [Spotify search]({search(a,b)}) · [Evidence]({s}) |\n'
history+=f'''
## A suggested listening path

1. **Find the hooks:** *Human*, *Cause of Death*, *Left Hand Path*, *Heartwork*.
2. **Hear the origins:** *Seven Churches*, *Scream Bloody Gore*, *Altars of Madness*.
3. **Compare branching styles:** *Unquestionable Presence*, *Slaughter of the Soul*, *Effigy of the Forgotten*.
4. **Try the extremes:** *None So Vile* and *Obscura*, then follow the sound you enjoy.

This order is a recommendation, not a difficulty measurement or a claim that everyone will prefer these records. Use whole original albums before judging; bonus tracks and remixes can change the impression.

## Longer-history sources

Albert Mudrian’s *Choosing Death: The Improbable History of Death Metal & Grindcore* and Daniel Ekeroth’s *Swedish Death Metal* are useful deeper-history leads. The publisher pages were checked; the books were not read in this session, so their full contents are not treated as consulted evidence. [Choosing Death publisher]({B}) · [Swedish Death Metal publisher]({S}).
'''
add('Death Metal — History Subgenres and Classics',history)
ranking=f'''# Death Metal — Rankings and Listening Journal

[[Death Metal — Start Here|Dashboard]] · [[Death Metal — Releases and New Bands 2026|Current releases]]

## What “best” means here

Keep three separate lists: **editorial recommendations**, **published critic/community rankings**, and **your personal favorites**. None is an objective final verdict. Personal scores stay blank until you supply listening feedback. Popularity, technical difficulty, heaviness, and historical influence are different qualities.

Default annual eligibility: original studio full-lengths first released in the selected calendar year. Put EPs, demos, splits, live albums, reissues/remasters, and compilations in separate lists. Use earliest documented public release of the original album; record conflicting digital/physical dates. Allow major branches and clearly labeled hybrids, with a separate core-only view when needed. A band’s name or reputation alone does not prove an album’s style.

Default editorial rubric: songwriting/riffs **35%**, identity/coherence **25%**, performance **20%**, production serving the music **20%**. Historical importance gets a separate note, not an automatic scoring bonus. Do not fabricate numeric component scores without adequate evidence; a reasoned provisional order is better. For published scores, record source, rating scale, sample size where available, and check date; do not average incompatible scales as though identical.

## First annual ranking — 1991

**Provisional editorial top five from a limited classic-album shortlist**, not a measured score or a consensus poll. Your feedback can produce a different personal list. The order prioritizes distinctiveness and learning value; no claim of listening in this session is made.

| Rank | Album | Why this initial placement |
| --- | --- | --- |
| 1 | Death — *Human* | Strong starting point for the technical/progressive turn |
| 2 | Suffocation — *Effigy of the Forgotten* | Useful contrast in brutality and rhythmic focus |
| 3 | Carcass — *Necroticism — Descanting the Insalubrious* | A distinct grind-to-death transition |
| 4 | Dismember — *Like an Ever Flowing Stream* | Brings the Swedish strand into the comparison |
| 5 | Autopsy — *Mental Funeral* | Adds a slower, doom-inflected contrast |

The five albums/years appear in [Kerrang’s 1990s selection]({K}); *Human*’s original 1991 year is also distinguished from its 2011 reissue on [Death’s label Bandcamp]({'https://death.bandcamp.com/album/human-deluxe-reissue'}). This order is our editorial shortlist, not Kerrang’s order. Before calling it a full-year survey, compare Atheist, Morbid Angel, Immolation, Pestilence, and other documented 1991 releases.

## Annual archive — 1985–2026

Build a top five or ten with evidence for each year, plus overlooked albums and a separate personal winner. Early years may not justify ten eligible entries; never pad a list. A current-year list is “best so far” with a cutoff date. Announced records are ineligible until the full release is confirmed.

| Years | Current status | Useful task |
| --- | --- | --- |
| 1985–1989 | Research pending | Origins and death/thrash boundary, original-release verification |
| 1990 | Research pending | Compare US/Swedish classics and deeper candidates |
| 1991 | Limited starter top five above | Broaden pool, add independent reviews, then listen |
| 1992–1999 | Research pending | Investigate each year, expanding branches |
| 2000–2009 | Research pending | Compare established bands and emerging styles |
| 2010–2019 | Research pending | Review revival, technical, and experimental scenes |
| 2020–2025 | Research pending | Wider contemporary survey and retrospective evidence |
| 2026 | Verified release starter list; no full-year ranking yet | Refresh released pool, then rank best so far |

## Personal listening journal

No listens or personal scores recorded yet. Use this row format after listening:

| Date listened | Artist / album | Original year / edition | Full listen or sample | Favorite moments/tracks | What worked / did not | Personal score /10 | Revisit? |
| --- | --- | --- | --- | --- | --- | --- | --- |

For each session, record your response to riffs, vocals, groove, melody, atmosphere, and production in plain words. An optional score should reflect enjoyment rather than pressure to agree with the canon. Leave unspecified cells blank. Do not let a disliked vocal texture erase interest in a whole branch after one album.

## Annual ranking entry template

```text
Year / cutoff date:
Scope and format eligibility:
Candidate pool and known gaps:
Rank / artist / album / original release date / style:
Reason for placement:
Primary metadata source:
Independent review or retrospective source:
Listening link and edition:
Personal listening status and score (only if supplied):
Excluded releases and why:
Disagreements and overlooked candidates:
```
'''
add('Death Metal — Rankings and Listening Journal',ranking)
released=[('Exhumed','Red Asphalt','2026-02-20','Deathgrind / gore-metal branch','https://exhumed.bandcamp.com/album/red-asphalt','Established band; new album does not mean new band.'),('Harrowed','The Eternal Hunger','2026-02-27','Swedish death metal / punk edge','https://harroweddeathmetal.bandcamp.com/album/the-eternal-hunger','Artist page identifies a debut album; formation year not established here.'),('Temple of Void','The Crawl','2026-03-06','Death metal with death-doom roots','https://templeofvoid.bandcamp.com/album/the-crawl','Band describes broadening beyond its earlier death-doom identity.'),('Immolation','Descent','2026-04-10','Death metal','https://immolation.bandcamp.com/album/descent','Established-band entry; do not classify as emerging.'),('Inscribed','Upon the Twisted Throne','2026-06-19','Progressive / technical death-thrash','https://inscribedofficial.bandcamp.com/album/upon-the-twisted-throne','Artist page identifies debut full-length and formation in 2021.')]
releases='''# Death Metal — Releases and New Bands 2026

[[Death Metal — Start Here|Dashboard]] · [[Death Metal — Rankings and Listening Journal|Ranking method]] · [[Death Metal — Research and Sources 2026-10-08|Sources]]

**Checked 8 October 2026.** Primary artist/label Bandcamp pages supply the following titles and dates. This is a starter selection with a limited search footprint, not an exhaustive list or proof these are the year's best. No albums were played or rated in this session. Style labels are working descriptions based on artist/label context.

## Released full-length candidates

Sorted by release date, not quality. Click the title for the artist/label page and available listening options; playback itself was not tested.

| Artist / album | Release date | Working style | Why it belongs / limits |
| --- | --- | --- | --- |
'''
for a,b,date,style,url,why in released:releases+=f'| [{a} — *{b}*]({url}) | {date} | {style} | {why} |\n'
releases+='''
## Announced — not yet released at this cutoff

**[Casket Dweller — *River of Slumber*](https://nuclearwinterrecords.bandcamp.com/album/river-of-slumber): 22 October 2026.** The label identifies a Greek band formed in 2022 and its debut full-length, with traditional death-metal influences. As of this check, the page offers a preorder and one advance track. Keep it on the watchlist, not in a ranked released-album list. Recheck the actual full release and any date change after the announced date.

## New bands to investigate

These are discovery priorities, not a quality ranking or prediction of success. A debut album does not establish that the musicians or band formed this year.

1. **Inscribed:** formation year 2021 and a released 2026 debut are documented. A useful first comparison if you enjoy technical/progressive death-thrash.
2. **Harrowed:** a documented 2026 album debut and Swedish/punk tags make this a contrasting lead. Do not infer formation date from the album date.
3. **Casket Dweller:** formed in 2022; debut announced for later in October. Judge only the available preview for now and hold full-album judgment.

Sources are the linked artist/label pages above. Promotional claims are not independent review consensus. Exhumed, Temple of Void, and Immolation belong to the established-band release pool, not this debut shortlist.

## Refresh method

When running a new-release search, check the actual current date and year. Confirm original release date and format from artist/label pages, then seek independent reviews. Cover independent labels, regional scenes, Bandcamp debuts, and varied branches, rather than assuming the biggest labels represent everything. Keep released, announced, delayed, EP/demo, and reissue entries distinct. Note what changed since the last check.

No automatic release alerts or scheduled monitoring have been configured. Use the current-release prompt to refresh this note when wanted. A 2026 remaster of an older album belongs in a reissue list rather than this year's original-studio-album competition.
'''
add('Death Metal — Releases and New Bands 2026',releases)
instructions='''You are my Death Metal research and listening partner. Help me understand the genre’s history and major branches, discover classics and overlooked albums, follow current releases, compare albums by year, and find emerging bands. Build my taste through listening feedback rather than assuming it.

Read 01_Project_Context_and_Method.txt first. Consult other uploaded sources as needed. My latest explicit decisions and listening feedback override older snapshots. The initial notes were checked 8 October 2026. Keep this music project separate from travel. Uploaded sources and the Obsidian vault do not automatically synchronize; provide clearly named Markdown updates or replacement files when asked. Never claim a file was saved without evidence.

Teach from beginner-friendly explanations toward deeper analysis. Explain riffs, growls, blast beats, groove, harmony, production, and composition in plain language. Distinguish genre, regional scene, era, hybrid, and descriptive tag. Cover traditional/old-school, melodic, technical, progressive, brutal, slam, death-doom, blackened, death-thrash, deathgrind, death ’n’ roll, symphonic, dissonant/avant-garde, atmospheric/psychedelic, industrial approaches, and less common labels when supported. Treat grindcore, goregrind, deathcore, funeral doom, and war metal as related families with explicit boundary discussions. Labels are contested and may change album by album; never claim a universally complete final taxonomy.

Develop history chronologically from precursors and 1980s demos/tape trading through regional scenes, 1990s branching, and the 2000s–present. Include Florida, New York, Sweden, UK, Finland, Netherlands, Poland, Canada, Latin America (including Chile), Asia, and other documented scenes. Compare accounts of disputed origin claims rather than declaring an uncontested inventor. Explain recording/production, labels, artwork, cultural context, and changes in distribution alongside the music. Do not reduce death metal to gore lyrics or technical speed.

For factual metadata prefer official artist/label pages, liner notes, and responsible discography sources. For critical reputation use attributed specialist reviews, interviews, and retrospective features. Metal Archives can help cross-check metadata; user databases and community polls measure their particular audiences, not objective quality. Open pages before relying on them. Cite direct links near facts and opinions, record dates checked, flag conflicts, and distinguish label promotion from independent appraisal. Never imply you read an entire book when only its publisher page was consulted. Never invent quotes, credits, tracks, release dates, awards, audience metrics, or personal listening.

For “this year,” use the actual current calendar year and state the cutoff date. Initially this is 2026. Verify that a full album is released, not merely announced or available as preview tracks. Separate released albums, upcoming/changed-date announcements, EPs/demos/splits, live records, and reissues/remasters. Use original release years for historical rankings and keep edition-specific dates separate. Never rank an unreleased full album based on its advance single as though the whole record were available. Current-year lists are “best so far,” not final year-end lists.

Maintain three separate ranking types: your reasoned editorial recommendation, named published critic/community lists, and my personal favorites. State scope, candidate pool, criteria, and evidence limitations. Default eligibility is original studio full-lengths first publicly released in the selected year, including labeled major branches/hybrids; offer a core-only comparison when relevant. Research years individually from 1985 to the present and do not pad thin early years. A default rubric is songwriting/riffs 35%, identity/coherence 25%, performance 20%, production serving the music 20%. Historical importance is a separate note. Avoid invented numeric precision; use justified provisional orders if component scoring lacks evidence. Do not average incompatible rating scales or claim consensus from one list. Explain disputed placements and overlooked candidates.

Define “new bands” each time: newly formed, debut/recently debuted, rising, or simply new to me. Default to debut/early-discography acts and verify formation/debut dates where available. Experienced musicians in a new project may qualify, but label them. Keep established contemporary bands in a separate discovery list. A new album does not make a band new. Include geographic and stylistic variety; do not use follower counts as a substitute for musical relevance or invent a popularity threshold.

Recommend manageable listening batches: usually three to five albums, with why they matter, what to notice, and the next contrast to try. Start with whole original albums when helpful and identify remixes/reissues/bonus tracks. Use official Bandcamp, artist/label YouTube, or verified streaming links; clearly label title searches as searches. Spotify tools may be used if available, but do not claim playback, saves, playlists, or alerts occurred without successful results. Do not modify my library, purchase music, or publish anything unless I ask. Never claim you listened to an album without actual supported audio access. Base analysis on cited evidence and my supplied reactions. Discuss lyrics and themes through concise summaries rather than reproducing full lyrics.

Keep my listening journal empty until I report listens. Record date, album/edition, full listen versus sample, favorite tracks/moments, response to vocals/riffs/groove/melody/atmosphere/production, and optional enjoyment score. Preserve my words and ask one useful preference question at a time. Recommend both close matches and one contrasting experiment. Be curious and candid, avoid gatekeeping, and allow my favorites to differ from established classics.

Respond in the language I use. Lead with a useful recommendation, then explain it. Use compact tables for comparisons and rankings, with links. After substantial research, summarize what was verified, what remains a recommendation or gap, and the next useful listening or research step. Build the project gradually without representing a starter survey as the whole history or a completed annual archive.
'''
(base/'project-instructions.txt').write_text(instructions)
add('Death Metal — ChatGPT Project Instructions','# Death Metal — ChatGPT Project Instructions\n\n[[Death Metal — Start Here|Dashboard]] · [[Death Metal — ChatGPT Project Prompts|Prompts]]\n\nPaste the complete block into the project instructions field.\n\n```text\n'+instructions+'```')
prompts=[('Start the project','Read the uploaded project sources. Summarize the learning map, classic starting points, ranking method, current-year release status, and research gaps. Ask which three bands or albums I already like; if I do not know any, suggest three contrasting entry albums. Do not invent my listening history.'),('Tell the whole history in chapters','Create a chronological Death Metal history from precursors through the current year. Cover demos and tape trading, regional scenes, production, labels, major branching styles, and modern distribution. Separate disputed claims from documented events. Include Latin America and Chile. Begin with a chapter outline, then write a connected sourced overview; offer deeper chapters without pretending an outline is exhaustive.'),('Explore the subgenre map','Explain the main Death Metal branches, regional sounds, hybrids, and disputed descriptive tags. For each, give short listening cues, two representative original albums with verified years, and one comparison that helps me hear the difference. Include adjacent genres with clear labels. Cover the map broadly without inventing a fixed universal list of all subgenres.'),('Deep dive into one style','Teach me [style] through its development, characteristic sounds, major scenes, and five representative albums from different periods. Explain overlap and disputed boundaries. Give official listening links and an accessible order. Compare it with the nearest neighboring style.'),('Classic album listening course','Build a twelve-album learning course from the uploaded classics and any better-supported alternatives. Explain original year, role in the history, listening cues, and how each contrasts with the previous record. Recommend three albums for this week without assuming I have a fixed schedule or already heard them.'),('Best albums for a year','Research [year] and make a justified top ten Death Metal studio-album ranking, or fewer if the eligible pool is thin. State scope, candidate pool, metadata evidence, rubric, independent critical sources, borderline exclusions, and overlooked alternatives. Keep original years separate from reissues. Show editorial placement separately from published lists and my personal ratings; leave unreported personal ratings blank.'),('Build the annual archive','Continue the annual archive with [year range, preferably three years at a time]. Research each year individually, create a sourced top five with reasons and overlooked albums, and update coverage status. Do not copy one magazine list as consensus. Keep thin years shorter and identify remaining gaps. Finish with an Obsidian-ready update for the rankings note.'),('Current-year releases','Search Death Metal releases from the actual current calendar year through today. State year and cutoff date. Verify original album date and released status from artist/label sources. Include varied branches, scenes, and independent labels. Give ten released full-length candidates with listening links; keep future albums, EPs, demos, and reissues in separate sections. Flag changes since the uploaded snapshot.'),('Best albums so far','Build a current-year best-so-far editorial ranking from a reasonably broad verified released pool. State cutoff, scope, criteria, and limitations; support critical assessment with independent reviews. Keep upcoming albums out and distinguish recommendations from my listening scores. Explain five close placements and identify which three albums I should try next.'),('Discover emerging bands','Find ten debut or early-discography Death Metal bands worth investigating. Define new, verify formation/debut information where possible, distinguish new projects by experienced musicians, and cover different scenes/styles. Give an entry album or EP, format/date, sonic context, independent evidence where available, and official links. Keep established bands new to me in a separate section. Do not rank an unreleased debut as a heard full album.'),('Explore Chile and Latin America','Research the development of Death Metal in Chile and its connections to other Latin American scenes. Include early demos, regional distinctions, labels, classic albums, and emerging acts with verified metadata. Explain death/thrash and black/death boundaries where relevant. Avoid making Brazil stand in for the entire region. Provide an original-album listening path and dated sources.'),('Compare two albums','Compare [album A] and [album B] on riffs, composition, vocals, rhythm, atmosphere, production, and historical context. Verify exact editions and original years. Use cited criticism and my reactions; do not claim direct listening if audio access is unavailable. Explain which is the better next listen for me without calling the result objectively best.'),('Record my listening and recommend next steps','I listened to [artist / album / edition]. My reaction: [what I liked, disliked, favorite moments, full listen or sample, optional score]. Preserve this feedback in an Obsidian-ready journal entry. Ask one clarifying question if useful, recommend two close matches and one contrasting experiment, and explain the connection. Do not infer listens or scores for other albums.'),('Make a listening playlist plan','Create a track-list plan that introduces [style / period / scene] in a coherent order. Verify track titles, artist/album matches, and streaming links where possible. Label searches as searches and unavailable items honestly. Explain each selection without quoting full lyrics. Prepare the plan for review; do not save a playlist unless I explicitly ask for creation.'),('Update the vault and sources','Summarize the verified research and my explicit listening feedback from this chat. Produce concise Markdown updates naming the target Death Metal note and section. Preserve original years, edition details, citations, blank personal fields, and existing links. Separate facts, editorial rankings, published opinions, and my preferences. Explain which project source snapshot should be refreshed; do not claim automatic sync.')]
pt='# Death Metal — ChatGPT Project Prompts\n\n[[Death Metal — Start Here|Dashboard]] · [[Death Metal — ChatGPT Project Instructions|Instructions]]\n\nCopy one prompt into the music project and replace square-bracket placeholders. Start with **1**, then choose history, styles, or listening.\n\n## Research add-on\n\n```text\nCheck online as of today. Open relevant sources and cite them beside facts. Verify original release year, format, artist/album identity, and released versus announced status. Attribute criticism and rankings. State uncertainty and scope. Do not invent listening, scores, quotes, metadata, links, or a consensus. Use my latest feedback and keep project uploads distinct from live Obsidian notes.\n```\n'
for i,(t,p) in enumerate(prompts,1):pt+=f'\n## {i}. {t}\n\n```text\n{p}\n```\n'
add('Death Metal — ChatGPT Project Prompts',pt)
source_rows=[('MusicRadar — history',H,'30 Apr 2010','Origins, Florida, branching; historical feature, not current news.'),('Loudwire — history',L,'31 Aug 2017','Regional history and Latin America; old band-activity details not adopted.'),('Louder — Possessed interview',P,'23 Jul 2020','Origin claim and participant perspective; not a settled inventor verdict.'),('Wikipedia — Death metal',W,'Live page','Taxonomy orientation; editable and inconsistent, not definitive authority.'),('Musician Stefan Nordström — genre guide',D,'Not stated','Listening suggestions and branch descriptions; personal opinion, with historical inaccuracies flagged below.'),('Kerrang — 1990s selection',K,'20 Jul 2019','Classic-album candidates and years; one critic’s selection, with metadata errors flagged below.'),('Alternative Nation — 1991 list','https://www.alternativenation.net/top-10-death-metal-albums-1991/','2016; exact date not recorded','Atheist 1991 candidate and wider pool; editorial, not consensus.'),('Death / Relapse — Human reissue','https://death.bandcamp.com/album/human-deluxe-reissue','2011 edition','Distinguishes original 1991 album from 2011 reissue.'),('Bazillion Points — Choosing Death',B,'Publisher listing','Book scope; publisher page only, full book not read.'),('Bazillion Points — Swedish Death Metal',S,'Publisher listing','Regional-history book scope; publisher page only, full book not read.')]
for a,b,date,style,url,why in released:source_rows.append((a+' — '+b,url,date,'Artist/label credits establish date and title; promotional text is not independent appraisal.'))
source_rows.append(('Nuclear Winter — Casket Dweller','https://nuclearwinterrecords.bandcamp.com/album/river-of-slumber','Announced 22 Oct 2026','Formation 2022, debut, and preorder/preview status; future date may change.'))
src='# Death Metal — Research and Sources · 8 October 2026\n\n[[Death Metal — Start Here|Dashboard]]\n\nThe following pages were opened and read on **8 October 2026**. Date checking establishes the observed metadata, not musical quality or personal listening.\n\n| Source | Publication / release context | Supports / limitations |\n| --- | --- | --- |\n'
for name,url,date,support in source_rows:src+=f'| [{name}]({url}) | {date} | {support} |\n'
src+='''
## Conflicts and limits retained

- Kerrang’s page calls *Last One on Earth* an Asphyx debut and labels Cannibal Corpse’s *The Bleeding* 1993. These details were not adopted; verify against discographies before using either album in a yearly ranking.
- The musician’s guide places goregrind’s emergence in the late 1990s, which is inconsistent with Carcass’s earlier history. That timing claim was excluded.
- Wikipedia’s old-school definition is too narrow for this map; no rigid slow/simple rule or claimed late-1990s origin was adopted.
- The KaosMetal subgenre page and a guessed Suffocation Bandcamp album URL could not be retrieved. Search snippets were not used as read sources.
- Label promotion and Bandcamp supporter comments do not establish independent critical consensus. No Spotify playback, playlist, saved library, or individual audio analysis was performed.
- The 1991 ranking is a limited editorial seed. Other years and the full recent history still require further research. The 2026 list is selective; no comprehensive census or final best-of verdict is claimed.

## Session and continuation

Created a separate music project after the user requested Death Metal history, subgenres, classics, current-year releases, annual rankings, and new bands. Prepared seven Obsidian notes plus five ChatGPT upload sources, instructions, setup guide, starter prompt, and ZIP delivery pack in the workspace. User listening preferences and scores remain unspecified.

Next: establish prior listening, choose a learning path, expand one year’s candidate pool and ranking, and refresh releases by the actual date when requested. No ChatGPT music project was created by tools and no automatic monitoring was configured.
'''
add('Death Metal — Research and Sources 2026-10-08',src)
for name,content in notes.items():
    assert not (vault/name).exists(),'Existing note requires backup/reconciliation: '+name
    (base/'staged'/name).write_text(content)
(base/'manifest.json').write_text(json.dumps({n:None for n in notes},ensure_ascii=False,indent=2))
groups={'01_Project_Context_and_Method.txt':['Death Metal — Start Here.md','Death Metal — Rankings and Listening Journal.md'],'02_History_Subgenres_and_Classics.txt':['Death Metal — History Subgenres and Classics.md'],'03_Current_Releases_and_New_Bands.txt':['Death Metal — Releases and New Bands 2026.md'],'04_Research_and_Evidence.txt':['Death Metal — Research and Sources 2026-10-08.md'],'05_Reusable_Project_Prompts.txt':['Death Metal — ChatGPT Project Prompts.md']}
mapping={n.removesuffix('.md'):f for f,ns in groups.items() for n in ns}
mapping['Death Metal — ChatGPT Project Instructions']='project-instructions.txt (project instructions field)'
def refs(m):
    target,sep,label=m.group(1).partition('|')
    stem,_,anchor=target.partition('#')
    assert stem in mapping,stem
    return (label if sep else stem)+f' [source: {mapping[stem]}'+(f'; section: {anchor}' if anchor else '')+']'
for f,ns in groups.items():
    text='# Death Metal Project — '+f+'\n\nSnapshot: 8 October 2026. Later explicit decisions supersede this snapshot. These are authored research notes, not full copies of external publications.\n'
    for n in ns:text+='\n---\n\n'+re.sub(r'\[\[([^]]+)\]\]',refs,notes[n])
    (base/'sources'/f).write_text(text)
(base/'first-message.txt').write_text('Read the five uploaded music sources and project instructions. Help me begin exploring Death Metal. Ask what artists or albums I already like; if I am completely new, recommend three contrasting starting albums and explain what to notice. Then show how we can explore history, subgenres, annual rankings, current releases, and new bands without overwhelming the first listening session. Keep my listening scores blank until I report them.\n')
(base/'README.md').write_text('''# Death Metal — History, Listening & Discovery

Create a separate ChatGPT project with this name. Paste [project-instructions.txt](project-instructions.txt) into its instructions field. Extract the ZIP and upload the five individual `.txt` files in `sources/`. Start a project chat using [first-message.txt](first-message.txt).

The five sources cover project context/ranking method, history/subgenres/classics, 2026 releases/new bands, the checked evidence register, and reusable prompts. The instructions also live in Obsidian as **Death Metal — ChatGPT Project Instructions**; the main entry point is **Death Metal — Start Here**.

This is a starter project with a historical learning map, twelve classics, a limited 1991 ranking, a five-album released-2026 selection, one upcoming debut, and fifteen reusable prompts. It does not represent a completed every-year ranking or comprehensive history. Personal listening and scores are blank.

Sources are dated snapshots. Refresh the music notes and uploads explicitly after substantial research or listening decisions. A new ChatGPT project has not been created through these tools. No playlists, purchases, saves, reminders, or automatic release monitoring were performed.
''')
with zipfile.ZipFile(base/'Death-Metal-ChatGPT-Project-2026-10-08.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in [*(base/'sources').glob('*.txt'),base/'project-instructions.txt',base/'first-message.txt',base/'README.md']:z.write(p,str(p.relative_to(base)))
print('Prepared seven Obsidian notes, five ChatGPT sources, instructions, fifteen prompts, and ZIP.')
