#!/usr/bin/env bash
#
# refresh.sh — one-command maintenance for the Japan 2027 ChatGPT project files.
#
# WHAT THIS IS
#   A convenience wrapper. It runs the existing Python scripts, checks whether
#   your Obsidian vault has changed since the last export, and verifies the
#   result. You can always run export.py directly instead; nothing here is
#   required, and no logic lives only in this file.
#
# USAGE
#   ./refresh.sh            refresh everything (export + split)
#   ./refresh.sh --check    report staleness only, change nothing
#   ./refresh.sh --status   show current export state
#   ./refresh.sh --help     this message
#
# WHY IT EXISTS
#   export.py rewrites Project instructions.txt, README.md and manifest.json
#   from scratch on every run, so anything hand-edited in those files is lost.
#   That is deliberate for the generated files, but it means the refresh has
#   to be all-or-nothing and verified. This script does that in one step.

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VAULT="${VAULT:-/home/ivanaguilera/Documents/Obsidian Vault}"

MANIFEST="$SCRIPT_DIR/manifest.json"
EXPORT_PY="$SCRIPT_DIR/export.py"
SPLIT_PY="$SCRIPT_DIR/split-guide.py"
LEDGER="$SCRIPT_DIR/Japan 2027 — Confirmed Decisions.txt"

PARTS=(
  "Japan 2027 — Dashboard and Decisions.txt"
  "Japan 2027 — Itinerary and Pocket Cards.txt"
  "Japan 2027 — City Chapters and Regions.txt"
  "Japan 2027 — Shopping Food and Experiences.txt"
  "Japan 2027 — Planning Essentials and Seasons.txt"
  "Japan 2027 — Maps and Routes.txt"
)

# ---- pretty output -------------------------------------------------------
if [[ -t 1 ]]; then
  B=$'\033[1m'; DIM=$'\033[2m'; R=$'\033[31m'; G=$'\033[32m'; Y=$'\033[33m'; N=$'\033[0m'
else
  B=""; DIM=""; R=""; G=""; Y=""; N=""
fi
info() { printf '%s\n' "${DIM}·${N} $*"; }
ok()   { printf '%s\n' "${G}✓${N} $*"; }
warn() { printf '%s\n' "${Y}!${N} $*" >&2; }
die()  { printf '%s\n' "${R}✗${N} $*" >&2; exit 1; }

usage() {
  cat <<EOF
${B}refresh.sh${N} — maintain the Japan 2027 ChatGPT project files

  ${B}./refresh.sh${N}            refresh everything (export + split + verify)
  ${B}./refresh.sh --check${N}    report staleness only, change nothing
  ${B}./refresh.sh --status${N}   show current export state
  ${B}./refresh.sh --help${N}     this message

${DIM}Vault:${N} $VAULT
${DIM}Project folder:${N} $SCRIPT_DIR

${DIM}After a refresh, re-upload the six guide files to the ChatGPT project.
Project instructions.txt and README.md are regenerated each run — do not hand-edit
them. Japan 2027 — Confirmed Decisions.txt is yours and is never overwritten.
EOF
}

# ---- staleness -----------------------------------------------------------
# Compares each vault note's current sha256 against the value recorded in
# manifest.json at export time. Any mismatch means the snapshot is behind.
staleness() {
  [[ -f "$MANIFEST" ]] || die "no manifest.json — run './refresh.sh' once to create it"

  local stamp
  stamp="$(jq -r '.exported_at' "$MANIFEST")"

  python3 - "$MANIFEST" "$VAULT" <<'PY'
import hashlib, json, pathlib, sys

manifest_path, vault = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
data = json.loads(manifest_path.read_text(encoding="utf-8"))

changed, missing = [], []
for entry in data["files"]:
    rel = entry["source"]
    path = vault / rel
    if not path.exists():
        missing.append(rel)
        continue
    now = hashlib.sha256(path.read_bytes()).hexdigest()
    if now != entry["sha256"]:
        changed.append(rel)

# Notes present in the vault but absent from the manifest are new since export.
manifest_names = {e["source"] for e in data["files"]}
added = sorted(
    p.relative_to(vault).as_posix()
    for p in vault.glob("Japan*.md")
    if p.relative_to(vault).as_posix() not in manifest_names
)

for rel in changed:
    print(f"CHANGED\t{rel}")
for rel in missing:
    print(f"MISSING\t{rel}")
for rel in added:
    print(f"NEW\t{rel}")

total = len(data["files"])
print(f"TOTAL\t{len(changed)}\t{len(missing)}\t{len(added)}\t{total}")
PY
}

