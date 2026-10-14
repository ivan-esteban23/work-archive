---
locations:
---
# 🗺️ Japan 2027 — Interactive maps

[[Japan 2027 — Start Here|← Dashboard]] · [[Japan 2027 — Maps|All Google Maps destinations]] · [[Japan Travel Guide 2027|Full guide]]

**Starter map · prepared 6 October 2026.** Eleven landmarks and stations from the guide, grouped into Tokyo and Kyoto/Uji. Pins use Wikidata location records; park, temple, and station coordinates identify the site, not a verified entrance or platform. Uji remains an optional excursion. Shops and cafés are in the complete Google Maps index and still need exact-branch coordinates before being pinned.

## Using the maps

Open this note in **Reading view** to see the interactive maps. Click a pin to identify its place; use the Google Maps link below for walking or train directions. The **Open** control opens the full Map View, where you can adjust the query. Map tiles need internet unless downloaded in Map View beforehand.

Suggested full-map queries: `tag:#japan2027`, `tag:#japan2027 AND tag:#tokyo`, or `tag:#japan2027 AND tag:#transport`.

## Tokyo

```mapview
{
  "name": "Japan 2027 \u2014 Tokyo",
  "mapZoom": 12,
  "centerLat": 35.69,
  "centerLng": 139.75,
  "query": "tag:#japan2027 AND tag:#tokyo",
  "chosenMapSource": 0,
  "autoFit": true,
  "lock": false,
  "showLinks": false,
  "markerLabels": "off",
  "embeddedHeight": 430
}
```

## Kyoto and optional Uji

```mapview
{
  "name": "Japan 2027 \u2014 Kyoto and optional Uji",
  "mapZoom": 12,
  "centerLat": 35.0,
  "centerLng": 135.77,
  "query": "tag:#japan2027 AND (tag:#kyoto OR tag:#uji)",
  "chosenMapSource": 0,
  "autoFit": true,
  "lock": false,
  "showLinks": false,
  "markerLabels": "off",
  "embeddedHeight": 430
}
```

## Pin directory

Each line is a Map View location with inline tags. Sources link to the coordinate record; navigation searches include the named destination.

- [Sensō-ji](geo:35.714556,139.796639) tag:japan2027 tag:tokyo tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Sens%C5%8D-ji+tokyo+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q615183)

- [Shinjuku Gyoen](geo:35.687169,139.710644) tag:japan2027 tag:tokyo tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Shinjuku+Gyoen+tokyo+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q776863)

- [Ueno Park](geo:35.712222,139.771111) tag:japan2027 tag:tokyo tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Ueno+Park+tokyo+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q746216)

- [Tokyo Station](geo:35.680833,139.766944) tag:japan2027 tag:tokyo tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Tokyo+Station+tokyo+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q283196)

- [Shibuya Station](geo:35.658514,139.701331) tag:japan2027 tag:tokyo tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Shibuya+Station+tokyo+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q428811)

- [Kiyomizu-dera](geo:34.994831,135.785003) tag:japan2027 tag:kyoto tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Kiyomizu-dera+kyoto+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q221716)

- [Fushimi Inari-taisha](geo:34.967202,135.773386) tag:japan2027 tag:kyoto tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Fushimi+Inari-taisha+kyoto+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q714828)

- [Yasaka Shrine](geo:35.003645,135.778529) tag:japan2027 tag:kyoto tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Yasaka+Shrine+kyoto+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q692714)

- [Nijō Castle](geo:35.014167,135.747500) tag:japan2027 tag:kyoto tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Nij%C5%8D+Castle+kyoto+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q1013399)

- [Kyoto Station](geo:34.985556,135.758611) tag:japan2027 tag:kyoto tag:transport
  [Google Maps](https://www.google.com/maps/search/?api=1&query=Kyoto+Station+kyoto+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q801046)

- [Byōdō-in — optional Uji excursion](geo:34.889444,135.807778) tag:japan2027 tag:uji tag:sightseeing
  [Google Maps](https://www.google.com/maps/search/?api=1&query=By%C5%8Dd%C5%8D-in+uji+Japan) · [Coordinate source](https://www.wikidata.org/wiki/Q61094)

## Add your next place

For a shop or café, confirm its exact branch and coordinates first, then add a line in the same format:

```text
[Place name](geo:LATITUDE,LONGITUDE) tag:japan2027 tag:tokyo tag:shopping
```

Use `tag:cafe`, `tag:music`, or `tag:film` for your other interests. Replace both coordinate placeholders with verified numbers. Add hotel pins after booking the exact property.

[Map View documentation](https://esm7.github.io/obsidian-map-view/) · [Location formats](https://esm7.github.io/obsidian-map-view/location-formats.html)
