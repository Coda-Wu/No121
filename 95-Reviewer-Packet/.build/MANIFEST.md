# Reviewer Packet — MANIFEST (Phase 1 proposal)

Status: **awaiting approval**. Nothing has been built. The vault has not been modified.
Generated 2026-09-18 from a read-only survey of 185 notes (51,073 source words).

---

## A. Blockers — need your answer before Phase 2

### A1. pandoc is not installed

`pandoc: command not found`. There is no ImageMagick either. Python 3.14.3 and
Pillow 12.1.1 *are* present, so the image work is covered.

Options:

- **(a)** You install pandoc (`winget install --id JohnMacFarlane.Pandoc`), I use it as specced.
- **(b)** I add `python-docx` as a dependency and write the converter myself.
- **(c)** I emit `.md` + `.html` only and you import into Word manually.

I have not installed anything. **(a)** is the only option that meets your
"default styles, preserve heading levels, no new dependencies" constraints cleanly.

### A2. Working tree is not clean

```
 D "50-Moodboards/_assets/06 - Apartment.md"     <- tracked, deleted
?? "50-Moodboards/_assets/00-Pixel Arts/"        <- untracked (your pixel art)
?? 50-Moodboards/_assets/06-Apartment.md         <- untracked (rename of the above?)
?? "50-Moodboards/_assets/06-Satellite Scenes/Pasted Image 20260913102723_382.png"
?? 50-Moodboards/_assets/07-Characters.md
?? "50-Moodboards/_assets/07-Characters/"
```

Phase 3 requires `git status` to show `.gitignore` as the only modified tracked
file. That cannot be true while `06 - Apartment.md` is staged-deleted. Commit or
restore it before I build, or tell me to report Phase 3 against a baseline diff instead.

### A3. Scope: the packet cannot fit 6,000–9,000 words without real cuts

The minimum coherent packet as specced is **~11,750 words**, ~30% over ceiling.
Since I may not summarise, the only lever is dropping whole notes or sections.
See section F for three drop options. **Pick one, or accept the overage.**

---

## B. Decisions I need from you

### B1. `20-Cast/Anna.md` is a hard spoiler

It is `status: locked`, `type: character`, *not* flagged `secret: true` — but the
Role section states "She does not know she is dead" and "She is the Building."
Your rule sends any reveal about Anna's nature to `04b_Endings-SPOILERS`.

**Proposal:** Anna gets no prose section in `03_Characters`; she appears only as
rows in the relations table and a `[TO WRITE: spoiler-free description of Anna as
Otto knows her]` placeholder. The full note goes to `04b`.

### B2. Where does `30-Narrative/The Ontology.md` go?

`02_World-and-Rules` is specced to carry "the Building's ontology", but that note
is `secret: true` and *is* the reveal. **Proposal:** `The Ontology.md` goes to
`04b`; `02` gets a `[TO WRITE: spoiler-free statement of what the Building is]`
placeholder.

### B3. Canon conflict — art resolution and palette size

- `60-Production/Art Spec.md` (**locked**): "320 x 180 base", "master 80 colors"
- `50-Moodboards/_Index.md` (`seed`): "640×360, 48–64 colors"

Per CLAUDE.md I will not silently resolve against a locked note. **Proposal:** use
the locked Art Spec figures; `_Index.md` is excluded from the packet anyway.
Flagging so you can fix the index separately.

### B4. Pixel art is already above the target width

Your three PNGs are 3190–3217 px wide — above the 1280–1920 band. Getting them
into the band needs a *downscale* at a non-integer factor, which destroys the
pixel grid. **Proposal:** embed the PNGs at native size, unmodified, no resample.
The eight GIFs are 1920×1920 (Noel 960×960) — already in band.

### B5. GIFs must become PNG

Your rule says PNG only. The eight character files are animated GIFs (11–20
frames). **Proposal:** extract frame 0 to PNG. Originals untouched. `Noel.gif` at
960×960 gets a clean ×2 nearest-neighbor upscale to 1920.

---

## C. Confirmed scope decisions

- **`95-Reviewer-Packet/` does not exist** — no collision.
- **DESIGN.md = `00-Inbox/processed/world_bible_v1.md`** (4,252 w, no frontmatter,
  21 numbered sections). Your explicit exception to the `00-Inbox/` exclusion; the
  rest of `00-Inbox/` stays excluded.
