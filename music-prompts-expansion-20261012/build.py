from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).parent
VAULT = Path('/home/ivanaguilera/Documents/Obsidian Vault')
TOPICS = ['Death Metal', 'Black Metal', 'Heavy Metal', 'Goth Rock', 'Hardcore & Punk']

FOCUS = {
    'Death Metal': 'riff construction, rhythmic changes, growls, groove, dissonance, arrangement, and production',
    'Black Metal': 'tremolo patterns, repetition, harmony, drum feel, vocal texture, atmosphere, and production',
    'Heavy Metal': 'riff and hook construction, vocal phrasing, guitar harmony, bass movement, solos, and arrangement',
    'Goth Rock': 'bass movement, guitar texture, live drums or drum machines, vocal character, melody, and atmosphere',
    'Hardcore & Punk': 'pace, riff economy, hooks, vocal delivery, rhythm, arrangement, and production',
}
BOUNDARY = {
    'Death Metal': 'Keep death metal central and label deathgrind, deathcore, black/death, and other neighboring or hybrid recordings explicitly.',
    'Black Metal': 'Keep black metal central; distinguish sonic styles from production descriptors, lyrical themes, and ideology. Never infer affiliations from imagery or association.',
    'Heavy Metal': 'Default to traditional heavy metal; label speed, doom, power, progressive, and other neighboring or hybrid recordings explicitly.',
    'Goth Rock': 'Keep gothic rock central; label deathrock, darkwave, coldwave, ethereal wave, industrial/EBM, and gothic metal according to the actual recording.',
    'Hardcore & Punk': 'Keep punk rock and hardcore punk central. Label related explorations and include crossover thrash, metallic hardcore, metalcore, or grindcore only when I request them. Preserve EP, single, demo, and split identities.',
}

