# №121 — AI Reference Prompt System v1

Scope: mood-board reference generation only. Outputs are redraw sources, never shipped assets, never traced.

## How the system works

Every prompt assembles as: `{FORMAT}` + subject template + `{PALETTE}` + `{MOOD}` (+ optional `{NEGATIVE}`).

`{BLOCKS}` are constants — edit once, reuse everywhere. `[Variables]` are per-prompt swaps. All menus below are starters: overwrite with canon locations, props, and wrongness from the vault.

## Shared blocks

**{FORMAT-FILM}** — the atmosphere workhorse:
> still frame from an early-2000s network television mystery series, shot on 35mm film, soft halation, fine film grain, muted broadcast color

**{FORMAT-GAME}** — layout/color thumbnails only (models fake pixel grids; never treat output as real pixel art):
> screenshot of a 2D side-view adventure game, flat perspective, limited color palette, painterly low resolution

**{PALETTE-BASE}** — vocabulary drawn from the locked palette-80 lanes:
> cream and honeyed amber highlights, tungsten lamplight, walnut and tan wood tones, faded rose and dusty salmon fabrics, olive and mustard institutional paint, muted teal-gray shadows

**{PALETTE-NIGHT}** — append when relevant:
> slate blue night tones, washed lavender dusk light

**[Intruder]** — the reserved-accent rule in prompt form. Use ONE per prompt maximum; omit entirely for pure-nostalgia shots:
> a single hot cyan glow · an acid green light · one signal-red point of light · a deep ultramarine doorway

**{MOOD}**:
> orderly, too quiet, warmly nostalgic, vacant, faintly wrong

**{NEGATIVE}** — if the generator supports negative prompts (kills era drift):
> modern smartphones, flat-screen TVs, LED strip lighting, minimalist decor, lens flare, HDR, oversaturated
> (add "people" for empty environment shots; remove it for character prompts)

---

## T1A — Environment, long shot (film track)

> {FORMAT-FILM}. Wide establishing shot of [Location] in an aging apartment building, [Architecture detail], [Era prop], lit by [Primary light] with [Secondary light], {PALETTE-BASE}, [Intruder], [Wrongness], empty of people, signage present but unreadable, {MOOD}, [Camera], generous negative space.

**[Camera]:** one-point perspective straight down the corridor · flat side-on elevation, like a dollhouse cross-section

The dollhouse phrasing is the one to lean on — it produces side-view-native compositions that map directly to screen layouts.

## T1B — Environment, long shot (game-view track)

> {FORMAT-GAME}. Interior cross-section of [Location] in an old apartment building, side-on elevation, the room reads left to right, [Era prop], lit by [Primary light], {PALETTE-BASE}, [Wrongness], {MOOD}.

## T2 — Detail, close shot (film track)

> {FORMAT-FILM}. Insert close-up of [Object] on [Surface], [Material and age detail], lit by [Primary light], shallow depth of field, {PALETTE-BASE}, [Intruder — or omit], {MOOD}, centered tabletop framing.

---

## T3 — Character reference (photo track)

Purpose: costume, silhouette, pose, and figure lighting. Redraw source only.

> {FORMAT-FILM}. Full-body [Angle] of [CHARACTER BLOCK], [Face treatment], standing in [Minimal setting], lit by [Primary light], {PALETTE-BASE}, {MOOD}, plain uncluttered background, entire figure in frame head to toe, feet visible.

**[Angle]:** strict side profile (the sprite's native view — prioritize this) · three-quarter view

**[Minimal setting]:** bare corridor · elevator interior · in front of a numbered door

**[Face treatment]:** face turned away from camera · face lost in shadow · backlit to a silhouette · smooth featureless face
*(the last one yields mannequin-blank results — sometimes exactly right for this game, sometimes junk; the first three are reliable)*

**Character blocks:**

**[OTTO-AGENT]**
> a trim man with neat dark hair in a plain black two-piece suit, narrow black tie, white shirt, polished black shoes, composed upright posture, [Constant detail]

**[OTTO-HANDYMAN]**
> the same trim man with neat dark hair in a worn [olive-drab · slate-gray] coverall, sleeves rolled, work boots, tool belt, cloth name patch, same composed upright posture, [Constant detail]

**[Constant detail]** — the invariant that survives both personas so Otto reads as Otto. Example: "an old camera on a neck strap." Your call what it is — but once chosen, keep the wording identical in every prompt, both states.

Other cast members get their own blocks in the same shape: build + one garment sentence + posture + one identifying detail. Two sentences maximum; models ignore the rest.

## T3B — Persona shift diptych

> split-frame diptych, the same man photographed twice in identical stance and framing: left panel, [OTTO-AGENT]; right panel, [OTTO-HANDYMAN]; both standing in an elevator interior, lit by [Primary light], {PALETTE-BASE}, {MOOD}, {FORMAT-FILM}.

The transformation is the ownable image — this template doubles as capsule/trailer composition exploration for Round 8.

## T4 — Character, sprite-adjacent track

> {FORMAT-GAME}, single full-body character, [Proportion], facing right in strict profile, strong simple silhouette, [selective dark outlines · no outlines], limited palette of [3–5 words from the palette lanes], plain flat background.

**[Proportion]:** squat cartoon proportions, about two and a half heads tall · stylized, about three and a half heads tall · slightly stylized, four heads tall

---

## Menus (starters — overwrite with canon)

**[Location]:** lobby with brass mailboxes · reception desk · corridor of numbered doors · elevator interior · stairwell · laundry room · boiler room · kitchenette

**[Era prop]:** CRT television · answering machine with a blinking light · corded telephone · cork noticeboard · halogen torchiere · floral carpet runner · wood-veneer paneling · popcorn ceiling · beige computer tower

**[Primary / Secondary light]:** tungsten wall sconce · single fluorescent tube · sodium streetlight through blinds · television glow · elevator cab light · red EXIT sign glow · desk lamp · daylight through frosted glass

**[Wrongness]** — exactly ONE per prompt: hallway slightly too long · ceiling a little too low · every door ajar at the same angle · a door where a window should be · furniture facing the wall · wet floor with no source · one apartment door with no number

**[Object]:** room key on a fob · stack of developed photographs · intercom panel · key cabinet with one empty hook · ashtray · mail slot · fuse box · guest ledger

---

## Usage rules

1. **Never name games, shows, films, actors, or characters in a prompt.** Describe era and craft instead. Named-IP prompts drag output toward the exact comps we're diverging from, and train your eye on the wrong target.
2. **One wrongness, one intruder color, maximum.** Warmth is the base; wrong is the guest. This mirrors the reserved-accent rule in the palette.
3. **Generate large at 16:9, crop to canvas ratio afterward.** Study, never trace.
4. **Squint test every character ref:** shrink it to ~90px tall. Whatever survives the shrink is what the sprite can actually carry — silhouette, value contrast, the constant detail.
5. **Log template + variables** in each ref's filename or vault note so the board stays reproducible (mood: scope).
