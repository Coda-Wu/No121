---
type: production
status: locked
---
# Localization Spec

**Order:** EN first → zh-Hans + zh-Hant second → EFIGS + JA third.

## Architecture, built from day one
- `tr()` over a **CSV pipeline** — one `keys,en,zh_Hans` table per card, a sibling `.beats.json` carrying speaker and running order. Generated from [[70-Script]] by `tools/build_locale.py`; contract in [[README]], spec in [[WS-3-text-spine]], coverage in [[_Index]].
  - *Amended 2026-09-07 (Coda).* This spec previously said PO. CSV is the same pipeline one step earlier and far cheaper for a solo dev with a bilingual vault; `csv → po` is a ~20-line script if an agency is ever engaged. More locales are new **columns**, never new files.
- **Cast display names are localized**, one row each in `locale/cast.csv` — see [[Glossary]] for the policy and the palindrome consequence. Dialogue references a name as a `{token}`, so a name is localized once and always carries the speaker's colour.
- **A face per locale, not a fallback chain.** Han unification means zh-Hans, zh-Hant and ja share codepoints drawn differently per region; only swapping the face picks the regional variant. Fusion Pixel sits behind every face to close gaps (em-dash, bullet, **№**).
- A **document-viewer layer** for diegetic text — the House Rules, notices, the Schedule, [[Pip]]'s blueprint annotations. Diegetic paper exports under its own `doc.` key prefix and its own budget. 🔧 Not built.

Diegetic text is a large share of the 15,000-word budget in the [[Scope Ledger]]; the viewer layer is what keeps it translatable.

## Open
🔧 Faces are now chosen per locale — the table is in [[WS-3-text-spine]] (`liusong` for en/zh-Hans, `Taipei24`, `EnkaDotMincho24`, `fusion-pixel-12px-monospaced-ko`, Fusion behind all of them). **License verification is still outstanding** on the pixel faces. See [[Workshop Agendas]].
