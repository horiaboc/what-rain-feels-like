# Reader feedback — French edition (v1)

Phase one is collection only. Nothing in the text changes while items are being
gathered here. Phase two applies the accepted ones in a single deliberate pass,
chapter by chapter, and **that pass must run on Fable 5.1 at max effort**,
because it edits book content.

Feedback arrives in whatever language the reader writes in. It is recorded here
**in English**, so every edition can be worked from one language. The reader's
own words are kept verbatim underneath, because a nuance lost in translating the
feedback is exactly the kind of thing that matters later.

## How an entry works

Each item gets an ID, a status, a location and a category. Status moves
`open` → `accepted` or `declined` → `applied`.

Categories: `idiom` (reads translated), `grammar`, `voice` (wrong register for
that character), `terminology` (glossary conflict), `typography`, `factual`,
`echo` (touches a repeated phrase), `question` (answers an open item in `translations/fr/NOTES.md` §H).

**Before accepting anything, check echo impact.** If the wording a reader
objects to is one of the guarded phrases, it appears at several sites and they
must all move together, or the callback breaks. Run:

```
.venv/bin/python tools/check_echoes.py fr --check
```

after the phase-two pass, and re-snapshot if a guarded phrase is deliberately
retired.

`translations/fr/NOTES.md` §H already carries **11 open questions** for this edition.
If a reader answers one, file it here with category `question` and cite the
number, so the answer lands next to the decision it settles.

## How a reader should point at something

The EPUB is reflowable and carries no page map, so page numbers depend on the
reader's font size, device and margins. Two readers see different numbers for
the same sentence. Page numbers are only stable in the print interior PDF.

Ask for this instead, in order of usefulness:

1. **The chapter number, plus the words themselves** quoted as they appear.
   Even three or four words is enough to locate a line exactly. This is what
   actually works, and costs the reader nothing.
2. Roughly where in the chapter, if the words are common: near the start, the
   middle, or the end.
3. Page number as a bonus, useful only if they are reading the print PDF.

## Tally

Open: 0 · Accepted: 1 · Declined: 1 · Applied: 0

---

## Entries

Reader 1 (French native, writes feedback in German). Page numbers below are as
the reader gave them, but EPUB paging is device-dependent; the quoted words are
what located each item.

### FR-001 · accepted · ch01 · idiom

**Reader says (EN):** In the evening-news sentence at the start of the Mekong
paragraph, the verb should be *rapporte* ("reports"), not *apporte* ("brings").
Their page 10.

**Original (de):** « le journal du soir rapporte statt apporte - Bei mir ist es
Seite 10 am Anfang des Absatz über Mekong. »

**Echo impact:** safe. The one guarded phrase in that sentence is the delta
name, which the fix does not touch. Re-run the French echo check after applying
anyway.

**Assessment:** Confirmed defect. The English source has the evening news
*carrying* a flood, meaning reporting it. *Apporter* is physical delivery and
does not carry that sense, so the French currently reads as though the newspaper
delivers a flood. The reader's correction is the idiomatic verb and needs no
further discussion.

**Action:** One word in `translations/fr/chapters/chapter-01-jonas.md`,
*apporte* → *rapporte*. Book content, so it waits for the Fable pass.

### FR-002 · declined · ch03 · question

**Reader says (EN):** In chapter three they notice the narrator appears to be a
woman, and ask for a correction if that is not the case. They cite *certaine*
twice on their page 20, *arrêtée* on page 23, and *malheureuse*, noting the
masculine forms would be *certain*, *arrêté*, *malheureux*.

**Original (de):** « In dem 3. Kapitel stelle ich fest dass es eine Frau die
erzählt. Wenn es nicht der Fall ist braucht es auch eine Korrektur: s. 20 kommt
2 mal das Wort certaine vor, die männliche Form ist certain. Selbe Bemerkung
s23, arrêtée oder arrêté? Und auch: malheureuse vs malheureux »

**Echo impact:** none.

**Assessment:** No defect. The reader's inference is correct: chapter three is
narrated by Iris, so every feminine form they flagged is right. All four sit
inside her chapter, including the closing line. Chapter four, narrated by Jonas,
correctly uses the masculine *certain*, and chapter five uses the feminine only
where Aleph is describing Iris. Twenty-one French chapters have a female
first-person narrator, Iris or Mara, and the agreement was checked across the
edition.

Worth noting for the author rather than the text: the chapter headings do not
name the speaker, by design in the English too, so a reader meets the switch
through the prose alone. This reader read it correctly at chapter three, which
is the intended behaviour working.

**Action:** None. Confirm back to the reader that the narrator is female.

<!-- Template — copy for each new item:

### FR-001 · open · ch00 · idiom

**Reader says (EN):**

**Original ({src-lang}):**

**Echo impact:** none

**Assessment:** *(phase 2)*

**Action:** *(phase 2)*

-->