- **Pixel art pool = `50-Moodboards/_assets/00-Pixel Arts/` only** (11 files).
- **No `<!-- lang:… -->` marker blocks exist anywhere in the vault.** Nothing to
  strip. But see E2 — some notes are Chinese-*source*, which is a different problem.

---

## D. Document plan

Word counts are **source counts** measured on the note body with frontmatter and
marker blocks removed. Post-extraction counts will land within a few percent.

---

### 00_Start-Here.docx — 303 w

| Source note | Type / Status | Headings included | Headings omitted | Words |
|---|---|---|---|---|
| `30-Narrative/Logline and Thesis.md` | canon / **locked** | Logline · Thesis · Elevator pitch (internal) · Working title | — | 303 |

Placeholders (4):

- `[TO WRITE: one-paragraph cover note — what this packet is and who it is for]`
- `[TO WRITE: reading order and what each document contains]`
- `[TO WRITE: spoiler warning naming 04b as the spoiler document]`
- `[TO WRITE: studio / contact / fellowship-application header]`

---

### 01_GDD.docx — 1,172 w

All from `00-Inbox/processed/world_bible_v1.md` (no frontmatter; `type`/`status` absent).

| Section | Words | Fate |
|---|---|---|
| preamble (title block) | 107 | **include** |
| 1 · COMMERCIAL FRAME | 138 | **include** — platforms |
| 4 · THE ANTAGONIST | 192 | **include** — premise |
| 6 · STRUCTURE — 7 DAYS + FINAL NIGHT | 364 | **include** — structure |
| 8 · THE DAY LOOP (the Hunt) | 267 | **include** — core loop |
| 18 · SCOPE LOCKS & LEDGER | 104 | **include** — scope |
| 0 · LOGLINE & THESIS | 99 | omit — duplicated by 00_Start-Here |
| 2 · REGISTERS, TONE & THE TWO-GRAMMAR RULE | 141 | omit — 02 carries the atomized note |
| 3 · ONTOLOGY (top-secret layer) | 159 | omit — spoiler, → 04b |
| 5 · CAST | 472 | omit — 03 carries the atomized Cast notes |
| 7 · PERSONA LAW | 230 | omit — 05 carries the atomized note |
| 9 · CAMERA, FILM & LIGHT | 279 | omit — 05 |
| 10 · NIGHT PHASE & THE DREAM | 213 | omit — 05 |
| 11 · PERMUTATION & PERSISTENCE | 137 | omit — 05 |
| 12 · POCKETS & SET-PIECES | 303 | omit — budget |
| 13 · THE RULER | 109 | omit — 05 |
| 14 · ENDINGS | 179 | omit — spoiler, → 04b |
| 15 · ANECDOTE BANK | 95 | omit — budget |
| 16 · ART SPEC | 124 | omit — 06 carries the locked note |
| 17 · AUDIO SPEC | 82 | omit — budget |
| 19 · OPEN ITEMS | 111 | omit — internal |
| 20 · PRODUCTION, POSITIONING & LAUNCH CANON | 229 | omit — 07 carries the atomized notes |

Placeholders (2):

- `[TO WRITE: design pillars — no note in the vault states a pillar list]`
- `[TO WRITE: target platforms and input, if Commercial Frame does not state them]`

---

### 02_World-and-Rules.docx — ~1,103 w

| Source note | Type / Status | Headings included | Headings omitted | Words |
|---|---|---|---|---|
| `40-Mechanics/The Two-Grammar Rule.md` | system / **locked** | LAWFUL WEIRD · SICK WEIRD · The three dread registers, one owner each · Tone dial · Banned | — | 353 |
| `20-Cast/Naming Canon.md` | canon / **locked** | The rule · Family names · The violations that prove it · Restraint amendment (R9) | **The secret layer** (→ 04b) · Accounting note (R9) | ~324 |
| `40-Mechanics/Clauses/Clause 01 — Smoking and Alcohol.md` | clause / draft | Text (legalese as literature) · Exploit (steering use) · The second twist — what the rule is for · Sick-weird violations it diagnoses | Note | ~340 |
| `40-Mechanics/Clauses/Clause 09 — Quiet Hours.md` | clause / draft | all | — | 86 |

