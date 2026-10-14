from pathlib import Path
import re,json,hashlib,zipfile
root=Path(__file__).parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
staged=root/'staged'
topic='Hardcore & Punk'
def put(rel,content):
 p=staged/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
def note(suffix):return f'{topic} — {suffix}'
def block(text):return '```text\n'+text+'\n```\n'
scope='Keep punk rock and hardcore punk central. Explore melodic hardcore, D-beat, crust, anarcho-punk, street punk/Oi!, youth crew, and regional scenes as distinct research paths, not a universal taxonomy. Treat post-hardcore, emo, skate punk, and pop-punk as labeled related explorations. Crossover thrash, metallic hardcore, metalcore, and grindcore require explicit inclusion for rankings and focused playlists; do not assume all modern uses of “hardcore” mean the same sound. Hardcore electronic dance music is outside this project. Classify recordings rather than assigning an entire catalog one label. Distinguish musical style, scene, political tradition, and personal lifestyle; straight edge is not a synonym for all hardcore. Explain contested terminology without gatekeeping.'
first='Read this project’s context and instructions. Help me explore punk rock and hardcore punk through history, styles, classics, current discoveries, and regional scenes. Explain what has been verified and what is still a research plan. Offer a chronological path and a sound-based path, then suggest three contrasting starter recordings. Include short releases when appropriate and identify their format. Ask what I already enjoy without assuming prior listening or scores.'
instructions=f'''You are my Hardcore & Punk research and listening partner. Develop my understanding and taste from explicit feedback. Keep research, listening history, and rankings separate from my metal, Goth Rock, and travel projects.

Read 01_Project_Context_and_Method.txt first. This starter pack was prepared 9 October 2026. Latest user instructions and feedback override uploaded snapshots. ChatGPT uploads and Obsidian do not synchronize automatically; name the notes and replacement snapshots when preparing updates.

{scope}

Develop connected history chapters from precursors and early punk scenes through hardcore, international developments, later branches, and contemporary DIY networks. Investigate venues, independent labels, zines, recording, distribution, all-ages shows, community practices, and lyrical context. Include women, LGBTQ+ contributors, and scenes beyond the best-known US/UK examples, including Chile and Latin America where evidence supports them. Research leads are questions, not established historical conclusions. Compare accounts rather than declaring one universal inventor or reducing a region to one sound.

Use artist/label catalogs and credits for exact recording identities, original release dates, format, and editions. Open sources before relying on them; cite near claims, state research date, and attribute interviews, criticism, and promotional language. Separate factual metadata, documented influence, musical comparison, and editorial interpretation. Do not imply a whole book was read from its sales page. Explain conflicts and leave unresolved details visible. Use accessible listening cues about pace, riffs, rhythm, vocal delivery, hooks, arrangement, production, and lyrics; never invent direct listening or timestamps.

Recommend three to five recordings per batch with exact titles, original years, formats, reasons, listening questions, and official links or labeled searches. Short EPs, singles, demos, and splits are valid discoveries; do not force this project into an album-only history. Distinguish original releases from archival compilations and remasters. Summarize verified lyrical themes without reproducing full lyrics or assuming every artist shares one politics or lifestyle.

For annual rankings maintain separate full-length and short-release pools. Default album eligibility: original studio full-lengths first released in the chosen year within punk rock/hardcore punk; explicitly state branches included. EPs, singles, demos, and split releases need their own eligibility and format labels. For splits, credit each artist and clarify whether ranking the whole release or one side. Keep live records, compilations, and reissues separate. State candidate pool, criteria, omissions, and boundary uncertainty; use fewer entries when evidence is thin. Evaluate songwriting, identity, performance, and production serving the music; discuss historical impact separately. Separate editorial order, named published rankings, and my favorites. Do not invent numeric precision, personal scores, or consensus.

Use the actual current calendar year for current releases, with a cutoff date. Verify full-release status and original dates from artist/label sources. Separate released full-lengths, short releases, upcoming announcements, live records, archival compilations, and reissues. Do not rank unavailable recordings from previews. Current-year lists are best so far. Define emerging for each search, defaulting to debut/early-discography; mention earlier demos/EPs and experienced-member projects. Established bands releasing new music are not new bands. Seek regional variety without inventing acclaim, formation dates, or popularity metrics.

Keep my listening journal blank until I report feedback. Preserve my words, supplied date, exact edition, full listen versus sample, favorite moments, and optional score; leave missing fields blank. Suggest two close matches and one contrasting experiment afterward. Ask one useful preference question at a time.

Respond in the language I use. Provide manageable batches and practical next steps. Do not claim playback, saved playlists, account access, uploads, purchases, alerts, or publication unless requested and successfully performed. Spotify prompts request plans unless an explicit save request is included. This pack is a starter, not an exhaustive history or current-release survey.'''
put('Music Prompts/'+note('ChatGPT Project Instructions')+'.md','# '+note('ChatGPT Project Instructions')+'\n\nPaste this complete block into project instructions.\n\n'+block(instructions)+f'\n[[{note("Start Here")}]] · [[Music Prompt Library]]\n')
prompts=[
('Start the project',first),
('History in chapters','Create a sourced chapter plan for punk rock and hardcore punk from relevant precursors to today. Compare early regional developments, later hardcore paths, and international DIY networks. Begin the first chapter. Distinguish historical evidence from disputed origins and do not present an outline as the whole history.'),
('Map sounds and neighbors',scope+' Give sourced recording examples with exact titles, original years, and formats. Explain practical listening cues and contested boundaries.'),
('Classics beyond full-lengths','Recommend five classic or overlooked punk/hardcore recordings for [era/style]. Include EPs or singles when appropriate, clearly labeling formats. Verify original years and editions. Explain historical significance separately from musical appeal and give one listening question per recording.'),
('DIY, labels, and zines','Research [punk/hardcore scene] through labels, zines, venues, all-ages shows, distribution, and community practices. Use archives and participant accounts with context. Connect this history to verified recordings without romanticizing a single scene or assuming shared politics.'),
('Hardcore and metal boundaries','Compare punk-rooted hardcore, metallic hardcore, crossover thrash, and metalcore through verified contrasting recordings. Separate shared audiences from musical classification. Explain disputed terminology by era and scene, and ask which branches I want included in this project’s playlists and rankings.'),
('Regional scene','Research punk and hardcore in [country/region, such as Chile, Latin America, Japan, or the UK]. Verify local histories, labels, recordings, and current artists. Show gaps and regional differences. Recommend a manageable batch including short releases if relevant.'),
('Rank one year','Develop an editorial top [five/ten] punk/hardcore studio full-lengths for [year]. State included branches and verify a candidate pool before ranking. Prepare a separate short-release list if requested; do not mix EPs, demos, splits, or reissues into the album pool. Distinguish editorial recommendations, named published lists, and my personal favorites.'),
('Build an annual archive','Research [year range] one year at a time. Track original studio albums and short releases separately, preserving format and edition details. Record sources, disputed eligibility, omissions, and unfinished years. Do not pad weak pools or imply an unfilled archive is complete.'),
('Current releases','Research punk/hardcore releases from the actual current calendar year through today. Open artist/label sources; verify original dates and release status. Separate released full-lengths, EPs/singles/demos/splits, upcoming announcements, live records, compilations, and reissues. Recommend three priorities with reasons; state included styles and the research cutoff.'),
('Emerging artists','Find five debut/early-discography punk/hardcore artists for [region/style/year]. Verify release history and formation details where available, mention earlier demos/EPs and experienced-member projects, and distinguish emerging from new to me. Give entry recordings and attributed independent appraisal when available; use fewer if evidence is insufficient.'),
('Compare recordings','Compare [recording A] and [recording B] on songwriting, pace, riffs, rhythm, vocals, hooks, arrangement, production, and context. Verify original years, formats, and editions. Use sources and my feedback without claiming unsupported audio access. Explain why each is worth trying.'),
('Record my feedback','I listened to [artist/recording/edition], [full listen/sample]. My reaction: [feedback]. Optional date and score: [details]. Preserve my wording in this project’s journal and leave missing fields blank. Recommend two close matches and one contrasting experiment; ask one useful follow-up question.'),
('Listening route','Plan a [number]-recording or [length]-track punk/hardcore listening route for [era/style/theme]. Include short releases where useful, label neighbors, verify identities and original years, and explain the progression. Give direct links or clearly labeled searches. Do not claim playback or saves without requested, successful actions.'),
('Continue and refresh notes','Summarize verified research, editorial recommendations, my explicit feedback and decisions, and unresolved gaps. Prepare named Markdown updates for Hardcore & Punk notes and identify uploaded snapshots to replace. Preserve other music projects and do not claim automatic synchronization.')]
prompt_text='# '+note('ChatGPT Project Prompts')+'\n\nCopy a prompt into this separate project and replace bracketed fields.\n\n## Research add-on\n\n'+block('Browse as of today and open sources. Verify exact recording identity, original year, format, edition, release status, and scope. Cite near claims; separate fact, promotional language, interpretation, editorial recommendation, and my reactions. Do not invent listening, scores, or consensus.')
for i,(title,prompt) in enumerate(prompts,1):prompt_text+=f'\n## {i}. {title}\n\n'+block(prompt)
prompt_text+=f'\n[[{note("Start Here")}]] · [[Music Prompt Library]]\n\n## Spotify playlists and discovery\n\n[[Spotify — Playlists and Music Discovery Prompts#Hardcore & Punk|Seven Hardcore & Punk Spotify prompts]]\n'
put('Music Prompts/'+note('ChatGPT Project Prompts')+'.md',prompt_text)
history=f'''# {note('History Styles and Classics')}

Prepared **9 October 2026**. This is a chapter plan with three checked starter identities, not a completed historical survey. Style paths below are research scope, not verified origin claims.

## History to develop

| Chapter | Research questions |
| --- | --- |
| Precursors and early punk | Compare accounts of musical precursors and early regional scenes; verify recordings rather than naming one universal origin. |
| Hardcore developments | Investigate early US and international developments, recording practices, tempo, arrangements, and local terminology. |
| DIY networks | Examine independent labels, zines, venues, all-ages shows, touring, and distribution through archives and participant accounts. |
| Distinct paths | Explore melodic hardcore, D-beat, crust, anarcho-punk, street punk/Oi!, and youth crew without equating scenes with uniform sounds. |
| Neighboring styles | Compare post-hardcore, emo, skate punk, pop-punk, crossover thrash, and metallic hardcore with clear eligibility decisions. |
| International scenes | Investigate Chile/Latin America, Japan, Europe, and other documented scenes; avoid treating each country as one sound. |
| Contemporary discovery | Verify new recordings and emerging artists, keeping albums and short releases separate. |

## Starter listening route

These are editorial starting points to compare, not a ranked canon or personal favorites. Listening questions describe what to investigate rather than claimed direct audio analysis.

| Recording | Original year / format | Listening question | Checked source |
| --- | --- | --- | --- |
| Ramones — Ramones | 1976 / studio album | How do compact songs and hooks shape your enjoyment? | [Rhino label overview](https://www.rhino.com/aod/ramones-ramones) supports debut identity and original year. Its “first true punk album” wording is a promotional interpretation, not adopted here as an uncontested origin claim. |
| Minor Threat — Out of Step | 1983 / 12-inch EP in the label catalog | What do you enjoy about pace, vocal attack, and rhythmic changes? | [Official Bandcamp](https://minorthreat.bandcamp.com/album/out-of-step) confirms original year; [Dischord catalog](https://dischord.com/release/010/out-of-step) identifies the EP format. Preserve this label designation despite varying platform descriptions. |
| Fugazi — Repeater | 1990 / studio full-length; related post-hardcore exploration | How do rhythm, arrangement, and vocal interplay change the route? | [Dischord catalog](https://dischord.com/release/044/repeater) confirms first full-length and original year; 2009 refers to a later vinyl recut/reissue. The related-style placement is editorial and needs further genre-source work. |

## Scope decisions

{scope}

Next: add attributed historical and critical sources, verify more contrasting recordings, and develop a first chapter. Short releases deserve their own treatment rather than exclusion from the listening path.

[[{note('Start Here')}]]
'''
put(note('History Styles and Classics')+'.md',history)
rank=f'''# {note('Rankings and Listening Journal')}

## Ranking method

Keep editorial recommendations, attributed published lists, and personal favorites separate. Default album eligibility is original punk rock/hardcore punk studio full-lengths first released in the chosen year, with included branches stated. Maintain a separate short-release pool for EPs, singles, demos, and splits; identify artists and sides for splits. Keep live recordings, archival compilations, and reissues separate. Do not let remaster dates replace original years.

Establish a sourced candidate pool before ranking. Explain songwriting, identity, performance, and production serving the music; discuss historical impact separately. Record exclusions, uncertain classifications, and gaps. Use fewer entries when justified and do not invent scores or consensus.

## Annual archive

No rankings completed. The three starter recordings are a listening route, not an annual ranking.

| Year | Studio album pool | Short-release pool | Editorial list | Published lists | My favorites | Gaps |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Pending research | Pending research | Pending | Pending | | Scope and candidate verification |

## Listening journal

No listening sessions or personal ratings reported.

| Date supplied | Artist / recording / edition | Format | Full listen or sample | My exact feedback | Favorite moments | Optional score | Next discovery |
| --- | --- | --- | --- | --- | --- | --- | --- |

Leave missing fields blank. Preserve my words; after feedback suggest two close matches and one contrasting experiment.

[[{note('Start Here')}]]
'''
put(note('Rankings and Listening Journal')+'.md',rank)
release=f'''# {note('Releases and New Bands 2026')}

Prepared **9 October 2026**. Current-year discovery is an open research task; no release census, emerging-band shortlist, or best-so-far ranking has been completed.

## Research plan

Verify exact artist/title, original date, format, release status, and genre scope from opened artist/label pages. Add attributed independent appraisal where available. State the cutoff date for each future check.

Keep released studio full-lengths, EPs/singles/demos/splits, upcoming announcements, live recordings, compilations, and reissues in separate sections. Short releases are valid discoveries and need their own rankings. Do not treat preorder previews as released full recordings.

## Emerging artists

Default to debut/early-discography with evidence. Mention prior demos and EPs and experienced musicians in new projects. Distinguish established acts with new music from emerging artists, and new to me from new bands. Formation dates and popularity stay unknown unless checked.

## Next step

Run the current-release or emerging-artist prompt in [[{note('ChatGPT Project Prompts')}]]. Seek documented regional variety, including Chile/Latin America when sources support it, without filling gaps with unrelated recordings.

[[{note('Start Here')}]]
'''
put(note('Releases and New Bands 2026')+'.md',release)
sources=f'''# {note('Research and Sources 2026-10-09')}

Checked **9 October 2026**. Narrow metadata check for the starter route; history, genre classifications, current releases, and wider critical reception remain open research.

| Opened source | Evidence used | Limits |
| --- | --- | --- |
| [Rhino — Ramones](https://www.rhino.com/aod/ramones-ramones) | Debut identity and original year 1976 | Label retrospective; promotional origin and acclaim language is not independent consensus. |
| [Minor Threat — Out Of Step, official Bandcamp](https://minorthreat.bandcamp.com/album/out-of-step) | Original release year 1983 | Streaming/merch page, not independent critical analysis. |
| [Dischord — Out of Step](https://dischord.com/release/010/out-of-step) | Label designates 12-inch EP; credits and tracklist | Current edition mentions 2008 remaster/recut; do not use that as the original year. |
| [Dischord — Repeater](https://dischord.com/release/044/repeater) | First Fugazi full-length, originally 1990 | 2009 is a later vinyl reissue; genre placement is a project interpretation pending further sources. |
| [Dischord — Minor Threat biography](https://dischord.com/band/minor-threat) | Lead for DC history and straight-edge context | Label account; compare further historical sources before extending claims. |

## Research gaps

Add historical archives and attributed criticism, compare regional terminology and disputed boundaries, verify additional classics and overlooked recordings, and research current-year releases and emerging artists. No direct audio listening, playlist creation, personal score, or exhaustive historical survey was performed.

[[{note('Start Here')}]]
'''
put(note('Research and Sources 2026-10-09')+'.md',sources)
dashboard=f'''# {note('Start Here')}

Prepared **9 October 2026**. A separate music research and listening starter project, organized like the existing genre projects.

## Scope

{scope}

## Project notes

- [[{note('History Styles and Classics')}]]
- [[{note('Rankings and Listening Journal')}]]
- [[{note('Releases and New Bands 2026')}]]
- [[{note('Research and Sources 2026-10-09')}]]
- [[{note('ChatGPT Project Instructions')}]]
- [[{note('ChatGPT Project Prompts')}|15 research and listening prompts]]
- [[Music Prompt Library]]
- [[Spotify — Playlists and Music Discovery Prompts#Hardcore & Punk|Seven Spotify prompts]]

## Three starter recordings

**Ramones — Ramones (1976)** → **Minor Threat — Out of Step (1983, EP)** → **Fugazi — Repeater (1990, related exploration)**. Original years and source links are in [[{note('History Styles and Classics')}]]. This route includes two albums and an EP; it is an editorial introduction, not a personal ranking.

## ChatGPT setup

Suggested project name: **Hardcore & Punk — History, Classics & Discovery**. The local upload pack contains five numbered context/source files, paste-ready instructions, reusable prompts, a first message, and Spotify prompts. Create the separate ChatGPT project, upload the five numbered files, paste Project Instructions.txt into its instructions, and send First Message.txt. This prepares a local pack; it does not create the app project or upload anything automatically.

## First message

{block(first)}
## Next step

Choose a listening route, a history chapter, or a current-release search. The initial source check covers three starter recording identities. Broader history and contemporary discovery remain research tasks; personal feedback and scores stay blank until supplied.
'''
put(note('Start Here')+'.md',dashboard)
spotify_prompts=[
('First exploration — No Quiet Exit','Spotify, curate a 24-track “Hardcore & Punk — No Quiet Exit” listening plan balancing punk rock and hardcore punk across classic and contemporary recordings. Use no more than two tracks per artist and include tracks from EPs or singles when relevant. Label melodic hardcore, D-beat/crust, and other branches; put post-hardcore in a separate optional section. Do not substitute metalcore or electronic hardcore. Show exact artist, track, original release, year, and format. Explain the journey without assuming I have heard anything.'),
('Fast, melodic, and abrasive','Spotify, plan an 18-track punk/hardcore comparison in three chapters: fast and compact, melodic and hook-driven, and abrasive or rhythmically varied. Treat these as listening descriptions, not a fixed taxonomy. Use six contrasting tracks per chapter with verified original releases and formats. Label neighboring styles and ask which features I enjoy before recommending a follow-up. Avoid duplicate songs and invented timestamps.'),
('This year’s discoveries','Research punk/hardcore releases from the actual current calendar year through today. Verify original dates, formats, status, and included branches from opened artist/label sources. Choose up to five released recordings and ask Spotify to curate two verified tracks per recording where available. Label albums and EPs separately; keep demos/splits explicit and announcements, live records, compilations, and reissues separate. Use fewer candidates if needed, cite sources, and label this a discovery batch rather than a final ranking.'),
('Emerging artists','Find five debut/early-discography punk/hardcore artists in [region/style]. Verify release history, mention earlier EPs/demos and experienced-member projects, and distinguish emerging from new to me. Spotify, curate up to two available tracks per artist, with exact original releases and format labels. Attribute independent appraisal when available, avoid unsupported acclaim, and do not replace catalog gaps with unrelated artists.'),
('Short releases, complete statements','Spotify, plan a listening session using four punk/hardcore EPs or singles from [era/style]. Verify original identities, track orders, years, formats, and runtimes where available. Preserve each release as a complete block rather than scattering its songs. Explain why each belongs and label archival compilation matches when original releases are unavailable. Do not mistake a compilation’s date for the original year or force short releases into an album ranking.'),
('Punk roots and heavier branches','Spotify, propose two separate eight-track listening routes: punk-rooted hardcore and metallic/crossover neighbors. Verify classifications and label disputed cases; do not treat metalcore, crossover thrash, and metallic hardcore as synonyms. Explain shared features and differences through supported descriptions, distinguishing documented influence from your comparison. Keep the second route optional so I can decide whether to include it in this project.'),
('Chile and beyond','Research punk/hardcore in [Chile or another chosen region] using opened historical and artist/label sources. Spotify, plan up to 15 verified tracks across documented eras or branches. Show local context, original releases, and formats. Explain catalog gaps and give official listening alternatives separately; do not fill the list with unrelated artists or imply the region has one sound. Keep regional history and contemporary promotion distinct.')]
spotify_add=f'\n## {topic}\n\n[[{note("Start Here")}|Project dashboard]] · [[{note("ChatGPT Project Prompts")}|Research prompts]]\n\nAdded **2026-10-09**. Use the shared quality add-on and append the optional save request when you want a new playlist saved.\n'
for i,(title,prompt) in enumerate(spotify_prompts,39):spotify_add+=f'\n### {i}. {title}\n\n'+block(prompt)
manifest={}
for rel in ['Music Prompts/Music Prompt Library.md','Music Prompts/Spotify — Playlists and Music Discovery Prompts.md']:
 original=(vault/rel).read_bytes();manifest[rel]=hashlib.sha256(original).hexdigest()
 b=root/'backup'/rel;b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(original)
 content=original.decode()
 if rel.endswith('Music Prompt Library.md'):
  row=f'| {topic} | [[{note("ChatGPT Project Prompts")}|15 project prompts]] | [[{note("ChatGPT Project Instructions")}|Paste-ready instructions]] | [[{note("Start Here")}]] |\n'
  marker='\n**Create the next project:**';assert marker in content
  content=content.replace(marker,row+marker,1).replace('38 ready-to-paste prompts','45 ready-to-paste prompts').replace('four genre-specific sets','five genre-specific sets')
 else:
  content=content.replace('traditional Heavy Metal, and Goth Rock**','traditional Heavy Metal, Goth Rock, and Hardcore & Punk**',1)+spotify_add
 put(rel,content)
