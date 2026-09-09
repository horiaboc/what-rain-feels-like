"""Wraparound print cover for KDP, plus an annotated proof.

KDP takes the paperback cover as a single PDF containing back panel, spine and
front panel side by side, with 0.125" bleed on all four sides. The spine width
is a function of the interior page count, so this module cannot run until the
interior PDF exists.

`build_cover` also writes a proof PNG with trim lines, safe margins, the spine
boundaries and the ISBN barcode keep-out box drawn on top. The PDF is what you
upload; the proof is what you look at.
"""

from __future__ import annotations

from PIL import Image, ImageDraw

from . import config as c, covertext

# KDP prints the ISBN barcode into the lower-right of the back panel. It is
# 2" x 1.2" and sits 0.25" in from the trim edges; anything underneath it is
# covered up.
BARCODE_W_IN, BARCODE_H_IN = 2.0, 1.2
BARCODE_INSET_IN = 0.25
# KDP's recommended keep-out for live text, measured in from the trim edge.
SAFE_IN = 0.25


def _fit(im: Image.Image, w: int, h: int) -> Image.Image:
    """Scale to cover w×h, preserving aspect, then centre-crop the overflow."""
    scale = max(w / im.width, h / im.height)
    resized = im.resize((max(w, round(im.width * scale)), max(h, round(im.height * scale))),
                        Image.LANCZOS)
    left = (resized.width - w) // 2
    top = (resized.height - h) // 2
    return resized.crop((left, top, left + w, top + h))


def _px(inches: float) -> int:
    return round(inches * c.COVER_DPI)


def build_cover(page_count: int) -> dict:
    c.BUILD_DIR.mkdir(parents=True, exist_ok=True)

    spine_in = c.spine_width_in(page_count)
    total_w_in, total_h_in = c.full_cover_size_in(page_count)

    total_w, total_h = _px(total_w_in), _px(total_h_in)
    panel_w = _px(c.BLEED_IN + c.TRIM_W_IN)  # a panel plus its outer bleed
    spine_w = total_w - 2 * panel_w

    if c.COVER_TEXT == "generated":
        back = covertext.render_back(panel_w, total_h)
        spine = covertext.render_spine(spine_w, total_h, page_count)
        front = covertext.render_front(panel_w, total_h)
    else:
        back = _fit(Image.open(c.COVER_BACK).convert("RGB"), panel_w, total_h)
        spine = _fit(Image.open(c.COVER_SPINE).convert("RGB"), spine_w, total_h)
        front = _fit(Image.open(c.COVER_FRONT).convert("RGB"), panel_w, total_h)

    canvas = Image.new("RGB", (total_w, total_h), "black")
    canvas.paste(back, (0, 0))
    canvas.paste(spine, (panel_w, 0))
    canvas.paste(front, (panel_w + spine_w, 0))

    canvas.save(c.OUT_COVER, "PDF", resolution=float(c.COVER_DPI))

    _write_proof(canvas.copy(), panel_w, spine_w, total_w, total_h)

    return {
        "page_count": page_count,
        "spine_in": spine_in,
        "cover_w_in": total_w_in,
        "cover_h_in": total_h_in,
        "cover_w_px": total_w,
        "cover_h_px": total_h,
        "spine_px": spine_w,
    }


def _write_proof(img: Image.Image, panel_w: int, spine_w: int, total_w: int, total_h: int) -> None:
    """Overlay trim, safe-area, spine and barcode guides for visual checking."""
    d = ImageDraw.Draw(img, "RGBA")
    bleed = _px(c.BLEED_IN)
    safe = bleed + _px(SAFE_IN)

    # Trim box (what actually survives the guillotine).
    d.rectangle([bleed, bleed, total_w - bleed - 1, total_h - bleed - 1],
                outline=(255, 60, 60, 255), width=6)
    # Safe area for live text.
    d.rectangle([safe, safe, total_w - safe - 1, total_h - safe - 1],
                outline=(80, 255, 120, 200), width=4)
    # Spine boundaries.
    for x in (panel_w, panel_w + spine_w):
        d.line([(x, 0), (x, total_h)], fill=(90, 190, 255, 255), width=5)

    # Barcode keep-out, lower right of the back panel (the back panel is on the
    # left of a wraparound cover).
    bx2 = bleed + _px(c.TRIM_W_IN - BARCODE_INSET_IN)
    bx1 = bx2 - _px(BARCODE_W_IN)
    by2 = total_h - bleed - _px(BARCODE_INSET_IN)
    by1 = by2 - _px(BARCODE_H_IN)
    d.rectangle([bx1, by1, bx2, by2], fill=(255, 255, 255, 110),
                outline=(255, 210, 0, 255), width=6)
    d.text((bx1 + 24, by1 + 20), "ISBN BARCODE\n(KDP prints here)", fill=(255, 230, 0, 255))

    proof = c.BUILD_DIR / f"{c.SLUG}_cover-proof.png"
    img.thumbnail((2400, 2400), Image.LANCZOS)
    img.save(proof)
