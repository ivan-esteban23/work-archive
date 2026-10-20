---
tags:
  - automation
  - systemd
  - codex
  - recovery
  - obsidian
created: 2026-10-20
---

# Machine Recovery — Agent Rules, Timers & Codex Fixes

> [!abstract] One-line recovery
> On a fresh Omarchy install: `mise use -g gh` → `gh auth login` → `gh repo clone ivan-esteban23/machine-setup ~/Work/machine-setup` → `cd ~/Work/machine-setup && ./agent-rules-setup --bootstrap`.

Source of truth: private repo **`ivan-esteban23/machine-setup`** (commit `bb9476d`, 2026-10-20). The script is self-contained; `snapshot/` holds this machine's package lists, mise toolset, Codex config, git identity, `allowed_signers`, personal desktop/tool config, and all 30 Obsidian community plugins. Print the full runbook with `agent-rules-setup --restore-guide`.

Related: [[Instagram Downloads — Rules, Commands and Context]]

---

## 1. Quick reference

| Task | Command |
|---|---|
| Apply / repair everything | `agent-rules-setup` |
| Check for drift only | `agent-rules-setup --check` |
| Real Codex sandbox test | `agent-rules-setup --smoke` |
| Full reinstall runbook | `agent-rules-setup --restore-guide` |
| Refresh snapshot | `agent-rules-setup --snapshot` |
| Snapshot + commit + push | `agent-rules-setup --snapshot --push` |
| Snapshot + push + wipe checklist | `agent-rules-setup --pre-reset` |
| Fresh-machine restore | `./agent-rules-setup --bootstrap` |
| Restore only gh + codex tools | `./agent-rules-setup --bootstrap --minimal` |
| Restore full package lists too | `./agent-rules-setup --bootstrap --with-packages` |
| Reinstall every snapshotted package | `agent-rules-setup --install-packages` |
| Report package coverage only | `agent-rules-setup --check --install-packages` |
| Tailscale browser login (manual) | `sudo tailscale up --accept-routes` |
| Overwrite the rule files | `agent-rules-setup --force` |
| Install files but leave systemd alone | `agent-rules-setup --no-enable` |

The script must run **outside** the Codex sandbox — the sandbox cannot write `$HOME`.

---

## 2. Fresh Omarchy restore

Omarchy already provides **mise**, git, yay and systemd, so none of those are reinstalled. `gh` and `codex` are mise tools.

### Step 1 — authenticate to GitHub (repo is private)

```bash
mise use -g gh
gh auth login
```

### Step 2 — clone and bootstrap

```bash
mkdir -p ~/Work
gh repo clone ivan-esteban23/machine-setup ~/Work/machine-setup
cd ~/Work/machine-setup
./agent-rules-setup --bootstrap
```

Optional variants:

```bash
./agent-rules-setup --bootstrap --minimal        # only gh + codex tools
./agent-rules-setup --bootstrap --with-packages  # also reinstall pacman + AUR snapshots
```

### Step 3 — interactive logins

```bash
gh auth setup-git
codex login
sudo tailscale up --accept-routes      # browser auth; the daemon is already set up
```

For Instagram, log into **instagram.com in Firefox**, then prime the saved session once:

```bash
ig-download pdm.clara --new-only --cookies firefox
```

The hourly timers reuse the saved session afterwards. Both Instagram timers share session `ivan_esteban23`, so their hits add up against one rate limit.

### Step 4 — verify

```bash
agent-rules-setup --check
agent-rules-setup --smoke
```

`--smoke` starts a real Codex sandbox and checks DNS, `gh` auth/API, `git ls-remote`, and SSH commit signing.

### Step 5 — sidecar tools and VPN

`qodercli` (Qoder) and `agy` (Antigravity) are installed automatically by the script with their official installers. Only these are not in the repo:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # uv / uvx
uv tool install free-claude-code                  # fcc-* commands
# reason: vendor installer only