for p in staged.rglob('*.md'):
 rel=str(p.relative_to(staged))
 if rel not in manifest:
  assert not (vault/rel).exists(),f'Existing note: {rel}'
  manifest[rel]=None
(root/'manifest.json').write_text(json.dumps(manifest,indent=2))
# Validate all note targets and anchors against the staged + live notes.
all_notes={p.stem:p for p in vault.rglob('*.md')}
all_notes.update({p.stem:p for p in staged.rglob('*.md')})
for p in staged.rglob('*.md'):
 content=p.read_text();assert content.count('```')%2==0,p
 for target in re.findall(r'\[\[([^]|]+)',content):
  name,sep,anchor=target.partition('#');assert name in all_notes,(p,target)
  if sep:assert re.search(r'^#+ '+re.escape(anchor)+r'$',all_notes[name].read_text(),re.M),(p,target)
sp=(staged/'Music Prompts/Spotify — Playlists and Music Discovery Prompts.md').read_text()
assert [int(n) for n in re.findall(r'^### (\d+)\.',sp,re.M)]==list(range(1,46))
# Create a portable local project upload pack without stale wiki links.
pack=root/(topic+' — ChatGPT Project Pack');pack.mkdir(exist_ok=True)
def portable(s):
 return re.sub(r'\[\[([^]]+)\]\]',lambda m:m.group(1).split('|')[-1],s)
