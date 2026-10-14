from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
import hashlib, json, re, shutil, sys

V = Path('/home/ivanaguilera/Documents/Obsidian Vault')
W = Path('/home/ivanaguilera/Work/japan-guide-update/island-maps')
NAME = 'Japan 2027 — Best Islands.md'
PLACES = [
 ('Miyajima', [('Itsukushima Shrine','Itsukushima Shrine Miyajima Hiroshima'),('Momijidani Park','Momijidani Park Miyajima Hiroshima'),('Mount Misen','Mount Misen Miyajima Hiroshima')], [('Miyajimaguchi ferry terminal','Miyajimaguchi ferry terminal Hiroshima'),('Miyajima ferry terminal','Miyajima ferry terminal Hiroshima')]),
 ('Naoshima', [('Chichu Art Museum','Chichu Art Museum Naoshima'),('Benesse House Museum','Benesse House Museum Naoshima'),('Honmura / Art House Project','Art House Project Honmura Naoshima')], [('Uno Port','Uno Port Tamano Okayama'),('Miyanoura Port','Miyanoura Port Naoshima Kagawa'),('Takamatsu Port','Takamatsu Port Kagawa')]),
 ('Shodoshima', [('Olive Park','Shodoshima Olive Park Kagawa'),('Kankakei Gorge','Kankakei Gorge Shodoshima Kagawa'),('Angel Road','Angel Road Shodoshima Kagawa')], [('Island overview — select the port for your actual ferry','Shodoshima Kagawa Japan')]),
 ('Yakushima', [('Shiratani Unsuikyo','Shiratani Unsuikyo Yakushima'),('Yakusugi Land','Yakusugi Land Yakushima')], [('Yakushima Airport','Yakushima Airport Kagoshima'),('Miyanoura Port','Miyanoura Port Yakushima Kagoshima')]),
 ('Ishigaki', [('Kabira Bay','Kabira Bay Ishigaki Okinawa'),('Tamatorizaki Observatory','Tamatorizaki Observatory Ishigaki Okinawa')], [('New Ishigaki Airport','New Ishigaki Airport Okinawa'),('Ishigaki ferry terminal','Ishigaki Port Remote Island Terminal Okinawa')]),
 ('Taketomi', [('Village area','Taketomi village Okinawa'),('Kondoi Beach','Kondoi Beach Taketomi Okinawa')], [('Taketomi Port','Taketomi Port Okinawa')]),
 ('Miyako', [('Miyako Island overview','Miyako Island Okinawa Japan'),('Irabu Island overview','Irabu Island Miyakojima Okinawa')], [('Miyako Airport — verify your actual arrival airport','Miyako Airport Okinawa')]),
 ('Enoshima', [('Enoshima Shrine','Enoshima Shrine Fujisawa'),('Sea Candle','Enoshima Sea Candle Fujisawa'),('Iwaya Caves','Enoshima Iwaya Caves Fujisawa')], [('Katase-Enoshima Station','Katase Enoshima Station Fujisawa')]),
 ('Sado', [('Shukunegi','Shukunegi Sado Niigata'),('Iwakubi rice terraces','Iwakubi rice terraces Sado Niigata')], [('Ryotsu Port','Ryotsu Port Sado Niigata'),('Ogi Port — verify seasonal service','Ogi Port Sado Niigata')]),
]

def links(items):
    return ' · '.join('['+label+'](https://www.google.com/maps/search/?'+urlencode({'api':'1','query':query})+')' for label,query in items)

rows = '\n'.join('| '+island+' | '+links(sights)+' | '+links(access)+' |' for island,sights,access in PLACES)
BLOCK = '''## Google Maps — sights and arrival points

Tap a place below to open a **Google Maps search**. These links are not verified Place IDs, saved lists, offline downloads, or live route checks. Confirm the result name and island before navigating, especially **Miyanoura**, which appears on both Naoshima and Yakushima. Island/village overview links orient you to an area rather than an exact entrance.

| Island | Places to visit / explore | Arrival and transport anchors |
| --- | --- | --- |
'''+rows+'''

**Use on the day:** select your actual hotel or starting point in Maps, then compare the proposed directions with the official ferry/bus timetable. A port pin does not establish that the required sailing operates. Confirm your airline's arrival airport on Miyako; the airport link above is one named airport, not an assumption about your flight. For forests and Mount Misen, use official trail maps and access notices alongside the location pin. Check the tide for Angel Road and the Miyajima waterfront; Kabira Bay remains a sightseeing stop with no beach swimming/snorkeling permitted.

'''

def validate(data):
    assert data.count('## Google Maps — sights and arrival points') == 1
    urls = re.findall(r'\]\((https://www.google.com/maps/search/\?[^)]+)\)',data)
    expected = sum(len(sights)+len(access) for _,sights,access in PLACES)
    assert len(urls) == expected
    for url in urls:
        query = parse_qs(urlparse(url).query)
        assert query['api'] == ['1'] and query['query'][0]
    for island,_,_ in PLACES: assert '| '+island+' |' in data
    print(f'Validated {expected} Google Maps links across {len(PLACES)} island entries.')

if '--install' in sys.argv:
    manifest = json.loads((W/'manifest.json').read_text())
    assert hashlib.sha256((V/NAME).read_bytes()).hexdigest() == manifest['original_sha256']
    staged = (W/'staged.md').read_text()
    validate(staged)
    shutil.copy2(V/NAME,W/'backup.md')
    shutil.copy2(W/'staged.md',V/NAME)
    assert (V/NAME).read_bytes() == (W/'staged.md').read_bytes()
    print('Saved island Maps section; original chapter backed up and installed bytes verified.')
else:
    W.mkdir(parents=True,exist_ok=True)
    original = (V/NAME).read_bytes()
    data = original.decode()
    assert '## Google Maps — sights and arrival points' not in data
    anchor = '## 1. Miyajima — my first choice for this guide'
    assert anchor in data
    data = data.replace(anchor,BLOCK+anchor,1)
    line = '[[Japan 2027 — Seasonal Guides|← Seasonal guides]]'
    data = data.replace(line,'[[#Google Maps — sights and arrival points|📍 Google Maps locations]] · '+line,1)
    validate(data)
    (W/'staged.md').write_text(data)
    (W/'manifest.json').write_text(json.dumps({'original_sha256':hashlib.sha256(original).hexdigest()}))
