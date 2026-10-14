# Live version 44 verification — 14 October 2026

Live site: https://visual-edit-ivan.greymelon66.chatgpt.site
Website main: `58ecf6fcac1c973902e7704758e32bf0df40ddbb`.

User authorized step 4, live/phone/offline verification. No physical phone or installed-app control is available through this environment. Completed the independently available live-origin checks using isolated Chromium with touch/mobile emulation. No production source, deployment, account settings or user browser data changed.

`node check-live.mjs` passed nine checks; detailed measurements are in `results.json`:

- Live service-worker SHA-256 matches the local deployed v44 source exactly. Cache v3's HTML includes the translated-search fix.
- At 320 and 390 CSS-pixel mobile viewports, document width fits and masthead controls stay inside the viewport.
- The live seven-asset shell reports offline-ready. A sample favorite, explicit dark mode, Spanish and a shared Japan filter were saved in an isolated temporary browser profile.
- Online reload retained the state.
- With a dedicated proxy disconnected and all of its open upstream sockets destroyed, root reload and reopening `/index.html` after leaving the app document succeeded offline. Browser offline emulation was also enabled, but the disconnected proxy provides the actual worker-network cutoff.
- A full Chromium process shutdown/restart using the same isolated profile, while the proxy remained disconnected, reopened the live-origin cached directory with all 58 source records and the exact saved state.
- Reconnecting and reloading retained state without extra navigation/reload loops. No page JavaScript exceptions. No service-worker bypass or unregister operations.

The proxy tunnels HTTPS end to end, permits only the exact Site host and has no interception certificate. Temporary browser profile, proxy sockets and browser/server processes were removed/stopped after the test. No credentials are used by the script. `browser.mjs` adapts the repository's dependency-free test helper for the dedicated proxy and retained profile across restart; site source remains unchanged.

These results are for Chromium mobile emulation on the production origin, not physical Android/iOS, Safari or an OS-installed standalone PWA. The older-cache v42/v43 migrations were previously tested locally; this live test starts with the current v44 installation and does not seed a historical worker on the live origin. External providers require internet as expected.

## Remaining device check

1. Open the existing app or live site online. In app settings, wait for offline-ready, then save a favorite and choose a language/theme.
2. Disable Wi-Fi and mobile data. Close/reopen the app or site and confirm the directory, saved favorite and chosen language/theme remain available. Do not clear site data.
3. Reconnect and reload once; confirm the latest version remains usable without repeating reloads.

Device/browser and user-observed result are pending. An optional device question was sent during the automated checks. End-of-task archive sync covers only this task directory; no website commit or redeployment is needed.
