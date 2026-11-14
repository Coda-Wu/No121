# Instructions for Claude Code: apply Round 15 to the №121 vault

You are working in the №121 Obsidian vault. Its own `CLAUDE.md` is the law for conventions, and it still applies. This pack carries a redesign that Coda decided on 13 and 14 November 2026, called **Round 15**. Your job is structural: put the notes in place, keep links and indexes sound, and report. You do not make creative decisions.

Read `MANIFEST.md` first. Then read `vault/60-Production/Round 15 Decision Record.md`, which lists every decision and every open question.

## What is in this pack

| Path | What it is |
|---|---|
| `vault/` | The exact final content of every note that is new or changed, at its vault path. 23 new, 66 replaced. |
| `manifest.json` | Each file's action and its checksums before and after. |
| `MANIFEST.md` | The same list, readable, with one line on what changes. |
| `round15.patch` | The exact change as a git patch against commit `0156b4a`. For review and for hand merges. |
| `RESIDUAL_TERMS.md` | Lines that still use a retired or renamed term after the update. |
| `tools/apply_round15.py` | Writes the files, and refuses to overwrite a note that changed since `0156b4a`. |
| `tools/check_links.py` | Lists wikilinks that resolve to no note. |

## Rules for this task

1. **Do not rewrite creative text.** Sticky prose, script lines and Coda's wording stay as they are.
2. **Do not resolve any 🔧 item.** Every open point is Coda's. List them in your report.
3. **Do not promote a status.** Notes rewritten in this round are `draft`. Only Coda sets `locked`.
4. **Do not rename or delete a note.** This pack renames nothing, so no backlink needs moving.
5. **Never edit** `35-Corkboard/Notes/`, `00-Inbox/processed/`, or `95-Reviewer-Packet/.build/`.
6. **In `70-Script/`** the pack only adds one HTML comment under the title of ten files. Add no other text there.
7. If a note in the vault disagrees with a note in this pack, the pack wins **only** where the text is marked Round 15. Otherwise flag it and leave it.

## Steps

### 1. Check the starting point

```bash
git status --short          # must be clean
git log --oneline -1        # the pack was built on 0156b4a "change tram to bus"
```

If the working tree is not clean, stop and ask Coda. A different HEAD is acceptable: step 2 checks each file on its own.

### 2. Dry run

```bash
python3 <pack>/tools/apply_round15.py --vault .
```

It prints how many files are ready, already applied, or in conflict. It writes nothing.

### 3. Apply

```bash
python3 <pack>/tools/apply_round15.py --vault . --apply
```

**If it reports conflicts,** those notes changed after `0156b4a`, and they were not written. For each one:

- open the pack's version at `<pack>/vault/<path>` and the matching hunk in `round15.patch`;
- carry the Round 15 change into the vault's current note by hand, and keep everything Coda wrote since;
- if you cannot tell which text should stand, leave the note alone and list it in your report.

### 4. Check the links

```bash
python3 <pack>/tools/check_links.py .
```

The changed and new notes have no dangling wikilink. The vault had about 100 dangling targets before this pack, mostly pasted images. Two matter:

- `[[Street and Tram]]`. The note was renamed to `Street and Bus` in `0156b4a`, and some links were left behind. The pack fixed them in the notes it touched. Fix any that remain, except in the folders named in rule 5.
- `[[The Script Protocol]]` in `20-Cast/The Aunt and Uncle.md`. It predates this pack. Report it. Do not guess the target.

### 5. Regenerate what is generated

- **`_Index.md`** in `10-World/`, `20-Cast/`, `30-Narrative/`, `40-Mechanics/` and `60-Production/`. They are generated maps and the pack did not touch them. They must pick up the 23 new notes. In `30-Narrative/_Index.md` the critical beat of card 01 is now "The second fall, and the waking in 202".
- **`70-Script/_Word Count.md`**: run `python3 tools/wordcount.py`. Never edit it by hand. The spoken total must not change, because the pack added comments only. It was 368 Han characters when the pack was built. The file was already stale by one title, from the tram to bus rename.

### 6. Sweep the residual terms

Open `RESIDUAL_TERMS.md`. Round 15 changed these terms:

