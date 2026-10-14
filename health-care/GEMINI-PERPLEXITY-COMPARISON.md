# Gemini vs Perplexity — health research comparison
Reviewed 2026-10-12.

## Assessment
Perplexity is the stronger starting outline for this project because its source trail is broader and easier to follow, although it has citation mismatches and overstatements documented in [the earlier review](RESEARCH-REVIEW.md). Gemini adds useful explanations, but its source handling and some specific instructions require more substantial repair.

Neither report should be adopted as a personal health plan. Agreement is not independent confirmation: both draw on overlapping authorities and studies, and Gemini's prompt specifically highlighted issues found in the first report.

## Original documents and review scope
- [Gemini PDF](</home/ivanaguilera/Downloads/Evidence-Based Health Habit Review.pdf>): 27 pages, 21 numbered works-cited entries, nine main annotated bibliography entries.
- [Perplexity PDF](</home/ivanaguilera/Downloads/Health Care — Daily Life & Habits  Evidence-Based Review on Caffeine, Sleep, Diet, Movement, Stress, and Habits.pdf>): 36 pages, 68 numbered references.
- Full Gemini text reread, alongside the prior full Perplexity review. Selected consequential claims checked against authoritative or original sources.
- Nine distinct PDF hyperlink annotations recovered from Gemini; this count is not the total number of source URLs printed in the document. Some hyperlink targets contain broken span markup.
- Reference counts describe coverage, not quality. This is not an exhaustive audit of every source or a formal systematic review.

## Comparison
| Area | Perplexity | Gemini | Decision for the project |
| --- | --- | --- | --- |
| Caffeine dose and timing | Useful overview, but repeated six-hour language is too simple | Better discussion of the 400-mg timing trial, but adds an unsupported routine dosing schedule | Keep dose/timing distinctions; no automatic cutoff or microdosing program |
| Pregnancy/breastfeeding | Describes the conservative 200-mg reference | Uses an EFSA consultation draft to give 400 mg/day for lactation | Replace draft with final published opinion |
| Sleep | Useful journal and caveats, with some poorly matched precise citations | Detailed mechanisms, but often stronger causal language and rigid numerical suggestions | Emphasize duration, regularity, functioning and appropriately sourced guidance |
| Diet | Broad coverage, but observational carbohydrate minima become “safest” in summaries | Better explicit warning against prescribing an exact carbohydrate percentage; bibliography still says “proves” | Preserve observational wording throughout |
| Sugar and sodium | Merges different authorities' sodium limits | Correct WHO sodium amount and clearer sugar definitions; incorrect source link and guideline year | Keep verified WHO facts with correct primary sources |
| Activity/sitting | Overstates some adjusted observational findings as independent effects | Adds evidence that activity modifies the association, then says exercise proves complete risk elimination | Describe observed associations, not guaranteed cancellation |
| Habits | More accessible, recognizes variation and setbacks | Richer mechanism explanation, but no proper habit-study bibliography entry and converts one study's range into a requirement | Use simple cue-based learning without deadlines |
| Stress | Acknowledges varying evidence and interventions | Usefully distinguishes passive and active comparators; treats entire feedback loops as strongly proved | Verify each link separately |
| Everyday use | Lighter, more flexible learning roadmap | More demanding physiology, calculations and tracking despite unknown context | Start with a short optional journal |
| Sources | Broader, traceable bibliography with identified mismatches | More serious title/link mismatches, an unrelated citation and broken markup | Verify claims individually; do not merge bibliographies uncritically |

## Important Gemini findings

### 1. A draft EFSA document is presented as the final opinion — pages 2 and 22
The cited consultation PDF labels itself DRAFT SCIENTIFIC OPINION and carries placeholder journal metadata. It says 400 mg/day for lactating women; Gemini reproduces that value.

