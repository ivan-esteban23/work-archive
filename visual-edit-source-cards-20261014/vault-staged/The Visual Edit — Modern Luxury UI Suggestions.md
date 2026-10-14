# The Visual Edit — Modern Luxury UI Suggestions

Prepared: 14 October 2026  
Website: https://visual-edit-ivan.greymelon66.chatgpt.site  
Status: Typography, color palette, layout/spacing, and source cards implemented on the live website, 14 October 2026. Other sections remain design proposals.

## Recommended direction

A contemporary luxury magazine: expressive typography, generous spacing, precise alignment, and restrained detail. The directory should feel curated while remaining easy to search, filter, and save.

Keep the existing 58 sources in A–Z order, country and category filters, favorites, six language options, and installable app functionality.

## 1. Typography

Typography should lead the redesign.

- Pair an elegant serif for the masthead and large editorial headlines with a clean sans-serif for descriptions, navigation, filters, and buttons.
- First explore the website’s existing embedded fonts. Change families only if their letterforms do not support the intended direction.
- Use a small, consistent set of sizes and weights. Prefer contrast between headline scale and body text over many competing styles.
- Keep source names readable at a glance; use a medium-weight sans-serif for directory titles, reserving the serif for editorial sections.
- Limit uppercase and wide letter spacing to short section labels. Avoid small, faint text for essential information.
- Give body text comfortable line spacing and bounded paragraph widths.
- Check Chinese, Japanese, and Korean text separately for font coverage, line wrapping, weight, and spacing. Latin typography rules should not be applied indiscriminately to these scripts.

**Suggested starting scale:** body text 16–18 px; source titles 20–24 px; section headlines 32–48 px; cover headline 48–88 px, adjusted responsively. Use relative units and fluid sizing in implementation.

## 2. Color palette

Use a quiet palette with a single restrained accent.

| Role | Suggested color | Intended use |
| --- | --- | --- |
| Warm ivory | `#F7F4EE` | Main light background |
| Soft white | `#FFFDF9` | Cards and elevated surfaces |
| Charcoal | `#232323` | Primary text |
| Warm gray | `#615B54` | Supporting text |
| Pale stone | `#DCD5CB` | Dividers and subtle borders |
| Muted bronze | `#80623D` | Selected states and small accents |

Treat these values as starting points. Verify contrast for each text, control, focus, and background pairing before implementation. Bronze should appear sparingly; avoid gradients or decorative gold effects.

Retain dark mode with equally clear hierarchy and readable controls.

## 3. Layout and spacing

- Use a consistent spacing system, such as 8, 16, 24, 32, 48, 64, and 96 px.
- Increase breathing room around the masthead, section introductions, and card groups.
- Establish a clear content width and align headings, cards, and controls to the same grid.
- Use one column on phones, two on tablets, and three on wider screens where card copy remains comfortable.
- Reduce repetitive boxes and heavy borders. Separate major sections through spacing and occasional fine rules.
- Keep the directory prominent and easy to reach; supporting editorial content should complement browsing.

## 4. Source cards

- Give every card the same internal hierarchy: source name, research purpose, key metadata, then actions.
- Make category, country, and access information quieter without reducing readability.
- Keep longer access notes and evidence links in the existing disclosure panel.
- Align Save and Copy actions consistently across cards.
- Use subtle background or border changes on hover, with equally clear keyboard focus states.
- Refine logo and initial-badge sizing for a consistent visual rhythm. Preserve authentic publisher identities.
- Avoid adding large imagery merely for decoration. Image-led cards would require a separate asset and rights review.

## 5. Navigation and filters

- Simplify the visual hierarchy of the header and section navigation.
- Make search the most prominent browsing control, followed by category, country, coverage, and access.
- Give active filters clear selected states and an easy reset action.
- Keep the visible results count close to the controls.
- Preserve alphabetical order in the directory and relevant lists.
- Keep mobile filters compact while maintaining comfortable touch targets and clear labels.
- Ensure sticky controls, if used, do not obscure content or keyboard focus.

## 6. Editorial sections

- Refine editor picks and research routes with the same typography, spacing, and surface treatments as the directory.
- Use source names as the strongest card element and supporting labels as secondary information.
- Keep workflow instructions in their logical step order.
- Shorten overly dense introductions only where meaning and source context can be preserved.
- Use one coherent design system across the cover, directory, supporting sections, dialogs, and footer.

## 7. Interaction and accessibility

- Use short, subtle transitions for buttons, disclosure panels, and selection states.
- Respect reduced-motion preferences.
- Retain visible keyboard focus, clear button labels, and usable touch targets.
- Avoid essential information appearing only on hover.
- Check light and dark modes, narrow screens, zoomed text, and all six languages.
- Preserve favorites, shared filter links, printing, and the existing app update flow.

## Proposed implementation order

1. Audit the current typography and establish the font pairing, type scale, colors, and spacing tokens.
2. Apply the direction to the masthead and one representative source card for visual review.
3. Refine the directory grid, search, filters, and navigation.
4. Extend the design to editor picks, routes, dialogs, and the footer.
5. Verify responsiveness, accessibility, multilingual text, and existing interactions.
6. Publish the completed design and update the app’s offline cache.

## Choices to settle before implementation

- **Recommended style:** contemporary luxury editorial.
- **Typography:** retain and refine the embedded families if suitable; otherwise select a new pairing after checking language coverage and licensing.
- **Card presentation:** refined text-and-logo cards as the first direction. Larger image-led cards remain an optional later exploration.
- **Scope:** typography and spacing first, then controls and supporting sections.

These are design suggestions, not verified claims about new fonts, licenses, or assets. Specific font families and final color combinations remain to be selected and checked.


## Implementation progress · 14 October 2026

- **Typography — completed:** retained Instrument Serif and Source Sans 3; fluid type scale, larger supporting text, reduced uppercase metadata, regional CJK font stacks.
- **Color palette — completed:** applied the proposed light palette; added stronger essential control borders and a coordinated dark palette. Checked text, focus, selected and hover states.
- **Directory — completed:** 58 sources in A–Z order; supporting website menus and reference lists alphabetized.
- **Layout and spacing — completed:** shared 8/16/24/32/48/64/96 px spacing tokens, aligned content gutters, one/two/three-column directory, roomier section introductions, and fewer enclosing borders.
- **Source cards — completed:** source name and logo, research purpose, quiet key metadata, existing disclosures, then aligned Save/Copy actions; subtle hover, clear keyboard focus, and consistent 40 px logo/initial sizing.
- **Remaining proposals:** navigation refinements and editorial section design.

See [[The Visual Edit — Website Updates]] for saved version details and verification limits.
