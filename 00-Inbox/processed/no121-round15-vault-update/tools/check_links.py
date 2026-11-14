#!/usr/bin/env python3
"""List wikilinks that resolve to no note. Usage: check_links.py <vault> [file ...]"""
import re, sys
from pathlib import Path
root = Path(sys.argv[1])
# every note name in the vault, by file stem
names = {p.stem for p in root.rglob("*.md") if ".git" not in p.parts}
link = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
files = [root / f for f in sys.argv[2:]] or [p for p in root.rglob("*.md") if ".git" not in p.parts]
bad = {}
for p in files:
    for m in link.finditer(p.read_text(encoding="utf-8")):
        t = m.group(1).strip()
        if t not in names:
            bad.setdefault(t, set()).add(str(p.relative_to(root)))
for t in sorted(bad):
    print(f"{t!r}: {sorted(bad[t])[:4]}")
print(f"{len(bad)} dangling targets")