Clause sample = 2 of 12 (01 is the richest, 09 the tersest).
`Clause 02 — The Measure` (134 w) is the obvious third if budget allows.

Placeholders (2):

- `[TO WRITE: spoiler-free statement of what the Building is]` (see B2)
- `[TO WRITE: bridge from the naming canon into the House Rules]`

---

### 03_Characters-and-Relations.docx — ~1,700 w

Role + Voice only. **Relations bullets are not reproduced as prose** — they become
the relations table, which is where they earn their place. `Appears in` and
`🔧 Open` omitted throughout (link lists and internal TODO).

| Source note | Type / Status | Included | Omitted | Words |
|---|---|---|---|---|
| `20-Cast/Otto.md` | character / **locked** | Role · Voice | Relations (→ table) · Appears in | ~600 |
| `20-Cast/Mr. Vacancy.md` | character / draft | Role · The consent rule · Two tiers · Voice | The delusions (spoiler) · Relations · Appears in · 🔧 Open | ~520 |
| `20-Cast/Eve.md` | character / **locked** | Role · Voice | Relations · Appears in | ~300 |
| `20-Cast/Renner.md` | character / **locked** | Role · Voice | Relations · Appears in | ~270 |
| `20-Cast/Leon.md` | character / **locked** | Role · Voice | Relations · Appears in | ~130 |
| `20-Cast/Anna.md` | character / **locked** | — see B1 — | entire note (→ 04b) | 0 |

Then a **relations table** built only from explicit `## Relations` bullets:

| Column | Source |
|---|---|
| A | the note's subject |
| B | the wikilink target named in the bullet |
| Relation | the bullet text verbatim, brackets stripped |
| Source note | the note path |

Covers all 12 Character notes (~45 rows), including those with no prose section —
every relation is stated in a note, none inferred. ~250 w of table text.

Placeholders (3):

- `[TO WRITE: spoiler-free description of Anna as Otto knows her]`
- `[TO WRITE: intro naming the loop-name / palindrome conceit for reviewers]`
- `[TO WRITE: note on why Pip, Nan, Elle, Noel, The Couple and The Aunt and Uncle are table-only]`

**Dropped for budget** (all present in the vault, all restorable on request):
Nan 288 · Elle 254 · Pip 356 · Noel 145 · The Couple 102 · The Aunt and Uncle 343.

---

### 04_Story-Structure.docx — ~1,744 w

| Source note | Type / Status | Included | Omitted | Words |
|---|---|---|---|---|
| `30-Narrative/Chapters/01 №121 — Arrival.md` | chapter / **locked** | Owns · Beats | Microbeats (anecdote bank) | ~156 |
| `30-Narrative/Chapters/02 SPOOL — The Job.md` | chapter / **locked** | Owns · Beats | Microbeats | ~249 |
| `30-Narrative/Chapters/03 LIVED — The Name.md` | chapter / draft | Owns · Structure · Also here | Microbeats | ~296 |
| `30-Narrative/Chapters/04 RADAR — Detection.md` | chapter / **locked** | Owns · Beats | Microbeats | ~68 |
| `30-Narrative/Chapters/05 REPAPER — The Twins.md` | chapter / **locked** | Owns · Beats · Also here | Microbeats | ~197 |
| `30-Narrative/Chapters/06 ANNA — The Wound.md` | chapter / draft | Owns · Beats | Microbeats | ~181 |
| `30-Narrative/Chapters/07 DEED — The Family.md` | chapter / draft | Owns · Structure · Consequences · Also here | Microbeats | ~381 |
| `30-Narrative/Chapters/08 REDIVIDER — The Door.md` | chapter / **locked** | Owns · Beats | Microbeats | ~216 |

Placeholder (1): `[TO WRITE: one-paragraph framing of the day-card structure]`

**Dropped for budget:** `30-Narrative/Tapes to Anna.md` (246 w, locked) ·
all 9 `30-Narrative/Anecdotes/` notes (530 w total).

Note: chapter notes reference endings and the bridge by name. Mild spoiler leak is
unavoidable here unless you want `07 DEED` and `08 REDIVIDER` cut too.

---

### 04b_Endings-SPOILERS.docx — ~2,616 w

