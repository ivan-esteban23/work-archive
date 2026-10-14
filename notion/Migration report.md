# Notion migration report — 8 October 2026

Built from a consistent read-only snapshot of `/home/ivanaguilera/Documents/Obsidian Vault`. Live notes and settings were not changed. Nothing has been uploaded to Notion.

## Contents

- 151 original Markdown notes converted to HTML pages.
- 10 unchanged images bundled with valid local image paths.
- 7 non-image attachments preserved as readable HTML pages (CSV tables or literal text), with originals in the content archive.
- One generated start page listing every note and readable attachment page.
- 3 historical backup files retained only in the original-content archive, avoiding duplicate imported pages.
- Hidden files and folders, including `.obsidian` plugin settings, excluded from both packages. This is a note/content archive, not a complete Obsidian configuration backup.

## Transformations

- 1206 wiki links converted to ordinary HTML links.
- 10 image/embed references converted.
- 191 wiki section links converted to page links with visible section labels; Notion heading navigation may need manual repair.
- 45 note metadata blocks kept as readable text, not native database properties.
- 6 callout labels kept as ordinary blockquotes.
- 7 plugin blocks kept as readable configuration; they are not interactive maps.
- Fenced prompt examples remain literal code; links inside examples are not rewritten as live navigation.

## Import limitations

Notion may not remap every relative HTML page link to a native Notion page link. Local output links were checked, but this does not prove successful Notion remapping. Inspect your dashboards after import. Section anchors, application links, metadata properties, image sizing, table layout, and plugin functions may need repair. CSVs in the optional folder can be imported separately as databases; importing them in addition to HTML tables creates separate copies with no automatic synchronization.

Notion's official guide documents desktop/web imports, HTML with reachable bundled images, and ZIP imports. It also documents plan-specific per-file limits and roughly 120 file imports per 12 hours; this pack has 159 HTML pages, so an import may be throttled or partial. Check progress and partial pages before retrying. The portrait test has just two HTML pages and ten images.

Source checked 8 October 2026: https://www.notion.com/help/import-data-into-notion

## Issues for review

- app-or-local-link: 50
- csv-attachment: 2
- frontmatter: 45
- missing-link: 3
- plugin-block: 7
- section-link: 191

See `Migration issues.csv` for per-file details. Missing source links are preserved as readable labels rather than inventing destinations. Native Notion page links and working map views require review after import.

## Verification performed

All source hashes were checked against the live files after conversion. The original archive preserves each included file byte for byte. Every generated local HTML href/src resolves to a packaged file. All ZIP archives passed integrity checks. These are filesystem/conversion checks, not a live test inside Notion.
