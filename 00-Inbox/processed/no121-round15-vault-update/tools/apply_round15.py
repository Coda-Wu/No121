#!/usr/bin/env python3
"""Apply the Round 15 vault update.

Usage:
    python3 tools/apply_round15.py --vault /path/to/vault            # dry run: report only
    python3 tools/apply_round15.py --vault /path/to/vault --apply    # write the files

The pack was built against vault commit 0156b4a ("change tram to bus").
For every file it would replace, the script compares the vault's current
content with the content the pack was built from. A file that has changed
since then is reported as a CONFLICT and is never overwritten.
"""
import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent      # the unzipped pack folder
SRC = PACK / "vault"                               # the new and replacement notes


def sha(path: Path) -> str:
    """SHA-256 of a file's bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault", required=True, help="path to the root of the Obsidian vault")
    ap.add_argument("--apply", action="store_true", help="write files; without it the run is a dry run")
    args = ap.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not (vault / "CLAUDE.md").exists() or not (vault / "30-Narrative").is_dir():
        print(f"ERROR: {vault} does not look like the №121 vault (no CLAUDE.md or 30-Narrative/).")
        return 2

    manifest = json.loads((PACK / "manifest.json").read_text(encoding="utf-8"))
    ok, conflicts, already = [], [], []

    for entry in manifest["files"]:
        rel = entry["path"]
        src, dst = SRC / rel, vault / rel
        if sha(src) != entry["sha256_after"]:
            print(f"ERROR: the pack itself is damaged: {rel}")
            return 2

        if entry["action"] == "new":
            if dst.exists():
                # a note of this name already exists in the vault
                (already if sha(dst) == entry["sha256_after"] else conflicts).append(rel)
            else:
                ok.append(rel)
        else:  # "replace"
            if not dst.exists():
                conflicts.append(rel)          # the note was moved, renamed or deleted
            elif sha(dst) == entry["sha256_after"]:
                already.append(rel)            # this file was applied on an earlier run
            elif sha(dst) == entry["sha256_before"]:
                ok.append(rel)                 # untouched since the pack was built
            else:
                conflicts.append(rel)          # edited since commit 0156b4a

    print(f"vault: {vault}")
    print(f"ready to write : {len(ok)}")
    print(f"already applied: {len(already)}")
    print(f"conflicts      : {len(conflicts)}")
    for rel in conflicts:
        print(f"  CONFLICT  {rel}")

    if not args.apply:
        print("\nDry run. Nothing was written. Add --apply to write the files that are ready.")
        return 1 if conflicts else 0

    for rel in ok:
        dst = vault / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SRC / rel, dst)
    print(f"\nWrote {len(ok)} files.")
    if conflicts:
        print("Conflicted files were NOT written. Merge each one by hand:")
        print("  the new text is in  vault/<path>  inside this pack,")
        print("  and the exact change is in  round15.patch.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
