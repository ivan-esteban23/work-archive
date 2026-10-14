from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
PICS=Path('/home/ivanaguilera/Pictures')
ROOT.mkdir(exist_ok=True)
(ROOT/'backup').mkdir(exist_ok=True)
(ROOT/'staged').mkdir(exist_ok=True)
promptfile=PICS/'Editorial Portrait — Prompt.txt'
data=promptfile.read_bytes()
shutil.copy2(promptfile,ROOT/'backup'/promptfile.name)
text=data.decode()
delimiter='\n\n\n============================================================\nLAVENDER AND SILVER — EDITORIAL BEAUTY PORTRAIT\n============================================================\n\n'
assert delimiter in text
first,second=text.split(delimiter,1)
sources=[
 ('/home/ivanaguilera/Downloads/#goyounjung.jpeg','Reference Images/01 — Gray Suit — Original.jpeg'),
 ('/home/ivanaguilera/Downloads/_.jpeg','Reference Images/02 — Lavender and Silver — Original.jpeg')
]
for source,dest in sources:
 p=Path(source)
 target=ROOT/'staged'/dest
 target.parent.mkdir(exist_ok=True)
 shutil.copy2(p,target)
records=[]
for source,dest in sources:
 records.append((source,str(PICS/dest),hashlib.sha256(Path(source).read_bytes()).hexdigest()))
header='''EDITORIAL PORTRAIT PROMPT LIBRARY
Reference mapping added 8 October 2026.

Visual companion: /home/ivanaguilera/Pictures/Editorial Portrait Prompt Library.md
Reference originals are copied unchanged into Pictures/Reference Images so they remain available if Downloads is cleaned. The original Downloads files are retained.

HOW TO REUSE
For reference-guided generation, attach the corresponding reference image along with the prompt. A file path written in this TXT file does not itself attach an image or make it accessible to a model. State whether to preserve the person's appearance or only borrow styling/composition. For a new subject, use the prompt alone and expect a different face.

'''
first_meta=f'''============================================================
01 — GRAY SUIT — STUDIO EDITORIAL PORTRAIT
============================================================

Recognize it: charcoal-gray suit, white shirt and dark tie; long dark hair; hand resting against the cheek; pale blue-gray backdrop.
Original supplied: {records[0][0]}
Stable reference copy: {records[0][1]}
Reference SHA-256: {records[0][2]}
Generated result: /home/ivanaguilera/Pictures/Editorial Portrait.png
Generation method: supplied image was used as the reference input with the prompt below.
Requested aspect ratio: 4:5 vertical.

FULL PROMPT

'''
second_meta=f'''\n\n============================================================
02 — LAVENDER AND SILVER — EDITORIAL BEAUTY PORTRAIT
============================================================

Recognize it: lavender textured V-neck knit, pulled-back dark hair, layered silver necklaces, pale blue-gray wall; original includes magazine lettering.
Original supplied later: {records[1][0]}
Stable reference copy: {records[1][1]}
Reference SHA-256: {records[1][2]}
Generated result: /home/ivanaguilera/Pictures/Lavender and Silver — Editorial Portrait.png
Generation method: the existing generated result used the written prompt alone. This original was associated with it afterward for future reference-guided generations; it was not attached to that generation.
Requested aspect ratio: 3:4 vertical.
Intentional differences: the prompt requests a rectangular halo crystal drop earring, while the original shows a curved/drop-shaped jewelry motif. It requests no text, while the original contains magazine lettering. Treat the prompt as an editorial adaptation rather than an exact reconstruction.

FULL PROMPT

'''
updated=header+first_meta+first.strip()+'\n'+second_meta+second
(ROOT/'staged'/promptfile.name).write_text(updated)
md='''# Editorial Portrait Prompt Library

Reference index created 8 October 2026. Each entry pairs an original, its generated result, and the exact saved prompt. The reference copies below are unchanged; original Downloads files are retained.

[Open the TXT prompt library](<Editorial Portrait — Prompt.txt>)

## How to use this library

Attach a reference image and paste its prompt for reference-guided generation. Say whether you want the same person's appearance or just the visual style. Use the prompt alone for a new subject. File paths in a prompt do not attach images automatically. Change one feature at a time—wardrobe, background, lighting or framing—to compare variations easily.

## 01 — Gray Suit

**Recognition:** hand against cheek, gray suit and tie, long black hair, cool studio background.

### Original reference

![Gray-suit original reference](<Reference Images/01 — Gray Suit — Original.jpeg>)

Original path: `/home/ivanaguilera/Downloads/#goyounjung.jpeg`.

### Generated result

![Generated gray-suit editorial portrait](<Editorial Portrait.png>)

**Provenance:** generated with this original supplied as the reference image. Requested format: 4:5 vertical.

### Exact generation prompt

```text
'''+first.strip()+'''
```

## 02 — Lavender and Silver

**Recognition:** lavender knit, pulled-back hair, two necklaces, pale blue-gray wall. The original has magazine lettering.

### Original reference

![Lavender original reference](<Reference Images/02 — Lavender and Silver — Original.jpeg>)

Original path: `/home/ivanaguilera/Downloads/_.jpeg`.

### Generated result

![Generated lavender and silver editorial portrait](<Lavender and Silver — Editorial Portrait.png>)

**Provenance:** this result was generated from text alone. The original above was supplied afterward and linked here for future reference-guided generations. It was not an input to the saved result.

**Adaptation details:** the prompt specifies a rectangular halo crystal earring; the original uses a different curved/drop-shaped motif. The prompt omits magazine lettering. Requested format: 3:4 vertical. These are creative directions, not an exact reconstruction of every original detail.

### Exact generation prompt and short variant

```text
'''+second.strip()+'''
```

## Add a future entry

Record: title, original reference filename, generated result filename, exact prompt, whether the original was actually attached, requested format, and any deliberate differences. Copy the reference into `Reference Images` with a descriptive filename. This keeps each prompt understandable after Downloads is cleaned.
'''
mdname='Editorial Portrait Prompt Library.md'
assert not (PICS/mdname).exists(),'Existing visual library requires review before replacing'
(ROOT/'staged'/mdname).write_text(md)
manifest={promptfile.name:hashlib.sha256(data).hexdigest(),mdname:None}
for _,dest in sources:
 assert not (PICS/dest).exists(),dest
 manifest[dest]=None
(ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Staged reference copies, two prompt mappings, and visual Markdown library; original TXT backed up.')
