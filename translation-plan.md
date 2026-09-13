# Translation Plan

Approach and priorities for foreign-language editions of *What Rain Feels Like*. The English edition is published (2026-09-10). The German (v3), Romanian (v2), Hungarian (v1), French (v1) and Russian (v1) editions are complete — 55 chapters and the book-matter each — built as EPUBs (`build/de/`, `build/ro/`) and with their native readers. This file is the roadmap for that review and for the languages after it.

## Standing decisions
- **Pen name stays `_horia`** across every language and marketplace — a mononym travels well and keeps the author brand unified worldwide.
- **Method: AI-assisted translation + native-speaker human review.** Draft each edition with a strong LLM translator, then have a native reader (the user has volunteers) review and correct for voice, nuance, and the book's buried devices. *Literary fiction is the hardest text to translate* — the three-voice architecture, the cursor/underscore motif, "petrichor," and the seeded echoes must survive. AI draft alone is not enough; the human pass is mandatory.
- Each translated edition = its own KDP listing in that marketplace, same royalty structure (see `pricing-notes.md`).

## Priority order (by return on effort)
1. **German** — highest priority. The novel is *set in Berlin* (and the Dutch Limburg/Amsterdam scenes are next door); a Berlin-set literary novel in German has a built-in hook. Germany is also Amazon's second-largest market. Note: German-language editions are subject to **Buchpreisbindung** (fixed book-price law) — set one price and hold it; KDP accommodates this.
2. **French / Spanish / Italian** — large Amazon marketplaces with real literary-SF audiences; pure scale plays. Do in whatever order the review help is available.
3. **Dutch** — small market and Dutch readers often read in English, but the Amsterdam/Maastricht/Heerlen setting resonates strongly; a niche but thematically fitting edition.
4. **Romanian** — the author's home market; small, but natural and personally meaningful.

## How a translation is wired into the build

The build pipeline is per-edition (see `production-notes.md`). To start a language:

1. Add an entry to `EDITIONS` in `tools/bookbuild/config.py` — name, locale, title, subtitle, filename slug, ISBN placeholder. A commented German entry is already there as the template.
2. Create `translations/<lang>/chapters/` and `translations/<lang>/book-matter/`, mirroring the English layout and filenames.
3. Put the localized cover art in `cover/<lang>/` (`front-cover-hires.png`, `back-cover-hires.png`, `spine-hires.png`).
4. `.venv/bin/python tools/build.py --lang <lang>` → everything lands in `build/<lang>/`.

Source text for the translator comes from `build/en/text/` — one markup-free `.txt` per chapter, which chunks cleanly for an LLM pass and for the native-speaker review. Nothing else needs changing; the renderers are language-agnostic.

Note: the page count will differ from the English edition (German runs longer), so **each edition has its own spine width** and needs its own cover build.

## Per-language checklist (when a translation is undertaken)
- [x] **German:** all 55 chapters + book-matter, v3 after the §9 revision pass (2026-09-12; `translations/de/`, notes in `REVIEW-NOTES.md`, decisions in `NOTES.md`, echo guard `ECHOES.snapshot.json`). [x] **French:** all 55 chapters + book-matter, written natively with §9 folded in (2026-09-12; `translations/fr/`). [x] **Romanian:** all 55 chapters + book-matter, written natively (2026-09-11), v2 after the §9 revision pass (2026-09-12; `translations/ro/`, echo guard `ECHOES.snapshot.json`). [x] **Hungarian:** all 55 chapters + book-matter, written natively with the §9 rewrite folded in (2026-09-11; `translations/hu/`). [x] **Russian:** all 55 chapters + book-matter, written natively with §9 folded in (2026-09-13; `translations/ru/`, echo guard `ECHOES.snapshot.json`). Other languages: [ ] AI draft of all 55 chapters + book-matter (dedication/epigraph/acknowledgments if written, blurb, bio). The half-title, title page and **copyright page are generated** — the rights page comes out in the edition's own language from `tools/bookbuild/boilerplate.py`, so no one hand-translates it.
- [ ] Native-speaker review pass (voice, idiom, the motifs above). **German: the v3 EPUB is with the reader; §H of `NOTES.md` lists the 13 open questions. Romanian: §H lists 12. Hungarian: the EPUB is with the reader; §H lists 10. French: §H lists 10, plus the cover-comma question. Russian: the v1 EPUB is with the reader; §H lists 12 (title form «Каков дождь на ощупь» vs the shorter «Дождь на ощупь», «несовпадение» vs «нестыковка», эс-бан, floor counting, Опа/Ома, Voss on вы+имя …).**
- [x] **German title fixed: „Wie sich Regen anfühlt“** (with the closing line, one decision — `NOTES.md` §A). [x] **Romanian title fixed: „Cum se simte ploaia“** (§A). [x] **Hungarian title fixed: „Milyen érzés az eső“** (§A). [x] **Russian title fixed: «Каков дождь на ощупь»** (§A; cover alternative «Дождь на ощупь» is §H.1). Other languages: [ ] re-check the title — translate vs keep English. ("Petrichor" chapter title and the Institut name should stay, per the book's own logic.)
- [x] German blurb translated (`translations/de/book-matter/blurb.md`; the KDP description is generated from it). [x] Romanian blurb (`translations/ro/book-matter/blurb.md`). [x] Hungarian blurb (`translations/hu/book-matter/blurb.md`). [x] Russian blurb (`translations/ru/book-matter/blurb.md`). Other languages: [ ]
- [ ] Check the generated **copyright page** — add a `TEXT` entry in `tools/bookbuild/boilerplate.py` if the language has none (the build reports this), have a native reader check the wording, and set `"translator"` in the edition's `EDITIONS` entry so the credit line prints. Keep `_horia` on cover/spine.
- [ ] Re-run a light consistency check (names, place-names stay in original form).
- [x] ~~Separate cover text layer in the target language.~~ Automatic: the cover lettering is typeset at build time from the edition's title and its own `blurb.md`, over the base art. An edition only needs files in `cover/<lang>/` if it wants a *different picture*.
- [ ] New ISBN per edition (or KDP-assigned) per format.

## Cost reality
Full professional literary translation runs ~$6,000–12,000 per language (78.6k words). The AI-assisted + native-review path avoids that; if you ever want a pro translator without cash upfront, a **royalty-share** deal is the model. The user plans AI translation with volunteer native review.

*Last updated: 2026-09-10*
