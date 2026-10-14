# Automatic project GitHub sync — 14 October 2026

Completed setup for end-of-task Codex sync. Standing authorization is saved in Work/AGENTS.md and /home/ivanaguilera/.codex/AGENTS.md. Existing workspace instructions were preserved; original backup is backups/AGENTS-before-sync.md. The global file did not previously exist.

Existing private targets: https://github.com/ivan-esteban23/work-archive and https://github.com/ivan-esteban23/the-reference-edit. The reusable command is sync.py; its scope, policy and examples are documented in README.md. All Work projects and explicitly selected Obsidian project notes use the archive, while verified website commits also push to their own repository. Notion edits require fresh local exports/readbacks before sync.

Initial live run archived 202 added/changed source files, including live Japan/Goth Rock notes, music prompts, maps and relevant Goth Rock snapshot/attachment folders. Original vault files were only read. Both private remotes were verified. The website commit remains 228912190b90435c10a9acbc12b99f068e33c6bf. Initial successful follow-up archive verification: c7024fed70319a0d5b6a0503d72a7dffa1588b8b. See verification.json for the dated setup receipt; subsequent receipt/documentation pushes have later commits.

Seven focused checks passed: explicit exclusions, browser profile pruning, credential abort before a commit, JSON credential detection, authorized source/symlink boundaries, vault copying and idempotent replay, history-preserving explicit deletions, and a website with no LFS files. The first live pass revealed LFS can return files:null for the website; this was corrected and covered by a regression check.

Assets use the standard GitHub LFS API through a bounded HTTP/1.1 client. Credentials are obtained from the signed-in GitHub CLI and are not saved or printed. Already-uploaded objects are skipped. Private repository/account/origin and remote commit are checked. The command does not force-push or silently discard archive edits.

No background watcher was installed. Edits outside Codex are not monitored. Offline/rejected uploads remain pending and must be reported; source files and local commits are retained. Next optional decision is whether to add a separately scoped background watcher for external edits; end-of-task sync is enabled now.
