from pathlib import Path
from datetime import date, timedelta
import json, hashlib, shutil, re, sys

W = Path(__file__).resolve().parent
V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
S = W/'staged'
TITLE = 'Japan 2027 — Photography and Filming Wishlist'
RULES = 'https://policies.env.go.jp/national-garden/shinjukugyoen/english/photography/image_capture/'
KYOTO = 'https://kyoto.travel/en/news/sightseeing-guidelines/'
SHOTS = [
('Travel moments', 'One first-impression detail and a short spoken arrival note; recovery comes first.'),
('Asakusa', 'One temple/streetscape wide shot and one detail; Sumida river composition only if already visiting.'),
('Chidorigafuchi', 'A moat reflection photo plus a steady blossom-and-water clip.'),
('Shinjuku Gyoen', 'One garden-wide frame and a backlit blossom detail; check equipment and filming rules.'),
('Nakameguro', 'River perspective and reflections; night clips only if seasonal lighting is confirmed.'),
('Tokyo buffer', 'Revisit one missed blossom shot, or capture textures in the single chosen neighborhood.'),
('Travel moments', 'Ticket-free packing details, a window view, and a short Kyoto arrival note.'),
('Philosopher’s Path', 'Canal-leading-lines photo, petal detail if present, and a steady water clip.'),
('Historic Kyoto', 'An allowed temple composition and a street detail; follow photography/private-lane signs.'),
('Fushimi Inari', 'Torii repetition and a quiet detail from an allowed spot without blocking the path.'),
('Matcha and shops', 'If choosing Uji, tea color, cup detail, and a river clip; tea preparation only with permission.'),
('Kyoto buffer', 'One favorite Kyoto scene; if choosing Arashiyama, a bamboo composition from the path.'),
('Travel moments', 'A window view or Tokyo return note; transfer logistics come first.'),
('Matcha and shops', 'One souvenir story or a final favorite Tokyo image; shop interiors only with permission.'),
('Travel moments', 'Optional closing voice note or bag detail; airport timing comes first.'),
]

