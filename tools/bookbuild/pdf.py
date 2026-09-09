"""Print interior PDF for KDP paperback.

KDP requires every font embedded and the page geometry to match the declared
trim size exactly. WeasyPrint embeds subsets of the vendored EB Garamond
automatically, so the output is self-contained.

Front matter and body are rendered as two documents and concatenated. That is
not decoration: WeasyPrint ignores element-level `counter-reset: page`, so
rendering the body on its own is the only way to make the story begin on
folio 1 with the front matter left unnumbered.

The returned page count determines the spine width, so this module must run
before the cover is built.
"""

from __future__ import annotations

import io

import pypdfium2 as pdfium
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from . import config as c
from .html import print_document
from .sources import Book
from .styles import print_css


def _render(book: Book, part: str) -> bytes:
    font_config = FontConfiguration()
    # base_url on the stylesheet, not just the document: the @font-face `src`
    # URLs are relative to the repo root and are resolved against the CSS's own
    # base URL. Without it WeasyPrint drops every @font-face rule with a
    # warning and silently falls back to the system serif — which on a machine
    # with no matching italic face also loses every italic in the book.
    doc = HTML(string=print_document(book, part), base_url=str(c.ROOT)).render(
        stylesheets=[CSS(string=print_css(), base_url=str(c.ROOT),
                         font_config=font_config)],
        font_config=font_config,
    )
    buf = io.BytesIO()
    doc.write_pdf(buf)
    return buf.getvalue()


def render_interior(book: Book) -> int:
    """Write the interior PDF. Returns its page count."""
    c.BUILD_DIR.mkdir(parents=True, exist_ok=True)

    front_pdf = pdfium.PdfDocument(_render(book, "front"))
    body_pdf = pdfium.PdfDocument(_render(book, "body"))

    out = pdfium.PdfDocument.new()
    out.import_pages(front_pdf)

    # The body must open on a recto, so the front matter has to end on a verso.
    if len(out) % 2:
        w, h = out[0].get_size()
        out.new_page(w, h)

    out.import_pages(body_pdf)
    out.save(str(c.OUT_INTERIOR))

    n = len(out)
    for d in (out, front_pdf, body_pdf):
        d.close()
    return n
