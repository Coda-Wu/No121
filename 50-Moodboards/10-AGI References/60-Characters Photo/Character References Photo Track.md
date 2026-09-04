---
type: prompts
status: seed
---
# Character References — Photo Track

Costume, silhouette, pose, figure lighting. **Redraw source only** — the game ships bubble dialogue and no portraits ([[Art Spec]]). Blocks in [[Blocks and Constants]].

## T3 — full-body reference

> {FORMAT-FILM}. Full-body [Angle] of [CHARACTER BLOCK], [Face treatment], standing in [Minimal setting], lit by [Primary light], {PALETTE-BASE}, {MOOD}, plain uncluttered background, entire figure in frame head to toe, feet visible.

**[Angle]:** strict side profile *(the sprite's native view — prioritize this)* · three-quarter view

**[Minimal setting]:** bare corridor · elevator interior · in front of a numbered door

**[Face treatment]:** face turned away from camera · face lost in shadow · backlit to a silhouette · smooth featureless face
*(the last yields mannequin-blank results — sometimes exactly right for this game, sometimes junk; the first three are reliable)*

## T3B — the persona diptych

The ownable image, and a capsule composition candidate — see `90-Capsule and Key Art`.

> split-frame diptych, the same man photographed twice in identical stance and framing: left panel, [OTTO-AGENT]; right panel, [OTTO-HANDYMAN]; both standing in an elevator interior, lit by [Primary light], {PALETTE-BASE}, {MOOD}, {FORMAT-FILM}.

---

## Character blocks

Shape for every block: build + one garment sentence + posture + one identifying detail. **Two sentences maximum** — models ignore the rest.

**[OTTO-AGENT]** — [[Otto]], hub self
> a trim man with neat dark hair in a plain black two-piece suit, narrow black tie, white shirt, polished black shoes, composed upright posture, [Constant detail]

**[OTTO-HANDYMAN]** — [[Otto]], floor self
> the same trim man with neat dark hair in a worn [olive-drab · slate-gray] coverall, sleeves rolled, work boots, tool belt, cloth name patch, same composed upright posture, [Constant detail]

**[Constant detail]** — 🔧 **unchosen.** The invariant that survives both personas so Otto reads as Otto. Example: *an old camera on a neck strap.* Coda's call — but once chosen, the wording stays identical in every prompt, both states.

**[EVE]** — [[Eve]], the Nurse, clinical register
> a calm woman in a plain white nursing uniform of no particular decade, flat shoes, hands at rest, unhurried posture, a folded blanket over one arm

**[LEON-NOEL]** — [[Leon]] / [[Noel]], one role, two bodies
> a trim man in a crisp white shirt under a plain dark waistcoat, [Tie], standing at patient attention with his hands at his sides

**[Tie]** — the only thing that differs between the two bodies. [[Leon]]: *a plain black necktie.* [[Noel]]: *a bolo tie on a thin black cord with a plain brass slide* — administrative and odd, never western: no turquoise, no conchos, no tooling.

**Mirrored, not different.** Same build, same haircut, same waistcoat. Everything sided reverses between them — hair part, watch wrist, waistcoat pocket in use — and the sprite runs **one idle loop played mirrored**, so the two bodies breathe on the same clock. Generate the pair as the same man photographed twice in identical stance and framing, then flip one.

**[ELLE]** — [[Elle]], the Insomniac
> a heavyset man in a dressing gown over day clothes, slippers, standing in a doorway, holding a mug in both hands

**[NAN]** — [[Nan]], 1998
> an elderly woman in a floral housecoat and cardigan, house slippers, one hand on a doorframe, warm settled posture

**[PIP]** — [[Pip]], the Child Cartographer
> an infant on hands and knees on a carpeted floor, seen from adult standing height, a rolled paper plan beside them

**[VACANCY]** — [[Mr. Vacancy]]
> the same trim man, identical build and hair, wearing whichever of the suit or the coverall the reference sheet's Otto is not, absolutely still, [Face treatment]

---

## Canon constraints — read before generating

- **[[Anna]] has no body outside the endings.** Generating her as a standing figure invents canon. Refs of her belong to ending exploration only, and go in `90-Capsule and Key Art` with that flag on them.
- **[[Renner]] has no standing form in the present** — he is merged into the junction, wires and warmth, no gore. Prompt the *junction*, in `40-Details and Props`, not a man.
- **[[The Couple]] are never seen.** No figure refs. Ever.
- **The doppelganger rule is absolute:** [[Mr. Vacancy]] wears the persona Otto is not. A ref showing both in the same costume is wrong, not a variant.
- Faces stay unresolved by policy — the game has no portraits, and a face you fall in love with here is a face you will try to smuggle in later.

## Squint test

Shrink every ref to ~90 px tall before filing it. What survives — silhouette, value contrast, the constant detail — is what the sprite can actually carry.
