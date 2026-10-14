from pathlib import Path
import json
ROOT=Path(__file__).parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
NAME='Goth Rock — Notion Development Prompts'
groups=[('Develop the whole note',[
('Audit the listening room','Read my current Goth Rock note, linked dossiers, and source archive. Identify missing context, repetitive sections, confusing navigation, and unsupported claims. Give five concrete improvements in priority order, naming the target section and expected benefit. Preserve my existing preferences and distinguish new work from work already complete.'),
('Build the next expansion','Expand [section] with a connected explanation, a compact visual element, and three useful listening questions. Read the existing section first. Preserve its sources and user-written material; add verified references next to new factual claims. Make the addition fit the rest of the note.'),
('Make an accessible entry route','Create a short Start Here block for the listening room, with routes for raw deathrock, classic gothic rock, and atmospheric exploration. Link existing dossiers before proposing new ones. Explain what each route helps me hear; keep recommendations separate from confirmed favorites.'),
('Improve the seven-part structure','Review my album gallery, album dossiers, visual listening profile, history timeline, scene atlas, journal, and visual rhythm together. Identify gaps between them, add useful cross-links, and implement the three strongest improvements within the current structure. Keep unfinished research visibly marked.'),
('Turn a research question into a section','Investigate [question] using opened, dated sources. Write a focused addition for [target section] with the answer, competing accounts where material, recordings to explore, and remaining uncertainty. Explain why this question matters for my Goth Rock listening.'),
('Create a monthly development plan','Create a four-week plan to develop this note: one history task, one scene task, one underground discovery task, and one review of my actual feedback. Each week needs a small deliverable and an existing section to update. Treat listening as a proposed activity until I report it.')]),
('Album gallery and dossiers',[
('Add a complete album dossier','Add [artist — album] to the appropriate gallery shelf and create its dossier. Verify original release date, exact linked edition, format, tracklist, credits, and official listening page. Include musical context from attributed sources, three listening questions, cover art with source, and links to a scene and timeline milestone where supported.'),
('Deepen an existing dossier','Expand [album dossier] with historical context, personnel and production credits, edition differences, attributed reception, and an entry track. Separate source-backed facts from editorial listening suggestions. Preserve my feedback verbatim and leave unknown listening status or scores blank.'),
('Compare three deathrock records','Build a comparison of 45 Grave’s Sleep in Safety, Kommunity FK’s The Vision and the Voice, and Cinema Strange’s The Astonished Eyes of Evening. Compare rhythm, guitar texture, voice, atmosphere, period, and edition considerations using sources. End with a three-record listening worksheet; do not claim I heard them.'),
('Explain originals and reissues','Audit [album or shelf] for original-year versus linked-edition confusion. Show original release, current listening edition, bonus tracks or remaster differences when documented, and unresolved metadata conflicts. Update dossier labels so a reissue is not presented as a new studio album.'),
('Improve gallery shelves','Organize the existing albums into useful views or sections: next listens, explicitly stated favorites, deathrock references, atmospheric comparisons, and all albums. Use existing metadata, prevent accidental favorite assignments, and show title, artist, original year, cover, and dossier link. State which native Notion views were actually created.'),
('Add overlooked recordings','Research five less-covered recordings for [style, era, or region]. Explain what makes each a useful addition rather than simply calling it underrated. Verify identity, genre fit, original year, edition, and official links. Add the best three dossiers with sources and covers; keep the rest as a research shortlist.')]),
('Images and visual design',[
('Find authentic album covers','For [albums], find authentic covers on artist, label, or official release pages. Check the artwork matches the linked edition. Add images, captions, source links, and available credits. Flag uncertain edition matches; use actual cover art rather than generated substitutes.'),
('Build a band photo wall','Find documented photographs for [bands]. Add one useful image per band with photographer, source, date or era if known, and license information where supplied. Distinguish performance lineup from recording lineup. Place images near relevant dossiers without implying that a later photo depicts the original album personnel.'),
('Give the note a consistent visual rhythm','Apply a consistent hierarchy of headings, short introductions, dividers, image captions, callouts, and navigation links. Keep the dark music theme readable and accessible. Reduce decorative clutter and repeated images while preserving artwork sources and all substantive content. Use supported Notion features and report any layout limitation.'),
('Make my listening profile visual','Use only my explicit feedback to create a visual profile of rhythm, atmosphere, guitar/bass weight, vocals, and hooks. Cite the reaction behind each observation. Do not invent numeric values. If comparative scores are missing, use qualitative labels such as stated preference, exploratory interest, and unknown, plus one useful question.'),
('Create a cover comparison panel','Build an artwork panel for [three albums], with matching-edition covers, credited sources, and short visual observations about composition, typography, color, and mood. Separate your visual interpretation from documented artist intent. Link each image to its dossier and source.'),
('Check image and navigation accessibility','Audit the note for missing captions, image sources, unclear link names, overlong callouts, and information expressed only by color. Improve the weak spots. Confirm which images and links were checked, and distinguish remote images from locally downloaded attachments.')]),
('History and scene atlas',[
('Expand a timeline decade','Expand [decade] in the history timeline with a manageable set of verified recordings, clubs, publications, or distribution milestones. Cite evidence and preserve date precision: year, month, exact day, or documented period. Explain links between events without inventing direct influence.'),
('Add context between milestones','Identify the largest narrative gap between existing timeline entries. Research it and add a short bridge explaining musical, scene, and industry changes with sources and two listening examples. Avoid turning an isolated release chronology into an unsupported complete history.'),
('Build a country scene dossier','Create a scene dossier for [country/city] with documented history, local artists, labels, clubs or events, recordings, and current discovery links. Distinguish verified scenes from leads. Include a compact location table and links back to existing albums; do not assume one national sound.'),
('Develop Chilean research','Expand the Chilean entry beyond the existing Puerto Montt lead. Find documented artists, releases, labels, and scene accounts from Chile, using Spanish-language sources where useful. Verify identities and locations. Keep broader Latin American comparisons separate and clearly label gaps in the evidence.'),
('Explain deathrock and its neighbors','Create a sourced comparison of deathrock, gothic rock, darkwave, coldwave, and darker punk/hardcore crossover. Compare musical cues and historical usage with album examples. Treat tags as leads, acknowledge contested boundaries, and explain album-specific changes rather than assigning every release by a band one genre.'),
('Document neglected contributions','Research women, LGBTQ+ musicians, and less-covered contributors relevant to [scene or era]. Use documented self-identification or responsible sources for personal identity. Focus on musical and scene contributions, add sourced recordings and timeline links, and avoid unsupported biographical assumptions.')]),
('Bandcamp and current releases',[
('Refresh this year’s discoveries','Research the actual current calendar year through today for gothic rock, deathrock, and separately labeled neighbors on Bandcamp. Add six verified full-length discoveries with exact release dates, artist/label links, cover sources, credits, and editorial listening questions. Sort released albums newest first; separate future releases, EPs, and reissues.'),
('Find raw underground deathrock','Find five underground Bandcamp recordings aligned with my stated interest in raw deathrock, catchy rhythm, and guitar/bass weight. Support genre and metadata with artist/label sources and attributed appraisal where available. Explain the match as a recommendation, not a claim of listening, and provide direct album links plus authentic covers.'),
('Explore a tag without trusting it blindly','Explore Bandcamp tags [tags] within [region or date range]. Verify each candidate beyond its tags using credits, artist descriptions, or responsible coverage. Separate strong matches, adjacent experiments, and unresolved candidates. Produce a short listening route with direct links and cover sources.'),
('Review the existing discovery list','Check each release in my Bandcamp section against its current official page. Verify date, format, edition, release status, links, and artwork. Record changed information with the check date; preserve earlier corrections when still supported. Move a preorder to released only after confirming the full release.'),
('Build a release watchlist','Create a watchlist of verified upcoming [style] releases. Include announced date, artist, title, format, label, direct Bandcamp page, cover source, and available preview status. Keep it separate from released-album recommendations and rankings. Add a manual next-check date without claiming an automatic alert exists.'),
('Guide my first Bandcamp session','Create a practical browsing route through three existing Bandcamp discoveries. Explain where to find credits, tracklist, edition information, label links, and available formats. Give one listening question for each album and a blank feedback template. Do not purchase, follow artists, or claim playback.')]),
('International labels and sources',[
('Expand the international label directory','Add [number] relevant labels from [countries] to the existing directory. Check for duplicates and verify each label’s Bandcamp page, official website, location, genre focus, and catalog examples. Separate headquarters from artist origins. Mark unknown or inaccessible information and date the checks.'),
('Create a label dossier','Create a dossier for [label] with verified country or city, official website, Bandcamp link, documented history, catalog scope, and three useful releases with direct links and covers. Attribute promotional descriptions and avoid treating a distributor or artist account as a label without evidence.'),
('Compare labels across countries','Compare [labels] by documented location, catalog focus, formats, artist roster, and discovery usefulness. Use representative recordings, not national stereotypes. Provide official and Bandcamp links side by side and explain which catalog to browse for raw deathrock, guitar-led goth, or atmospheric neighbors.'),
('Audit all label links','Check every Bandcamp and official-site link in the label directory. Verify that each account belongs to the named label, identify redirects and changed domains, and record the check date. Distinguish a site that cannot be read from a proven broken link. Preserve historical information when useful and label it.'),
('Expand research websites responsibly','Add [number] useful sources for gothic rock and related underground scenes, grouped into official catalogs, interviews/history, reviews, and discovery. Open each source, explain its scope and limitations, and include direct links plus a representative useful page. Keep editorial opinion separate from metadata authority.'),
('Resolve conflicting source claims','Investigate the disagreement about [date, lineup, genre, scene, or edition]. Compare opened primary sources and attributed independent accounts. Show what each supports, explain your conclusion and remaining uncertainty, and make a focused correction in the relevant dossier without erasing the provenance of the earlier claim.')]),
('Listening, maintenance, and Obsidian',[
('Create a useful journal entry','I listened to [artist — album — edition], [sample/full listen], on [date if known]. My feedback: [words]. Add an entry preserving my wording and supplied details. Leave missing fields blank. Link the dossier and recommend two close matches plus one contrast with verified recording links.'),
('Turn feedback into my next route','Read only my recorded reactions and build a three-album route based on what worked and what did not. Quote or paraphrase the feedback supporting each choice, verify albums and links, and explain one useful contrast. Keep recommendations separate from my personal rankings and unheard records.'),
('Make a qualitative comparison worksheet','Create a reusable worksheet for comparing [albums] on hooks, rhythm, voice, guitar/bass texture, atmosphere, and identity. Leave my response fields blank. Include source-backed context, edition links, and one question per dimension; do not fill in a simulated listening session.'),
('Prepare an Obsidian snapshot','Export the current note with linked album, scene, timeline, and journal content into an Obsidian-ready folder. Convert native Notion databases to linked notes and readable indexes, download images with credits, and preserve sources. Back up any overwritten notes, check wiki links and attachments, and label the copy as a dated snapshot without automatic synchronization.'),
('Compare Notion and my local copy','Compare the live Notion note with my dated Obsidian snapshot. Report additions, removals, source changes, and explicit listening feedback differences. Update [chosen destination] with a focused merge, preserving newer user edits and backing up affected files. Do not assume the two versions synchronize or silently replace one with the other.'),
('Finish a development session','Review what was actually changed in this session. Verify saved sections, cross-links, image sources, release status, and blank personal fields. Add a concise dated recap of completed work, remaining gaps, and three next actions. Distinguish saved results from proposed work and identify snapshots that now need refreshing.')])]
body=f'''---
tags: [music, goth-rock, prompts, notion]
created: 2026-10-09
---
# {NAME}

**42 ready-to-paste prompts** for developing your Goth Rock listening room. These extend the existing 15 project prompts; they are instructions for future work, not research results or completed changes.

[[Goth Rock — ChatGPT Project Prompts|General Goth Rock prompts]] · [[Music Prompt Library]] · [[Goth Rock — Start Here]]

## How to use

Copy one prompt, replace bracketed fields, and supply the current note or an accessible link. For Notion editing, paste it into a tool that can read and edit your page. In a research-only chat, ask for a paste-ready section with named targets. A local file or ChatGPT upload does not give access to the live Notion page.

Live page: [Goth Rock — Research and Listening](https://app.notion.com/p/3f4e10956af481718f92cc70d06d02d8). Local version: [[Goth Rock — Notion Snapshot 2026-10-09/Goth Rock — Research and Listening|Illustrated Obsidian snapshot]].

## Shared context to paste once

```text
Develop my existing Goth Rock research and listening note. Read its current content before editing and preserve my writing, sources, linked notes, and explicit preferences. Keep gothic rock central and label deathrock, darkwave, coldwave, ethereal wave, and punk/hardcore connections appropriately. My stated direction includes raw deathrock, dark atmosphere, catchy rhythm, guitar/bass weight, and distinctive sounds. Do not transfer preferences or listening history from other music projects.

For factual additions, browse and open sources, state the check date, and cite beside claims. Verify original dates separately from editions, and released records separately from preorders. Use authentic band photos and matching-edition cover art with sources and available credits. Never invent listening, personal scores, dates, biographies, links, or consensus. Keep fact, attributed opinion, editorial suggestions, and my actual feedback distinct.

If you can edit the live page, make the scoped update and read it back. If you lack access, provide paste-ready content and exact target sections without claiming it was saved. Preserve newer edits when refreshing snapshots. Notion, Obsidian, and ChatGPT uploads do not synchronize automatically.
```

## Choose a task

'''
for title,_ in groups:body+=f'- [[#{title}|{title}]]\n'
num=0
for title,items in groups:
 body+=f'\n## {title}\n\n'
 for heading,prompt in items:
  num+=1;body+=f'### {num:02d}. {heading}\n\n```text\n{prompt}\n```\n\n'
assert num==42
(ROOT/(NAME+'.md')).write_text(body)
paths=[Path('Music Prompts/Goth Rock — ChatGPT Project Prompts.md'),Path('Music Prompts/Music Prompt Library.md'),Path('Goth Rock — Start Here.md'),Path('Goth Rock — Notion Snapshot 2026-10-09/Goth Rock — Research and Listening.md')]
manifest=[]
for i,path in enumerate(paths):
 current=(VAULT/path).read_text(); backup=ROOT/f'before-{i}.md';backup.write_text(current)
 addition=f'\n## Prompts for developing the Notion note\n\n[[{NAME}|42 development prompts]] — album dossiers, artwork, visual layout, history, scenes, Bandcamp releases, international labels, listening feedback, and Obsidian snapshots.\n'
 (ROOT/f'after-{i}.md').write_text(current.rstrip()+'\n'+addition)
 manifest.append({'path':str(path),'before':backup.name,'after':f'after-{i}.md'})
(ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Prepared 42 prompts in seven sections; four existing notes staged with focused links.')
