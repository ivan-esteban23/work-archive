# The Visual Edit — UI improvements

Published with Sites as version 20: https://visual-edit-ivan.greymelon66.chatgpt.site

Added compact sticky search and Filters controls; Access filtering; independently removable active-filter chips for search, category, region, access and favorites. Access filters are restored from shared view URLs; favorite selections remain browser-local. Chip labels and accessibility labels support all six languages.

All 52 card bodies and embedded fonts remain identical. Original publishing file is in backup/index.html. The prepared HTML matches the saved publishing source. prepare.py is historical preparation code; do not rerun against the updated source.

Checks passed: six width/theme layouts; eighteen language/width combinations; twenty-four language/access combinations; independent chip removal and focus retention; shared filter restoration and invalid-value fallback; compact sticky positioning and Filters navigation; keyboard skip link; original search/category filters; favorites; translated Markdown generation and download; clipboard fallback and share URL; print expansion and restoration.

CSS: 182 to 187 style rules, zero duplicate selectors within a context, one print block. Git diff: one file, 25 additions and 17 deletions. Screenshots: filters-390-light.png, filters-390-dark.png, filters-768-light.png, filters-768-dark.png, filters-1440-light.png, filters-1440-dark.png.
