# Reader feedback — Russian edition (v1)

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
`echo` (touches a repeated phrase), `question` (answers an open item in `translations/ru/NOTES.md` §H).

**Before accepting anything, check echo impact.** If the wording a reader
objects to is one of the guarded phrases, it appears at several sites and they
must all move together, or the callback breaks. Run:

```
.venv/bin/python tools/check_echoes.py ru --check
```

after the phase-two pass, and re-snapshot if a guarded phrase is deliberately
retired.

`translations/ru/NOTES.md` §H already carries **12 open questions** for this edition.
If a reader answers one, file it here with category `question` and cite the
number, so the answer lands next to the decision it settles.

## Tally

Open: 0 · Accepted: 0 · Declined: 0 · Applied: 0

---

## Entries

*(none yet)*

<!-- Template — copy for each new item:

### RU-001 · open · ch00 · idiom

**Reader says (EN):**

**Original ({src-lang}):**

**Echo impact:** none

**Assessment:** *(phase 2)*

**Action:** *(phase 2)*

-->
