---
description: Relay the corkboard canvas by a lens and print the census
argument-hint: [register | day | cast | motif | status] (default register)
---
Lens: $ARGUMENTS (default `register`).

1. Read every note in `35-Corkboard/Notes/`.
2. Rewrite `35-Corkboard/Corkboard.canvas` as **file nodes** grouped by the lens, with text-node group headers, ~280×200 nodes, tidy spacing, no overlaps.
   - `day` lens: an 8-column grid — №121, SPOOL, LIVED, RADAR, REPAPER, ANNA, DEED, REDIVIDER — plus an UNPLACED gutter. Use `day` if placed, else `when` day-guesses.
   - Node colors by register: sick-weird `1`, clinical `2`, dream `3`, lawful-weird `4`, mundane `5`, domestic `6`, unassigned uncolored.
3. `motif` lens only: first extract recurring concrete images (nouns) across all **What happens** text; print a frequency table (motif × count × sticky IDs); update each note's `motifs` list additively; then lay out clusters for motifs with ≥3 members.
4. Print the census: totals by status · register balance against the three-register ownership rule · bible cast with zero stickies · chapters with the fewest stickies (placed or guessed).
5. Commit `mood: board relaid (<lens>)`.

The canvas is a view; the notes are the truth. This command never edits note content (except the additive `motifs` list in step 3).
