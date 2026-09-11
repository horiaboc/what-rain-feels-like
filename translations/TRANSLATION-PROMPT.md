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

## 7. The native-idiom pass (Lektorat) — mandatory, separate from drafting

A single translation pass produces text that is faithful and grammatical and
still reads as *translated*. Native reviewers describe it the same way in
every language: "some idioms and habits don't quite fit." The remedy is not a
better first pass but a **second pass with a different job**, done with the
source open beside the draft, by a translator (or model) told to act as a
native literary editor and to change nothing about *what* is said.

Hunt, sentence by sentence:

- **Fixed phrases carried word for word.** For every English set phrase
  ("patience of a saint", "no one in particular", "lose track", "middle
  distance"), ask what the target language's *own* set phrase of the same size
  is, and use that even when its image differs. Never a longer paraphrase —
  length inflation is itself a loss of restraint.
- **Source punctuation copied.** Dash form and spacing, quotation marks,
  comma rules (before conjunctions, before a year, before subordinate
  clauses). Apply the target norms mechanically after drafting.
- **English clause architecture.** Stacked relative and nominal clauses
  ("the one I get when…", "whatever he is late for", "any of the things
  that…") must be re-planned from the target grammar, never rendered clause
  for clause.
- **Verb prefixes and aspect.** English simple verbs usually need a specific
  prefixed or aspectual form in the target language. Check every verb of
  motion or change for the form a native writer would use *in that context*.
- **Participles and "and"-chains** ("comes back smelling of…", "carrying X
  and Y and the expressions of…") mis-resolved into purpose clauses or
  agreement conflicts.
- **Translationese register.** Uniform formal relative pronouns, nominal
  style, officialese synonyms where the narrator is warm and spoken. Match the
  voice; reserve the formal forms for the voice that is meant to be slightly
  more precise, and record the split in the edition's `NOTES.md`.
- **Domain words.** Tech, media and everyday-technology terms in the form the
  target-language community actually uses (concurrency, edge case, chyron,
  typing in a chat, the news), not a dictionary gloss. Officialese must be
  re-made as the target language's own officialese so deadpan jokes land.
- **Hedges that crept in.** Diff each sentence against the source for added
  intensifiers, articles, connectives ("rather", "again", "meanwhile") and
  remove any the source does not license.
- **Clock and time expressions** in the native colloquial form unless the
  voice is explicitly clinical; fix the choice in `NOTES.md`.

Then a **fidelity check** — adversarial, paragraph by paragraph against the
source — confirms the editor changed *how* and not *what*: nothing dropped,
nothing added, no fact or hedge altered, no restraint amplified, every §3–§5
term intact. The editor and the checker must not be the same pass.

One boundary the editor may not cross alone: §3's fixed names. Allusive names
with a domesticated form in the target language (Diogenes → Diogenész in
Hungarian) are a per-edition decision for the author, recorded in `NOTES.md`,
not an editor's call.

## 8. The procedure, per language — passes until it reads native

Standing order from the author (2026-09-10): a translation is finished only
when it reads as if written in the target language — 9.5 out of 10 or
better as prose in that language, not as a rendering. Names, places and the
deliberately foreign words (§3) are the only things allowed to read as
imported. Run as many passes as that takes, one chapter at a time, in one
working context; never fan out to parallel agents.

1. **Decisions first.** `NOTES.md` for the edition: title ↔ closing line,
   the T–V register for every pair, the reserved phrase and the word banned
   elsewhere, chapter labels, glossary of every seeded echo, voice notes in
   the target language's own terms, typography.
2. **Draft** — the full chapter, faithful, in the fixed decisions.
3. **Native pass (§7)** — with the source beside it: calques, set phrases,
   clause architecture, verb aspect, register, domain words, hedges.
4. **Tic pass.** Count the translator's own fingerprints across the whole
   book with `tools/check_translation.py <lang>` — the frames a native
   writer would vary (German: „die Sorte X, die …“, „Beschaffenheit“,
   „auf die Art, wie“, „nicht direkt“; each language gets its own list) —
   and the trailing afterthought clauses that copy an English *which …*.
   Reduce them to what a native text would carry; vary, don't just delete.
5. **Inquit pass.** Thin *said I / said she* to the density of the target
   language's fiction once speakers are clear; German drops roughly a third.
6. **Gates.** Structure (scene breaks, headings), typography, names, the
   reserved word's count, the title phrase's sites, the concealment rule for
   the early ALEPH chapters. All must be clean before a build.
7. **Read-through** of the chapters the passes touched most, for rhythm —
   the quiet last sentences must still drop.

Then build, then the native reader. Their marked passages go back into the
tic list for the next language.

## 9. The native rewrite — from 9.5 to 9.8

What §7–§8 cannot reach is sentence architecture: clause order, participial
tails, comma-spliced runs, the given-before-new order of German and Romanian
prose, the cadence of a paragraph's last sentence. A polish pass cannot
remove them, because the polisher is still looking at the English sentence.
§9 removes the sentence from view.

**The instruction in one line: don't translate the paragraph — brief a
native author on it, then write it blind.**

### 9.1 Unit = the paragraph, never the sentence

For each paragraph, build a *brief* from the source, then close the source
and write from the brief. The brief holds:

- **What it says** — facts, images, numbers, names, in order.
- **What it does** — the beat: a joke landing, a feeling withheld, a turn,
  a callback; which sentence carries the weight.
- **What it must keep verbatim** — glossary phrases, seeded echoes, the
  fixed lines (§4–§5, `NOTES.md`), italics sites, anything the reserved-
  phrase and title-phrase gates check.
- **Its shape** — sentence count within one or two, where the short
  sentence falls, whether it ends on a noun or a verb, how much of the
  paragraph is one sentence.
- **Dialogue** — each line's speech act (assent, deflection, a question
  under a question), not its wording; the T–V register of the pair.

Then: *close the English; write this paragraph as [voice] would have
written it in [language].* Nothing may be added or dropped; everything may
be re-ordered, re-cut, re-clausen. The book's own strangeness (§9.3) stays.

### 9.2 The native sheet — the only file open while writing

`translations/<lang>/NATIVE-SHEET.md`, kept short so it costs nothing to
hold in context. It carries, per language:

1. **Voice exemplars** — original paragraphs *written natively* in each
   voice (Jonas, Iris, Aleph, Conrad, Mara): the target for rhythm and
   sentence-length variance, not for wording. They are not from the book
   and must never be quoted into it.
2. **The calque list** — the English-isms this language keeps producing,
   with the native move for each.
3. **The deliberate-strangeness list** — what stays odd because the book
   made it odd.
4. **Rhythm rules** — where the language puts new information; when a
   participial tail becomes its own sentence; when an English semicolon
   becomes a full stop; the paragraph-final cadence (short, ending on the
   weighted word).

`NOTES.md` is consulted only when a brief flags a fixed phrase.

### 9.3 Two audits after the write, in this order

- **Fidelity.** Every item of the brief ticked in the rewrite: facts,
  images, numbers, names, echoes verbatim, italics on the same words, each
  dialogue line's speech act intact, register intact. A rewrite that is
  lovelier and lost a beat fails.
- **Nativeness.** Read-aloud test — no sentence needs the English to parse.
  Sentence-length variance of the paragraph against the voice exemplar.
  Frame tics at zero (`tools/check_translation.py <lang>`). Inquit density
  inside the voice's band. No sentence left in English word order where the
  language would front the new information.

### 9.4 The measure

Not a self-rating. Three rewritten paragraphs mixed with three from a
comparable native novel, given to the reader blind: can they pick the
translations? At 9.8 they cannot, or only by content. Their picks go back
into the calque list.

### 9.5 Sequencing

One chapter per step: brief → write → audits → commit, in the main
context, no fan-out. Start with one chapter per language and let the author
judge the difference before the rest of the book goes through it. Budget
about twice a translation pass per chapter.
