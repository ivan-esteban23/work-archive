from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
PICS=Path('/home/ivanaguilera/Pictures')
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
STAGED=ROOT/'staged'
ATT=Path('Attachments/Editorial Portraits')

def stage():
    STAGED.mkdir(parents=True,exist_ok=True)
    images={
      'Reference Images/01 — Gray Suit — Original.jpeg':'01 — Gray Suit — Original.jpeg',
      'Reference Images/02 — Lavender and Silver — Original.jpeg':'02 — Lavender and Silver — Original.jpeg',
      'Editorial Portrait.png':'Editorial Portrait.png',
      'Lavender and Silver — Editorial Portrait.png':'Lavender and Silver — Editorial Portrait.png',
    }
    note=(PICS/'Editorial Portrait Prompt Library.md').read_text()
    note=note.replace('[Open the TXT prompt library](<Editorial Portrait — Prompt.txt>)','[[Attachments/Editorial Portraits/Editorial Portrait — Prompt.txt|Open the TXT prompt library]]')
    for source,dest in images.items():
        pattern=r'!\[[^\]]*\]\(<'+re.escape(source)+r'>\)'
        note,count=re.subn(pattern,'![[Attachments/Editorial Portraits/'+dest+'|450]]',note)
        assert count==1,(source,count)
        target=STAGED/ATT/dest
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes((PICS/source).read_bytes())
    note=note.replace('Copy the reference into `Reference Images` with a descriptive filename.','Copy the reference into `Attachments/Editorial Portraits` with a descriptive filename.')
    (STAGED/'Editorial Portrait Prompt Library.md').write_text(note)
    text=(PICS/'Editorial Portrait — Prompt.txt').read_text()
    text=text.replace(str(PICS/'Editorial Portrait Prompt Library.md'),str(VAULT/'Editorial Portrait Prompt Library.md'))
    text=text.replace('into Pictures/Reference Images','into the vault’s Attachments/Editorial Portraits folder')
    for source,dest in images.items():
        text=text.replace(str(PICS/source),str(VAULT/ATT/dest))
    (STAGED/ATT/'Editorial Portrait — Prompt.txt').write_text(text)
    files=sorted(p for p in STAGED.rglob('*') if p.is_file())
    for p in files: assert not (VAULT/p.relative_to(STAGED)).exists(),'Destination already exists'
    manifest={p.relative_to(STAGED).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Staged note, TXT library, and four unchanged image copies.')

def apply():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    for name,digest in manifest.items():
        assert not (VAULT/name).exists(),'Destination already exists: '+name
        assert hashlib.sha256((STAGED/name).read_bytes()).hexdigest()==digest
    for name,digest in manifest.items():
        p=VAULT/name
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes((STAGED/name).read_bytes())
        assert hashlib.sha256(p.read_bytes()).hexdigest()==digest
    note=(VAULT/'Editorial Portrait Prompt Library.md').read_text()
    for ref in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',note):
        assert (VAULT/ref).exists(),ref
    assert note.count('```')%2==0
    print('Saved and read back six files; all vault attachment links verified. Live Obsidian rendering was not tested.')

if __name__=='__main__':
    import sys
    stage() if sys.argv[1]=='stage' else apply()
