---
type: prompts
status: seed
---
# Environment Cross-Sections — Game View Track

Layout and color thumbnails that read left-to-right like the actual screens. **Never treat the output as pixel art** — models fake the grid. Blocks in [[Blocks and Constants]].

## T1B — interior cross-section

> {FORMAT-GAME}. Interior cross-section of [Location] in an old apartment building, side-on elevation, the room reads left to right, [Era prop], lit by [Primary light], {PALETTE-BASE}, [Wrongness], {MOOD}.

## T1B-R — ring face study

For the four faces of one floor, per [[Corridor Ring]]:

> {FORMAT-GAME}. Interior cross-section of a corridor face in an old apartment building, side-on elevation, [Door count] numbered doors evenly spaced along the wall, a perspective-rotating corner at the [left · right] edge, [Era prop], lit by [Primary light], {PALETTE-BASE}, {MOOD}, flat unified value range.

**[Door count]:** three · four · five

## T1B-P — permutation pair

The same face, rearranged, to test whether a screen stays legible after the Building moves it — see [[Permutation and Persistence]].

> {FORMAT-GAME}. Two variants of the same corridor face side by side, identical palette and lighting, [What moved] differing between them, side-on elevation, {PALETTE-BASE}, {MOOD}.

**[What moved]:** the door order · the corner position · one door's number · which end the radiator sits at

---

## Constraints from locked canon

Do not prompt against these — they are the ruler you judge output with ([[Art Spec]]):

- 640×360 base, integer scaling. Thumbnails inform layout, never resolution.
- Master palette **48–64 colors**, per-scene LUT grading.
- **≤30 base scenes**, elevator included. Faces are variant-cheap; new *rooms* are not.
- Two dressings per persona-visible screen — generate both or neither.
- No filler rooms: every enterable space holds a case beat, a side anomaly, a resident scene, or a document.

## Ready-to-paste example

> screenshot of a 2D side-view adventure game, flat perspective, limited color palette, painterly low resolution. Interior cross-section of a caretaker's flat in an old apartment building, side-on elevation, the room reads left to right, cork noticeboard and a corded telephone, lit by a desk lamp, cream and honeyed amber highlights, tungsten lamplight, walnut and tan wood tones, faded rose and dusty salmon fabrics, olive and mustard institutional paint, muted teal-gray shadows, one picture frame hanging crooked, orderly, too quiet, warmly nostalgic, vacant, faintly wrong.
