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
speakers: ["[[Otto]]"]
status: seed          # seed -> draft -> locked
```

## Counting

`tools/wordcount.py` walks this folder and reports per scene, per card, per speaker, and the totals against the lock. Output goes to [[_Word Count]]. **Regenerate it; never hand-edit it.**

## The bilingual layer

Script files may carry `<!-- lang:zh -->` blocks like any other note, maintained by `/translate`. 🔧 Whether they get them from the start or at a later seam is open — see [[Localization Spec]].

## Rules carried over

- [[Otto]] is near-silent in the world and voluble on tape. The tapes will take the largest single share.
- [[Pip]] is non-verbal and costs almost nothing.
- [[Anna]] says very little across the whole game.
- Diegetic paper renders in a formal register that must survive translation — see [[Glossary]].
