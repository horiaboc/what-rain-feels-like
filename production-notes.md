# Production Notes — Formats, Ebooks & Audiobook

Reference for turning the finished manuscript into distributable formats. Numbers are for the current draft: **~78,700 words ≈ ~450,000 characters ≈ ~8.5 finished audio-hours**.

---

## The build pipeline

Everything publishable is generated from `chapters/` and `book-matter/` by one command. Nothing downstream is edited by hand — edit the chapters, rebuild.

```bash
python3 -m venv .venv                          # once per machine
.venv/bin/pip install -r tools/requirements.txt

.venv/bin/python tools/build.py                # build everything (~16s)
.venv/bin/python tools/build.py --check        # validate only, write nothing
.venv/bin/python tools/build.py --only epub    # a single target
.venv/bin/python tools/build.py --lang de      # a translation
.venv/bin/python tools/build.py --editions     # list what can be built
```

| Output (`build/en/`) | What it's for |
|---|---|
| `manuscript.md` | **The compiled source.** Whole book in one file — the input for translation, voiceover prep and the copyright check |
| `text/*.txt` | Markup-free text, one file per chapter + `full-book.txt` — feedstock for TTS and `tools/plagiarism_check.py` |
| `What-Rain-Feels-Like.epub` | KDP Kindle upload, and Send-to-Kindle |
| `..._interior.pdf` | KDP paperback interior, 6×9, fonts embedded |
| `..._cover.pdf` | KDP paperback wraparound cover, spine sized to the page count |
| `..._cover-proof.png` | The cover with trim, safe area, spine and barcode guides drawn on — check this before uploading |
| `..._manuscript.docx` | Standard manuscript format, for an editor's Track Changes |
| `kdp-metadata.md` | Every KDP form field pre-filled, plus the print spec |

**Publishing decisions live in `tools/bookbuild/config.py`** — metadata, trim size, margins, typography, the scene-break mark. Change it there and every format follows.

**Three front-matter pages are generated, not file-backed:** the half-title and title page are pure layout over values config already holds, and the copyright page is legal boilerplate whose wording lives per language in `tools/bookbuild/boilerplate.py`. That is what lets a translation get a correct rights page in its own language — original title, translator credit, localised edition and format words — without anyone re-deriving it. Languages currently carried: en, de, fr, ro, hu, ru, uk, sr. A language with no entry falls back to English and `--check` reports it as a blocker. Dropping a `03-copyright.md` into an edition's `book-matter/` overrides the generated page.

### One folder per edition

The build is per-language and always has been scoped that way, so translations never collide:

```
chapters/  book-matter/  cover/          English sources (base edition)
translations/de/chapters/               German sources
translations/de/book-matter/
cover/de/                               German cover art
build/en/   build/de/   …               outputs, one folder per edition
```