SPECIAL = {
    'Death Metal': [
        ('Trace a riff language across scenes', 'Research [riff approach, such as Swedish-style buzzsaw riffs, Finnish atmosphere, or New York groove] through three contrasting recordings. Explain what the description refers to, how composition differs from guitar tone, and where regional shorthand becomes misleading. Verify original years and recording credits; distinguish documented influence from sonic resemblance. End with a compact comparison and one question to use while listening.'),
        ('Demos, tape trading, and the first album', 'Follow [band] from its earliest documented demos to [debut album]. Verify recording dates separately from release dates, track reuse, lineup changes, labels, and distribution where evidence exists. Explain what changed in composition and presentation using sources. Do not treat an archival compilation date as the original demo year. Choose a three-recording route and mark unavailable originals or uncertain chronology.'),
        ('Complexity versus groove', 'Build a three-album Death Metal study around [complexity, groove, or their interaction]. Compare rhythmic organization, recurring motifs, song length, transitions, and space for memorable riffs. Label technical, progressive, brutal, and slam descriptions when supported rather than treating them as interchangeable. Explain why difficulty and speed alone do not determine musical appeal. Offer listening questions without inventing time signatures or timestamps.'),
        ('Explore a studio or producer network', 'Research [studio, producer, or engineer] through three Death Metal albums by different artists. Verify the person’s exact role on each edition. Separate recording, mixing, mastering, musicianship, and later remastering. Explain documented working methods through interviews and credits; attribute sonic assessments to reviews or my feedback. Identify contrasts instead of assigning every album one house sound.'),
        ('Death-doom, deathgrind, and blackened borders', 'Investigate [one boundary: death-doom, deathgrind, or black/death] using two central examples and one disputed recording. Explain riffs, rhythm, vocals, atmosphere, and album-specific classification. Compare responsible accounts, state what remains contested, and separate musical resemblance from documented influence. Keep this exploration within the Death Metal project and do not import personal preferences from other projects.'),
    ],
    'Black Metal': [
        ('Atmosphere through composition', 'Research how [repetition, melody, drones, keyboards, or long-form arrangement] creates atmosphere in Black Metal. Choose three contrasting recordings and explain the compositional mechanisms in accessible language. Distinguish raw recording from deliberate repetition and atmospheric descriptors from formal subgenres. Attribute analysis, verify credits and original years, and give one concrete listening question per album without inventing timestamps.'),
        ('International histories beyond one center', 'Investigate [two regions outside Norway] during [period]. Build a short parallel chronology with verified recordings, labels, distribution networks, and participant accounts. Distinguish documented contact or influence from developments that merely resemble one another. Explain evidence gaps and local variation rather than treating either country as a uniform sound. Recommend three recordings that clarify the comparison.'),
        ('One-person projects and collaboration', 'Research [solo project or a small set of one-person Black Metal projects]. Verify which instruments, compositions, vocals, production tasks, and artwork were actually handled by whom on the selected recordings. Distinguish a solo identity from guest contributions and live lineups. Explain documented creative choices without romanticizing isolation or inventing biography. Choose an entry album and a contrasting later release.'),
        ('Ambient interludes and dungeon synth neighbors', 'Explore the relationship between [Black Metal artist or scene] and ambient music or dungeon synth. Distinguish interludes within metal albums, separate non-metal releases, and later scene labels. Use verified dates and artist statements for influence claims. Compare three recordings with practical listening questions, keep neighboring formats clear, and exclude non-metal releases from a core Black Metal album ranking unless I explicitly broaden it.'),
        ('Test a disputed historical claim', 'Investigate the claim [specific claim about a Black Metal origin, influence, recording, or scene event]. Locate the earliest accessible evidence, compare participant accounts and later retellings, and separate documented events from allegations, promotional language, and mythology. State source limits and unresolved disagreements. Avoid reducing musical history to controversy; finish with the implications for this project’s history note and a sourced replacement paragraph.'),
    ],
    'Heavy Metal': [
        ('Twin guitars and the rhythm section', 'Build a three-recording traditional Heavy Metal study of [guitar harmony, lead exchanges, bass-led movement, or drum feel]. Explain how the chosen element supports songs rather than listing virtuoso moments. Verify players and original releases; use attributed musical analysis and my feedback. Offer practical listening questions and identify contrasting approaches without inventing harmony intervals or transcriptions.'),
        ('Epic songs and concise anthems', 'Compare [long-form album or song] with [concise album or song] within traditional Heavy Metal. Explain arrangement, recurring motifs, vocal hooks, narrative pacing, and how each sustains attention. Verify exact versions and lyrical context. Separate epic as a descriptive approach from disputed genre labels. Recommend one further contrast and avoid assuming that longer songs are more ambitious or better.'),
        ('Singles, independent labels, and NWOBHM', 'Research [local NWOBHM scene, label, or band] through its original singles, demos, EPs, and first full-length. Verify dates, formats, credits, and documented distribution or compilation appearances. Distinguish original releases from later collections and older influences from movement participants. Build a short chronology and three-recording route; do not classify every contemporary British hard rock or metal band as NWOBHM.'),
        ('Traditional metal across languages', 'Explore traditional Heavy Metal sung in [language or region]. Research three contrasting artists through exact recordings, verified original years, and sourced local context. Discuss vocal phrasing and verified lyrical themes without treating language as a musical genre or assuming artists share one politics. Label neighboring styles, give official listening links or searches, and summarize lyrics rather than reproducing or inventing them.'),
        ('Revival and reinterpretation', 'Compare [older traditional Heavy Metal recording] with [modern recording]. Research the newer artist’s documented influences, then distinguish homage, shared vocabulary, and original choices in composition, performance, and production. Use reviews as attributed opinions rather than declaring an artist derivative from visual styling. Verify original dates and editions, explain the strongest reason to try each, and keep personal favorites separate from historical importance.'),
    ],
    'Goth Rock': [
        ('Bass, guitar, and rhythm in three records', 'Build a three-recording gothic rock study around [bass-led songs, guitar texture, or drum machines versus live drums]. Verify personnel and equipment claims from credits or interviews. Explain how rhythm and texture shape the songs through cited analysis and my reactions; do not infer a drum machine from sound alone. Label neighboring styles and provide concrete listening questions without invented timestamps.'),
        ('Club culture and recorded sound', 'Research [club, city, or documented goth scene] during [period]. Separate venue history, DJ programming, audiences, press labels, and the music artists actually released. Use archives and participant accounts with dates and limitations. Recommend three recordings relevant to the evidence without assuming everyone associated with a club played gothic rock. Explain how the scene changed and what remains unresolved.'),
        ('Deathrock and darkwave through contrasts', 'Help me distinguish [gothic rock, deathrock, darkwave, or coldwave] using three carefully chosen recordings. Compare bass and guitar roles, rhythm, electronics, vocal delivery, and arrangement rather than imagery alone. Explain regional and historical differences in terminology, attribute disputed classifications, and identify hybrids. End with listening questions and a core gothic rock alternative if the route moves into neighboring styles.'),
        ('Literature, cinema, and visual references', 'Investigate [Goth Rock artist or album] and its documented references to literature, cinema, photography, or visual art. Separate confirmed references from my suggested resemblance [optional observation]. Verify artwork and video credits, connect the references to sourced lyrical or compositional context, and preserve artist statements. Link original material where accessible without inventing influence, quoting full lyrics, or claiming research sources were watched or read in full.'),
        ('Develop the existing 1980s album archive', 'Read this project’s existing Top 30 albums of the 1980s if that note is accessible; otherwise ask me for the relevant excerpt. Audit [selected entries or a chosen year] for exact identity, original release year, edition, genre eligibility, evidence, and explanation of placement. Research up to three overlooked alternatives. Propose focused revisions with reasons, preserving the published/editorial/personal distinction and all unreported personal fields. Provide Markdown for the named rankings note without assuming the uploaded copy matches live Obsidian.'),
    ],
    'Hardcore & Punk': [
        ('A short release as a complete statement', 'Develop a focused dossier for [EP, single, demo, or split] in Hardcore & Punk. Verify original format, release year, track order, credits, and later compilation appearances. For a split, credit all artists and specify whether studying both sides or one. Explain structure and context without treating brevity as incompleteness. Prepare three listening questions and label the release separately from studio-album rankings.'),
        ('Zines and oral history as evidence', 'Investigate [punk/hardcore scene or event] using accessible contemporary zines, interviews, flyers, and later oral histories. Give each source’s author, date, perspective, and limitations. Compare disagreements without forcing consensus, distinguish a later memory from contemporary documentation, and verify recording identities independently. Draft a connected scene paragraph with citations and a short list of research gaps.'),
        ('D-beat, crust, and anarcho-punk', 'Explore [one or more of D-beat, crust, and anarcho-punk] through three contrasting recordings. Distinguish rhythmic description, musical approach, scene affiliation, and political tradition. Explain overlap and disputed labels through sourced context and practical cues. Verify original years and formats, include short releases where useful, and avoid assuming every artist shares one ideology, aesthetic, or production method.'),
        ('All-ages spaces and local networks', 'Research [city/region] punk and hardcore through documented all-ages spaces, independent labels, promoters, zines, and distribution during [period]. Connect each supported network claim to a recording or participant source where possible. Distinguish past venues from current activity and verify changing facts as of the research date. Explain local differences and gaps; do not contact anyone or treat a scene survey as a current events calendar.'),
        ('Melody, abrasion, and heavier boundaries', 'Build a three-recording route between [two punk/hardcore approaches I choose]. Compare hooks, pace, vocal delivery, riff construction, and arrangement. Label post-hardcore, emo, skate punk, or other related explorations explicitly. Include metallic hardcore, crossover thrash, metalcore, or grindcore only if my chosen scope requests them. Verify original formats and years, explain transitions, and keep short releases distinct from albums.'),
    ],
}

