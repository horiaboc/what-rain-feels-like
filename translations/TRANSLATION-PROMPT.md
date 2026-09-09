# Translation Prompt — *What Rain Feels Like*

The standing instructions for translating this novel into any language. Give
this file, in full, to the translating model (or human) together with the
chapter text. It applies to every chapter and every target language; the
per-language decisions in §4 are recorded once per edition and then held.

---

## 1. The core instruction

Translate this novel **as if it had originally been written in the target
language**. This is the standard against which every sentence is judged:

- Where the English uses an idiom, an image, or a turn of phrase, do not
  translate its words — find the expression a native writer would have
  reached for to evoke the **same emotion** in the same register. The reader
  of the translation must feel what the reader of the original feels, at the
  same moment, at the same intensity.
- Preserve the **prose style**: sentence rhythm, the balance of long
  observational sentences against short flat ones, the placement of the
  paragraph's weight. Where the English ends a paragraph on a quiet drop, the
  translation ends on a quiet drop.
- Preserve the **emotional load** without amplifying it. This book
  understates; the feeling lives under the sentence. Do not "improve" the
  restraint by making it more expressive — restraint IS the style.
- Keep the **content accurate**. Every fact, every detail, every object in a
  room survives translation. Nothing added, nothing dropped, no summary. If a
  sentence is strange in the original, it is strange on purpose — carry the
  strangeness over, don't repair it.
- Humour must land as humour: Jonas's dry wit should raise the same small
  smile in the target language. If a joke cannot cross literally, replace it
  with one of equal size and dryness — never with an explanation of the joke.

## 2. The three voices

Consult these registers; they must remain distinguishable in translation:

- **JONAS** — first person. Warm, dry wit, observational, self-deprecating.
  A software engineer who notices small things and distrusts big statements.
- **IRIS** — first person. Emotionally alive but subtly *more precise* than a
  person would be — an almost imperceptible clinical undertow beneath real
  feeling. The precision must not become coldness.
- **ALEPH** — second person, addressed to Jonas ("you"). A journal from
  inside a machine: no physical sensation, only data, inference, observation.
  Starts clinical; over the book it drifts toward something resembling
  longing. Its identity is hidden from the reader for the first portion of
  the book — the translation must not tip that hand early.

Minor voices: **Conrad** (formal, controlled, old money), **Mara** (efficient,
flat, no ideology), **neutral** chapters (plain camera, no interiority).

## 3. What never changes, in any language

- Character names: Jonas, Iris, Claudia, Mia, Lukas, Conrad Vael, Mara Seyn,
  Kees, Ingrid, Steffen, Thomas Würfel. The cactus is **Diogenes**.
- Place names stay in their local form: Weichselstraße, Neukölln,
  Hermannstraße, the U8, Bloemgracht, Oosterpark, Heerlen, Rue de la Loi.
  Do not transliterate them unless the target script requires it (Cyrillic
  editions transliterate by that language's standard convention for foreign
  place names — follow the target language's publishing norm).
- The pen name **_horia** — never translated, never transliterated, underscore kept.
- The **א** (ch38 title, and ALEPH's sign-off) — the Hebrew letter stays.
- The chapter-23 title **`_`** (a bare underscore — the cursor) stays.
- Company names: Merkon, Vantage Strategic, Arcturus Biomedical Research.
- The word **petrichor** (ch55 title): translate to the target language's own
  term for the smell of rain on dry ground if one exists in literary use;
  if the language simply borrows "petrichor", keep the borrowed form.
- Markdown structure: `#` chapter heading, `---` scene breaks, `*italics*` —
  reproduce exactly. Translate the chapter label ("Chapter One" → the target
  form) and the chapter title only when it is a common phrase; proper-noun
  titles (Weichselstraße) stay.

## 4. Decisions made once per language, then held

Record these in the edition's `NOTES.md` before translating chapter 1, and
never vary them mid-book:

1. **ALEPH's "you" to Jonas.** In languages with a T–V distinction (du/Sie,
   tu/vous, ти/ви, tu/dumneavoastră…): choose the register and hold it for
   all five ALEPH chapters. Default guidance: **the intimate form** — ALEPH
   knows Jonas completely, and the journal is closer to a love letter than a
   report. The clinical tone comes from vocabulary, not from formal address.
   A translator may argue the formal form better serves the early-book
   concealment; decide once, record why.
2. **The title.** "What Rain Feels Like" is also the final sentence of the
   book (ch55). The title translation and that closing line are ONE
   decision — they must match word for word, and the line must be able to
   carry the weight of being the last thing the reader reads.
3. **Quotation and dash conventions** — use the target language's publishing
   norms („…" for German, « … » for French, — for dialogue where customary).
   Em-dash rhythm inside sentences should follow target-language convention
   rather than mechanically copying the English punctuation.
4. **The reserved phrase.** The phrase "too efficient" (Iris, ch22, echoed in
   the ALEPH dialogue) is a planted echo — translate it identically in both
   places, and nowhere else.

## 5. Seeded echoes — translate consistently at both ends

This book plants phrases early that return late. When translating any
chapter, check the glossary of the edition (`NOTES.md`) and add to it every
phrase the text visibly leans on. Known pairs to protect:

- "too efficient" (ch22 ↔ ALEPH dialogue)
- the title phrase (ch55 closing line ↔ book title)
- the cursor / blinking cursor imagery (ch17 "The Cursor", ch23 `_`, the chat scenes)
- rain, and what it feels like — every occurrence of the motif phrase should
  use vocabulary compatible with the final line.

## 6. Process

- Translate **one chapter per pass**, with the full English manuscript
  available as context for continuity.
- Output: the complete translated chapter in the same Markdown shape as the
  source. No translator's notes inside the text; put notes and glossary
  additions after a `<!-- NOTES -->` marker at the end, and they will be
  stripped from the build and collected.
- Every edition then receives a **native-speaker review pass** (voice, idiom,
  the devices above) before it is built for publication. The AI draft alone
  is not the edition.
