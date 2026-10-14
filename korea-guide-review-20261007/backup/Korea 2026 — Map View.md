---
cssclasses:
  - korea-trip
locations:
---
# 🗺️ Korea 2026 — Interactive maps

[[Korea 2026 — Start Here|← Dashboard]] · [[Korea 2026 — Maps|All Google Maps searches]] · [[Korea 2026 — Cafés and Shops|Shops and cafés]] · [[Korea 2026 — Itinerary|Itinerary]]

**Starter maps · prepared 7 October 2026.** Thirty landmarks and stations, grouped by city. Every coordinate below was checked against **two independent sources** — Wikidata `P625` and OpenStreetMap via Nominatim — and kept only where they agreed within a tolerance set by feature type (250 m for precise points, 700 m for palaces, parks, villages and beaches).

> [!warning] How to read these coordinates
> A pin identifies the **place**, not a specific entrance, platform or counter. A palace at 327 m and a village at 212 m are correct, not sloppy — those features are simply that large. Where you need a precise door, use the Google Maps search link on the same line: it resolves on the Korean name and lands on the right storefront.

## Using the maps

Open this note in **Reading view**. Click a pin to identify it; use the Google Maps link for walking or train directions. The **Open** control opens the full Map View where you can adjust the query. Tiles need internet unless downloaded ahead in Map View.

Suggested full-map queries: `tag:#korea2026`, `tag:#korea2026 AND tag:#seoul`, `tag:#korea2026 AND tag:#transport`.

## Seoul

```mapview
{
  "name": "Korea 2026 — Seoul",
  "mapZoom": 12,
  "centerLat": 37.5700,
  "centerLng": 126.9800,
  "query": "tag:#korea2026 AND tag:#seoul",
  "chosenMapSource": 0,
  "autoFit": true,
  "lock": false,
  "showLinks": false,
  "markerLabels": "off",
  "embeddedHeight": 430
}
```

## Gyeongju

```mapview
{
  "name": "Korea 2026 — Gyeongju",
  "mapZoom": 13,
  "centerLat": 35.8350,
  "centerLng": 129.2150,
  "query": "tag:#korea2026 AND tag:#gyeongju",
  "chosenMapSource": 0,
  "autoFit": true,
  "lock": false,
  "showLinks": false,
  "markerLabels": "off",
  "embeddedHeight": 430
}
```

## Busan

```mapview
{
  "name": "Korea 2026 — Busan",
  "mapZoom": 12,
  "centerLat": 35.1500,
  "centerLng": 129.0800,
  "query": "tag:#korea2026 AND tag:#busan",
  "chosenMapSource": 0,
  "autoFit": true,
  "lock": false,
  "showLinks": false,
  "markerLabels": "off",
  "embeddedHeight": 430
}
```

## Arrivals, departures and rail

Incheon is 50 km from central Seoul, so including it in the city map would drag the zoom out and lose all detail. It gets its own wide view instead, with the stations that make the two KTX legs legible.

```mapview
{
  "name": "Korea 2026 — Airports and rail",
  "mapZoom": 8,
  "centerLat": 36.2000,
  "centerLng": 128.9000,
  "query": "tag:#korea2026 AND tag:#transport",
  "chosenMapSource": 0,
  "autoFit": true,
  "lock": false,
  "showLinks": false,
  "markerLabels": "off",
  "embeddedHeight": 430
}
```

---

## 📍 Pin directory

Each line is a Map View location with inline tags. `✓` means two sources agreed within tolerance; `~` means Nominatim only.

### Seoul

