# The Visual Edit — proposed design

Status: approved design implemented and published as Site version 19.

Live URL: https://visual-edit-ivan.greymelon66.chatgpt.site

Original file and hosting manifest are preserved in `implementation-backup/`. The preview and publishing HTML are identical. `create_preview.py` is a historical preparation script; do not rerun it against the redesigned source.

Open `index.html` directly in a browser. All 52 sources, existing language dictionaries, embedded fonts, logos and portrait are retained.

## Direction

An editorial reference shelf: keep the warm paper and charcoal palettes, serif display typography and portrait; On mobile, show the complete portrait at the content width below the introduction. Shorten the opening and put the source directory immediately after it. Add direct directory and Asia shortlist links. Keep supporting editor selections and research routes below the directory.

Use a consistent card hierarchy: logo and region, category and name, purpose, comparable language/content/access fields, visible review date, expandable context, save and copy actions. Group search, region and category controls in one panel, with collection actions below. Use one/two/three columns across phone/tablet/desktop.

## Review artifacts

- preview-390-light.png and preview-390-dark.png
- preview-768-light.png and preview-768-dark.png
- preview-1440-light.png and preview-1440-dark.png
- cards-light.png and cards-dark.png
- preview-checks.json

Checked: no page overflow at 390/768/1440 in both themes; no overflow across all six languages at those widths; Japan filter returns four cards; favorite view returns one saved source; Markdown generation includes that source; reset restores 52 cards.

Additional implementation checks passed: keyboard skip link and focus outline; search and category filtering; mobile filter disclosure; print expansion/restoration and white print layout with all 52 sources; clipboard fallback dialog; public share URL; translated Markdown generation in all six languages; actual Markdown download.

Publication succeeded with the Sites plugin. Metrics are recorded in `implementation-metrics.json`; comparison statistics are in `diff-stat.txt`.