sudo cp wg-JP-446.conf /etc/wireguard/            # from secure backup, then:
sudo systemctl enable --now wg-quick@wg-JP-446
```

### Step 6 — Obsidian plugins

All 30 community plugins and their settings live in `snapshot/obsidian/` (`manifest.json`, `main.js`, `styles.css`, `data.json`) with `community-plugins.json`. They are restored automatically once the vault exists. If the vault is copied **after** bootstrap, run `agent-rules-setup` again. Plugin `data.json` files that look like they contain a token are never snapshotted.

---

## 3. What `--bootstrap` does, in order

1. Confirms platform is `omarchy`/`arch` (warns otherwise).
2. Installs missing packages from Omarchy repos: `pacman-contrib`, `tmux`, `libnotify`, `yay`.
3. Installs **`instaloader` from the AUR via `yay`** (not in the official repos).
4. Restores `~/.config/mise/config.toml` from the snapshot, runs `MISE_YES=1 mise install`, then `mise reshim`.
5. Restores personal config that is **missing** — git aliases/ignore, starship, alacritty, Hypr bindings, Omarchy bar layout + default agent, fcitx5 profile + tray drop-in, GTK_IM_MODULE fix, Obsidian vault registry, VS Code settings, Qoder settings, Claude theme — plus `~/.codex/config.toml` and `~/.ssh/allowed_signers`.
6. Restores git identity (`user.name`, `user.email`) and — only if the private key exists — SSH signing settings; configures the `gh` credential helper if authenticated. If the key is missing and signing is on, it turns signing off.
7. Installs `free-claude-code` with `uv tool install` when `uv` is present.
8. Adds a guarded `~/.local/bin` PATH block to `~/.bash_profile` and `~/.bashrc`.
9. Enables systemd linger with `sudo -n loginctl enable-linger "$USER"`.
10. With `--with-packages`, reinstalls the snapshotted explicit pacman and AUR lists.
11. Runs the normal apply: rule files, tools, units, services, timers, Codex sandbox config, Tailscale feature, Qoder/Antigravity CLIs, Obsidian plugins.
12. Prints the remaining interactive steps (gh, codex, Tailscale auth, Instagram, personal data).

`--minimal` skips the full mise toolset and restores only `gh` + `codex`.

### Package restore (`--install-packages`)

`snapshot/packages-explicit.txt` holds the explicit pacman set (195 packages, including `tailscale`) and `packages-aur.txt` the AUR set (`instaloader`, `python-browser-cookie3`, epson driver, `ttf-ms-fonts`).

The explicit list also contains AUR names, so `pacman -S` of the raw list would abort. The script:

1. Reads both snapshots and removes AUR names from the pacman set.
2. Checks each remaining name against `pacman -Ssq`; unknown names are listed and skipped, never passed to a transaction.
3. Installs repo packages with `sudo -n pacman -S --needed --noconfirm` in batches of 50.
4. Installs AUR packages with `yay -S --needed --noconfirm`.

```bash
agent-rules-setup --install-packages            # apply
agent-rules-setup --check --install-packages    # report missing packages only
```

---

## 4. Installed components

### Rule files (written only if missing, or with `--force`)

| File | Purpose |
|---|---|
| `~/AGENTS.md` | Autonomy / no-confirmation rules |
| `~/GEMINI.md` | Same autonomy rules for Gemini CLI |
| `~/.gemini/config/AGENTS.md` | Same autonomy rules for Gemini CLI |
| `~/.qoder/AGENTS.md` | Instagram, monitoring, update checks, account timers, Codex sandbox rules |
| `~/.codex/AGENTS.md` | End-of-task GitHub sync rule |

### Tools in `~/.local/bin`

| Tool | Role |
|---|---|
| `agent-rules-setup` | This installer/checker/snapshotter |
| `ig-download` | Images-only Instagram archiver for any account |
| `download-monitor` | tmux/log progress monitor for long downloads |
| `pdm-clara-autodl` | Hourly pdm.clara poller (newest 36 posts) |
| `system-update-check` | Counts pending pacman + AUR updates |
| `codex-git` | Codex with workspace-write + network + `GH_TOKEN` |
| `gh` | gh wrapper with a read-only-sandbox fallback |
| `obsidian` | CLI bridge to Obsidian's Unix socket |
| `wireguard-jp-toggle` | Japan VPN toggle (`SUPER+SHIFT+V`) |
| `claude`, `codex`, `gemini`, `grok`, `copilot`, `crush`, `opencode`, `pi`, `muse`, `cursor-agent`, `hunk`, `omp`, `ghui`, `playwright` | mise-run wrappers (auto-install on first use) |

### systemd user units (`~/.config/systemd/user/`)

| Unit | Schedule / behavior |
|---|---|
| `pdm-clara-autodl.timer` | Hourly, ±120s; images only; metadata cleaned |
| `julie-autodl.timer` | Hourly, ±300s; `ig-download julie.tuzet --new-only` |
| `system-update-check.timer` | `OnCalendar=00/3:00` → 00:00, 03:00, 06:00… local |
| `codex-remote-control.service` | Codex mobile/browser access, starts at login |
| `qoder-remote-control.service` | Qoder mobile/browser access, starts at login |

All three timers use `Persistent=true` and `RemainAfterElapse=no`.

### Personal config restored from `snapshot/config/`

Only **missing** files are copied; existing local config is never overwritten.

| Area | Files |
|---|---|
| Git | `~/.config/git/config` (aliases, pull/rerere settings), `ignore` |
| Shell / terminal | `~/.config/starship.toml`, `~/.config/alacritty/alacritty.toml` |
| Hyprland | `~/.config/hypr/{autostart,bindings,hyprland,input,looknfeel,monitors}.lua`, `hyprsunset.conf`, `xdph.conf` |
| Omarchy | `~/.config/omarchy/shell.json` (bar layout), `defaults/agent` |
| Input method | `~/.config/fcitx5/profile`, `conf/*.conf`, `~/.config/environment.d/20-fcitx-gtk.conf`, `omarchy-fcitx5.service.d/override.conf` |
| Apps | `~/.config/obsidian/obsidian.json`, `~/.config/Code/User/settings.json`, `~/.qoder/settings.json`, `~/.claude/settings.json` |

### Omarchy Tailscale feature

The script reproduces `omarchy-install-service-tailscale` without the interactive auth step:

| Piece | What is done |
|---|---|
| Package | `sudo -n pacman -S --needed tailscale` |
| Daemon | `sudo -n systemctl enable --now tailscaled.service` |
| Operator | `sudo -n tailscale set --operator=$USER` |
| Taildrop | `systemctl --user enable --now omarchy-tailscale-receive.service` |
| Bar | `omarchy-plugin-enable omarchy.tailscale` (widget appended to the bar's right section) |
| Login | **Manual**: `sudo tailscale up --accept-routes` (browser auth; `tailscale up` blocks, so it is never automated) |

The admin-console web app from Omarchy's installer is skipped because `omarchy-webapp-install` is an interactive TUI; add it from the Omarchy menu if wanted.

### Qoder and Antigravity CLIs

| Tool | Installer |
|---|---|
| `qodercli` | `curl -fsSL https://qoder.com/install \| bash` (binary in `~/.qoder/bin`, symlink `~/.local/bin/qodercli`) |
| `agy` | `curl -fsSL https://antigravity.google/cli/install.sh \| bash` (binary `~/.local/bin/agy`) |

Both are installed only when missing, so the script stays idempotent. Updates: `qodercli update`, `agy update`.

### Obsidian community plugins

30 plugins (~34 MB) are snapshotted under `snapshot/obsidian/`: every plugin folder plus `community-plugins.json` (the enabled list). Restore copies only missing plugin folders and merges the enabled IDs; existing plugin folders and their settings are left alone. A plugin `data.json` is skipped when it matches the token-like pattern the script already uses for Codex config.

---

## 5. Rules enforced

### Autonomy and permissions

- Proceed without confirmation for system changes, package operations, config edits, services/timers, firewall, and GitHub operations (commits, pushes, branches, PRs, issues, workflow runs).
- Passwordless sudo is available (`sudo -n`).
- Pause only for credentials/2FA or a genuinely ambiguous request.

### Instagram archives

1. **Images only** — never download videos; video posts keep only their `.jpg` thumbnail.
2. **Clean archive** — delete all `*.txt` captions and `*.json.xz` metadata in the target folder at the end (also on Ctrl+C/errors).
3. **Resume-safe batches** — posts already on disk are skipped by UTC-timestamp filename prefix.
4. **Rate limits** — roughly 350–450 post fetches/hour; instaloader sleeps through HTTP 429 pauses. Use tmux for long runs.

### Download monitoring

- Long downloads run in tmux.
- Report progress roughly every 20 posts or 20%.
- Report errors and rate-limit pauses.
- Report the final count and cleanup status.
- Never leave a download running unmonitored.

`download-monitor` attaches to a tmux session named `ig-*`/`instaloader*`, or shows the last progress lines with `download-monitor --logs`.

### System update checks

- Every 3 hours via `system-update-check.timer`.
- Log: `~/.local/state/system-update-check.log`.
- Report pacman and AUR counts; show lists when asked.
- **Never install or upgrade packages automatically.**

### Account monitoring

- `pdm.clara` → `pdm-clara-autodl.timer` (saved session).
- `julie.tuzet` → `julie-autodl.timer` (`ig-download … --new-only --session ivan_esteban23`).
- Keep both enabled unless told otherwise.
- Add another account with a matching service/timer pair using `ig-download <account> --new-only --session ivan_esteban23`.
- `katarinabluu` is **manual-only** (no timer): `ig-download katarinabluu --session ivan_esteban23` in tmux, in batches.

> [!tip] Timer scheduling rule
> Use `OnCalendar=…` + `RemainAfterElapse=no`. A monotonic `OnBootSec`/`OnUnitActiveSec` pair can wedge at `next_elapse=0` after a failed run, leaving the timer `active (elapsed)` with no next fire.

### Codex sandbox / GitHub

- Default Codex sandbox stays `read-only`.
- Use `codex-git` for any push/merge/PR work.
- `[sandbox_workspace_write] network_access = true` is in `~/.codex/config.toml`.
- Verified in-sandbox: `gh api user`, `gh pr view`, `git ls-remote`, `git push`, SSH commit signing.
- Repo/TMPDIR writes work; writes outside the workspace (e.g. `$HOME`) stay blocked.
- `codex -p <profile> sandbox` loads the profile but ignores its `sandbox_mode`; only `-c` overrides take effect there.

### End-of-task GitHub sync

After completed tasks that change files in `~/Work` or `~/Documents/Obsidian Vault`:

```bash
python ~/Work/github-project-sync/sync.py \
  --path '/absolute/path/to/changed-file-or-folder' \
  --message 'short description'
```

- Repeat `--path` for every changed note, attachment, export, or script.
- Website commits go to `ivan-esteban23/the-reference-edit`; Work/Vault files go to `ivan-esteban23/work-archive`.
- For intentionally removed files use `--delete '/original/path'`.
- Never select all of Work or the whole vault; scope to task-owned files.
- Preserve credentials, unrelated edits, and history. Never force-push. If offline, keep local work and report the upload as pending.

---

## 6. Why Codex PRs used to fail

| Cause | Effect | Fix |
|---|---|---|
| Default sandbox is read-only with no network | No DNS; `gh`/`git push` cannot reach GitHub | `codex-git` uses `workspace-write` + network |
| No `GH_TOKEN` inside the sandbox | `gh` reports the keyring token as invalid | `codex-git` exports `GH_TOKEN` |
| Login shells re-prepend `~/.local/bin` | `gh` hits the auto-update wrapper, which runs `mise use -g` and exits on the read-only FS | `gh` wrapper falls back to the installed mise shim |

`codex-git` also puts mise shims first and passes `shell_environment_policy.inherit=all`.

Config change applied to `~/.codex/config.toml`:

```toml
sandbox_mode = "read-only"

[sandbox_workspace_write]
network_access = true
```

---

## 7. Tool usage

### `ig-download`

```bash
ig-download USER                   # next 100 new posts, Firefox cookies
ig-download USER -n 300            # 300 posts this run
ig-download USER --all             # everything remaining
ig-download USER --new-only        # only newest 36 posts
ig-download USER -d /path          # parent dir → /path/USER/
ig-download USER --cookies chrome
ig-download USER --cookiefile /path/cookies.sqlite
ig-download USER --session ivan_esteban23
ig-download USER --login your_ig_user   # interactive + 2FA, saves session
```

| Option | Meaning |
|---|---|
| `-n, --count N` | Posts this run (default 100; `0` = all) |
| `--all` | Same as `--count 0` |
| `--new-only` | Scan only the newest 36 posts |
| `-d, --base-dir DIR` | Parent download directory (default `~/Downloads`) |
| `--cookies BROWSER` | firefox, chrome, chromium, brave, edge, librewolf, opera, vivaldi |
| `--cookiefile PATH` | Explicit `cookies.sqlite` |
| `--session USER` | `~/.config/instaloader/session-USER` |
| `--login USER` | Interactive login, saves the session |

Default layout: `~/Downloads/<account>/<UTC timestamp>_UTC[_n].jpg`.

### `codex-git`

Same arguments as `codex`:

```bash
codex-git
codex-git exec "run the tests and push the branch"
```

### `system-update-check`

```bash
system-update-check
```

Runs `checkupdates` and `yay -Qua`, logs the summary, sends a desktop notification when updates exist, and prints the package lists.

### Timer operations

```bash
systemctl --user list-timers pdm-clara-autodl.timer julie-autodl.timer system-update-check.timer
systemctl --user status julie-autodl.timer
systemctl --user start julie-autodl.service                 # run once now
journalctl --user -u julie-autodl.service -n 50 --no-pager
systemctl --user show system-update-check.timer -p TimersCalendar,NextElapseUSecRealtime
```

---

## 8. Snapshot before resetting

```bash
cd ~/Work/machine-setup
./agent-rules-setup --pre-reset     # snapshot + commit + push + full runbook
```

`--snapshot --push` does the same without printing the runbook.

### Included in `snapshot/`

| File | Contents |
|---|---|
| `packages-explicit.txt` | All explicit pacman packages (195 as of 2026-10-20, includes `tailscale`) |
| `packages-aur.txt` | Foreign/AUR packages (4: instaloader, python-browser-cookie3, epson driver, ttf-ms-fonts) |
| `mise-config.toml` | Full global mise toolset |
| `codex-config.toml` | Codex config; skipped if a token-like value is detected |
| `allowed_signers` | Public signing-key allowlist |
| `git-user-name`, `git-user-email` | Commit identity |
| `git-signing-key`, `git-signing-format`, `git-allowed-signers` | Signing settings (path only) |
| `config/` | 26 personal config files (git, starship, alacritty, Hypr, Omarchy, fcitx5, Obsidian, VS Code, Qoder, Claude), token-scanned before copying |
| `obsidian/community-plugins.json` | Enabled plugin IDs |
| `obsidian/plugins/<id>/` | All 30 community plugins with settings (~34 MB), token-scanned before copying |

### NOT in the repo — back these up separately

| Path | Why |
|---|---|
| `~/.ssh/` | Private commit-signing key + `allowed_signers` |
| `~/.codex/auth.json` | Codex login |
| `~/.config/gh/hosts.yml` | gh token |
| `~/.config/instaloader/session-*` | Instagram session |
| `~/.secrets/github-token` | Local token copy |
| `~/.fcc/.env` | free-claude-code credentials |
| `~/.bashrc` | Contains `TAVILY_API_KEY` |
| `/etc/wireguard/wg-JP-446.conf` | VPN private key (root-owned) |
| `~/Downloads` | Instagram archives |
| `~/Work` | Projects |
| `~/Documents/Obsidian Vault` | Notes and attachments (plugin folders are in `snapshot/obsidian/`) |
| `~/Pictures`, `~/Videos` | Personal media |

If the private signing key is missing after restore, bootstrap turns `commit.gpgsign` off and prints instructions. Do not regenerate it unless the new public key is registered as a GitHub signing key.

The repo is private. To restore without GitHub auth, copy the directory to a USB stick, or make it public with `gh repo edit ivan-esteban23/machine-setup --visibility public`.

---

## 9. Verification

```bash
agent-rules-setup --check
```

Checks: all managed files and snapshot configs match, timers are enabled + active + have a next elapse, remote-control services are enabled, required commands exist (`mise`, `git`, `tmux`, `checkupdates`, `python3`, `gh`, `codex`, `flock`), the Tailscale package/daemon/Taildrop/bar widget state, Qoder + Antigravity CLIs, every snapshotted package is installed, Obsidian plugins are present, Python can `import instaloader`, mise resolves `gh`/`codex`, `uv` has `free-claude-code`, the WireGuard config is present, and reports auth status.

Targeted checks:

```bash
agent-rules-setup --check --install-packages   # package coverage
systemctl --user status omarchy-tailscale-receive.service
tailscale status                               # exit 1 = not logged in
jq -c '[.bar.layout[]?[]? | if type=="object" then .id else . end]' ~/.config/omarchy/shell.json
```

```bash
agent-rules-setup --smoke
```

Runs a real `codex sandbox` with workspace-write + network and verifies:

1. `getent hosts github.com`
2. `~/.local/bin/gh auth status`
3. `gh api user` (token + API)
4. `git ls-remote` against a real repo
5. Signed empty commit (`Good "git" signature`)

Current verified result: **0 drift**, smoke passes all five.

---

## 10. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Codex says repo not found / DNS failure | Read-only sandbox, no network | Use `codex-git`, not bare `codex` |
| `mise ERROR … Read-only file system` in sandbox | `~/.local/bin` wrapper ran `mise use` | Fixed `gh` fallback; keep shims first |
| `gh` says token invalid in sandbox | No `GH_TOKEN` | Use `codex-git`; it exports the token |
| Timer `active (elapsed)`, `next=none` | Monotonic timer wedged after failure | Re-apply; uses `OnCalendar` + `RemainAfterElapse=no` |
| Timers stop after logout | Linger disabled | `sudo -n loginctl enable-linger $USER` |
| Instagram `400 feedback_required` | Rate limit | Stop hammering; wait; re-login via Firefox cookies |
| Commit signing fails | Signing key missing | Restore `~/.ssh/id_ed25519_signing`; signing stays off until then |
| Restore is missing `instaloader` | AUR-only package | `yay -S instaloader` (bootstrap does this) |
| Private repo clone fails | Not authenticated | `mise use -g gh && gh auth login` first |
| Remote-control service keeps restarting | `qodercli`/`codex` missing or not logged in | Reinstall the sidecar CLI, sign in, `systemctl --user restart <unit>` |
| Personal config was not restored | A file already exists at that path | Restore is missing-only by design; copy from `snapshot/config/` manually |
| `tailscale up` hangs | It waits for browser authentication | Complete the login in the browser; that step is never automated |
| Tailscale bar widget missing | `omarchy-plugin-enable` hit the shell's 2s IPC timeout | Run `omarchy-plugin-enable omarchy.tailscale` again (the script retries once) |
| `omarchy-shell is not responding` | The quickshell IPC is busy or the shell is not running | Check `pgrep -af quickshell`; log into the desktop session and retry |
| Package reinstall aborts on an AUR name | Raw explicit list contains AUR names | Use `agent-rules-setup --install-packages`; it filters AUR names and verifies repos |
| Obsidian plugins missing after bootstrap | Vault copied after the script ran | Run `agent-rules-setup` again once the vault exists |
| Need to undo a managed file | Backup exists | Restore from `<file>.bak-agent-rules` |

---

## 11. Do I need TypeScript or React installed?

**No — not for this setup or the recovery kit.**

- The automation stack is **bash + systemd + Python/instaloader**, plus Codex/gh as mise tools.
- TypeScript and React are **per-project dependencies**, not system languages. Each web repo declares them in `package.json`; run the repo's `npm install` (or pnpm/yarn) and it fetches the right versions.
- React is a library, never a global install.
- A global `tsc` is optional; `npm install -g typescript` only if you want the compiler available outside a project.
- Node **26.8.2** is already in the mise snapshot, so a fresh restore brings it back automatically.
- For `the-reference-edit` / `visual-edit-public`, use the project's own install/build commands. No extra system packages are needed for the rules, timers, or Codex sandbox fixes.

---

## 12. Files and rollback

- Managed scripts: `~/.local/bin/*`
- Units: `~/.config/systemd/user/*.service`, `*.timer` (timers + `codex-remote-control`, `qoder-remote-control`)
- Codex config: `~/.codex/config.toml` (backup: `config.toml.bak-agent-rules`)
- Rule files: `~/AGENTS.md`, `~/GEMINI.md`, `~/.gemini/config/AGENTS.md`, `~/.qoder/AGENTS.md`, `~/.codex/AGENTS.md`
- Personal config: `snapshot/config/` → restored only when missing
- Obsidian plugins: `snapshot/obsidian/` → missing plugin folders + enabled list
- Tailscale: `tailscale` package, `tailscaled.service` (system), `~/.config/systemd/user/omarchy-tailscale-receive.service`, `omarchy.tailscale` bar widget in `~/.config/omarchy/shell.json`
- Update log: `~/.local/state/system-update-check.log`
- Recovery repo: `~/Work/machine-setup` → `https://github.com/ivan-esteban23/machine-setup` (private)

Every overwritten managed file keeps a one-time `.bak-agent-rules` backup. The recovery repo's git history records each snapshot.
