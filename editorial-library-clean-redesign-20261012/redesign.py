from pathlib import Path
import re,shutil
v=Path('/home/ivanaguilera/Documents/Obsidian Vault');p=v/'Editorial Portrait Prompt Library.md';t=Path('/home/ivanaguilera/Work/editorial-library-clean-redesign-20261012');archive=v/'Editorial Portrait Reference Archive.md'
old=p.read_bytes();s=old.decode();matches=list(re.finditer(r'^## (\d{2}) — (.+)$',s,re.M));assert len(matches)==21;assert not archive.exists()
front='''# Editorial Portrait Prompt Library

21 reference studies for professional fashion and beauty photography.

Attach the reference image, then copy the complete prompt from its text block. Use the block’s copy control in Reading view.

[[Attachments/Editorial Portraits/Editorial Portrait — Prompt.txt|Text edition]] · [[Editorial Portrait Reference Archive|Reference details and generation history]]

## Index

| No. | Editorial |\n| :--- | :--- |\n'''
for m in matches:front+=f'| {m[1]} | [[#{m[1]} — {m[2]}|{m[2]}]] |\n'
front+='\n---\n\n';out=[front];details=['# Editorial Portrait Reference Archive\n\nSource files, visual analysis, adaptations and generation history for the [[Editorial Portrait Prompt Library|prompt library]]. Original images are organized in `/home/ivanaguilera/Pictures/Reference Images`.\n\n']
for i,m in enumerate(matches):
 sec=s[m.end():matches[i+1].start() if i+1<len(matches) else s.index('## Add a future entry')]
 block=re.search(r'```text\n[\s\S]*?\n```',sec)[0];image=re.search(r'!\[\[[^\n]+\]\]',sec)[0]
 lines=sec.splitlines();start=next(j for j,l in enumerate(lines) if l.startswith('> [!info]- Editorial archive'))
 archived=[]
 for line in lines[start+1:]:
  if line.startswith('> '):archived.append(line[2:])
  elif line=='>':archived.append('')
  else:break
 detail='\n'.join(archived).strip()
 brief=re.search(r'\*\*Recognition:\*\* (.+)',detail)
 if brief:brief=brief[1]
 else:
  analysis=re.search(r'\*\*Image analysis and luxury direction\*\*\s*\n\n([^\n]+)',detail)
  brief=analysis[1] if analysis else ''
 # A short descriptive caption belongs with the image; the full analysis remains in the archive.
 if len(brief)>210:brief=brief.split('. ')[0].rstrip('.')+'.'
 out.append(f'## {m[1]} — {m[2]}\n\n{image}\n\n'+(f'{brief}\n\n' if brief else '')+f'### Prompt\n\n{block}\n\n[[Editorial Portrait Reference Archive#{m[1]} — {m[2]}|Reference details]] · [[#Index|Back to index]]\n\n---\n\n')
 details.append(f'## {m[1]} — {m[2]}\n\n{detail}\n\n[[Editorial Portrait Prompt Library#{m[1]} — {m[2]}|Open image and prompt]]\n\n---\n\n')
result=''.join(out).rstrip()+'\n';record=''.join(details).rstrip()+'\n'
assert re.findall(r'```text\n([\s\S]*?)\n```',s)==re.findall(r'```text\n([\s\S]*?)\n```',result)
assert sorted(re.findall(r'!\[\[([^\n]+)\]\]',s))==sorted(re.findall(r'!\[\[([^\n]+)\]\]',result+record))
for link in re.findall(r'!\[\[([^]|]+)',result+record):assert (v/link).exists()
for content in [result,record]:assert '[!info]' not in content and '[!tip]' not in content
(t/'backup').mkdir(exist_ok=True);(t/'staged').mkdir(exist_ok=True);shutil.copy2(p,t/'backup'/p.name)
(t/'staged'/p.name).write_text(result);(t/'staged'/archive.name).write_text(record)
assert p.read_bytes()==old
archive.write_text(record);p.write_text(result)
assert p.read_text()==result and archive.read_text()==record
print('Saved clean catalog and separate reference archive. All 21 copy blocks unchanged; all 26 image embeds preserved. Prior layout backed up.')
