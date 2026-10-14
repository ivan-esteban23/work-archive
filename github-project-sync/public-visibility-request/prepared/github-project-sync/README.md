# Automatic GitHub sync after project updates

Enabled workflow: after each completed Codex task that changes project files, sync the files produced by that task to the existing public repositories. The instruction is saved in Work's `AGENTS.md` and the user's global Codex `AGENTS.md`, so it also applies when opening a project separately. This is a Codex working agreement and a tested command, not a background filesystem watcher.

| Source | GitHub destination |
| --- | --- |
| Website commits in `Work/visual-edit-public` | `ivan-esteban23/the-reference-edit` |
| Each project's notes, scripts, exports and assets in Work | Same relative folders in `ivan-esteban23/work-archive` |
| Relevant live Obsidian project files | `Obsidian Vault/` in `ivan-esteban23/work-archive`, preserving note and attachment paths |
| Notion project updates | Save fresh readbacks/exports of the edited pages in the project Work folder, then sync those files |

Projects do not need separate repositories. New projects anywhere in Work use the same command. Files in the Obsidian vault must be explicitly selected. No Obsidian settings are modified. A dated Notion export stays a dated export; do not describe it as current without fetching updated content.

Run after the task's normal focused verification:

```bash
python /home/ivanaguilera/Work/github-project-sync/sync.py \
  --path '/home/ivanaguilera/Documents/Obsidian Vault/Japan Travel Guide 2027.md' \
  --path '/home/ivanaguilera/Work/japan-guide-update/new-research' \
  --message 'Japan: update the completed research'
```

Repeat `--path` for every changed note, attachment, export or script. A complete task-owned project folder is also supported. Select the actual files touched by the task; do not select all of Work or the whole vault. Shared music prompt notes, indexes, dashboards and relevant linked attachments should accompany a topic update when changed. The guide's live files remain the source of truth.

For the website, create the normal tested website commit first, then pass its changed files or its source directory to the command. It uploads that commit and archives the selected working files. The command refuses to commit unrelated dirty website files. GitHub source sync and website deployment remain separate steps in the existing website workflow.

Use `--dry-run` to inspect a scope without copying, committing or uploading. For an intentionally removed source file, pass `--delete '/original/path'`; the command requires that the file is already absent and previously archived. Renames use a new `--path` and an old `--delete`. A directory selection does not infer deletions.

Unchanged files do not create a new commit. The command preserves the previous archive's credential exclusions, omits browser profiles, Git internals, dependency caches, symlinks and environment files, and checks new/changed text, JSON and ZIP content for credential candidates. Detection is a focused safeguard, not a comprehensive secret audit. Large assets use Git LFS; the manifest records original SHA-256 hashes. Use the exclusion policy in `_github-upload/excluded.json` as the baseline, and never bypass it to force credentials online.

Local commits are kept if a network transfer fails. Retry the same scope when connectivity returns. The command never force-pushes, resets history, resolves remote divergence, or silently discards pending archive edits. If the archive checkout has pending changes after an interrupted copy, inspect and reconcile those changes before rerunning. Report a failed push as pending, with its local commit if one was created.

GitHub authorization is standing authorization for these scoped uploads to these two public repositories; no separate conversational permission question is needed. Use the normal filesystem/network escalation mechanism when the environment requires it. If a reviewer blocks the action, report the actual rejection rather than claiming success.

Configuration: `config.json`. Archive checkout: `/home/ivanaguilera/Work/github-upload-preparation-20261014/work-archive`. Local Git LFS binary is retained in the prior upload preparation directory; keep it or update the configured location. GitHub CLI is resolved to its installed binary to avoid the copied mise launcher configuration.

Verification: `python -m unittest discover -s github-project-sync -p test_sync.py -v`. Live sync results are saved in `verification.json` after initial setup. Saved instructions take effect in future sessions; external edits in Obsidian/Notion and edits outside Codex do not trigger this workflow themselves.

Instruction discovery follows [official OpenAI documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Asset transfer follows the [Git LFS basic transfer API](https://github.com/git-lfs/git-lfs/blob/main/docs/api/basic-transfers.md).

Repository visibility changed to public at the user's request on 14 October 2026. The sync command verifies the configured `PUBLIC` policy before uploading. Credential and cache exclusions continue to apply.
