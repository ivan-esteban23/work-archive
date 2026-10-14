# Workspace instructions

## Purpose and locations

This workspace contains research, scripts, staged updates, and backups for the user's personal travel guides. The active travel notes live in the local Obsidian vault, not in Google Drive.

- Live vault: `/home/ivanaguilera/Documents/Obsidian Vault`
- Japan research and backups: `/home/ivanaguilera/Work/japan-guide-update`
- Earlier resume reference: `japan-guide-update/session/RESUME.md`
- Current Japan dashboard: `Japan 2027 — Start Here.md` in the live vault
- Current full guide: `Japan Travel Guide 2027.md` in the live vault

These instructions apply to travel-guide work. For unrelated tasks, follow the user's request and the relevant project instructions.

## Resume from current notes

When asked to continue a saved guide, read the relevant live dashboard, latest dated session recap, and notes needed for the requested task. The vault may contain newer material than the workspace's recap or staged copies. Treat live notes as the source of truth for existing content, and resolve conflicts using the user's latest instructions.

Use the guide's current dates, itinerary, budget, and interests as provisional context. Do not treat estimated costs, proposed dates, research ideas, or optional city chapters as confirmed bookings. Check traveler count and rooms before interpreting quotes; check passport nationality when entry or transit rules depend on it.

Japan interests recorded in the guide include photography and filming, matcha, cafés, food, vintage clothing, vinyl records, film-related shops, hobby browsing, and meaningful gifts. Use only the interests relevant to the current request. Keep other travel guides, including Korea, separate unless the user asks to connect them.

## Research and connected tools

Use available connected tools when they fit the request: Klook for tours/experiences, Skyscanner for flights, and Tripadvisor for hotel research. Discover current capabilities and connection state rather than assuming a tool is still available. Booking.com or another app may require setup; do not claim sign-in, installation, or connection without evidence.

**Web search and scraping fallbacks:** Tavily, fastCRW (`crw_scrape`, `crw_search`, `crw_crawl`, `crw_map`), and direct page fetches are all available for research. If one search provider fails, rate-limits, or returns irrelevant results, use whichever of the others works rather than stopping or reporting failure. Prefer opening the authoritative page directly for facts (artist, label, or official site) over relying on a search snippet. See `Music Research Tooling.md` in the Obsidian vault root for connection details, key locations, and known rate limits.

For time-sensitive facts, use current provider or official sources. Record the research date and put source links next to the relevant facts. Preserve the currency, displayed amount, applicable dates, and stated pricing unit. Distinguish search prices from exact-date quotes and final booking totals; do not assume private-tour prices are group totals or that minimum listing prices include all package options.

Check actual destination, departure point, route, season, package inclusions, language, and cancellation terms before presenting an option as a match. A geographic search may return unrelated activities. Label inconsistent titles/summaries and missing details; exclude mismatches instead of inventing coverage. An empty or irrelevant result does not prove no options exist.

Flights departing Santiago and arriving Japan use different local dates. Hotel comparisons need actual check-in/out dates, room count, occupancy, taxes, and full-stay totals. Hotel guest review scores are distinct from property star classifications. Follow each provider's current attribution requirements and tool constraints.

## Update the vault carefully

When the user asks to add or update guide content, make the requested changes and link them from the relevant dashboard or chapter. Prefer a focused addition over replacing a long existing guide. Preserve user-written content, note names, Obsidian wiki links, attachments, source links, and unrelated plugin settings.

Keep research shortlists separate from confirmed reservation records. Add a reservation to the booking ledger only when the user chooses it or supplies an actual confirmation. Do not book, pay, cancel, contact businesses, or alter confirmed travel arrangements unless explicitly requested.

Before overwriting an existing note or plugin configuration, save a backup under a task-specific directory in the workspace. Read the current file immediately before applying a prepared update and check for changes made while working. Existing build scripts may contain old content, fixed dates, non-idempotent edits, or direct vault writes; inspect them before reuse.

The Documents vault may be outside the writable sandbox. Prepare and check the update in the workspace, then use the normal approval/escalation mechanism when required. These instructions do not expand filesystem permissions. A request to edit a guide already authorizes the scoped edit; do not add a separate confirmation step unless genuinely required.

Do not alter `.obsidian` settings, install plugins, or restart Obsidian merely to edit travel notes. When plugin work is requested, preserve unrelated settings and distinguish configuration checks from features actually tested inside Obsidian.

## Verify and communicate

After saving, read back the changed files. Verify new wiki-link targets, section anchors, source URLs, dates/night counts where relevant, and figures copied from research. For ordinary Markdown updates, focused checks are enough; do not add a test suite or rerun every historical script.

For substantial continuations, update the latest session recap with the work completed and the next unresolved decisions. Keep historical recaps intact. End with a concise description of what changed, a clickable link to the main result, and any material uncertainty, such as unconfirmed future availability. Never claim a booking, sign-in, offline download, reminder, or live feature test that was not performed.

## Music projects and prompt organization

The user wants a separate ChatGPT research/listening project for each music topic and a shared prompt directory in the live Obsidian vault.

- Music prompt directory: `/home/ivanaguilera/Documents/Obsidian Vault/Music Prompts`
- Shared index: `Music Prompt Library.md` in that directory
- New-project template: `Music Project Starter Template.md` in that directory
- Keep topic prompt and project-instruction notes in this directory, using `[Topic] — ChatGPT Project Prompts.md` and `[Topic] — ChatGPT Project Instructions.md`; link them from the shared index and the topic's dashboard.
- Keep music topics' research, listening feedback, and personal rankings separate from each other and from travel projects. Do not infer that an album was heard or personally rated.
- ChatGPT uploads are snapshots and do not automatically synchronize with Obsidian. Preserve existing note names, links, and sources; back up existing notes before changes, use normal filesystem escalation when required, and read back saved updates. Do not alter `.obsidian` settings for ordinary note work.
