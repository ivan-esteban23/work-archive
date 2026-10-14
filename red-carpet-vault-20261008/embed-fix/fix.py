from pathlib import Path
import hashlib,shutil
root=Path('/home/ivanaguilera/Work/red-carpet-vault-20261008/embed-fix')
live=Path('/home/ivanaguilera/Documents/Obsidian Vault/Editorial Portrait Prompt Library.md')
old=live.read_bytes();text=old.decode()
broken='''### Reference and generated result

| Original reference | Generated result |
| --- | --- |
| ![[Attachments/Editorial Portraits/05 — Red Carpet Gold — Original.jpeg|300]] | ![[Attachments/Editorial Portraits/Red Carpet Gold — Beauty Portrait.png|300]] |'''
fixed='''### Original reference

![[Attachments/Editorial Portraits/05 — Red Carpet Gold — Original.jpeg|450]]

### Generated result

![[Attachments/Editorial Portraits/Red Carpet Gold — Beauty Portrait.png|450]]'''
assert text.count(broken)==1
updated=text.replace(broken,fixed,1)
(root/'before.md').write_bytes(old)
(root/'updated.md').write_text(updated)
(root/'expected.sha256').write_text(hashlib.sha256(old).hexdigest())
print('Prepared standalone image embeds matching the working entries.')