CONTENT = f'''# 📷 Japan 2027 — Photography and filming wishlist

[[Japan 2027 — Start Here|← Dashboard]] · [[Japan 2027 — Daily Pocket Cards|Daily cards]] · [[Japan 2027 — Today|Today]] · [[Japan 2027 — Memories|Keep your favorites]]

**Creative plan · added 7 October 2026.** Based on the proposed 25 March–8 April itinerary. Light suggestions are creative preferences, not promised conditions or entry times. Check access, weather, flowering, and local signs; choose one photo and one short sequence each day rather than collecting everything.

## My three priorities

- [ ] **A blossom photo I love:** one strong wide scene, reflection, or close detail.
- [ ] **A matcha memory:** tea color, a cup in my hands, and a sentence about the taste.
- [ ] **One 30–90 second travel film:** blossoms, city/temple details, tea or food, and a personal moment.

These support [[Japan 2027 — My Five Things]]; a finished personal memory counts even if nothing is posted.

## Chidorigafuchi

**Slot:** [[Japan 2027 — Pocket 2027-03-27|27 March]]; a Tokyo buffer can replace it.
- [ ] Photo: blossom branches framing the moat; try one reflection and one close detail.
- [ ] Film: a steady wide view, water movement, then a blossom close-up; 5–10 seconds per clip.
**Light:** soft morning light or overcast for details; reflections depend on wind. Keep evening footage optional until illumination is confirmed.

## Shinjuku Gyoen

**Slot:** [[Japan 2027 — Pocket 2027-03-28|28 March]].
- [ ] Photo: garden-wide context, then a branch against a clean background.
- [ ] Film: a stationary garden view and blossom movement from a permitted spot.
**Light:** morning within verified access hours; gentle backlight if available. A handheld session keeps the kit simple; see the venue rules below.

## Nakameguro

**Slot:** [[Japan 2027 — Pocket 2027-03-29|29 March]].
- [ ] Photo: river perspective, reflections, and neighborhood textures.
- [ ] Film: one river-wide clip and a nearby detail; record only from a place where stopping is allowed.
**Light:** late afternoon; optional blue-hour/night footage only if access and seasonal lighting are confirmed. Move off busy bridges before composing.

## Philosopher’s Path

**Slot:** [[Japan 2027 — Pocket 2027-04-01|1 April]] or a swapped Kyoto day.
- [ ] Photo: canal leading lines; add petals on water only if conditions provide them.
- [ ] Film: steady water, a tree detail, and a short personal reaction from a clear standing spot.
**Light:** soft morning light; overcast can suit blossom detail. Protect the relaxed 2–3 hour photo block.

## Historic Kyoto

**Slot:** [[Japan 2027 — Pocket 2027-04-02|2 April]].
- [ ] Photo: an allowed Kiyomizu-dera architectural composition, then one historic-street detail.
- [ ] Film: a wide view and a texture/detail without blocking steps or foot traffic.
**Light:** morning within visiting hours; choose architecture and textures if blossoms disappoint. Gion footage depends on local permissions and signs.

## Fushimi Inari

**Slot:** [[Japan 2027 — Pocket 2027-04-03|3 April]].
- [ ] Photo: torii repetition or a close architectural detail from an allowed public position.
- [ ] Film: one stationary corridor view and one detail; skip a shot if it would interrupt worship or obstruct movement.
**Light:** try gentler morning light; the full mountain route is optional. No empty-corridor promise.

## Asakusa

**Slot:** [[Japan 2027 — Pocket 2027-03-26|26 March]].
- [ ] Photo: temple/streetscape context and one small detail; Sumida Park is an optional existing extension.
- [ ] Film: a street-wide clip and a purchased snack close-up where permitted.
**Light:** easy morning session; shorten it for jet lag. Do not add a separate outing just for footage.

## Matcha and shops

**Slots:** [[Japan 2027 — Pocket 2027-04-04|optional Uji on 4 April]], existing café stops, or [[Japan 2027 — Pocket 2027-04-07|7 April shopping]].
- [ ] Photo: matcha color beside natural window light; souvenir and hands; one personally meaningful record or vintage find.
- [ ] Film: tea preparation only if staff agree, cup-to-table detail, and a tasting reaction. For shops, choose an approved detail or record the purchase back at the hotel.
**Light:** natural window light when available; protect the experience and meal time. Uji remains one excursion choice, replacing Nara/Osaka.

## Tokyo buffer

**Slots:** [[Japan 2027 — Pocket 2027-03-30|30 March]] and [[Japan 2027 — Pocket 2027-04-07|7 April]].
- [ ] Revisit one missed blossom shot or make a small neighborhood story in the single area chosen that day.
**Light:** choose from current weather and bloom reports. A skyline shot stays optional; visibility and access decide.

## Kyoto buffer

**Slot:** [[Japan 2027 — Pocket 2027-04-05|5 April]].
- [ ] Revisit the strongest blossom scene; if choosing Arashiyama instead, frame bamboo from the permitted path and capture one steady clip.
**Light:** soft light when available; return with time to pack. The alternative replaces the blossom outing.

## Travel moments

**Slots:** arrival, the two intercity transfers, and departure.
- [ ] Packing detail, a window landscape if practical, and a short arrival/return voice note.
Avoid showing passport, boarding-pass codes, reservation numbers, or private screens. Filming is optional; transfers and recovery take priority.

## A simple film sequence

1. **Opening:** a blossom scene or first-impression voice note.
2. **Tokyo:** one wide street/river view and one detail.
3. **Journey:** a brief window view or packing transition.
4. **Kyoto:** canal or temple context, then a detail.
5. **Tea and a personal moment:** matcha and one sentence about the experience.
6. **Ending:** favorite scene and a closing thought.

For each chosen scene, aim for a **wide view → medium view → detail**, holding clips about 5–10 seconds with a little stillness before/after the action. Capture a short clean ambient sound where recording is welcome. Use vertical framing for your primary social clips; take a separate horizontal view only if you want a landscape version. Keep recording choices consistent with a kit tested before departure.

Livestreaming is a separate optional activity: choose a permitted location, test the connection/audio, and set a short time limit. Recording footage does not establish permission to broadcast it.

## Permissions and venue checks

**Shinjuku Gyoen:** the official page distinguishes personal non-commercial filming from commercial work, restricts obstructive professional equipment for specified photo activities during busy seasons, and says monetized livestreaming is not permitted. Check the exact activity and equipment rules before visiting. Its current 2027 restriction listing pairs dates with inconsistent weekdays, so reconfirm the dated notice rather than treating it as a final calendar. [Official photography/filming rules]({RULES})

**Kyoto/Gion:** respect designated photography areas, private property, and street access. Do not follow or photograph geiko/maiko without permission or block streets. [Kyoto City visitor guidance]({KYOTO})

For each café, shop, temple, or other venue, check its own rules; asking about photos does not establish permission for video, livestreaming, commercial work, or a tripod. Until confirmed, mark permission as **not checked**. Sources checked 7 October 2026; recheck before travel.

### Permission record — copy per venue

- **Place / date:** …
- **Intended use:** personal photo / recorded video / public post / monetized content / livestream …
- **Equipment:** handheld / grip / tripod / microphone …
- **Status:** not checked / allowed with conditions / declined …
- **Rule link or staff response, checked on:** …
- **Allowed area, time, and conditions:** …
- **Alternative if declined:** another permitted shot or a voice note later …

## Choose today’s shots

Copy your choices into [[Japan 2027 — Today]]:
- **Photo I most want:** …
- **Short sequence:** wide … → medium … → detail …
- **Light / access / permission checked:** …
- **Favorite file and story:** …

Each evening, keep one favorite photo and one useful clip in [[Japan 2027 — Memories]]. Back up originals separately from the camera card/device and verify the copies before deleting anything. Editing and posting can wait until home.
'''

