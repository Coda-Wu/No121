---
description: Sync the bilingual layer — regenerate the other-language block in notes whose source text changed
argument-hint: [paths] (default: 35-Corkboard/Notes 30-Narrative)
---
Scope: $ARGUMENTS (default `35-Corkboard/Notes` and `30-Narrative`). Always skip: `90-Templates/`, `_Index.md` files, `35-Corkboard/Threads/`, `PROTOCOL.md`, `CLAUDE.md`, `60-Production/Glossary.md`.

**The contract:** in every note, the human source text is everything OUTSIDE `<!-- lang:… -->` marker blocks. You own only the inside of your own marker block. You never modify, reflow, or "fix" anything outside it — including frontmatter, wikilinks, and code blocks.

Per note in scope:

1. Extract the human text (everything outside marker blocks, excluding frontmatter). Detect its dominant language: `en` or `zh-Hans`. Target = the other one.
2. Compute `source-hash` = first 8 hex chars of sha256 of the human text with whitespace runs collapsed.
3. If a marker block exists with the same `source-hash`, **skip the note** (report as unchanged).
4. Otherwise regenerate the block in full — never patch inside it — appended at the end of the note body:

```
<!-- lang:zh source-hash:a1b2c3d4 machine -->
> [!quote]- 中文（机器译稿）
> …译文…
<!-- /lang:zh -->
```

(or `lang:en` / `English (machine draft)` when the source is Chinese). The foldable callout keeps notes visually clean.

**Translation rules:**
- This is a literary pass, not a gloss. Preserve register: deadpan stays deadpan; House Rules clauses render as 公文/合同 legalese; sick-weird prose stays wrong in the same way.
- `60-Production/Glossary.md` is binding for rows marked `ratified` or `locked`. Rows marked `seed` are defaults — use them, but note in the report that they're unratified.
- Loop-names (Otto, Anna, Eve, Bob, Pip, Nan, Renner, Leon, Noel), №121, and all room numbers stay in Latin script / numerals inside Chinese text. The palindrome canon is visual; transliteration destroys it.
- Wikilinks pass through untouched (`[[Otto]]` stays `[[Otto]]`).
- When you must coin a rendering for a recurring canon term not yet in the glossary, choose one, use it consistently in this run, and APPEND it to the glossary as `status: seed` — never leave a new term unglossaried.
- Never translate inside other tools' marker blocks or HTML comments.

**Report and commit:** list synced / unchanged / skipped counts, any newly seeded glossary rows, and any note where source language was ambiguous (mixed roughly 50/50 — translate toward the note's majority and flag it). Commit: `meta: lang sync (N notes, en↔zh)`.
