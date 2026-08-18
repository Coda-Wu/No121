#!/usr/bin/env bash
# EXPERIMENTAL — optional file-watcher for the bilingual sync. OFF by default; the
# recommended rhythm is running /translate at session end. Know before enabling:
#   * Obsidian autosaves continuously — there is no "save" event. The debounce
#     below waits for 90s of quiet so the sync never fires mid-sentence.
#   * Each trigger is a headless Claude Code run (costs usage).
#   * Requires watchexec (brew install watchexec / cargo install watchexec-cli).
# Run from the vault root:  ./tools/watch-translate.sh     Stop: Ctrl-C.

set -euo pipefail
cd "$(dirname "$0")/.."

exec watchexec \
  --watch 35-Corkboard/Notes \
  --exts md \
  --debounce 90s \
  --postpone \
  --on-busy-update=do-nothing \
  -- claude -p "Run the language sync exactly as specified in .claude/commands/translate.md, scope 35-Corkboard/Notes only." \
       --permission-mode acceptEdits \
       --allowedTools "Read,Edit,Write,Bash(git add:*),Bash(git commit:*)"
