from pathlib import Path
import re,shutil
v=Path('/home/ivanaguilera/Documents/Obsidian Vault');p=v/'Editorial Portrait Prompt Library.md';t=Path('/home/ivanaguilera/Work/editorial-library-redesign-20261012')
original=p.read_bytes();text=original.decode()
parts=list(re.finditer(r'^## (\d{2}) — (.+)$',text,re.M));assert len(parts)==21
end=text.index('## Add a future entry')
collections=[('Beauty & Jewelry',[2,3,5,9,11,16,17,18],'Intimate portraits, sculptural silver and luminous beauty.'),('Modern Wardrobe',[1,6,7,10,14,15],'Precise tailoring, confident silhouettes and effortless ease.'),('Resort & Heritage',[4,8,12,13,19,20,21],'Tactile fabrics, cinematic settings and archival fashion.')]
titles={int(m[1]):m[2] for m in parts}
front='''# Editorial Portrait Prompt Library

*THE PORTRAIT ATELIER · REFERENCE COLLECTION*

A curated collection of 21 photographic directions, from intimate beauty to heritage tailoring. Each editorial pairs its original reference with a complete, ready-to-copy image prompt.

> [!tip] Select · Attach · Copy
> Choose an editorial from the collection index, attach its reference image to your image generator, then copy the complete `text` block beneath **Copy the image prompt**. In Reading view, use the block’s copy control as shown in your screenshot; its visibility depends on your Obsidian theme. Paths and wiki links do not attach images automatically.

[[Attachments/Editorial Portraits/Editorial Portrait — Prompt.txt|Open the complete TXT edition]]

**Reference archive:** `/home/ivanaguilera/Pictures/Reference Images`  
**Collection established:** 8 October 2026 · **Layout refined:** 12 October 2026

---

## Collection Index

'''
for name,nums,description in collections:
 front+=f'### {name}\n\n*{description}*\n\n| Editorial | Direction |\n| :--- | :--- |\n'
 for n in nums:
  title=titles[n];front+=f'| {n:02d} | [[#'+f'{n:02d} — {title}|{title}]] |\n'
 front+='\n'
front+='> [!info]- Reference and generation notes\n> Original references are preserved unchanged inside the vault. Entries 01–05 include existing generated results and their original provenance; entries 06–21 contain prepared prompts without generated results. Expand an editorial’s archive for analysis, filenames, hashes, adaptations and settings notes.\n\n---\n\n'
output=[front]
for i,m in enumerate(parts):
 section=text[m.end():parts[i+1].start() if i+1<len(parts) else end].strip()
 blocks=re.findall(r'```text\n[\s\S]*?\n```',section);assert len(blocks)==1,(m[1],len(blocks))
 embed=re.search(r'!\[\[[^\n]+\]\]',section);assert embed
 reference=embed[0]
 # Remove only the exposed original embed and prompt section; retain all historical detail.
 detail=section.replace(reference,'',1)
 detail=re.sub(r'^### (?:Exact[^\n]*|Full professional image prompt)\n\n'+re.escape(blocks[0]),'',detail,flags=re.M)
 assert blocks[0] not in detail
 detail=re.sub(r'\n{3,}','\n\n',detail).strip()
 detail=re.sub(r'^### Original reference\s*\n','',detail)
 detail=re.sub(r'^### (.+)$',r'**\1**',detail,flags=re.M)
 group=next(name for name,nums,_ in collections if int(m[1]) in nums)
 output.append(f'## {m[1]} — {m[2]}\n\n*{group.upper()} · EDITORIAL {m[1]}*\n\n### Reference Image\n\n{reference}\n\n### Copy the image prompt\n\n{blocks[0]}\n\n> [!info]- Editorial archive · analysis, provenance & reference details\n'+ '\n'.join('> '+line if line else '>' for line in detail.splitlines())+'\n\n[[#Collection Index|Return to the collection index]]\n\n---\n\n')
output.append('''## Add a future entry

Use the next editorial number and a descriptive title. Place the original reference first, followed by **Copy the image prompt** and one visible fenced `text` block containing only the complete prompt. Add analysis, filenames, provenance, requested format, deliberate adaptations and any settings notes in a collapsible archive callout. Keep unchanged reference copies in `Attachments/Editorial Portraits`, organize originals in `Pictures/Reference Images`, and update the collection index and TXT edition.
''')
result=''.join(output)
assert re.findall(r'```text\n([\s\S]*?)\n```',text)==re.findall(r'```text\n([\s\S]*?)\n```',result),'Prompt text changed'
assert sorted(re.findall(r'!\[\[([^\n]+)\]\]',text))==sorted(re.findall(r'!\[\[([^\n]+)\]\]',result)),'Image references changed'
for target in re.findall(r'!\[\[([^]|]+)',result):assert (v/target).exists(),target
anchors=set(re.findall(r'^## (.+)$',result,re.M))
for anchor in re.findall(r'\[\[#([^|]+)\|',result):assert anchor in anchors,anchor
(t/'staged').mkdir(exist_ok=True);(t/'backup').mkdir(exist_ok=True)
(t/'staged'/p.name).write_text(result);shutil.copy2(p,t/'backup'/p.name)
assert p.read_bytes()==original,'Live note changed during staging'
shutil.copy2(t/'staged'/p.name,p)
assert p.read_text()==result
print('Redesigned 21 editorials; all 21 prompt blocks unchanged, 26 image embeds preserved, index anchors verified. Backup: '+str(t/'backup'/p.name))
