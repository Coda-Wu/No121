# Brief — The Corkboard deduction system

**For: a Grill session in the Obsidian vault, to re-author `30-Narrative/The Corkboard Thread`.**

Written from the engine side. Everything below is either quoted vault canon, a ratified decision, or a statement of what the engine will need back. Paste this whole file into the vault-side session; it is meant to be readable without repo access.

The output of that session should be a re-authored `The Corkboard Thread` note plus the three tables listed under **What the engine needs back**.

---

## 1. What exists today, in canon

`The Corkboard Thread` (LOCKED) currently says, in full:

> The Agent's old case board, arrived wrapped in Otto's luggage — Anna's thread already strung in his own years-old handwriting. Second beat of Night Phase: develop → **pin** → tape → alarm → sleep.
>
> Day 0 shows ritual pins plus **one sealed aged envelope marked "A."**, opened cold-open in `06 ANNA — The Wound`.
>
> ## How it works
> - **~30 nodes** total — a scope lock, see Scope Ledger.
> - Pins auto-place; **the player draws the threads**.
> - Prints pin here after developing; empty-camera main anomalies log a pencil sketch instead ("the Agent draws what the Handyman half-remembers"), and side anomalies met filmless pin as rumours, re-shootable if they persist. See The Camera.
>
> ## The gate
>
> The completed Anna-thread is **one condition on two surfaces**: the Reverse Film gate and the photo-evidence gate.

That is the whole note. The design below is much larger than it, which is why the note needs re-authoring rather than extending.

## 2. What Coda ratified, 2026-09-09

> We need to design a comprehensive corkboard investigation system that balances player freedom with guided narrative progression, allowing players to test various thread connections to answer core mysteries like **"Where is Anna?"** and **"Where am I?"**. The board will automatically populate with key questions, characters (including Otto, Anna, NPCs, and the mysterious Mr. Vacancy), and evidence unlocked through plot milestones, anomaly discoveries, or photo development. Players can manually string these nodes together, governed by a **hidden compatibility logic** where only specific threads can successfully link. The resulting web of deductions dynamically generates conclusions; while illogical connections yield obviously incorrect answers, **plausible but flawed theories will direct the narrative toward neutral or bad endings**. Ultimately, deriving the absolute true answers on the corkboard is necessary to **unlock critical dialogue options** and progress toward the game's true ending.

So the board is not a notebook. It is the game's **deduction engine and one of its ending determinants**.

## 3. Constraints the design must respect

These are locks and existing canon. A design that breaks one of them needs the lock changed first, deliberately.

**Scope**
- **~30 nodes total.** A `Scope Ledger` lock, and the only reason this is tractable.
- **≤15,000 words** across the whole game, and diegetic paper already has a large share of it. Board text competes with the tapes, which carry most of Otto's characterisation.
- 8 cards: the cold open, six days, the final night. **The demo is the cold open + Day 1 only.**

**Structure**
- **Pins auto-place. The player draws the threads.** The player never arranges the board; they only connect it.
- **Four endings**: True (`I See You`), Bad, Neutral, Hollow Return (`Do I Know You`). No fail states anywhere in the game.
- The **completed Anna-thread** is already one condition on two surfaces — the `Reverse Film` gate and the photo-evidence gate. Any new design has to keep both satisfied.
- **`Clauses Known` ≥ 8** is a separate condition on the True Ending. The board and the clauses are two different gates; the design should say how they relate, or say plainly that they do not.
- **Day 0 already has content on it**: ritual pins, plus one sealed aged envelope marked "A." opened cold in `06 ANNA`.

**Register**
- **The two-grammar rule**: lawful-weird and sick-weird are distinct aesthetic registers. Evidence carries one or the other; the board should know which.
- **The hint ladder is diegetic and already exists**: idle sleeps escalate, each fruitless night adding **exactly one** new detail (`The Dream and Hint Ladder`). If a player cannot see a connection, that ladder is the answer — the board must not grow a hint system of its own.
- **No timers**, and nothing that pressures the player to stop thinking.

**Feeding it**
- Prints pin after developing. An **empty-camera main anomaly** logs a pencil sketch instead — "the Agent draws what the Handyman half-remembers". **Side anomalies met filmless pin as rumours**, re-shootable if they persist.
- **Mr. Vacancy is camera-immune.** It is only ever photographed because it permits it, and **every print of it differs slightly from what the shutter saw.** A node fed by such a print is unreliable *by canon*, and the design should decide whether the board knows that.
- **Otto's central belief is false**: he did not grow up in this building. He grew up in the real №121. A deduction system whose subject is a man reasoning from a false premise is an opportunity, not a problem.
- **The Building and the Administration are the same entity in different registers.** Anna's institutional voice. Two nodes or one is a real design question.

## 4. What the engine already provides

So the design can lean on it rather than re-inventing it.

