# Import your Obsidian content into Notion

## 1. Test the portrait library

On Notion desktop or web, go to Settings → Import → Convert Zip to pages. Upload `Portrait Library — Notion Import Test.zip` into a temporary/private test location. Inspect entry 05 and the other reference/result pairs: ten images should be present. The ZIP also has the linked prompt-library text as an HTML page. Check the prompt code blocks and image links. Remove the temporary test pages before the full import if you want to avoid duplicates.

## 2. Import the full pack

Use the same importer with `Obsidian Vault — Notion HTML Import.zip`. Choose a private destination named “Obsidian Vault Import” if the importer offers destination selection. Open the generated “00 — Start Here” page and inspect the Japan/Korea/China dashboards, Music Prompt Library, Goth Rock and Spotify prompts, and Editorial Portrait Prompt Library.

The package preserves original note names and folder paths. Native Notion hierarchy and page-link remapping need checking after import. The official importer has rate and plan limits: this full pack exceeds roughly 120 page files. If the import stops, check Import progress and partially created pages; wait for the import allowance to reset before retrying affected files, and avoid blindly importing the whole ZIP again. The extracted `html-import` folder in the workspace can support targeted retries with the same asset paths.

## 3. Repair special features

Consult `Migration report.md` and `Migration issues.csv`. Map View blocks remain text, and should be rebuilt as Notion Map database views or separately hosted embeds. Convert preserved metadata into properties only if you want databases. Section links may need to be replaced with Notion heading links. Unsupported original attachments remain in the archive; upload manually as files where useful.

## 4. Optional CSV databases

The `CSV for optional Notion databases` folder contains the original two CSV files. Import through Settings → Import → CSV only if you want native databases in addition to the readable HTML tables. The destination searches are search leads, not a fully verified unique-venue database. Add/verify a Place property before using a Notion Map view.

## 5. Keep the original archive

`Obsidian Vault — Original Content Archive.zip` includes unchanged notes, attachments, and three historical backup files. It excludes hidden configuration folders. Keep your live Obsidian vault until you have reviewed the imported content. Importing creates a snapshot, not ongoing synchronization. Nothing in this pack modifies your vault or creates content in Notion automatically.

Official import instructions, checked 8 October 2026: https://www.notion.com/help/import-data-into-notion