The final opinion, published 27 May 2015, instead states that single and habitual intakes up to 200 mg for lactating women do not raise safety concerns for breastfed infants. The document history explains this difference; it is not a reason to average the two values. This is an authority-specific reference, not personalized advice. [Consultation draft](https://www.efsa.europa.eu/sites/default/files/consultation/150115.pdf); [Final EFSA opinion](https://www.efsa.europa.eu/en/efsajournal/pub/4102).

### 2. Bibliographic labels and destinations disagree — pages 23–24
- The entry labeled WHO's sodium guideline links to a commercial electrolyte/water blog. The amount of sodium is consistent with WHO, but its provenance is wrong. The original WHO guideline is dated 2012, not the report's 2023. [WHO publication record](https://www.who.int/publications/i/item/9789241504836).
- The entry attributed to Rynders and colleagues in Nutrients (2019) links to a different review, “Religious and Traditional Fasting May Be an Alternative Method to Tackle Global Health Threats and the Epidemic of Obesity.” That destination itself lists the Rynders paper as reference 35, confirming that it is a separate publication. [Linked review](https://www.lidsen.com/journals/icm/icm-09-03-055).
- The sugar entry names the 2015 guideline but links to a healthy-diet fact sheet. A useful supporting summary is not the same document as the named guideline.
- The works-cited list on page 27 includes a microplastics review about Bangladesh that is unrelated to this project's main claims.

### 3. Observational exercise evidence becomes a guarantee — pages 16 and 25–26
Gemini says that Ekelund's study proved exercise completely eliminates sitting-related mortality risk. The original was a harmonized analysis of prospective cohorts. Its highly active group did not show a statistically significant increased mortality association with high sitting, relative to the active reference group.

That supports activity as a modifier of the observed association. It does not establish a randomized intervention, a guaranteed personal “buffer,” or elimination of every harm associated with sitting. [Original study abstract at the authors' university](https://research.bond.edu.au/en/publications/does-physical-activity-attenuate-or-even-eliminate-the-detrimenta/).

### 4. A numerical caffeine example is wrong — page 4
The example starts with 100 mg, an eight-hour half-life, and eight elapsed hours, but says about 43 mg remains. Under the stated simple model:
remaining amount = 100 × 0.5^(8/8) = 50 mg.

Even corrected, this is an illustrative amount-remaining calculation, not a blood concentration, a measurement of personal clearance, or a reliable prediction of sleep effects. A journal cannot establish an individual's metabolic half-life.

### 5. Proposed protocols exceed the evidence shown — pages 2 and 17–18
Gemini proposes repeated 30–50 mg caffeine doses, an 8–10-hour cutoff, and a precise taper schedule. It does not supply direct claim-level trial evidence establishing these as suitable routines for this user. A dose-timing trial does not validate a repeated-dose program or determine someone's personal clearance.

Similar precision appears in light-exposure times, room temperatures and daily wake-time windows. Treat them as suggestions needing suitable sources and personal context, not established universal requirements.

### 6. “Systematic review” is not demonstrated
The report gives no reproducible search strategy, eligibility criteria, screening flow, or formal risk-of-bias assessment for its own review. Its narrative can be useful, but the label does not establish systematic-review quality. Claims of coverage through October 2026 are not supported by a documented comprehensive search.

### 7. General agreement hides shared weaknesses
Both reports emphasize caffeine sensitivity, variable sleep cycles, food quality, movement and contextual habits. Both also sometimes move from evidence about components to stronger claims about entire feedback loops. A trial showing caffeine disrupts sleep does not by itself prove that the whole sleep-loss → escalating-caffeine → repeated-sleep-loss loop occurs for everyone.

Gemini's mechanistic detail does not necessarily add certainty. Human outcomes should carry more weight than an elaborate biological explanation alone.

## What to retain
- Perplexity's overall learning structure and low-burden journal.
- Gemini's explicit distinction between free and intrinsic sugars and its warning against exact carbohydrate prescriptions.
- Gemini's point that activity can modify sedentary-time associations, with observational wording restored.
- Discussion of uncertainty, study populations, food access, practical preferences and sustainable habits.
- Primary sources checked directly, rather than AI-report agreement.

## What to hold back
Repeated-dose caffeine programs, personal half-life calculations, fixed carbohydrate prescriptions, risk-cancellation exercise targets, rigid habit timelines, unsourced taper schedules, and device-specific sleep accuracy generalized to all wearables.

## Next step
Use [the corrected working guide](WORKING-GUIDE.md) as the project's provisional learning reference. Keep both PDFs as background sources. Begin with sleep and caffeine concepts, then describe current routine before considering changes. Personal medical context remains unknown; no intake targets, diagnoses, ratings or completed habit changes have been entered.

