# №121 vault update: Round 15

**Episodes, selves and the opening dream.** This pack brings the vault's storytelling and level-design notes up to the redesign decided on 13 and 14 November 2026.

It was built against vault commit `0156b4a` ("change tram to bus"). It holds 23 new notes and 66 replaced notes, each as its exact final text.

## How to use it

1. Unzip this folder anywhere outside the vault.
2. Open Claude Code in the vault and send it this:

```text
Apply the Round 15 vault update from <path to this folder>.
Read CLAUDE_CODE_INSTRUCTIONS.md in that folder first and follow it step by step.
Stop and ask me if the working tree is not clean or if any note is in conflict.
```

To look before anything is written, run the dry run yourself:

```bash
python3 <this folder>/tools/apply_round15.py --vault /path/to/vault
```

## What to read first

- `vault/60-Production/Round 15 Decision Record.md`: every decision, where it now lives, and what is open.
- `MANIFEST.md`: every note in the pack, with one line on what changes.
- `round15.patch`: the exact change, for review.

## What the redesign does

| Area | Change |
|---|---|
| Structure | A card is an episode. It opens inside its plot and ends on its strongest beat. The day routine and the nightly routine are gone. |
| Opening | The game and the demo open on a dream that starts and ends with falling. It is the tutorial. |
| Arrival | Told as six to eight memory rooms. The fifteenth night ends at a cliff, and he jumps. |
| Tasks | From residents, the pocket note and the place. No work order. |
| Board | It fills itself. It is never wrong, and it may be incomplete. |
| Darkroom | Played twice. |
| Selves | The Suit and the Agent. No uniform. The Agent's face burns. |
| Mr. Vacancy | It is sharpening Otto in order to consume him and Anna together. The player feels this and is never told. |
| Her side | One reveal in each chapter, in a different form. The Queen game changes form. Its last run is the burning of the usher. |
| Level design | The walk, seven kinds of door, four abilities, six ways between floors, the shadow rules. The Ruler is retired. |

## Read this before you trust it

- **Your wording was not rewritten.** Script files gained one design-note comment each and nothing else. Stickies were not touched.
- **Rewritten notes are set to `draft`.** Promote them to `locked` when you have read them.
- **Some lines are my proposals, not your decisions.** They are marked 🔧 or headed "Proposed, not yet ratified". The main ones: the pocket note's three lines and its being written by the Suit; the three-room reach of a request; the engine's two board tables.
- **Thirteen conflicts with existing canon are listed and not resolved.** They are under "Conflicts to settle" in the Decision Record. The largest are the police markings at the cliff, whether Otto survives the jump, and how the ten seconds with the rose are restaged.
- **Nothing in the round is paid for** under the scope-tax rule. The Scope Ledger has a new section that lists what was added and what was removed.
- **Not covered:** the internals of the mazes, the Queen game's design document, the full grid of sixteen gates, and any new script.
