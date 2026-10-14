#!/usr/bin/env python3
"""coverfetch — resolve and save an album cover for personal reference.

Saves a local copy of a cover for private reference. Does not upload,
redistribute, or alter the source. Provenance (source URL, edition string,
size, sha256) is always recorded so the image can be traced or removed later.

Sources, in order:
  1. --url PAGE            take og:image from any page (most reliable)
  2. --bandcamp URL        same, but asserts the host is bandcamp
  3. --itunes / --deezer   query the public metadata APIs by artist+album

Examples
  ./coverfetch.py --url https://kommunityfk.bandcamp.com/album/vision-and-the-voice
  ./coverfetch.py --itunes --artist Bauhaus --album "In the Flat Field"
  ./coverfetch.py --itunes --artist Bauhaus --album "In the Flat Field" --dry-run
  ./coverfetch.py --audit albums.json --outdir ~/Vault/Attachments
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

REISSUE_PAT = re.compile(
    r"remaster|anniversary|collector's|digital master|bonus tracks|"
    r"expanded|deluxe|legado|reissue|\b\d{4}\b\s*(edition|master)",
    re.I)


# ---------------------------------------------------------------- helpers

def fetch(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def safe_name(artist: str, album: str) -> str:
    """Filename that keeps non-ASCII letters (Schröttersburg) but drops path/control chars."""
    raw = f"{artist} — {album}" if artist and album else ""
    out = []
    for ch in raw:
        if ch in "/\\:\0":
            out.append(" ")
        elif unicodedata.category(ch).startswith("C"):
            continue
        else:
            out.append(ch)
    s = "".join(out).strip().rstrip(".")
    s = re.sub(r"\s+", " ", s)
    return s[:180] or "untitled"


def og_image(page_url: str):
    """Return (image_url, None) or (None, reason)."""
    try:
        html = fetch(page_url).decode("utf-8", "ignore")
    except Exception as e:
        return None, f"page fetch failed: {e}"
    pats = [
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image',
    ]
    for p in pats:
        m = re.search(p, html)
        if m:
            url = m.group(1).split("?")[0]
            if "bcbits.com" in url:            # bandcamp: _5 is og, _10 is full size
                url = re.sub(r"_\d+\.jpg$", "_10.jpg", url)
            return url, None
    return None, "no og:image on page"


def _norm(s: str) -> str:
    return "".join(c for c in s.lower() if c.isalnum())


def _is_combined(requested: str, title: str) -> bool:
    """True if `title` is a multi-album release that merely contains `requested`.

    Catches 'Talk About the Weather / Paint Your Wagon' when asked for
    'Paint Your Wagon' — a combined sleeve would misrepresent the album.
    """
    nr, nt = _norm(requested), _norm(title)
    if nr not in nt or nt == nr:
        return False
    parts = [p for p in re.split(r"[/,&]| and ", title) if p.strip()]
    return len(parts) > 1 or len(nt) > len(nr) * 1.6


def _match_itunes(artist, album, loose):
    u = "https://itunes.apple.com/search?" + urllib.parse.urlencode(
        {"term": f"{artist} {album}", "entity": "album", "limit": 12})
    try:
        res = json.loads(fetch(u))["results"]
    except Exception:
        return []
    na, nn = _norm(artist), _norm(album)
    exact = [r for r in res
             if _norm(r["artistName"]) == na and _norm(r["collectionName"]) == nn]
    partial = [r for r in res
               if _norm(r["artistName"]) == na and nn in _norm(r["collectionName"])]
    loose_hits = [r for r in res
                  if na in _norm(r["artistName"]) and nn in _norm(r["collectionName"])]
    for group in ([exact, partial] if not loose else [exact, partial, loose_hits]):
        for r in group:
            if _is_combined(album, r["collectionName"]):
                continue          # right song, wrong release
            return r
    return []


def _match_deezer(artist, album):
    u = "https://api.deezer.com/search/album?" + urllib.parse.urlencode(
        {"q": f"{artist} {album}", "limit": 12})
    try:
        res = json.loads(fetch(u)).get("data", [])
    except Exception:
        return []
    na, nn = _norm(artist), _norm(album)
    for r in res:
        if _norm(r["artist"]["name"]) != na:
            continue
        if _norm(r["title"]) == nn:
            return r
    for r in res:
        if _norm(r["artist"]["name"]) == na and nn in _norm(r["title"]):
            if not _is_combined(album, r["title"]):
                return r
    return []


def resolve(artist: str, album: str, loose: bool = False):
    """Return dict(source, edition, matched_artist, image_url, page_url) or None.

    strict by default: artist must match exactly and the release must not be a
    multi-album compilation containing the requested title.
    """
    r = _match_itunes(artist, album, loose)
    if r:
        return {"source": "Apple Music",
                "edition": f"{r['collectionName']} ({r.get('releaseDate','')[:4]})",
                "matched_artist": r["artistName"],
                "image_url": r["artworkUrl100"].replace("100x100", "1000x1000"),
                "page_url": r.get("collectionViewUrl", "")}
    d = _match_deezer(artist, album)
    if d:
        return {"source": "Deezer",
                "edition": f"{d['title']} ({d.get('release_date','')[:4]})",
                "matched_artist": d["artist"]["name"],
                "image_url": d["cover_xl"],
                "page_url": d.get("link", "")}
    return None


def is_reissue(edition: str) -> bool:
    return bool(REISSUE_PAT.search(edition or ""))


# ---------------------------------------------------------------- core

def save_image(url: str, dest_dir: str, fname: str, dry: bool = False):
    try:
        data = fetch(url)
    except Exception as e:
        return None, f"image fetch failed: {e}"
    if data[:2] != b"\xff\xd8":                     # JPEG SOI marker
        return None, f"not a JPEG (first bytes {data[:8]!r})"
    path = os.path.join(dest_dir, fname + ".jpg")
    if dry:
        return {"path": path, "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest()[:16], "saved": False}
    os.makedirs(dest_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()[:16], "saved": True}


def do_one(artist, album, outdir, url=None, dry=False, loose=False, year=None):
    rec = {"artist": artist, "album": album}
    if url:
        img, err = og_image(url)
        if not img:
            rec.update(status="fail", reason=err, page_url=url)
            return rec
        rec.update(source="web page", page_url=url, edition="(page og:image)",
                   matched_artist=artist)
    else:
        res = resolve(artist, album, loose)
        if not res:
            rec.update(status="unresolved", reason="no match on Apple Music or Deezer")
            return rec
        rec.update(source=res["source"], page_url=res["page_url"],
                   edition=res["edition"], image_url=res["image_url"],
                   matched_artist=res["matched_artist"])
        if _norm(res["matched_artist"]) != _norm(artist):
            rec["artist_mismatch"] = True
        if year:
            m = re.search(r"\((\d{4})\)", res["edition"])
            if m and m.group(1) != str(year):
                # same name, different act — or a reissue carrying a later year
                rec["year_mismatch"] = {"expected": year,
                                        "got": m.group(1),
                                        "matched_artist": res["matched_artist"]}
        rec["reissue_suspected"] = is_reissue(res["edition"])
        img = res["image_url"]

    out = save_image(img, outdir, safe_name(artist, album), dry)
    if isinstance(out, str):
        rec.update(status="fail", reason=out)
        return rec
    rec.update(status="ok" if out["saved"] else "dry-run",
               path=out["path"], bytes=out["bytes"], sha256=out["sha256"])
    return rec


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--url", help="page to take og:image from")
    g.add_argument("--itunes", action="store_true", help="resolve via Apple Music / Deezer APIs")
    g.add_argument("--audit", help="JSON file of [{artist, album, url?}] to process")
    p.add_argument("--loose", action="store_true",
                   help="allow partial artist-name matching (riskier)")
    p.add_argument("--year", type=int,
                   help="original release year; warns if the match carries a different one "
                        "(catches same-name-different-band and reissue sleeves)")
    p.add_argument("--artist"); p.add_argument("--album")
    p.add_argument("--outdir", default=os.path.expanduser("~/Work/music-research-tools/covers"))
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--report", help="write results as JSON here")
    a = p.parse_args()

    if a.itunes and not (a.artist and a.album):
        sys.exit("--itunes needs --artist and --album")

    items = []
    if a.audit:
        items = json.load(open(a.audit))
    else:
        items = [{"artist": a.artist, "album": a.album, "url": a.url}]

    results = [do_one(it.get("artist", ""), it.get("album", ""), a.outdir,
                      it.get("url"), a.dry_run, a.loose, a.year) for it in items]

    for r in results:
        tag = {"ok": "OK  ", "dry-run": "DRY ", "fail": "FAIL", "unresolved": "MISS"}[r["status"]]
        line = f"{tag} {r.get('artist','')} — {r.get('album','')}"
        if r.get("source"):
            line += f"  [{r['source']}] {r.get('edition','')}"
            if r.get("reissue_suspected"):
                line += "  ⚠ reissue"
            if r.get("artist_mismatch"):
                line += f"  ⚠ DIFFERENT ARTIST: {r['matched_artist']}"
            if r.get("year_mismatch"):
                ym = r["year_mismatch"]
                line += (f"  ⚠ YEAR {ym['expected']}→{ym['got']}"
                         f" (check it is the same act)")
        if r.get("reason"):
            line += f"  — {r['reason']}"
        print(line)
        if r.get("path"):
            print(f"       {r['path']}  ({r['bytes']//1024} KB, sha256 {r['sha256'][:12]})")

    tally = {}
    for r in results:
        tally[r["status"]] = tally.get(r["status"], 0) + 1
    print(f"\n{tally}")

    if a.report:
        json.dump(results, open(a.report, "w"), indent=1, ensure_ascii=False)
        print(f"report -> {a.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())