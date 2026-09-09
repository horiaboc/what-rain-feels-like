"""Parse chapters/ and book-matter/ into an in-memory book.

Every renderer consumes the structures built here, so the parsing rules live
in exactly one place.

Chapter file shape (verified across all 55 files):

    # Chapter One: Weichselstraße
    <blank>
    ---                 <- title separator, NOT a scene break; dropped
    <blank>
    body...
    ---                 <- every later rule IS a scene break
    more body...

`chapter-53-document.md` additionally carries in-fiction headings (the
newspaper piece). Those are demoted rather than treated as chapter starts.
"""

from __future__ import annotations

import html as _stdlib_html
import re
from dataclasses import dataclass, field
from pathlib import Path

import markdown as md

from . import config

CHAPTER_RE = re.compile(r"^chapter-(\d+)-([a-z]+)\.md$")
HEADING_RE = re.compile(r"^#\s+(.*)$")
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]{2,}\]")
# Italic guidance notes in book-matter — e.g. *(Optional. One line, centred…)*
GUIDANCE_RE = re.compile(r"^\*\(.*\)\*$", re.S)

# xhtml output, not html: EPUB is XML, and the html serializer emits void
# elements unclosed (`<br>`), which breaks any page using a hard line break.
_MD = md.Markdown(extensions=["smarty"], output_format="xhtml")

# smarty emits named entities (&rsquo;, &mdash;). Those are undefined in XHTML
# without a DTD and make EPUB validators fail, so they are folded to literal
# characters — while the four entities XML actually defines are preserved.
_XML_SAFE = {"&amp;": "\x00A\x00", "&lt;": "\x00L\x00",
             "&gt;": "\x00G\x00", "&quot;": "\x00Q\x00"}


def _literalise_entities(html: str) -> str:
    for ent, tok in _XML_SAFE.items():
        html = html.replace(ent, tok)
    html = _stdlib_html.unescape(html)
    for ent, tok in _XML_SAFE.items():
        html = html.replace(tok, ent)
    return html


def _render_md(text: str) -> str:
    _MD.reset()
    html = _literalise_entities(_MD.convert(text))
    # In-fiction headings inside a chapter body must not compete with the
    # chapter heading itself, so demote them and tag them for styling.
    html = re.sub(r"<h1>(.*?)</h1>", r'<p class="doc-headline">\1</p>', html, flags=re.S)
    html = re.sub(r"<h2>(.*?)</h2>", r'<p class="doc-subhead">\1</p>', html, flags=re.S)
    html = re.sub(r"<h3>(.*?)</h3>", r'<p class="doc-standfirst">\1</p>', html, flags=re.S)
    return html


def _strip_guidance(text: str) -> str:
    """Drop the *(parenthetical editorial notes)* from book-matter pages."""
    blocks = re.split(r"\n\s*\n", text)
    keep = [b for b in blocks if not GUIDANCE_RE.match(b.strip())]
    return "\n\n".join(keep).strip()


def _plain_text(html: str) -> str:
    txt = re.sub(r"<br\s*/?>", "\n", html)
    txt = re.sub(r"</p>", "\n\n", txt)
    txt = re.sub(r"<[^>]+>", "", txt)
    txt = (txt.replace("&#8217;", "’").replace("&#8216;", "‘")
              .replace("&#8220;", "“").replace("&#8221;", "”")
              .replace("&#8212;", "—").replace("&#8230;", "…")
              .replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
              .replace("&nbsp;", " ").replace("&quot;", '"'))
    return re.sub(r"\n{3,}", "\n\n", txt).strip()


@dataclass
class Chapter:
    number: int
    voice: str
    label: str          # "Chapter One"
    title: str          # "Weichselstraße"  (may be "_" or "א")
    scenes: list[str]   # rendered HTML, one entry per scene
    source: Path

    @property
    def slug(self) -> str:
        return f"chapter-{self.number:02d}"

    @property
    def heading_plain(self) -> str:
        return f"{self.label}: {self.title}" if self.title else self.label

    @property
    def text(self) -> str:
        body = f"\n\n{config.SCENE_BREAK}\n\n".join(_plain_text(s) for s in self.scenes)
        return f"{self.heading_plain}\n\n{body}"

    @property
    def word_count(self) -> int:
        return len(" ".join(_plain_text(s) for s in self.scenes).split())


@dataclass
class MatterPage:
    stem: str           # "03-copyright"
    kind: str           # "half-title", "copyright", …
    heading: str
    html: str
    placeholders: list[str] = field(default_factory=list)
    unfilled: bool = False

    @property
    def css_class(self) -> str:
        return f"bm-{self.kind}"


