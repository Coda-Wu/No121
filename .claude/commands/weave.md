---
description: Run one synthesis phase over the corkboard
argument-hint: [census | cluster | place | gaps]
---
Phase: $ARGUMENTS

Ground rules for every phase: **propose, never decide.** Outputs are dated notes in `35-Corkboard/Threads/`. Sticky prose is never rewritten. Only Coda promotes `loose → pinned` and approves placements; you may set `canon-pressure` and `parked` when detected.

**census** — full inventory: counts by status / register / cast / where; blank-field report; duplicate candidates (near-identical scenes, listed as pairs with a one-line reason each); coverage gaps (bible cast with zero stickies, chapters with none). Write `Threads/Census <date>.md`.

**cluster** — over `status: pinned` notes only:
(a) motif clusters (≥3 stickies sharing a concrete image);
(b) escalation-ladder candidates (one motif at rising intensity — propose the order, ruler-scare style);
(c) recurring cast pairings;
(d) register-ownership violations (a register appearing under the wrong owner: Building = spatial, residents = domestic, Administration = clinical).
For each cluster: members, the pattern in one line, and a proposed thread name Coda is free to rename. Write `Threads/Clusters <date>.md`. When Coda approves and names a cluster, create `Threads/<Thread Name>.md` listing its members as wikilinks.

**place** — over pinned notes: propose `day` + `slot` (critical | microbeat | dream | clause | pocket | tape | anomaly) per sticky, one-line reasoning, confidence. Honor canon: bodied Vacancy ≈2 rationed appearances plus mazes · Anna on-screen in endings only · floor-5 material D7+ · demo carries only №121 + SPOOL content · pocket cap 6 · exactly 7 MISSING notices. Where candidates exceed a cap, flag the scope pressure explicitly — the scope-tax rule applies to placements too. Write the table to `Threads/Placement <date>.md`; apply only rows Coda approves: set `day`/`slot`/`status: placed` and append a wikilink line to the matching `30-Narrative/Chapters/` note.

**gaps** — after placements: per chapter, list unfilled slots (critical beat sourced? 2–3 microbeats? dream rung?); clauses without a discovery scene; ladders missing a rung; starving registers. End with the ten most valuable stickies that don't exist yet, each as a one-line writing prompt — a constraint, not content. Write `Threads/Gaps <date>.md`.

Commit `narrative: weave <phase>`.
