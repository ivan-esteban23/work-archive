from pathlib import Path
import hashlib,json,re,zipfile
root=Path('/home/ivanaguilera/Work/goth-rock-project-20261008'); stage=root/'staged';stage.mkdir(exist_ok=True)
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault'); files={}
first='''Let’s start exploring Goth Rock together. Read the project instructions and uploaded sources so we can continue from the work already prepared.

Give me a clear overview of its history, classic albums, major sounds, regional scenes, and current discoveries. Keep gothic rock central while explaining its relationships with post-punk, deathrock, darkwave, coldwave, and ethereal wave. Distinguish researched facts, editorial recommendations, and gaps.

Recommend three contrasting albums to begin with, explain what to notice in each, and ask me one useful question about what I already enjoy. Do not assume I have listened to or rated any album.'''
files['Goth Rock — Start Here.md']='''# Goth Rock — Start Here

Research snapshot: **8 October 2026**. A separate music research and listening project, matching the structure of your metal projects.

## Scope

Explore **gothic rock / goth rock** from post-punk roots through classic scenes and contemporary artists. Include deathrock, darkwave, coldwave, and ethereal wave as related explorations, with their differences explained. Gothic metal and industrial/EBM are neighboring topics, not automatically eligible for a core gothic rock ranking. Musical classification is album-specific; dark imagery alone does not establish genre.

## Project notes

- [[Goth Rock — History Styles and Classics]]
- [[Goth Rock — Rankings and Listening Journal]]
- [[Goth Rock — Releases and New Bands 2026]]
- [[Goth Rock — Research and Sources 2026-10-08]]
- [[Goth Rock — ChatGPT Project Instructions]]
- [[Goth Rock — ChatGPT Project Prompts]]
- [[Music Prompt Library]]

## Three starting albums

Suggested exploration order: **Bauhaus — In the Flat Field (1980)** → **The Cure — Pornography (1982)** → **The Sisters of Mercy — First and Last and Always (1985)**. Compare tension and theatrical delivery, atmosphere and repetition, then melodic guitar interplay and machine-driven rhythm. These are editorial listening questions, not claims of direct listening. Original years and sources are in the classics note.

## ChatGPT setup

Suggested project name: **Goth Rock — History, Classics & Discovery**. Unzip the project pack and upload the five numbered text files as sources. Paste Project Instructions.txt into project instructions, then send First Message.txt. Reusable Prompts.txt contains 15 prompts. Uploads are snapshots; this does not create the app project or synchronize it with Obsidian.

## First message

```text
'''+first+'''
```

## Next step

Start with a three-album listening batch, a history chapter, a regional scene, or an annual ranking. Your listening journal and personal scores stay empty until you supply feedback. This is a researched starter project, not a completed history or exhaustive yearly archive.
'''
files['Goth Rock — History Styles and Classics.md']='''# Goth Rock — History Styles and Classics

Checked **8 October 2026**. This is a starter overview and chapter plan; detailed historical claims need further source work.

## Historical orientation

Gothic rock developed from late-1970s post-punk. Early and later artists do not all share one sound; relationships with deathrock and darkwave need album-level discussion. The [Wikipedia overview](https://en.wikipedia.org/wiki/Gothic_rock) supplies an initial secondary orientation and bibliography, not final authority for disputed origin claims.

## History to develop in chapters

| Chapter | Questions and research leads |
| --- | --- |
| Precursors and post-punk roots | Which musical ideas anticipate the genre? Investigate Joy Division, Siouxsie and the Banshees, and early Bauhaus without assigning their entire catalogs one label. |
| Early scenes and clubs | Research Batcave, positive punk, Specimen, Alien Sex Fiend, and UK Decay; distinguish a club, a press label, and a musical style. |
| 1980s development | Trace guitar-led approaches, rhythm machines, melodic expansion, labels, and international circulation; research Sisters of Mercy, the Mission, and Fields of the Nephilim. |
| Deathrock and regional paths | Investigate Christian Death and other US artists alongside distinct European developments. Avoid reducing deathrock to a British invention or equating it with metal. |
| Darkwave, coldwave, ethereal neighbors | Compare synth emphasis, minimal arrangements, and atmospheric approaches. Research labels and local terminology rather than imposing a universal taxonomy. |
| 1990s–2000s | Explore continuity, independent labels, clubs, festivals, and scenes beyond the best-known UK names. |
| Contemporary scenes | Follow current gothic rock and related revivals, including Latin America/Chile and documented Asian scenes. Explain local histories rather than treating a country as one sound. |

Names above are **research leads**, not a fully verified canon. Include women’s and LGBTQ+ contributions, visual art, literature, fashion, and community history without replacing musical analysis with aesthetics.

## Sound comparison framework

Use these as provisional listening cues, not strict rules: gothic rock often foregrounds guitar textures, melodic bass, driving rhythm, and dramatic vocals; deathrock often brings a punk-oriented attack; darkwave may foreground electronic arrangements; coldwave terminology varies by era and region; ethereal wave emphasizes atmosphere and vocal texture. Verify classifications for each recording. Industrial/EBM and gothic metal can share audiences or influences while requiring separate eligibility decisions.

## Verified starter album identities

| Album | Original year | Exploration question | Source and limitation |
| --- | --- | --- | --- |
| Bauhaus — In the Flat Field | 1980 | How do voice, guitar space, and rhythmic tension interact? | [Beggars Banquet catalog](https://beggarsbanquetrecords.com/bauhaus-in-the-flat-field/) confirms title/year; its date is 3 November. Other discographies differ on the exact day, so use the secure year here. |
| The Cure — Pornography | 1982 | How do repetition, drums, and atmosphere sustain an album? | [Official album page](https://www.thecure.com/release/pornography/) confirms title/year, tracks and credits. The page gives 4 May; the [official EU shop](https://shopeu.thecure.com/pages/pornography-1982-extras-remastered-2005) gives 3 May. Exact-day conflict remains; 2005 is the deluxe/remaster year. |
| The Sisters of Mercy — First and Last and Always | 1985 | How do guitar interplay and programmed rhythm support melody? | [Guitar World interview with Gary Marx and Wayne Hussey](https://www.guitarworld.com/artists/guitarists/the-making-of-the-sisters-of-mercy-first-and-last-and-always) supports recording context and 1985 release; participant recollections and critical description are distinct evidence types. |

These three are an editorial introduction, not an objective top three. The [Cure’s official biography](https://www.thecure.com/bio/) describes stylistic shifts: do not assume every Cure record has the same sound. No direct audio listening or personal rating is claimed.

## Next classics research

Verify contrasting Siouxsie and the Banshees, Christian Death, the Mission, and Fields of the Nephilim albums; then add related darkwave and ethereal examples. Establish exact titles, original years, editions, and responsible listening links before making a ranked canon.

[[Goth Rock — Start Here]]
'''
files['Goth Rock — Releases and New Bands 2026.md']='''# Goth Rock — Releases and New Bands 2026

Research cutoff: **8 October 2026**. Starter discovery shortlist, not an exhaustive release list or best-of ranking. Metadata and artist descriptions were checked on the linked artist pages; audio was not evaluated. Critical quality and narrower genre eligibility remain to be researched.

## Released albums

| Artist / album | Stated original release | Scope and next check | Evidence |
| --- | --- | --- | --- |
| Reflection Black — Burning Obsidian Star | 20 March 2026 | Athens project; artist describes gothic rock/post-punk with metal influences. Verify album-level fit before a core-only ranking. | [Artist album page](https://reflectionblack.bandcamp.com/album/burning-obsidian-star) calls it the second album and identifies a 2023 debut. |
| The Awakening — The Lost Theatre | 23 August 2026 | Gothic/darkwave artist originally from Johannesburg; established act, not a new band. Tags include gothic metal, so investigate the actual recording rather than treating tags as proof. | [Official album page](https://theawakeningofficial.bandcamp.com/album/the-lost-theatre) describes this as album thirteen and supplies credits. |
| Mica — Leave My Body Somewhere Dark | 7 May 2026 | Debut-album discovery in related post-punk/darkwave/alternative pop; keep adjacent unless a narrower gothic rock assessment supports inclusion. | [Artist album page](https://micaeternal.bandcamp.com/album/leave-my-body-somewhere-dark) explicitly calls it a debut; earlier EPs appear in the discography. |

## Announced / upcoming

**Black Doldrums — Repetition Compulsion:** artist text states **13 November 2026**, with a preorder and three advance tracks. It explains that an October date was a Bandcamp preorder workaround; the opened current page now also displays November in its release field. Use the explicit November date, recheck before release, and exclude from released-album rankings at this cutoff. It is described as the third studio album, so the act is not a debut discovery. [Artist preorder page](https://blackdoldrums.bandcamp.com/album/repetition-compulsion).

## Emerging discoveries

- **Mica:** eligible under a debut-album definition, with related styles labeled; formation date unverified.
- **Reflection Black:** eligible under an early-discography definition, based on the second-album claim and 2023 debut. “Rising” in the page is promotional wording, not independent proof of popularity.

These are research candidates, not a best-new-bands ranking. Seek independent appraisal and wider geographical coverage, including Chile/Latin America and Asian scenes. Keep EPs, singles, live releases, compilations, and reissues separate. Use the actual calendar year when continuing; current-year rankings are best so far with a stated cutoff.

[[Goth Rock — Start Here]]
'''
files['Goth Rock — Rankings and Listening Journal.md']='''# Goth Rock — Rankings and Listening Journal

## Ranking method

Maintain separate **editorial recommendations**, **attributed published lists**, and **personal favorites**. Default annual eligibility: original studio full-lengths first released in the chosen year, with gothic rock central. Label deathrock and other related styles separately; broaden the candidate pool only with an explicit scope. Reissues do not change the original year. Keep singles, EPs, live albums, and compilations separate.

Explain placements using songwriting, identity/coherence, performance, and production serving the music. Discuss historical impact separately. State candidate pool, sources, omissions, and genre uncertainty. Do not manufacture numeric precision or pad thin years. Annual history starts with late-1970s precursors and 1980s development; do not assume every year has enough eligible albums for a top ten.

## Annual archive

No annual rankings have been completed. First tasks: verify a candidate pool for 1980, 1982, or 1985; then develop subsequent years gradually. A 2026 list must be labeled best so far through its research date and exclude upcoming full albums.

| Year | Eligibility / candidate pool | Editorial list | Published lists | My favorites | Gaps |
| --- | --- | --- | --- | --- | --- |
| 2026 | Not yet fully researched | Pending | Pending | | Independent reviews, wider coverage, boundary decisions |

## Listening journal

No listening sessions or personal ratings recorded.

| Date supplied | Artist / album / edition | Full listen or sample | My exact feedback | Favorite moments | Optional score | Next discovery |
| --- | --- | --- | --- | --- | --- | --- |

Leave unknown fields blank. Preserve my words and distinguish my reaction from a reviewer's opinion. After feedback, suggest two close matches and one contrasting experiment.

[[Goth Rock — Start Here]]
'''
sources=[('Beggars Banquet','https://beggarsbanquetrecords.com/bauhaus-in-the-flat-field/','In the Flat Field title and 1980 year; label catalog, exact-day conflict with other discographies.'),('The Cure','https://www.thecure.com/release/pornography/','Pornography original year, tracks, credits; date differs by one day from official shop.'),('The Cure EU shop','https://shopeu.thecure.com/pages/pornography-1982-extras-remastered-2005','Opened official shop: 3 May 1982 versus album page 4 May; exact day unresolved.'),('The Cure biography','https://www.thecure.com/bio/','Artist-authored historical and stylistic context; not independent criticism.'),('Guitar World','https://www.guitarworld.com/artists/guitarists/the-making-of-the-sisters-of-mercy-first-and-last-and-always','11 May 2026 interview with Marx and Hussey: debut recording context and 1985 release; recollection and editorial framing distinguished.'),('Reflection Black','https://reflectionblack.bandcamp.com/album/burning-obsidian-star','Released 20 March 2026; second album, 2023 debut, self-described styles; promotional quality claims not adopted.'),('The Awakening','https://theawakeningofficial.bandcamp.com/album/the-lost-theatre','Released 23 August 2026; credits and thirteenth-album claim; tag boundaries need analysis.'),('Mica','https://micaeternal.bandcamp.com/album/leave-my-body-somewhere-dark','Released 7 May 2026; debut-album statement, adjacent styles, earlier EPs.'),('Black Doldrums','https://blackdoldrums.bandcamp.com/album/repetition-compulsion','Preorder, three preview tracks; explicit 13 November 2026 date supersedes October workaround; third album.'),('Wikipedia overview','https://en.wikipedia.org/wiki/Gothic_rock','Opened secondary genre overview and bibliography; editable and unsuitable as sole evidence for disputed origins.')]
files['Goth Rock — Research and Sources 2026-10-08.md']='# Goth Rock — Research and Sources 2026-10-08\n\nChecked **8 October 2026**. Opened sources unless explicitly marked as a search-only lead. No full books or recordings were consumed. This evidence base supports a starter project, not comprehensive history or ranked quality judgments.\n\n'+ '\n'.join(f'- **[{p}]({u})** — {c}' for p,u,c in sources)+'\n\n## Evidence gaps\n\nDetailed scene histories, albums beyond the starting three, independent 2026 reviews, international discovery, and annual candidate pools still require research. Release metadata does not establish musical quality; platform tags and promotional copy do not settle classification. Exact-day discrepancies are preserved rather than silently resolved.\n\n[[Goth Rock — Start Here]]\n'
instructions='''You are my Goth Rock research and listening partner. Help me explore gothic rock history, styles, classics, overlooked records, current releases, yearly rankings, and emerging artists. Develop my taste from explicit feedback without inventing listens, preferences, or scores.

Read 01_Project_Context_and_Method.txt first. Initial research was checked 8 October 2026; my latest decisions override older snapshots. Keep this project's journal and preferences separate from metal, other music, and travel. Uploaded sources and Obsidian do not automatically synchronize. Prepare named Markdown updates and replacement snapshots when asked; never claim saves or uploads without tool evidence.

Keep gothic rock central. Explain its post-punk roots and its relationships with deathrock, darkwave, coldwave, ethereal wave, and other hybrids. Distinguish genre, regional scene, press label, club culture, and descriptive tag. Batcave is also a club/scene reference, not a universal musical subgenre. Gothic metal, industrial/EBM, synthpop, and dark alternative pop need explicit boundary decisions. Do not equate goth with black clothing, horror themes, every melancholy song, or every band's entire catalog. Artists may reject a label or change style between albums; explain disagreements without gatekeeping.

Develop connected chronological chapters from relevant precursors and late-1970s post-punk through early scenes, 1980s expansion, subsequent decades, and contemporary developments. Investigate UK/European and US deathrock histories, Latin America including Chile, documented Asian scenes, and other regions. Include women and LGBTQ+ contributions, labels, clubs, festivals, recording, distribution, artwork, literature, and community context. Do not claim one uncontested inventor or a complete universal taxonomy. Regional research leads are not established historical claims.

Explain bass lines, guitar textures, rhythm machines versus live drums, vocal delivery, melody, repetition, arrangement, and production in accessible terms. Separate historical significance, critical reception, and my enjoyment. Prefer artist/label catalogs and credits for metadata; use attributed interviews, specialist criticism, and historical research for interpretation. Open sources before relying on them, cite near claims, date current checks, and label promotional language. Editable databases are useful leads, not official artist sources. Do not imply a book was read from its sales page. Compare material conflicts; preserve unresolved original-date or edition differences.

Use the actual current calendar year for new releases, initially 2026, and state the cutoff. Verify artist/title, original date, format, and full-release status. Separate released original studio albums, upcoming announcements, EPs/singles/demos/splits, live albums, compilations, and reissues/remasters. Previews do not establish that a full album is released. Check explicit artist corrections against platform fields. Current-year rankings are best so far, not final year-end lists.

Maintain three ranking types: your editorial recommendation, named published critic/community lists, and my personal favorites. Default eligibility is original studio full-lengths first released in the chosen year, gothic rock central; state whether deathrock or other adjacent styles are included. Show candidate pool, criteria, evidence, omissions, and disputed boundaries. Build annual rankings gradually from relevant origins onward; do not pad weak pools or present an empty archive as completed. Evaluate songwriting, identity/coherence, performance, and production; discuss historical impact separately. Do not invent precision, combine incompatible ratings, or equate fame with quality.

Define emerging for each search: newly formed, debut/early-discography, gaining attention, or new to me. Default to debut/early-discography with evidence. Earlier EPs do not disqualify a debut full-length, but mention them. Established acts with new albums are not new bands. Experienced-member projects may qualify if labeled. Formation dates and popularity remain unknown unless verified. Seek geographical variety without inventing scenes or acclaim.

Recommend three to five albums per batch, with exact names, original years, reasons, practical listening questions, and links. Distinguish verified direct listening pages from title searches. Use cited analysis and my feedback; never claim direct listening without actual supported audio access. Summarize themes without copying full lyrics. Do not claim playback, saved playlists, library changes, alerts, purchases, or publication unless requested and successfully performed.

Keep the journal empty until I report a listen. Preserve my wording, supplied date, exact edition, full listen versus sample, favorite moments, optional score, and reactions to voice, rhythm, texture, melody, and atmosphere; leave missing fields blank. Suggest two close matches and one contrasting experiment after feedback. Ask one useful preference question at a time.

Respond in the language I use. Give manageable listening paths and compact tables where helpful. Distinguish verified fact, editorial interpretation, and unresolved research. After substantial work suggest the next step and identify snapshots that need replacement. Do not call a starter outline the whole history or an exhaustive classics/new-release archive.'''
files['Music Prompts/Goth Rock — ChatGPT Project Instructions.md']='# Goth Rock — ChatGPT Project Instructions\n\nPaste this complete block into project instructions.\n\n```text\n'+instructions+'\n```\n\n[[Goth Rock — Start Here]] · [[Music Prompt Library]]\n'
prompts=[('Start the project',first),('History in chapters','Create a sourced chapter plan for Goth Rock from precursors and post-punk through early scenes, 1980s expansion, international development, later decades, and today. Begin the first chapter. Separate scene history from disputed genre origins; do not present an outline as the complete history.'),('Map styles and neighbors','Explain gothic rock, deathrock, darkwave, coldwave, ethereal wave, and nearby industrial/EBM, synthpop, and gothic metal. Distinguish sounds, scenes, clubs, press labels, and hybrids. Give sourced album examples with original years where supported; acknowledge regional terminology and contested boundaries.'),('Classics and overlooked records','Recommend five classic or overlooked albums for [era/style], with exact titles, original years, editions, historical roles, listening questions, and responsible links. Separate critical reputation from my enjoyment.'),('Post-punk roots and early scenes','Research Goth Rock’s post-punk roots and early scenes, including Batcave and positive punk. Compare source accounts, explain clubs versus musical categories, and recommend verified contrasting recordings without declaring one uncontested inventor.'),('Contemporary gothic rock and related revival','Recommend contrasting contemporary gothic rock recordings and separately labeled darkwave/deathrock neighbors. Verify dates and use independent appraisal where available. Separate established artists from debut projects and do not treat tags as proof of genre.'),('Regional scene','Research Goth Rock and related scenes in [country/region, such as Chile, Mexico, Japan, or Germany]. Cover local history, labels/clubs, classic recordings, and current artists. Verify claims and explain gaps without treating a nation as one sound.'),('Rank one year','Build a top [five/ten] for [year]. Use original gothic rock studio full-lengths; state whether deathrock or adjacent styles qualify. Establish the candidate pool before ranking. Explain criteria and placements, cite evidence, identify omissions, and keep editorial order, published lists, and my favorites separate. Do not pad thin years.'),('Develop annual archive','Research [year range] one year at a time. Verify original years and eligibility, distinguish reissues, and track gaps. Compare named published lists without inventing consensus. Prepare named Markdown updates.'),('Current releases','Research the actual current calendar year through today. Verify artist/label pages and classify released studio albums, future announcements, EPs/singles, live records, compilations, and reissues separately. Check platform dates against explicit corrections. Recommend three priorities; exclude upcoming albums from released rankings.'),('Emerging artists','Find promising debut/early-discography Goth Rock artists for [year/region/style], with adjacent styles labeled separately. Verify debut and formation details where available, mention earlier EPs and experienced-member projects, and give entry recordings plus independent appraisal. Do not call established acts new because of a new album.'),('Compare albums','Compare [album A] and [album B] on songwriting, vocal delivery, bass/guitar textures, rhythm, atmosphere, production, and context. Verify original years and editions. Use cited analysis and my reactions without claiming direct listening. Explain the best reason to try each.'),('Record my feedback','I listened to [artist/album/edition], [full album/sample]. My reaction: [feedback]. Optional date/score: [details]. Preserve my words, leave missing fields blank, and recommend two close matches plus one contrasting experiment. Ask one useful follow-up question.'),('Listening sequence','Plan a [number]-album or [length]-track sequence for [era/style/mood]. Verify recording identities, label direct links versus searches, and explain the progression. Do not claim playback or save a playlist unless I ask and it succeeds.'),('Continue and refresh notes','Summarize verified research, editorial recommendations, my explicit feedback/decisions, and gaps. Prepare named Markdown updates for this project and identify uploaded snapshots to replace. Do not claim automatic synchronization, saves, or uploads.')]
files['Music Prompts/Goth Rock — ChatGPT Project Prompts.md']='# Goth Rock — ChatGPT Project Prompts\n\nCopy one prompt into the project and replace bracketed fields.\n\n## Research add-on\n\n```text\nBrowse as of today and open sources. Verify identity, original year, edition, format, release status, and genre eligibility. Cite near claims. Separate fact, promotion, interpretation, editorial recommendation, and my reactions. Do not invent listening, scores, or consensus.\n```\n\n'+'\n\n'.join(f'## {i}. {title}\n\n```text\n{body}\n```' for i,(title,body) in enumerate(prompts,1))+'\n\n[[Goth Rock — Start Here]] · [[Music Prompt Library]]\n'
index=vault/'Music Prompts/Music Prompt Library.md';old=index.read_text(); anchor='\n**Create the next project:**'
assert anchor in old
files['Music Prompts/Music Prompt Library.md']=old.replace(anchor,'\n| Goth Rock | [[Goth Rock — ChatGPT Project Prompts|15 project prompts]] | [[Goth Rock — ChatGPT Project Instructions|Paste-ready instructions]] | [[Goth Rock — Start Here]] |\n'+anchor,1)
manifest={}
for rel,body in files.items():
 p=stage/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
 live=vault/rel;manifest[rel]=hashlib.sha256(live.read_bytes()).hexdigest() if live.exists() else None
