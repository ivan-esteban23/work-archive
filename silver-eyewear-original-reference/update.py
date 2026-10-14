from pathlib import Path
import hashlib,json,re,shutil,sys
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
SOURCE=Path('/home/ivanaguilera/Downloads/𝙛𝙤𝙧 𝙙𝙞𝙫𝙚𝙨   💬.jpeg')
REFERENCE=VAULT/'Attachments/Editorial Portraits/03 — Silver Eyewear — Original.jpeg'
NOTE=VAULT/'Editorial Portrait Prompt Library.md'
TXT=VAULT/'Attachments/Editorial Portraits/Editorial Portrait — Prompt.txt'

def stage():
    (ROOT/'backup').mkdir(parents=True,exist_ok=True)
    (ROOT/'staged').mkdir(exist_ok=True)
    manifest={}
    for p in [NOTE,TXT]:
        shutil.copy2(p,ROOT/'backup'/p.name)
        manifest[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
    note=NOTE.read_text()
    old='''### Generated image and future reference

![[Attachments/Editorial Portraits/Silver Eyewear — Editorial Portrait.png|450]]

**Original reference photo:** none supplied for this generation.

**Provenance:** an original fictional adult subject generated from the written prompt alone using the built-in image generator. The image above is the generated result; you can attach it as a reference for future variations. It is not an original source photograph.'''
    new='''### Original reference

![[Attachments/Editorial Portraits/03 — Silver Eyewear — Original.jpeg|450]]

**Original file supplied:** `/home/ivanaguilera/Downloads/𝙛𝙤𝙧 𝙙𝙞𝙫𝙚𝙨   💬.jpeg`.

The reference above is now preserved as an unchanged attachment in this vault. Its silver eyewear, pinstripe blazer, raised hand and charcoal background correspond to this prompt.

### Generated result

![[Attachments/Editorial Portraits/Silver Eyewear — Editorial Portrait.png|450]]

**Provenance:** the saved result was generated from the written prompt alone using the built-in image generator. The original photograph was supplied afterward and is now linked here for future reference-guided generation; it was not attached to the earlier generation. The prompt asks for an original fictional adult subject, so it does not request an exact identity match to the original photo.'''
    assert old in note
    note=note.replace(old,new,1)
    old='**Reuse:** attach this generated image and specify what to keep—face, eyewear, styling, pose or lighting—then name the detail to change. Use the prompt alone for a new fictional subject.'
    new='**Reuse:** attach the original reference to follow its styling and composition, or the generated result to develop that version. Specify which features to preserve and which to change. Keep the fictional-subject instruction if you want a new person rather than the original photo\'s likeness.'
    assert old in note
    note=note.replace(old,new,1)
    text=TXT.read_text()
    old='Original reference photo: none supplied.\nGeneration method: written prompt only; original fictional adult subject, built-in image generator.'
    new='Original reference supplied afterward: '+str(SOURCE)+'\nStable vault reference copy: '+str(REFERENCE)+'\nReference SHA-256: '+hashlib.sha256(SOURCE.read_bytes()).hexdigest()+'\nGeneration method: the existing result used the written prompt only. This original was linked afterward and was not an input to that generation. The prompt specifies an original fictional adult subject.'
    assert old in text
    text=text.replace(old,new,1)
    old='Reuse: attach the generated image for image-guided variations and specify which features to preserve. A path in this file does not attach an image automatically. Use the text alone for a new fictional subject.'
    new='Reuse: attach the original photo for styling/composition reference, or the generated result for variations of that version. Specify which features to preserve. A path in this file does not attach an image automatically. Keep the fictional-subject instruction for a new person.'
    assert old in text
    text=text.replace(old,new,1)
    for p,data in [(NOTE,note.encode()),(TXT,text.encode()),(REFERENCE,SOURCE.read_bytes())]:
        (ROOT/'staged'/p.name).write_bytes(data)
    assert not REFERENCE.exists()
    manifest[str(REFERENCE)]=None
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Staged original reference and corrected Markdown/TXT mappings; existing files backed up.')

def apply():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    for filename,expected in manifest.items():
        p=Path(filename)
        actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
        assert actual==expected,'Changed since staging: '+filename
    for filename in manifest:
        p=Path(filename)
        p.write_bytes((ROOT/'staged'/p.name).read_bytes())
        assert p.read_bytes()==(ROOT/'staged'/p.name).read_bytes()
    assert REFERENCE.read_bytes()==SOURCE.read_bytes()
    note=NOTE.read_text()
    for ref in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',note): assert (VAULT/ref).exists(),ref
    assert note.count('## 03 — Silver Eyewear')==1
    assert 'Original reference photo: none supplied.' not in TXT.read_text()
    assert note.count('```')%2==0
    print('Saved and verified original reference, both portrait previews, TXT mapping and all attachment links. Original Downloads file retained.')

if __name__=='__main__': stage() if sys.argv[1]=='stage' else apply()
