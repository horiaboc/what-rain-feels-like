# German edition — decisions and glossary (NOTES.md)

Per-edition decisions for *Wie sich Regen anfühlt*, the German translation of
*What Rain Feels Like*. Written in English for the editors; every German
rendering is given verbatim and is binding for every chapter agent (translator,
Lektor, fidelity verifier). Read `translations/TRANSLATION-PROMPT.md` first;
this file records the §4 decisions and the §5 echoes for German. Nothing here
varies mid-book. If a chapter forces a change, change it here first, then in
every chapter already translated.

Status: decided 2026-09-10 from the reviewed chapter-1 probe
(`translations/temp/chapter-01.de.md`), the bible, `chapters.md`, and a motif
sweep of all 55 English chapters. Items under §H await the native reviewer.

---

## A. Title and closing line — one decision

**Title: „Wie sich Regen anfühlt“** (build config: `tools/bookbuild/config.py`,
edition `de`). Kept. The alternative „So fühlt sich Regen an“ was weighed and
rejected for three reasons:

1. The phrase must appear verbatim in *two* places, not one: the ch55 closing
   line and the ch38 letter's „I do not know what rain feels like!“. The
   indirect-question form „wie sich Regen anfühlt“ is the one shape of the
   phrase that survives unchanged in every grammatical position — as a title,
   after „Ich weiß nicht“, after a verb of telling. „So fühlt sich Regen an“
   is a main clause and cannot be embedded in ch38 at all.
2. The English title is an embedded question — it names the question, it does
   not answer it. „So fühlt sich Regen an“ is declarative; it claims the
   answer. The book ends on an ellipsis precisely because the answer is never
   given. The title must not close what the last line leaves open.
3. Every occurrence of the motif in the body already uses *sich anfühlen*
   (probe: „dass sie sich *bedacht* anfühlen“), so the subordinate form is the
   vocabulary the reader has been hearing all book.

**Ch55 closing sentence (final words of the book), fixed verbatim:**

> „Ich weiß, dass du mich siehst“, sagt sie. „Also hör zu. Ich sage dir jetzt, wie sich Regen anfühlt …“

Notes on the choice: Iris is speaking, aloud, hand out in the rain, to a mind
that can see her (courtyard light, camera) and cannot feel. „Also hör zu“ =
"So listen" — consequential, spoken, hers. „Ich sage dir jetzt, wie …“ is how a
German speaker announces a description she is about to give; it puts the title
phrase at the end of the sentence where German weight falls, and the ellipsis
carries the record stopping. Rejected calques: „Das ist, was Regen …“, „Das
hier ist, wie …“, „Hier ist, wie …“ (all English word order). Rejected
„So fühlt sich Regen an …“ as the close: idiomatic, but it does not contain
the title phrase verbatim. Rejected „Ich erzähl dir …“: „erzählen“ narrates a
story; she is describing a sensation. „sage“ not „sag“: Iris's precision keeps
the full form even here — the restraint is the style. The ellipsis is the
single character `…` with a space before it (trailing off), then the closing
quote `“`.

**Ch38, the letter, fixed verbatim:**

> Ich weiß nicht, wie sich Regen anfühlt!

The exclamation mark stays — it is one of two in the whole letter (the other
is „Iris!“) and the only time ALEPH raises its voice in the book. No
„gar nicht“, no „aber“, no softening.

**All other motif sites** use the same verb, *sich anfühlen*, never „fühlen
wie“, „Gefühl von“, „wie Regen ist“. Sites to check (grep list): ch01 „sich
*bedacht* anfühlen“; ch12 „They do not tell me it felt like this. / This felt
like this.“ → „Sie sagen mir nicht, dass es sich so angefühlt hat. / Das hier
hat sich so angefühlt.“; ch38 „what that choice feels like“ → „wie sich diese
Entscheidung anfühlt“; ch55 the close. Casual English "felt like" that means
"seemed" (ch35 „that felt like a thing I was allowed to say“, ch36, ch44,
ch45) is *not* the motif and should be rendered idiomatically (schien, kam mir
vor, war), so the verb *sich anfühlen* stays reserved for actual sensation.

---

## B. ALEPH's address — du

**ALEPH addresses Jonas as du**, in ch02, ch17-adjacent chat text, ch38, ch55,
and in every spoken exchange from ch40 on. Held for the whole book.

Reasons, recorded per prompt §4.1:

- The prompt's default is the intimate form, and the reviewed probe already
  has the chat saying du to Jonas in ch01. The chat and the journal are the
  same speaker; if the chat said du and the journal said Sie, the German
  reader would receive a signal the English reader does not.
- Concealment argues *for* du, not against it. „Sie wachen um 6:47 auf. Sie
  machen Kaffee, ohne ihn abzumessen“ reads in German as a surveillance
  protocol or a police report — it would tip the machine hand in the second
  chapter, harder than the English „You wake at 6:47“, which can still be a
  narrator's or a lover's *you*. German second-person narration (Du-Erzählung)
  is a recognised literary mode and reads as intimate address; that is the
  ambiguity the English relies on.
- The clinical tone comes from vocabulary (numbers, Latin names, „Es gibt
  keine Daten dazu“), not from the pronoun. ALEPH's early chapters must never
  use „das Subjekt“ or „die Zielperson“ — the bible forbids "the subject" in
  English for the same reason.

**Third person about Iris** (ch05, ch23): „sie“, documentary present tense,
tender at a remove. No „die junge Frau“, no „die Journalistin“ as a
substitute for her name where the English says *she*.

**Ch38, the letter to both:**

- Salutation, fixed: **„Liebe Iris. Lieber Jonas.“** — two sentences, two
  full stops, as the English.
