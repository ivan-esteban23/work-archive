from pathlib import Path
import hashlib,json,re
root=Path('/home/ivanaguilera/Work/spotify-music-prompts-20261008');vault=Path('/home/ivanaguilera/Documents/Obsidian Vault');stage=root/'staged';stage.mkdir(exist_ok=True)
name='Spotify — Playlists and Music Discovery Prompts';rel='Music Prompts/'+name+'.md'
intro='''---
tags: [music, prompts, spotify]
created: 2026-10-08
---
# Spotify — Playlists and Music Discovery Prompts

[[Music Prompt Library|Music prompt index]]

Ready-to-paste prompts for **Death Metal, Black Metal, traditional Heavy Metal, and Goth Rock**. Open the matching ChatGPT music project so its uploaded sources and conversation can inform the request. Mention **Spotify** explicitly. Replace bracketed fields; use English or translate the prompt into Spanish.

## How to use

1. Start with a genre's **first exploration** prompt, or choose current releases / emerging artists.
2. If you want a saved playlist, append the **save request** below. Without it, the prompts request curation rather than a library change.
3. Review unavailable recordings, editions, and the resulting Spotify card. A text tracklist is a plan, not evidence of a saved playlist.
4. Bring back your reactions using the feedback prompt. Local Obsidian notes and uploaded project sources do not automatically synchronize; upload updated notes when needed. For a combined playlist, provide context from all relevant projects instead of assuming cross-project access.

The earlier Spotify guidance was checked against [Spotify’s official ChatGPT announcement](https://newsroom.spotify.com/2025-10-06/spotify-personalized-prompts-chatgpt/). Premium supports custom selections; automatic saving and precise editing depend on the actions available in your chat. These prompts do not guarantee account access or successful saves. No playlist or playback was performed while preparing this library.

## Optional save request

Append this to a playlist prompt when you want the action performed:

```text
Create this as a new playlist in my linked Spotify account, named “[playlist name]”. Use private visibility if that option is supported; if visibility cannot be controlled, explain before saving. Leave existing playlists unchanged. If the available Spotify integration cannot save a playlist, provide the curated tracklist and available Spotify links instead. Only confirm creation when the tool reports success, and return the playlist link; otherwise state the remaining step.
```

## Shared quality add-on

```text
Use this project's available sources and my explicit feedback. Verify exact artist, track, album, and edition; show original release year rather than substituting a remaster year. Use Spotify's catalog tools if available to check matches, and label unverified matches or title searches. Prefer studio versions unless I ask otherwise; avoid duplicates. Explain any unavailable track and proposed replacement. Do not claim access to my listening history or other projects unless it is actually available. Do not claim direct listening, playback, or saves without evidence.
```
'''
parts=[intro];n=0
scopes={
'Death Metal':('old-school, technical, brutal, and melodic death metal, with death/doom and progressive hybrids clearly labeled','riffs, growled vocals, rhythm, melody, atmosphere, and production','death-metal'),
'Black Metal':('early roots, raw, melodic, atmospheric, and symphonic black metal, with experimental hybrids clearly labeled','guitar texture, harsh vocals, repetition, atmosphere, melody, and production','black-metal'),
'Heavy Metal':('traditional heavy metal, NWOBHM, epic/melodic approaches, and modern traditional revival; distinguish movements from styles and label heavy/speed or heavy/doom hybrids','riffs, clean vocals, guitar harmonies, groove, melody, and production','traditional-heavy-metal'),
'Goth Rock':('gothic rock, with deathrock and darkwave in separately identified related sections; explain coldwave and ethereal wave as neighbors when relevant, and keep gothic metal and industrial/EBM outside the core selection','bass lines, guitar texture, vocal delivery, rhythm, atmosphere, and production','goth-rock')}
for genre,(scope,cues,slug) in scopes.items():
 parts.append(f'## {genre}\n\n[[{genre} — Start Here|Project dashboard]] · [[{genre} — ChatGPT Project Prompts|Research prompts]]\n')
 prompts=[('First exploration playlist',f'''Spotify, curate a 24-track “{genre} — First Exploration” playlist using this project's sources. Balance classics, overlooked recordings, and contemporary discoveries. Use {scope}. Choose no more than two tracks per artist, avoid duplicate songs, and arrange the sequence as a gradual listening journey. Show artist, track, album, original year, and a short explanation of each section. Use my stated preferences if available; otherwise label the selection as exploratory. Do not assume I have heard these recordings.'''),
 ('Explore styles through songs',f'''Spotify, curate an 18-track listening tour of {genre}. Cover {scope}. Choose contrasting recordings with verified identities and years rather than claiming to cover every subgenre. Explain which musical feature each track illustrates and label disputed boundaries. Give me a compact tracklist and practical questions about {cues}. Keep album-level classification distinct from a band's entire catalog.'''),
 ('Discover this year’s releases',f'''Research {genre} releases from the actual current calendar year through today, stating the year and cutoff date. Open artist/label sources and verify original dates and release status. Recommend five released studio albums with reasons, then ask Spotify to curate a 10-track discovery selection using two verified tracks from each eligible album when available. Label hybrids and adjacent styles. Keep upcoming albums, EPs/singles, live records, compilations, and reissues in separate research sections; do not fill the released-album selection with preorder previews. If fewer than five suitable albums are verified, use fewer. Provide sources and Spotify matches or labeled searches. This is a discovery selection, not a final year-end ranking.'''),
 ('Find emerging artists',f'''Find five promising {genre} artists under a debut/early-discography definition. Verify debut albums and original dates, mention earlier EPs, and identify experienced musicians in new projects when supported. Do not call established acts new because they released a new album. Explain why each candidate is worth exploring using attributed independent appraisal where available; label promotional claims and unknown formation dates. Then ask Spotify for a 10-track introduction with up to two available recordings per artist. Include varied documented scenes and label hybrids; do not invent acclaim or force a regional quota. Keep new to me separate from genuinely early-discography.''')]
 for title,prompt in prompts:
  n+=1;parts.append(f'### {n}. {title}\n\n```text\n{prompt}\n```\n')
