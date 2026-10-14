#!/usr/bin/env python3
"""albumaudit — report album-dossier artwork coverage across the music projects.

Finds per-album dossier notes, checks each for embedded artwork, and emits a
JSON list usable as coverfetch.py --audit input.

  ./albumaudit.py                     # summary + write albums.json
  ./albumaudit.py --vault ~/Documents/Obsidian\\ Vault
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re

PROJECTS = ["Goth Rock", "Black Metal", "Death Metal", "Heavy Metal", "Hardcore & Punk"]
RE_ALBUM = re.compile(r'^- \*\*Album:\*\* (.+)$', re.M)
RE_ARTIST = re.compile(r'^- \*\*Artist:\*\* (.+)$', re.M)
RE_YEAR = re.compile(r'^- \*\*Original year:\*\* (.+)$', re.M)
RE_IMG = re.compile(r'^!\[\[', re.M)


def dossiers(vault: pathlib.Path, project: str):
    snap = vault / f"{project} — Notion Snapshot 2026-10-09"
    files = []
    if snap.exists():
        files += sorted(snap.glob("Album*.md"))
    files += sorted(vault.glob(f"{project} — Album*.md"))
    return [f for f in files if not f.name.startswith("Album Gallery")]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--vault", default=os.path.expanduser("~/Documents/Obsidian Vault"))
    p.add_argument("--out", default="albums.json")
    a = p.parse_args()
    vault = pathlib.Path(a.vault)

    rows = []
    for proj in PROJECTS:
        files = dossiers(vault, proj)
        for f in files:
            t = f.read_text(errors="ignore")
            al, ar, yr = RE_ALBUM.search(t), RE_ARTIST.search(t), RE_YEAR.search(t)
            if not (al and ar):
                continue
            rows.append({
                "project": proj,
                "file": f.name,
                "path": str(f),
                "artist": ar.group(1).strip(),
                "album": al.group(1).strip(),
                "year": yr.group(1).strip() if yr else "",
                "artwork": bool(RE_IMG.search(t)),
            })

    out = pathlib.Path(a.out)
    json.dump(rows, open(out, "w"), ensure_ascii=False, indent=1)

    total_missing = 0
    print(f"{'project':20} {'dossiers':>9} {'no artwork':>11}")
    for proj in PROJECTS:
        r = [x for x in rows if x["project"] == proj]
        miss = [x for x in r if not x["artwork"]]
        total_missing += len(miss)
        if not r:
            print(f"{proj:20} {'0':>9} {'— (no dossiers yet)':>11}")
            continue
        print(f"{proj:20} {len(r):>9} {len(miss):>11}")

    print(f"\ntotal dossiers: {len(rows)}   without artwork: {total_missing}")
    print(f"-> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())