# The Visual Edit — navigation and filters · 14 October 2026

Published version 35: https://visual-edit-ivan.greymelon66.chatgpt.site
Commit: aa050ba54990454d4ae61d72af1e646664cfaf29
Version ID: appgprj_6ace7cad170c8191adbe36fd345102d0~appgver_2943e206105c8191a70f0fb2d4b60970
Deployment: appgdep_6acf99e1556c8191b097b64447e79054 (succeeded)

Implemented search-first navigation with nearby results count/reset; filters ordered category/country/coverage/access; mobile category select; active states/chips; collapsible section navigation/country shortcuts; focus protection below sticky search and above mobile navigation; static search in short landscape. All 58 source cards and anchor destinations preserved. Existing PWA cache bumped.

QA: 42 viewport/language combinations, alphabetical order, grid/action alignment, type bounds, no overflow/broken images; search, country and favorite persistence. Focused navigation checks: mobile open/focus, selected state, empty results/reset, deep-link restoration, actual Tab focus, desktop filters, short landscape. Screenshots reviewed. See qa-results.json and navigation-results.json. No physical-device or Obsidian in-app test.

Vault HTML and both design notes saved and read back; source byte match and wiki-link targets verified. Original files backed up with concurrent-change hashes. update.py is historical; the focus guard subsequently received a height limit for large section targets.

All five user prompts complete. Supporting editorial design remains a proposal pending the next prompt.
