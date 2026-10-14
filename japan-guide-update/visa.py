from pathlib import Path
from shutil import copy2
p=Path('/home/ivanaguilera/Documents/Obsidian Vault/Japan 2027 — Travel Essentials.md')
s=p.read_text()
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Travel Essentials-before-visa.md'))
marker='## 🛬 Arrival card — complete after booking'
assert marker in s and '## 🛂 Visa check — passport confirmation pending' not in s
s=s.replace(marker,'''## 🛂 Visa check — passport confirmation pending

**Checked 6 October 2026. Traveler passport nationality and type remain unconfirmed.**

**If traveling on an ordinary Chilean passport for tourism:** Chile appears on Japan’s current visa-exemption list, with a usual short-stay period of up to **90 days**. The proposed 14-night holiday fits that duration. Exemption covers eligible short visits without remunerated professional activity in Japan; it is not permission to work. [Japan MOFA exemption list](https://www.mofa.go.jp/j_info/visit/visa/short/novisa.html) · [Embassy in Chile visa guidance](https://www.cl.emb-japan.go.jp/itpr_ja/procedimientodevisado.html)

**Documents recommended by the Embassy of Japan in Chile:** a valid passport with at least six months remaining, return-flight evidence, and printed accommodation confirmations covering the stay. It also recommends insurance and evidence of financial means. Its approximate US$100/day figure is document-preparation guidance, not a fee or a replacement for your budget. Confirm directly with the embassy if passport validity is close to that recommendation. [Embassy’s visa-exempt traveler checklist](https://www.cl.emb-japan.go.jp/itpr_ja/exencion.html)

- [ ] Confirm the passport country and type for every traveler; do not use Chilean residence as proof of eligibility.
- [ ] Confirm tourism purpose and the actual dates; recheck rules before booking and departure in 2027.
- [ ] Check passport expiry against embassy guidance and the chosen transit route.
- [ ] Save return/onward travel evidence and accommodation confirmations.
- [ ] Check **transit requirements separately** after choosing connection countries and airports.

Visit Japan Web handles arrival procedures; it is not a visa application or a substitute for visa eligibility. Your personal visa status remains pending passport confirmation.

'''+marker,1)
p.write_text(s)
print('Saved conditional visa findings and embassy document checklist; passport confirmation remains pending.')
