from pathlib import Path
import hashlib,json,re
base=Path(__file__).resolve().parent
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
for folder in ['backup','staged']:(base/folder).mkdir(exist_ok=True)
new='China — ChatGPT Project Prompts.md'
assert not (vault/new).exists(),new
manifest={new:None}
(base/'staged'/new).write_bytes((base/new).read_bytes())
names=['China — Start Here.md','Trip Planning Prompt Library.md','China — Session Recap 2026-10-08.md']
for name in names:
    data=(vault/name).read_bytes()
    (base/'backup'/name).write_bytes(data)
    manifest[name]=hashlib.sha256(data).hexdigest()
    text=data.decode()
    if name=='China — Start Here.md':
        anchor='## First route to compare'
        assert text.count(anchor)==1
        text=text.replace(anchor,'**ChatGPT project:** [[China — ChatGPT Project Prompts|17 copy-ready planning prompts]] — routes, research, costs, preparation, and bringing decisions back to Obsidian.\n\n'+anchor)
    elif name=='Trip Planning Prompt Library.md':
        anchor='[[Japan 2027 — Start Here|Japan dashboard]] · [[Korea 2026 — Start Here|Korea dashboard]]'
        assert text.count(anchor)==1
        text=text.replace(anchor,anchor+'\n\n**China project:** [[China — ChatGPT Project Prompts|China prompt library — 17 prompts]] · [[China — Start Here|China dashboard]]')
    else:
        text+='''\n## ChatGPT project and prompt library — same day

Prepared a ChatGPT project pack in `/home/ivanaguilera/Work/china-chatgpt-project-20261008/`: five upload sources representing ten live China notes, project instructions, setup guide, and first-message prompt. User reported creating the project; account uploads and instruction settings were not independently checked. Snapshots and the live vault do not synchronize automatically.

Following the request for prompts in Obsidian, added [[China — ChatGPT Project Prompts]] with 17 copy-ready prompts and a reusable dated-research add-on. Linked from Start Here and the existing Trip Planning Prompt Library. Prompt topics cover route/timing, itinerary, food/tea, shops/gifts, photography, excursions, experiences, flights/rail, hotels, budget, preparation, Amap, supplied confirmations, and decision updates.

Backups/staged prompt updates: `/home/ivanaguilera/Work/china-project-prompts-20261008/`. No provider facts were refreshed in this prompt-writing task. Next: use the first-chat and route prompts, record priorities and timing, then refresh the affected project source snapshots after material decisions. No trip dates, budget, travelers, reservations, phone tests, or app setup were confirmed by this work.
'''
    (base/'staged'/name).write_text(text)
(base/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Prepared one new prompt note, three focused updates, and backups.')
