#!/usr/bin/env bash
# Omarchy/Arch workstation installer. Research: 2026-10-12.
set -Eeuo pipefail
umask 077
MODE=plan
VAULT="${HOME}/Documents/Obsidian Vault"
BACKUP_ROOT="${HOME}/Work/workstation-setup/backups"
AM_APPS=()
usage() {
  cat <<'HELP'
Usage: bash setup.sh [--apply | --download-only] [--vault PATH]
                     [--backup-root PATH] [--am-app NAME ...]
Default: print the plan without downloading or changing anything.
--download-only: validate/download missing Obsidian plugins; no vault/system changes.
--apply: install packages, Qoder, AM; enable SSH; install/enable Obsidian plugins.
Run as your regular user in a terminal. Close Obsidian before --apply.
Existing complete plugins and their settings are preserved.
AM apps supplied with --am-app are installed, unlocked if locked, and updated.
HELP
}
while (($#)); do
  case "$1" in
    --apply) MODE=apply; shift ;;
    --download-only) MODE=download; shift ;;
    --vault|--backup-root|--am-app)
      (($# >= 2)) || { usage >&2; exit 2; }
      case "$1" in
        --vault) VAULT="$2" ;;
        --backup-root) BACKUP_ROOT="$2" ;;
        --am-app) [[ "$2" =~ ^[a-zA-Z0-9][a-zA-Z0-9._+-]*$ ]] || exit 2; AM_APPS+=("$2") ;;
      esac
      shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; exit 2 ;;
  esac
done
[[ $EUID -ne 0 ]] || { echo "Run as your regular user, without sudo." >&2; exit 1; }
[[ -d "$VAULT/.obsidian" ]] || { echo "No .obsidian directory in $VAULT" >&2; exit 1; }
cat <<PLAN
Vault: $VAULT
Packages: curl, python, git, jq, openssh, fuse2, vlc, vlc-plugins-all, ttf-ms-fonts
Obsidian: existing plugin set + 16 baseline plugins + 4 additions; safeMode=false
Qoder: https://qoder.com/install (official native installer)
AM: official ivan-hc/AM installer if missing; synchronize AM
SSH: enable sshd, open its configured TCP ports if UFW is active
Backups: $BACKUP_ROOT
Mode: $MODE
PLAN
if (("${#AM_APPS[@]}")); then printf 'AM install/update: %s\n' "${AM_APPS[@]}"; fi
[[ "$MODE" != plan ]] || exit 0
if [[ "$MODE" == apply ]]; then
  command -v omarchy >/dev/null || { echo "This installer requires Omarchy." >&2; exit 1; }
  if pgrep -u "$(id -u)" -x obsidian >/dev/null || pgrep -u "$(id -u)" -x Obsidian >/dev/null; then
    echo "Close Obsidian before applying plugin changes." >&2
    exit 1
  fi
  # The official installer and AM use sudo internally; do not run this script as root.
  sudo -v
  omarchy pkg add curl python git jq openssh fuse2 vlc vlc-plugins-all
  if ! pacman -Q ttf-ms-fonts >/dev/null 2>&1; then
    if pacman -Si ttf-ms-fonts >/dev/null 2>&1; then
      omarchy pkg add ttf-ms-fonts
    else
      omarchy pkg aur add ttf-ms-fonts
    fi
  fi
  fc-cache -f
fi
for tool in curl python3; do command -v "$tool" >/dev/null || { echo "Missing $tool" >&2; exit 1; }; done
mkdir -p "$BACKUP_ROOT"
RUN_DIR=$(mktemp -d "$BACKUP_ROOT/run-$(date +%Y%m%d-%H%M%S)-XXXXXX")
echo "Staging, report and backups: $RUN_DIR"
export SETUP_RUN_DIR="$RUN_DIR"
# JSON handling and staged plugin validation use Python's standard library.
python3 - "$VAULT" "$RUN_DIR" "$MODE" <<'PY'
import hashlib, json, os, pathlib, re, shutil, subprocess, sys
vault, run, mode = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
config = vault / ".obsidian"
baseline = [
 "obsidian-map-view", "obsidian-local-images-plus", "obsidian-meta-bind-plugin",
 "omnisearch", "pdf-plus", "obsidian-spaced-repetition", "obsidian-tracker",
 "quickadd", "templater-obsidian", "obsidian-tasks-plugin", "calendar",
 "table-editor-obsidian", "tag-wrangler", "dataview",
 "obsidian-minimal-settings", "obsidian-style-settings",
 "obsidian-excalidraw-plugin", "obsidian-linter", "note-toolbar", "periodic-notes"
]
def load(path, default):
    return json.loads(path.read_text()) if path.exists() else default
