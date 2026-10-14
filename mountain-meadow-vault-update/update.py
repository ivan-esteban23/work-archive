from pathlib import Path
import hashlib,json,re,shutil,sys
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
ATT=Path('Attachments/Editorial Portraits')
NOTE=Path('Editorial Portrait Prompt Library.md')
TXT=ATT/'Editorial Portrait — Prompt.txt'
REF=ATT/'04 — Mountain Meadow — Original.jpg'
IMAGE=ATT/'Mountain Meadow — Resort Editorial.png'
SOURCE=Path('/home/ivanaguilera/Downloads/peakpx (1).jpg')
GENERATED=Path('/home/ivanaguilera/Pictures/Mountain Meadow — Resort Editorial.png')
PROMPT=Path('/home/ivanaguilera/Pictures/Mountain Meadow — Resort Editorial — Prompt.txt')

def stage():
    for folder in ['backup','staged']: (ROOT/folder).mkdir(parents=True,exist_ok=True)
    manifest={}
    for rel in [NOTE,TXT]:
        p=VAULT/rel
        target=ROOT/'backup'/rel
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,target)
        manifest[str(rel)]=hashlib.sha256(p.read_bytes()).hexdigest()
    content=PROMPT.read_text().strip()
    prompt,settings=content.split('\n\nUSER SETTINGS TIP',1)
    tip='USER SETTINGS TIP'+settings
    note=(VAULT/NOTE).read_text()
    assert '## 04 — Mountain Meadow' not in note
    assert '## Add a future entry' in note
    entry='''## 04 — Mountain Meadow

**Recognition:** windblown blonde hair, black eyelet dress, coral-red statement necklace, black handbag with a striped strap, mountain backdrop and yellow foreground flowers.

### Original reference

![[Attachments/Editorial Portraits/04 — Mountain Meadow — Original.jpg|450]]

**Original file supplied:** `/home/ivanaguilera/Downloads/peakpx (1).jpg`.

The original is copied unchanged into this vault so the reference survives cleaning Downloads.

### Generated result

![[Attachments/Editorial Portraits/Mountain Meadow — Resort Editorial.png|450]]

**Provenance:** the saved result was generated from the written prompt alone using the built-in image generator. This original reference was supplied afterward and associated with the prompt for future use; it was not attached to the earlier generation. The prompt specifies an original fictional adult subject, not an exact identity match to the photograph.

**Saved Pictures copy:** `/home/ivanaguilera/Pictures/Mountain Meadow — Resort Editorial.png`.

**Requested format:** 3:4 vertical. The generated image is an adaptation: its full-body framing includes black boots, which were not specified in the prompt.

**Reuse:** attach the original for its styling/composition, or the generated result for variations of that version. Name what to preserve, then change one feature at a time, such as necklace size or slit height. A file path alone does not attach an image.

### Exact generation prompt

```text
'''+prompt+'''
```

### Settings note

'''+tip+'''

These are the user's settings suggestions. The built-in generation tool used here does not expose raw mode, stylize, quality or seed controls; a fixed seed was not set.

'''
    note=note.replace('## Add a future entry',entry+'## Add a future entry',1)
    text=(VAULT/TXT).read_text()
    addition='''\n\n============================================================
04 — MOUNTAIN MEADOW — RESORT EDITORIAL
============================================================

Recognize it: blonde hair, black eyelet dress, coral-red necklace, black handbag with striped strap, yellow wildflowers and layered mountains.
Original reference supplied afterward: '''+str(SOURCE)+'''
Stable vault reference copy: '''+str(VAULT/REF)+'''
Reference SHA-256: '''+hashlib.sha256(SOURCE.read_bytes()).hexdigest()+'''
Generated result: '''+str(VAULT/IMAGE)+'''
Pictures copy: '''+str(GENERATED)+'''
Generation method: written prompt only, built-in image generator. The original reference was added afterward and was not an input to the saved result. The prompt specifies an original fictional adult subject.
Requested aspect ratio: 3:4 vertical.
Observed adaptation: generated full-body framing includes black boots not specified in the prompt.
Reuse: attach either the original for its styling/composition or the generated result for variations. Specify what to preserve and change. File paths do not attach images automatically.

FULL PROMPT

'''+content+'\n\nActual tool controls: raw mode, stylize, quality and seed were not exposed by the built-in tool; a fixed seed was not set.\n'
    for rel,data in [(NOTE,note.encode()),(TXT,(text+addition).encode()),(REF,SOURCE.read_bytes()),(IMAGE,GENERATED.read_bytes())]:
        p=ROOT/'staged'/rel
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(data)
        if rel not in [NOTE,TXT]:
            assert not (VAULT/rel).exists(),'Existing attachment: '+str(rel)
            manifest[str(rel)]=None
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Staged entry 04 with original, result and prompt. Existing note and TXT backed up.')

def apply():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    for rel,expected in manifest.items():
        p=VAULT/rel
        actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
        assert actual==expected,'Changed since staging: '+rel
    for rel in manifest:
        p=VAULT/rel
        p.parent.mkdir(parents=True,exist_ok=True)
        data=(ROOT/'staged'/rel).read_bytes()
        p.write_bytes(data)
        assert p.read_bytes()==data,rel
    note=(VAULT/NOTE).read_text()
    for ref in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',note): assert (VAULT/ref).exists(),ref
    assert note.count('## 04 — Mountain Meadow')==1
    assert note.count('```')%2==0
    assert (VAULT/REF).read_bytes()==SOURCE.read_bytes()
    assert (VAULT/IMAGE).read_bytes()==GENERATED.read_bytes()
    prompt=PROMPT.read_text().split('\n\nUSER SETTINGS TIP')[0].strip()
    assert prompt in note and prompt in (VAULT/TXT).read_text()
    for heading in ['## 01 — Gray Suit','## 02 — Lavender and Silver','## 03 — Silver Eyewear']:
        assert heading in note
    print('Saved and read back four files; original, result, exact prompt and all library links verified. Previous entries preserved.')

if __name__=='__main__': stage() if sys.argv[1]=='stage' else apply()
