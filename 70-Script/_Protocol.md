---
type: protocol
status: draft
---
# The Script Protocol

Where the finished text lives. One folder per card, one file per scene.

**The chapter notes and flowchart canvases stay canon.** This folder is where the words are actually written, and the only place they are counted.

## Format — and why it is strict

The **15,000-word lock** in the [[Scope Ledger]] governs every speaker. The format exists so a word count can be run honestly, without anyone maintaining a tally by hand.

```
**OTTO:** One set of prints. Mine.

*He straightens, and does not look at the door.*

<!-- design note: the pause here is authored, not performance -->
```

- **Spoken lines** are `**SPEAKER:** text`. **These count.**
- **Stage directions** are *italic*. These do not count.
- **Design notes** are HTML comments. These do not count.
- Anything else is prose and does not count.

## Two budgets, kept apart

| Budget | What | Files |
|---|---|---|
| **Spoken — ≤15,000** | dialogue, tapes, the calls, dream voices | `type: script` |
| **Diegetic paper — 🔧 unset** | notices, work orders, the tenancy agreement, newspapers, the ledger, MISSING notices | `type: document` |

Paper is **read, not heard**, and it is the main misdirection channel in [[The Tomb Reading]] — it should not be starved by dialogue. 🔧 Its own limit is unset and needs one.

## Frontmatter

```yaml
type: script          # or: document
card: "SPOOL"
day: "1"
scene: "04"
locale: spool.teaching_pocket   # the export anchor - see below
speakers: ["[[Otto]]"]
status: seed          # seed -> draft -> locked
```

## Counting

`tools/wordcount.py` walks this folder and reports per scene, per card, per speaker, and the totals against the lock. Output goes to [[_Word Count]]. **Regenerate it; never hand-edit it.**

## The locale export

`tools/build_locale.py` derives the engine's text tables from this folder into `60-Production/locale/` — one `<card>.csv` and one `<card>.beats.json` per card, plus a shared `doc.*` pair for diegetic paper. Contract: [[README]]; spec: [[WS-3-text-spine]]; coverage report: [[_Index]].

**This folder stays the single source.** The CSV is derived and never hand-edited — a fix goes into the scene file and the export is rerun, or the 15,000-word lock ends up measuring a copy.

- **`locale: card.scene`** is the export anchor, and the only thing that puts a scene in the pipeline. It is a *key*, not a filename: renaming this file must never renumber anything downstream. Cards are `prologue spool lived radar repaper anna deed redivider`; diegetic paper is always `doc.<document>` whatever card it appears on.
- **A 🔧 placeholder reserves its key** with empty text. An unwritten line is visibly blank in playtest; an invented one is not.
- **Names in dialogue are written as wikilinks** — `[[Leon]]` — and export as the `{leon}` token that carries his colour. Spelled-out names are only warned about, never auto-converted: Chinese has no word boundaries, and 奶奶 is also just the word for grandmother.
- **Diegetic paper exports its blockquotes.** `> …` paragraphs are the paper; prose around them is brief, not text, and reserves no key.
- **Keys are never renumbered.** An edited line keeps its key, an inserted line takes a number from the gap, and a deleted line's key is reported as orphaned rather than quietly reused.

## The bilingual layer

Script files may carry `<!-- lang:zh -->` blocks like any other note, maintained by `/translate`. 🔧 Whether they get them from the start or at a later seam is open — see [[Localization Spec]].

## Rules carried over

- [[Otto]] is near-silent in the world and voluble on tape. The tapes will take the largest single share.
- [[Pip]] is non-verbal and costs almost nothing.
- [[Anna]] says very little across the whole game.
- Diegetic paper renders in a formal register that must survive translation — see [[Glossary]].
