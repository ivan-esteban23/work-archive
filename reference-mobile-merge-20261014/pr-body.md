Cards now show the source name, purpose and a category · country · access summary. Language, content, coverage and review dates remain available in More details. The search bar contains search and Filters, with results and Reset below it; the phone Filters button shows the active-filter count. Brand, theme toggle and a compact language picker share the masthead, replacing the separate Appearance bar.

The 320 px follow-up removes an inherited full-width Filters rule and keeps the masthead controls beside the brand. At enlarged text sizes, controls can stack to remain readable. The service-worker cache key is bumped to refresh the offline shell.

Validation:
- Passed 96 browser layout combinations: 320/390/768/1440 px, normal/200% root text, six languages, and light/dark themes.
- Search, country filtering, badge reset, theme/favorite persistence, language labels and print-detail expansion passed; no JavaScript exceptions observed.
- All 58 source records, links and images preserved; inline scripts and service worker compile; git diff --check passes.
- Reviewed 320 px light and 390 px dark previews. Browser UI checks bypassed the localhost service-worker cache path after its reload stalled. Offline migration was not tested in this run; the worker's only change is its cache key.