| Source note | Type / Status | Included | Omitted | Words |
|---|---|---|---|---|
| `30-Narrative/The Ontology.md` | canon / **locked** / secret | What the world is · The lifeboat, misread as a tomb · Why the Building fades · The two accounts of leaving · Why Otto · The Administration | — | 722 |
| `20-Cast/Anna.md` | character / **locked** | Role · Voice · Relations | Appears in · 🔧 Open | ~450 |
| `30-Narrative/Endings/Bad Ending — Ignorant Breach.md` | ending / **locked** | Gates · What it means · Shape | — | 284 |
| `30-Narrative/Endings/Neutral Ending — Stay.md` | ending / **locked** | What it means · Gates · Shape | 🔧 Open | ~230 |
| `30-Narrative/Endings/Do I Know You — The Hollow Return.md` | ending / draft | Gates · Shape · Cost | Related | ~150 |
| `30-Narrative/Endings/I See You — The True Ending.md` | ending / draft | Gates · What it means · Settled in Round 3 | 🔧 Open | ~300 |
| `20-Cast/Naming Canon.md` | canon / **locked** | The secret layer | rest (→ 02) | ~80 |
| `30-Narrative/The Death of Anna.md` | canon / draft / secret | What is settled · Both memories are sharp | 🔧 Open · Depends on this note | ~400 |

Placeholder (1): `[TO WRITE: spoiler gate — "do not read this before playing"]`

**Available but dropped for budget** — say the word and any come back in:
`The Hidden Family` 661 · `Timeline` 1,005 · `The Body` 290 · `The Curse` 651 ·
`The Delusions` 722 · `The Organ Map` 597 · `The Tomb Reading` 526 ·
`Key Items` 580 · `The Real World` 642.

---

### 05_Game-Design-Systems.docx — ~2,535 w

| Source note | Type / Status | Included | Omitted | Words |
|---|---|---|---|---|
| `40-Mechanics/The Day Loop.md` | system / **locked** | Five beats · Reference channels (anti-pixel-hunt) · Day-advance rules · Day math · Meters | Certification (ruler framing) | ~350 |
| `40-Mechanics/Persona Law.md` | system / **locked** | The two selves · Trigger · Memory model — THE HAZE · Rules | — | 259 |
| `40-Mechanics/The Camera.md` | system / **locked** | Controls · Capacitor · Viewfinder law · Snap tiers · Film economy | Related | ~300 |
| `40-Mechanics/Permutation and Persistence.md` | system / **locked** | Axes (deterministic, always) · Persistence · House Rules | — | 196 |
| `40-Mechanics/Festering.md` | system / **locked** | body · Locks | — | 88 |
| `40-Mechanics/Purge and Light.md` | system / **locked** | Rules · Teaching order · Purge-pinning | The final purge (spoiler) | ~170 |
| `40-Mechanics/Develop-to-Heal.md` | system / **locked** | The mid-game realization · Surfaces | — | 95 |
| `40-Mechanics/The Work Order HUD.md` | system / draft | Behaviour · Contents · The rule it protects | — | 256 |
| `40-Mechanics/Saving.md` | system / draft | Three granularities · **What is deliberately absent** — this is the no-fail-state rule, stated verbatim | The diegetic touch · What the save must contain | ~430 |
| `10-World/Pockets/Teaching Pocket.md` | screen / **locked** | all — included only because it explains the teaching system | — | 178 |
| `40-Mechanics/Flags/MISSING Notices Collected.md` | flag / seed | What the Building remembers · Surfaces where it shows — included only because it explains permanence | — | 213 |

Placeholder (1): `[TO WRITE: intro framing the anomaly hunt as the core verb]`

**Dropped for budget:** Night Phase 166 · The Ruler 256 · Locks and Openers 316 ·
Filters 298 · Sanity 362 · The Three Hums 182 · The Dream and Hint Ladder 153 ·
Disposition Tracker 136 · Reverse Film 104 (also an ending gate) ·
The Cataract Operations 424 (body-horror, spoiler-adjacent).

---

### 06_Art-Direction.docx — 232 w + 11 images

