"""CSS for the two rendered formats.

Print and ebook diverge more than they share — print is a fixed 6×9 page with
mirrored gutters and folios, the ebook reflows to an unknown screen — so they
get separate stylesheets rather than one stylesheet with overrides.
"""

from __future__ import annotations

from . import config as c


def _font_faces(prefix: str) -> str:
    """@font-face blocks. `prefix` locates the .ttf files for each target."""
    faces = [
        ("EB Garamond", 400, "normal", "EBGaramond-Regular.ttf"),
        ("EB Garamond", 700, "normal", "EBGaramond-Bold.ttf"),
        ("EB Garamond", 400, "italic", "EBGaramond-Italic.ttf"),
        ("EB Garamond", 700, "italic", "EBGaramond-BoldItalic.ttf"),
        ("Hebrew Fallback", 400, "normal", "HebrewFallback-Regular.ttf"),
        # The ch38 title and the ch55 sign-off are set in the italic chapter
        # style. Hebrew has no italic, and with no face declared for it the
        # renderer skews the upright one — so א, which is ALEPH's signature,
        # comes out leaning. Pointing italic at the same file keeps it upright.
        ("Hebrew Fallback", 400, "italic", "HebrewFallback-Regular.ttf"),
    ]
    return "\n".join(
        "@font-face{{font-family:'{}';font-weight:{};font-style:{};"
        "src:url('{}{}') format('truetype');}}".format(fam, w, s, prefix, f)
        for fam, w, s, f in faces
    )


# The Hebrew face carries only א and is listed purely as a per-glyph fallback,
# so the ch38 title renders without dragging in a system font.
STACK = f"'{c.BODY_FONT}', 'Hebrew Fallback', serif"


def print_css() -> str:
    return f"""
{_font_faces('assets/fonts/')}

@page {{
  size: {c.TRIM_W_IN}in {c.TRIM_H_IN}in;
  margin-top: {c.MARGIN_TOP_IN}in;
  margin-bottom: {c.MARGIN_BOTTOM_IN}in;
  @bottom-center {{
    content: counter(page);
    font-family: {STACK};
    font-size: 9.5pt;
    margin-top: 0.18in;
    vertical-align: top;
  }}
}}

/* Verso: gutter on the right, running head and folio to the outside.
   `first-except` suppresses the head on the page where the string is set —
   i.e. on each chapter's opening page, which is the correct convention.
   WeasyPrint does not scope `@page name:first` per chapter, so this is the
   mechanism that actually works. */
@page :left {{
  margin-left: {c.MARGIN_OUTSIDE_IN}in;
  margin-right: {c.MARGIN_INSIDE_IN}in;
  @top-left {{
    content: string(runverso, first-except);
    font-family: {STACK}; font-size: 9pt;
    letter-spacing: 0.06em; margin-bottom: 0.20in;
    vertical-align: bottom;
  }}
}}

/* Recto: gutter on the left. */
@page :right {{
  margin-left: {c.MARGIN_INSIDE_IN}in;
  margin-right: {c.MARGIN_OUTSIDE_IN}in;
  @top-right {{
    content: string(runrecto, first-except);
    font-family: {STACK}; font-size: 9pt;
    font-style: italic; margin-bottom: 0.20in;
    vertical-align: bottom;
  }}
}}

/* Blank versos inserted to force a recto start carry nothing at all. */
@page :blank {{
  @top-left {{ content: none; }}
  @top-right {{ content: none; }}
  @bottom-center {{ content: none; }}
}}

/* Front and back matter: no folio, no running head. */
@page matter {{
  @top-left {{ content: none; }}
  @top-right {{ content: none; }}
  @bottom-center {{ content: none; }}
}}

html {{
  font-family: {STACK};
  font-size: {c.BODY_SIZE_PT}pt;
  line-height: {c.LINE_HEIGHT};
  hyphens: auto;
  -weasy-hyphens: auto;
}}

body {{ margin: 0; }}

p {{
  margin: 0;
  text-indent: {c.INDENT_EM}em;
  text-align: justify;
  orphans: 2;
  widows: 2;
  hyphenate-limit-chars: 6 3 3;
}}

/* No indent on the first line of a chapter or of a new scene — the standard
   rule: indentation marks continuation, not a beginning. */
p.opening {{ text-indent: 0; }}

em {{ font-style: italic; }}

.scene-break {{
  text-indent: 0;
  text-align: center;
  margin: {c.LINE_HEIGHT * 0.9}em 0;
  font-size: 10pt;
  letter-spacing: 0.1em;
  break-inside: avoid;
}}

/* ── Chapters ─────────────────────────────────────────────────────────── */

section.chapter {{
  page: chapter;
  break-before: {'right' if c.CHAPTER_BREAK == 'right' else 'page'};
}}

/* Arabic folios restart at 1 with the body; the front matter is unnumbered.
   The class is applied in html.py — `:first-of-type` would match by tag and
   land on the half-title instead. */
section.chapter-first {{ counter-reset: page 1; }}

.chapter-head {{
  margin-top: 0.55in;
  margin-bottom: 0.42in;
  text-align: center;
  break-after: avoid;
  string-set: runverso "{c.RUNNING_HEAD_VERSO}", runrecto "{c.RUNNING_HEAD_RECTO}";
}}

.ch-label {{
  text-indent: 0;
  text-align: center;
  font-size: 9.5pt;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  margin-bottom: 0.14in;
}}

.ch-title {{
  font-size: 15pt;
  font-weight: 400;
  font-style: italic;
  margin: 0;
  line-height: 1.25;
}}

/* ── In-fiction document (ch53, the newspaper piece) ──────────────────── */

.doc-headline {{
  text-indent: 0; text-align: center;
  font-size: 13pt; font-weight: 700;
  letter-spacing: 0.04em;
  margin: 0.9em 0 0.5em;
  break-after: avoid;
}}

.doc-standfirst {{
  text-indent: 0;
  font-size: 10.2pt; font-style: italic;
  margin-bottom: 0.8em;
}}

.doc-subhead {{
  text-indent: 0;
  font-weight: 700; font-size: 11pt;
  margin: 1.1em 0 0.35em;
  break-after: avoid;
}}

/* ── Front and back matter ────────────────────────────────────────────── */

section.matter {{
  page: matter;
  break-before: right;
}}

/* The copyright page is the verso of the title page, so it takes the very
   next page rather than being pushed to the next recto. */
section.bm-copyright {{ break-before: page; }}

section.matter p {{ text-indent: 0; text-align: left; hyphens: none; }}

section.bm-half-title, section.bm-title-page,
section.bm-dedication, section.bm-epigraph {{
  text-align: center;
}}
/* The p rule above ranges matter text left; these pages centre their lines. */
section.bm-dedication p, section.bm-epigraph p {{ text-align: center; }}

section.bm-half-title {{ padding-top: 2.6in; }}
section.bm-half-title h1 {{
  font-size: 17pt; font-weight: 400;
  letter-spacing: 0.05em;
}}

section.bm-title-page {{ padding-top: 1.9in; }}
section.bm-title-page h1 {{
  font-size: 26pt; font-weight: 400;
  letter-spacing: 0.02em; line-height: 1.15;
  margin: 0 0 0.3in;
}}
section.bm-title-page p {{ text-align: center; text-indent: 0; }}
section.bm-title-page .tp-subtitle {{
  font-size: 12pt; font-style: italic; margin-bottom: 1.5in;
}}
section.bm-title-page .tp-author {{
  font-size: 15pt; letter-spacing: 0.04em;
}}
section.bm-title-page .tp-imprint {{
  font-size: 9.5pt; margin-top: 2.0in; letter-spacing: 0.05em;
}}

section.bm-copyright {{ padding-top: 0.9in; font-size: 8.8pt; line-height: 1.45; }}
section.bm-copyright h1 {{ display: none; }}
section.bm-copyright p {{ margin-bottom: 0.62em; }}
section.bm-copyright .cp-title {{ font-style: italic; }}

section.bm-dedication {{ padding-top: 2.8in; font-style: italic; font-size: 11.5pt; }}
section.bm-dedication h1 {{ display: none; }}

section.bm-epigraph {{ padding-top: 2.6in; font-style: italic; }}
section.bm-epigraph h1 {{ display: none; }}

section.matter h1 {{
  font-size: 13pt; font-weight: 400;
  letter-spacing: 0.16em; text-transform: uppercase;
  text-align: center; margin: 0 0 0.4in;
}}

section.bm-about-the-author p, section.bm-colophon p,
section.bm-acknowledgments p {{
  text-align: justify;
}}
"""


