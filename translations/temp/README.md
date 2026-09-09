# Translation probe — chapter 1

A quality probe, 2026-08-30: chapter 1 translated into seven languages per
`../TRANSLATION-PROMPT.md`, for native-speaker review before committing to any
full edition. Drafted by the Fable model, one independent pass per language.

**This folder is disposable.** Nothing here feeds `tools/build.py`; a real
edition starts from `translations/<lang>/` + an `EDITIONS` entry per
`translation-plan.md`.

## Files

| Language | Markdown | PDF |
|---|---|---|
| English (source) | chapter-01.en.md | chapter-01.en.pdf |
| German | chapter-01.de.md | chapter-01.de.pdf |
| French | chapter-01.fr.md | chapter-01.fr.pdf |
| Ukrainian | chapter-01.uk.md | — |
| Russian | chapter-01.ru.md | — |
| Serbian (Cyrillic) | chapter-01.sr.md | chapter-01.sr.pdf |
| Romanian | chapter-01.ro.md | chapter-01.ro.pdf |
| Hungarian | chapter-01.hu.md | chapter-01.hu.pdf |

(The MD/PDF split follows what each native reviewer was asked to check; every
language has a Markdown source, PDFs regenerate with
`.venv/bin/python tools/chapter_pdf.py <file.md> <lang>`.)

## What reviewers should check

Per `../TRANSLATION-PROMPT.md`: does it read as if originally written in the
language (idiom, not literalism); is the dry, understated register kept
(restraint is the style — nothing amplified); rhythm of long/short sentences;
names and street names handled per the notes at the end of each file; humour
landing as humour. Each file ends with the translator's own notes flagging its
judgement calls.
