from pathlib import Path
import shutil

root = Path('/home/ivanaguilera/Work/japan-guide-update/preparation-20261008')
backup = root / 'backup' / 'workspace'
backup.mkdir(exist_ok=True)

def update(path, transform):
    before = path.read_text()
    after = transform(before)
    assert before != after
    shutil.copy2(path, backup / path.name)
    assert path.read_text() == before
    path.write_text(after)
    assert path.read_text() == after

audit = Path('/home/ivanaguilera/Work/japan-guide-update/audit-20261008/Japan research audit.md')
def correct_audit(s):
    s = s.replace('There is a missing rail-price qualification, an inherited flight-search date mismatch, and several tour-description differences that need clearer interpretation.', 'There is a missing rail-price qualification and several tour-description differences that need clearer interpretation. The user subsequently clarified that differing flight-search dates were exploratory tests, not a selected itinerary.')
    a = s.index('| Previous flight search does not match the stay dates |')
    b = s.index('\n', a)
    s = s[:a] + '| Flight searches were exploratory tests — user clarification | On 8 October the user confirmed that no season/month was chosen and earlier flight searches were tests. Different test dates are not evidence of a planning error. | Preserve tests as labeled scenarios. Ensure local departure/arrival dates agree when comparing an actual route. No new flight quote was obtained in this audit. |' + s[b:]
    s += '\n## Subsequent clarification and continuation · 8 October 2026\n\nThe user confirmed that season/month are open and requested more internet research. The original flight-mismatch interpretation above has been corrected. The live dashboard now links to `Japan 2027 — Preparation Before Choosing Dates.md`, and a new 8 October recap records the work. The seasonal guide uses a separate US$4,100 + US$900 reserve example, while the blossom model uses US$3,850 + US$1,150. These are route scenarios, not contradictory totals. The earlier statement that vault notes and the essay were unchanged describes the audit-only turn; targeted context updates were made during this subsequent continuation.\n'
    return s
update(audit, correct_audit)

essay = Path('/home/ivanaguilera/Work/japan-guide-update/chatgpt-project/Japan 2027 — Travel Essay and Verified Sources.txt')
def correct_essay(s):
    s = s.replace('Research checked: 7 October 2026\n', 'Research checked: 7 October 2026\nPlanning context clarified: 8 October 2026; rail-pass purchase-channel detail rechecked 8 October 2026. Other source checks retain their original date.\n')
    s = s.replace('The proposed stay remains arrival in Japan on 25 March and departure on 8 April 2027:', 'The user clarified on 8 October that the travel season/month remain undecided and earlier flight searches were exploratory tests. The following spring journey is one comparison scenario, not the chosen travel window. The sample stay uses arrival in Japan on 25 March and departure on 8 April 2027:')
    s = s.replace('On the research date, the official JAPAN RAIL PASS site listed adult Ordinary passes at ¥50,000 for seven days and ¥80,000 for fourteen days.', 'On the 8 October recheck, the official JAPAN RAIL PASS site distinguished online adult Ordinary prices of ¥50,000 for seven days and ¥80,000 for fourteen days from overseas designated-agency prices of ¥53,000 and ¥84,000 respectively.')
    s = s.replace('Before turning this essay into reservations, confirm travelers, passport nationality, local flight dates, rooms, and budget scope.', 'Before turning this essay into reservations, choose a season and confirm travelers, passport nationality, local flight dates, rooms, and budget scope.')
    return s
update(essay, correct_essay)
print('Updated and read back audit clarification and local essay; originals backed up.')
