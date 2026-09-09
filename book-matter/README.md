# Book Matter — front & back pages for final mounting

Non-chapter pages that wrap the manuscript when the book is assembled. Kept out of `chapters/` on purpose, so the chapter build/glob and word counts stay clean.

## How these files are used

`tools/build.py` reads them, so a few rules apply:

- **`{{TOKEN}}` is substituted from `tools/bookbuild/config.py`.** `{{TITLE}}`, `{{AUTHOR_LEGAL}}`, `{{YEAR}}`, `{{IMPRINT}}`, `{{ISBN_PAPERBACK}}` and any other config name. Set the value once in config, not in eight files.
- **Italic `*(parenthetical notes)*` are stripped** before typesetting — they are guidance to you, not book content. Keep writing them.
- **A page whose only real content is a `[bracketed placeholder]` is dropped** from the build, and `build.py --check` lists it. That is why the dedication, epigraph and acknowledgments do not currently appear in the book: write them and they mount automatically.
- The half-title, title page and copyright page are **generated** (`tools/bookbuild/html.py`), not read from here. The first two are pure layout over values config already holds; the copyright page is legal boilerplate, so its wording lives per language in `tools/bookbuild/boilerplate.py` and every translation gets a rights page in its own language without anyone re-deriving it. Drop a `03-copyright.md` back into this directory (or into `translations/<lang>/book-matter/`) and it overrides the generated page for that edition.

## Mounting order (front to back)

**Front matter** (right-hand pages start recto; blanks fall where needed)
1. Half title — *generated from config*
2. Title page — *generated from config*
3. Copyright page **(required)** — *generated, per language, from `tools/bookbuild/boilerplate.py`* — verso of the title page
4. `04-dedication.md` — dedication *(optional)*
5. `05-epigraph.md` — book-level epigraph *(optional; chapters already carry their own)*
   - *Table of contents:* optional for a novel. The **ebook auto-generates** a nav TOC, so print can skip it.

**Body** — `chapters/chapter-01 … chapter-55`

**Back matter**
6. `90-acknowledgments.md` — acknowledgments *(optional)*
7. `91-about-the-author.md` — about the author *(optional but recommended)*
8. `92-colophon.md` — colophon / note on the type *(optional)*

Not a page in the book:
- `blurb.md` — the back-cover / Kindle product-page description (goes on the print back cover and in the KDP Book Description field, not inside the book). Art prompt for the back cover lives in `../back-cover.md`.

## Required vs optional
Truly required: **title page + copyright page**. Everything else is convention — include what suits the book. For a quiet literary novel, spare front matter reads well.

Still to write, if you want them: `04-dedication.md`, `05-epigraph.md`, `90-acknowledgments.md`.

## Format notes
- Ebook (Kindle) uses **only the front cover** + these pages flow as the opening screens; the blurb goes in the KDP **Book Description** field.
- Print (paperback/hardcover) prints the blurb on the **back cover** (see `../back-cover.md`), and these pages are typeset into the interior.
- **AI-content disclosure:** at KDP upload you'll be asked whether the book used AI. This manuscript was **AI-assisted** (drafted with an AI collaborator, author-directed) and the **cover art is AI-generated** — disclose accordingly. Not a page in the book, but part of mounting prep.

*Run `.venv/bin/python tools/build.py --check` to list every placeholder still outstanding.*
