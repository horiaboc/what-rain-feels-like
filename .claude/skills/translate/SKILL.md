---
name: translate
description: Produce a new-language edition of the novel (or rerun a pass on an existing one). Use whenever the user asks to translate the book, build the German/Romanian/Hungarian/… edition, run the native pass, or rate a translation.
---

# Translate — a new-language edition of *What Rain Feels Like*

The full contract is `translations/TRANSLATION-PROMPT.md` (§1–§9). This skill is the entry
point and the order of work. Read the prompt file once at the start of the edition; after
that keep only the edition's `NOTES.md` and `NATIVE-SHEET.md` open.

## Standing rules (from the author)

- **No delegation.** One context, sequential, chapter by chapter. No subagents, no
  workflows, no fan-out — it burned the usage limit twice. Even if ultracode is on.
- **The bar is 9.5–9.8/10 as native prose.** A draft is never finished after one pass.
  Only names, places and the deliberately foreign words (§3) may read as imported.
- **Finished editions go to the author by email** (msmtp as horia@bochis.com; pipe a MIME
  message to `msmtp -t`; check `~/.msmtp.log` for `smtpstatus=250`) and are attached in
  the session with SendUserFile.

## Order of work for a new language `<lang>`

1. **Decisions first — `translations/<lang>/NOTES.md`** (§4–§5): title ↔ closing line
   (one decision, ch55 last words and ch38 „I don't know what rain feels like!“), the T–V
   register for every pair, the reserved phrase „Too perfect. Too — efficient.“ and the
   word banned everywhere else, chapter-label form, the glossary of every seeded echo
   (§E in the de/ro NOTES is the template — ~75 entries), voice notes in the language's
   own terms, typography, §H open questions for the native reviewer.
2. **Native sheet — `translations/<lang>/NATIVE-SHEET.md`** (§9.2): original paragraphs
   written in each voice (never quoted into the book), the calque list, the
   deliberate-strangeness list, rhythm rules. Model on `translations/de/` and `ro/`.
3. **Build-side:** add the edition to `EDITIONS` in `tools/bookbuild/config.py` (name,
   locale, title, subtitle, slug, scene_break, contents_label, byline_prefix, optional
   `title_lines` for the cover stack); a `<lang>` entry in `boilerplate.py` if missing;
   a `RULES["<lang>"]` entry in `tools/check_translation.py` (label regex, bad typography,
   word-ratio band, the language's tic list). `mkdir translations/<lang>/{chapters,book-matter}`.
4. **Chapters, two per step, committing as you go** — `chapters/chapter-NN-*.md` →
   `translations/<lang>/chapters/` with the same file names. Each chapter is written with
   §7 (native idiom), §8 (tic/inquit) and §9 (paragraph briefs, write blind, two audits)
   folded into the same write, and ends with a `<!-- NOTES -->` trailer (the build strips
   it): echoes placed, register choices, anything for the reviewer.
5. **Book-matter:** `04-dedication.md`, `91-about-the-author.md` (keep `{{TITLE}}`),
   `92-colophon.md` (keep `{{BODY_FONT}}`), `blurb.md`.
6. **Gates before any build:** `tools/check_translation.py <lang>` at 0 issues; the
   reserved word only at ch22/ch47 (grep the bodies, not the NOTES trailers); the title
   phrase only at ch38/ch55; no „letter“ in ch02/05/23; the one permitted „kind of“ frame
   only at ch17; tic counts book-wide at native levels.
7. **Build:** `.venv/bin/python tools/build.py --lang <lang> --only cover` then
   `--only epub`; check the cover lettering (Read the `_ebook-cover.jpg`) — fix the title
   split with `title_lines` if a word sits alone on a line.
8. **REVIEW-NOTES.md** — concatenate the chapter trailers (the ro/de files show the form).
9. **Deliver:** email + SendUserFile; update `STATUS.md`, `translation-plan.md`, the
   session log; commit and push.

## For an existing edition

- Rate honestly before touching anything; the last stretch to 9.8 is §9, not another
  polish. Run it one chapter per step; show the author one chapter first.
- Keep the fixed lines and echoes verbatim while re-cutting sentences around them.

## Files

- `translations/TRANSLATION-PROMPT.md` — the contract (§1–§9)
- `translations/<lang>/NOTES.md`, `NATIVE-SHEET.md`, `REVIEW-NOTES.md`, `chapters/`, `book-matter/`
- `tools/check_translation.py`, `tools/bookbuild/config.py`, `boilerplate.py`, `covertext.py`
- Done so far: German (v2, native pass), Romanian (v1, written natively); Hungarian probe in `translations/temp/`.