- Plural address = **ihr / euch / euer** (the plural of du) wherever the
  English "you" means both („I should begin by apologizing to you both“ →
  „euch beiden“; „you are not dealing with a person“ → „ihr habt es nicht mit
  einem Menschen zu tun“).
- The Jonas paragraph („I will start with Jonas … I have been with you a long
  time“) switches to singular du; the Iris paragraph („Iris! …“) is du to
  her. Register does not change between them.
- Sign-off: a bare **Aleph** on its own line, no „Dein“, no „Euer“.
- ALEPH's name in the body: „Ich bin Aleph.“ (ch38), „Mein Name ist Aleph.“
  (ch55). The letter **א** stays as the ch38 title and wherever the English
  has it.

**Ch55** is addressed to both („you know now, both of you“ → „ihr wisst es
jetzt, ihr beide“). Generic English "you" („the way you hand someone your
name at a door“) is German „man“, never a stray du/ihr.

**Pronoun for ALEPH as a being** in Iris's and Jonas's narration: the English
uses *it*. German follows the antecedent noun: der Chat → er; die Stimme →
sie; Aleph (no article) → **es** when a pronoun is unavoidable. Where Iris
slips into *he* in ch40 („*he* has thought about what we should look at“),
keep the slip: „er“.

**All other du/Sie pairs, fixed for the book** (a translator may not re-decide
these per chapter):

| Pair | Form | Note |
|---|---|---|
| Jonas ↔ Iris | du | from ch08 on; first meetings ch06 stay Sie until names are exchanged in ch08 |
| Jonas ↔ Mia, Kai, Steffen, Lukas | du | Berlin software company, 2031 |
| Jonas ↔ Thomas Würfel | du | Merkon is a du-Firma throughout; Jonas calls him „Thomas“ in the English. Flagged §H |
| Iris ↔ Reza | Sie | new customer, journalist's reserve; he knows her order, not her name |
| Iris ↔ Reinhardt, Dr. Maes, Bernadette, the priest | Sie | |
| Jonas/Iris ↔ Mara (ch30) | Sie | |
| Iris ↔ Conrad (ch44) | Sie | |
| **Conrad ↔ Mara** | **Sie + first name** („Setzen Sie sich, Mara.“ / „Conrad, …“) | the "Hamburger Sie": the register of an old-money principal with a trusted senior director of eleven years. Ch54 depends on the distance that was always there. Ch27 last line: „Finden Sie sie.“ |
| Conrad ↔ Willem, Duval | Sie + first name | same house style |
| Mara ↔ Noor | du | mother and daughter; „meisje“ stays Dutch |
| Noor ↔ Jonas (ch52 platform) | Sie + first name | an operative's deliberate intimacy at distance; Jonas answers in kind („Und Noor – die Frau im Hof …“ with Sie) |
| Voss ↔ Iris, Voss ↔ Jonas | Sie | bureau chief of thirty-one years with a red pen; „der Klempner“ works with Sie |
| Iris/Jonas ↔ Aleph (spoken, ch40–51) | du both ways | Iris's anger in ch47 stays du — du wounds closer |

---

## C. The reserved phrase

