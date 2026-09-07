# -*- coding: utf-8 -*-
"""Derive the Godot locale tables in 60-Production/locale/ from 70-Script/.

Contract lives in 60-Production/locale/README.md (the engine-side brief).
Two files per card:

    <card>.csv             keys,en,zh_Hans        -> Godot csv_translation
    <card>.beats.json      ordered {key, speaker} -> playback order and voice

A scene enters the pipeline only when its script file carries a `locale:`
frontmatter key, e.g. `locale: spool.dream_1`. That key - not the filename -
is the stable anchor, so renaming a scene file cannot renumber anything.

THE LAW THIS FILE ENFORCES: keys are never renumbered. Existing keys are
matched to the script by text alignment; an edited line keeps its key, a new
line takes a number from the gap. If no gap is wide enough the run FAILS
rather than shifting keys, because renumbering invalidates every translation
already done against them.

Run from the vault root:  python tools/build_locale.py [--dry-run]
Writes 60-Production/locale/*.csv, *.beats.json and _Index.md
"""
import csv, difflib, io, json, os, re, sys, collections

ROOT = "70-Script"
OUT = os.path.join("60-Production", "locale")
CAST = os.path.join(OUT, "cast.csv")
STEP = 10
WRENCH = u"\U0001f527"

# Speakers as written in the script -> cast id. Anything else is a hard error:
# a typo must not silently become a new voice.
ALIASES = {"mr. vacancy": "vacancy", "mr vacancy": "vacancy"}


def die(msg):
    sys.stderr.write("build_locale: %s\n" % msg)
    sys.exit(1)


def read(p):
    return io.open(p, encoding="utf-8").read()


def cast_ids():
    ids = []
    for row in csv.DictReader(io.StringIO(read(CAST))):
        k = (row.get("keys") or "").strip()
        if k.startswith("cast."):
            ids.append(k[len("cast."):])
    if not ids:
        die("no cast ids in %s" % CAST)
    return ids


# ---------------------------------------------------------------- extraction

def strip_comments(s):
    return re.sub(r"<!--.*?-->", " ", s, flags=re.S)


def clean(t, warn, where, ids):
    """A spoken line as it should reach the engine."""
    t = t.strip()

    # [[Leon]] and [[Leon|LiAng]] are explicit author markers -> name tokens.
    # Bare names are NOT auto-detected: Chinese has no word boundaries and
    # the word for grandmother is also a cast name.
    def tok(m):
        name = m.group(1).split("|")[0].strip()
        if name.lower() in ids:
            return "{%s}" % name.lower()
        warn("%s: [[%s]] in dialogue is not a cast id - left verbatim" % (where, name))
        return name

    t = re.sub(r"\[\[([^\]]+)\]\]", tok, t)
    t = t.replace(WRENCH, " ").strip()                 # wrench = unwritten
    if t:
        for i in ids:
            if re.search(r"(?<![{\w])%s(?![}\w])" % re.escape(i), t, re.I):
                warn("%s: bare name %r - write {%s} so it carries the colour"
                     % (where, i, i))
    return re.sub(r"\s{2,}", " ", t)


def spoken(body, warn, where, ids):
    out = []
    for m in re.finditer(r"^\*\*([^*:]+):\*\*(.*)$", body, re.M):
        raw = m.group(1).strip().lower()
        sid = ALIASES.get(raw, raw)
        if sid not in ids:
            die("%s: speaker %r is not a cast id (%s)"
                % (where, m.group(1).strip(), ", ".join(ids)))
        out.append((clean(m.group(2), warn, where, ids), sid))
    return out


def paper(body):
    """Diegetic paper: one key per blockquote paragraph. Prose around it is
    brief, not text - it stays out until Coda quotes it."""
    out, buf = [], []
    for line in body.splitlines():
        if line.lstrip().startswith(">"):
            buf.append(line.lstrip()[1:].strip())
        elif buf:
            out.append(" ".join(x for x in buf if x).strip())
            buf = []
    if buf:
        out.append(" ".join(x for x in buf if x).strip())
    return [(t, None) for t in out if t]


