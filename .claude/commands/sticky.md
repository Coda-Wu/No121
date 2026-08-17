---
description: File raw scene dumps as sticky notes on the corkboard, verbatim
argument-hint: [pasted scenes, or empty to read 00-Inbox/stickies_raw.md]
---
Raw scene material: $ARGUMENTS

If no material was passed, read `00-Inbox/stickies_raw.md`; after filing, move it to `00-Inbox/processed/stickies_raw_<date>.md`.

For each distinct scene in the material:

1. Next ID = highest `id` in `35-Corkboard/Notes/` + 1.
2. Create `35-Corkboard/Notes/S<id, 3 digits> <Evocative Title>.md` from `90-Templates/Sticky.md`. If Coda gave a title, use it; otherwise derive one from the scene's central image, not its plot.
3. Place Coda's text under **What happens** / **Vibe / dream logic** VERBATIM. Never rewrite, tighten, correct, or "improve" the prose — filing and formatting only. Spelling stays as written.
4. Fill only frontmatter inferable with high confidence: cast explicitly named, an explicit day, an obvious register per the two-grammar rule. If registers mix, leave `unassigned` and add one HTML comment naming the tension. Everything else stays default.
5. A note that pitches a new SYSTEM rather than a scene: file it anyway, set `status: parked` (systems freeze), and say so in the report.
6. A note that contradicts a `status: locked` canon note: file it anyway, set `status: canon-pressure`, and name the conflicting note. Never resolve the conflict yourself.

Finish with a one-line census (total stickies · count toward 70 · by status · by register), then commit: `narrative: +N stickies (S0xx–S0yy)`.