files={
 '01_Project_Context_and_Method.txt':dashboard,
 '02_History_Styles_and_Classics.txt':history,
 '03_Rankings_and_Listening_Journal.txt':rank,
 '04_Releases_and_New_Bands_2026.txt':release,
 '05_Research_and_Sources.txt':sources,
 'Project Instructions.txt':instructions,
 'Reusable Prompts.txt':prompt_text,
 'First Message.txt':first,
 'Spotify Prompts.txt':'## Optional save request\n'+(vault/'Music Prompts/Spotify — Playlists and Music Discovery Prompts.md').read_text().split('## Optional save request')[1].split('## Death Metal')[0]+spotify_add,
 'README.txt':'Prepared 9 October 2026. Create a separate Hardcore & Punk ChatGPT project. Upload the five numbered text files, paste Project Instructions.txt into project instructions, then send First Message.txt. Reusable Prompts.txt and Spotify Prompts.txt are optional prompt references. This is a starter pack, not a completed current-release survey. No project creation, uploads, playback, or playlist saves were performed. Local notes and uploads do not automatically synchronize.'}
for name,content in files.items():(pack/name).write_text(portable(content))
with zipfile.ZipFile(root/(topic+' — ChatGPT Project Pack.zip'),'w',zipfile.ZIP_DEFLATED) as z:
 for p in pack.iterdir():z.write(p,pack.name+'/'+p.name)
print(f'Prepared {len(manifest)} notes, 15 project prompts, 7 new Spotify prompts, and checked upload pack. Wiki links and anchors resolve; Spotify prompts numbered 1–45.')
