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

Source of truth: private repo **`ivan-esteban23/machine-setup`** (commit `bd98835`, 2026-10-20). The script is self-contained; `snapshot/` holds this machine's package lists, mise toolset, Codex config, git identity and `allowed_signers`.

Related: [[Instagram Downloads — Rules, Commands and Context]]

---

## 1. Quick reference

| Task | Command |
|---|---|
| Apply / repair everything | `agent-rules-setup` |
| Check for drift only | `agent-rules-setup --check` |
| Real Codex sandbox test | `agent-rules-setup --smoke` |
| Refresh snapshot | `agent-rules-setup --snapshot` |
| Snapshot + commit + push | `agent-rules-setup --snapshot --push` |
| Fresh-machine restore | `./agent-rules-setup --bootstrap` |
| Restore only gh + codex tools | `./agent-rules-setup --bootstrap --minimal` |
| Restore full package lists too | `./agent-rules-setup --bootstrap --with-packages` |
| Overwrite the three AGENTS.md files | `agent-rules-setup --force` |
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

---

## 3. What `--bootstrap` does, in order

1. Confirms platform is `omarchy`/`arch` (warns otherwise).
2. Installs missing packages from Omarchy repos: `pacman-contrib`, `tmux`, `libnotify`, `yay`.
3. Installs **`instaloader` from the AUR via `yay`** (not in the official repos).
4. Restores `~/.config/mise/config.toml` from the snapshot, runs `MISE_YES=1 mise install`, then `mise reshim`.
5. Restores `~/.codex/config.toml` and `~/.ssh/allowed_signers`.
6. Restores git identity (`user.name`, `user.email`) and — only if the private key exists — SSH signing settings; configures the `gh` credential helper if authenticated.
7. Adds a guarded `~/.local/bin` PATH block to `~/.bash_profile` and `~/.bashrc`.
8. Enables systemd linger with `sudo -n loginctl enable-linger "$USER"`.
9. With `--with-packages`, reinstalls the snapshotted explicit pacman and AUR lists.
10. Runs the normal apply: rule files, tools, units, timers, Codex sandbox config.
11. Prints the remaining interactive steps (gh, codex, Instagram, personal data).

`--minimal` skips the full mise toolset and restores only `gh` + `codex`.

---

## 4. Installed components

### Rule files (written only if missing, or with `--force`)

| File | Purpose |
|---|---|
| `~/AGENTS.md` | Autonomy / no-confirmation rules |
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

### systemd user units (`~/.config/systemd/user/`)

| Unit | Schedule / behavior |
|---|---|
| `pdm-clara-autodl.timer` | Hourly, ±120s; images only; metadata cleaned |
| `julie-autodl.timer` | Hourly, ±300s; `ig-download julie.tuzet --new-only` |
| `system-update-check.timer` | `OnCalendar=00/3:00` → 00:00, 03:00, 06:00… local |

All three use `Persistent=true` and `RemainAfterElapse=no`.

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
./agent-rules-setup --snapshot --push
```

### Included in `snapshot/`

| File | Contents |
|---|---|
| `packages-explicit.txt` | All explicit pacman packages (194 as of 2026-10-20) |
| `packages-aur.txt` | Foreign/AUR packages (4: instaloader, python-browser-cookie3, epson driver, ttf-ms-fonts) |
| `mise-config.toml` | Full global mise toolset |
| `codex-config.toml` | Codex config; skipped if a token-like value is detected |
| `allowed_signers` | Public signing-key allowlist |
| `git-user-name`, `git-user-email` | Commit identity |
| `git-signing-key`, `git-signing-format`, `git-allowed-signers` | Signing settings (path only) |

### NOT in the repo — back these up separately

| Path | Why |
|---|---|
| `~/.ssh/id_ed25519_signing` | Private commit-signing key |
| `~/.codex/auth.json` | Codex login |
| `~/.config/instaloader/session-*` | Instagram session |
| `~/Downloads` | Instagram archives |
| `~/Work` | Projects |
| `~/Documents/Obsidian Vault` | Notes and attachments |

If the private signing key is missing after restore, bootstrap leaves `commit.gpgsign` off and prints instructions. Do not regenerate it unless the new public key is registered as a GitHub signing key.

The repo is private. To restore without GitHub auth, copy the directory to a USB stick, or make it public with `gh repo edit ivan-esteban23/machine-setup --visibility public`.

---

## 9. Verification

```bash
agent-rules-setup --check
```

Checks: all managed files match, timers are enabled + active + have a next elapse, required commands exist (`mise`, `git`, `tmux`, `checkupdates`, `python3`, `gh`, `codex`), Python can `import instaloader`, mise resolves `gh`/`codex`, and reports auth status.

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
- Units: `~/.config/systemd/user/*.service`, `*.timer`
- Codex config: `~/.codex/config.toml` (backup: `config.toml.bak-agent-rules`)
- Rule files: `~/AGENTS.md`, `~/.qoder/AGENTS.md`, `~/.codex/AGENTS.md`
- Update log: `~/.local/state/system-update-check.log`
- Recovery repo: `~/Work/machine-setup` → `https://github.com/ivan-esteban23/machine-setup` (private)

Every overwritten managed file keeps a one-time `.bak-agent-rules` backup. The recovery repo's git history records each snapshot.
