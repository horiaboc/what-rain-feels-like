# Launch Plan — *What Rain Feels Like*

Written 2026-09-11, for a debut novel by an unknown author with no mailing
list, no prior titles, and one real asset: a small group of Telegram readers
who followed the book as it was written.

**The strategy in one line:** get the book live cheaply, convert the people who
already care into the first reviews, and only spend money once there is
something for money to amplify.

Everything below is ordered. Do the steps in sequence; each one exists because
the one after it needs it.

---

## Where things stand

- Kindle setup in progress; publishing tomorrow (2026-09-12).
- Paperback not started — it needs one ISBN round-trip (Phase 2).
- Final files in `build/en/`; every KDP field pre-filled in
  `build/en/kdp-metadata.md`.
- Prices decided: **ebook $4.99**, **paperback $16.99**.
- Plagiarism sweep clean (`plagiarism-check.md`).

---

## Phase 1 — Finish the Kindle edition (tomorrow)

1. **Territories:** All territories (worldwide rights).
2. **Royalty:** 70%. List **$4.99**; round the auto-converted rows to natural
   points — €4.99, £3.99, and whatever is natural elsewhere.
3. **KDP Select:** enrol. Then **immediately turn auto-renew OFF** — that
   converts an open-ended exclusivity into a single bounded 90-day experiment,
   reviewed in Phase 6.
4. **Preview** the book in the online previewer before submitting. Look at:
   the dedication page, the ch38 title (א), a scene break, the cover.
5. **Publish.** Review takes 24–72 hours. Do nothing else until it is live —
   there is no audience to tell yet.

*Do not run a launch-week discount.* A sale nobody attends spends royalty on
your earliest and most motivated buyers, and the price rise afterwards reads
as a downgrade. Discounting is a tool for when there is reach to amplify;
that comes in Phase 5.

---

## Phase 2 — The paperback (once the Kindle is live)

Order matters: the ISBN only exists partway through setup, and it has to be
printed inside the book.

1. From the same title record choose **Create paperback** — this links both
   formats on one product page rather than creating a second, competing listing.
2. Print options: **6×9, cream paper, black ink, matte cover**. Cream is what
   the spine calculation assumes; changing it changes the spine width.
3. ISBN: **Get a free KDP ISBN**. Copy the number it assigns.
4. **Send the ISBN to Claude.** It goes into `tools/bookbuild/config.py`
   (`isbn_paperback`), the book rebuilds, and the ISBN prints on the copyright
   page. Upload *that* interior, not the current one.
5. Upload `_interior.pdf` and `_cover.pdf` from the rebuilt `build/en/`.
6. Run the **Print Previewer**. It will flag that the barcode zone overlays the
   lower-right of the back cover — that area is deliberately empty. Everything
   else should pass clean.
7. Price **$16.99** (~$6.06 net); round the other marketplaces — €16.99, £11.99.
8. **Order a proof copy before publishing.** You have never held this book.
   Screens lie about ink density, cover finish, and how the type sits on paper.
   It is a few euros and a week, and it is the only irreversible-feeling part
   of the whole process.
9. Publish once the proof looks right.

---

## Phase 3 — The free scaffolding (same week)

None of this costs anything, and the later phases assume it exists.

1. **Author Central** (authorcentral.amazon.com) — claim the book. Add the bio
   from `book-matter/91-about-the-author.md` and a photo if you want one. This
   turns "Horia" from plain text into a clickable author page, and lets you add
   an editorial description later.
   *Register on amazon.com **and** amazon.de* — Author Central is per-marketplace.
2. **Goodreads** — claim the author profile (Amazon-owned, free). Readers check
   it. Do not chase Goodreads reviews; just exist there.
3. Verify **Look Inside** is enabled — chapter one is the book's best
   salesperson and it should be readable for free.
4. Check the live product page as a stranger would: cover thumbnail legible at
   small size, description formatting intact, both formats listed together.

---

## Phase 4 — The one thing that actually matters (launch week)

**Ask your Telegram readers for honest reviews.**

These are people who read chapters as they were written. They are the entire
reason this launch is not starting from zero, and they are worth more than any
advertising budget you would be willing to spend.

Write to them personally, not as a broadcast. Say: the book is finished and
live, you read it as it was being written, and an honest review — including a
critical one — is the single most useful thing anyone can do for a debut.

Rules that matter:
- **Never offer anything in exchange.** Amazon removes incentivised reviews and
  penalises the book. "Honest" is not a politeness; it is the whole point.
- Ask for a review **on Amazon**, and mention that it can be two sentences.
  Length does not matter; existence does.
- Do not ask family members who share your address or payment methods —
  Amazon detects the relationship and removes those reviews.

**Target: 10–15 reviews.** That is the threshold where conversion changes and
where promotion becomes worth doing. Everything in Phase 5 waits for this.

---

## Phase 5 — Promotion, once there are reviews (roughly weeks 3–8)

Only start here when Phase 4's reviews exist. Promoting a book with two reviews
sends traffic to a page that cannot convert it.

1. **Kindle Countdown Deal** (Select only) — a timed drop to $0.99–$2.99 with a
   visible countdown and "was $4.99" strikethrough. You keep 70% royalty even
   below the usual band. Run it for a few days, not weeks.
2. **Amazon Ads** — optional, and treat the first month as buying information,
   not profit. Start at **$5/day**, target keywords and comparable authors, and
   accept that most keywords will lose money while a few pay. With one title
   and ~$3.30 per sale, the honest goal is finding out what converts, not
   turning a margin.
3. Do **not** buy review services, follower packages, or "book promotion"
   blasts. They are ineffective at best and account-threatening at worst.

---

## Phase 6 — Decide with data (around day 75, ~end of November 2026)

Open the KDP dashboard and look at two numbers: **paid sales** and **KU page
reads**.

- **KU is bringing readers you would not otherwise have reached** → let Select
  renew (turn auto-renew back on before the term ends).
- **KU is negligible** → let it lapse and go wide: Kobo (strong in Germany and
  Canada), Apple Books, Google Play. The EPUB in `build/en/` uploads to all of
  them as-is.

Either answer is fine. The point of the bounded term was to replace a guess
with an observation.

---

## Phase 7 — What comes after (December onward, in rough priority)

1. **The German edition.** Berlin setting, second-largest marketplace, and the
   pipeline already produces it — `--lang de` gives a German cover, a German
   rights page and its own spine from the same artwork. Needs: the translation
   itself, a native review pass, a German blurb, and a native reader for the
   `boilerplate.py` German rights text. See `translation-plan.md`.
2. **Book two.** The strongest marketing any book has is the next book by the
   same author. `bible.md` records the seed: the AGI press conference opens any
   sequel.
3. **Audiobook.** `build/en/text/` is already clean feedstock for narration or
   TTS.

---

## Things to keep in mind throughout

- **The first month will be quiet.** That is not failure; it is what a debut
  without an audience looks like. The numbers that matter arrive over quarters.
- **Reviews compound; ads do not.** A review earned in week two still works in
  year two.
- **Do not chase rank.** It is noisy at low volume and tells you nothing
  actionable day to day.
- **Everything is reversible except the DRM choice** (already correctly set to
  none). Prices, categories, keywords, descriptions and even the interior can
  all be changed after publishing without penalty.

---

*Plan written 2026-09-11. Revisit at Phase 6.*
