# Japan 2027 project — command reference

Everything you need to run, check, and undo this project. Written 7 October 2026.

> [!info] Read this file first
> It lives in the project folder. To reopen it: `cd "/home/ivanaguilera/Work/japan-guide-update/chatgpt-project" && less COMMANDS.md`
> Or open `COMMANDS.md` in Obsidian — it's plain text, opens fine in any editor.

**Most of the time you only need one command:**

```bash
cd "/home/ivanaguilera/Work/japan-guide-update/chatgpt-project" && ./refresh.sh
```

Then upload the six files it produces. That's the whole loop.

---

## The one-line habit

Set up a shell alias once and forget the long path:

```bash
echo 'alias japancheck="cd /home/ivanaguilera/Work/japan-guide-update/chatgpt-project && ./refresh.sh"' >> ~/.bashrc
source ~/.bashrc
```

Then just type `japancheck`. To undo the alias, delete that line from `~/.bashrc`.

---

## `refresh.sh` — the main command

Run from the project folder. Four modes:

| Command | What it does | Changes files? |
|---|---|---|
| `./refresh.sh` | Full refresh: export from Obsidian, split into 6 files, verify | **Yes** |
| `./refresh.sh --check` | Reports whether files are out of date | No |
| `./refresh.sh --status` | Lists the files and sizes to upload | No |
| `./refresh.sh --help` | Shows usage | No |

### `./refresh.sh` — what it actually does

1. Runs `export.py`, which copies your 64 Obsidian notes + 2 map exports into one big file
2. Runs `split-guide.py`, which cuts that into the 6 topical files
3. Rewrites `manifest.json` with fresh checksums of every vault file
4. Regenerates `Project instructions.txt` and `README.md`
5. Verifies everything, then tells you what to upload

### `./refresh.sh --check` — the important one

Compares your vault against `manifest.json`. Answers "are my uploaded files still current?" without touching anything.

| Output | Meaning |
|---|---|
| `Snapshot is current` | Nothing to do |
| `1 changed · 0 new · 0 missing` | Listed files drifted; refresh needed |
| `Snapshot is stale` + filenames | Exactly which notes changed |

Exits 0 when current, 1 when stale — so it also works from other scripts.

---

## When to run a refresh

| Trigger | Why |
|---|---|
| After editing notes in Obsidian | The export is a snapshot; it doesn't track the vault |
| After making a booking | Prices and confirmations change |
| Any time `--check` says stale | That's what it's for |
| January 2027 | Rail timetable for 2027 published |
| February 2027 | Cherry blossom forecasts published |

You don't need to refresh daily. The twice-daily reminder handles it.

---

## The reminder (already set up)

Checks automatically at **08:00 and 15:00** every day. Silent when current; desktop notification when stale.

```bash
# see when it next runs
systemctl --user list-timers japan-export-staleness.timer --no-pager

# test it right now (sends a real notification if stale)
systemctl --user start japan-export-staleness.service

# turn it off completely
omarchy-japan-export-staleness-remove
```

**Changing the times** — edit `~/.config/systemd/user/japan-export-staleness.timer`, then:

```bash
systemctl --user daemon-reload
systemctl --user restart japan-export-staleness.timer
```

**The 60-minute quiet window:** if it notifies and then runs again within an hour, the second one stays silent. Prevents double-notifications from a boot catch-up landing next to a scheduled slot. Override for testing with `JAPAN_CHECK_QUIET_MINUTES=0`.

---

## What to upload to ChatGPT

Seven files, all in the project folder:

| File | Size | Notes |
|---|---|---|
| `Japan 2027 — Dashboard and Decisions.txt` | ~32 KB | **Read this one first** |
| `Japan 2027 — Itinerary and Pocket Cards.txt` | ~194 KB | The 14-night plan |
| `Japan 2027 — City Chapters and Regions.txt` | ~243 KB | Fukuoka, Osaka, Okinawa, etc. |
| `Japan 2027 — Shopping Food and Experiences.txt` | ~103 KB | Shops, gifts, Klook |
| `Japan 2027 — Planning Essentials and Seasons.txt` | ~85 KB | Bookings, health, seasonal |
| `Japan 2027 — Maps and Routes.txt` | ~70 KB | Pins, searches, offline |
| `Japan 2027 — Confirmed Decisions.txt` | small | **Yours to edit.** Never overwritten |

Also paste into the project's instructions box: **`Project instructions.txt`**

> **Do not upload** `Japan 2027 — Complete Guide for ChatGPT.txt`. It's the intermediate step the six files are cut from. Uploading both would make everything count twice.

---

## Files you edit vs files that are generated

| File | Who writes it |
|---|---|
| `Japan 2027 — Confirmed Decisions.txt` | **You.** Log decisions here as you make them |
| `Japan 2027 — Maps.md`, `Saved Maps.md` | Your Obsidian vault, then the export copies them |
| `Project instructions.txt` | Regenerated every refresh. **Don't hand-edit** |
| `README.md` | Regenerated every refresh. **Don't hand-edit** |
| `manifest.json` | Regenerated every refresh |
| The 6 guide files | Regenerated every refresh |

The guardrail line about never pasting passport numbers lives inside `export.py`, so it survives every refresh. That's why you can't just add it by hand to `Project instructions.txt`.

---

## Recording decisions

Edit `Japan 2027 — Confirmed Decisions.txt` after any chat where something gets settled. One line per decision:

```
Date decided | Decision | Status | Notes
```

Status is either **CONFIRMED** (you chose it, no money moved) or **BOOKED** (money moved).

Never put confirmation codes, passport numbers, or card details in it — record dates, totals, and cancellation deadlines only.

---

## If something goes wrong

| Problem | What to do |
|---|---|
| `assert len(notes) == 64` fails | You added or removed Japan notes. Tell me the new count — one line to fix |
| Any other error from `export.py` | Copy the last 5 lines and send them. Don't re-run blindly |
| Timer not firing | `systemctl --user list-timers --all \| grep japan` |
| Want to undo everything | `./refresh.sh` is safe to re-run. Reminder: `omarchy-japan-export-staleness-remove` |

The vault is never modified by any of this — everything reads from it.

---

## Quick reference card

```bash
cd "/home/ivanaguilera/Work/japan-guide-update/chatgpt-project"

./refresh.sh              # do everything, then upload
./refresh.sh --check      # am I current? (changes nothing)
./refresh.sh --status     # what do I upload?
./refresh.sh --help       # usage

# reminder
systemctl --user list-timers japan-export-staleness.timer --no-pager
systemctl --user start japan-export-staleness.service
omarchy-japan-export-staleness-remove
```