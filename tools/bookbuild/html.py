"""Turn the parsed Book into HTML — the common ground for PDF and EPUB.

The half-title, title page and copyright page are generated here rather than
read from book-matter/, because they are pure layout over values that already
live in config.py (and, for the rights-page wording, boilerplate.py). Every
other page comes from a file and stays editable.

A generated page steps aside if book-matter/ supplies a file of the same kind,
so an edition whose rights page has to differ can still hand-write one.
"""

from __future__ import annotations

import html as _html
import re

from . import boilerplate, config as c
from .sources import Book, Chapter, MatterPage


def esc(s: str) -> str:
    return _html.escape(s, quote=False)


def _mark_opening(scene_html: str) -> str:
    """First paragraph of a scene loses its indent (indent marks continuation)."""
    return scene_html.replace("<p>", '<p class="opening">', 1)


def chapter_html(ch: Chapter, *, heading_tag: str = "h1") -> str:
    title = f'<{heading_tag} class="ch-title">{esc(ch.title)}</{heading_tag}>' if ch.title else ""
    parts = [
        '<header class="chapter-head">',
        f'<p class="ch-label">{esc(ch.label)}</p>',
        title,
        "</header>",
    ]
    for i, scene in enumerate(ch.scenes):
        if i:
            parts.append(f'<p class="scene-break">{esc(c.SCENE_BREAK)}</p>')
        parts.append(_mark_opening(scene))
    return "\n".join(p for p in parts if p)


def half_title_html() -> str:
    return f'<h1>{esc(c.TITLE)}</h1>'


def title_page_html() -> str:
    imprint = f"{c.IMPRINT} · {c.IMPRINT_CITY}" if c.IMPRINT_CITY else c.IMPRINT
    return (
        f'<h1>{esc(c.TITLE)}</h1>\n'
        f'<p class="tp-subtitle">{esc(c.SUBTITLE)}</p>\n'
        f'<p class="tp-author">{esc(c.AUTHOR_DISPLAY)}</p>\n'
        f'<p class="tp-imprint">{esc(imprint)}</p>'
    )


def _emphasise(line: str) -> str:
    """Escape a boilerplate line, then honour its `*emphasis*` spans."""
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", esc(line))


def copyright_html(*, heading_tag: str = "h1") -> str:
    parts = [f'<{heading_tag}>{esc(boilerplate.copyright_heading())}</{heading_tag}>']
    for css, lines in boilerplate.copyright_blocks():
        attr = f' class="{css}"' if css else ""
        parts.append(f"<p{attr}>" + "<br/>".join(_emphasise(ln) for ln in lines) + "</p>")
    return "\n".join(parts)


def matter_html(page: MatterPage, *, heading_tag: str = "h1") -> str:
    parts = []
    if page.heading:
        parts.append(f'<{heading_tag}>{esc(page.heading)}</{heading_tag}>')
    if page.html:
        parts.append(page.html)
    return "\n".join(parts)


# Generated pages, in mounting order, that precede the file-backed front matter.
GENERATED_FRONT = [
    ("half-title", half_title_html),
    ("title-page", title_page_html),
    ("copyright", copyright_html),
]


def generated_front(book: Book) -> list[tuple[str, str]]:
    """Generated front matter for this edition, already rendered.

    A kind that book-matter/ supplies as a file is dropped here so the file
    wins — the escape hatch for an edition that needs a hand-written page.
    """
    supplied = {p.kind for p in book.front}
    return [(kind, fn()) for kind, fn in GENERATED_FRONT if kind not in supplied]


def print_document(book: Book, part: str = "all") -> str:
    """The book as an HTML document for WeasyPrint.

    `part` selects "front" or "body"; the print build renders the two
    separately so the body's page numbering can start at 1. WeasyPrint has no
    element-level reset for the `page` counter, so separate documents are the
    only way to restart the folios. "all" renders everything in one pass and is
    used for previews.
    """
    out = [
        "<!DOCTYPE html>",
        f'<html lang="{c.LANGUAGE}"><head><meta charset="utf-8">',
        f"<title>{esc(c.TITLE)}</title></head><body>",
    ]

    if part in ("all", "front"):
        for kind, markup in generated_front(book):
            out.append(f'<section class="matter bm-{kind}">{markup}</section>')
        for page in book.front:
            if page.unfilled:
                continue
            out.append(f'<section class="matter {page.css_class}">{matter_html(page)}</section>')

    if part in ("all", "body"):
        for i, ch in enumerate(book.chapters):
            first = " chapter-first" if i == 0 else ""
            out.append(
                f'<section class="chapter{first}" id="{ch.slug}">{chapter_html(ch)}</section>'
            )
        for page in book.back:
            if page.unfilled:
                continue
            out.append(f'<section class="matter {page.css_class}">{matter_html(page)}</section>')

    out.append("</body></html>")
    return "\n".join(out)