def snapshot():
    return {str(p.relative_to(config)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in config.rglob("*") if p.is_file()}
original = snapshot()
enabled = load(config / "community-plugins.json", [])
app = load(config / "app.json", {})
if not isinstance(enabled, list) or not all(isinstance(x, str) for x in enabled):
    raise SystemExit("community-plugins.json must be a list of plugin IDs.")
if not isinstance(app, dict):
    raise SystemExit("app.json must be an object.")
installed = []
for manifest_path in (config / "plugins").glob("*/manifest.json"):
    manifest = load(manifest_path, {})
    if manifest.get("id") != manifest_path.parent.name:
        raise SystemExit(f"Invalid installed manifest: {manifest_path}")
    installed.append(manifest["id"])
wanted = list(dict.fromkeys(enabled + installed + baseline))
if any(not re.fullmatch(r"[A-Za-z0-9_-]+", x) for x in wanted):
    raise SystemExit("Unsafe plugin ID in existing configuration.")
stage = run / "staged-plugins"
stage.mkdir()
def fetch(url, target):
    subprocess.run(["curl", "--fail", "--show-error", "--silent", "--location",
                    "--retry", "3", "--connect-timeout", "20", "--max-time", "180",
                    "--proto", "=https", "--proto-redir", "=https",
                    url, "-o", str(target)], check=True)
registry_path = run / "community-registry.json"
fetch("https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json",
      registry_path)
registry = {x["id"]: x for x in load(registry_path, [])}
report = []
for plugin_id in wanted:
    target = config / "plugins" / plugin_id
    if (target / "main.js").is_file() and (target / "main.js").stat().st_size:
        manifest = load(target / "manifest.json", {})
        if manifest.get("id") == plugin_id and manifest.get("version"):
            print(f"Keep {plugin_id} {manifest['version']}", flush=True)
            report.append({"id": plugin_id, "version": manifest["version"], "action": "preserved"})
            continue
    if plugin_id not in registry:
        raise SystemExit(f"{plugin_id} is not in the official community registry; supply it manually.")
    repo = registry[plugin_id]["repo"]
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise SystemExit(f"Invalid repository: {repo}")
    print(f"Stage {plugin_id} from {repo}", flush=True)
    release_path = run / f"{plugin_id}-release.json"
    fetch(f"https://api.github.com/repos/{repo}/releases/latest", release_path)
    release = load(release_path, {})
    assets = {a["name"]: a["browser_download_url"] for a in release.get("assets", [])}
    if not {"manifest.json", "main.js"} <= assets.keys():
        raise SystemExit(f"{repo}: latest stable release lacks required Obsidian assets.")
    dest = stage / plugin_id
    dest.mkdir()
    for name in ("manifest.json", "main.js", "styles.css"):
        if name in assets:
            url = assets[name]
            if not url.startswith(f"https://github.com/{repo}/releases/download/"):
                raise SystemExit(f"Unexpected asset URL: {url}")
            fetch(url, dest / name)
    manifest = load(dest / "manifest.json", {})
    if manifest.get("id") != plugin_id or not manifest.get("version") or not (dest / "main.js").stat().st_size:
        raise SystemExit(f"Invalid release assets for {plugin_id}")
    report.append({"id": plugin_id, "repo": repo, "version": manifest["version"],
                   "minAppVersion": manifest.get("minAppVersion"),
                   "tag": release["tag_name"], "action": "staged",
                   "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in dest.iterdir()}})
(run / "plugin-report.json").write_text(json.dumps(report, indent=2) + "\n")
if mode == "download":
    print("Downloads validated. No changes to vault or system.")
    sys.exit(0)
def ensure_closed():
    for name in ("obsidian", "Obsidian"):
        if subprocess.run(["pgrep", "-u", str(os.getuid()), "-x", name],
                          stdout=subprocess.DEVNULL).returncode == 0:
            raise SystemExit("Obsidian opened during staging. Close it and rerun.")
ensure_closed()
if snapshot() != original:
    raise SystemExit("Obsidian configuration changed during staging; rerun to preserve those changes.")
backup = run / "obsidian-config-before"
shutil.copytree(config, backup)
if snapshot() != original:
    raise SystemExit("Configuration changed while backing up; no plugin changes applied.")
changed = [p.name for p in stage.iterdir()]
def atomic_json(path, data):
    tmp = path.with_name(path.name + ".setup-tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    tmp.replace(path)
try:
    for plugin_id in changed:
        src, dst = stage / plugin_id, config / "plugins" / plugin_id
        dst.mkdir(parents=True, exist_ok=True)
        for p in src.iterdir():
            shutil.copy2(p, dst / p.name)
    app["safeMode"] = False
    atomic_json(config / "app.json", app)
    atomic_json(config / "community-plugins.json", wanted)
    assert load(config / "app.json", {})["safeMode"] is False
    assert load(config / "community-plugins.json", []) == wanted
    for plugin_id in wanted:
        assert load(config / "plugins" / plugin_id / "manifest.json", {})["id"] == plugin_id
        assert (config / "plugins" / plugin_id / "main.js").stat().st_size > 0
except BaseException:
    for plugin_id in changed:
        dst, old = config / "plugins" / plugin_id, backup / "plugins" / plugin_id
        if dst.exists():
            shutil.rmtree(dst)
        if old.exists():
            shutil.copytree(old, dst)
    for name in ("app.json", "community-plugins.json"):
        dst, old = config / name, backup / name
        if old.exists():
            shutil.copy2(old, dst)
        elif dst.exists():
            dst.unlink()
        tmp = dst.with_name(dst.name + ".setup-tmp")
        if tmp.exists():
            tmp.unlink()
    raise
print(f"Installed/enabled {len(wanted)} plugins; settings preserved. Backup: {backup}")
PY
[[ "$MODE" == apply ]] || exit 0
# Official Qoder native installer, downloaded before execution.
curl -fsSL --retry 3 --proto '=https' --proto-redir '=https' https://qoder.com/install -o "$RUN_DIR/qoder-install.sh"
bash "$RUN_DIR/qoder-install.sh"
export PATH="$HOME/.local/bin:$HOME/.qoder/bin:$HOME/.qoder/entry:$PATH"
qoder --version

if ! command -v am >/dev/null; then
  curl -fsSL --retry 3 --proto '=https' --proto-redir '=https' \
    https://raw.githubusercontent.com/ivan-hc/AM/main/AM-INSTALLER -o "$RUN_DIR/AM-INSTALLER"
  bash "$RUN_DIR/AM-INSTALLER" -i am
fi
# AM manages its own elevation. Its system-managed app directories belong
# to the installing user by design; no blanket sudoers rule is necessary.
am -s
for app_name in "${AM_APPS[@]}"; do
  am -i "$app_name"
  if [[ -f "/opt/$app_name/AM-LOCK" ]]; then
    am unlock "$app_name" # AM may ask its normal unlock question.
  fi
  am -u "$app_name"
done
# Validate existing SSH settings before starting the server.
sudo ssh-keygen -A
sudo /usr/bin/sshd -t
sudo /usr/bin/sshd -T > "$RUN_DIR/sshd-effective.txt"
# Open actual configured ports before starting, only if UFW already enforces rules.
if command -v ufw >/dev/null; then
  sudo env LC_ALL=C ufw status > "$RUN_DIR/ufw-before.txt"
  if grep -q '^Status: active$' "$RUN_DIR/ufw-before.txt"; then
    while read -r ssh_port; do
      sudo ufw allow "$ssh_port/tcp" comment 'SSH remote access'
    done < <(awk '$1 == "port" {print $2}' "$RUN_DIR/sshd-effective.txt")
  fi
fi
systemctl is-enabled sshd > "$RUN_DIR/sshd-enabled-before.txt" 2>&1 || true
systemctl is-active sshd > "$RUN_DIR/sshd-active-before.txt" 2>&1 || true
sudo systemctl enable --now sshd
systemctl is-active --quiet sshd
systemctl is-enabled --quiet sshd
pacman -Q vlc vlc-plugins-all ttf-ms-fonts openssh
echo "Setup complete. Reopen Obsidian to load plugins."
echo "Qoder sign-in, Obsidian runtime checks and remote SSH login were not performed."
echo "SSH login example: ssh $(id -un)@<this-machine-IP>"
echo "SSH listen ports:"
awk '$1 == "port" {print $2}' "$RUN_DIR/sshd-effective.txt"
echo "Local addresses:"
ip -brief address
echo "Reports and backups: $RUN_DIR"