| Old | New |
|---|---|
| Agent Otto, the Agent (the hub self, in the suit) | **the Suit** |
| Handyman Otto, the Handyman, the uniform (the floor self) | **the Agent** |
| work order | none. See `The Pocket Note` and `Requests`. |
| Night Phase, as a step in a routine | none. See `Episode Structure`. |
| The Ruler, certification, the Payout | retired |
| Dream 0, the Calling | `The Opening Dream` |
| tram | bus. This is the vault's own earlier rename. |

**Order matters for the two selves.** The word *Agent* has changed meaning. Never run a blind replace. Read each line.

Treat each group like this:

| Where | What to do |
|---|---|
| Notes written or rewritten by this pack | Leave. They name the old terms on purpose, to point at what was retired. |
| Other notes in `10-World/`, `20-Cast/`, `30-Narrative/`, `40-Mechanics/`, `60-Production/` | If the line names a self, fix the term. If the line describes a retired system, add nothing and list the note in your report. Do not rewrite the passage. |
| `handyman` as a job: "the predecessor handyman", "handyman roster", HANDYMAN (ACTING) | Leave. The post is a job title and not the name of a self. Whether the post survives is an open question. |
| `50-Moodboards/` prompt notes | List them in your report. Coda decides, because the prompts drive image work. Two lines in `Blocks and Constants.md` are already fixed. |
| `35-Corkboard/Notes/`, `00-Inbox/processed/`, `95-Reviewer-Packet/.build/` | Never edit. |
| `70-Script/` | Never edit the text. |
| `_Index.md` files | Regenerate, as in step 5. |

### 7. Things outside the Markdown notes

Do not change these. Report each as out of date:

- **`30-Narrative/Flowcharts/*.canvas`.** One canvas for each card, laid out in the order of the old day, ending in a night column. Round 15 changes that order. Ask Coda before regenerating any canvas.
- **`35-Corkboard/Corkboard.canvas`.** A generated view. Leave it.
- **`95-Reviewer-Packet/`.** It is a build of the vault and is now stale. Rebuild it only with its own build step, and only if Coda asks.
- **`60-Production/locale/`.** `cast.csv` and the text spine are not touched. The Glossary has new `seed` rows for the two selves. Do not ratify them.
- **The engine repository.** `30-Narrative/corkboard.md` is a brief from the engine side for a deduction board. Round 15 supersedes it. The two tables the engine now needs are at the end of `30-Narrative/The Corkboard Thread.md`. Carrying that to the engine repo is a separate task.

### 8. Translation layer

None of the notes in this pack carries a `<!-- lang:… -->` block. Run `/translate` at the session seam as usual. New terms go to the Glossary as `seed`. Invent none silently.

### 9. Scope

The vault's scope guard says that an addition which breaches a lock must name its deletion first. Round 15 adds scenes, systems and words, and **nothing in it is paid for yet**. Coda knows this. It is written down in the Round 15 section of `60-Production/Scope Ledger.md`. Do not block on it, and do not try to pay for it. Mention it in your report.

### 10. Commit

Use the vault's prefixes, one commit for each coherent group. Never rewrite history and never force-push. A suggested split:

```text
narrative: round 15: episodes, threads, the opening dream, memory rooms, her side
narrative: round 15: chapter notes 01 to 08 in episode form
mech: round 15: retire the ruler, the work order and the night phase; pocket note and requests
mech: round 15: the walk, doors, abilities, connectors, shadows, persona law
world: round 15: the cliff, the rock path, new connectors, room 222, persona terms
cast: round 15: otto, mr. vacancy, leon, renner, elle
prod: round 15: decision record, scope ledger, workshop agendas, glossary
meta: round 15: script design notes, indexes, word count
```

### 11. Report to Coda

End with a short report:

1. Files written, files in conflict, and how each conflict was merged or left.
2. Dangling links that remain.
3. Residual terms you fixed, and those you left for Coda, by note.
4. Out-of-date items from step 7.
5. The list headed "🔧 Open after this round" from the Decision Record, unchanged.

## What this pack does not contain

- **The mazes.** The Blot, the Fold, the blind mazes, the lung maze and the Turn are named in the notes and are not atomized. Their designs are in other working documents.
- **The Queen game's design document.**
- **The grid of sixteen gates.** It exists only as a diagram in the redesign plan. `Abilities and Gates` records what the plan's text states.
- **New script.** The opening dream, the memory rooms, the second Leon scene and the side requests have no script files yet. The ten design-note comments in `70-Script/` say where each is needed.
