---
type: production
status: locked
---
# Art Spec

- **Resolution:** 640×360 base, integer scaling.
- **Sprites:** tall, ~90–110 px (6–7 heads); faces capable of stillness.
- **Transforms:** nearest-neighbor with free transforms — a **deliberate mixels policy**, applied consistently.
- **Palette:** master 48–64 colors, plus per-scene **LUT grading via shader**. This is the scope weapon: a re-grade plus prop swaps yields a permutation variant or an era shift ([[Room 434]]'s 1998, [[The Ward]]).
- **Dialogue:** speech bubbles, **no portraits** — Darkside Detective style. The portrait cut funded the purge verb, see [[Scope Ledger]].
- **Dressings:** two per persona-visible screen (performance vs truth), drawn from the existing ≤2-variant budget — see [[Persona Law]].

## Screen ledger

**≤30 base scenes total**, elevator included. A ring floor counts as **1** base scene rendered as 4 faces from shared tilesets — faces are variant-cheap, not separate scenes. See [[Corridor Ring]].

**Demo uses ~10:** [[Street and Tram]] · [[Lobby]] · [[Stairwell]] · [[Elevator]] · [[Corridor Ring]] (floor 2) · [[Room 202]] (+bathroom) · [[Room 242]] · [[Teaching Pocket]] · [[Mirror Maze]] · [[The Ward]].

Every note in `10-World/` carries `in-demo` and `dressings` — the ledger is queryable from the folder.

## Banned techniques

Glitch shaders · datamosh · scanlines · digital-simulation clichés — see [[The Two-Grammar Rule]] and the register board in `50-Moodboards/`.
