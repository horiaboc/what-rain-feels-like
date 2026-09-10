"""Single place for every knob the build responds to.

Everything that is a publishing decision — metadata, trim size, margins,
typography — lives here rather than being scattered through the renderers.
Edit this file, re-run the build, and every output format follows.

The build is per-edition. `EDITIONS` holds one entry per language; calling
`configure(lang)` points the source directories, the cover art and the output
paths at that edition. Nothing is shared between editions except the physical
book specification (trim, margins, fonts) and the author's identity.

    build/en/…        English edition
    build/de/…        German edition, once it exists

Adding a translation is one entry in EDITIONS plus a `translations/<lang>/`
directory — no renderer changes.
"""

from pathlib import Path
import uuid

ROOT = Path(__file__).resolve().parents[2]
FONTS_DIR = ROOT / "assets" / "fonts"
BUILD_ROOT = ROOT / "build"
COVER_ROOT = ROOT / "cover"
TRANSLATIONS_ROOT = ROOT / "translations"

# ─────────────────────────────────────────────────────────────────────────────
# Editions
#
# The base edition keeps its sources at the repo root (chapters/, book-matter/,
# cover/). Every translation lives under translations/<lang>/ with the same
# internal layout, and its cover art under cover/<lang>/.
#
# Per `translation-plan.md`: the pen name `_horia` is constant across all
# languages; the title may or may not be translated — decide per edition.
# ─────────────────────────────────────────────────────────────────────────────

BASE_LANG = "en"

