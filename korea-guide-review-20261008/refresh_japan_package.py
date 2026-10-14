from pathlib import Path
import shutil,hashlib,json
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
OUT=Path('/home/ivanaguilera/Work/japan-guide-update/chatgpt-project')
BACKUP=ROOT/'backup'/'japan-project'
BACKUP.mkdir(parents=True,exist_ok=True)
for name in ['README.md','Project instructions.txt']:
    if (OUT/name).exists(): shutil.copy2(OUT/name,BACKUP/name)
brief='''# Japan — Current Planning Brief, 8 October 2026

Read this file and the latest user instructions before historical route examples. Season and month remain undecided; flight searches are tests. Nothing is booked. Existing 2027 filenames and the March 25–April 8 sample do not select dates. Traveler count, rooms and passport nationality remain unresolved for Japan; do not import the confirmed Korea profile into this project without confirmation.

The original fourteen-night Tokyo 6 + Kyoto 6 + Tokyo 2 model is one example. Its US$3,850 allocation plus US$1,150 reserve and the alternate US$4,100 plus US$900 reserve each total US$5,000 excluding flights. They are separate scenarios, not cumulative spending.

The following notes were read from the live vault for this export. The complete snapshot contains historical content as well; current preparation guidance and latest user choices take precedence.
'''
for name in ['Japan 2027 — Start Here.md','Japan 2027 — Preparation Before Choosing Dates.md','Japan 2027 — Session Recap 2026-10-08.md']:
    brief+='\n\n---\n\n'+(VAULT/name).read_text()
(OUT/'Japan — Current Planning Brief 2026-10-08.md').write_text(brief)
notes=sorted(VAULT.glob('Japan*.md'))
snapshot='''JAPAN — COMPLETE VAULT SNAPSHOT, 8 OCTOBER 2026

This is a local snapshot, not an upload or live synchronization. Historical dates, prices and recaps do not override Japan — Current Planning Brief 2026-10-08.md or the user's latest instructions. All Japan Markdown notes are included; map coordinates and unresolved venue leads retain their original limitations. No Korea notes or Obsidian settings are included. This export does not imply every historical claim was newly rechecked today.
'''
manifest=[]
for p in notes:
    snapshot+='\n\n'+'='*60+'\nSOURCE NOTE: '+p.name+'\n'+'='*60+'\n\n'+p.read_text()
    manifest.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
name='Japan — Complete Vault Snapshot 2026-10-08.txt'
(OUT/name).write_text(snapshot)
assert all(p.read_text() in (OUT/name).read_text() for p in notes)
(OUT/'snapshot-manifest-2026-10-08.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
instructions=(OUT/'Project instructions.txt').read_text()
(OUT/'Project instructions.txt').write_text('''Current context, 8 October 2026: season and month undecided, flight searches are tests, no bookings. The 2027 label and March dates are provisional. Japan — Current Planning Brief 2026-10-08.md and latest user instructions override older worksheets or recaps. Do not import Korea's confirmed solo/nationality/budget profile into Japan automatically. Keep the two trips separate.

'''+instructions)
(OUT/'README.md').write_text('''# Japan Trip — refreshed ChatGPT source package

Updated 8 October 2026 from the live Obsidian vault. Saved locally; no native ChatGPT project was created or modified and nothing was uploaded.

1. Use a separate **Japan Trip** project (or your existing Japan project).
2. Add `Japan — Current Planning Brief 2026-10-08.md` and `Japan 2027 — Travel Essay and Verified Sources.txt` to Sources.
3. Optionally add `Japan — Complete Vault Snapshot 2026-10-08.txt` for all current Japan Markdown notes. Treat historical examples as provisional and the current brief as authoritative.
4. Paste `Project instructions.txt` into project instructions.
5. Start a project chat: “Compare seasons and preparation needs before choosing my Japan dates. Treat flights as test searches and confirm traveler count and nationality before personal entry advice.”

The older six topical files and Complete Guide file dated 7 October remain historical exports and are not the current upload set. Do not upload both complete copies. Existing export.py assumes exactly 64 notes and an older recap; it has not been rerun. Today's new snapshot was produced with a dynamic inventory and includes the current preparation and recap notes. Refresh exports after subsequent vault edits; uploaded copies do not sync automatically.

[Official ChatGPT project guidance](https://learn.chatgpt.com/docs/projects). Keep Korea in a separate project.
''')
print('Refreshed Japan package: '+str(len(notes))+' notes; '+str(len(snapshot.encode()))+' bytes; local only.')
