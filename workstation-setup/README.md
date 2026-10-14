# Workstation setup
Prepared 2026-10-12 for this Omarchy/Arch workstation.

Run as your regular user in a terminal, without sudo:
```bash
bash /home/ivanaguilera/Work/workstation-setup/setup.sh
# Close Obsidian, then apply:
bash /home/ivanaguilera/Work/workstation-setup/setup.sh --apply
```

The default prints a plan and makes no changes. `--download-only` stages and validates missing plugin downloads, preserving the live vault. `--vault PATH` selects a different existing vault. `--backup-root PATH` changes the staging/backup directory.

The baseline is the 16 enabled plugins found in your vault: Map View, Local Images Plus, Meta Bind, Omnisearch, PDF++, Spaced Repetition, Tracker, QuickAdd, Templater, Tasks, Calendar, Advanced Tables, Tag Wrangler, Dataview, Minimal Theme Settings and Style Settings. The installer also includes installed/enabled plugins discovered at runtime.

Four GitHub additions:
- [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin): diagrams and visual notes.
- [Linter](https://github.com/platers/obsidian-linter): configurable Markdown formatting.
- [Note Toolbar](https://github.com/chrisgurney/obsidian-note-toolbar): shortcuts in notes.
- [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes): daily/weekly/monthly notes.

This is a selected set, not the entire community catalog. Complete existing plugins remain at their installed versions. Missing plugins come from latest stable GitHub release assets, resolved through [Obsidian's registry](https://github.com/obsidianmd/obsidian-releases/blob/master/community-plugins.json). The report records versions, source repositories, minimum Obsidian versions and downloaded asset hashes. Check the recorded minimum versions against your Obsidian version; loading inside Obsidian has not been tested.

The installer backs up all .obsidian files before applying plugin changes, preserves plugin data.json settings and unrelated configuration, verifies saved assets and settings, and restores changed plugin directories and configuration if the plugin application step fails. It sets app.json safeMode=false: community plugins require Restricted Mode to be off. Reopen Obsidian after completion. Linter rules, templates and toolbar layouts can then be configured in the app.

System actions:
- Installs missing VLC, vlc-plugins-all and OpenSSH through Omarchy's package helper; ttf-ms-fonts uses an enabled repository if available, otherwise Omarchy's AUR helper. Refreshes the font cache.
- Installs Qoder using [the official native installer](https://docs.qoder.com/cli/installation), fetched with curl from https://qoder.com/install and executed as your user. Sign-in remains interactive.
- Installs [ivan-hc AM](https://github.com/ivan-hc/AM#installation) if missing, then synchronizes the manager with am -s. AM handles its normal sudo operations internally.
- For specific AM apps, add repeated --am-app flags, e.g. --am-app obsidian. The script installs them, uses am unlock when /opt/NAME/AM-LOCK exists, then runs am -u NAME. No app list was supplied, so the default does not update every unrelated app. AM's own prompts may appear. No blanket passwordless sudo or filesystem permission changes are added.
- Validates SSH configuration, creates missing host keys, opens configured TCP ports when UFW is active, and enables/starts sshd. Existing SSH authentication policy remains in effect. Other firewalls and router port forwarding are not configured. Remote login is not tested.

Each run has its own backups and reports under workstation-setup/backups. System package operations, Qoder/AM installers and SSH changes are not automatically rolled back if a later step fails. Existing SSH configuration files are not overwritten. The script stops on errors so rerunning can continue with installed components.

Verification performed by the author is documented in validation.txt. Building this script does not execute its system changes.