def prompts(topic):
    focus, boundary = FOCUS[topic], BOUNDARY[topic]
    common = [
        ('Build a full recording dossier', f'Develop a sourced dossier for [artist / recording / edition] in my {topic} project. Verify exact title, original date, format, track order, personnel, label, recording/mixing/mastering credits, and edition differences. Explain composition and context with attention to {focus}. Separate artist statements, attributed criticism, editorial interpretation, and my supplied reaction [optional feedback]. Include three listening questions, verified official links or labeled searches, and unresolved metadata. Do not claim direct listening or fill personal scores. {boundary}'),
        ('Choose a route through one discography', f'Build a manageable listening route through [artist] for my {topic} project. Verify original releases and identify meaningful changes in personnel, composition, or presentation. Choose three entry recordings for [goal or sound], explain why each belongs, and list two later branches to explore. Distinguish chronological order from the recommended route; label demos, EPs, live recordings, compilations, and reissues. {boundary} Use this project’s explicit feedback only and leave listening status unknown unless I reported it.'),
        ('Prepare a track-by-track listening companion', f'Create a listening companion for [artist / recording / exact edition]. Verify the original track order and separate bonus tracks. For each original track give one short question about {focus}, based on sourced analysis or my notes [optional notes]. Identify track-specific statements as documented or interpretive. If evidence supports only album-level discussion, give album-level questions instead of invented song details. Do not fabricate timestamps, transcriptions, direct listening, or my reactions. Finish with a blank three-question feedback form.'),
        ('Artwork, credits, and edition identity', f'Research the artwork and presentation of [artist / recording] in my {topic} project. Verify the original cover, credited artist or photographer, design, and documented later variants. Explain confirmed artistic intent separately from visual interpretation; preserve conflicting or unavailable credits. Link responsible image sources without treating a product thumbnail as evidence of an edition’s contents. Compare original, remastered, remixed, or expanded versions where relevant; do not infer audio quality from format, price, or cover art. Produce a short illustrated-note plan, without claiming images were downloaded or attached.'),
        ('Use my feedback to choose the next experiment', f'Read only the feedback I explicitly supplied in this {topic} project, including [optional new reaction]. Extract tentative preferences about {focus}; distinguish repeated evidence from one-off impressions and do not infer preferences from research lists. Choose two close matches and one deliberate contrast, explaining which preference each tests. Verify recording identities, original years, formats, and official links. {boundary} Avoid repeating reported listens unless I ask for a revisit, leave unheard scores blank, and finish with one useful question for my next feedback.'),
    ]
    return common + SPECIAL[topic]

