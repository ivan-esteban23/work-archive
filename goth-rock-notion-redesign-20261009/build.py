from pathlib import Path
import json
root=Path(__file__).parent
images=json.loads((root/'images.json').read_text())
images['https://beggarsbanquetrecords.com/bauhaus-in-the-flat-field/']='https://s3.eu-west-1.amazonaws.com/cf-cdn.beggars.com/beggars_archive/wp-content/uploads/2018/09/17130509/CAD2901LPX-Bauhaus-4000.jpg'
LA='https://www.laweekly.com/the-la-deathrock-starter-guide/'
BAT='https://post-punk.com/young-limbs-rise-again-the-story-of-the-batcave-nightclub-1982-1985-compilation-and-book-zeroes-in-on-goths-formative-lair-the-batcave/'
CHILE='https://post-punk.com/chilean-gothic-rockers-a-traves-del-manto-unveil-their-macabre-video-for-xmal-funeral/'
KFK='https://kommunityfk.wixsite.com/kommunityfk/discography'
CIN='https://lucaslanthier.bandcamp.com/album/album-the-astonished-eyes-of-evening'
SIS='https://www.guitarworld.com/artists/guitarists/the-making-of-the-sisters-of-mercy-first-and-last-and-always'
rows=[]
def album(title,artist,year,style,shelf,entry,listen,image,edition,why,facts,route,compare,gaps):
 props={'Album':title,'Artist':artist,'Original year':year,'Style':json.dumps(style),'Shelf':shelf,'Listening status':'Unknown','Edition':edition,'Entry track':entry,'Listen':listen,'Order':len(rows)+1}
 content=(f'![{artist} — {title}. Artwork from the linked edition.]({image})\n' if image else '')
 content+=f'''<callout icon="🎧" color="purple_bg">
	**{artist} · {year}**
	{shelf} · {', '.join(style)}
</callout>
## Why this belongs here
{why}
## Recording dossier
{facts}
## Edition to use
{edition}
[Listening / catalog route]({listen})
## Three listening doors
'''
 for track,prompt in route:content+=f'- **{track}** — {prompt}\n'
 content+=f'''## Compare with your reference shelf
{compare}
## Your response
Leave this section blank until you report a listen. Add a session in the main Listening journal and link this album. Record the exact edition, sample/full listen, one memorable moment, and your own words. Scores are optional.
## Research still open
{gaps}
Metadata checked <mention-date start="2026-10-09"/>. The listening questions are editorial suggestions, not a claim of direct audio evaluation. Artwork identifies the linked edition; no ownership or reuse license is claimed.
'''
 row={'properties':props,'icon':'💿','content':content}
 if image:row['cover']=image
 rows.append(row)
