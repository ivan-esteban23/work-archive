from pathlib import Path
import hashlib, json, re, shutil, zipfile

base = Path(__file__).resolve().parent
vault = Path('/home/ivanaguilera/Documents/Obsidian Vault')
manifest = json.loads((base/'manifest.json').read_text())
paths = list(vault.rglob('*.md'))
stems = {p.stem for p in paths}
stems.update(Path(item['relative']).stem for item in manifest)
for item in manifest:
    target = vault/item['relative']
    expected = item['expected']
    if expected is None:
        assert not target.exists(), f'New target already exists: {target}'
        assert not any(p.stem == target.stem for p in paths), f'Ambiguous wiki target: {target.stem}'
    else:
        assert hashlib.sha256(target.read_bytes()).hexdigest() == expected, f'Note changed during preparation: {target}'
    text = (base/'staged'/item['relative']).read_text()
    assert text.count('```') % 2 == 0
    for ref in re.findall(r'\[\[([^\]]+)\]\]',text):
        name = ref.split('|')[0].split('#')[0]
        assert name in stems, f'Unresolved link: {name}'
with zipfile.ZipFile(base/'Black Metal — ChatGPT Project Pack.zip') as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == 9
for item in manifest:
    target = vault/item['relative']
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(base/'staged'/item['relative'],target)
    assert target.read_bytes() == (base/'staged'/item['relative']).read_bytes()
print('Saved and read back seven Black Metal notes plus the music prompt index; wiki targets, code fences, and ZIP checked.')