manifest = []

def stage(relative, transform):
    source = VAULT / relative
    original = source.read_text()
    updated = transform(original)
    assert original != updated, relative
    backup = ROOT / 'backup' / relative
    output = ROOT / 'staged' / relative
    backup.parent.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, backup)
    output.write_text(updated)
    manifest.append({'relative': relative, 'before_sha256': hashlib.sha256(original.encode()).hexdigest(), 'after_sha256': hashlib.sha256(updated.encode()).hexdigest()})

for topic in TOPICS:
    def expand(s, topic=topic):
        assert len(re.findall(r'^## \d+\.', s, re.M)) == 15
        section = '\n## Deeper research and listening — prompts 16–25\n\nAdded 12 October 2026. Copy one prompt into this topic’s project and replace bracketed fields. Apply the existing research add-on when researching facts. These extend the original 15 prompts.\n'
        for number, (title, body) in enumerate(prompts(topic), 16):
            section += f'\n## {number}. {title}\n\n```text\n{body}\n```\n'
        updated = s.rstrip() + '\n' + section
        assert len(re.findall(r'^## \d+\.', updated, re.M)) == 25
        assert updated.count('```') % 2 == 0
        return updated
    stage(f'Music Prompts/{topic} — ChatGPT Project Prompts.md', expand)

    def dashboard(s, topic=topic):
        s = s.replace(f'[[{topic} — ChatGPT Project Prompts]]: 15 reusable prompts.', f'[[{topic} — ChatGPT Project Prompts]]: 25 reusable prompts.')
        s = s.replace(f'[[{topic} — ChatGPT Project Prompts|15 research and listening prompts]]', f'[[{topic} — ChatGPT Project Prompts|25 research and listening prompts]]')
        return s.rstrip() + f'\n\n## Expanded project prompts — 12 October 2026\n\n[[{topic} — ChatGPT Project Prompts#Deeper research and listening — prompts 16–25|Ten new research and listening prompts]] extend this project’s library to **25 prompts**. Start with a recording dossier (16), a discography route (17), a track-by-track companion (18), artwork and edition research (19), or feedback-based discovery (20); prompts 21–25 focus on this topic’s scenes and musical questions. The existing ChatGPT upload packs remain older snapshots. Copy the prompts from the live note or replace the uploaded prompt snapshot manually.\n'
    stage(f'{topic} — Start Here.md', dashboard)

