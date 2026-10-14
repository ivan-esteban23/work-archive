from pathlib import Path
import hashlib
import re
stage=Path('/home/ivanaguilera/Work/china-guide-build-20261008/staged')
vault=Path('/home/ivanaguilera/Documents/Obsidian Vault')
files=sorted(stage.glob('*.md'))
conflicts=[p.name for p in files if (vault/p.name).exists()]
if conflicts:
    raise SystemExit('Stopped to preserve existing notes: '+', '.join(conflicts))
for p in files:
    with (vault/p.name).open('xb') as handle:
        handle.write(p.read_bytes())
for p in files:
    saved=(vault/p.name).read_bytes()
    assert saved==p.read_bytes(),p.name
    for link in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]',saved.decode()):
        assert (vault/(link.split('#')[0]+'.md')).exists(),link
    print('Saved and verified:',p.name)
