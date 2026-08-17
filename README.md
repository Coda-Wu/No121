# №121 — world vault starter

An Obsidian vault, pre-structured for the №121 world bible. The bible itself sits in `00-Inbox/` waiting to be atomized. Conventions live in `CLAUDE.md`.

## Setup (~10 minutes)

1. **Git.** From this folder: `git init && git add -A && git commit -m "meta: vault starter"`. Push to a private remote if you want off-machine backup.
2. **Obsidian.** Open this folder as a vault ("Open folder as vault"). Enable core plugins: **Templates** (set template folder to `90-Templates`), **Bases**, **Properties view**, **Backlinks**, **Canvas**. Everything else can stay off.
3. **One community plugin:** **Git** (a.k.a. obsidian-git) if you want auto-commits from inside the app. Optional — Claude Code and the CLI cover git fine.
4. **Claude Code.** From this folder, run `claude`, then paste the first prompt below. It reads `CLAUDE.md` automatically.

## First prompt for Claude Code

> Read CLAUDE.md. Atomize 00-Inbox/world_bible_v1.md into the tree: one note per cast member, screen/place, chapter card, House Rules clause, ending, pocket, and mechanic system, using the frontmatter schemas in 90-Templates. Don't invent or rewrite content — split, link, and tag `status: locked` for ratified canon vs `seed` for 🔧 workshop items. Build `_Index.md` maps of content for each top folder, move the bible to 00-Inbox/processed/, and commit.

Review the result in Obsidian's graph view — the cast/room/flag web should already be visible.

## Ongoing pattern

- New Grill/workshop notes → drop in `00-Inbox/` → ask Claude Code to atomize and link.
- Mood boards → drop images into `50-Moodboards/_assets/` → arrange on a `.canvas` by hand, or ask Claude Code to lay out a first pass grouped by register.
- Views (screen ledger vs the ≤30 lock, cast word-budget table, clause tracker) → create a Base in-app (two clicks: right-click folder → New base, filter on `type`), or ask Claude Code.
- Ask for structure, never build dashboards by hand. If you're tempted to decorate, it's a Claude Code prompt instead.

## Notes

- Images in git are fine at pixel-art reference scale. If large PSD/video refs accumulate, add git-lfs then — not before.
- Mobile: git sync on phones is clunky (Working Copy on iOS, the Git plugin on Android). Simplest is treating this vault as desktop-first.
- Optional later: kepano's official `obsidian-skills` repo (Obsidian-flavored markdown, Bases syntax, JSON Canvas skills for Claude Code) — drop into `.claude/skills/` if Claude Code ever fumbles a format.
