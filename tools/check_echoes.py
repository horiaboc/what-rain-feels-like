#!/usr/bin/env python3
"""Echo-integrity check for a translated edition.

The fixed lines and seeded echoes live in translations/<lang>/NOTES.md (sections
A, C, E) as quoted German/French/… strings. A nativeness rewrite is exactly the
kind of edit that silently breaks one. This tool snapshots, per chapter, how
often each quoted phrase occurs in the chapter bodies (NOTES trailers stripped),
and later verifies that no count has gone down.

  tools/check_echoes.py <lang> --snapshot   # write translations/<lang>/ECHOES.snapshot.json
  tools/check_echoes.py <lang> --check      # compare current text against the snapshot

Exit status 1 on any regression. Matching normalises no-break/thin spaces to
plain spaces and drops *italic* markers, so typography passes do not trip it.
"""
import json, pathlib, re, sys

QUOTES = {"de": ("„", "“"), "ro": ("„", "”"), "hu": ("„", "”"), "fr": ("«", "»")}
SECTIONS = re.compile(r"^## ([ACE])\.", re.M)

def norm(s: str) -> str:
    return re.sub(r"[  ]", " ", s).replace("*", "")

def phrases(lang: str) -> list[str]:
    notes = pathlib.Path(f"translations/{lang}/NOTES.md").read_text(encoding="utf-8")
    parts = re.split(r"^## ", notes, flags=re.M)
    keep = [p for p in parts if re.match(r"[ACE]\.", p)]
    text = "\n".join(keep)
    o, c = QUOTES[lang]
    found = re.findall(re.escape(o) + r"([^" + re.escape(o) + re.escape(c) + r"\n]{10,}?)" + re.escape(c), text)
    out = []
    for f in found:
        f = norm(f).strip()
        if "…" in f or "[" in f or "{" in f or f.startswith("- "):
            continue
        if f not in out:
            out.append(f)
    return out

def bodies(lang: str) -> dict[str, str]:
    d = {}
    for p in sorted(pathlib.Path(f"translations/{lang}/chapters").glob("*.md")):
        d[p.name] = norm(p.read_text(encoding="utf-8").split("<!-- NOTES")[0])
    return d

def count(lang: str) -> dict[str, dict[str, int]]:
    ph, bd = phrases(lang), bodies(lang)
    res = {}
    for f in ph:
        per = {ch: t.count(f) for ch, t in bd.items() if t.count(f)}
        if per:
            res[f] = per
    return res, ph

def main():
    lang, mode = sys.argv[1], sys.argv[2]
    snap = pathlib.Path(f"translations/{lang}/ECHOES.snapshot.json")
    res, ph = count(lang)
    if mode == "--snapshot":
        missing = [f for f in ph if f not in res]
        snap.write_text(json.dumps({"phrases": res, "not_found": missing}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{lang}: {len(ph)} quoted phrases in NOTES §A/§C/§E; {len(res)} present in the text ({sum(sum(v.values()) for v in res.values())} sites); {len(missing)} not found (listed in the snapshot).")
        return 0
    old = json.loads(snap.read_text(encoding="utf-8"))["phrases"]
    bad = []
    for f, per in old.items():
        now = res.get(f, {})
        for ch, n in per.items():
            if now.get(ch, 0) < n:
                bad.append((ch, f, n, now.get(ch, 0)))
    for ch, f, n, m in sorted(bad):
        print(f"REGRESSION {ch}: „{f}“ {n} → {m}")
    print(f"{lang}: {len(old)} guarded phrases, {len(bad)} regressions.")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