| Source note | Type / Status | Included | Omitted | Words |
|---|---|---|---|---|
| `60-Production/Art Spec.md` | production / **locked** | body · Screen ledger · Banned techniques | — | 196 |
| `50-Moodboards/_assets/05-Color Ref/Color Reference.md` | — / — | body (36 hex values, no headings) | — | 36 |

**Images — all from `50-Moodboards/_assets/00-Pixel Arts/`:**

| File | Native | Mode | Plan | Output |
|---|---|---|---|---|
| `apt_bright_2.png` | 3201×1887 | RGBA | native, no resample (B4) | 3201×1887 |
| `apt_dark_2.png` | 3190×1863 | RGBA | native, no resample (B4) | 3190×1863 |
| `pc_closeup.png` | 3217×1901 | RGBA | native, no resample (B4) | 3217×1901 |
| `Otto.gif` | 1920×1920 | P, 14 fr | frame 0 → PNG, ×1 | 1920×1920 |
| `Otto_2.gif` | 1920×1920 | P, 14 fr | frame 0 → PNG, ×1 | 1920×1920 |
| `Elle.gif` | 1920×1920 | P, 11 fr | frame 0 → PNG, ×1 | 1920×1920 |
| `Eve.gif` | 1920×1920 | P, 20 fr | frame 0 → PNG, ×1 | 1920×1920 |
| `Leon.gif` | 1920×1920 | P, 13 fr | frame 0 → PNG, ×1 | 1920×1920 |
| `Nan.gif` | 1920×1920 | P, 16 fr | frame 0 → PNG, ×1 | 1920×1920 |
| `Pip.gif` | 1920×1920 | P, 12 fr | frame 0 → PNG, ×1 | 1920×1920 |
| `Noel.gif` | 960×960 | P, 13 fr | frame 0 → PNG, **×2 nearest** | 1920×1920 |

**No note anywhere in the vault references any of these filenames.** Captions
therefore fall back to file names plus a placeholder each — **11 placeholders**:
`[TO WRITE: caption for Otto.gif]` and so on.

Placeholders (13): 11 captions ·
`[TO WRITE: palette rationale — the colour note is a bare hex list]` ·
`[TO WRITE: art-direction opening statement]`

---

### 07_Production-Plan.docx — 935 w

| Source note | Type / Status | Included | Omitted | Words |
|---|---|---|---|---|
| `60-Production/Scope Ledger.md` | production / **locked** | Locks · Systems freeze (in effect) · Amendments · Paid ledger to date · Word budget note | — | 651 |
| `60-Production/Schedule.md` | production / **locked** | Hours audit · Engine · Trailer and capsule | — | 163 |
| `60-Production/Positioning.md` | production / **locked** | Tags · Trailer and capsule (R9 brief, standing as working draft) | — | 121 |

Placeholders (3):

- `[TO WRITE: demo scope statement — Art Spec names ~10 screens, but no note states demo length or content]`
- `[TO WRITE: milestones with dates — Schedule has an hours audit, not a milestone list]`
- `[TO WRITE: release target and funding ask]`

**Dropped:** `Commercial Frame.md` 238 w (overlaps world_bible §1, which is in
01_GDD) · `Workshop Agendas.md` 846 w (internal process) ·
`Localization Spec.md` 277 w · `Audio Spec.md` 132 w.

---

## E. Budget

| Document | Words | Placeholders |
|---|---|---|
| 00_Start-Here | 303 | 4 |
| 01_GDD | 1,172 | 2 |
| 02_World-and-Rules | ~1,103 | 2 |
| 03_Characters-and-Relations | ~1,700 | 3 |
| 04_Story-Structure | ~1,744 | 1 |
| 04b_Endings-SPOILERS | ~2,616 | 1 |
| 05_Game-Design-Systems | ~2,535 | 1 |
| 06_Art-Direction | 232 | 13 |
| 07_Production-Plan | 935 | 3 |
| **TOTAL** | **~12,340** | **30** |

**Over the 9,000 ceiling by ~3,340 words**, after the drops already applied above
(~7,400 words of eligible source material is already cut).

### E1. Notes excluded wholesale, and why

