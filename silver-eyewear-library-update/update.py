from pathlib import Path
import hashlib,json,re,shutil,sys
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
NOTE=Path('Editorial Portrait Prompt Library.md')
TXT=Path('Attachments/Editorial Portraits/Editorial Portrait — Prompt.txt')
IMAGE=Path('Attachments/Editorial Portraits/Silver Eyewear — Editorial Portrait.png')
SOURCE=Path('/home/ivanaguilera/Pictures/Silver Eyewear — Editorial Portrait.png')

def stage():
    for folder in ['backup','staged']: (ROOT/folder).mkdir(exist_ok=True)
    manifest={}
    for rel in [NOTE,TXT]:
        p=VAULT/rel
        backup=ROOT/'backup'/rel
        backup.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,backup)
        manifest[str(rel)]=hashlib.sha256(p.read_bytes()).hexdigest()
    prompt=(ROOT/'prompt.txt').read_text().strip()
    note=(VAULT/NOTE).read_text()
    assert '## 03 — Silver Eyewear' not in note
    entry='''## 03 — Silver Eyewear

**Recognition:** rimless silver glasses with dangling metal accents, navy pinstripe blazer, rose lips, glossy nude nails and a charcoal studio background.

### Generated image and future reference

![[Attachments/Editorial Portraits/Silver Eyewear — Editorial Portrait.png|450]]

**Original reference photo:** none supplied for this generation.

**Provenance:** an original fictional adult subject generated from the written prompt alone using the built-in image generator. The image above is the generated result; you can attach it as a reference for future variations. It is not an original source photograph.

**Saved Pictures copy:** `/home/ivanaguilera/Pictures/Silver Eyewear — Editorial Portrait.png`.

**Requested format:** 3:4 vertical. Prompt details describe the intended result; the saved image shows four cuff buttons, rather than the three requested.

**Reuse:** attach this generated image and specify what to keep—face, eyewear, styling, pose or lighting—then name the detail to change. Use the prompt alone for a new fictional subject.

### Exact generation prompt

```text
'''+prompt+'\n```\n\n'
    assert '## Add a future entry' in note
    note=note.replace('## Add a future entry',entry+'## Add a future entry',1)
    note=note.replace('Each entry pairs an original, its generated result, and the exact saved prompt.','Each entry records its reference status, generated result, and exact saved prompt. Some entries include original reference photographs; others were generated from text alone.')
    txt=(VAULT/TXT).read_text()
    addition='''\n\n============================================================
03 — SILVER EYEWEAR — EXECUTIVE EDITORIAL PORTRAIT
============================================================

Recognize it: rimless silver glasses with dangling accents, navy pinstripe blazer, charcoal background, glossy nude nails beside the face.
Original reference photo: none supplied.
Generation method: written prompt only; original fictional adult subject, built-in image generator.
Generated result and reference for future variations: '''+str(VAULT/IMAGE)+'''
Pictures copy: /home/ivanaguilera/Pictures/Silver Eyewear — Editorial Portrait.png
Requested aspect ratio: 3:4 vertical.
Observed variation: saved image shows four cuff buttons instead of the requested three.
Reuse: attach the generated image for image-guided variations and specify which features to preserve. A path in this file does not attach an image automatically. Use the text alone for a new fictional subject.

FULL PROMPT

'''+prompt+'\n'
    for rel,content in [(NOTE,note),(TXT,txt+addition)]:
        dest=ROOT/'staged'/rel
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(content)
    assert not (VAULT/IMAGE).exists()
    dest=ROOT/'staged'/IMAGE
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(SOURCE,dest)
    manifest[str(IMAGE)]=None
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Staged third library entry, appended TXT prompt and image; both existing files backed up.')

def apply():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    for name,expected in manifest.items():
        p=VAULT/name
        actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
        assert actual==expected,'File changed since staging: '+name
    for name in manifest:
        p=VAULT/name
        p.parent.mkdir(parents=True,exist_ok=True)
        data=(ROOT/'staged'/name).read_bytes()
        p.write_bytes(data)
        assert p.read_bytes()==data,name
    text=(VAULT/NOTE).read_text()
    for ref in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',text):
        assert (VAULT/ref).exists(),ref
    assert text.count('```')%2==0
    assert (VAULT/IMAGE).read_bytes()==SOURCE.read_bytes()
    prompt=(ROOT/'prompt.txt').read_text().strip()
    assert prompt in text and prompt in (VAULT/TXT).read_text()
    for rel in [NOTE,TXT]:
        old=(ROOT/'backup'/rel).read_text()
        assert 'SUBJECT: Young East Asian woman' in old and 'SUBJECT: Young East Asian woman' in (VAULT/rel).read_text()
    print('Saved and read back three files; exact prompt, previous entries and all attachment links verified.')

if __name__=='__main__': stage() if sys.argv[1]=='stage' else apply()
