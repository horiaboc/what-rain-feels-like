#!/usr/bin/env python3
"""Render a single chapter Markdown file to a review PDF.

    .venv/bin/python tools/chapter_pdf.py <chapter.md> <lang> [out.pdf]

For translation probes and native-speaker review — A4, generous margins,
the book's own EB Garamond, per-language hyphenation. Not a KDP artifact;
the full book goes through tools/build.py.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bookbuild import config as c  # noqa: E402  (fonts dir, root)
from bookbuild.sources import _render_md  # noqa: E402
from bookbuild.styles import _font_faces, STACK  # noqa: E402

from weasyprint import CSS, HTML  # noqa: E402
from weasyprint.text.fonts import FontConfiguration  # noqa: E402

CSS_TMPL = """
{fonts}
@page {{
  size: A4;
  margin: 2.4cm 2.6cm;
  @bottom-center {{ content: counter(page); font-family: {stack}; font-size: 9.5pt; }}
  @top-right {{ content: "{header}"; font-family: {stack}; font-size: 9pt; font-style: italic; }}
}}
html {{ font-family: {stack}; font-size: 11.5pt; line-height: 1.5;
       hyphens: auto; -weasy-hyphens: auto; }}
p {{ margin: 0; text-indent: 1.2em; text-align: justify; orphans: 2; widows: 2; }}
p.opening {{ text-indent: 0; }}
h1 {{ font-size: 16pt; font-weight: 400; text-align: center; margin: 1.2em 0 2em; }}
.scene-break {{ text-indent: 0; text-align: center; margin: 1.3em 0; letter-spacing: 0.1em; }}
.notes {{ margin-top: 3em; border-top: 1px solid #999; padding-top: 1em; font-size: 9.5pt; }}
.notes p {{ text-indent: 0; text-align: left; }}
"""


def render(md_path: Path, lang: str, out_path: Path) -> None:
    raw = md_path.read_text(encoding="utf-8")

    # Split off translator notes, if present.
    notes = ""
    if "<!-- NOTES -->" in raw:
        raw, notes = raw.split("<!-- NOTES -->", 1)

    lines = raw.strip().split("\n")
    heading = lines[0][2:].strip() if lines and lines[0].startswith("# ") else md_path.stem
    body = "\n".join(lines[1:])
    body = re.sub(r"\A\s*\n?-{3,}\s*\n", "\n", body, count=1)

    segments = [s.strip() for s in re.split(r"^\s*-{3,}\s*$", body, flags=re.M) if s.strip()]
    parts = [f"<h1>{heading}</h1>"]
    for i, seg in enumerate(segments):
        if i:
            parts.append('<p class="scene-break">·   ·   ·</p>')
        parts.append(_render_md(seg).replace("<p>", '<p class="opening">', 1))
    if notes.strip():
        parts.append('<div class="notes"><p><strong>Translator notes</strong></p>'
                     + _render_md(notes.strip()) + "</div>")

    html = (f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8">'
            f"<title>{heading}</title></head><body>{''.join(parts)}</body></html>")

    css = CSS_TMPL.format(fonts=_font_faces("assets/fonts/"), stack=STACK,
                          header=f"What Rain Feels Like — {lang}")
    fc = FontConfiguration()
    HTML(string=html, base_url=str(c.ROOT)).write_pdf(
        out_path,
        # The stylesheet needs its own base_url — the @font-face src URLs are
        # relative to the repo root and resolve against the CSS, not the
        # document. Without it every @font-face rule is dropped.
        stylesheets=[CSS(string=css, base_url=str(c.ROOT), font_config=fc)],
        font_config=fc)
    print(f"  {out_path}  ({out_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    src = Path(sys.argv[1])
    lang = sys.argv[2]
    out = Path(sys.argv[3]) if len(sys.argv) > 3 else src.with_suffix(".pdf")
    render(src, lang, out)