shared=[('Discover from my feedback','''I listened to [artist / album / tracks] in my [genre] project. I enjoyed [details] and disliked [details]. My known artists are [list, or leave unknown]. Recommend three albums: two close matches and one contrasting experiment, explaining the connections. Spotify, curate a nine-track preview with three verified tracks per album where available. Exclude only the tracks/artists I explicitly ask to exclude. Preserve my feedback for a Markdown journal update, leave missing fields blank, and do not infer full-album listening from track samples.'''),('Overlooked music beyond familiar names','''Find five overlooked [genre] albums for [era/region/style], using this project's scope. Define overlooked for this search and use evidence without claiming unsupported listener counts or universal obscurity. Avoid [artists I already know]. Include independent appraisal when available, original years, and one useful listening question per album. Spotify, curate a 15-track introduction with up to three verified tracks per album. Label artist promotion and genre uncertainty.'''),('Explore a regional scene','''Research [genre] in [country/region, such as Chile, Latin America, Japan, or Korea]. Give me a sourced introduction and five album discoveries spanning documented eras or styles where possible. Distinguish local history from current artist descriptions; do not treat a country as one sound. Spotify, curate an introduction of up to 15 verified tracks. Report catalog gaps and provide official listening alternatives separately; do not replace unavailable local artists with unrelated bands just to fill the list.'''),('Turn an annual ranking into a playlist','''Use the sourced [genre] album ranking for [year] already developed in this project. If it does not exist, establish eligibility and a verified candidate pool before proposing a provisional editorial ranking; do not invent my personal favorites or a critical consensus. Spotify, curate up to three tracks per ranked album in ranking order. Show original release years, distinguish edition dates, and explain song choices. Exclude unavailable or upcoming full albums from a released-album ranking and do not pad thin years.'''),('A separate playlist for each music project','''I want four distinct discovery playlists: Death Metal, Black Metal, traditional Heavy Metal, and Goth Rock. Use the project summaries and preferences I provide below; do not assume access to separate project chats. [Paste relevant context from each project.] Spotify, curate 20 tracks per genre, balancing classic and contemporary recordings with no duplicate songs within each list. Follow each project's genre boundaries, label hybrids, and explain the listening sequence. Keep the playlists separate and show exact matches or unresolved searches. Do not save them unless I explicitly include a save request.'''),('Refresh discoveries when I return','''Refresh my [genre] discovery research as of today. Here is the previous tracklist and cutoff: [paste]. Verify newly released recordings since that date and recommend up to ten fresh tracks, avoiding duplicates from the supplied list. Separate released albums, EPs/singles, future announcements, and reissues. Spotify, curate a new dated discovery selection rather than changing my previous playlist. Do not claim continuous monitoring or scheduled updates; run this refresh only for this request.''')]
parts.append('## Reusable discovery prompts\n')
for title,prompt in shared:
 n+=1;parts.append(f'### {n}. {title}\n\n```text\n{prompt}\n```\n')
body='\n'.join(parts)
files={rel:body}
indexrel='Music Prompts/Music Prompt Library.md';index=(vault/indexrel).read_text()
# Repair accidental blank line that interrupted the project table.
index=index.replace('| [[Heavy Metal — Start Here]] |\n\n| Goth Rock','| [[Heavy Metal — Start Here]] |\n| Goth Rock')
anchor='## Research add-on\n';assert anchor in index
index=index.replace(anchor,f'## Spotify playlists and discovery\n\n[[{name}|22 ready-to-paste prompts]] — four genre-specific sets, plus feedback, overlooked albums, regional scenes, annual rankings, and refresh prompts. Includes an optional save request.\n\n'+anchor,1)
files[indexrel]=index
for genre in scopes:
 for path in [f'{genre} — Start Here.md',f'Music Prompts/{genre} — ChatGPT Project Prompts.md']:
  old=(vault/path).read_text()
  files[path]=old.rstrip()+f'\n\n## Spotify playlists and discovery\n\n[[{name}]] — use the {genre} section for playlist creation requests, current releases, and emerging artists.\n'
manifest={}
for path,text in files.items():
 p=stage/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
 live=vault/path;manifest[path]=hashlib.sha256(live.read_bytes()).hexdigest() if live.exists() else None
known={p.stem for p in vault.rglob('*.md')}|{Path(p).stem for p in files}
for path,text in files.items():
 assert text.count('```')%2==0,path
 for target in re.findall(r'\[\[([^\]|#]+)',text):assert target in known,(path,target)
assert n==22
(root/'manifest.json').write_text(json.dumps(manifest,indent=2))
(root/'Spotify — Playlists and Music Discovery Prompts.txt').write_text(body)
print(f'Staged {len(files)} notes; verified {n} prompts, wiki targets, and code fences.')
