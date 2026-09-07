# locale/ — the text pipeline

This file is the brief. **Paste it into the vault** and let the vault-side agent generate against it from `70-Script/`.

Full rationale in `WS-3-text-spine.md`.

---

## Two files per card, not one

A key→text table has no **running order**, and dialogue is a sequence, not a bag of strings. Godot's CSV importer also treats *every column after the key as a locale* — a `speaker` column silently produces a `speaker.translation` file. So speaker and order cannot live in the CSV, and both go in a sibling file.

```
locale/
  cast.csv               display names. already written, do not regenerate
  spool.csv              the text            -> Godot translations
  spool.beats.json       who says it, in order
  prologue.csv
  prologue.beats.json
```

### `<card>.csv` — the text

Exactly three columns. Nothing else, ever.

```csv
keys,en,zh_Hans
spool.tape_2.010,"Otto's line here","..."
spool.tape_2.020,"the next one","..."
```

- UTF-8, no BOM. Quote any field containing a comma.
- `\n` inside a quoted field becomes a line break in game.
- More locales are new **columns** (`zh_Hant`, `ja`, `ko`), never new files.

### `<card>.beats.json` — who, and in what order

```json
{
  "card": "spool",
  "scenes": {
    "tape_2": [
      { "key": "spool.tape_2.010", "speaker": "otto" },
      { "key": "spool.tape_2.020", "speaker": "otto" }
    ],
    "dream_1": [
      { "key": "spool.dream_1.010", "speaker": "eve" }
    ]
  }
}
```

`speaker` is a lowercase cast id: `otto anna eve elle leon noel renner pip nan vacancy`. It must match exactly — it selects the voice and the name colour.

---

## Keys

`card.scene.NNN`, all lowercase.

- **Number in tens** — `010, 020, 030`. A line inserted between two others must not renumber everything after it, because renumbering invalidates every translation already done against those keys.
- **Keys are stable across rewrites.** Editing a line's text keeps its key. Only a genuinely new line gets a new number.
- **Diegetic paper takes a `doc.` prefix** and its own files: `doc.clause_02.010`. `70-Script/_Protocol.md` budgets `type: script` and `type: document` separately, and the keys keep that separation.

## Names are tokens, never spelled out

Write `{leon}`, not `Leon` and not `里昂`.

```csv
spool.lived.010,"So... you're saying that you and {leon} are twins.","所以…你是说，你和{leon}是双胞胎。"
```

Valid tokens: `{otto} {anna} {eve} {elle} {leon} {noel} {renner} {pip} {nan} {vacancy}`

Three reasons this matters:

1. **A name is localized once**, in `cast.csv`. Changing 莱纳 to 雷纳 is one edit, not a search across 15,000 words.
2. **The token carries the speaker's colour** automatically. Spelled-out names render as plain body text and silently lose it.
3. **Auto-detecting names in running text would misfire in Chinese**, which has no word boundaries and where 奶奶 is also just the word for grandmother.

An unknown token is left on screen verbatim, so a typo shows up in playtest rather than vanishing.

## Brackets

A literal `[` is escaped automatically and cannot become markup. Write dialogue normally.

---

## Rules for the vault-side agent

1. **`70-Script/` is the source.** The CSV is derived from it and never edited by hand — a fix goes into the script, and the CSV is regenerated.
2. **Never renumber existing keys.** New lines take the gaps.
3. **Do not touch `cast.csv`** unless Coda changes a cast name.
4. `tools/wordcount.py` still counts the vault, not the CSV. The CSV must not become a second source, or the 15,000-word lock is measuring a copy.
5. Emit one CSV **and** one beats file per card. A CSV with no beats file is unplayable text.
6. Leave `en` empty rather than guessing if a line is unwritten. An empty string is visibly missing; an invented one is not.