@dataclass
class Book:
    chapters: list[Chapter]
    front: list[MatterPage]
    back: list[MatterPage]

    @property
    def word_count(self) -> int:
        return sum(c.word_count for c in self.chapters)

    def all_placeholders(self) -> list[tuple[str, str]]:
        out = []
        for p in self.front + self.back:
            out.extend((p.stem, ph) for ph in p.placeholders)
        for key in ("AUTHOR_LEGAL", "IMPRINT", "IMPRINT_CITY", "ISBN_PAPERBACK"):
            val = getattr(config, key)
            if PLACEHOLDER_RE.search(val or ""):
                out.append((f"config.{key}", val))
        return out


def parse_chapter(path: Path) -> Chapter:
    m = CHAPTER_RE.match(path.name)
    if not m:
        raise ValueError(f"unexpected chapter filename: {path.name}")
    number, voice = int(m.group(1)), m.group(2)

    raw = path.read_text(encoding="utf-8")
    lines = raw.split("\n")

    hm = HEADING_RE.match(lines[0]) if lines else None
    if not hm:
        raise ValueError(f"{path.name}: expected an '# ' heading on line 1")
    heading = hm.group(1).strip()
    label, _, title = heading.partition(":")
    label, title = label.strip(), title.strip()

    body = "\n".join(lines[1:])

    # Remove the single title separator that follows the heading, then treat
    # each remaining rule as a scene break.
    body = re.sub(r"\A\s*\n?-{3,}\s*\n", "\n", body, count=1)

    segments = [s.strip() for s in re.split(r"^\s*-{3,}\s*$", body, flags=re.M)]
    scenes = [_render_md(s) for s in segments if s]

    return Chapter(number=number, voice=voice, label=label, title=title,
                   scenes=scenes, source=path)


def _matter_kind(stem: str) -> str:
    return re.sub(r"^\d+-", "", stem)


TOKEN_RE = re.compile(r"\{\{([A-Z_]+)\}\}")


def _substitute(text: str) -> str:
    """Replace {{CONFIG_KEY}} tokens with their values from config.py."""
    def repl(m):
        key = m.group(1)
        if not hasattr(config, key):
            raise SystemExit(f"unknown template token {{{{{key}}}}} in book-matter")
        return str(getattr(config, key))
    return TOKEN_RE.sub(repl, text)


def parse_matter(path: Path) -> MatterPage:
    stem = path.stem
    text = _substitute(_strip_guidance(path.read_text(encoding="utf-8")))
    lines = text.split("\n")

    heading = ""
    if lines and lines[0].startswith("# "):
        heading = lines[0][2:].strip()
        text = "\n".join(lines[1:]).strip()

    placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
    # A page whose entire remaining content is placeholder text is not ready to
    # print; the build drops it and says so. A page that is legitimately just a
    # heading (the half-title) is complete, not unfilled.
    if not text.strip():
        unfilled = not heading
    else:
        unfilled = not re.sub(r"[\s*_·—–]", "", PLACEHOLDER_RE.sub("", text))

    return MatterPage(stem=stem, kind=_matter_kind(stem), heading=heading,
                      html=_render_md(text) if text else "",
                      placeholders=placeholders, unfilled=unfilled)


def blurb_blocks() -> list[str]:
    """The back-cover / KDP description copy, as plain paragraphs.

    `blurb.md` is a working document: a heading and a note about what the file
    is, then the copy itself between two `---` rules, then a parenthetical note
    about word count and what the blurb protects. Only the middle section is
    the blurb, and everything downstream — the printed back cover and the KDP
    description — must take it from here so the two cannot drift apart.
    """
    path = config.MATTER_DIR / "blurb.md"
    if not path.is_file():
        return []

    sections = re.split(r"^\s*-{3,}\s*$", path.read_text(encoding="utf-8"), flags=re.M)
    copy = sections[1] if len(sections) > 2 else sections[-1]
    copy = GUIDANCE_RE.sub("", copy)

    blocks = []
    for raw in re.split(r"\n\s*\n", copy):
        block = raw.strip()
        if block and not GUIDANCE_RE.match(block):
            blocks.append(block)
    return blocks


def load_book() -> Book:
    chapter_paths = sorted(
        (p for p in config.CHAPTERS_DIR.glob("chapter-*.md") if CHAPTER_RE.match(p.name)),
        key=lambda p: int(CHAPTER_RE.match(p.name).group(1)),
    )
    if not chapter_paths:
        raise SystemExit(f"no chapters found in {config.CHAPTERS_DIR}")

    chapters = [parse_chapter(p) for p in chapter_paths]

    numbers = [c.number for c in chapters]
    expected = list(range(1, len(numbers) + 1))
    if numbers != expected:
        missing = sorted(set(expected) - set(numbers))
        raise SystemExit(f"chapter numbering is not contiguous; missing/odd: {missing}")

    matter = sorted(config.MATTER_DIR.glob("*.md"))
    front, back = [], []
    for p in matter:
        if p.stem == "README" or p.stem == "blurb":
            continue
        page = parse_matter(p)
        (front if p.stem[0] == "0" else back).append(page)

    return Book(chapters=chapters, front=front, back=back)