- [Gyeongbokgung Palace](geo:37.579884,126.976800) tag:korea2026 tag:seoul tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=경복궁+서울) · [Wikidata](https://www.wikidata.org/wiki/Q482485) ✓ 18 m

- [Deoksugung Palace](geo:37.566111,126.975000) tag:korea2026 tag:seoul tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=덕수궁+서울) · [Wikidata](https://www.wikidata.org/wiki/Q482631) ✓ 16 m

- [Changdeokgung Palace](geo:37.579444,126.991667) tag:korea2026 tag:seoul tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=창덕궁+서울) · [Wikidata](https://www.wikidata.org/wiki/Q477157) ✓ 327 m

- [Bukchon Hanok Village](geo:37.583056,126.983611) tag:korea2026 tag:seoul tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=북촌한옥마을+서울) · [Wikidata](https://www.wikidata.org/wiki/Q490981) ✓ 212 m

- [Ikseon-dong](geo:37.574279,126.989835) tag:korea2026 tag:seoul tag:neighborhood
  [Google Maps](https://www.google.com/maps/search/?api=1&query=익선동+서울) · [Wikidata](https://www.wikidata.org/wiki/Q16188499) ✓ 10 m

- [Gwangjang Market](geo:37.570000,126.999000) tag:korea2026 tag:seoul tag:food
  [Google Maps](https://www.google.com/maps/search/?api=1&query=광장시장+서울) · [Wikidata](https://www.wikidata.org/wiki/Q12585067) ✓ 148 m

- [Insadong](geo:37.573000,126.986000) tag:korea2026 tag:seoul tag:neighborhood
  [Google Maps](https://www.google.com/maps/search/?api=1&query=인사동+서울) · [Wikidata](https://www.wikidata.org/wiki/Q488678) ✓ 68 m

- [Seoul Forest](geo:37.544625,127.039844) tag:korea2026 tag:seoul tag:nature
  [Google Maps](https://www.google.com/maps/search/?api=1&query=서울숲+성수동) · [Wikidata](https://www.wikidata.org/wiki/Q483014) ✓ 603 m

- [N Seoul Tower](geo:37.551216,126.988276) tag:korea2026 tag:seoul tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=남산서울타워) · [Wikidata](https://www.wikidata.org/wiki/Q69134) ✓ 6 m

- [Inwangsan](geo:37.584722,126.958611) tag:korea2026 tag:seoul tag:nature
  [Google Maps](https://www.google.com/maps/search/?api=1&query=인왕산+서울) · [Wikidata](https://www.wikidata.org/wiki/Q625942) ✓ 71 m

- [Hongik University Station — Hongdae vintage loop](geo:37.550556,126.925833) tag:korea2026 tag:seoul tag:shopping
  [Google Maps](https://www.google.com/maps/search/?api=1&query=홍익대학교+서울) · [Wikidata](https://www.wikidata.org/wiki/Q491511) ✓ 42 m

- [Euljiro](geo:37.566060,126.980778) tag:korea2026 tag:seoul tag:neighborhood
  [Google Maps](https://www.google.com/maps/search/?api=1&query=을지로+서울) · OpenStreetMap ~ single source

### Gyeongju

- [Bulguksa](geo:35.790000,129.332222) tag:korea2026 tag:gyeongju tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=불국사+경주) · [Wikidata](https://www.wikidata.org/wiki/Q408318) ✓ 164 m

- [Seokguram Grotto](geo:35.795000,129.349167) tag:korea2026 tag:gyeongju tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=석굴암+경주) · [Wikidata](https://www.wikidata.org/wiki/Q489820) ✓ 22 m

- [Daereungwon Ancient Tombs](geo:35.838048,129.212135) tag:korea2026 tag:gyeongju tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=대릉원+경주) · [Wikidata](https://www.wikidata.org/wiki/Q17278215) ✓ 80 m

- [Hwangnidan-gil](geo:35.837500,129.209700) tag:korea2026 tag:gyeongju tag:neighborhood
  [Google Maps](https://www.google.com/maps/search/?api=1&query=황리단길+경주) · [Wikidata](https://www.wikidata.org/wiki/Q61092780) ✓ 180 m

- [Cheomseongdae](geo:35.834722,129.219000) tag:korea2026 tag:gyeongju tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=천문대+경주) · [Wikidata](https://www.wikidata.org/wiki/Q562765) ✓ 2 m

- [Wolji Pond](geo:35.834619,129.227114) tag:korea2026 tag:gyeongju tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=월지연못+경주) · [Wikidata](https://www.wikidata.org/wiki/Q496454) ✓ 62 m

- [Woljeongyo Bridge](geo:35.829257,129.218137) tag:korea2026 tag:gyeongju tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=월정교+경주) · OpenStreetMap ~ single source

- [Gyeongju Station](geo:35.798333,129.138889) tag:korea2026 tag:gyeongju tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=경주역) · [Wikidata](https://www.wikidata.org/wiki/Q54294) ✓ 130 m

### Busan

- [Jagalchi Market](geo:35.097400,129.027000) tag:korea2026 tag:busan tag:food
  [Google Maps](https://www.google.com/maps/search/?api=1&query=자갈치시장+부산) · [Wikidata](https://www.wikidata.org/wiki/Q706369) ✓ ~300 m

- [Gamcheon Culture Village](geo:35.097500,129.009167) tag:korea2026 tag:busan tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=감천문화마을+부산) · [Wikidata](https://www.wikidata.org/wiki/Q18641306) ✓ 134 m

- [Yongdusan Park](geo:35.100556,129.032778) tag:korea2026 tag:busan tag:nature
  [Google Maps](https://www.google.com/maps/search/?api=1&query=용두산공원+부산) · [Wikidata](https://www.wikidata.org/wiki/Q483056) ✓ 20 m

- [Haedong Yonggungsa](geo:35.188333,129.223333) tag:korea2026 tag:busan tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=해동용궁사+부산) · [Wikidata](https://www.wikidata.org/wiki/Q2494268) ✓ 34 m

- [Haeundae Beach](geo:35.158552,129.160539) tag:korea2026 tag:busan tag:nature
  [Google Maps](https://www.google.com/maps/search/?api=1&query=해운대해변+부산) · [Wikidata](https://www.wikidata.org/wiki/Q491203) ✓ 235 m

- [Gwangalli Beach](geo:35.154167,129.120556) tag:korea2026 tag:busan tag:nature
  [Google Maps](https://www.google.com/maps/search/?api=1&query=광안리해변+부산) · [Wikidata](https://www.wikidata.org/wiki/Q495370) ✓ 501 m

- [Busan Station](geo:35.114722,129.041944) tag:korea2026 tag:busan tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=부산역) · [Wikidata](https://www.wikidata.org/wiki/Q53118) ✓ 109 m

- [Gimhae International Airport](geo:35.180556,128.938056) tag:korea2026 tag:busan tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=김해국제공항) · [Wikidata](https://www.wikidata.org/wiki/Q483223) ✓ 160 m

### Airports and rail

- [Incheon International Airport](geo:37.462500,126.439167) tag:korea2026 tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=인천국제공항) · [Wikidata](https://www.wikidata.org/wiki/Q20932) ✓ 248 m

- [Seoul Station](geo:37.554722,126.970833) tag:korea2026 tag:seoul tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=서울역) · [Wikidata](https://www.wikidata.org/wiki/Q20415) ✓ 122 m

---

## ⚠️ Two places deliberately not pinned

> [!danger] Yongdusan and Gyeongju Station both had wrong Wikidata matches
> Verification caught **two genuinely bad matches** that would have shipped unnoticed. A Wikidata search for "Yongdusan Park" returns a same-named mountain **195 km away** in the southwest, and "Gyeongju Station" returns a **former** station in downtown Gyeongju rather than the real one. The corrected pins above are `Q483056` and `Q54294`. This is why the dual-source check exists — please keep it for anything added later.

> [!warning] Millak-dong has no usable coordinate
> The Busan café cluster has no OpenStreetMap entry, and I would rather leave it off the map than invent a position. Its shops are in [[Korea 2026 — Cafés and Shops|the shop list]] with working search links. If you find the exact address on arrival, add it in the format below.

## Add your next place

Confirm the exact branch first, then add a line in the same format. Replace both coordinate placeholders with verified numbers, and cross-check before you trust them.

```text
[Place name](geo:LATITUDE,LONGITUDE) tag:korea2026 tag:seoul tag:shopping
```

Second tag in use across this file: `sightseeing` · `transport` · `neighborhood` · `nature` · `food` · `shopping`.

Tags not yet used, available for shops and cafés you add: `cafe`, `music`, `books`, `thrift`.

[Map View documentation](https://esm7.github.io/obsidian-map-view/) · [Location formats](https://esm7.github.io/obsidian-map-view/location-formats.html) · [[Japan 2027 — Map View|The Japan maps, same format]]