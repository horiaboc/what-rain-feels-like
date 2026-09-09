#!/usr/bin/env python3
"""Build every publishable artifact for one edition.

    .venv/bin/python tools/build.py              # everything, base edition
    .venv/bin/python tools/build.py --check      # validate only, write nothing
    .venv/bin/python tools/build.py --only epub  # one target
    .venv/bin/python tools/build.py --lang de    # a translation
    .venv/bin/python tools/build.py --editions   # list what can be built

Each edition builds into its own folder — `build/en/`, `build/de/` — and reads
its own sources, so translations never overwrite each other. Editions are
declared in `bookbuild/config.py`.

Order matters in one place: the cover depends on the interior's page count,
because that is what sets the spine width. Asking for a cover therefore builds
the interior first.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bookbuild import boilerplate, config as c
from bookbuild.sources import load_book

TARGETS = ["manuscript", "text", "epub", "interior", "cover", "docx", "metadata"]


def _human(path: Path) -> str:
    size = path.stat().st_size
    unit = "KB" if size < 1_048_576 else "MB"
    val = size / 1024 if size < 1_048_576 else size / 1_048_576
    return f"{path.relative_to(c.ROOT)}  ({val:,.0f} {unit})"


def check(book) -> int:
    print(f"  edition       {c.LANG} — {c.EDITION_NAME} ({c.LANGUAGE})")
    print(f"  sources       {c.CHAPTERS_DIR.relative_to(c.ROOT)}, "
          f"{c.MATTER_DIR.relative_to(c.ROOT)}")
    print(f"  output        {c.BUILD_DIR.relative_to(c.ROOT)}/")
    print(f"  chapters      {len(book.chapters)}")
    print(f"  words         {book.word_count:,}")
    voices = {}
    for ch in book.chapters:
        voices[ch.voice] = voices.get(ch.voice, 0) + 1
    print("  voices        " + ", ".join(f"{v}×{n}" for v, n in sorted(voices.items())))

    skipped = [p.stem for p in book.front + book.back if p.unfilled]
    if skipped:
        print(f"  skipped pages {', '.join(skipped)}  (placeholder only — not printed)")

    blocked = False

    # The copyright page is generated in the edition's own language. Without
    # boilerplate for that language the build still produces a proof, but with
    # the base language's rights page in it — which must not ship.
    if not boilerplate.has_copyright(c.LANG):
        print(f"\n  no copyright boilerplate for '{c.LANG}' — the page will fall back "
              f"to {c.BASE_LANG}.\n  Add an entry to tools/bookbuild/boilerplate.py "
              f"before publishing this edition.")
        blocked = True

    missing = book.all_placeholders()
    if missing:
        print(f"\n  {len(missing)} unfilled placeholder(s) — resolve before uploading to KDP:")
        for where, what in missing:
            print(f"    {where:24s} {what}")
        blocked = True
    else:
        print("\n  no unfilled placeholders")

    art = ((c.COVER_FRONT_RAW, c.COVER_BACK_RAW) if c.COVER_TEXT == "generated"
           else (c.COVER_FRONT, c.COVER_BACK, c.COVER_SPINE))
    for f in art:
        if not f.exists():
            print(f"    MISSING cover art: {f.relative_to(c.ROOT)}")
            return 1
    return 1 if blocked else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", default=c.BASE_LANG,
                    help=f"edition to build (default: {c.BASE_LANG})")
    ap.add_argument("--editions", action="store_true",
                    help="list the declared editions and exit")
    ap.add_argument("--only", choices=TARGETS, action="append",
                    help="build just this target (repeatable)")
    ap.add_argument("--check", action="store_true",
                    help="validate the sources and report placeholders; build nothing")
    args = ap.parse_args()

    if args.editions:
        print("\nDeclared editions:\n")
        for code, ed in sorted(c.EDITIONS.items()):
            base = " (base)" if code == c.BASE_LANG else ""
            print(f"  {code}{base:7s}  {ed['name']:10s}  {ed['title']}  -> build/{code}/")
        print("\nAdd more in tools/bookbuild/config.py\n")
        return 0

    c.configure(args.lang)

    t0 = time.time()
    print(f"\n{c.TITLE} — {c.EDITION_NAME} edition\n")

    if not c.CHAPTERS_DIR.is_dir():
        print(f"  no sources for '{c.LANG}': {c.CHAPTERS_DIR.relative_to(c.ROOT)} does not exist")
        return 1

    book = load_book()

    status = check(book)
    if args.check:
        return status

    wanted = set(args.only or TARGETS)
    # The spine width comes from the interior page count, so a cover request
    # implies an interior build.
    if "cover" in wanted or "metadata" in wanted:
        wanted.add("interior")

    print()
    written: list[Path] = []
    pages = None
    cover_info = None

    if "manuscript" in wanted:
        from bookbuild.manuscript import write_manuscript
        write_manuscript(book)
        written.append(c.OUT_MANUSCRIPT)

    if "text" in wanted:
        from bookbuild.manuscript import write_text_exports
        write_text_exports(book)
        print(f"  text/         {len(book.chapters)} chapters + full-book.txt")

    if "epub" in wanted:
        from bookbuild.epub import build_epub
        build_epub(book)
        written.append(c.OUT_EPUB)

    if "interior" in wanted:
        from bookbuild.pdf import render_interior
        pages = render_interior(book)
        written.append(c.OUT_INTERIOR)
        print(f"  interior      {pages} pages")

    if "cover" in wanted:
        from bookbuild.cover import build_cover
        cover_info = build_cover(pages)
        written.append(c.OUT_COVER)
        print(f"  spine         {cover_info['spine_in']:.4f}in "
              f"({cover_info['spine_px']}px) at {pages} pages")

    if "docx" in wanted:
        from bookbuild.docx_out import build_docx
        build_docx(book)
        written.append(c.OUT_DOCX)

    if "metadata" in wanted:
        from bookbuild.cover import build_cover
        from bookbuild.meta import write_metadata
        if cover_info is None:
            cover_info = build_cover(pages)
        write_metadata(book, cover_info)
        written.append(c.OUT_METADATA)

    print("\n  written:")
    for p in written:
        print(f"    {_human(p)}")
    proof = c.BUILD_DIR / f"{c.SLUG}_cover-proof.png"
    if proof.exists() and "cover" in wanted:
        print(f"    {_human(proof)}")

    print(f"\n  done in {time.time() - t0:.1f}s\n")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
