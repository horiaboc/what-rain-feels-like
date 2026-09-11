"""Typeset the cover text onto the raw art.

`cover/` carries two versions of each panel: `*-raw-hires.png` (the generated
art, no lettering anywhere) and `*-hires.png` (the same art with text already
burned in). The burned-in versions came out of a scratch session and cannot be
regenerated or corrected — the back-cover text collides with KDP's barcode
zone, the spine was set for a spine width the book no longer has, and the blurb
on it has drifted from `book-matter/blurb.md`.

So the text is set here instead, at build time, over the raw art:

* the barcode keep-out and the safe margins are the same constants the proof
  draws, so text cannot collide with them by construction;
* the spine is typeset to whatever width the current page count implies;
* the wording comes from the same sources as everything else — the title from
  config, the blurb from `book-matter/blurb.md` — so it cannot drift;
* a translation gets a cover by supplying raw art and its own blurb, with no
  image model asked to render words in a language it will misspell.

Type is EB Garamond, the book's own face. The palette is sampled from the art
rather than hardcoded, so a different edition's art carries its own colour.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from . import config as c
from .sources import blurb_blocks

# KDP's barcode block and live-text margin, in inches. Kept in sync with
# cover.py, which draws these same boxes on the proof.
BARCODE_W_IN, BARCODE_H_IN = 2.0, 1.2
BARCODE_INSET_IN = 0.25
SAFE_IN = 0.25
# KDP wants spine text no closer than this to either spine fold.
SPINE_SAFE_IN = 0.0625

REGULAR = "EBGaramond-Regular.ttf"
ITALIC = "EBGaramond-Italic.ttf"
BOLD = "EBGaramond-Bold.ttf"


def _px(inches: float) -> int:
    return round(inches * c.COVER_DPI)


def _font(name: str, size_px: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(c.FONTS_DIR / name), size_px)


@dataclass
class Palette:
    ink: tuple[int, int, int]      # the lettering
    body: tuple[int, int, int]     # back-panel copy — a step more saturated
    warm: tuple[int, int, int]     # the amber foot of a display gradient
    shade: tuple[int, int, int]    # the shadow under it


# Lettering colours measured off the approved covers: the title fill, the amber
# at the foot of the glyphs, and the more saturated gold of the back-panel copy.
# Gold on a blue-and-amber ground is what carries; a pale cream washes out
# against the bright horizon.
INK_GOLD = (252, 213, 141)
WARM_GOLD = (226, 166, 82)
BODY_GOLD = (254, 222, 109)

# How much of the art's own highlight hue survives the pull toward those golds.
# Enough that a differently-coloured edition's art still tints its lettering;
# not so much that the letters stop reading as gold.
ART_TINT = 0.30


def _palette(art: Image.Image) -> Palette:
    """Gold lettering, tinted by the art's own highlights.

    Taking the hue from the picture keeps the type part of the image, but left
    to itself it drifts pale — and pale type dies on the bright horizon that
    runs across both panels. So the sampled colour is pulled most of the way
    toward the golds measured off the approved covers.
    """
    small = art.convert("RGB").resize((64, 96), Image.LANCZOS)
    pixels = list(small.getdata())
    brightest = sorted(pixels, key=sum)[-len(pixels) // 12:]
    sampled = tuple(sum(p[i] for p in brightest) // len(brightest) for i in range(3))

    def toward(target: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(min(255, max(0, round(t + (s - t) * ART_TINT)))
                     for t, s in zip(target, sampled))

    return Palette(ink=toward(INK_GOLD), body=toward(BODY_GOLD),
                   warm=toward(WARM_GOLD), shade=(10, 16, 28))


def _draw_text(base: Image.Image, xy, text, font, palette: Palette,
               anchor="mm", blur: int = 9, offset: int = 5) -> None:
    """Draw text with a soft drop shadow so it survives a busy background."""
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).text((xy[0] + offset, xy[1] + offset), text, font=font,
                                fill=palette.shade + (190,), anchor=anchor)
    base.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(base).text(xy, text, font=font, fill=palette.ink + (255,), anchor=anchor)


def _draw_display_text(base: Image.Image, xy, text, font, palette: Palette,
                       anchor="mm", blur: int = 13, offset: int = 9) -> None:
    """Title lettering: cream at the top of each glyph, amber at the foot.

    The approved art lights the title as if the sunrise behind it were catching
    the bottom of the letters. A flat fill loses that and reads as a caption
    dropped on a painting, so the fill is a vertical gradient between the
    palette's pale and warm ends.
    """
    box = font.getbbox(text)
    w, h = box[2] - box[0], box[3] - box[1]
    if w <= 0 or h <= 0:
        return

    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).text((xy[0] + offset, xy[1] + offset), text, font=font,
                                fill=palette.shade + (240,), anchor=anchor)
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    # Twice, so the shadow reads as depth under the letter rather than haze.
    base.alpha_composite(shadow)
    base.alpha_composite(shadow)

    mask = Image.new("L", base.size, 0)
    ImageDraw.Draw(mask).text(xy, text, font=font, fill=255, anchor=anchor)

    top, bottom = palette.ink, palette.warm
    gradient = Image.new("RGB", (1, max(2, h)))
    for y in range(gradient.height):
        t = y / (gradient.height - 1)
        # Hold the pale colour through the upper half, then fall to amber.
        k = max(0.0, (t - 0.42) / 0.58) ** 1.25
        gradient.putpixel((0, y), tuple(round(a + (b - a) * k) for a, b in zip(top, bottom)))

    fill = Image.new("RGB", base.size)
    y0 = mask.getbbox()[1] if mask.getbbox() else 0
    fill.paste(gradient.resize((base.width, gradient.height), Image.BILINEAR), (0, y0))
    base.paste(fill, (0, 0), mask)


def _cap_font(name: str, cap_px: int) -> ImageFont.FreeTypeFont:
    """A font whose capital letters stand `cap_px` tall.

    Point size is not a usable unit for cover layout — two faces at the same
    size have different cap heights. Measuring a capital and scaling makes the
    geometry constants below mean the same thing whatever face is vendored.
    """
    probe = _font(name, 200)
    box = probe.getbbox("H")
    measured = box[3] - box[1]
    return _font(name, max(8, round(200 * cap_px / measured)))


def _fit_width(text: str, name: str, target_w: int, start: int) -> ImageFont.FreeTypeFont:
    """Largest size at or below `start` whose rendered width fits `target_w`."""
    size = start
    while size > 12:
        f = _font(name, size)
        if f.getbbox(text)[2] - f.getbbox(text)[0] <= target_w:
            return f
        size -= 2
    return _font(name, 12)


# ─────────────────────────────────────────────────────────────────────────────
# Front panel
# ─────────────────────────────────────────────────────────────────────────────

def _title_lines(title: str) -> list[str]:
    """Break the title for the cover stack.

    The approved art set it as three lines with the middle one largest. That
    only works for a title that breaks three ways; anything else falls back to
    an even two- or one-line stack.
    """
    if getattr(c, "TITLE_LINES", None):
        return list(c.TITLE_LINES)
    words = title.split()
    if len(words) == 4:
        return [words[0], words[1], " ".join(words[2:])]
    if len(words) == 3:
        return words
    if len(words) > 4:
        mid = len(words) // 2
        return [" ".join(words[:mid]), " ".join(words[mid:])]
    return [title]


# Geometry measured off the approved front cover, as fractions of the panel.
# The title sits in the clear sky above the two figures; going any larger or
# any lower runs the last line into them, which is what pinned these numbers.
TITLE_TOP = 0.170          # top of the first line's cap height
DISPLAY_CAP = 0.088        # cap height of the largest line
LINE_STEP = 1.30           # baseline-to-baseline, as a multiple of cap height
TITLE_MAX_W = 0.56         # widest line, as a fraction of panel width
BYLINE_UP_IN = 0.60        # byline centre, measured up from the trimmed foot


def render_front(panel_w: int, panel_h: int) -> Image.Image:
    art = _load(c.COVER_FRONT_RAW, panel_w, panel_h)
    pal = _palette(art)
    canvas = art.convert("RGBA")

    safe_x = _px(c.BLEED_IN + SAFE_IN)
    text_w = panel_w - 2 * safe_x

    lines = _title_lines(c.TITLE)
    # The middle line of a three-line stack is the display line; the others sit
    # a step below it. A one- or two-line title is set evenly.
    weights = [0.76, 1.0, 0.72] if len(lines) == 3 else [1.0] * len(lines)

    # Size from cap height so the stack keeps the approved proportions, then
    # step down if a long line (or a translated title) overruns the margin.
    cap = round(panel_h * DISPLAY_CAP)
    while cap > 24:
        fonts = [_cap_font(BOLD, round(cap * w)) for w in weights]
        widest = max(f.getbbox(ln)[2] - f.getbbox(ln)[0] for ln, f in zip(lines, fonts))
        if widest <= min(text_w, round(panel_w * TITLE_MAX_W)):
            break
        cap -= 4

    # Centre each line on its own cap height, and step by the mean of this
    # line's and the next line's, so a big line is not crowded by a small one.
    y = round(panel_h * TITLE_TOP + cap * weights[0] * 0.5)
    for i, (ln, f) in enumerate(zip(lines, fonts)):
        _draw_display_text(canvas, (panel_w // 2, y), ln, f, pal)
        if i + 1 < len(lines):
            y += round(cap * LINE_STEP * (weights[i] + weights[i + 1]) / 2)

    byline = f"{c.BYLINE_PREFIX} {c.AUTHOR_DISPLAY}"
    bf = _fit_width(byline, REGULAR, round(text_w * 0.55), round(panel_h * 0.030))
    _draw_over(canvas, art, (panel_w // 2, panel_h - _px(c.BLEED_IN + BYLINE_UP_IN)),
               byline, bf, pal)

    return canvas.convert("RGB")


# ─────────────────────────────────────────────────────────────────────────────
# Back panel
# ─────────────────────────────────────────────────────────────────────────────

# Back-panel geometry, as fractions of the panel.
BLURB_TOP = 0.135          # first baseline
BLURB_SHADOW = 1.6         # the back panel carries a paragraph of small type
                           # over cloud and water — it needs more behind it
                           # than a single display line on the front does
BLURB_MEASURE = 0.71       # column width. Not the full safe width: at this
                           # size that ran to 77 characters a line, above the
                           # 60-70 the eye tracks comfortably.


def _tagline_font(tagline: str, width: int, start: int) -> ImageFont.FreeTypeFont:
    """Largest size that keeps the tagline to two lines or fewer.

    The tagline is the one line doing the selling, and the approved art gave it
    two generous lines rather than one small one. Fitting it to a single line
    would shrink it to the size of the blurb and lose that.
    """
    size = start
    while size > 16:
        f = _font(REGULAR, size)
        if len(_wrap(tagline, f, width)) <= 2:
            return f
        size -= 2
    return _font(REGULAR, 16)


def _blurb_parts() -> tuple[str, list[str], str]:
    """(tagline, body paragraphs, closing line) from book-matter/blurb.md.

    The blurb's own shape carries the roles: the first block is the tagline
    (bold in the source), the last is the closing line naming the book (it
    opens with the title, italicised), and what lies between is the body.
    """
    blocks = blurb_blocks()
    if not blocks:
        return ("", [], "")

    def plain(block: str) -> str:
        text = re.sub(r"[*_]", "", block).replace("\n", " ").strip()
        return _smart_quotes(text)

    tagline = plain(blocks[0])
    rest = [plain(b) for b in blocks[1:]]

    closing = ""
    if rest and (rest[-1].startswith(c.TITLE)
                 or rest[-1].startswith(c.EDITIONS[c.BASE_LANG]["title"])):
        closing = rest.pop()
    return tagline, rest, closing


def _mean_luma(art: Image.Image, box: tuple[int, int, int, int]) -> float:
    """Average brightness of the art under a text box."""
    x1, y1, x2, y2 = (max(0, box[0]), max(0, box[1]),
                      min(art.width, box[2]), min(art.height, box[3]))
    if x2 <= x1 or y2 <= y1:
        return 128.0
    patch = art.convert("L").crop((x1, y1, x2, y2)).resize((24, 8), Image.BILINEAR)
    data = list(patch.getdata())
    return sum(data) / len(data)


def _draw_over(base: Image.Image, art: Image.Image, xy, text, font, palette: Palette,
               anchor="mm", ink: tuple[int, int, int] | None = None,
               weight: float = 1.0) -> None:
    """Draw pale text, with the halo behind it sized to the ground it sits on.

    Cream lettering disappears on the bright column of the sun's reflection.
    Rather than move the text somewhere duller, the shadow behind it is
    measured against the art and thickened where the background is light, so
    the same line stays readable wherever the layout puts it.
    """
    box = font.getbbox(text)
    w, h = box[2] - box[0], box[3] - box[1]
    x1 = xy[0] if anchor.startswith("l") else xy[0] - w // 2
    luma = _mean_luma(art, (x1, xy[1] - h, x1 + w, xy[1] + h))

    # 0 on a dark ground, 1 on a bright one.
    lift = min(1.0, max(0.0, (luma - 95) / 90))
    halo = Image.new("RGBA", base.size, (0, 0, 0, 0))
    alpha = min(255, round((175 + 80 * lift) * weight))
    ImageDraw.Draw(halo).text(xy, text, font=font,
                              fill=palette.shade + (alpha,), anchor=anchor)
    halo = halo.filter(ImageFilter.GaussianBlur(round(h * (0.24 + 0.45 * lift)) or 1))
    for _ in range(round((2 + 2 * lift) * weight)):
        base.alpha_composite(halo)

    ImageDraw.Draw(base).text(xy, text, font=font,
                              fill=(ink or palette.ink) + (255,), anchor=anchor)


def _smart_quotes(text: str) -> str:
    """Typographic punctuation for cover copy.

    Interior text gets this from the Markdown renderer's smartypants pass; the
    cover is drawn straight onto pixels and would otherwise print the typewriter
    apostrophes that sit in `blurb.md`.
    """
    text = re.sub(r"(?<=\w)'(?=\w)", "’", text)          # don't, Iris's
    text = re.sub(r"'(?=\w)", "‘", text)                  # opening single
    text = text.replace("'", "’")                         # anything left
    text = re.sub(r'"(?=\w)', "“", text)
    text = text.replace('"', "”")
    return text


def _wrap(text: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if font.getbbox(trial)[2] - font.getbbox(trial)[0] <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def render_back(panel_w: int, panel_h: int) -> Image.Image:
    art = _load(c.COVER_BACK_RAW, panel_w, panel_h)
    pal = _palette(art)
    canvas = art.convert("RGBA")

    bleed = _px(c.BLEED_IN)
    safe = bleed + _px(SAFE_IN)
    # A blurb set to the full safe width is an uncomfortable measure at this
    # size — the printed back cover reads better with the column pulled in.
    text_w = round(panel_w * BLURB_MEASURE)

    # Everything must finish above the barcode block, not merely miss it
    # horizontally — a line of text ending level with a barcode reads as a
    # mistake even when nothing overlaps.
    floor_y = panel_h - bleed - _px(BARCODE_INSET_IN + BARCODE_H_IN) - _px(0.22)

    tagline, paragraphs, closing = _blurb_parts()

    body_f = _font(REGULAR, 50)
    lead = round(body_f.size * 1.42)

    def block_height() -> tuple[int, list]:
        """Lay the whole block out at the current body size; return its height.

        Items are (text, font, step, align). The tagline and the closing line
        are display lines and sit centred; the blurb paragraphs are set flush
        left. Centring a multi-line paragraph gives the eye no fixed left edge
        to return to, which is why the approved art set the body ranged left.
        """
        tag_f = _tagline_font(tagline, text_w, round(body_f.size * 2.2))
        items, h = [], 0
        for ln in _wrap(tagline, tag_f, text_w):
            items.append((ln, tag_f, round(tag_f.size * 1.22), "center"))
            h += round(tag_f.size * 1.22)
        h += round(body_f.size * 1.15)
        for para in paragraphs:
            for ln in _wrap(para, body_f, text_w):
                items.append((ln, body_f, lead, "left"))
                h += lead
            items.append((None, None, round(lead * 0.60), "left"))
            h += round(lead * 0.60)
        if closing:
            close_f = _font(ITALIC, body_f.size)
            for ln in _wrap(closing, close_f, round(text_w * 0.90)):
                items.append((ln, close_f, lead, "center"))
                h += lead
        return h, items

    # Shrink the body until tagline, blurb and byline all clear the barcode.
    byline = f"{c.BYLINE_PREFIX} {c.AUTHOR_DISPLAY}"
    while body_f.size > 26:
        height, items = block_height()
        by_f = _font(REGULAR, round(body_f.size * 1.5))
        needed = height + round(by_f.size * 2.8)
        if round(panel_h * BLURB_TOP) + needed <= floor_y:
            break
        body_f = _font(REGULAR, body_f.size - 2)
        lead = round(body_f.size * 1.42)

    height, items = block_height()
    by_f = _font(REGULAR, round(body_f.size * 1.5))

    # The copy hangs from the top, as on the approved art; the byline sits at
    # the foot of the space the barcode leaves, not adrift in the middle of it.
    y = round(panel_h * BLURB_TOP)
    left_x = (panel_w - text_w) // 2
    for text, font, step, align in items:
        if text is not None:
            x = left_x if align == "left" else panel_w // 2
            _draw_over(canvas, art, (x, y), text, font, pal,
                       anchor="lm" if align == "left" else "mm",
                       ink=pal.body, weight=BLURB_SHADOW)
        y += step

    if not c.COVER_BACK_BYLINE:
        return canvas.convert("RGB")

    # Among the positions the barcode leaves free, prefer the darkest ground —
    # then let the halo make up whatever contrast is still missing.
    lowest = y + round(by_f.size * 1.8)
    highest = floor_y - round(by_f.size * 0.9)
    span = max(0, highest - lowest)
    candidates = [lowest + round(span * t / 6) for t in range(7)] if span else [lowest]
    bw = by_f.getbbox(byline)[2] - by_f.getbbox(byline)[0]
    byline_y = min(candidates, key=lambda cy: _mean_luma(
        art, (panel_w // 2 - bw // 2, cy - by_f.size, panel_w // 2 + bw // 2, cy + by_f.size)))

    _draw_over(canvas, art, (panel_w // 2, byline_y), byline, by_f, pal,
               ink=pal.body, weight=BLURB_SHADOW)

    return canvas.convert("RGB")


# ─────────────────────────────────────────────────────────────────────────────
# Spine
# ─────────────────────────────────────────────────────────────────────────────

# KDP will not print spine text on a book thinner than this.
SPINE_TEXT_MIN_PAGES = 79


def render_spine(spine_w: int, panel_h: int, page_count: int) -> Image.Image:
    """Spine art carried over from the front panel, with the text set to width.

    There is no text-free spine art in `cover/`, and the spine width now moves
    with the page count, so the panel is cut from the front cover's inner edge
    — which is what physically continues around the fold anyway.
    """
    front = _load(c.COVER_FRONT_RAW, _px(c.BLEED_IN + c.TRIM_W_IN), panel_h)
    strip = front.crop((0, 0, min(spine_w, front.width), panel_h))
    pal = _palette(front)

    if page_count < SPINE_TEXT_MIN_PAGES:
        # Too thin to letter — KDP rejects spine text below this, and at this
        # width it would be unreadable anyway.
        return strip.convert("RGB")

    # Set the text horizontally on a rotated canvas, then turn it upright, so
    # the type is laid out in its natural orientation.
    flat = Image.new("RGBA", (panel_h, spine_w), (0, 0, 0, 0))

    usable = spine_w - 2 * _px(SPINE_SAFE_IN)
    run = panel_h - 2 * _px(c.BLEED_IN + 0.5)

    title_f = _fit_width(c.TITLE, BOLD, round(run * 0.72), max(24, round(usable * 0.62)))
    by_f = _font(REGULAR, max(18, round(title_f.size * 0.62)))

    mid = spine_w // 2
    _draw_text(flat, (round(panel_h * 0.42), mid), c.TITLE, title_f, pal, blur=6, offset=3)
    _draw_text(flat, (panel_h - _px(c.BLEED_IN + 0.75), mid), c.AUTHOR_DISPLAY, by_f, pal,
               blur=6, offset=3)

    # Spine text on an English-language book reads top-to-bottom.
    canvas = strip.convert("RGBA")
    canvas.alpha_composite(flat.rotate(-90, expand=True))
    return canvas.convert("RGB")


def _load(path: Path, w: int, h: int) -> Image.Image:
    if not path.is_file():
        raise SystemExit(
            f"missing cover art: {path.relative_to(c.ROOT)}\n"
            f"Each edition needs text-free art at cover/<lang>/ (see production-notes.md)."
        )
    im = Image.open(path).convert("RGB")
    scale = max(w / im.width, h / im.height)
    im = im.resize((max(w, round(im.width * scale)), max(h, round(im.height * scale))),
                   Image.LANCZOS)
    left, top = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((left, top, left + w, top + h))