report_staleness() {
  local stamp out changed missing added total
  stamp="$(jq -r '.exported_at' "$MANIFEST")"
  out="$(staleness)"
  total="$(awk -F'\t' '$1=="TOTAL"{print $5}' <<<"$out")"
  changed="$(grep -c '^CHANGED' <<<"$out" || true)"
  missing="$(grep -c '^MISSING' <<<"$out" || true)"
  added="$(grep -c '^NEW' <<<"$out" || true)"

  printf '%s\n' "${B}Last export:${N} $stamp"
  printf '%s\n' "${B}Tracked sources:${N} $total"
  if [[ "$changed" -eq 0 && "$missing" -eq 0 && "$added" -eq 0 ]]; then
    printf '\n%s\n' "${G}Snapshot is current — nothing to refresh.${N}"
    return 0
  fi

  printf '\n%s\n' "${Y}Snapshot is stale:${N}"
  grep '^CHANGED' <<<"$out" | cut -f2 | sed "s|^|  ${Y}changed${N}  |"
  grep '^MISSING' <<<"$out" | cut -f2 | sed "s|^|  ${Y}missing${N}  |"
  grep '^NEW'     <<<"$out" | cut -f2 | sed "s|^|  ${Y}new${N}     |"
  printf '\n%s\n' "  run ${B}./refresh.sh${N} to update"
  return 1
}

# ---- status --------------------------------------------------------------
show_status() {
  [[ -f "$MANIFEST" ]] || die "no manifest.json yet — run './refresh.sh' once"
  printf '%s\n' "${B}Last export:${N} $(jq -r '.exported_at' "$MANIFEST")"
  printf '%s\n' "${B}Tracked sources:${N} $(jq -r '.source_count' "$MANIFEST")"
  printf '\n%s\n' "${B}Project files:${N}"
  for f in "${PARTS[@]}"; do
    if [[ -f "$SCRIPT_DIR/$f" ]]; then
      local kb
      kb=$(( $(wc -c <"$SCRIPT_DIR/$f") / 1024 ))
      printf '  %s✓%s %-50s %5s KB\n' "$G" "$N" "$f" "$kb"
    else
      printf '  %s✗%s %-50s MISSING\n' "$R" "$N" "$f"
    fi
  done
  [[ -f "$LEDGER" ]] \
    && printf '  %s✓%s %-50s (yours — never overwritten)\n' "$G" "$N" "$(basename "$LEDGER")" \
    || printf '  %s✗%s %-50s MISSING\n' "$R" "$N" "$(basename "$LEDGER")"

  printf '\n%s\n' "${B}Upload list (7 files):${N}"
  printf '  · the six guide files above\n  · %s\n' "$(basename "$LEDGER")"
}

# ---- refresh -------------------------------------------------------------
do_refresh() {
  [[ -d "$VAULT" ]] || die "vault not found: $VAULT"
  [[ -f "$EXPORT_PY" ]] || die "export.py not found next to this script"
  [[ -f "$SPLIT_PY" ]] || die "split-guide.py not found next to this script"

  printf '%s\n\n' "${B}Refreshing from vault${N} ${DIM}$VAULT${N}"

  if ! python3 "$EXPORT_PY"; then
    die "export.py failed — nothing further was run. See the error above."
  fi

  printf '\n%s\n' "${B}Verifying${N}"
  local f
  for f in "${PARTS[@]}"; do
    [[ -s "$SCRIPT_DIR/$f" ]] || die "expected part missing or empty: $f"
  done

  # Project instructions.txt is regenerated by export.py: the guardrail line
  # must have survived. If someone edits export.py and drops it, catch it here
  # rather than discovering it after upload.
  grep -q "Never paste passport numbers" "$SCRIPT_DIR/Project instructions.txt" \
    || die "guardrail line missing from Project instructions.txt"

  # Count BEGIN markers across the six named parts only. Globbing
  # "Japan 2027 — *.txt" would also pick up the Trip Profile, the Travel
  # Essay and the Confirmed Decisions ledger, which have no BEGIN markers.
  python3 - "$SCRIPT_DIR" "${PARTS[@]}" <<'PY'
import re, sys, pathlib
d = pathlib.Path(sys.argv[1])
names = sys.argv[2:]
total, empty = 0, []
for name in names:
    p = d / name
    n = len(re.findall(r"(?m)^BEGIN SOURCE \d+:", p.read_text(encoding="utf-8")))
    total += n
    if n == 0:
        empty.append(name)
if total != 66 or empty:
    if empty:
        print(f"  ✗ no sources found in: {', '.join(empty)}")
    print(f"  ✗ expected 66 sources across six parts, found {total}")
    sys.exit(1)
print("  ✓ 66/66 sources placed across six files")
PY

  ok "all six project files rebuilt and verified"
  printf '\n%s\n' "Next: upload the six files and ${B}Japan 2027 — Confirmed Decisions.txt${N} to the project."
}

# ---- main ----------------------------------------------------------------
case "${1:-}" in
  --help|-h)   usage ;;
  # Exit 0 = current, 1 = stale, so this is usable from scripts and timers.
  --check)     report_staleness ;;
  --status)    show_status ;;
  "")          do_refresh ;;
  *)           die "unknown option: $1 (try --help)" ;;
esac