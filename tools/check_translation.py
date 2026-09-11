#!/usr/bin/env python3
"""Structural check of a translated edition against the English source.

    .venv/bin/python tools/check_translation.py de

Nothing here judges the prose. It catches what a build would silently accept
and a reader would notice: a missing chapter, a scene break dropped or added,
a heading that does not follow the edition's label rule, English typography
left in the text, a translator-notes trailer missing (or not last), a name
that changed. Word-count ratios are printed for orientation only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "chapters"
NAMES = ["Jonas", "Iris", "Claudia", "Mia", "Lukas", "Conrad", "Vael", "Mara", "Seyn",
         "Kees", "Ingrid", "Steffen", "Würfel", "Diogenes", "Merkon", "Vantage",
         "Arcturus", "Weichselstraße", "Neukölln", "Hermannstraße", "Bloemgracht",
         "Oosterpark", "Heerlen", "Aleph"]

# Per-language expectations. Extend when an edition is added.
RULES = {
    "de": {
        "label_re": re.compile(r"^# Kapitel [A-ZÄÖÜ][a-zäöüß]+(?::\s+.+)?$"),
        "bad_typography": [("—", "English em dash (use spaced en dash –)"),
                           ("\"", "straight double quote (use „…“)"),
                           (" - ", "hyphen used as dash")],
        "ratio": (0.85, 1.25),
        # Translator fingerprints a native writer would vary. Counted
        # book-wide; the number is the report, the target is "few".
        "tics": ["die Sorte", "Beschaffenheit", "auf die Art", "nicht direkt",
                 ", was ", "sagte ich", "sagte sie"],
    },
    "ro": {
        "label_re": re.compile(r"^# Capitolul [a-zăâîșț ]+(?::\s+.+)?$"),
        "bad_typography": [("\"", "straight double quote (use „…”)"),
                           ("ş", "cedilla ș (use comma-below)"), ("ţ", "cedilla ț (use comma-below)")],
        "ratio": (0.9, 1.3),
        "tics": ["de fapt", "genul de", "un fel de", "felul în care", "care ", "am spus", "a spus"],
    },
    "hu": {
        "label_re": re.compile(r"^# [A-ZÁÉÍÓÖŐÚÜŰ][a-záéíóöőúüű]+ fejezet(: .+)?$"),
        "bad_typography": [("\"", "straight double quote (use „…”)"),
                           ("\u201c", "English opening quote “ (use „)")],
        "ratio": (0.70, 1.15),
        "tics": ["az a fajta", "olyan, amely", "ami azt illeti", "valahogy", "egyszerűen", "mondtam", "mondta"],
    },
}


def scene_breaks(text: str) -> int:
    body = text.split("<!-- NOTES -->", 1)[0]
    lines = body.split("\n")[1:]
    rules = [i for i, l in enumerate(lines) if re.match(r"^\s*-{3,}\s*$", l)]
    return max(0, len(rules) - 1)   # first rule is the title separator


def words(text: str) -> int:
    body = text.split("<!-- NOTES -->", 1)[0]
    return len(re.sub(r"[#*_—–]", " ", body).split())


def main(lang: str) -> int:
    rules = RULES.get(lang)
    if not rules:
        print(f"no rules for '{lang}' — add an entry to RULES in {Path(__file__).name}")
        return 2
    tgt = ROOT / "translations" / lang / "chapters"
    problems = 0
    en_files = sorted(EN.glob("chapter-*.md"))
    print(f"{'chapter':26s} {'sb en/de':>9s} {'words en/de':>13s} {'ratio':>6s}  issues")
    for src in en_files:
        dst = tgt / src.name
        if not dst.is_file():
            print(f"{src.name:26s} {'':>9s} {'':>13s} {'':>6s}  MISSING")
            problems += 1
            continue
        en, de = src.read_text(encoding="utf-8"), dst.read_text(encoding="utf-8")
        issues = []
        sb_en, sb_de = scene_breaks(en), scene_breaks(de)
        if sb_en != sb_de:
            issues.append(f"scene breaks {sb_en}≠{sb_de}")
        head = de.split("\n", 1)[0]
        if not rules["label_re"].match(head):
            issues.append(f"heading {head!r}")
        if "<!-- NOTES -->" not in de:
            issues.append("no NOTES trailer")
        body = de.split("<!-- NOTES -->", 1)[0]
        for needle, what in rules["bad_typography"]:
            n = body.count(needle)
            if n:
                issues.append(f"{what} ×{n}")
        if lang in ("ro", "hu"):
            stray = sum(1 for l in body.split("\n") if "—" in l.lstrip()[1:] or (lang == "hu" and "—" in l))
            if stray:
                issues.append(f"em dash inside a line ×{stray} (dialogue dash only at line start; use – for pauses)")
        # Hungarian suffixes lengthen a final a/e (Claudia → Claudiát); compare on a folded copy
        body_names = body.replace("á", "a").replace("é", "e") if lang == "hu" else body
        for name in NAMES:
            n_en, n_de = en.count(name), body_names.count(name)
            if n_en and not n_de:
                issues.append(f"name lost: {name}")
        w_en, w_de = words(en), words(de)
        ratio = w_de / w_en if w_en else 0
        lo, hi = rules["ratio"]
        if not lo <= ratio <= hi:
            issues.append(f"length ratio {ratio:.2f}")
        if issues:
            problems += 1
        print(f"{src.name:26s} {sb_en:>4d}/{sb_de:<4d} {w_en:>6d}/{w_de:<6d} {ratio:>6.2f}  {'; '.join(issues)}")
    print(f"\n{len(en_files)} chapters, {problems} with issues")
    tics = rules.get("tics")
    if tics:
        text = "".join(p.read_text(encoding="utf-8").split("<!-- NOTES -->", 1)[0]
                       for p in sorted(tgt.glob("chapter-*.md")))
        print("\ntic counts (book-wide):")
        for t in tics:
            print(f"  {t!r:16s} {text.count(t):5d}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "de"))