def epub_css() -> str:
    """Reflowable styling. No page geometry — the reading system owns that."""
    return f"""
{_font_faces('../fonts/')}

html, body {{
  font-family: {STACK};
  line-height: {c.LINE_HEIGHT};
  margin: 0;
  padding: 0 0.6em;
}}

p {{
  margin: 0;
  text-indent: {c.INDENT_EM}em;
  text-align: justify;
  orphans: 2;
  widows: 2;
}}

p.opening {{ text-indent: 0; }}

.scene-break {{
  text-indent: 0;
  text-align: center;
  margin: 1.3em 0;
  letter-spacing: 0.1em;
}}

.chapter-head {{ margin: 1.6em 0 2.1em; text-align: center; page-break-after: avoid; }}

.ch-label {{
  text-indent: 0; text-align: center;
  font-size: 0.8em; letter-spacing: 0.22em;
  text-transform: uppercase; margin-bottom: 0.7em;
}}

.ch-title {{ font-size: 1.5em; font-weight: normal; font-style: italic; margin: 0; }}

.doc-headline {{
  text-indent: 0; text-align: center;
  font-size: 1.2em; font-weight: bold;
  margin: 1.1em 0 0.6em;
}}
.doc-standfirst {{ text-indent: 0; font-style: italic; margin-bottom: 1em; }}
.doc-subhead {{ text-indent: 0; font-weight: bold; margin: 1.3em 0 0.4em; }}

.cover-page {{ margin: 0; padding: 0; text-align: center; }}
.cover-page img {{ max-width: 100%; height: auto; }}

section.matter p {{ text-indent: 0; text-align: left; }}
section.bm-half-title, section.bm-title-page,
section.bm-dedication, section.bm-epigraph {{ text-align: center; }}
section.bm-dedication p, section.bm-epigraph p {{ text-align: center; }}
section.bm-title-page h1 {{ font-size: 2em; font-weight: normal; }}
section.bm-title-page p {{ text-indent: 0; text-align: center; }}
section.bm-title-page .tp-subtitle {{ font-style: italic; margin-bottom: 2.5em; }}
section.bm-title-page .tp-author {{ font-size: 1.2em; margin-bottom: 3em; }}
section.bm-copyright {{ font-size: 0.85em; }}
section.bm-copyright h1 {{ display: none; }}
section.bm-copyright .cp-title {{ font-style: italic; }}
section.bm-dedication {{ font-style: italic; margin-top: 3em; }}
section.bm-dedication h1 {{ display: none; }}
section.bm-epigraph h1 {{ display: none; }}
section.matter h1 {{
  font-size: 1.15em; font-weight: normal;
  letter-spacing: 0.16em; text-transform: uppercase;
  text-align: center; margin-bottom: 1.6em;
}}
"""
