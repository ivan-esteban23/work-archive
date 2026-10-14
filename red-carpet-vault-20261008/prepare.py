from pathlib import Path
import hashlib,json,shutil
root=Path('/home/ivanaguilera/Work/red-carpet-vault-20261008');stage=root/'staged';vault=Path('/home/ivanaguilera/Documents/Obsidian Vault');stage.mkdir(exist_ok=True)
prompt='''Generate a photographic high-luxury red-carpet beauty portrait, premium evening campaign aesthetic. Vertical 3:4 composition, tight head-and-shoulders crop with enough upper bodice visible to showcase couture embroidery; face centered. Original fictional adult woman, mid-20s, mixed East Asian and European features, long straight ash-blonde hair with center part falling over shoulders, luminous smooth skin with natural pores and texture preserved, soft defined brows, warm brown eyes with long separated lashes and soft winged liner, subtle peach blush, glossy rose-nude lips slightly parted showing upper teeth, calm soft gaze directly into lens. Hero wardrobe: black luxury evening dress, wide sculpted asymmetric neckline, matte velvet-like bodice, thick shoulder straps and front panels made of sheer mesh fully embroidered with champagne-gold sequins and antique-gold floral applique; intricate reflective beadwork, believable continuous couture craftsmanship. Solid muted royal-blue studio backdrop, smooth matte finish, no props. Soft direct on-axis beauty key like premium event photography, balanced fill, gentle specular highlights on lips, collarbones and sequins, crisp catchlights in both eyes, minimal shadow, even natural skin tone. 85mm f/2.0 full-frame photographic look, tack-sharp eyes and lips, softly rendered hair edges. Palette: deep black, champagne gold, royal blue, warm skin tones; medium-high clarity, rich natural saturation, filmic highlight rolloff, subtle fine grain, high-end beauty retouching preserving pores and sequin texture. Elegant, serene, modern red-carpet royalty and quiet luxury glamour. Avoid text, watermarks, logos, borders, collage, oversaturation, harsh flash hotspots, HDR, plastic over-smoothed skin, heavy contour, asymmetric eyes, blurry eyes, crooked lips, distorted shoulders, broken sequin patterns, noisy background, cartoon or illustration. High quality, low stylization, photorealistic.'''
ref='Attachments/Editorial Portraits/05 — Red Carpet Gold — Original.jpeg';result='Attachments/Editorial Portraits/Red Carpet Gold — Beauty Portrait.png'
entry=f'''## 05 — Red Carpet Gold

**Recognition:** long blonde hair, black evening dress with gold floral embroidery, blue backdrop, direct beauty lighting.

### Reference and generated result

| Original reference | Generated result |
| --- | --- |
| ![[{ref}\u007c300]] | ![[{result}\u007c300]] |

**Original file supplied:** `/home/ivanaguilera/Downloads/Miku Martineau.jpeg`. This is the user-supplied filename, not an independently verified identification. The reference is copied unchanged into the vault.

**Provenance:** generated from the written prompt alone using the built-in image generator. The reference photograph was supplied afterward and is saved here for future use; it was not an input to this result. The prompt requested an original fictional adult subject rather than an exact likeness.

**Pictures original:** `/home/ivanaguilera/Pictures/red-carpet-beauty-portrait.png` remains in place; the vault holds an identical copy.

**Requested format:** 3:4 vertical. **Adaptation:** the result uses a wider upper-bodice crop and free-flowing hair rather than reproducing the reference's hair styling and neckline exactly.

**Reuse:** attach the reference for its appearance or styling, or attach the result to develop that version. Specify what to preserve and what to change. A filesystem path alone does not attach an image.

### Exact submitted generation prompt

```text
{prompt}
```

### Settings note

The user's suggested controls were photographic/raw mode, low stylization, high quality, and a locked seed for variations. These were expressed as photographic directions where applicable; the built-in tool did not expose raw, stylize, quality, or seed parameters. No seed was locked. Background transparency was set to false.

'''
lib='Editorial Portrait Prompt Library.md';old=(vault/lib).read_text();anchor='## Add a future entry';assert anchor in old;assert '## 05 — Red Carpet Gold' not in old
texts={lib:old.replace(anchor,entry+anchor,1)}
txt='Attachments/Editorial Portraits/Editorial Portrait — Prompt.txt';texts[txt]=(vault/txt).read_text().rstrip()+'\n\n05 — Red Carpet Gold\n\nReference supplied after generation: Miku Martineau.jpeg. Generated from text alone; fictional adult subject.\n\nExact submitted prompt:\n'+prompt+'\n\nActual tool controls: transparent_background=false. Raw, stylize, quality, and seed parameters not exposed; no seed locked.\n'
manifest={}
for rel,body in texts.items():
 p=stage/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
for rel,source in [(ref,Path('/home/ivanaguilera/Downloads/Miku Martineau.jpeg')),(result,Path('/home/ivanaguilera/Pictures/red-carpet-beauty-portrait.png'))]:
 p=stage/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,p)
 assert p.read_bytes()==source.read_bytes()
for p in stage.rglob('*'):
 if p.is_file():
  rel=str(p.relative_to(stage));live=vault/rel;manifest[rel]=hashlib.sha256(live.read_bytes()).hexdigest() if live.exists() else None
(root/'manifest.json').write_text(json.dumps(manifest,indent=2))
assert texts[lib].count('```')%2==0
print('Staged library entry, exact prompt, and two unchanged image copies.')