def scan(warn, ids):
    """-> ({card: {scene: [(en, speaker|None)]}}, [files with no locale key])."""
    cards, skipped = collections.OrderedDict(), []
    for dp, _, fns in os.walk(ROOT):
        for fn in sorted(fns):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            p = os.path.join(dp, fn)
            s = read(p)
            fm = re.match(r"^---\n(.*?)\n---\n", s, re.S)
            meta, body = (fm.group(1), s[fm.end():]) if fm else ("", s)
            label = os.path.basename(dp) + " / " + fn[:-3]
            m = re.search(r"^locale:\s*([a-z0-9_]+)\.([a-z0-9_]+)\s*$", meta, re.M)
            if not m:
                skipped.append(label)
                continue
            card, scene = m.group(1), m.group(2)
            kind = (re.search(r"^type:\s*(\S+)", meta, re.M) or [None, "script"])[1]
            b = strip_comments(body)
            lines = paper(b) if kind == "document" else spoken(b, warn, label, ids)
            bucket = cards.setdefault(card, collections.OrderedDict())
            if scene in bucket:
                die("%s: locale key %s.%s is already used by another file"
                    % (label, card, scene))
            bucket[scene] = lines
    return cards, skipped


# ------------------------------------------------------------------ numbering

def existing(card):
    """-> (fieldnames, {key: row}) from the card's current CSV, if any."""
    p = os.path.join(OUT, card + ".csv")
    if not os.path.exists(p):
        return ["keys", "en", "zh_Hans"], {}
    r = csv.DictReader(io.StringIO(read(p)))
    rows = collections.OrderedDict()
    for row in r:
        k = (row.get("keys") or "").strip()
        if k:
            rows[k] = row
    return list(r.fieldnames or ["keys", "en", "zh_Hans"]), rows


def gap(low, high, n, where):
    """n numbers strictly between low and high. Never renumbers to make room."""
    if high is None:
        return [low + STEP * (i + 1) for i in range(n)]
    if high - low - 1 < n:
        die("%s: no room for %d new line(s) between %03d and %03d. Renumbering is "
            "forbidden - split the insert across a wider gap." % (where, n, low, high))
    step = (high - low) // (n + 1)
    return [low + step * (i + 1) for i in range(n)]


MATCH = 0.6         # below this, two lines are different lines, not an edit


def score(a, b):
    """How strongly an existing line `a` claims the new line `b`. None = no claim.

    Positional pairing is wrong here: a line inserted above an edited one would
    take the edited line's key and inherit its translation. Similarity is what
    tells an edit apart from an insert."""
    if a == b:
        return 1.0
    if a == "" or b == "":
        return 0.55         # a placeholder key is a reservation - reuse it
    r = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
    return r if r >= MATCH else None


def align(old_txt, new_txt):
    """Order-preserving best-total-similarity pairing. -> {new index: old index}."""
    n, m = len(old_txt), len(new_txt)
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            best = max(dp[i - 1][j], dp[i][j - 1])
            s = score(old_txt[i - 1], new_txt[j - 1])
            if s is not None:
                best = max(best, dp[i - 1][j - 1] + s)
            dp[i][j] = best
    pairs, i, j = {}, n, m
    while i and j:
        s = score(old_txt[i - 1], new_txt[j - 1])
        if s is not None and abs(dp[i][j] - (dp[i - 1][j - 1] + s)) < 1e-9:
            pairs[j - 1] = i - 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return pairs


def assign(card, scene, lines, old_rows, warn):
    """Align new script lines against existing keys. -> [(key, en, speaker)]."""
    pre = "%s.%s." % (card, scene)
    old = sorted(((int(k[len(pre):]), old_rows[k]) for k in old_rows
                  if k.startswith(pre) and k[len(pre):].isdigit()), key=lambda x: x[0])
    old_txt = [r.get("en") or "" for _, r in old]
    new_txt = [t for t, _ in lines]

    pairs = align(old_txt, new_txt)
    for i in range(len(old_txt)):
        if i not in pairs.values():
            warn("%s%03d dropped - its line is gone from the script; any translation "
                 "against that key is now orphaned" % (pre, old[i][0]))

    # Fill inserts from the gaps between their surrounding anchors.
    nums = [None] * len(new_txt)
    for ni, oi in pairs.items():
        nums[ni] = old[oi][0]
    i = 0
    while i < len(nums):
        if nums[i] is not None:
            i += 1
            continue
        j = i
        while j < len(nums) and nums[j] is None:
            j += 1
        low = nums[i - 1] if i > 0 else 0
        high = nums[j] if j < len(nums) else None
        for k, n in enumerate(gap(low, high, j - i, pre.rstrip("."))):
            nums[i + k] = n
        i = j
    return [("%s%03d" % (pre, nums[i]), lines[i][0], lines[i][1])
            for i in range(len(lines))]


