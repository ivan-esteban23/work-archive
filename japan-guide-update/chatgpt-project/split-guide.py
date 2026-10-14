#!/usr/bin/env python3
"""Split the monolithic ChatGPT export into topical files for better retrieval.

Usage:
    python3 split-guide.py [input-file]

Reads "Japan 2027 — Complete Guide for ChatGPT.txt" (default) and emits six
topical .txt files in the same directory. Safe to re-run after a fresh vault
export: outputs are overwritten, the input is never modified.

Grouping rationale: ChatGPT Projects retrieve over uploaded files in chunks.
One 737KB blob forces every query through the same haystack; topical files
let retrieval select the right haystack first.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "Japan 2027 — Complete Guide for ChatGPT.txt"

# source number -> (output file, short reason)
GROUPS = {
    # A. Read-first: dashboard, recaps, priorities
    1:  "A", 2: "A", 58: "A", 25: "A", 35: "A",
    # B. The dated plan: full guide, pocket cards, daily ops
    3: "B", 10: "B", 63: "B", 24: "B", 52: "B",
    **{n: "B" for n in range(37, 52)},
    # C. Regional chapters and alternates
    12: "C", 13: "C", 26: "C", 27: "C", 28: "C", 29: "C",
    33: "C", 34: "C", 31: "C", 32: "C", 53: "C", 54: "C",
    7: "C", 18: "C", 21: "C", 16: "C", 17: "C",
    # D. Shopping, food, paid experiences, capture
    59: "D", 60: "D", 14: "D", 9: "D", 4: "D", 5: "D",
    11: "D", 36: "D",
    # E. Planning backbone: bookings, essentials, seasons
    8: "E", 64: "E", 15: "E", 20: "E", 19: "E", 56: "E",
    57: "E", 30: "E", 62: "E", 61: "E", 6: "E",
    # F. Maps and offline
    22: "F", 23: "F", 55: "F", 65: "F", 66: "F",
}

FILES = {
    "A": ("Japan 2027 — Dashboard and Decisions.txt",
          "Dashboard, session recaps, priorities, photography wishlist. Read this file first."),
    "B": ("Japan 2027 — Itinerary and Pocket Cards.txt",
          "The dated 14-night plan: full guide, daily pocket cards, Today, Memories, Quick Capture."),
    "C": ("Japan 2027 — City Chapters and Regions.txt",
          "Fukuoka, Nagoya, Nara, Osaka, Okinawa, Sapporo chapters + islands, hidden gems, hiking."),
    "D": ("Japan 2027 — Shopping Food and Experiences.txt",
          "Shopping shortlist, shops/cafés, gifts, clothing, Klook tours, expenses, place inbox."),
    "E": ("Japan 2027 — Planning Essentials and Seasons.txt",
          "Bookings, travel essentials, health, Japanese practice, seasonal guides and comparisons."),
    "F": ("Japan 2027 — Maps and Routes.txt",
          "Map View pins, Maps searches, saved offline maps, CSV/KML exports."),
}


SEP = "=" * 78 + "\n"


def parse(text):
    """Return (preamble, [(num, title, body)]) with boundary separators
    normalized: each body is content + its END SOURCE line, no leading or
    trailing === runs (those are re-emitted canonically)."""
    parts = re.split(r'(BEGIN SOURCE \d+: .+?)\n', text)
    preamble = parts[0]
    out = []
    # parts: [preamble, header1, body1, header2, body2, ...]
    it = iter(parts[1:])
    for header, body in zip(it, it):
        m = re.match(r'BEGIN SOURCE (\d+): (.+)', header)
        num, title = int(m.group(1)), m.group(2).strip()
        # strip boundary === runs carried over from the monolith layout
        body = re.sub(r'\A(?:=+[ \t]*\n)+', '', body)
        end = re.search(rf'END SOURCE {num}[ \t]*$', body, re.M)
        assert end, f"missing END SOURCE {num}"
        body = body[: end.end()].rstrip('\n')
        out.append((num, title, body))
    return preamble, out


def file_header(code, fname, desc, members, siblings):
    lines = [
        fname.replace(".txt", "").upper() + " — PROJECT SOURCE (PART "
        + code + " OF 6)",
        "",
        "Exported: 2026-10-07T14:18:27-03:00",
        "Source: live local Obsidian Japan guide (same snapshot as the complete export).",
        "",
        desc,
        "",
        "This is a snapshot for a ChatGPT project, not a live connection to Obsidian.",
        "Later vault edits require a refreshed export. The current dashboard and latest",
        "session recap live in Part A; newer notes and the user's latest instructions",
        "take precedence over everything here.",
        "",
        "All source note content and external URLs are preserved. Obsidian [[wiki links]]",
        "refer to other named source notes; they are not public web links.",
        "No Korea notes, plugin settings, account credentials, or backup copies are included.",
        "Map content holds search queries and starter coordinates; do not assume every",
        "query is a verified venue or every coordinate is an entrance.",
        "",
        "Existing dates, budgets, destinations, shopping ideas, and tour shortlists retain",
        "their original provisional status. An activity appearing here is not a booking,",
        "and displayed prices are not confirmed 2027 quotes. Follow the user's current",
        "choices and verify time-sensitive information before making recommendations.",
        "",
        "SIBLING FILES (upload all six together):",
    ]
    for c in "ABCDEF":
        mark = " <-- this file" if c == code else ""
        lines.append(f"  - {FILES[c][0]}{mark}")
    lines += ["", "SOURCE INDEX (original export numbering preserved)", ""]
    for num, title in members:
        lines.append(f"{num}. {title}")
    lines += ["", ""]
    return "\n".join(lines)


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    text = src.read_text(encoding="utf-8")
    preamble, sources = parse(text)
    assert len(sources) == 66, f"expected 66 sources, got {len(sources)}"
    assert sorted(n for n, _, _ in sources) == list(range(1, 67))

    by_num = {n: (t, b) for n, t, b in sources}
    assert set(by_num) == set(GROUPS), (
        "unassigned: " + str(sorted(set(by_num) - set(GROUPS)))
        or "unknown: " + str(sorted(set(GROUPS) - set(by_num)))
    )

    # emit: every body lands in exactly one output, with canonical separators
    for code in "ABCDEF":
        fname, desc = FILES[code]
        members = [(n, by_num[n][0]) for n in sorted(k for k, v in GROUPS.items() if v == code)]
        siblings = [FILES[c][0] for c in "ABCDEF"]
        body = file_header(code, fname, desc, members, siblings)
        for n, _ in members:
            body += SEP
            body += f"BEGIN SOURCE {n}: {by_num[n][0]}\n"
            body += SEP + "\n"
            body += by_num[n][1].lstrip("\n") + "\n\n\n"
        out = HERE / fname
        out.write_text(body, encoding="utf-8")
        kb = out.stat().st_size // 1024
        print(f"  {fname}  ({len(members)} sources, ~{kb} KB)")

    # verify: union of emitted normalized bodies == original normalized bodies
    emitted = sum(len(by_num[n][1]) for n in GROUPS)
    original = sum(len(b) for _, _, b in sources)
    assert emitted == original, f"byte mismatch: {emitted} vs {original}"
    print(f"OK: 66/66 sources placed, {original:,} normalized body bytes preserved.")


if __name__ == "__main__":
    main()