def library(s):
    for topic in TOPICS:
        s = s.replace(f'[[{topic} — ChatGPT Project Prompts|15 project prompts]]', f'[[{topic} — ChatGPT Project Prompts|25 project prompts]]')
    return s.rstrip() + '''

## Expanded project prompts — 12 October 2026

Added **50 prompts**, ten to each of the five existing genre projects. Each topic now has **25 project prompts**. Keep these in the matching project so its scope, journal, and preferences stay separate.

| Goal | Prompt in each topic library |
| --- | --- |
| Develop one recording thoroughly | 16 — recording dossier |
| Explore an artist without starting with every release | 17 — discography route |
| Prepare questions for a focused listen | 18 — track-by-track companion |
| Investigate covers, credits, and versions | 19 — artwork and edition identity |
| Choose the next listen from actual feedback | 20 — two close matches and one experiment |
| Study topic-specific musical and historical questions | 21–25 — five prompts tailored to each genre |

### Topic-specific choices

- [[Death Metal — ChatGPT Project Prompts#21. Trace a riff language across scenes|Death Metal]] — riff languages; demos and tape trading; complexity and groove; studio networks; death-doom, deathgrind, and blackened borders.
- [[Black Metal — ChatGPT Project Prompts#21. Atmosphere through composition|Black Metal]] — atmosphere; international parallel histories; one-person projects; ambient/dungeon synth neighbors; disputed historical claims.
- [[Heavy Metal — ChatGPT Project Prompts#21. Twin guitars and the rhythm section|Heavy Metal]] — guitar and rhythm interplay; epics and anthems; NWOBHM short releases; language and local context; revival and reinterpretation.
- [[Goth Rock — ChatGPT Project Prompts#21. Bass, guitar, and rhythm in three records|Goth Rock]] — bass/guitar/rhythm; club culture; deathrock/darkwave contrasts; literature and cinema; the existing 1980s ranking archive.
- [[Hardcore & Punk — ChatGPT Project Prompts#21. A short release as a complete statement|Hardcore & Punk]] — short-release dossiers; zines and oral history; D-beat/crust/anarcho-punk; all-ages spaces; melody and heavier boundaries.

Use the recording dossier for depth, the discography route for discovery, or the feedback prompt after a listen. These prompts request research when run; adding them does not perform that research, change listening history, or update ChatGPT uploads. The original prompts, project instructions, Spotify library, and Goth Rock development library remain available.
'''

stage('Music Prompts/Music Prompt Library.md', library)
(ROOT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'README.md').write_text('# Music prompt expansion — 12 October 2026\n\nPrepared 50 new prompts across five existing topic libraries, numbered 16–25. Updated the shared index and each dashboard. Original instructions and existing 1–15 prompts are preserved. Backups and staged files retain vault-relative paths. ChatGPT upload packs were not changed.\n\nNext: choose a prompt in the matching music project; copy it from the live note or refresh its uploaded prompt snapshot. No new listening preferences or scores were recorded.\n')
print(f'Staged {len(manifest)} files; 50 new prompts; backups complete.')