def prepare():
    S.mkdir(parents=True, exist_ok=True)
    assert not (V/(TITLE+'.md')).exists()
    (S/(TITLE+'.md')).write_text(CONTENT)
    originals = {}
    def save(filename, transform):
        p = V/filename
        originals[filename] = hashlib.sha256(p.read_bytes()).hexdigest()
        (S/filename).write_text(transform(p.read_text()))
    link = f'**Photography and filming:** [[{TITLE}|📷 Shot ideas, light, and permissions]]'
    def top(s):
        pos=s.index('\n')+1
        return s[:pos]+'\n'+link+'\n'+s[pos:]
    for filename in ['Japan 2027 — Start Here.md','Japan Travel Guide 2027.md','Japan 2027 — My Five Things.md','Japan 2027 — Memories.md','Japan 2027 — Daily Pocket Cards.md']:
        save(filename, top)
    def today(s):
        assert '## 📍 Main plan' in s
        return top(s).replace('## 📍 Main plan',f'''## 📷 Today’s photo and film

- **Photo I most want:** …
- **Short sequence:** wide … → medium … → detail …
- **Suggested light / verified access:** …
- **Permission and equipment conditions:** …
- **Favorite file / story:** …

## 📍 Main plan''',1)
    save('Japan 2027 — Today.md', today)
    for i,(section,prompt) in enumerate(SHOTS):
        d=date(2027,3,25)+timedelta(days=i)
        filename=f'Japan 2027 — Pocket {d.isoformat()}.md'
        def add(s, section=section, prompt=prompt):
            assert '**Rain backup:**' in s
            return s.replace('**Rain backup:**', f'**Photo / film:** {prompt} [[{TITLE}#{section}|Shot ideas]]\n\n**Rain backup:**',1)
        save(filename,add)
    (W/'manifest.json').write_text(json.dumps(originals,indent=2))
    validate(S)
    print('Prepared wishlist, 15 daily prompts, and links in 6 companion notes; links and content verified.')

def validate(root):
    text=(root/(TITLE+'.md')).read_text()
    for section,_ in SHOTS:
        assert f'## {section}\n' in text
    assert RULES in text and KYOTO in text
    for p in root.glob('*.md'):
        if p.name.startswith('Japan 2027 — Pocket '):
            assert '**Photo / film:**' in p.read_text()
        if p.stem == TITLE:
            for target in re.findall(r'\[\[([^\]|]+)', text):
                target=target.split('#')[0]
                assert (V/(target+'.md')).exists() or (root/(target+'.md')).exists(),target
    assert '## 📷 Today’s photo and film' in (root/'Japan 2027 — Today.md').read_text()

def install():
    manifest=json.loads((W/'manifest.json').read_text())
    for filename,expected in manifest.items():
        assert hashlib.sha256((V/filename).read_bytes()).hexdigest()==expected,filename
    assert not (V/(TITLE+'.md')).exists()
    backup=W/'backup';backup.mkdir(exist_ok=True)
    for filename in manifest:
        shutil.copy2(V/filename,backup/filename)
    for p in S.glob('*.md'):
        shutil.copy2(p,V/p.name)
    validate(V)
    assert all(p.read_bytes()==(V/p.name).read_bytes() for p in S.glob('*.md'))
    print('Saved and verified wishlist, 15 pocket-card shot prompts, and 6 companion-note integrations. Existing notes backed up.')

if __name__=='__main__':
    install() if '--install' in sys.argv else prepare()