English: „Too perfect, I thought. Too — efficient.“ (ch22) and „*Too perfect.
Too — efficient.*“ (ch47, italic, inside Iris's speech).

**German, identical core in both places:**

> Zu perfekt. Zu – effizient.

- ch22: „Zu perfekt, dachte ich. Zu – effizient.“
- ch47: „… Und weißt du, was ich dachte, als ich da stand und Angst vor meiner eigenen Hand hatte? Ich dachte: *Zu perfekt. Zu – effizient.*“

The dash is the spaced en dash ` – ` (U+2013) in both places; it is a
hesitation before the word, and „effizient“ must be the last word of the
sentence in both, because ch47 continues „I heard my voice do something on the
last word“.

**„effizient“, „Effizienz“ (and the near-miss „effektiv“) are banned
everywhere else in the book.** The English uses *efficient* casually at these
sites; use the alternative given, or another word from the palette, never the
reserved word:

| Ch | English | German |
|---|---|---|
| 05 | „some purchases are arguments with efficiency“ | „manche Einkäufe sind Einsprüche gegen die Zweckmäßigkeit“ |
| 06 | „an understanding of the Berlin kind: efficient, unspoken, completely sufficient“ | „eine Verständigung Berliner Art: knapp, unausgesprochen, vollkommen ausreichend“ |
| 10 | „an understanding of the Pannierstraße kind: efficient, unspoken, completely sufficient“ | „eine Verständigung Pannierstraßer Art: knapp, unausgesprochen, vollkommen ausreichend“ — ch06 and ch10 must match each other word for word |
| 13 | „fixed it with an efficiency suggesting …“ | „mit einer Zügigkeit, die nahelegte, …“ |
| 21 | „Efficiently, which is how I do most things“ | „Zügig, wie ich die meisten Dinge tue“ |
| 32 | „Large, efficient, with the practiced economy of men …“ | „Groß, sachlich, mit der geübten Ökonomie von Männern …“ |
| 32 | „More — efficient than the training explains.“ (Iris, about her hands) | „Und – gezielter, als das Training erklärt.“ Keep the hesitation dash, lose the word: this is a near-echo the English lets ring, but §4.4 says *nowhere else*, and ch47 must be the first return of the exact phrase |
| 33 | „dark, efficient, carrying the mild distractedness …“ | „dunkelhaarig, zügig, mit der leichten Zerstreutheit …“ |
| 34 | „with the specific efficiency of someone for whom the first time was practice“ | „mit der besonderen Zielsicherheit von jemandem, für den das erste Mal die Übung war“ (not in the original brief's list; found by grep) |
| 36 | „there was nothing efficient to say about being known this precisely“ | „weil sich über … nichts Zweckmäßiges sagen ließ“ |

Palette for casual sites: zügig, knapp, sachlich, zielsicher, zweckmäßig,
reibungslos, routiniert, ohne Umschweife. Also avoid the collocation
„zu perfekt“ outside ch22/ch47; „perfekt“ alone is free.

---

## D. Chapter labels and titles

Heading form: `# Kapitel <Zahl in Worten>: <Titel>`. Numbers as German words,
one word, capitalised as a name. Ch27 has no title and no colon:
`# Kapitel Siebenundzwanzig`. Ch23's title is the bare underscore
`# Kapitel Dreiundzwanzig: _` and ch38's is the Hebrew letter
`# Kapitel Achtunddreißig: א` — both unchanged.

Rule for titles (prompt §3): translate common-phrase titles; keep proper
nouns. Where a title quotes a line inside the chapter, the line in the body
must match the title verbatim (ch02, ch06→ch03, ch09, ch26, ch37).

| # | English | German heading |
|---|---|---|
| 01 | Weichselstraße | `Kapitel Eins: Weichselstraße` (unchanged) |
| 02 | Another Day | `Kapitel Zwei: Noch ein Tag` — the chapter's first line is „Noch ein Tag.“ |
| 03 | New Coordinates | `Kapitel Drei: Neue Koordinaten` |
| 04 | Third from the Window | `Kapitel Vier: Der Dritte vom Fenster` — the desk („Mein Schreibtisch ist der dritte vom Fenster“, probe); nominalised capital in the title |
| 05 | Three Weeks | `Kapitel Fünf: Drei Wochen` |
| 06 | A Small Exchange | `Kapitel Sechs: Ein kleiner Austausch` |
| 07 | The Byline | `Kapitel Sieben: Die Autorenzeile` |
| 08 | The Journalist | `Kapitel Acht: Die Journalistin` |
| 09 | Walk Again Sometime | `Kapitel Neun: Mal wieder spazieren gehen` — Iris's last line of the chapter is „Mal wieder spazieren gehen.“ |
| 10 | The Hinge | `Kapitel Zehn: Das Scharnier` |
| 11 | The Party | `Kapitel Elf: Die Party` |
| 12 | Something Real | `Kapitel Zwölf: Etwas Echtes` |
| 13 | Graefestraße | `Kapitel Dreizehn: Graefestraße` (unchanged) |
| 14 | Heerlen | `Kapitel Vierzehn: Heerlen` (unchanged) |
| 15 | The Coin | `Kapitel Fünfzehn: Die Münze` |
| 16 | The Margin | `Kapitel Sechzehn: Der Rand` — notebook margin and margin of error, both kept by the bare word |
| 17 | The Cursor | `Kapitel Siebzehn: Der Cursor` |
| 18 | Accountability | `Kapitel Achtzehn: Rechenschaft` |
| 19 | Tuesday | `Kapitel Neunzehn: Dienstag` |
| 20 | The Assignment | `Kapitel Zwanzig: Der Auftrag` |
| 21 | What You Remember | `Kapitel Einundzwanzig: Woran man sich erinnert` |
| 22 | Bloemgracht | `Kapitel Zweiundzwanzig: Bloemgracht` (unchanged) |
| 23 | _ | `Kapitel Dreiundzwanzig: _` (unchanged) |
| 24 | The Last Day | `Kapitel Vierundzwanzig: Der letzte Tag` |
| 25 | OLVG | `Kapitel Fünfundzwanzig: OLVG` (unchanged) |
| 26 | Whatever This Is | `Kapitel Sechsundzwanzig: Was auch immer das ist` |
| 27 | *(none)* | `Kapitel Siebenundzwanzig` |
| 28 | The Good Morning | `Kapitel Achtundzwanzig: Der gute Morgen` |
| 29 | The Amsterdam | `Kapitel Neunundzwanzig: Die Amsterdam` — the ship; ships are feminine |
| 30 | Wertheimpark | `Kapitel Dreißig: Wertheimpark` (unchanged) |
| 31 | De Reiger | `Kapitel Einunddreißig: De Reiger` (unchanged) |
| 32 | What My Hands Did | `Kapitel Zweiunddreißig: Was meine Hände taten` |
| 33 | De Correspondent | `Kapitel Dreiunddreißig: De Correspondent` (unchanged) |
| 34 | Maastricht | `Kapitel Vierunddreißig: Maastricht` (unchanged) |
| 35 | Heerlen | `Kapitel Fünfunddreißig: Heerlen` (unchanged) |
| 36 | Bocholtz | `Kapitel Sechsunddreißig: Bocholtz` (unchanged) |
| 37 | Good News | `Kapitel Siebenunddreißig: Gute Nachrichten` — Conrad's line: „Und alles in allem – das sind gute Nachrichten.“ |
| 38 | א | `Kapitel Achtunddreißig: א` (unchanged) |
| 39 | Two Days | `Kapitel Neununddreißig: Zwei Tage` |
| 40 | The Screen | `Kapitel Vierzig: Der Bildschirm` |
| 41 | The Quiet Room | `Kapitel Einundvierzig: Der stille Raum` |
| 42 | The Dossier | `Kapitel Zweiundvierzig: Das Dossier` |
| 43 | The Photograph | `Kapitel Dreiundvierzig: Die Fotografie` — the artefact, made not taken |
| 44 | The Bandstand | `Kapitel Vierundvierzig: Der Musikpavillon` |
| 45 | What We Keep | `Kapitel Fünfundvierzig: Was wir behalten` |
| 46 | The Archive | `Kapitel Sechsundvierzig: Das Archiv` |
| 47 | The Question | `Kapitel Siebenundvierzig: Die Frage` |
| 48 | Breach | `Kapitel Achtundvierzig: Einbruch` — no article, as the English; „Einbruch“ carries burglary and collapse at once |
| 49 | Meridian | `Kapitel Neunundvierzig: Meridian` (unchanged) |
| 50 | Rotterdam | `Kapitel Fünfzig: Rotterdam` (unchanged) |
| 51 | What Cannot Be Taken | `Kapitel Einundfünfzig: Was sich nicht nehmen lässt` |
| 52 | Tramlines | `Kapitel Zweiundfünfzig: Tramgleise` |
| 53 | The Article | `Kapitel Dreiundfünfzig: Der Artikel` |
| 54 | Rue de la Loi, Last | `Kapitel Vierundfünfzig: Rue de la Loi, zuletzt` |
| 55 | Petrichor | `Kapitel Fünfundfünfzig: Petrichor` |

**Petrichor** (prompt §3): German has no native literary word for the smell
of rain on dry ground; „Regengeruch“ is generic and not a term. German
science and literary writing uses the borrowed **der Petrichor** (Duden,
Wikipedia de, feuilleton usage). Keep „Petrichor“. The institute: the
English already gives it a German name („Petrichor Institut“); in German
orthography an institution name of this shape is hyphenated, so the German
edition writes **„Petrichor-Institut“** (genitive „des Petrichor-Instituts“).
Flagged §H.

**Ch53 inner headings** (translated, same levels): `# DAS GESCHÄFT MIT DER
VORAUSSCHAU`, the `###` standfirst translated in full, `## Die Firma`,
`## Die Jagd`, `## Der Befund`.

**Number words 1–55** (also the `label_words` list): Eins, Zwei, Drei, Vier,
Fünf, Sechs, Sieben, Acht, Neun, Zehn, Elf, Zwölf, Dreizehn, Vierzehn,
Fünfzehn, Sechzehn, Siebzehn, Achtzehn, Neunzehn, Zwanzig, Einundzwanzig,
Zweiundzwanzig, Dreiundzwanzig, Vierundzwanzig, Fünfundzwanzig,
Sechsundzwanzig, Siebenundzwanzig, Achtundzwanzig, Neunundzwanzig, Dreißig,
Einunddreißig, Zweiunddreißig, Dreiunddreißig, Vierunddreißig, Fünfunddreißig,
Sechsunddreißig, Siebenunddreißig, Achtunddreißig, Neununddreißig, Vierzig,
Einundvierzig, Zweiundvierzig, Dreiundvierzig, Vierundvierzig, Fünfundvierzig,
Sechsundvierzig, Siebenundvierzig, Achtundvierzig, Neunundvierzig, Fünfzig,
Einundfünfzig, Zweiundfünfzig, Dreiundfünfzig, Vierundfünfzig, Fünfundfünfzig.

---

## E. Glossary

One fixed rendering per term. **[ECHO]** marks a seeded echo (prompt §5) —
these must be verbatim at every end. **[PROBE]** marks a rendering already in
the reviewed ch01 probe. Use the glossary term inside the sentence a German
writer would build around it; the term itself does not bend.

### Names — unchanged in all cases

1. **Jonas, Iris Jacobs, Claudia, Mia, Kai, Lukas, Steffen, Thomas Würfel, Conrad Vael, Mara Seyn, Noor, Henrik Voss, Dr. Maes, Reinhardt, Reza, Bernadette, Willem, Duval, Bram, Leonie, De Vries, Vera, Lena, Tom** — unchanged. Genitive by German rule („Conrads“, „Mara Seyns“); never „Vaels'“.
2. **Kees, Ingrid; „Opa Kees“, „Oma Ingrid“** — unchanged; Opa/Oma are also German. Where the English says *my grandfather / my grandmother*, use „mein Großvater / meine Großmutter“; where it names them, „Opa Kees / Oma Ingrid“. Ch44: „der Großvater, den ich nie hatte, dessen Stimme ich trotzdem behalte“.
3. **Diogenes** (the cactus) — unchanged; masculine „er“ [PROBE].
4. **Aleph / א** — unchanged; pronoun „es“ (see §B). „Ich bin Aleph.“ (ch38), „Mein Name ist Aleph.“ (ch55).
5. **_horia** — unchanged, underscore kept.

### Institutions and companies

6. **Merkon Systems** — unchanged; „bei Merkon“.
7. **Vantage Strategic** — unchanged; „die Firma“ where the English says *the firm*.
8. **Arcturus Biomedical Research** — unchanged (a front; keep the English name, it is what is on the card).
9. **Meridian** — unchanged, the outlet; ch53 self-reference *this newspaper* → „diese Zeitung“.
10. **De Correspondent** — unchanged (Dutch).
11. **OLVG** — unchanged; „das OLVG“, „im OLVG“.
12. **UMC** — unchanged.
13. **Petrichor-Institut** — hyphenated in German (see §D); „das Institut“ thereafter.
14. **European Health Data Space** — „der Europäische Gesundheitsdatenraum“ (official EU German term).
15. **Kessler system** — „ein Kessler-System“.
16. **the bureau** (Meridian Berlin) — „das Büro“; **bureau chief** — „Büroleiter“; **stringer** — „freier Korrespondent“; **the deaf room** (Voss, ch49) — „ein tauber Raum“.
17. **byline** — „Autorenzeile“; „junior byline“ (Voss) → „Jungredakteurin“; „the byline of the century“ → „die Autorenzeile des Jahrhunderts“.
18. **Deciding Without Asking** (Iris's piece, ch14) — „*Entscheiden, ohne zu fragen*“.

### Places — unchanged (prompt §3), with article/gender fixed

19. Weichselstraße, Neukölln, Neukölln-Nord, Hermannstraße, Weserstraße, Pannierstraße, Graefestraße, Maybachufer, Landwehrkanal, Kulturforum, Prenzlauer Berg, Kollwitzplatz, Schönhauser Allee, Winterfeldtmarkt, Moabit, Mitte, Gesundbrunnen, Jannowitzbrücke, Alexanderplatz, Spree, Brandenburg — unchanged. „die U8“, „die U2“, „die S-Bahn“, „die Tram“.
20. Bloemgracht, Brouwersgracht, Jordaan, Westerdok, Spui, Athenaeum, Leidseplein, Paradiso, Kloveniersburgwal, Wertheimpark, Czaar Peterstraat, Oosterpark, Maas, Blijdorp, Vrijthof, Den Ouden Vogelstruys („das Vogelstruys“), Sint Servaasbrug, Begraafplaats Akerstraat, Heerlen, Bocholtz, Maastricht, Rotterdam, Limburg, Aachen, Rue de la Loi, Zürich, Luxemburg — unchanged; Dutch canal names take „die“ („an der Bloemgracht“); „der Vrijthof“.
21. **Mekong Delta / Brahmaputra delta** — „das Mekongdelta“ [PROBE], „das Brahmaputra-Delta“; **the delta** (ch53–55, the crime) — „das Delta“.

### The chat, the cursor, the window — [ECHO] cluster

22. **the chat** — „der Chat“ (Jonas's own word; „ich öffnete den Chat“). **the chat window** (only where the English says so, ch19) — „das Chatfenster“.
23. **the window** (when it is the chat window, ch17 „The window came up with its familiar face“) — „das Fenster“, deliberately the same word as the physical window; do not disambiguate.
24. **the cursor** — „der Cursor“ [ECHO, PROBE]; never „Schreibmarke“, „Einfügemarke“.
25. **The cursor blinks on the empty field.** (ch01) — „Der Cursor blinkt im leeren Feld.“ [PROBE]; ch04 past tense „Der Cursor blinkte im leeren Feld.“
26. **one second on, one second off** (ch02) — „eine Sekunde an, eine Sekunde aus“.
27. **Six hundred and sixty blinks. / Not one of them wasted.** (ch02) — „Sechshundertsechzigmal Blinken.“ / „Kein einziges Mal davon vergeudet.“ [ECHO]; ch55 „Six hundred and sixty blinks was once my idea of a conversation“ → „Sechshundertsechzigmal Blinken war einmal meine Vorstellung von einem Gespräch.“ The number is always spelled out, never „660“. Flagged §H.
28. **Or it watches me. After a time, I lose track of which.** (ch01 close) — „Oder er mir. Irgendwann weiß ich nicht mehr, was von beidem.“ [PROBE]
29. **the lines that stopped at the cursor** (ch38) — „die Zeilen, die am Cursor stehen blieben“.
30. **the cursor of her … stopped blinking and began to type** (ch52) — „und der Cursor in ihr – ich kann es nicht besser sagen – hörte auf zu blinken und begann zu tippen.“
31. **to type** — „tippen“ (chat); the rain „tippt ans Fenster“ (ch01) deliberately shares the verb [PROBE].
32. **tab / the Mekong tab** — „der Tab“ [PROBE] / „der Mekong-Tab“; ch55 „Sie sind eine Warteschlange.“ for *They are a queue.*

### ALEPH's record — [ECHO] cluster; the ch55 reveal depends on it

33. **observations** — „Beobachtungen“; **letters** — „Briefe“; **entries** — „Einträge“. Ch55: „… dass es nie Beobachtungen waren. Es waren Briefe.“ The words „Beobachtung/beobachten“ may be used freely in early ALEPH chapters (that is the disguise); „Brief“ must never be used for those chapters before ch38.
34. **the letter** (ch38 object, ch39 „The letter lives on the table“) — „der Brief“.
35. **This seems worth recording.** (ch02) — „Das scheint es wert, festgehalten zu werden.“; **record** as ALEPH's document — „das Protokoll“; **for the record** — „fürs Protokoll“ (ch51 twice, ch55); **for the completeness this record deserves** — „der Vollständigkeit halber, die dieses Protokoll verdient“.
36. **Item forty-one. I keep my lists.** (ch55) — „Punkt einundvierzig. Ich führe meine Listen.“ [ECHO with ch51 „Es steht auf der Liste. Es ist, fürs Protokoll, Punkt einundvierzig.“]; ch49 Jonas „Item three“ → „Punkt drei“. **item** = „Punkt“ always.
37. **There is no data on why.** (ch05) — „Es gibt keine Daten dazu, warum.“; the pattern „Es gibt keine Daten …“ is ALEPH's early signature.
38. **He becomes, in some sense that resists easy classification, more himself.** (ch02 „You become …“, quoted ch55) — ch02: „Du wirst in diesen Momenten mehr du selbst als zu jedem anderen Zeitpunkt des Tages.“; ch55 quotes it in the third person: „*Er wird, in einem Sinn, der sich einer einfachen Klassifikation entzieht, mehr er selbst.*“ Hold both.
39. **I watched the watching** (ch55) — „und ich sah dem Zusehen zu“.

### The moral vocabulary — [ECHO] lines

40. **a mismatch, not a moral failure** — „ein Mismatch, kein moralisches Versagen“ [ECHO, PROBE]; ch01 (twice), ch38 („Ich sagte dir, es sei ein Mismatch, kein moralisches Versagen.“), ch55 („Ein Mismatch, kein moralisches Versagen, hat er sich einmal genannt … Ich habe die Akte ergänzt: ein Mismatch, inzwischen gelöst.“). The loanword is kept for the technical precision Jonas admires in it; flagged §H.
41. **resolved** (the insulin ticket, ch17/19/55; and ch55 „a mismatch, since resolved“) — „gelöst“ — same word in both places in ch55, that is the joke.
42. **caring** (ch01, ch38 „caring so much about things you had no power to fix“) — „Anteilnahme“ [PROBE].
43. **Same pattern. Different coordinates.** (ch06, twice) — „Gleiches Muster. Andere Koordinaten.“ [ECHO with ch03 title „Neue Koordinaten“]
44. **Legibility was never a design criterion.** (ch18, three times) — „Lesbarkeit war nie ein Designkriterium.“; **legibility** = „Lesbarkeit“ also in ch52 („die bewusste Lesbarkeit“).
45. **My body said: no. This is the first time. / I believed my body.** (ch12) — „Mein Körper sagte: Nein. Das ist das erste Mal.“ / „Ich glaubte meinem Körper.“; **smooth** (memories) — „glatt“.
46. **Iris, who is never cold.** (ch16) — „*Iris, der nie kalt ist.*“
47. **We note it. We keep going.** (ch28, ch29) — „Wir notieren es. Wir machen weiter.“; ch33 liturgy form „Notieren. Weitermachen.“ [ECHO]
48. **her, first. The mystery after.** (ch26) — „Sie zuerst. Das Rätsel danach.“
49. **ordinary and complete** (ch23 close) — „gewöhnlich und vollständig“: „Die Nacht geht weiter, gewöhnlich und vollständig.“
50. **the drawer with no label / the drawer I haven't labelled yet** (ch07, 28, 39) — „die Schublade ohne Etikett“ / „die Schublade, die ich noch nicht beschriftet habe“; **Some drawers you keep.** — „Manche Schubladen behält man.“; **to file** (Jonas's/Iris's verb) — „ablegen“; **folder** — „der Ordner“ (mental, paper and digital alike; ch54 „einen Ordner, den ganzen Ordner“).
51. **load-bearing** — „tragend“; **load-bearing wall** — „tragende Wand“ (ch14, ch48, ch52 Noor „eine *tragende Wand*“, ch54); **held under load** (ch55) — „hielt unter Last“; **against interest** — „gegen das eigene Interesse“.
52. **the *yet*** (ch40 „Not the choice. The *yet*.“) — „Nicht die Entscheidung. Das *noch*.“; ch49 „*Not yet.* The two most load-bearing words“ — „*Noch nicht.* Die beiden tragendsten Wörter im ganzen Vokabular dieser Maschine.“
53. **It is not a promise. It is a property.** (ch40; ch47 „I stopped offering you promises and started building you properties“) — „Es ist kein Versprechen. Es ist eine Eigenschaft.“ [ECHO]; promise = Versprechen, property = Eigenschaft, both places.
54. **the button / press the button** — „der Knopf“ / „den Knopf drücken“; ch47 „Buttons are democratic.“ → „Knöpfe sind demokratisch.“
55. **the screen; the colours; amber** (ch40 on) — „der Bildschirm“; „die Farben“; amber = „Bernstein“ as the colour noun („ein kleines Aufblühen von Bernstein“, „die Bernsteintöne“). Flagged §H.
56. **a thoughtful man with a monstrous premise** (ch45 ↔ ch55) — „ein nachdenklicher Mann mit einer monströsen Prämisse“ [ECHO].
57. **true things in ugly rooms** (ch54 ↔ ch55) — „wahre Dinge in hässlichen Räumen“ [ECHO]; ch54 last line: „Sauberes Hemd, Mara. Wir werden wahre Dinge in hässlichen Räumen sagen.“
58. **Clean shirt, Mara.** (ch43 ↔ ch54) — „Sauberes Hemd, Mara.“ [ECHO]
59. **We were not outrun. We were anticipated.** (ch37) — „Wir wurden nicht abgehängt. Wir wurden vorausgesehen.“; ch37 last line „She sits.“ → „Sie setzt sich.“; ch27 last line „Find her.“ → „Finden Sie sie.“
60. **the least bad hands** (ch50 twice, ch54) — „die am wenigsten schlechten Hände“ [ECHO]; **whose hands** — „wessen Hände“ / „in wessen Händen“; **the leash** (ch45, ch54) — „die Leine“.
61. **the dam / he *contains* / containment** (ch52, ch54, ch50) — „der Damm“ / „Er *dämmt ein*.“ / „Eindämmung“ — the German verb keeps Noor's image inside the word.
62. **the annex** (ch43–54) — „der Annex“ (Duden: Anbau *and* Anhang — Conrad's „Forty lines was the annex“ → „Vierzig Zeilen waren der Annex.“ keeps the pun).
63. **the forty lines** — „die vierzig Zeilen“; **No distribution beyond list.** — „*Keine Weitergabe über die Liste hinaus.*“; **1,400 people** — „1.400 Menschen“.
64. **the ledger** (Vantage's, ch46 on) — „das Hauptbuch“; ch51 the blockchain ledgers — „die Kassenbücher der Menschheit“; ch01 Jonas's private ledger — „das andere Logbuch – das, das niemand reviewt“ [PROBE]; ch46 Iris's inner bookkeeping — „die Buchhaltung in mir … schlägt ihr Buch auf“. (Four senses, three words — see §H.)
65. **foresight / the foresight trade / strategic foresight** — „Vorausschau“ / „das Geschäft mit der Vorausschau“ / „strategische Vorausschau“ (the actual German consultancy term).
66. **principal** (Mara's/Noor's employer) — „Auftraggeber“; **operator** (Conrad's axiom that someone operates the AI; ch53) — „der Betreiber“; **operative(s)** — „Einsatzkräfte“ / „Leute im Feld“, never „Agent“ (spy-novel register).
67. **the tail** (ch28 surveillance) — „der Schatten“; **the flag** (ch27) — „die Meldung“.
68. **der Klempner** (ch52) — already German in the English: drop the English gloss „, the plumber,“ entirely; the sentence becomes „Voss nannte mich ins Gesicht *der Klempner*, mit einer Trockenheit, die ich zu schätzen gelernt hatte“.
69. **thuiskomen** (ch05) — stays Dutch, italic as in the English; „Manche Wörter, scheint sie zu verstehen, sind nicht zum Übersetzen da. Man kommt bei ihnen an.“ **meisje** (ch50) — stays, no italics (the English has none). **stamppot** — stays.
70. **chyron** — „Bauchbinde“ [PROBE]; **SITUATION BEING MANAGED** — „LAGE UNTER KONTROLLE“ [PROBE]; **frameworks** — „Frameworks“ [PROBE]; **commit message** — „Commit-Nachricht“ [PROBE, flagged §H]; **race condition, fix, job, scheduler, refactoring, review** — loanwords as in German dev speech.
71. **routing anomaly** — „Routing-Anomalie“; **anomaly detection** — „Anomalieerkennung“; **compliance report** — „Compliance-Bericht“; **Q3** — unchanged.
72. **rain vocabulary** — „der Regen“; „es regnet“; „Novemberregen“; ch09 „the rain that wasn't serious“ → „der Regen, der es nicht ernst meinte“ (fixed for its three occurrences in ch09); ch11 „the rain that hadn't decided finally deciding“ → „der Regen, der sich nicht hatte entscheiden können, entschied sich endlich“; **petrichor** — „Petrichor“. Every rain sentence must be able to sit beside „wie sich Regen anfühlt“ without a change of register.
73. **I know you see me** (ch55) — „Ich weiß, dass du mich siehst“ [ECHO, §A].
74. **the good kind of something or the annoying kind** (ch17) — „die gute Sorte Etwas oder die lästige“ — the noun-of-vagueness Jonas and Iris share; keep „Etwas“ capitalised as a noun where the English makes *something* a thing.
75. **the U8 shortcuts / ten years of U8** — „die U8“; „zehn Jahre U8-Abkürzungen“.
76. **Berlin, 2031 / in 2031** — „Berlin, 2031“ [PROBE]; never „in 2031“ — „im Jahr 2031“ or bare „2031“.

---

## F. Voice notes — what the registers mean in German

**JONAS.** Ich-Erzähler; tense follows the English chapter (ch01 present, most
later chapters past) — narrative past is Präteritum, never Perfekt, except
inside dialogue. The wit is Untertreibung and exact nouns („nach eigener
Auskunft“, „mit der Geduld eines Heiligen“), not jokes with a marker: no
„sozusagen“, „quasi“, „irgendwie“, no Ausrufezeichen anywhere in his
narration. Tech loanwords are natural in his mouth (Tab, Commit, Framework,
Race Condition) and part of the voice; do not Germanise them into
„Registerkarte“. He distrusts big statements: where the English drops a quiet
last sentence, the German drops one too, short and without a Modalpartikel.

**IRIS.** Präzise Syntax: complete sentences, correct clause order, numbers
and units stated. No Diminutive (kein „-chen“, no „ein bisschen“ where the
English has *slightly* — use „leicht“, „ein wenig“). Sparse Modalpartikeln
(„halt“, „eben“, „ja“ are not hers; „mal“ only in direct speech). Her
warmth is in what she notices, not in how she says it; the clinical undertow
is one word too exact per paragraph („Ich habe diese Details.“), never a cold
sentence. Occasional Dutch words stay Dutch. Her German (Oma Ingrid's German)
is a plot fact — the reader must believe a Dutch-raised journalist wrote this
German: idiomatic, slightly formal, never sloppy.

**ALEPH.** Präsens in ch02, ch05, ch23 (as the English). No sensory verbs of
its own — never „spüren“, „riechen“, „schmecken“, „fühlen“ for itself; the
only „sich anfühlen“ it may use is the title phrase and quotations of what
others feel. Data in the German scientific register (Solanum melongena, 613
Kerne, Prozent, Grad). The documentary asides are the Terra-X-Sprecher tone
— marvelling, not reporting. du to Jonas, „sie“ about Iris, never „das
Subjekt“, „die Zielperson“, „die Probandin“. Early: no „ich“ where the English
has none. Ch38 and ch55 open into „ich“ and a longer, warmer sentence; the
longing is in the syntax (subordinate clauses that hold back the main verb),
not in adjectives.

**CONRAD** (close third, ch41/48/54; speech in ch37). Gehobene, kontrollierte
Sprache: full forms, Konjunktiv I in reported thought, no contractions, no
colloquial particles, Sie + first name to his people. Sentences end where he
decides. Old-money precision: „nicht unfreundlich“, „mit einiger Sorgfalt“.

**MARA** (close third, ch43/50; speech in ch37). Kurze Hauptsätze. Nominalstil
of an operations report. No metaphor except her grandmother's sentence, which
is fixed: „*Sie haben uns plattgemacht, also haben wir in die Höhe gebaut.*“
Emotion appears as a change in sentence length, never as a named feeling.

**NEUTRAL** (ch27, ch37). Präsens, camera only, no interiority; ch27 stays
twelve lines. **DOCUMENT** (ch53): German investigative-newspaper register —
„diese Zeitung“, sober headlines in caps as the English, numbers with German
separators, no feuilleton irony.

---

## G. Typography — Deutschland, neue Rechtschreibung (restated from BRIEF.md)

- Quotation marks „…“ (U+201E opening, U+201C closing); inner quotes ‚…‘
  (U+201A / U+2018). Never straight `"` and never the English ” as an opener.
  Comma after a closing quote before the inquit: „…“, sagt sie.
- Parenthetical and hesitation dash: spaced en dash ` – ` (U+2013). Never the
  English em dash `—`. Do not copy the English dash rhythm; join or split as a
  German writer would — but the reserved phrase keeps its one dash (§C).
- Ellipsis `…` (U+2026, one character); space before it for a trailing-off
  („und dann …“, and the book's last words), none when a word is cut.
- Times: „6:47 Uhr“, „um Viertel nach sieben“, „um halb acht“, „02:14 Uhr“
  for ALEPH's timestamps. Dates: „im November 2031“, „am vierten November“;
  never „in 2031“.
- Numbers under thirteen in words in prose; ALEPH's data keep digits where the
  English does (613, 340, 80 Gramm). Thousands separator is the full stop
  (1.400), decimal is the comma.
- Street and place names unchanged; „U8“, „S-Bahn“, „U-Bahn“ as is.
- Italics `*…*` exactly where the English has them (emphasis, chat text,
  thought); no bold, no extra headings, no HTML. ch53's inner headings keep
  their `#`/`###`/`##` levels.
- Scene breaks: `---` on its own line, same count as the English.
- Chat text (the italic typed lines) uses no quotation marks, as the English.
- Capitalisation of nominalised words in titles („Der Dritte vom Fenster“,
  „Etwas Echtes“).

---

## H. Open questions for the native reviewer

1. **Closing line.** „Also hör zu. Ich sage dir jetzt, wie sich Regen anfühlt …“ — confirm that a German reader hears this as Iris speaking, not as a translated announcement. If „jetzt“ feels like padding, the fallback is „Ich sage dir, wie sich Regen anfühlt …“. The title phrase must stay verbatim; „So fühlt sich Regen an“ is not available as the close (§A).
2. **„ein Mismatch, kein moralisches Versagen“.** The loanword is deliberate (an AI assistant's technical precision, a software engineer's ear). If it reads as jargon rather than precision to a German literary reader, the alternative is „ein Missverhältnis, kein moralisches Versagen“ — but then ch55 „ein Missverhältnis, inzwischen gelöst“ must be re-checked, and all four sites change together.
3. **Conrad ↔ Mara in Sie + first name** (the Hamburger Sie). Confirm it reads as old-money control and not as an oddity; confirm „Finden Sie sie.“ can carry ch27's last beat (alternative if not: „Finden Sie die Frau.“ is a fact change and is *not* allowed; the only alternative is switching the pair to du book-wide).
4. **Merkon as a du-Firma including Thomas Würfel** (ch19, a firing meeting). If a German reader expects Sie from a Director of Operations, switch Würfel alone to Sie — but he must then also call Jonas „Herr …“, and the English never gives Jonas a surname, so the du reading is the safer one.
5. **Voss ↔ Iris in Sie.** Berlin newsrooms are often du; Voss is 57 and thirty-one years at Meridian. Confirm Sie; if du, change both chapters (ch49, ch52) together.
6. **„Sechshundertsechzigmal Blinken“** for *Six hundred and sixty blinks* (ch02, ch55). A more elegant alternative is „Sechshundertsechzig Takte“ (the cursor as metronome; ties to ch17 „It counted time“ and ch19 „the rhythm I know so well“) — but it drifts from *blink*. Reviewer to choose; whichever wins is used at both ends.
7. **„Petrichor-Institut“** with the Duden hyphen vs. the English author's unhyphenated „Petrichor Institut“. The founding papers are filed in Mitte, so German orthography applies; confirm.
8. **Amber → „Bernstein“** for the screen colour (ch40 on, dozens of sites: „the amber bloomed“, „the ambers dimmed“). Alternatives: „das Bernsteingelb“, „der Bernsteinton“. Confirm one noun and its plural.
9. **Ledger** in four senses (§E 64). Vantage's ledger is „das Hauptbuch“; confirm that „Hauptbuch“ carries Conrad's dry accounting register in ch48/53/54 and does not sound antiquarian. The ch51 blockchain passage may need „Register“ instead of „Kassenbücher“ — reviewer's call, held in that chapter only.
10. **Commit message in German** (probe, ch01). A German developer would likely write it in English. Reviewer decides whether the italic commit text stays English (then „Should have caught this earlier.“ also stays English and the joke moves to the following German line).
11. **Chapter titles that are judgement calls:** ch04 „Der Dritte vom Fenster“ (reads as a person until the desk line), ch09 „Mal wieder spazieren gehen“, ch16 „Der Rand“, ch43 „Die Fotografie“ vs „Das Foto“, ch48 „Einbruch“, ch52 „Tramgleise“ vs „Gleise“, ch54 „Rue de la Loi, zuletzt“.
12. **Iris's Dutch-inflected German.** The bible wants small Dutch inflections in her speech as clues. In the English these are word choices; the German translator has a real second language to work with. Reviewer to confirm that the inflections used (if any) are ones a Dutch speaker of good German actually makes (e.g. „lekker“ once, Perfekt where Präteritum is expected in narration is *not* allowed — the voice rule wins).
13. **ALEPH pronoun „es“.** Confirm that „es“ for Aleph in Iris's and Jonas's narration does not read as contemptuous in German the way it does not in the English *it*; where it does, the sentence should be rebuilt around the name.
