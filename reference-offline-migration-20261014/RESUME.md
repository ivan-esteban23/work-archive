# Website version 43 and offline migration — 14 October 2026

User requested updating the website and offline migration following the merged mobile UI PR.

Live URL: https://visual-edit-ivan.greymelon66.chatgpt.site
GitHub: https://github.com/ivan-esteban23/the-reference-edit
Published source: `746988f5781dced727f59a37dcd0f61bdf349db6` (main).
Site project: `appgprj_6ace7cad170c8191adbe36fd345102d0`.
Saved version: `appgprj_6ace7cad170c8191adbe36fd345102d0~appgver_e90028e9a89c8191847e3fe43e84245e`, number 43.
Deployment: `appgdep_6ad00d5276288191a1a0fc6c6a5db7e2`, native status succeeded.
Existing public audience preserved. See deployment.json for native receipt and package hash.

Used Sites skill. Opened native source in isolated site-source/ checkout at version 42, then fast-forwarded it from the verified GitHub checkout. Source helper pushed exact merged commit and packaged dist/ with the existing hosting manifest. Saved and published through native Sites tools. No additional website source changes were needed. GitHub checkout remains clean main. The initial helper attempt from Work failed without preparing a checkout; reopening in the empty task source directory succeeded.

Actual service-worker upgrade tested in isolated Chromium with bypass disabled, from version 42's `visual-edit-shell-reference-name-20261014-v1` to `visual-edit-shell-mobile-ui-20261014-v2`. Local HTTP server used actual old/new assets and /index.html-to-root redirects. Two URL-based favorites, explicit dark mode and Spanish were seeded using old UI controls. A deliberately failed icon download left the old worker and cache active; retry activated the new worker. First navigation after upgrade was offline and loaded the new UI. Online reload, redirected index, HTTP 503, delayed headers exceeding the 4-second timeout, and offline root/index navigations passed with exact localStorage preservation. All seven shell assets cached; old app cache removed only on success; unrelated cache retained. No page JavaScript exceptions. See check-offline.mjs and offline-results.json. baseline-results.json records the initial successful six-case migration run before interrupted-install/offline-first cases were added.

The earlier browser reload stall from the merge task was not reproduced. No speculative worker logic changes were made. This tests migration logic in local Chromium, not physical-device installation or a live-origin migration. Existing 96-case layout/content/interaction checks from reference-mobile-merge-20261014 remain applicable to this exact source. No redundant full UI matrix was run.

Updated live vault `The Visual Edit — Website Updates.md` to version 43 and copied the exact published index.html to `Attachments/Pinterest Alternatives/Pinterest Alternatives — Visual Research and Moodboarding.html`. Originals backed up before editing; hash guards checked concurrent changes, and saved files were read back. The vault HTML remains a snapshot with no service worker under file://; linked external providers still need internet. No Obsidian in-app rendering test.

End-of-task GitHub sync uses explicit paths for test evidence, backups, deployment receipt, recap, publication log and snapshot. Native site-source/ checkout and deployment tar are local helper artifacts, not additional canonical GitHub source copies. Standing automatic sync still applies to future completed project updates.
