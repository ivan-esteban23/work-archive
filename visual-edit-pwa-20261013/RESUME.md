# The Visual Edit — Installable web app

Completed 2026-10-13 (America/Santiago). User requested a web app for phones, tablets, and desktops.

- Live: https://visual-edit-ivan.greymelon66.chatgpt.site
- Sites project: appgprj_6ace7cad170c8191adbe36fd345102d0; public audience preserved.
- Final published version: 28; commit 0d5b0622656cd83586486706cbb6f5eb456fb055.
- Publishing checkout: /home/ivanaguilera/Work/visual-edit-public; static root dist.
- Vault attachment synced and read back: /home/ivanaguilera/Documents/Obsidian Vault/Attachments/Pinterest Alternatives/Pinterest Alternatives — Visual Research and Moodboarding.html.

## Behavior

Install app is available in the footer and mobile Sections dialog. A translated app dialog explains browser installation, offline readiness, and per-browser/device favorites storage. Chromium's beforeinstallprompt is supported when offered; Apple browsers have manual instructions. Installed display mode shows App settings. Updates wait for explicit Update now, preserving local favorites. All six languages covered.

Manifest includes standalone display, stable id/start URL/scope, original VE icon in 192/512, maskable512 and Apple180 PNG exports, and Directory/Countries shortcuts. All supporting files are same-origin, with no new framework, build step, or CDN dependency. HTML retains embedded fonts and imagery. Local file:// vault copy skips manifest/SW and install UI and remains self-contained.

The service worker precaches only the directory and its local app assets. Cache-first navigation ignores query parameters so offline languages and hash filters work. External source sites require internet. Readiness is checked via service worker message against all seven cache entries. Favorites remain browser/app local and do not sync across devices.

Hosting redirects /index.html to /. Initial v26 offline navigation failed on the redirected cached Response; v27 normalized responses when precaching. Final v28 also consolidates shared dialog sizing in the existing rule, avoiding duplicate selectors. Future changes must update the cache version in dist/sw.js when HTML or local app assets change.

## Validation

- check-pwa.mjs: 390/768/1440 in both schemes; all six languages; modal width/overflow/focus/Escape; manifest installability (no Chromium errors); seven cached shell files; offline language URL reload; all52 cards/fonts/images; favorite persistence; deferred install prompt handler and dismissal; explicit new-version activation; file:// behavior; no JS exceptions. Final run passed with a local server reproducing production's index.html redirect. Test uses a dedicated Chromium profile, not the user's browser data.
- check-live.mjs and live-checks.json: final HTTPS asset MIME/status, service worker scope, Chromium installability and offline language reload.
- qa-results.json; install-{390,768,1440}-{light,dark}.png.
- All52 source cards byte-identical to the original; external link multiset, embedded fonts and embedded images unchanged.
- Physical iPhone/iPad/Android/desktop installation and Safari UI were not tested. Storage is browser-managed; actual installs have not been performed on the user's devices.
- HTML 1,893,983 → 1,907,860 bytes. Four icon assets + manifest + service worker were added for installation.
- Diff from previous live commit: 7 files, 96 insertions, 9 deletions; four PNG additions. Git clean after helper publication.

## Backups and maintenance

backup/site.html and backup/vault.html contain the originals; staged/dist contains the final complete app. visual-edit-pwa-final.tar.gz is the published bundle. Do not blindly rerun prepare.py: it is a historical one-time preparation script and predates the final shared-dialog consolidation and redirected-response fix. Check scripts are task QA tools, not deployment dependencies. No native source notes or Obsidian configuration changed.
