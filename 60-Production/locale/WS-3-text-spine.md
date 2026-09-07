# WS-3 — Text spine (spec)

Status: **Built 2026-09-08**, except the CSV, which waits on Coda's vault pass.

Vault sources: `60-Production/Localization Spec.md`, `Art Spec.md` (bubble dialogue, no portraits — LOCKED), `20-Cast/Naming Canon.md`, `40-Mechanics/The Day Loop.md`.

## Fonts

| Locale | Face | Design em |
|---|---|---|
| en, zh-Hans | `liusong` | 24 px |
| zh-Hant | `Taipei24` | 24 px |
| ja | `EnkaDotMincho24` | 24 px |
| ko | `fusion-pixel-12px-monospaced-ko` | 12 px |

**The face is chosen per locale, not by a fallback chain.** Han unification means zh-Hans, zh-Hant and ja share codepoints — 直 is one codepoint drawn differently in each region — so a glyph fallback cannot pick the regional variant. Only swapping the face can.

**Fusion sits behind every other face** to close gaps, which is a different and smaller job: `liusong` has no em-dash or bullet; `Taipei24` and `EnkaDotMincho24` have no **№**, the game's own title glyph.

Dialogue is **6 px** (Coda). ⚠️ Not pixel-exact at 1080p — see `STATE.md`.

## Names are tokens

Dialogue is written `"...you and {leon} are twins."` — never with the name spelled out. The token expands at runtime to the localized name in that speaker's colour.

1. **A name is localized once**, in `CastRegistry`, not in every line that mentions it. Changing 莱纳 to 雷纳 is one edit, not a search across 15,000 words.
2. **Translators never touch markup.** They keep the token and translate around it, so a colour tag cannot be mangled or dropped.
3. **Auto-detecting names in running text would misfire in Chinese**, which has no word boundaries and where 奶奶 is also just the word for grandmother.

A missing translation degrades to a readable fallback name, never a raw key: "Leon" in the wrong locale is a bug you can play past; `cast.leon` on screen is not.

## Cast colours (Coda, 2026-09-08)

安娜 Anna light beige · 奥托 Otto light white · 伊芙 Eve light orange · 艾尔 Elle light purple · 里昂 Leon light blue · 诺埃尔 Noel **the same** light blue · 莱纳 Renner silver grey · 皮皮 Pip grass green · 奶奶 Nan light brown · 空缺先生 Mr. Vacancy dark red, shaking.

**Leon and Noel sharing a colour is canon and is asserted by a test.** `Naming Canon` gives them no individual palindrome because they are not drawn from anyone — they are the Administration wearing two bodies, and their loop is a form rather than a person. A shared colour means colour can never tell you which twin you are talking to, which is what the tie-continuity gag and the "which twin" permutation axis both need.

## The bubble

Dark box, light grey body, **only names carry colour** — Darkside Detective register.

- **Frame is a `NinePatchRect`**, so Coda's hand-drawn art drops in as a texture swap: same node, same margins, no scene change.
- **Body is a `RichTextLabel`**, which earns wrapping, the typewriter and Mr. Vacancy's shake from one system rather than three.
- Anchored to the speaker, clamped to the screen, **tail still pointing at him** after the box has been clamped against an edge.
- **Typewriter** at 24 cps. Interact once finishes the reveal, again to advance. **It never auto-advances** — `The Day Loop` bans anything that pressures the player to stop thinking.

Prose is BBCode-escaped on the way in, so a stray `[` in a translated line cannot become a tag.

## Localization interchange

**Two files per card.** Full brief in `locale/README.md` — that file is what Coda pastes into the vault.

Verified 2026-09-08: Godot's CSV importer treats **every column after the key as a locale**. A `speaker` column silently produces a `speaker.translation`. And a key→text table carries no **running order**, which dialogue needs. So the CSV is text only, and both speaker and order live in a sibling file.

```
<card>.csv          keys,en,zh_Hans        -> Godot translations
<card>.beats.json   ordered {key, speaker} -> playback
cast.csv            display names          -> written, do not regenerate
```

- Keys are `card.scene.NNN`, lowercase, **numbered in tens** so a line inserted between two others does not renumber everything after it and invalidate work already translated.
- Keys are stable across rewrites: editing a line keeps its key, only a new line gets a new number.
- Diegetic paper takes a `doc.` prefix and its own files.
- `70-Script/` stays the single source; the CSV is derived and never hand-edited, or `wordcount.py` ends up measuring a copy.

> The `Localization Spec` was LOCKED on a **PO** pipeline. CSV is the same pipeline one step earlier and far easier for a solo dev with a bilingual vault; `csv -> po` is a ~20-line script if an agency is ever engaged. Coda approved CSV 2026-09-07; **the vault spec was amended to match on 2026-09-08** and the two now agree.

## Still open

- **The per-card CSVs and beats files** — waiting on Coda's vault pass. `cast.csv` is written.
- **Document viewer** for the House Rules, notices and the Schedule: full-screen overlay, suspends input but not the world. Not built.
- **Gibberish synth voices** — the reveal rate is tuned to land with them, but they belong to audio.
