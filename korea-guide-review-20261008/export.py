from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
VAULT=Path('/home/ivanaguilera/Documents/Obsidian Vault')
OUT=ROOT/'chatgpt-project'
def text(name):
    p=ROOT/'staged'/('Korea 2026 — '+name+'.md')
    if not p.exists(): p=VAULT/p.name
    return p.read_text()
brief='# South Korea — Current Planning Brief and Verified Sources\n\nSnapshot 8 October 2026. Current user decisions and the following active sections take precedence over older worksheets, pocket cards and recaps. Nothing is booked. Season, month, year and length remain open. Flight prices are test-search snapshots.\n\n'
for name in ['Preparation Before Choosing Dates','Solo Plan','Budget','Flights and Stays','Places Shortlist','Fitness and Protein','Departure Checklist','Review and Sources 2026-10-08']:
    content=text(name)
    if name=='Budget': content=content.split('## Historical worksheet')[0]
    brief+='\n\n---\n\n'+content
(OUT/'Korea — Current Planning Brief and Verified Sources.md').write_text(brief)
allnotes={p.name:p.read_text() for p in VAULT.glob('Korea*.md')}
allnotes.update({p.name:p.read_text() for p in (ROOT/'staged').glob('*.md')})
snapshot='# South Korea — All Guide Notes Snapshot\n\nSnapshot 8 October 2026. Includes all 33 existing reviewed notes and 4 new notes. Historical 6-night/two-traveler/no-meat drafts and old shopping allocations DO NOT override the current planning brief, confirmed solo profile, unrestricted diet, US$80 shopping allocation or latest user instructions. Filenames retain 2026 for link compatibility; travel year remains open. No map plugin rendering or live vault synchronization is included.\n'
for name,content in sorted(allnotes.items()): snapshot+='\n\n---\n\nSOURCE NOTE: '+name+'\n\n'+content
(OUT/'Korea — All Guide Notes Snapshot.md').write_text(snapshot)
print('Exported '+str(len(allnotes))+' notes; current brief '+str(len(brief))+' characters.')