# -------------------------------------------------------------------- writing

def write(p, text, dry):
    if dry:
        print("--- %s\n%s" % (p, text))
        return
    io.open(p, "w", encoding="utf-8", newline="\n").write(text)


def main():
    dry = "--dry-run" in sys.argv
    warnings = []
    warn = warnings.append
    ids = cast_ids()
    cards, skipped = scan(warn, ids)
    report = []

    for card, scenes in cards.items():
        fields, old_rows = existing(card)
        rows, beats = [], collections.OrderedDict()
        for scene, lines in scenes.items():
            got = assign(card, scene, lines, old_rows, warn)
            for key, en, spk in got:
                old = old_rows.get(key, {})
                if (old.get("en") or "").strip() and not en:
                    warn("%s: en emptied - the script line is a placeholder again" % key)
                row = dict((f, old.get(f) or "") for f in fields)
                row["keys"], row["en"] = key, en
                rows.append(row)
            beats[scene] = [({"key": k} if s is None else {"key": k, "speaker": s})
                            for k, _, s in got]
            report.append((card, scene, got))

        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow(r)
        write(os.path.join(OUT, card + ".csv"), buf.getvalue(), dry)
        write(os.path.join(OUT, card + ".beats.json"),
              json.dumps({"card": card, "scenes": beats},
                         ensure_ascii=False, indent=2) + "\n", dry)

    # ------------------------------------------------------------- the index
    total = sum(len(g) for _, _, g in report)
    empty = sum(1 for _, _, g in report for _, en, _ in g if not en)
    L = ["---", "type: report", "status: generated", "---",
         "# locale - coverage", "",
         "> [!warning] Generated by `tools/build_locale.py`. **Never hand-edit** any file",
         "> in this folder except `cast.csv`. Fixes go into `70-Script/`; rerun to refresh.",
         "",
         "Contract: [[README]] (engine-side brief) - [[WS-3-text-spine]] (spec).", "",
         "**%d keys** across %d card file(s); **%d** still awaiting text."
         % (total, len(cards), empty), "",
         "| Card | Scene | Keys | Written | Awaiting |", "|---|---|---|---|---|"]
    for card, scene, got in report:
        n = len(got)
        e = sum(1 for _, en, _ in got if not en)
        span = ("%s-%s" % (got[0][0].rsplit(".", 1)[1], got[-1][0].rsplit(".", 1)[1])
                if got else "-")
        L.append("| %s | %s | %s | %d | %d |" % (card, scene, span, n - e, e))
    L += ["", "## Not exported", "",
          "No `locale:` frontmatter key, so no keys are reserved. Add one",
          "(`locale: card.scene`) once the file has had its protocol pass.", ""]
    for s in skipped:
        L.append("- `%s`" % s)
    L += ["", "## Warnings", ""]
    L += (["- %s" % w for w in warnings] or ["None."])
    L += ["", "## Open for the engine side", "",
          "- **Documents carry no speaker.** `doc.beats.json` entries are `{key}` only, "
          "since diegetic paper is read, not heard. The document viewer is unbuilt - "
          "confirm the shape before it is.",
          "- **The beats format is linear.** The cafeteria scenes drafted for LIVED and "
          "RADAR contain player choice menus, which `{key, speaker}` in running order "
          "cannot express. A branch shape is needed before those cards can be exported.",
          "- **`.import` files belong to Godot.** Only `cast.csv.import` exists because "
          "Godot wrote it; the engine generates the rest on first import.", ""]
    write(os.path.join(OUT, "_Index.md"), "\n".join(L) + "\n", dry)

    print("build_locale: %d keys, %d cards, %d awaiting text, %d warning(s)"
          % (total, len(cards), empty, len(warnings)))
    for w in warnings:
        print("  ! %s" % w)


if __name__ == "__main__":
    main()