| Excluded | Why |
|---|---|
| `00-Inbox/` except `processed/world_bible_v1.md` | your exclusion list; the one file is your explicit exception |
| `35-Corkboard/` — 33 stickies + PROTOCOL | your exclusion list |
| `90-Templates/` — 6 notes | your exclusion list |
| `60-Production/Glossary.md` | your exclusion list |
| `50-Moodboards/00-AGI References/` (1) and `10-AGI References/` (11) | AI image prompt library |
| `50-Moodboards/_assets/*.md` — 7 notes | Excalidraw drawing files (`excalidraw-plugin: parsed`), not prose; they hold third-party / AI reference images |
| all images outside `00-Pixel Arts/` | not confirmed as drawn by you |
| `tools/`, `.claude/`, `.obsidian/`, `CLAUDE.md`, `README.md`, `grill-me.md` | tooling / workflow |
| `70-Script/_Protocol.md`, `70-Script/_Word Count.md`, `60-Production/locale/*` | tooling / workflow |
| all 8 `_Index.md` | generated maps of content |
| all 10 `.canvas` files | working surfaces, explicitly "not canon" per CLAUDE.md |

### E2. `70-Script/` excluded — a language problem, not a budget one

The script folder is mostly Chinese-**source**, not machine translation, so rule 6
("English text only") cannot be satisfied by stripping markers — there are no markers.

| Note | English w | Han chars |
|---|---|---|
| `00 Prologue/00a The Waking.md` | 96 | 335 |
| `00 Prologue/00c The Beach.md` | 171 | 220 |
| `02 LIVED — D2/01 Cafeteria.md` | 25 | 508 |
| `03 RADAR — D3/01- Cafeteria.md` | 3 | 150 |

The remaining scenes are English but all `status: seed` and very short (2–96 w);
days 4–7 are empty `_Scenes.md` stubs. A script sample would show a vertical slice
that is mostly unwritten. **Recommend excluding `70-Script/` entirely** — say if
you want an English-only scene sample anyway.

---

## F. Three ways to get under 9,000

**Option 1 — drop 04b entirely (−2,616 → ~9,724).** Still over, and reviewers get
no endings and no reveal. For a fellowship, probably the wrong cut.

**Option 2 — drop 03 prose, keep the relations table (−1,450 → ~10,890).**
Still over. Characters reduced to a table.

**Option 3 — trim across six documents (→ ~8,900):**

| Document | Cut | Words |
|---|---|---|
| 01_GDD | `4 · THE ANTAGONIST` | −192 |
| 02 | `Clause 09 — Quiet Hours` | −86 |
| 03 | `Leon`, `Renner` | −400 |
| 04 | chapters `04 RADAR`, `05 REPAPER` | −265 |
| 04b | `The Death of Anna`, Anna's Voice section | −580 |
| 05 | `The Work Order HUD`, `Develop-to-Heal`, `Teaching Pocket`, `MISSING Notices Collected` | −742 |
| | **total cut** | **−2,265** |
| | **new total** | **~10,075** |

Option 3 as drawn still lands at ~10,075. To reach 9,000 exactly, one of these
also has to go: `Scope Ledger` (−651) plus `Purge and Light` (−170) plus
`Festering` (−88) plus `Permutation and Persistence` (−196) — which guts 05 and 07.

**My recommendation: accept ~12,340 and skip the cuts.** That is roughly 24 Word
pages of body text; a fellowship reviewer reading 00 and 01 alone gets 1,475 words,
and the rest is reference they can dip into. The packet is already 76% smaller than
the vault. If you want a hard ceiling, tell me the number and which of the three
options to apply.

---

## G. What Phase 2 will do, once approved

1. Append `95-Reviewer-Packet/` to `.gitignore`; confirm with `git check-ignore -v`.
2. Write one build script, `95-Reviewer-Packet/.build/build.py`, with inline comments.
3. Extract to `.build/md/` — strip frontmatter, tags, block IDs, `%%comments%%`,
   Dataview/query blocks, HTML markers. `[[A|B]]` → `B`, `[[A]]` → `A`.
   `![[note]]` inlined only if in this manifest, else dropped. `![[image]]` kept
   only if listed under 06. Callouts → plain paragraphs, callout title as bold lead.
4. Images → `.build/img/` per the table under 06. Originals never touched.
5. `pandoc -f markdown -t docx` into `95-Reviewer-Packet/`. Default styles, no TOC.
6. Rule 5: if a target `.docx` already exists, write `<name>_v2.docx` and report it.
