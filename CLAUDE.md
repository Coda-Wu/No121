# CLAUDE.md — №121 world vault

Obsidian vault for the world bible, cast, narrative, mechanics, and mood boards of **№121** (working title). Everything here is plain Markdown with YAML frontmatter, plus `.canvas` (JSON Canvas) boards and image assets. It is version-controlled with git.

**Division of labor:** Claude Code does structural work; Coda does creative work. You handle atomizing documents into notes, wikilink and backlink integrity, frontmatter hygiene, regenerating `_Index.md` maps of content, generating and editing `.canvas` files, Bases views, and git commits. You never spend effort on themes, CSS snippets, dashboards, or visual decoration of any kind — the default theme is canon.

## Layout

- `00-Inbox/` — raw drops (session notes, new documents). Atomize into the tree, then move the original to `00-Inbox/processed/`.
- `10-World/` — one note per base screen or place. `Building/` (lobby, rings, rooms 202/212/232/313/434, 101, 242, 696…), `Pockets/` (teaching pocket, maze family, Penrose stair…), `Satellites/` (street/tram, the Ward).
- `20-Cast/` — one note per voice, including Renner, the Couple, and Mr. Vacancy.
- `30-Narrative/` — `Chapters/` (one note per day card: №121, SPOOL, LIVED, RADAR, REPAPER, ANNA, DEED, ROTOR, REDIVIDER), `Endings/`, `Anecdotes/`, plus tapes and the corkboard thread.
- `40-Mechanics/` — systems (camera, ruler, persona law, day loop, night phase, festering…). `Clauses/` holds one note per House Rule; `Flags/` holds one note per permanent "the Building remembers" flag.
- `50-Moodboards/` — `.canvas` boards. Binary images live only in `50-Moodboards/_assets/`; never modify binaries.
- `60-Production/` — scope ledger, art/audio/localization specs, schedule, positioning, and 🔧 workshop agendas.
- `90-Templates/` — frontmatter schemas (used by the core Templates plugin). These are the source of truth for properties; keep existing notes conforming.

## Conventions

- Wikilinks only (`[[Otto]]`), never relative markdown paths. When renaming a note, update every backlink.
- Every note opens with frontmatter containing at least `type` and `status` (`seed` → `draft` → `locked`).
- One entity per note. Keep notes short; link instead of duplicating canon. If two notes state conflicting canon, flag it — never silently resolve against a `status: locked` note.
- Filenames in Title Case, no dates in names. Attachments keep their original names inside `_assets/`.
- `_Index.md` in each top-level folder is a generated map of content. Regenerate on request; don't hand-curate.
- Flag notes list `set-by` and `read-by` as wikilinks to screens/beats, so the graph shows the permutation web.
- You may create and edit `.canvas` files directly (JSON Canvas format). Group mood images with text nodes for register labels (lawful weird / sick weird / banned).

## Scope guard

Scope locks live in `60-Production/` once atomized (≤30 base scenes, ~2 dressings avg, ≤15,000 words, 9–11 clauses, ≤6 bespoke pockets, 8–10 loops, 3–5 blackouts…). The scope-tax rule applies to the vault too: if a requested addition would breach a lock, say so and ask which deletion pays for it before executing. On request, report the running spoken-word total across dialogue and tape text.

## Git

- Commit after each coherent task with a scoped prefix: `world:`, `cast:`, `narrative:`, `mech:`, `mood:`, `prod:`, `meta:`.
- `.obsidian/workspace*.json` is gitignored (per-machine UI state). Other `.obsidian/` settings are versioned deliberately so the setup is reproducible.
- Never rewrite history; never force-push.
