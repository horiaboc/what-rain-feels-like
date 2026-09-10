# Working brief — German edition (agents)

Mechanics for every agent working on the German edition. The *literary*
instructions are in `translations/TRANSLATION-PROMPT.md` — read that file in
full first, every time. The *per-edition decisions* (title, closing line,
ALEPH's address, the reserved phrase, glossary) are in `translations/de/NOTES.md`
— read it in full, and never contradict it. This file only says where things
are and what each stage must do.

## Files

| What | Where |
|---|---|
| English source chapters | `chapters/chapter-NN-<voice>.md` (55 files) |
| English book-matter | `book-matter/04-dedication.md`, `91-about-the-author.md`, `92-colophon.md`, `blurb.md` |
| German chapters (output) | `translations/de/chapters/` — **same filename** as the English file |
| German book-matter (output) | `translations/de/book-matter/` — same filename |
| Literary instructions | `translations/TRANSLATION-PROMPT.md` |
| Edition decisions + glossary | `translations/de/NOTES.md` |
| Voice bible | `bible.md` — §Characters, §Style Notes, §ALEPH Chapter Style by Act, §Key Lines |
| One-line synopsis per chapter | `chapters.md` |
| Full English manuscript (continuity) | `build/en/manuscript.md` |
| First-chapter probe, reviewed voice reference | `translations/temp/chapter-01.de.md` |

The voice of a chapter is in its filename: `jonas`, `iris`, `aleph`, `conrad`,
`mara`, `neutral`, `document`. Read the bible's description of that voice
before translating.

## The shape of a chapter file — reproduce it exactly

```
# Kapitel <Zahl in Worten>: <Titel>
<blank>
---
<blank>
body…
---            <- every later rule is a scene break; keep the same count as the English
more body…
<!-- NOTES -->
- short translator notes, in English, for the editor (stripped from the build)
```

- The heading label is `Kapitel` + the number as a German word, exactly as
  fixed in `NOTES.md` (e.g. `Kapitel Eins`, `Kapitel Dreiundzwanzig`).
- Chapter 27 has **no title** — heading is just `# Kapitel Siebenundzwanzig`.
- Chapter 23's title is a bare underscore `_`; chapter 38's is `א`. Keep both.
- Chapter 53 contains a newspaper article with its own `#`, `###`, `##`
  headings inside the body. Keep every one, at the same level, translated.
- `*italics*` for emphasis and for typed chat text, exactly where the English
  has them. No bold, no extra headings, no HTML.
- Number of scene breaks (`---` lines after the first) must equal the English.

## German typographic conventions (Deutschland, neue Rechtschreibung)

- Quotation marks „…“ (U+201E … U+201C); inner quotes ‚…‘.
- Parenthetical dash: spaced en dash ` – ` (U+2013), never the English `—`.
  Do not copy the English dash rhythm mechanically; break or join sentences
  the way a German writer would.
- Ellipsis `…` (single character), with a space before it when it stands for
  a trailing-off (`und dann …`), none when a word is cut.
- Times: `6:47 Uhr`, `um Viertel nach sieben`; dates `im November 2031`, never
  `in 2031`.
- Numbers under thirteen in words in prose, as the English does.
- Street and place names unchanged (§3 of the prompt). `U8`, `S-Bahn` as is.

## Stage roles

**Translator.** Produce the complete German chapter, as if written in German.
Keep every fact, object, beat and joke; keep the paragraphing; keep the
scene-break count. Check `NOTES.md` for every glossary term and every seeded
echo before you start, and use them verbatim. Write the file. Add to the
`<!-- NOTES -->` trailer only what an editor needs: judgement calls, a
glossary term you had to coin (mark it `GLOSSARY:`), a place you were unsure.

**Native editor (Lektor).** You are a German literary editor with the English
open beside you. Your single job: make the German read as if it had been
written in German, without changing what it says. Hunt calques and
Anglicisms — `das ist, was …`, `Sinn machen`, `am Ende des Tages`, `nicht
wirklich`, `realisieren` for *realise*, `in 2031`, `Ich meine, …`, English
adverb placement, possessives where German uses the article (`sie hob ihre
Hand`), `-ing` constructions forced into `beim …`, English comma habits,
`Ding`/`Sache` as filler, the reflexive English `sich selbst`, over-hedging
with `irgendwie`. Fix wooden word order. Keep the restraint — do not make
anything more expressive than the English. Do not paraphrase for elegance
where the English is plain. Preserve every glossary term in `NOTES.md`
verbatim. Edit the file in place. Report every change as before/after.

**Fidelity verifier.** Adversarial. Compare English and German paragraph by
paragraph and try to find: an omitted sentence or clause; an added one; a
changed fact (number, time, object, who did what); a meaning shift; a joke
that vanished or became an explanation; a voice slip (Iris sounding warm-
and-loose, Jonas sounding earnest, ALEPH describing a sensation); a glossary
or echo term not used verbatim; ALEPH addressing Jonas in the wrong register;
a name or place altered; a structural error (heading, scene-break count,
italics). Fix what you find directly in the file — minimal edits, in the
established voice — and report each fix with severity. Report `clean` only
after a full pass, never on a sample.

## What every stage returns

Structured output per its schema. The final text of the agent is data for the
orchestrator, not a message to a person. Never return the chapter text
itself — it lives in the file.