album('Sleep in Safety','45 Grave',1983,['Deathrock'],'Next listens','Evil','https://music.apple.com/us/album/sleep-in-safety/162551605','https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/7e/f8/f0/7ef8f095-fd96-fe80-861b-48fa9410c94a/mzi.xbzrsdvi.jpg/600x600bf-60.jpg','Expanded Apple Music edition; original album year 1983. Keep bonus material identifiable.',
'Test your preference for sinister atmosphere and rhythmic grip through a different reference from your named Christian Death and Super Heroines interests. Prior listening is unknown.',
f'Apple Music identifies the 1983 release and describes horror-punk and harder-rock overlaps; its evaluation is platform editorial opinion. [Catalog metadata](https://music.apple.com/us/album/sleep-in-safety/162551605).\nDinah Cancer, drummer Don Bolles, and keyboardist Paul Roessler appear in the scene account. This does not establish a complete track-by-track personnel sheet. [Liz Ohanesian, LA Weekly, 2009]({LA}).',
[('Evil','Follow the voice, then the rhythmic accents. What holds your attention?'),('Partytime','Test how much a recurring refrain contributes to catchiness.'),('Surf Bat','Compare your reaction to a change in musical character.')],
'Compare the kind of darkness with Pornography: vocal character, guitar attack, and recurring rhythmic figures. Test each dimension separately rather than judging everything by loudness.',
'Verify original sequencing, complete recording credits, and lyrics through responsible sources. January 1 in platform metadata is not treated as a secure original release day.')
album('The Vision and the Voice','Kommunity FK',1983,['Deathrock','Post-punk'],'Next listens','Choose an original-album track from the confirmed edition','https://kommunityfk.bandcamp.com/album/vision-and-the-voice','https://f4.bcbits.com/img/a1424168393_5.jpg','Original vinyl: Independent Project, 1983. Pictured catalog: official 2006 CD reissue with bonus live material.',
'Test repetition, abrasion, and distinctive identity against your Voodoo Church and Christian Death interests. The aim is to discover whether rough texture adds tension for you.',
f'The official discography lists the 1983 vinyl and later CD/digital editions. [Band discography]({KFK}). LA Weekly places the band in the early Los Angeles deathrock context. [Scene account]({LA}).',
[('Original-album selection','Choose a track confirmed on the original sequence; follow one repeating instrumental figure.'),('A second original-album selection','Compare guitar texture and the amount of empty space.'),('Live bonus comparison, optional','Label it as bonus/live material and compare performance texture separately.')],
'Place one original-album sample after Evil by 45 Grave. Which matters more to your reaction: immediate rhythmic grip, guitar texture, or vocal character?',
'The catalog could not be read through the web research tool on this pass; artwork metadata was retrieved from its public page. Original tracklist, personnel, and playable full-album access need verification. Do not substitute Something Inside Me Has Died: the official discography connects it with other releases, and LA Weekly identifies Close One Sad Eye (1985).')
album('The Astonished Eyes of Evening','Cinema Strange',2002,['Deathrock'],'Next listens','Dead Eyes Open',CIN,'https://f4.bcbits.com/img/a2476914284_5.jpg','2002 original year; linked member catalog identifies the second Trisol CD. Exact original day remains unverified.',
'Test theatricality alongside weight. Your Virgin Prunes and Sex Gang Children interests support this experiment, without assuming you already know the record.',
f'Credits identify Lucas Lanthier on voices, Michael Ribiat on guitar, and Daniel Ribiat on bass, with programming and other instruments. Ashkelon Sain and the band produced it; recording is listed mainly in 2001. Legs and Tarpaulin draws on Poe’s King Pest. [Member catalog and credits]({CIN}).',
[('Dead Eyes Open','Follow shifts in vocal character and their relationship with the instrumental pattern.'),('Legs and Tarpaulin','Compare the narrative delivery with the hook you remember afterward.'),('Catacomb Kittens','Test whether a longer song sustains your interest through arrangement.')],
'Compare voice and theatrical phrasing with the artists you named, then contrast it with 45 Grave. A sound comparison does not prove a documented influence.',
'Add independent album criticism and verify original release-day evidence. Separate the catalog’s second-CD description from its first-full-length-recording-project description.')
album('Pornography','The Cure',1982,['Gothic rock','Post-punk'],'Stated favorite','One Hundred Years','https://www.thecure.com/release/pornography/','https://www.thecure.com/wp-content/uploads/sites/10452/2018/01/pornography.jpg','Original eight-track sequence first; 2005 deluxe material separately. Preserve the earlier official-page conflict between May 3 and May 4.',
'You explicitly named this album as a favorite. Use it to explain what “dark,” “heavy,” and “catchy” mean to you rather than treating it as an unheard recommendation.',
'Official credits name Phil Thornalley and The Cure as producers and RAK Studios in London as the recording location. [Official album page](https://www.thecure.com/release/pornography/).',
[('One Hundred Years','Identify the strongest source of tension for you.'),('The Hanging Garden','Describe the rhythmic element you return to.'),('The Figurehead','Compare vocal presence, texture, and sustained atmosphere.')],
'Use the same three questions for a deathrock sample: what grips rhythmically, where weight comes from, and which sound feels distinctive.',
'Your exact edition, favorite tracks, listening date, and score remain unreported. A stated favorite does not create a dated session.')
album('Disintegration','The Cure',1989,['Gothic rock'],'Stated favorite','Plainsong','https://www.thecure.com/release/disintegration/','https://www.thecure.com/wp-content/uploads/sites/10452/2018/01/Disintegration-1024x1024.jpg','1989 original year; 2010 deluxe release separately. Record your chosen format/edition; the official page provides a twelve-track sequence.',
'Your other explicit Cure album favorite. Use it as a reference for atmosphere, melody, and how much time you want a song to take.',
'Official credits name David M. Allen and Robert Smith as producers and Hookend Recording Studios as the recording location. [Official album page](https://www.thecure.com/release/disintegration/).',
[('Plainsong','Describe the sense of space and the role of the voice.'),('Fascination Street','Identify the repeating element that supplies rhythmic grip.'),('The Same Deep Water as You','Test how duration affects immersion for you.')],
'Compare your reactions with Pornography, then with Lycia’s Cold. Your personal description will be more useful than a presumed darkness score.',
'Favorite moments, exact edition, dated session, and any personal rating still need your feedback.')
album('Only Theatre of Pain','Christian Death',1982,['Deathrock'],'Historical reference','Cavity — First Communion','https://frontierrecords-christiandeath.bandcamp.com/album/only-theatre-of-pain-original','https://f4.bcbits.com/img/a3077196191_5.jpg','Frontier original-version listing; tracks 1–10 are the album, followed by Deathwish EP material. Distinct from the 2011 remaster.',
'You like Christian Death at artist level. This specific record remains a historical comparison, not a confirmed album favorite.',
'The label dates the recording to 1982 and explicitly separates the original-version listing from the later remaster. [Frontier catalog](https://frontierrecords-christiandeath.bandcamp.com/album/only-theatre-of-pain-original).',
[('Cavity — First Communion','Follow the relationship between guitar and vocal delivery.'),('Figurative Theatre','Identify which repeated gesture feels memorable.'),('Spiritual Cramp','Compare rhythmic drive with the current deathrock picks.')],
'Use it as one reference for the 1983 records without assuming the Los Angeles artists share one arrangement style.',
'Complete original credits, attributed lyrical analysis, and your album-specific reaction remain open.')
album('In the Flat Field','Bauhaus',1980,['Gothic rock','Post-punk'],'Historical reference','Double Dare','https://beggarsbanquetrecords.com/bauhaus-in-the-flat-field/',images['https://beggarsbanquetrecords.com/bauhaus-in-the-flat-field/'],'1980 debut; linked label catalog and pictured catalog sleeve. Exact-day conflicts noted in the original research remain open.',
'An earlier onboarding reference for guitar space, tension, and vocal character. Prior listening remains unknown.',
'The label identifies the debut, 4AD, original year 1980, and the original nine-track sequence. [Beggars catalog](https://beggarsbanquetrecords.com/bauhaus-in-the-flat-field/). Its historical evaluation is a label framing, not an objective ranking.',
[('Double Dare','Follow voice versus guitar space.'),('In the Flat Field','Identify the musical gesture you remember afterward.'),('Stigmata Martyr','Compare repetition with the other two selections.')],
'Compare a track with Cinema Strange on vocal character and rhythmic interest. Keep sound-based parallels separate from sourced influences.',
'Further original recording credits and independent historical accounts would deepen this dossier.')
album('Cold','Lycia',1996,['Darkwave','Ethereal / atmospheric'],'Atmospheric detour','Frozen','https://lycia.bandcamp.com/album/cold',images['https://lycia.bandcamp.com/album/cold'],'1996 original year; artist page offers remastered audio. Record the version used in your journal.',
'The earlier contrasting experiment tests whether your Cocteau Twins and Dead Can Dance interests extend to this atmospheric direction. It does not replace your raw-deathrock priority.',
'The artist credits David Galas, Tara Vanflower, and Mike VanPortfleet, with vocals, guitars, synths, bass, and drum programming; recording is listed in early 1996. [Artist catalog](https://lycia.bandcamp.com/album/cold).',
[('Frozen','Compare patience and atmosphere with immediate rhythmic attack.'),('Bare','Describe which layer holds your attention.'),('Drifting','Compare vocal appeal with the other two tracks.')],
'Contrast one track with Disintegration and one with 45 Grave. Does heaviness need sharp attack, or can sustained texture supply what you enjoy?',
'Your response and independent criticism remain open. Neighboring-style tags do not automatically grant core gothic-rock ranking eligibility.')
album('Talk About the Weather','Red Lorry Yellow Lorry',1985,['Post-punk','Gothic rock'],'Historical reference','Talk About the Weather','https://music.apple.com/us/album/talk-about-the-weather/277761688',images['https://music.apple.com/us/album/talk-about-the-weather/277761688'] .replace('1200x630wp-60','600x600bf-60'),'Expanded platform edition; original year 1985. Artist rejects the goth tag according to the artist/label biography.',
'The earlier close-match proposal tests your Play Dead and Sisters of Mercy interests through rhythm and guitar weight. This stays an optional comparison while raw deathrock leads.',
'The artist/label biography confirms 1985 and describes early bass/guitar/percussion approaches while noting rejection of the goth label. [Biography](https://redlorryyellowlorry.bandcamp.com/album/driving-black). [Album edition](https://music.apple.com/us/album/talk-about-the-weather/277761688).',
[('Talk About the Weather','Follow the repeating figure and vocal delivery.'),('Original-sequence contrast','Choose a second track after checking the edition’s album/bonus boundary.'),('Album return','Try the opening again after the contrast and describe what changes for you.')],
'Compare rhythm and guitar texture with the Sisters reference, without treating the artist’s preferred identity as settled by audience tags.',
'Original sequencing, recording credits, and additional track choices need closer edition work.')
album('Selected Scenes from the End of the World','London After Midnight',1991,['Gothic rock','Darkwave'],'Historical reference','Spider and the Fly','https://lamofficial.bandcamp.com/album/selected-scenes-from-the-end-of-the-world-9119',images['https://lamofficial.bandcamp.com/album/selected-scenes-from-the-end-of-the-world-9119'],'Artist-supplied original year 1991; linked 9119 remix/remaster released in 2019, with bonus recordings.',
'The earlier mixed batch proposed this as a theatrical, hook-focused comparison with your Angels of Liberty and Sisters of Mercy interests. Prior listening is unknown.',
'The artist identifies the original 1991 album and the 2019 remix/remaster. The linked edition credits Sean Brennan for writing, performance, and production. [Artist catalog](https://lamofficial.bandcamp.com/album/selected-scenes-from-the-end-of-the-world-9119).',
[('Spider and the Fly (9119)','Compare vocal drama with the repeating instrumental pattern.'),('Sacrifice (9119)','Describe the balance between melody and atmosphere.'),('This Paradise (9119)','Test which element supplies the hook for you.')],
'Compare the theatrical appeal with Cinema Strange; use exact versions so remix changes do not become presumed differences between original albums.',
'Broader date/edition comparison and original personnel remain research tasks. Tags spanning industrial and darkwave do not settle album-wide classification.')
album('First and Last and Always','The Sisters of Mercy',1985,['Gothic rock'],'Historical reference','Marian',SIS,None,'Original year 1985; exact edition not selected. Your “first two records” remains unresolved and this is not automatically marked as a favorite.',
'Preserve the earlier onboarding reference while waiting for your exact title pair. Artist familiarity does not establish a specific edition or dated listen.',
f'A recording interview with Gary Marx and Wayne Hussey discusses complementary guitar parts and recording choices and supports the 1985 year. Participant recollections and journalist evaluation are different evidence. [Guitar World interview]({SIS}).',
[('Marian','Compare complementary guitar parts and vocal character.'),('No Time to Cry','Identify the most memorable rhythmic or melodic element.'),('First and Last and Always','Compare the title track’s pull with the previous selections.')],
'Compare the specific qualities you enjoy with Red Lorry Yellow Lorry and the deathrock picks rather than assuming one whole genre preference.',
'Confirm which two records you meant; choose a direct album listening edition and add original credits. Cover remains unset until a responsible album-art source is added.')
(root/'albums.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
scenes=[
('Los Angeles — deathrock roots','North America','Punk attack, theatricality, and different early recording approaches','Source-backed overview',LA,
 f'LA Weekly’s 2009 account places Christian Death, 45 Grave, and Kommunity FK within the local deathrock story. [Scene account]({LA}).',
 ['Only Theatre of Pain — Christian Death','Sleep in Safety — 45 Grave','The Vision and the Voice — Kommunity FK'],
 'Compare the three dossiers through rhythm, guitar texture, and voice. A shared scene does not establish one uniform sound.',
 'The account names later club nights, but these are historical 2009 references, not verified current events. Research early venues, original flyers, labels, women’s contributions, and participant accounts next.'),
('London — Batcave connections','Europe','Club culture, theatrical performance, and a varied listening community','Source-backed overview',BAT,
 f'Andi Harriman’s 2023 feature discusses the 1982–1985 Batcave compilation and book, club repertoire, performances, and archival imagery. It is a retrospective tied to a reissue. [Feature]({BAT}).',
 ['Specimen — artist already named by you; select and verify a recording','Sex Gang Children — artist already named by you; select and verify a recording','Cinema Strange — comparison route, not a London-origin claim'],
 'Compare vocal character and arrangement with the Los Angeles records. Batcave is a club/scene reference; its broad repertoire is not a universal subgenre definition.',
 'Verify original venue chronology, credits for any flyers used, and recording identities. Avoid adopting promotional “birthplace” wording as a single origin verdict.'),
('Germany — international revival networks','Europe','Festivals and cross-border circulation','Research lead',LA,
 f'The 2009 scene account discusses Cinema Strange’s German-label/festival connections and wider European circulation. This is a route into research, not a national scene census. [Historical report]({LA}).',
 ['Cinema Strange — The Astonished Eyes of Evening','Scarlet’s Remains — liked artist; album identity to verify','Christ vs. Warhol — liked artist; album identity to verify'],
 'Ask how performance, distribution, and audiences connect geographically separated artists. Do not infer a band’s nationality from its label or festival appearances.',
 'Verify festival archives, label catalogs, touring dates, and independent German scene sources. Nothing here establishes a current event schedule.'),
('Chile — Puerto Montt and wider research','Latin America','A local lead connected to your dark, weighty preferences','Research lead',CHILE,
 f'A December 2024 specialist feature locates A Través del Manto in Puerto Montt and discusses Xmal Funeral. Its praise and stylistic comparisons have a promotional tone. [Feature]({CHILE}).',
 ['A Través del Manto — Xmal Funeral, single; direct artist link below'],
 'Compare rhythmic drive and atmosphere with your named references. “Death Goth” is an artist description here, not an established universal category.',
 'Build outward using Chilean interviews, venues, local labels, and original recordings. One band does not stand for Chile or Latin America. [Artist single](https://atravesdelmanto.bandcamp.com/track/xmal-funeral-2).'),
('Arizona — an atmospheric detour','North America','Recording texture and a related darkwave path','Source-backed overview','https://lycia.bandcamp.com/album/cold',
 'Lycia’s artist page identifies its Tempe, Arizona formation and supplies the Cold recording credits. This documents one artist’s context, not an entire regional genre history. [Artist catalog](https://lycia.bandcamp.com/album/cold).',
 ['Lycia — Cold'],
 'Test your Cocteau Twins and Dead Can Dance interests against a different recording palette. Keep this detour distinct from the raw-deathrock batch.',
 'Add label history, independent interviews, and original edition comparison before extending this into a wider regional account.')]
scene_rows=[]
for title,region,focus,evidence,source,context,records,question,gaps in scenes:
 content=f'''<callout icon="🗺️" color="purple_bg">
	**{focus}**
	{evidence} · checked <mention-date start="2026-10-09"/>
</callout>
## Context
{context}
## Listening anchors
'''+''.join('- '+r+'\n' for r in records)+f'''## Listen through the scene
{question}
## Venues, labels, and open research
{gaps}
'''
 scene_rows.append({'properties':{'Scene':title,'Region':region,'Focus':focus,'Evidence':evidence,'Source':source},'icon':'🗺️','content':content})
(root/'scenes.json').write_text(json.dumps(scene_rows,ensure_ascii=False,indent=2))
# Each visual year span is explicitly an uncertainty window, not an exact release date.
milestones=[
(1980,1980,'Bauhaus — In the Flat Field','Recording','UK recording reference','https://beggarsbanquetrecords.com/bauhaus-in-the-flat-field/','The label places the debut in 1980. Explore voice, rhythm, and guitar space; this milestone is not a claim that one record invented the genre.'),
(1982,1982,'Christian Death — Only Theatre of Pain','Recording','Los Angeles','https://frontierrecords-christiandeath.bandcamp.com/album/only-theatre-of-pain-original','Frontier identifies the original 1982 recording; the linked listing adds Deathwish material. Keep album and EP context separate.'),
(1982,1982,'The Cure — Pornography','Recording','UK recording reference','https://www.thecure.com/release/pornography/','One of your stated favorites. Original year 1982 is secure in the project; earlier official-day differences remain unresolved.'),
(1982,1985,'Batcave — documented retrospective period','Club / scene','London',BAT,'The retrospective compilation/book focuses on 1982–1985. This visual period follows that coverage, not a verified exact opening-to-closure range.'),
(1983,1983,'45 Grave — Sleep in Safety','Recording','Los Angeles','https://music.apple.com/us/album/sleep-in-safety/162551605','A 1983 entry in the current raw-deathrock route. Compare the expanded platform edition with original sequencing when researching further.'),
(1983,1983,'Kommunity FK — The Vision and the Voice','Recording','Los Angeles',KFK,'The official discography distinguishes the 1983 original vinyl from later editions, including the pictured 2006 CD reissue.'),
(1985,1985,'The Sisters of Mercy — First and Last and Always','Recording','UK recording reference',SIS,'The interview supports the original 1985 year and provides participant recollections about guitar arrangements. Your exact “first two records” preference remains unresolved.'),
(1989,1989,'The Cure — Disintegration','Recording','UK recording reference','https://www.thecure.com/release/disintegration/','Your other named Cure favorite. The official page identifies the original 1989 release separately from the 2010 deluxe edition.'),
(1996,1996,'Lycia — Cold','Recording','Arizona / related exploration','https://lycia.bandcamp.com/album/cold','Artist credits identify the original year 1996. Use the atmospheric route as a comparison, not an automatic extension of core ranking eligibility.'),
(2002,2002,'Cinema Strange — The Astonished Eyes of Evening','Recording','Later theatrical deathrock',CIN,'The member catalog supports 2002 and documents a varied instrumental palette. The exact original day is not independently established.'),
(2024,2024,'Puerto Montt — a documented Chilean discovery lead','Regional lead','Chile',CHILE,'A December 2024 feature documents A Través del Manto and its video. This is the publication year of the lead, not a claim that the single first appeared in 2024.')]
history=[]
for year,end,title,kind,scene,source,text in milestones:
 props={'Milestone':title,'Year':year,'date:Window start:start':f'{year}-01-01','date:Window start:is_datetime':0,'date:Window end:start':f'{end}-12-31','date:Window end:is_datetime':0,'Date precision':'Documented period' if end!=year else 'Year span','Kind':kind,'Scene':scene,'Source':source}
 content=f'''## What this entry establishes
{text} [Source]({source}).
## Follow the connection
Open the matching album dossier or scene page in the main hub. Compare rhythm, texture, voice, and the edition you use.
## Date precision
The timeline bar spans the calendar year(s) for visual placement. January 1 and December 31 are display boundaries, not asserted release or event dates. This is a selective history of your listening route; gaps between milestones do not imply nothing happened.
Checked <mention-date start="2026-10-09"/>.
'''
 history.append({'properties':props,'icon':'🕯️','content':content})
(root/'history.json').write_text(json.dumps(history,ensure_ascii=False,indent=2))
print('Prepared 11 album dossiers, 5 scene pages, and 11 timeline milestones.')
