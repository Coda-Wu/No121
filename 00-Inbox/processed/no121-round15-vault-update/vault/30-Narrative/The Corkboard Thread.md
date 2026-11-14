---
type: canon
status: draft
---
# The Corkboard Thread

> [!note] Rewritten in Round 15. See [[Round 15 Decision Record]]. The player no longer pins or draws.

The Suit's old case board, arrived wrapped in [[Otto]]'s luggage — [[Anna]]'s thread already strung in his own years-old handwriting. It hangs in [[Room 202]].

Day 0 shows ritual pins plus **one sealed aged envelope marked "A."**, opened cold-open in [[06 ANNA — The Wound]].

## What it is now

**A record of what Otto believes.** The player reads it and never operates it. It shows progress. It is never required: [[The Pocket Note]] carries the next step, and the board carries the meaning.

## How it works

- **~30 nodes** total — a scope lock, see [[Scope Ledger]].
- **A post lands at the moment of the find.** A short sound plays, and the post's shape shows for a second.
- **Otto strings the threads himself.** At the next cut the board is shown briefly with the new threads in place.
- **It can be read at any time.** One button opens his memory of the board. In 202 it is the real object on the wall.
- **A post says one line, in Otto's voice.**
- **An empty pin means that something belongs there.** It does not say what. The eight [[Key Items]] are eight pins from the first night. The seven notices are seven. The memories are a row of their own. See [[MISSING Notices Collected]] and [[Memory Rooms Found]].

## Three kinds of post

| Post | When it lands | What it tells the player |
|---|---|---|
| **Print** | He photographed it and kept the frame | He knows it. |
| **Pencil sketch** | He saw a main anomaly with an empty camera | He half remembers it. |
| **Rumour** | He met a side anomaly without film, or only heard of it | Someone told him. |

A sketch or a rumour becomes a print if he returns with film. See [[The Camera]].

## The board is never wrong

[[Mr. Vacancy]] has no access to Otto's room. Nothing reaches the board except through Otto.

- **A post is a fact.**
- **A thread is Otto's reading** of the facts he has. It is one branch of what is possible. When new facts arrive he restrings it himself.
- The board can therefore mislead by being incomplete. It is never false.

Threads show this: pencil for a reading, ink once it is confirmed.

## The gate

The completed Anna-thread is **one condition on two surfaces**: the [[Reverse Film]] gate and the photo-evidence gate. The thread is complete when its pins are full. See [[Anna Thread Completed]].

## Retired
- Pinning as the second beat of [[Night Phase]].
- The player drawing threads.

---

Not to be confused with `35-Corkboard/`, the vault's out-of-world writing tool.

## What the engine needs

Two tables. They replace the three asked for in `30-Narrative/corkboard.md`.

**① Post table** — one row for each post, ~30 rows.

| column | meaning |
|---|---|
| `id` | stable, snake_case, never reused |
| `row` | which row of pins it belongs to: key objects, notices, memories, people, other |
| `key` | `board.<id>` — the `tr()` key for its one line |
| `lands_on` | the find that places it: a milestone, an anomaly id, or a kept frame |
| `kind` | `print` / `sketch` / `rumour` — may rise to `print` |
| `card` | the card in which it can first land |

**② Thread table**

| column | meaning |
|---|---|
| `from`, `to` | post ids |
| `appears_at` | the cut after which Otto has strung it |
| `state` | `pencil` for a reading, `ink` once confirmed |
| `confirmed_by` | the find that turns pencil to ink |

There is no conclusion table. Prose columns go in the CSV pipeline. Structure goes in a sibling JSON.
