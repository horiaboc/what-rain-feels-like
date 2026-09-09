"""EPUB 3 for the KDP Kindle upload.

Hand-rolled rather than pulled from a library: an EPUB is a zip with a known
layout, and writing it directly keeps the dependency surface small and the
output predictable. A legacy toc.ncx is included alongside the EPUB 3 nav
document because Amazon's converter still reads it.

Amazon converts this file server-side into its own format, so this is the
upload artifact for both KDP and Send-to-Kindle.
"""

from __future__ import annotations

import io
import zipfile
from datetime import date

from PIL import Image

from . import config as c, covertext
from .html import chapter_html, esc, matter_html, generated_front
from .sources import Book
from .styles import epub_css

XHTML = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}">
<head><meta charset="utf-8"/><title>{title}</title>
<link rel="stylesheet" type="text/css" href="../styles/style.css"/></head>
<body>{body}</body>
</html>
"""

FONT_FILES = [
    "EBGaramond-Regular.ttf",
    "EBGaramond-Bold.ttf",
    "EBGaramond-Italic.ttf",
    "EBGaramond-BoldItalic.ttf",
    "HebrewFallback-Regular.ttf",
]


def _cover_jpeg() -> bytes:
    """Front cover as JPEG, sized for Kindle (long edge 2560px).

    The ebook cover is the front panel without the print bleed — a Kindle
    thumbnail wants the trimmed picture, not the part that gets guillotined.
    """
    target_h = 2560
    if c.COVER_TEXT == "generated":
        im = covertext.render_front(round(target_h * c.TRIM_W_IN / c.TRIM_H_IN), target_h)
    else:
        im = Image.open(c.COVER_FRONT).convert("RGB")
    if im.height != target_h:
        w = round(im.width * target_h / im.height)
        im = im.resize((w, target_h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=88, optimize=True, progressive=True)
    return buf.getvalue()


def _page(title: str, body: str) -> bytes:
    return XHTML.format(lang=c.LANGUAGE, title=esc(title), body=body).encode("utf-8")


def build_epub(book: Book) -> None:
    c.BUILD_DIR.mkdir(parents=True, exist_ok=True)

    # (id, href, media-type, xhtml-bytes-or-None, nav-label-or-None)
    items: list[tuple[str, str, str, bytes | None, str | None]] = []

    items.append(("cover-image", "images/cover.jpg", "image/jpeg", _cover_jpeg(), None))
    items.append(("css", "styles/style.css", "text/css",
                  epub_css().encode("utf-8"), None))
    for f in FONT_FILES:
        items.append((f.replace(".", "-"), f"fonts/{f}", "font/ttf",
                      (c.FONTS_DIR / f).read_bytes(), None))

    cover_body = ('<div class="cover-page">'
                  f'<img src="../images/cover.jpg" alt="{esc(c.TITLE)}"/></div>')
    items.append(("cover", "text/cover.xhtml", "application/xhtml+xml",
                  _page(c.TITLE, cover_body), None))

    for kind, markup in generated_front(book):
        items.append((kind, f"text/{kind}.xhtml", "application/xhtml+xml",
                      _page(c.TITLE, f'<section class="matter bm-{kind}">{markup}</section>'),
                      None))

    for page in book.front:
        if page.unfilled:
            continue
        body = f'<section class="matter {page.css_class}">{matter_html(page)}</section>'
        items.append((page.kind, f"text/{page.kind}.xhtml", "application/xhtml+xml",
                      _page(page.heading or c.TITLE, body), None))

    for ch in book.chapters:
        body = f'<section class="chapter">{chapter_html(ch)}</section>'
        items.append((ch.slug, f"text/{ch.slug}.xhtml", "application/xhtml+xml",
                      _page(ch.heading_plain, body), ch.heading_plain))

    for page in book.back:
        if page.unfilled:
            continue
        body = f'<section class="matter {page.css_class}">{matter_html(page)}</section>'
        items.append((page.kind, f"text/{page.kind}.xhtml", "application/xhtml+xml",
                      _page(page.heading or c.TITLE, body), page.heading))

    spine = [i for i in items if i[2] == "application/xhtml+xml"]
    nav_entries = [(i[1], i[4]) for i in spine if i[4]]

    manifest = "\n".join(
        f'    <item id="{iid}" href="{href}" media-type="{mtype}"'
        + (' properties="cover-image"' if iid == "cover-image" else "")
        + "/>"
        for iid, href, mtype, _, _ in items
    )
    spine_xml = "\n".join(f'    <itemref idref="{i[0]}"/>' for i in spine)

    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid"
         xml:lang="{c.LANGUAGE}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{c.EPUB_UUID}</dc:identifier>
    <dc:title>{esc(c.TITLE)}</dc:title>
    <dc:creator id="author">{esc(c.AUTHOR_METADATA)}</dc:creator>
    <meta refines="#author" property="file-as">{esc(c.AUTHOR_SORT)}</meta>
    <dc:language>{c.LANGUAGE}</dc:language>
    <dc:date>{date.today().isoformat()}</dc:date>
    <dc:publisher>{esc(c.IMPRINT)}</dc:publisher>
    <dc:rights>Copyright © {c.YEAR} {esc(c.AUTHOR_LEGAL)}</dc:rights>
    <meta property="dcterms:modified">{date.today().isoformat()}T00:00:00Z</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
{manifest}
  </manifest>
  <spine toc="ncx">
{spine_xml}
  </spine>
</package>
"""

    nav_items = "\n".join(
        f'      <li><a href="{href}">{esc(label)}</a></li>' for href, label in nav_entries
    )
    nav = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"
      lang="{c.LANGUAGE}">
<head><meta charset="utf-8"/><title>Contents</title></head>
<body>
  <nav epub:type="toc" id="toc"><h1>Contents</h1>
    <ol>
{nav_items}
    </ol>
  </nav>
</body>
</html>
"""

    ncx_points = "\n".join(
        f'    <navPoint id="n{i}" playOrder="{i}">'
        f'<navLabel><text>{esc(label)}</text></navLabel>'
        f'<content src="{href}"/></navPoint>'
        for i, (href, label) in enumerate(nav_entries, 1)
    )
    ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{c.EPUB_UUID}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{esc(c.TITLE)}</text></docTitle>
  <navMap>
{ncx_points}
  </navMap>
</ncx>
"""

    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""

    with zipfile.ZipFile(c.OUT_EPUB, "w", zipfile.ZIP_DEFLATED) as z:
        # The mimetype entry must be first and stored uncompressed.
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container)
        z.writestr("OEBPS/content.opf", opf)
        z.writestr("OEBPS/nav.xhtml", nav)
        z.writestr("OEBPS/toc.ncx", ncx)
        for _, href, _, data, _ in items:
            z.writestr(f"OEBPS/{href}", data)