EDITIONS: dict[str, dict] = {
    "en": {
        "name": "English",
        "locale": "en-GB",
        "title": "What Rain Feels Like",
        "subtitle": "a novel",
        "slug": "What-Rain-Feels-Like",
        "scene_break": "·   ·   ·",
        "isbn_paperback": "9798173180698",
    },
    # German is the priority translation (Berlin setting, second-largest
    # marketplace). Title and closing line are one decision — see
    # translations/de/NOTES.md before changing either.
    "de": {
        "name": "German",
        "locale": "de-DE",
        "title": "Wie sich Regen anfühlt",
        "subtitle": "Roman",
        "slug": "Wie-Sich-Regen-Anfuehlt",
        "scene_break": "·   ·   ·",
        "contents_label": "Inhalt",
        "byline_prefix": "von",   # the word before the pen name on the cover
        "isbn_paperback": "[assigned by KDP at publish]",
        # No translator credit: an AI draft with a native review is not a
        # translator in the copyright-page sense. Set a name here if a reviewer
        # takes on the edition as theirs.
    },
    "ro": {
        "name": "Romanian",
        "locale": "ro-RO",
        "title": "Cum se simte ploaia",
        "subtitle": "roman",
        "slug": "Cum-Se-Simte-Ploaia",
        "scene_break": "·   ·   ·",
        "contents_label": "Cuprins",
        "byline_prefix": "de",
        "isbn_paperback": "[assigned by KDP at publish]",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# Author identity — constant across every edition
# ─────────────────────────────────────────────────────────────────────────────

# Cover / retail byline. The leading underscore is an art treatment; KDP's
# author field should read "Horia" so the book is searchable (see
# production-notes.md). AUTHOR_METADATA is what goes into EPUB/DOCX metadata.
AUTHOR_DISPLAY = "_horia"
AUTHOR_METADATA = "Horia"
AUTHOR_SORT = "horia"

# The © line takes the legal name even when the cover carries the pen name.
AUTHOR_LEGAL = "Horia Bochis"

YEAR = "2026"
# The edition line ("First edition, 2026.") is language-specific and lives with
# the rest of the copyright-page boilerplate in boilerplate.py.
IMPRINT = "Independently published"
IMPRINT_CITY = "Meckesheim, Germany"

# ─────────────────────────────────────────────────────────────────────────────
# Print specification (KDP paperback) — the physical book, same in any language
# ─────────────────────────────────────────────────────────────────────────────

TRIM_W_IN = 6.0
TRIM_H_IN = 9.0

# "cream" is conventional for fiction and is what the spine maths below assumes.
PAPER = "cream"
PAPER_THICKNESS = {"white": 0.002252, "cream": 0.0025}  # inches per page

BLEED_IN = 0.125  # KDP requires 0.125" bleed on covers
COVER_DPI = 300

# Interior margins. KDP's minimum gutter for a 151–300pp book is 0.75";
# these sit above the minimum so the text block does not crowd the spine.
MARGIN_TOP_IN = 0.75
MARGIN_BOTTOM_IN = 0.70
MARGIN_INSIDE_IN = 0.875  # gutter side
MARGIN_OUTSIDE_IN = 0.625

# ─────────────────────────────────────────────────────────────────────────────
# Typography
# ─────────────────────────────────────────────────────────────────────────────

BODY_FONT = "EB Garamond"
BODY_SIZE_PT = 11.2
LINE_HEIGHT = 1.42
INDENT_EM = 1.2

# Start each chapter on a fresh page ("page") or force a right-hand page
# ("right"). "right" is the more formal setting and adds roughly 25 blank
# versos across 55 chapters.
CHAPTER_BREAK = "page"

RUNNING_HEAD_VERSO = AUTHOR_DISPLAY

# ─────────────────────────────────────────────────────────────────────────────
# Per-edition state — set by configure(), below
# ─────────────────────────────────────────────────────────────────────────────

LANG: str
EDITION_NAME: str
LANGUAGE: str
TITLE: str
SUBTITLE: str
SLUG: str
ISBN_PAPERBACK: str
EPUB_UUID: str

# The mark between scenes inside a chapter.
#
# `bible.md` reserves א as ALEPH's own signature (the ch38 title, the ch55
# sign-off). Using it on every scene break would spend that motif, so the
# default is a neutral triad. Set it per edition in EDITIONS above.
SCENE_BREAK: str
RUNNING_HEAD_RECTO: str
# Heading of the EPUB table of contents, in the edition's language.
CONTENTS_LABEL: str
# The word before the pen name on the cover ("by _horia" / "von _horia").
BYLINE_PREFIX: str

CHAPTERS_DIR: Path
MATTER_DIR: Path
COVER_DIR: Path
BUILD_DIR: Path

OUT_MANUSCRIPT: Path
OUT_TEXT_DIR: Path
OUT_EPUB: Path
OUT_INTERIOR: Path
OUT_COVER: Path
OUT_DOCX: Path
OUT_METADATA: Path

COVER_FRONT: Path
COVER_BACK: Path
COVER_SPINE: Path
COVER_FRONT_RAW: Path
COVER_BACK_RAW: Path

# Where the cover lettering comes from.
#
#   "generated" — typeset at build time over the `*-raw-hires.png` art by
#                 covertext.py. The spine follows the current page count, the
#                 blurb follows book-matter/blurb.md, and nothing can drift
#                 into KDP's barcode zone.
#   "baked"     — use the `*-hires.png` files with the text already in them.
#                 They cannot be corrected or re-cut, so this is only for
#                 comparing against the generated set.
COVER_TEXT = "generated"

# Print the byline on the back panel as well as the front and spine. It is the
# usual trade-paperback convention, but the name is already on both other
# panels, so dropping it is a legitimate choice — set this False.
COVER_BACK_BYLINE = True

# Kindle needs no ISBN — Amazon assigns an ASIN.
ISBN_EBOOK = ""


def configure(lang: str = BASE_LANG) -> None:
    """Point the build at one edition. Must run before anything is loaded."""
    global LANG, EDITION_NAME, LANGUAGE, TITLE, SUBTITLE, SLUG, ISBN_PAPERBACK
    global EPUB_UUID, SCENE_BREAK, RUNNING_HEAD_RECTO, CONTENTS_LABEL, BYLINE_PREFIX
    global CHAPTERS_DIR, MATTER_DIR, COVER_DIR, BUILD_DIR
    global OUT_MANUSCRIPT, OUT_TEXT_DIR, OUT_EPUB, OUT_INTERIOR
    global OUT_COVER, OUT_DOCX, OUT_METADATA
    global COVER_FRONT, COVER_BACK, COVER_SPINE, COVER_FRONT_RAW, COVER_BACK_RAW

    if lang not in EDITIONS:
        known = ", ".join(sorted(EDITIONS))
        raise SystemExit(
            f"unknown edition '{lang}'. Known editions: {known}.\n"
            f"Add one to EDITIONS in {Path(__file__).name} to build a translation."
        )

    ed = EDITIONS[lang]
    LANG = lang
    EDITION_NAME = ed["name"]
    LANGUAGE = ed["locale"]
    TITLE = ed["title"]
    SUBTITLE = ed["subtitle"]
    SLUG = ed["slug"]
    ISBN_PAPERBACK = ed["isbn_paperback"]
    SCENE_BREAK = ed["scene_break"]
    RUNNING_HEAD_RECTO = ed.get("running_head_recto") or ed["title"]
    CONTENTS_LABEL = ed.get("contents_label", "Contents")
    BYLINE_PREFIX = ed.get("byline_prefix", "by")

    # Stable per-edition identifier. Deterministic, so rebuilds keep the same
    # id, and distinct, so each translation is its own book to a reader's
    # library rather than a duplicate.
    EPUB_UUID = "urn:uuid:" + str(
        uuid.uuid5(uuid.NAMESPACE_URL, f"what-rain-feels-like/{lang}")
    )

    if lang == BASE_LANG:
        CHAPTERS_DIR = ROOT / "chapters"
        MATTER_DIR = ROOT / "book-matter"
    else:
        base = TRANSLATIONS_ROOT / lang
        CHAPTERS_DIR = base / "chapters"
        MATTER_DIR = base / "book-matter"

    # Cover art is per edition — only the text layer changes between languages,
    # but that text is on the artwork. The base edition may keep its files
    # directly in cover/; translations must use cover/<lang>/.
    per_lang = COVER_ROOT / lang
    COVER_DIR = per_lang if per_lang.is_dir() else (COVER_ROOT if lang == BASE_LANG else per_lang)

    COVER_FRONT = COVER_DIR / "front-cover-hires.png"
    COVER_BACK = COVER_DIR / "back-cover-hires.png"
    COVER_SPINE = COVER_DIR / "spine-hires.png"

    # Text-free art — what the lettering is set over. Because the lettering is
    # now typeset at build time rather than painted into the picture, the art
    # carries no language: a translation falls back to the base edition's art
    # and still gets its own title, blurb and spine. Dropping a file into
    # cover/<lang>/ overrides that, for an edition that wants its own image.
    def raw(name: str) -> Path:
        per_edition = COVER_DIR / name
        return per_edition if per_edition.is_file() else COVER_ROOT / name

    COVER_FRONT_RAW = raw("front-cover-raw-hires.png")
    COVER_BACK_RAW = raw("back-cover-raw-hires.png")

    BUILD_DIR = BUILD_ROOT / lang
    OUT_MANUSCRIPT = BUILD_DIR / "manuscript.md"
    OUT_TEXT_DIR = BUILD_DIR / "text"  # clean per-chapter text, for TTS/translation
    OUT_EPUB = BUILD_DIR / f"{SLUG}.epub"
    OUT_INTERIOR = BUILD_DIR / f"{SLUG}_interior.pdf"
    OUT_COVER = BUILD_DIR / f"{SLUG}_cover.pdf"
    OUT_DOCX = BUILD_DIR / f"{SLUG}_manuscript.docx"
    OUT_METADATA = BUILD_DIR / "kdp-metadata.md"


configure()


def paper_thickness() -> float:
    return PAPER_THICKNESS[PAPER]


def spine_width_in(page_count: int) -> float:
    """KDP spine width for a given interior page count."""
    return page_count * paper_thickness()


def full_cover_size_in(page_count: int) -> tuple[float, float]:
    """Wraparound cover dimensions, bleed included."""
    w = 2 * BLEED_IN + 2 * TRIM_W_IN + spine_width_in(page_count)
    h = 2 * BLEED_IN + TRIM_H_IN
    return w, h