- **Durable state** (`GameState`, saved at every beat): permanent flags, `clauses_known`, film count, certified measures, the permutation axes. `Saving` already says the save must carry **"The Corkboard Thread and its drawn threads"**, so board state is expected to persist.
- **Text pipeline**: every player-facing string is a `tr()` key from a per-card CSV, with a sibling `.beats.json` for running order. Cast names are `{tokens}` that expand to the localized name in the speaker's colour. Diegetic paper uses a `doc.` key prefix and its own budget.
- **A document viewer** that pauses the world, pages like paper, and renders any `doc.` key. If a conclusion is written down anywhere, it can be read there for free.
- **A camera** that bites at anything really there, and withholds *registration* for latents — so "the camera confirmed something and the board recorded nothing" is already an expressible state, and might be exactly what feeds an unreliable node.
- **The Ruler** certifies measurements; `Clause 02` makes a certified corridor stop changing length. Measurements annotate Pip's blueprint at night.

## 5. What the engine needs back

The design is only implementable if it lands as data. Three tables, and **the split between them matters**: prose is translated, structure is not, and mixing them means translators editing a graph.

**① Node table** — one row per node, ~30 rows.

| column | meaning |
|---|---|
| `id` | stable, snake_case, never reused |
| `kind` | `question` / `character` / `evidence` |
| `key` | `board.<id>` — the `tr()` key for its label |
| `unlocked_by` | milestone, anomaly id, or print id |
| `card` | the card it can first appear in |
| `grammar` | `lawful` / `sick` / `—` |

**② Link table** — the hidden compatibility graph.

| column | meaning |
|---|---|
| `from`, `to` | node ids |
| `directed` | whether the order of drawing matters |
| `asserts` | what the player is claiming by drawing it — for the writer, not the player |

**③ Conclusion table** — what a web resolves to.

| column | meaning |
|---|---|
| `id` | stable |
| `question` | which core question it answers |
| `requires` | the set of links that produce it |
| `tier` | `true` / `plausible_flawed` / `illogical` |
| `key` | `board.concl.<id>` — its text |
| `unlocks` | dialogue option ids, flags, gates |
| `ending_steer` | which of the four it pushes toward |

**Format:** the prose columns (`key` targets) belong in the same CSV pipeline as everything else, so they are translatable and diffable. The structural columns — the graph and the requirement sets — belong in a **sibling JSON**, because a compatibility graph is not prose and must not be exposed to translation.

## 6. Questions the Grill should answer

Roughly in dependency order. Anything unanswered here becomes a guess in the engine.

**Shape of the board**
1. How do the ~30 nodes divide between questions, characters and evidence?
2. Are there exactly two core questions ("Where is Anna?", "Where am I?"), or more? Do they arrive at once or unlock?
3. Is a thread **directed**? Does "Anna → the well" mean something different from "the well → Anna"?
4. Can a node carry unlimited threads? Is there a cap, and is the cap diegetic?
5. Can a thread be **removed**? If so, do the endings track the board's *final* state or the *first* conclusion the player reached? This decides whether the system is forgiving or committal, and it is the single biggest feel question here.

**Conclusions**
6. Are conclusions computed from a **set** of links, or from a **path** between two nodes?
7. **When does a conclusion fire** — the instant the last thread lands, or at a ritual moment (the morning after)? An instant answer is responsive; a morning answer is the game's own rhythm.
8. What does an "obviously incorrect answer" look and sound like? Who delivers it — the board, Otto's own voice, a tape?
9. Can a player hold two contradictory conclusions at once?
10. How many conclusions exist in total, and how many are `true`?

**Consequences**
11. Which **dialogue options** does a true conclusion unlock, and in which cards?
12. How does `ending_steer` accumulate — a counter, a latch, a last-one-wins?
13. How does the board relate to `Clauses Known` ≥ 8? Two independent gates, or does one feed the other?
14. What does the completed **Anna-thread** consist of now, in this new design, given it must still satisfy the `Reverse Film` and photo-evidence gates?

**Feeding and reliability**
15. Does a **rumour** node (a filmless side anomaly) behave differently from a print node — can it be threaded, and does it break when the anomaly stops persisting?
16. Does the board know a **Mr. Vacancy print is unreliable**? Every print of it differs from what the shutter saw, which is a ready-made source of plausible-but-flawed theories.
17. What happens to threads attached to a node that is later **invalidated**?
18. Does the **sealed "A." envelope** exist as a node from day 0, and what does opening it in `06 ANNA` do to the board?

**Rhythm and scope**
19. How many nodes and threads exist **by the end of the demo** (cold open + Day 1)?
20. **Does the demo fire any conclusion at all?** The engine recommendation is no — but the first pinning is where the player learns the board is a *tool*, and a board that answers nothing in 40 minutes may not teach that.
21. How does the **hint ladder** touch the board? An idle sleep adds exactly one detail — is that a new node, a new legal link, or a nudge toward one?
22. Does **Sanity** or the `Disposition Tracker` read or write the board?
23. How many **words** does the board carry, and against which line of the 15,000?

---

## 7. One engine-side recommendation, offered not decided

**Build the model whole and ship a thin slice.** The deduction graph is pure arithmetic — nodes, legal links, conclusion resolution, ending steer — and belongs entirely under test, which is where a system this load-bearing earns its cost. The demo then wires the first pinning only: a handful of auto-placed pins the player can string, with no conclusion firing.

That way the demo pays for a few rows of data rather than for a system, and nothing has to be rewritten when the other seven cards arrive.
