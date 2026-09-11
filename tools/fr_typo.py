#!/usr/bin/env python3
"""French typography pass for translations/fr: no-break space before ; : ? ! and inside « »,
and the in-line em dash (incise) turned into a spaced en dash, keeping the dialogue
cadratin only at line start. Idempotent. Usage: fr_typo.py <file> [<file> ...]"""
import re, sys, pathlib
NB = " "
def fix(text: str) -> str:
    out = []
    for line in text.split("\n"):
        if line.startswith("<!-- NOTES") or line.startswith("- ") and "→" in line:
            out.append(line); continue
        # in-line em dash → spaced en dash (dialogue dash only at line start)
        head, sep, rest = (line[:2], line[2:], "") if line.startswith("— ") else ("", "", line)
        body = rest if head else line
        body = re.sub(r"\s*—\s*", " – ", body) if "—" in body else body
        line = (head + body) if head else body
        line = re.sub(r"[  ]+([;:?!»])", NB + r"\1", line)
        line = re.sub(r"«[  ]*", "«" + NB, line)
        line = line.replace("–" + NB, "– ")  # never NBSP after a dash
        out.append(line)
    return "\n".join(out)
for p in sys.argv[1:]:
    f = pathlib.Path(p); t = f.read_text(); n = fix(t)
    if n != t: f.write_text(n)
