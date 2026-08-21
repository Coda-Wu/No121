> [!warning] **SUPERSEDED — historical record only.** Grill Rounds 1–5 (Aug 2026) reopened the fiction beneath the closed systems tree. The ontology, the cast's hidden relationships, the death, the endings and the anomaly law in this document are all out of date. The atomized notes in `10-World/`, `20-Cast/`, `30-Narrative/`, `40-Mechanics/` are the source of truth. Do not cite this file as canon.

# №121 — WORLD BIBLE & DESIGN CANON v1.1
*(№121 is the official working title; the final title is Coda's development-time call, same standing as "Mr. Vacancy." Compiled from Grill Rounds 1–9, August 2026 — the design tree is complete. Items marked 🔧 belong to the post-tree workshops.)*

---

## 0 · LOGLINE & THESIS

A handyman returns to the apartment building where he grew up and is quietly conscripted as its caretaker — measuring corridors that lie, photographing things that were never there, and reporting nightly to a woman who has been missing for years.

**Thesis:** *Leaving isn't wrong; leaving carelessly is.* The world is artificial and someone made it — the question is never whether to escape, but whether you understand what you'd be tearing open.

**Elevator pitch (internal):** An 8-like anomaly hunt fused with a narrative adventure — The Exit 8's loop with Norco's soul, in 2D pixel art, wearing a Lynchian deadpan.

---

## 1 · COMMERCIAL FRAME

- **Engine:** Godot 4.x, frozen at project-start stable (4.7.x as of Aug 2026) until demo ships.
- **Platforms:** Steam (primary), itch.io (demo). Controller/Steam Deck support from day one (cursorless design).
- **Length/price:** 3–4 hours at **$14.99** · 10% launch-week discount · Valve regional matrix · the demo stays live permanently post-launch.
- **Demo:** Cold Open + Day 1, 35–50 minutes, ends on the 3 AM ring. Free on itch + Steam.
- **Endings:** 3 (True / Bad / Neutral), disposition-shaded, knowledge- and diligence-gated.
- **Localization:** EN first → zh-Hans + zh-Hant second → EFIGS + JA third. Architecture (tr()/PO, dynamic CJK fallback fonts, document-viewer layer for diegetic text) built from day one. Candidate CJK bitmap faces: Ark Pixel / Fusion Pixel (🔧 license verification).
- **Budget reserves:** music/SFX commission (composer engaged ~M2–3), capsule/key art commission (~M3–4).

---

## 2 · REGISTERS, TONE & THE TWO-GRAMMAR RULE

Three dread registers, each with exactly one owner:
- **Spatial/architectural wrongness (LEAD)** — owned by the Building itself.
- **Domestic uncanny (support)** — owned by the residents.
- **Clinical-institutional (support)** — owned by the Administration.

**Tone dial:** 15–25% light, Lynch-style deadpan. Humor is situational and never winks. If deadpan fails in playtests, cut toward 0%, never broaden.

**The Two-Grammar Rule (load-bearing):**
- **LAWFUL WEIRD** — the Building's own metabolism. Clean, rule-bound, deterministic, almost polite. Governed by the House Rules. Never repaired, never festers. Photographing it = documentation (clause fragments in hidden layers).
- **SICK WEIRD** — the antagonist's intrusions. Rot-dark, asymmetric, rule-breaking. Its signature is **imperfect mimicry**: it imitates lawful patterns with one flaw (696 wearing a palindrome mask over 666). Diagnosis mechanic: sick anomalies *violate a clause the player knows*.

**Banned:** glitch shaders, datamosh, scanlines, digital-simulation clichés. Wrongness is analog, architectural, bureaucratic.

---

## 3 · ONTOLOGY (top-secret layer)

- The world is an artificial vessel — analog, administered, artisanal. Not a computer simulation. Microverse flavor (the car-trunk universe): the exit opens onto a single **scale-shock vista** screen.
- **Anna is the Maker.** The world is hers / entangled with her. Evidence accumulates (handwriting in blueprint margins, ledger gaps, the deed) but full confirmation is withheld until the endings, and each ending shades it differently.
- **Anchor physics (the truth):** the world runs on Otto's habitation and participation. As he binds to it, leaving = the vessel dying.
- **Decommission (the claim):** the Administration threatens "consolidation" in perfect legalese. The player can never cleanly verify which story is true — the danger of leaving is documented only by the party with an interest in staying (Silo machinery). Evidence planted both ways.
- **The Administration is triage, not tyranny.** Sealed floors and midnight hammering are desperate patching, misdirected as menace. Work crews are only ever heard through walls. Management is never seen.

---

## 4 · THE ANTAGONIST

- **Name:** placeholder **Mr. Vacancy** (final name is Coda's development-time call — 🔧). NOT a palindrome — the inhuman thing doesn't get a loop-name. A failed/near-palindrome is its typographic signature.
- **Nature:** the pollution that causes sick-weird anomalies and spatial rot. A building's natural predator: emptiness. The sealed fifth floor, the "no vacancies" policy, the triage — all siege logistics against it.
- **Residence:** Room 696 — doorsign's middle 6 has a fallen nail, reading 666. The Building shows five floors outside; 696 waits on the sixth that isn't there.
- **Bodied form:** Otto's doppelganger, always wearing the persona Otto is NOT currently wearing (it occupies whichever self you left empty). Bodied appearances strictly rationed (~2 in main game + maze encounters).
- **Camera immunity:** lesser shadows are permanently trapped by photographs; **the Vacancy is only ever photographed because it permits it**, and every print of it differs slightly from what the shutter saw.
- **Endgame role — THE USHER:** it wants the Building empty; an ignorant Breach does its work for it. On the final night the doppelganger *encourages* opening the door. The True ending requires burning the usher first (the final purge), then opening properly.

---

## 5 · CAST (voices, no portraits — bubble dialogue, Darkside Detective style)

| # | Name | Role | Notes |
|---|------|------|-------|
| 1 | **Otto** | Protagonist. Handyman outside; the Building's designated handyman inside ("HANDYMAN (ACTING)"). Dual persona (see §7). | Near-silent in world, voluble on tape. Blue tee, blue trousers, yellow tool belt (Handyman); black suit, white shirt, black tie (Agent). |
| 2 | **Anna** | The addressee. Missing/dead for years. The Maker. | Voice/tape only. Never has a portrait or sprite until endings. Appears ONLY inside endings, staged differently per ending. |
| 3 | **Eve** | The Nurse. The Building's self-purging manifestation. Once a tenant; chose to stay. | Ground-floor infirmary 101 (mundane) + the Ward (dream hub). Her room untouched by permutation. Administers scripted blackouts — every "death" ends with her having put Otto to bed. Dispenses oblique prescriptions (hint tier 3). |
| 4 | **Leon & Noel** | The Superintendent — twins, one role, alternating nights. Names are each other's reverses: individually incomplete, jointly a loop. | Sincere believers in the forms. Which twin you dealt with is a permutation axis. Deadpan continuity gags. |
| 5 | **Bob** | The Insomniac, room 232. Watches the corridor all night; has never once seen it change. | Coffee mug: WORLD'S BEST TENANT. |
| 6 | **Pip** | The Child Cartographer, room 313. A baby who crawls the corridors, speaks in ≤5-word sentences, signs in lollipops — and drafts like a municipal architect. | Sends the master blueprint on night 0 (under the door, mid-tape); refined copies every morning. Rates Otto's photographs brutally out of ten. Hint tier 2. |
| 7 | **Nan** | The Grandmother, room 434, still living in 1998. The domestic register's warm heart; the Stay ending's best argument. | Mint-condition biscuits, best-before 1999. |
| 8 | **The Couple** | Room 212, voices through Otto's wall only. Same argument every evening, wording drifting one word per day. Pauses politely as he passes; resumes mid-word. | One authored knock-beat. |
| — | **Renner** | Predecessor handyman. Voice only: the dream Calling (night 0) and — retcon revealed D7 — every corridor radio, intercom crackle, and static under doors all game. | Merged into the electrical-room junction; still hums. Lived in 202 (Otto's flat is his). Loop-name ✓. |

**Accounting note:** the ≤8 lock was written when portraits existed; with bubble dialogue the binding constraint is the **15,000-word budget**, which governs all speakers including Renner and the Couple. Voice-formant count (~10 gibberish-synth presets) is trivial cost. (Ratified R9.)

**Naming canon (diegetic):** palindrome names mark those who are *of the Building* — Otto, Anna, Eve, Bob, Pip, Nan, Renner; Leon & Noel as a two-body loop. Never stated aloud; discoverable via the lobby mailbox grid and the handyman roster. Room numbers are floor-unit-floor palindromes (202, 212, 232, 313, 434; infirmary 101; street №121). The antagonist's non-palindrome and 696≡666 are the violations that prove the rule.

**Restraint amendment (R9):** the palindrome canon is load-bearing in *character* names, room numbers, and the settled chapter cards — and deliberately restrained everywhere else. New names (title, achievements, items, signage) do not pile on further palindromes; the pattern stays special because it stays scarce.

---

## 6 · STRUCTURE — 7 DAYS + FINAL NIGHT (day = chapter = autosave at wake)

| Card | Day | Owns | Key beats |
|------|-----|------|-----------|
| **№121** | Cold Open | Arrival | Dusk, TV-style title sequence, Leon, cigarette vanish, key to 202, board unpacked (ritual pins + sealed envelope "A."), Pip's blueprint under the door mid-tape, tape #1, sleep, Dream 0 (Renner's Calling). |
| **SPOOL** | D1 | The job | Wake holding camera; work order; the service-lift Shift (floor 2 → floor 2); first lap; the Overrun (ruler); mirror maze (all 3 layers); first captures; darkroom; first pinning; MISSING notice (pocketed); tape #2; Dream 1 (the Ward, Eve, "Visiting hours end at three"); **3:00 AM ring — demo ends.** End-card reads LOOPS. |
| **LIVED** | D2 | The name | Steering epiphany (first deliberate permutation); flashgun prescribed; first played purge; the mirror holds his reflection one beat too long; **Mr. Vacancy named**. Title card rendered in water reflection — DEVIL semi-visible (Coda authors). |
| **RADAR** | D3 | Detection | Bob & Pip deepened; first Administration notice; idle-escalation likely fires. |
| **REPAPER** | D4 | The twins | Leon & Noel formally; renovation notices; the room-swap twist — Otto wakes in the Ward *as* 202, awake (the dream leaking); Administration revealed as triage. Maze variant #2 window. |
| **ANNA** | D5 | The wound | Cold open: the sealed envelope finally opened. The dig; the Building grows her a flat (a room on no plan, furnished from Otto's memories); her undeveloped roll found and developed on Renner's rig; the evening call — the real horror. Reverse Film window opens. |
| **DEED** | D6 | The past | Nan, 1998, the property deed; the exit found through the past; predecessor's ledger last page; the cost-evidence, both readings. Maze variant #3 window. Reverse Film grace window closes at the D6 dream. |
| **ROTOR** | D7 | Renner | The descent; the junction reveal (wires and warmth, no gore — he still hums); the intercom retcon lands; **the fuse-swap room puzzle (critical-path) → the Master Fuse**; the branch point: Stay can trigger here. |
| **REDIVIDER** | Final Night | The door | Disposition receipts in three conversations (Eve, the twins, the last tape); the usher; the triptych. |

**Day-advance rules:** only the day's critical beat advances the day. Idle sleeps escalate — each fruitless night adds exactly one new detail (the diegetic hint system, unified with dream sharpening). Scripted blackouts only (3–5 game-wide, film-cut style, Eve puts you to bed); zero timers anywhere; in-world clocks lie.

---

## 7 · PERSONA LAW (the Shift)

- **Agent Otto** (suit): hub self. Development, corkboard, tapes, night-roam (floor 2, stairwell, lobby). The Building *performs normalcy* for the Agent — same tilemap, composed dressing.
- **Handyman Otto** (uniform): floor self. Work orders, instruments, purging, pockets. Sees the truth dressing.
- **Trigger:** the elevator, only ever the elevator. The service-lift ride is a threshold ritual (works floor 2 → floor 2). Never shown as a costume change; never remarked on. Two gibberish-synth formants — the player hears the shift.
- **Memory model — THE HAZE:** knowledge persists; episodic detail blurs at the crossing. The artifacts are the reliable record: photographs are the Handyman's memory delivered to the Agent in the developing tray; work orders and the corkboard are the Agent's instructions passed back down. The two selves collaborate by leaving each other evidence. (Retro-charge: with hazy recall canon, Otto genuinely cannot rule himself out as the taker of the un-taken frame.)
- **Crossings:** satchel and camera cross; suit⇄uniform automatic; no exchange room exists.
- **Stairwell:** never shifts; blocked above floor 2 ("WET PAINT") until ~D4, after which persona-routing becomes an earned advanced verb — choosing *who arrives*.
- **Enforcement fiction:** no invisible walls. Doors and residents that only open for a suit; wrongness that only manifests for a uniform. 202's lock doesn't answer to the uniform (closes the skip-the-ritual hole).
- **Doppelganger rule:** the Vacancy always wears the persona you are NOT.

---

## 8 · THE DAY LOOP (the Hunt)

**Five beats:** ① work order (2–3 mundane jobs; the route is where the Building misbehaves) → ② the lap: ring-corridor observation → ③ diagnosis (lawful obeys a clause; sick violates one you know) → ④ resolution verb: **EXPLOIT** (use a clause to steer/traverse) / **PURGE** (light or photo) / **CAPTURE** (evidence) / **ESCAPE** (pocket) → ⑤ night phase.

**Floor topology:** each floor is a rectangular ring — four side-view faces, perspective-rotating corners, doors set into faces; lappable endlessly. Lap-anomaly menu: five-corner laps, a face occurring twice, direction-dependence (a lawful clause: "the third floor is to be walked against the clock"). Scope: corridors + palindrome rooms only; vacant flats are doors, not spaces; knocking is authored-only. Every enterable room contains a case beat, side anomaly, resident scene, or document — **no filler rooms, ever.**

**Reference channels (anti-pixel-hunt):** yesterday's prints (the album is haze-proof memory) · the House Rules · Otto's childhood memory (terse examine lines) · plain domestic sense.

**Viewfinder law:** faint glow toward the MAIN narrative anomaly only. Side anomalies: eyes and deduction only.

**Snap tiers:** true anomaly → the camera *bites* (heavier thunk; the thing settles/flinches; instant registration). False suspicion → ordinary click, film spent (knowledge too). **Latents** (narrative horrors) never bite — tray-only reveals. Fidelity ladder: eye < lens < print.

**Meters:** CUT as mechanic. Survives only as deadpan flavor + ≤3 authored visual beats (a wheel turning slowly backwards; dials at rest while the hum is loudest; warm glass).

**Certification (ruler framing):** some work orders demand certified measurements — MEASURED / SCHEDULED / DISCREPANCY / SIGNED, O. Most are boring on purpose.

**Day math:** orders 2–3 min + lap/hunt 8–12 + resolution 5–10 + night 5–8 + dream 1–2 ≈ 21–35 min × 8 ≈ 3–4 h.

---

## 9 · CAMERA, FILM & LIGHT (the hero object)

- **One rig:** Renner's camera (initials scratched in the plate), issued via dream with a requisition slip — "RETURN UPON TERMINATION OF TENANCY." Detachable flashgun (prescribed by Eve, D2), screw-on filters, film. Tool-belt torch = mundane demo-tier light.
- **Controls:** RMB raise viewfinder → LMB shoot (1 film, auto-flash). LMB-hold alone = directional light, free. Deck mapping: LT view / RT shoot / RT-hold light.
- **Capacitor:** shining drains it (coil-glow + rising whine); releasing recharges; emptied = seconds of dark while it whines back up. Purge setpieces are rhythm management. The photo-flash is exempt — film IS its charge.
- **Purge rules:** light disperses shadows temporarily (they return next day if the floor is revisited); a photograph traps lesser shadows permanently. The Vacancy is immune (see §4).
- **Film economy:** wake with ≥6 (dream restock, spool on the nightstand); bank to 10 max. Careful shooters earn hidden print layers (deepest layer requires good agitation) and one-night-only side anomalies. Empty camera on the main anomaly → board logs a pencil sketch ("the Agent draws what the Handyman half-remembers") — progression never blocks; no hidden layer. Side anomalies met filmless → rumor pins, re-shootable if they persist. Work orders declare the official job count; side-anomaly count revealed only at night ("IRREGULARITIES LOGGED: 2 OF 4").
- **Filters:** UV (D3–4) — fluorescent residue of the Settling-pollution + hidden marginalia on read documents. NIR (D6) — the original architecture under the wallpaper; the true floor plan (a True-ending gate). Each filter also purges a different shadow variant. Filters = cheap revisit content.
- **Develop-to-heal:** photograph a passive sick distortion → develop = the report is FILED → repaired overnight → muffled construction next day. Mid-game realization: the hammering has been following your own reports all along. Undeveloped film reports nothing.

---

## 10 · NIGHT PHASE & THE DREAM

**Order (fixed):** develop → pin → tape to Anna → set the alarm (permutation input) → sleep.

- **Darkroom:** 202's bathroom (Renner's own rig; basement station survives as a D7 discovery). Permutation-anchored. Minigames: hold-release chemical pour + memorized-rhythm agitation; soft-fail only (murkier print, instant retry); the image *arrives* under the liquid in red light.
- **Corkboard:** the Agent's old case board, arrived wrapped in his luggage, Anna's thread in his own years-old handwriting — Day 0 shows ritual pins + one sealed aged envelope marked "A." (opened cold-open D5). Threads only (~30 nodes); pins auto-place; the player draws threads. The completed Anna-thread = the Reverse Film gate = the photo-evidence gate (one condition, two surfaces).
- **Blueprint (Pip):** the map surface. Fog-of-war zoomed out; prop-level detail zoomed in. Morning updates mark repaired areas + "visited, not captured" anomalies. Ruler measurements annotate it. ≥1 blueprint-comparison anomaly per floor. The Administration's Schedule (official, wrong) vs Pip's blueprint (crayon, true) is the institutional/domestic thesis in paper form.
- **The Ward (dream hub):** Eve's hospital bed, Red-Room grammar. Debut = Dream 1 (in demo). The day's pinned prints appear as X-ray films on her lightbox. Dream-gifts are in-hand at waking. Idle-sleep escalation = the dream sharpening. The Ward absorbs the hospital-room satellite; waking infirmary 101 stays mundane. D4's REPAPER twist = the dream leaking (waking in the Ward-as-202).

---

## 11 · PERMUTATION & PERSISTENCE

- **Axes (deterministic, always):** satchel category carried to bed (hers / institutional / tools / nothing) · last door used · alarm-clock state · last conversation (advanced; includes which twin) . Authored beats override cleanly.
- **House Rules:** 9–11 physical, findable clauses from the ancient tenancy agreement — legalese as literature. Finding = being handed a tool; instruments verify; exploiting = steering. Demo teaches Clause #1 fully, shows #2 (Pip's crayon map).
- **Persistence:** satchel 3–5 slots + permanent "the Building remembers" flags. Photos/album live outside the satchel.
- **Purge-pinning:** a purged room's geometry stops permuting.
- **Festering:** missed sick anomalies ripen on revisit (darker, louder, easier); an authored subset hatch into active shadows on later days (one photograph closes wound + creature); hard cap 2 hatched entities alive at once; ending-texture only, never a gate.
- **Hint ladder:** dream escalation → Pip's maps → Eve's prescriptions.

---

## 12 · POCKETS & SET-PIECES (≤6 bespoke; one gimmick each; teaching pocket exempt; mirrored-tilemap default construction)

1. **Teaching pocket (demo, D1):** the corridor that shouldn't fit behind 242's far door — scripted pacing-count overrun (gibberish counting, air change, no minigame), nest, torch purge, Clause #1; exit three steps away. Pacing-count is scripted-only, everywhere, forever.
2. **Mirror maze (demo, D1 — all 3 layers, 4–6 min total):** 4×4 conceptual grid, perimeter side-scroll, opaque walls/glass shaders, spawn B1, Vacancy at C2 facing east always. Mirrored lateral movement; axis remaps per viewing face; wall-blocks desync with feedback — **the parking brake is the puzzle** (pin him against walls to reposition). Win: clear frontal photograph per layer. He wears the suit (the persona left behind). West-face shot develops as the back of your own head (once, authored). **The Concession (skip valve, ratified R9):** past ~2:30 on one layer or 5:00 maze total, the Vacancy steps into a clear line of sight and permits the shot — never announced, no prompt, the game never admits the valve exists; earned captures develop *neutral*, conceded captures develop *smiling*. **The contact sheet:** the three capture prints escalate within one darkroom session — L1 neutral, L2 the eyes have moved since the shutter, L3 closer than the glass allows. Dead work-order bulb hangs at center; changed after capture; order COMPLETE. 🔧 solver-validation of all layers (my job).
3. **Maze family (full game, ratified R9):** 2 further bespoke mazes (D4/D6 windows), a new twist each — the family occupies 3 of the 6 pocket slots, amending the one-gimmick rule for this family only. Twist candidates (he parks *you*; a two-Vacancy decoy; a true mirror showing the other persona) go to the workshop.
4. **Penrose stair (trimmed):** 2–3 mixed-persona duplicates, synced movement, persona-matched switches, single static screen.
5. **Flash-survival room:** the purge system under pressure; blackout = Eve puts you to bed.
6. 🔧 remaining slots assigned in the placement pass.

---

## 13 · THE RULER

Self-anchoring reel: hook fires left, bites the far wall itself; live line; fat pixel readout. Thesis: **a nerve ending into offscreen space.**
- **Scare 1 — the Overrun (demo):** certifying corridor 2, the tape passes the Schedule's number and keeps paying out.
- **Scare 2 — the Countdown (mid-game):** the number starts decreasing, accelerating — a reading of an approach — slack at ~3 m.
- **Scare 3 — the Taut Line (late):** the extended tape lifts, pulled tight against empty air; the hook is clipped to nothing.
- Ambient ±0.1 m shivers, rare. All measurements annotate the blueprint. **Canon: a mismatch that doesn't open a case or a clause doesn't ship.**

---

## 14 · ENDINGS (three camera verbs)

| Ending | Verb | Gates | Shape |
|---|---|---|---|
| **TRUE — informed Breach ("homecoming")** | *Un-take* a photograph | Reverse Film (≥5 of 7 MISSING notices → Eve's grant after ANNA thread completes; grace window to D6 dream) + Master Fuse (critical-path) + ≥8 clauses + NIR true plan + burning the usher in the final purge (unloseable: unprepared = thrown back, never dead) | Saves everyone, purges the antagonist, the vessel reborn open-skied, Anna at the tram stop. |
| **NEUTRAL — Stay (the socket)** | *Take* the last photograph | Master Fuse + going to Renner + choosing the socket | Album mounted, fuse seated, one final flash — his own last exposure. Safe "for now." Never meets her. Must be written warm and whole or the triptych collapses. |
| **BAD — ignorant Breach** | *No* photograph (tear) | None — choosable in ignorance, always | The door torn; the scale-shock vista; the Building exhales out into nothing behind him. Anna conspicuously absent from the crowd. |

Disposition tracker (satchel habits, door habits, treatment of residents) never selects an ending — it shades the final night's three conversations and the epilogue. All three endings reachable from Final Night's start. Anna appears only inside endings.

---

## 15 · ANECDOTE BANK (2–3 microbeats per chapter; charm quota)

Locked: the cigarette gag escalating across seven days (pack empties, nothing ever smoked) · dusting his own doorknob mid-tape ("One set of prints. Mine. …Noting for the record that this proves nothing.") · noir-corrections on tape · the crooked frame in 202 (optional nightly straightening; full-streak achievement) · Leon/Noel tie continuity · Bob's mug · Pip's brutal photo ratings ("The ghost one. Four. Blurry.") · Nan's 1999 biscuits · the couple's polite pause · the vending machine dispensing a spirit level ("It knows what you need."). Funny minigames welcome within word/scope locks. Demo carries: cigarette, doorknob, noir-correction, lift line, the frame.

---

## 16 · ART SPEC

640×360 base, integer scaling · tall sprites ~90–110 px (6–7 heads; faces capable of stillness) · nearest-neighbor with free transforms — deliberate mixels policy, applied consistently · master palette 48–64 colors + per-scene LUT grading via shader (the scope weapon: re-grade + prop swaps = a permutation variant or an era shift) · two dressings per persona-visible screen (performance vs truth) come from the existing ≤2-variant budget · bubble dialogue, no portraits · era-shifts and the Ward ship as LUT re-grades of existing screens.

**Screen ledger:** ≤30 base scenes total (elevator included). A ring floor = 1 base scene rendered as 4 faces from shared tilesets (faces are variant-cheap, not separate scenes). Demo uses ~10: street/tram, lobby, stairwell, elevator, corridor-2 ring, 202 (+bathroom), 242, teaching pocket, maze, the Ward.

---

## 17 · AUDIO SPEC

Two-layer hybrid: jazz-adjacent motifs (normal/domestic) + drone/musique-concrète (wrongness); diegetic crossfade sources (tram bell, radiators, elevator hum, radio — the radio is Renner). 8–10 loops. No VO: gibberish synth per character (pitch/formant presets; two formants for Otto's personas; "her" tape voice possible without casting). Signature sounds: the capacitor whine · the camera bite · the counting voice degrading · construction behind walls that follows your reports. Composer engaged M2–3; demo ships with final sonic identity (2–3 tracks + core SFX pass).

---

## 18 · SCOPE LOCKS & LEDGER

- ≤30 base scenes · ~2 dressing variants avg · ≤15,000 words · 9–11 clauses · ≤6 bespoke pockets · 8–10 music loops · 3–5 scripted blackouts · 3 ruler scares · ≤3 meter beats · festering cap 2 · 7 MISSING notices · ~30 corkboard nodes.
- **Scope-tax rule:** any mid-project addition must name its deletion out loud first.
- **Systems freeze (in effect):** new systems file to the post-launch parking lot. New pitches route to workshop agendas, not the tree.
- Paid ledger to date: portrait cut funded the purge verb; meter cut + chart-absorption funded festering; pacing-count system → one scripted moment; persona pitch ≈ +100 h absorbed against buffer.

---

## 19 · OPEN ITEMS

*(Round 9 complete — the design tree is closed. Everything below is workshop business, not tree business.)*

**🔧 Workshops:** House Rules clause-by-clause pass · puzzle validation incl. maze solver (Claude brings the solver) · microbeat & pocket placement pass · maze-family twist designs · critical-items slate (Coda's R8 note) · antagonist final name · **final title** (№121 stands until Coda replaces it) · achievements full list — naming unconstrained; locked concepts: **WOW** (perfect print), the **back-of-the-head** secret, the frame-streak accomplishment (name open), a receipt for meeting the Concession · **Sator-square lintel: offered, PARKED** — optional lore, adoptable only if it stays one weathered, never-explained carving under the restraint amendment · CJK font license verification · protagonist surname (if any) · Steam page copy · trailer production (post-vertical-slice).

---

## 20 · PRODUCTION, POSITIONING & LAUNCH CANON (ratified R9)

- **Positioning:** narrative adventure first, anomaly-hunt hook second, always in that order. Short-description formula: fantasy → verb → stakes.
- **Tags (first five):** Psychological Horror · Story Rich · Pixel Graphics · Adventure · Mystery. Behind: Surreal, Detective, Atmospheric, Puzzle, Multiple Endings, 2D, Singleplayer, Dark, Noir, Exploration. Excluded on purpose: Walking Simulator, Hidden Object.
- **Schedule (from Aug 2026):** M0–M2 systems vertical slice, composer engaged (Oct) · M3–M4 demo scenes; **capsule/key-art commission Nov (hard date — the page needs it)**; **Steam page live mid-Dec 2026** · M5–M6 demo complete → **itch demo mid-Feb 2027** (M6 milestone kept; the feedback build) · M7–M9 feedback fold-in → **Steam demo early Apr 2027** → June-fest registration late Apr · **Steam Next Fest June 14–21, 2027 — our one and only fest** · M10–M12 D5–Final Night; content-complete end Aug 2027 · **launch late Sep 2027**; first discount at the October horror fest.
- **Trailer & capsule:** the R9 brief stands as the working draft (facade capsule, №121 plate legible at thumbnail; 60–75s trailer cut for sound, ending on the 3 AM ring and the title card). Production waits for the vertical slice and core art assets; capsule art is the sole exception, commissioned Nov for the December page.
- **Engine:** Godot 4.7.1-stable, frozen through demo ship.
- **Hours audit:** ~1,150 available through launch vs. a ~1,090–1,290 budget — inside the band only while the systems freeze holds.
