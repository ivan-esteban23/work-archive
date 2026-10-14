from pathlib import Path
from shutil import copy2
p=Path('/home/ivanaguilera/Documents/Obsidian Vault/Japan 2027 — Travel Essentials.md')
s=p.read_text();marker='## 🛬 Arrival card — complete after booking'
assert marker in s and '## 📱 Visit Japan Web — prepare before flying' not in s
copy2(p,Path('/home/ivanaguilera/Work/japan-guide-update/Travel Essentials-before-arrival.md'))
s=s.replace(marker,'''## 📱 Visit Japan Web — prepare before flying

**Checked 6 October 2026; recheck terminal arrangements for 2027.** Online preparation reduces paperwork; it does not guarantee a short queue or replace immigration inspection.

1. Open [the official Visit Japan Web landing page](https://services.digital.go.jp/en/visit-japan-web/) and create an account.
2. Enter your traveler/passport information and the actual arrival flight and first accommodation details.
3. Complete the immigration and customs declarations and have the resulting arrival QR/2D code ready with your passport.
4. Keep the phone charged and save an offline copy of the code as a backup. Update the registration if flight or accommodation details change.

Visit Japan Web supports online arrival procedures. [Digital Agency explanation](https://www.digital.go.jp/en/policies/visit_japan_web)

### What happens after landing

Where integrated kiosks operate, scan your code and passport, complete the photo/fingerprint steps as instructed, and follow the displayed routing to the immigration booth. Collect luggage, then complete customs; eligible passengers may use a facial-recognition customs gate, while others are directed to an officer.

**Current integrated-kiosk locations relevant to your trip:** Haneda terminals **2 and 3**; Narita terminal **3**. The published list does not establish integrated-kiosk availability at Narita terminals 1 or 2. Check your actual arrival terminal and follow staff instructions. [Official terminal list](https://www.customs.go.jp/english/passenger/kiosk_2.pdf)

Integrated kiosks reduce duplicate data submission; dedicated immigration booths still involve inspection. Customs may require additional checks. **Do not plan an airport transfer around a guaranteed processing time.** [Official integrated-kiosk process](https://www.customs.go.jp/english/passenger/Pilot_kiosk.htm)

'''+marker,1)
p.write_text(s)
print('Saved Visit Japan Web preparation and terminal-specific arrival guidance.')
