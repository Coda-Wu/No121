# Phase-1 survey only: reads notes, reports headings/frontmatter/wordcount. Writes nothing to the vault.
import os, re, sys, json

LANG_BLOCK = re.compile(r'<!--\s*lang:[a-zA-Z-]+.*?-->.*?<!--\s*/lang:[a-zA-Z-]+\s*-->', re.S)

def split_fm(text):
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            return text[3:end].strip(), text[end+4:]
    return '', text

def survey(path):
    raw = open(path, encoding='utf-8').read()
    fm, body = split_fm(raw)
    body_nolang = LANG_BLOCK.sub('', body)
    heads = re.findall(r'^(#{1,6})\s+(.*)$', body_nolang, re.M)
    words = len(re.findall(r"[A-Za-z0-9'’\-]+", body_nolang))
    han = len(re.findall(r'[\u4e00-\u9fff]', body_nolang))
    fmd = {}
    for line in fm.splitlines():
        m = re.match(r'^([a-zA-Z_-]+):\s*(.*)$', line)
        if m: fmd[m.group(1)] = m.group(2).strip()
    return {'path': path, 'fm': fmd, 'heads': [(len(h), t) for h, t in heads],
            'words': words, 'han_outside_markers': han,
            'has_lang_block': bool(LANG_BLOCK.search(body))}

for p in sys.argv[1:]:
    if p == '--walk': continue
    print(json.dumps(survey(p), ensure_ascii=False))

# walk mode: `python survey.py --walk` surveys every candidate note
if len(sys.argv) == 2 and sys.argv[1] == '--walk':
    roots = ["10-World","20-Cast","30-Narrative","40-Mechanics","60-Production","70-Script","50-Moodboards"]
    paths = ["00-Inbox/processed/world_bible_v1.md"]
    for r in roots:
        for dp, dn, fn in os.walk(r):
            for f in sorted(fn):
                if f.endswith('.md'):
                    paths.append(os.path.join(dp, f).replace(os.sep, '/'))
    for p in paths:
        print(json.dumps(survey(p), ensure_ascii=False))
