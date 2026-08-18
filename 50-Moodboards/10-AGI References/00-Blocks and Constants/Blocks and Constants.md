---
type: prompts
status: seed
---
# Blocks and Constants

The single source of truth for every `{BLOCK}` used in `10-AGI References/`. **Edit here, and every folder inherits the change.** Source system: `50-Moodboards/00-AGI References/no121-prompt-templates-v1.md`.

Assembly is always: `{FORMAT}` + subject template + `{PALETTE}` + `{MOOD}` (+ optional `{NEGATIVE}`).

`{BLOCKS}` are constants. `[Variables]` are per-prompt swaps — everything in square brackets is yours to replace.

---

## {FORMAT-FILM}

> still frame from an early-2000s network television mystery series, shot on 35mm film, soft halation, fine film grain, muted broadcast color

## {FORMAT-GAME}

Layout and color thumbnails only. Models fake pixel grids — never treat the output as real pixel art.

> screenshot of a 2D side-view adventure game, flat perspective, limited color palette, painterly low resolution

## {PALETTE-BASE}

> cream and honeyed amber highlights, tungsten lamplight, walnut and tan wood tones, faded rose and dusty salmon fabrics, olive and mustard institutional paint, muted teal-gray shadows

## {PALETTE-NIGHT}

Append when relevant.

> slate blue night tones, washed lavender dusk light

## {MOOD}

> orderly, too quiet, warmly nostalgic, vacant, faintly wrong

## {NEGATIVE}

If the generator supports negative prompts — this is what kills era drift.

> modern smartphones, flat-screen TVs, LED strip lighting, minimalist decor, lens flare, HDR, oversaturated

Add `people` for empty environment shots; remove it for character prompts.

---

## [Intruder] — the reserved-accent rule

**One per prompt, maximum.** Omit entirely for pure-nostalgia shots. Warmth is the base; wrong is the guest.

> a single hot cyan glow · an acid green light · one signal-red point of light · a deep ultramarine doorway

## [Dressing] — the persona axis

Every persona-visible screen has two, per [[Persona Law]] and the ≤2-variant budget in [[Art Spec]]. Name one explicitly in environment prompts:

- **A / performance** — composed, tidy, everything where it should be. What the Building shows the Agent.
- **B / truth** — the same tilemap, unperformed. What the uniform sees.

## [Wrongness] — exactly ONE per prompt

Lawful ([[The Two-Grammar Rule]]) — clean, rule-bound, almost polite:

> hallway slightly too long · a corridor with five corners · the same corridor face occurring twice · every door ajar at the same angle · ceiling a little too low

Sick — imperfect mimicry, one flaw in an otherwise correct pattern:

> a door where a window should be · furniture facing the wall · wet floor with no source · one apartment door with no number · a numeral hanging from a fallen nail

## [Primary / Secondary light]

> tungsten wall sconce · single fluorescent tube · sodium streetlight through blinds · television glow · elevator cab light · red EXIT sign glow · desk lamp · daylight through frosted glass

## [Era prop]

> CRT television · answering machine with a blinking light · corded telephone · cork noticeboard · halogen torchiere · floral carpet runner · wood-veneer paneling · popcorn ceiling · beige computer tower

---

## Usage rules — apply to every folder

1. **Never name games, shows, films, actors, or characters in a prompt.** Describe era and craft instead.
2. **One wrongness, one intruder color, maximum.**
3. **Generate large at 16:9, crop afterward. Study, never trace.** These are redraw sources, never shipped assets.
4. **Squint test every character ref** — shrink to ~90 px tall. Whatever survives is what the sprite can carry.
5. **Log template + variables** in the ref's filename or a note beside it, so the board stays reproducible.
6. **Banned regardless of prompt:** glitch shaders, datamosh, scanlines, digital-simulation clichés. Wrongness here is analog, architectural, bureaucratic — see [[The Ontology]].