Each edition carries its own title, subtitle, locale, filename slug, cover art, ISBN and EPUB identifier (derived per language, so a translation is a distinct book in a reader's library rather than a duplicate). The physical specification — trim, margins, fonts — and the `_horia` byline are shared.

**Adding a translation is one entry in `EDITIONS` plus a `translations/<lang>/` directory.** No renderer changes. A commented German entry is already in `config.py` as the template; this was verified end-to-end with a throwaway German edition.

### Cover lettering is typeset, not painted

`cover/` holds two versions of each panel: `*-raw-hires.png`, the generated art
with no lettering anywhere, and `*-hires.png`, the same art with text burned in
by a scratch session that cannot be re-run. The burned-in set is kept only for
reference — it puts the back-cover byline into KDP's barcode block, sets the
spine for a width the book no longer has, and quotes a blurb that has since
drifted from `book-matter/blurb.md`.

`tools/bookbuild/covertext.py` sets the type at build time over the raw art
instead, in EB Garamond, with the palette sampled from the picture. That makes
three things true that were not before:

- **Nothing can collide with the barcode.** The keep-out box is the same
  constant the proof draws, and the back panel lays itself out above it — the
  blurb shrinks a step at a time until the whole block fits.
- **The spine follows the page count.** It is cut from the front art's inner
  edge and lettered to the current width; below 79 pages it is left blank,
  which is KDP's own rule.
- **A translation needs no new artwork.** The art carries no words, so an
  edition with nothing in `cover/<lang>/` falls back to the base art and still
  gets its own title, spine and blurb. Drop files into `cover/<lang>/` only if
  that edition wants a different picture.

Set `config.COVER_TEXT = "baked"` to build from the old burned-in files instead.

### Order dependency that matters

The spine width is the page count × paper thickness, so **the cover cannot be built until the interior is**. `build.py` enforces this: asking for a cover builds the interior first. Any edit that changes the page count changes the spine, so interior and cover must be re-uploaded together.

### Typography

Set in **EB Garamond** (OFL), vendored under `assets/fonts/` as static instances cut from the variable font, so builds are reproducible and don't depend on system fonts. EB Garamond has no Hebrew, so a subsetted Frank Ruhl Libre carries the single א (the ch38 title) as a per-glyph CSS fallback.

Two WeasyPrint constraints shaped the print stylesheet, both verified by experiment rather than assumed:
- `@page name:first` is **not** scoped per named-page group, so running heads are suppressed on chapter-opening pages via `string(runrecto, first-except)` instead.
- Element-level `counter-reset: page` is ignored, so front matter and body are rendered as two PDFs and concatenated. That is what lets the story open on folio 1 with the front matter unnumbered.
- **`@font-face` `src` URLs resolve against the stylesheet's own base URL, not the document's.** A `CSS(string=…)` built without `base_url` drops every `@font-face` rule — with only a warning — and falls back to the system serif. On a machine whose fallback serif has no installed italic, that also silently kills every italic in the book. Both `pdf.py` and `chapter_pdf.py` now pass `base_url`. Verified by rendering pages, not by trusting the absence of an error. (This is what put the interior at 327 pages until 2026-09-07; in real EB Garamond it is 271.)

---

## Ebook formats

| Format | File | Reads on | How it's built |
|---|---|---|---|
| **EPUB** | `build/What-Rain-Feels-Like.epub` | Apple Books (native); KDP upload; Send-to-Kindle | `tools/build.py` — hand-rolled EPUB3: 55 chapters, cover, nav + ncx TOC, embedded fonts, real א glyph |
| **AZW3** | — | e-ink Kindle over USB; Kindle for PC/Mac | `ebook-convert build/What-Rain-Feels-Like.epub out.azw3 --output-profile kindle_pw3` (calibre 9.2.1) |
| **PDF (print)** | `build/..._interior.pdf` | KDP paperback interior | `tools/build.py` — WeasyPrint, 6×9, EB Garamond embedded |

*Superseded:* the loose `What-Rain-Feels-Like.*` files in the repo root are pre-pipeline artifacts built by scratchpad scripts that no longer exist. They are git-ignored and can be deleted; `build/` replaces them.

### Kindle: how a personal book actually gets there
Amazon's own path for personal manuscripts is **Send to Kindle** (send-to-kindle.amazon.com, or email to your @kindle.com address). **Upload the EPUB, not the AZW3** — Amazon converts the EPUB to its proprietary format server-side, and it then appears in the Kindle app and on devices as a native Kindle book (fonts, layout, reading-position sync). The AZW3 file is only for sideloading an e-ink Kindle by cable, or Kindle for PC/Mac. The mobile Kindle **app cannot import AZW3 directly** — that's why EPUB→Send-to-Kindle is the route for phones/tablets.

Apple Books: open/AirDrop the **EPUB** — native, and the א renders as a real glyph.

---

## Audiobook

### Whispersync (ebook↔audio position sync)
Only exists for **Kindle-store + Audible purchases**. No personal-document format (EPUB/AZW3 included) can get it. Workaround for a personal audiobook: **one MP3 per chapter** so finding your place is trivial.

### Single vs multi-voice — the industry norm
- **~85–90% of audiobooks are single-narrator**: one reader performs everyone via subtle pitch/accent/pace shifts. Most cohesive; what listeners expect.
- **Dual / "duet" narration** (a male + female voice splitting alternating first-person POVs) is standard in romance/YA — and *fits this book's Jonas/Iris/ALEPH structure*, so it's a legitimate, non-weird choice here.
- **Full cast** (every speaking character voiced) is rare, drifts toward audio-drama, and is a lot more production work.

Voices this book would need (by narrator): **Jonas** 23ch (male, British, warm, 30s), **Iris** 19ch (female, British, mid-20s), **ALEPH** 5ch (*neither male nor female* per bible — hardest to cast), **Conrad** 3ch (male, older, 60s), **Mara** 2ch (female, cooler than Iris), **neutral+article** 3ch (plain narrator). → ~5–6 distinct voices.

### Can AI do the professional intonation-based character differentiation?
Not automatically — standard TTS reads everything in one register. But the top engines are **steerable/directable**:
- **ElevenLabs v3** — inline **audio tags** (`[whispers]`, `[sighs]`, emphasis) change delivery per line; best expressive long-form.
- **OpenAI `gpt-4o-mini-tts`** — **plain-English style instructions** per passage ("warm, dry, older man"); one base voice bends into characters.
- **Azure** — preset speaking styles (calm/sad/cheerful/whispering) via markup.

The real workflow = a **"direction" pass**: mark up dialogue/emotion per passage, then render. Model supplies the voice; you supply the acting notes. Gets impressively close line-by-line; still short of a top human narrator sustaining a cast over hours.

### AI TTS quality & cost — for THIS book (~450k chars)
| Engine | Quality | Whole-book cost |
|---|---|---|
| **ElevenLabs** (v3) | **Best** intonation; British voices; androgynous option for ALEPH; multilingual keeps one voice identity across ~30 languages (good for future translations) | ~**$99** (one month Pro ≈ 500k credits, then cancel) |
| **OpenAI** `gpt-4o-mini-tts` | Very good; instructable per-passage | ~**$7–15** |
| **Azure** neural | Good; many en-GB voices; less "acting" | ~**$7, often effectively free** (Azure grants ~500k chars/month free) |

**Recommendation:** best single-narrator = **ElevenLabs** (~$99 one-off). Value pick = **OpenAI ~$10**. Near-free = **Azure**. Test voices in-browser before buying: ElevenLabs Voice Library, Azure Speech Studio, OpenAI playground.

### Real human narrator — for THIS book (~8.5 finished hrs)
Priced per finished hour (PFH):
- Budget/newer pro (~$150/hr): **~$1,300**
- Solid professional (~$300–400/hr): **~$2,500–3,400**
- Top-tier/name ($600–1,000+/hr): **~$5,000–8,500**
- **$0 upfront option:** ACX **royalty-share** — narrator takes a cut of sales instead of a fee.

**Bottom line:** whole book AI-narrated = **free to ~$100** one-time; a good human narrator = **~$1,300–3,500**. Common path for a debut: start with AI, commission a human only if the book finds an audience.

### Free pipeline (proven on monkey)
- **Piper** (local, free forever): `en_US-lessac-medium` (flat/robotic), `en_GB-cori-high` (warmer British). Slow (~book = ~19h compute).
- **edge-tts** (free MS neural, needs network; installed in a scratchpad venv): `en-GB-SoniaNeural` etc. — much more natural; whole book ≈ ~2h compute, $0. Best free option for a draft audiobook.
- Encode WAV→MP3 with `ffmpeg` (present). Delivered ch01 samples in lessac, Sonia, Cori.

---

## Editor deliverable
- **DOCX** (`What-Rain-Feels-Like_EDITOR.docx`) — standard manuscript format (cover on page 1, 12pt Times New Roman, double-spaced, chapters on new pages), for Word Track Changes/comments or Google Docs (upload → open as Google Doc → Suggesting mode). Built hand-rolled from the chapters.
- A4 draft PDF also exists for print markup (2-up).

*Last updated: 2026-07-19*

## Author name (decided)
Publish as the mononym **`_horia`** — stylized with a leading underscore, echoing the book's cursor motif (ch23 `_`). Underscore is a **cover/art treatment**; retail metadata registers as **Horia** (searchable); legal name only on the copyright page. Stays `_horia` across all languages/marketplaces. See `back-cover.md`, `book-matter/`.
