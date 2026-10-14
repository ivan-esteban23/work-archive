from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
for name in ['staged','backup']:(base/name).mkdir(exist_ok=True)
actions=[]
def stage(target,text,source=None):
    path=Path(target)
    original=Path(source) if source else path
    expected=None
    if original.exists():
        data=original.read_bytes()
        expected=hashlib.sha256(data).hexdigest()
        backup_name=str(len(actions))+'-'+original.name
        (base/'backup'/backup_name).write_bytes(data)
    if source:assert not path.exists(),path
    stage_name=str(len(actions))+'-'+path.name
    (base/'staged'/stage_name).write_text(text)
    actions.append(dict(target=str(path),source=str(original),expected=expected,staged=stage_name,move=source is not None))
for name in ['Music Prompt Library.md','Music Project Starter Template.md']:
    target=vault/'Music Prompts'/name
    assert not target.exists(),target
    stage(target,(base/name).read_text())
for name in ['Death Metal — ChatGPT Project Prompts.md','Death Metal — ChatGPT Project Instructions.md']:
    source=vault/name
    text=source.read_text()
    lines=text.splitlines(keepends=True)
    assert lines[0].startswith('# ')
    lines.insert(2,'[[Music Prompt Library|Music prompt index]]\n\n')
    stage(vault/'Music Prompts'/name,''.join(lines),source)
p=vault/'Death Metal — Start Here.md'
text=p.read_text()
anchor='## Start listening'
assert text.count(anchor)==1
text=text.replace(anchor,'**Music prompt hub:** [[Music Prompt Library]] — reusable prompts and templates for future music projects.\n\n'+anchor)
stage(p,text)
p=vault/'Death Metal — Research and Sources 2026-10-08.md'
stage(p,p.read_text()+'''\n## Music prompt folder — same day

User requested a dedicated vault directory for prompts as future music projects are created. Added **Music Prompts** with [[Music Prompt Library]], eleven reusable music prompts, and [[Music Project Starter Template]]. Moved the existing Death Metal prompt and instruction notes into this folder, preserving their note names and content apart from index navigation. Linked the new hub from the Death Metal dashboard. Research notes and the listening journal remain in their current locations.

Recorded the future music prompt location in workspace instructions. Backups and staged updates: `/home/ivanaguilera/Work/music-prompts-folder-20261008/`. Existing ChatGPT uploads are unchanged snapshots; this folder operation does not update the app. No music research was refreshed, and no plugins or vault settings were changed.
''')
p=Path('/home/ivanaguilera/Work/AGENTS.md')
text=p.read_text()
assert '## Music projects and prompt organization' not in text
stage(p,text+'''\n## Music projects and prompt organization

The user wants a separate ChatGPT research/listening project for each music topic and a shared prompt directory in the live Obsidian vault.

- Music prompt directory: `/home/ivanaguilera/Documents/Obsidian Vault/Music Prompts`
- Shared index: `Music Prompt Library.md` in that directory
- New-project template: `Music Project Starter Template.md` in that directory
- Keep topic prompt and project-instruction notes in this directory, using `[Topic] — ChatGPT Project Prompts.md` and `[Topic] — ChatGPT Project Instructions.md`; link them from the shared index and the topic's dashboard.
- Keep music topics' research, listening feedback, and personal rankings separate from each other and from travel projects. Do not infer that an album was heard or personally rated.
- ChatGPT uploads are snapshots and do not automatically synchronize with Obsidian. Preserve existing note names, links, and sources; back up existing notes before changes, use normal filesystem escalation when required, and read back saved updates. Do not alter `.obsidian` settings for ordinary note work.
''')
(base/'manifest.json').write_text(json.dumps(actions,ensure_ascii=False,indent=2))
print('Prepared two new notes, two preserved-name moves, two navigation/recap updates, and workspace organization guidance; originals backed up.')