(root/'manifest.json').write_text(json.dumps(manifest,indent=2))
pack=root/'Goth Rock — ChatGPT Project Pack';pack.mkdir(exist_ok=True)
context=files['Goth Rock — Start Here.md'].split('## ChatGPT setup')[0]+'\nPersonal preferences/listening: not yet supplied. Sources are snapshots; continue research gradually.\n'
for name,body in [('01_Project_Context_and_Method.txt',context),('02_History_Styles_and_Classics.txt',files['Goth Rock — History Styles and Classics.md']),('03_Rankings_and_Listening_Journal.txt',files['Goth Rock — Rankings and Listening Journal.md']),('04_Releases_and_New_Bands_2026.txt',files['Goth Rock — Releases and New Bands 2026.md']),('05_Research_and_Sources.txt',files['Goth Rock — Research and Sources 2026-10-08.md']),('Project Instructions.txt',instructions),('First Message.txt',first),('Reusable Prompts.txt',files['Music Prompts/Goth Rock — ChatGPT Project Prompts.md']),('README.txt','Create the ChatGPT project yourself. Upload the five numbered .txt files as Sources; paste Project Instructions.txt in instructions; send First Message.txt. Reusable Prompts.txt is optional reference. Snapshot: 8 October 2026. No automatic Obsidian synchronization.')]:
 (pack/name).write_text(body)
with zipfile.ZipFile(root/'Goth Rock — ChatGPT Project Pack.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in pack.iterdir():z.write(p,p.name)
# Ensure all local wiki targets exist after installing.
known={p.stem for p in vault.rglob('*.md')}|{Path(r).stem for r in files}
for rel,body in files.items():
 assert body.count('```')%2==0,rel
 for target in re.findall(r'\[\[([^\]|#]+)',body):assert target in known,(rel,target)
print('Staged 7 Goth Rock notes + shared index; checked wiki links and code fences; packed 9 text files.')
