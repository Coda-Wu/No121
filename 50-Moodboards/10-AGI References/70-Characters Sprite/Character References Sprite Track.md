---
type: prompts
status: seed
---
# Character References — Sprite Track

Silhouette and palette studies at game scale. Layout thumbnails only — **models fake pixel grids**; never treat output as real pixel art. Blocks in [[Blocks and Constants]].

## T4 — single figure

> {FORMAT-GAME}, single full-body character, [Proportion], facing right in strict profile, strong simple silhouette, [selective dark outlines · no outlines], limited palette of [3–5 words from the palette lanes], plain flat background.

**[Proportion]:** slightly stylized, six heads tall · slightly stylized, seven heads tall

## T4-P — persona pair at scale

> {FORMAT-GAME}, two full-body characters side by side, the same figure in a dark suit and in a work coverall, [Proportion], both facing right in strict profile, identical silhouette apart from costume, limited palette of [3–5 words from the palette lanes], plain flat background.

## T4-S — silhouette sheet

The real test. Run it for every cast member you intend to sprite:

> {FORMAT-GAME}, a row of solid black silhouettes of [Count] different standing figures on a flat cream background, each with distinct body shape and one distinguishing carried object, all facing right in strict profile, no interior detail.

---

> [!warning] Canon conflict — flagged, not resolved
> The v1 template's `[Proportion]` menu offers **2.5 / 3.5 / 4 heads tall**. [[Art Spec]] is `status: locked` and specifies **tall sprites, ~90–110 px, 6–7 heads, faces capable of stillness**. Those are different games — 2.5 heads is a chibi, 6–7 heads is a person.
>
> The `[Proportion]` menu above follows the locked note. If Coda wants the squat proportions instead, that is an [[Art Spec]] amendment and a workshop item, not a prompt tweak — and the scope-tax rule applies, since sprite proportion drives every animation estimate in the hours audit.

## Palette lanes for the `[3–5 words]` slot

Pull from the master 48–64 ([[Art Spec]]), never invent lanes:

> cream · honeyed amber · tungsten gold · walnut · tan · faded rose · dusty salmon · olive · mustard · muted teal-gray · slate blue · washed lavender

One intruder accent maximum, and only when the character earns it — see [[Blocks and Constants]].

## Notes

- Strict right-facing profile is the native sprite view; generate it before anything else.
- The **squint test is the whole point of this folder**: shrink to ~90 px and see what is left.
- Nothing here is traced. These are silhouette arguments, not assets.
