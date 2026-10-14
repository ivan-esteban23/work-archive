# Mobile UI branch merged — 14 October 2026

PR: https://github.com/ivan-esteban23/the-reference-edit/pull/1
State: MERGED. Squash commit: 746988f5781dced727f59a37dcd0f61bdf349db6.

The user supplied /home/ivanaguilera/Downloads/codex-merge-prompt.md, requesting a PR from v0/mobile-ui-cards-header to main, checked then squash-merged and deleted. Initial branch was one commit ahead of main, with no missing main commits. Only dist/index.html and dist/sw.js differed.

The initial browser review found a 320 px regression: document width 323 px and a wrapped masthead; main had no horizontal overflow at the same viewport. User explicitly approved fixing it before continuing. Original branch files were backed up in backup/dist/. Fix commit: 0a69136ed77898c209025821d8767bb3e9e62afc.

Changes: keep masthead controls beside the brand at normal text sizes; allow the brand text to wrap within its column; make mobile search and Filters a two-column grid, overriding the inherited full-width Filters rule. At enlarged text sizes, allow controls to stack. Service-worker cache key bumped from mobile-ui v1 to v2; worker logic was not modified.

Validation: 96 combinations of 320/390/768/1440 px widths, normal/200% root text, six languages, and both themes passed. Source records (58), metadata, anchor URLs and images preserved. Search, country filtering and badge reset, theme/favorite persistence, language code synchronization, print detail expansion, inline-script and worker syntax checks passed; no JavaScript exceptions observed. git diff --check passed. Reviewed 320 px light and settled 390 px dark screenshots.

Browser reload stalled through the localhost service-worker path. UI checks were completed with Network.setBypassServiceWorker enabled; offline migration is explicitly untested in this run. See qa-results.json, layout-results.json and check.mjs. The earlier 390 px screenshot captured a color transition; the settled screenshot is the final dark preview.

GitHub reported no checks, and statusCheckRollup was empty. Mergeability was CLEAN. Immediately before merging, ancestry, exact reviewed head and the two-file scope were rechecked. Squash merge used --match-head-commit and no admin override. Both remote and local feature branches were removed, with local removal after verifying tree equality with the squash merge. Local main was fast-forwarded and is clean.

Latest website commits:
- 746988f Compact mobile UI: shorter cards, slimmer sticky search bar, one-row header (#1)
- 2289121 Update Site source
- e596d2c Update Site source

This task updated GitHub source and the local checkout. No hosted Sites deployment was performed; live-site publication is a separate step. Original prompt did not authorize changing repository settings or bypassing branch protection, and neither was done.
