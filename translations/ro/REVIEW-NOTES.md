# Romanian edition — review notes (v2)

Collected from the `<!-- NOTES -->` trailers of every chapter and book-matter file (the build strips them). v1 was written natively with the TRANSLATION-PROMPT §7/§8 passes folded into each chapter; v2 = after the §9 rewrite (paragraph briefs → blind rewrite → fidelity audit → nativeness audit), applied as a guarded revision pass: every chapter carries a „v2 (§9 rewrite)“ line saying what changed and that the fidelity audit passed. Echo integrity is checked mechanically by `tools/check_echoes.py ro --check` against `ECHOES.snapshot.json` (90 guarded phrases, 0 regressions). Fixed decisions and the glossary: `NOTES.md`; open questions: its §H.

## Capitolul întâi: Weichselstraße  ·  `chapters/chapter-01-jonas.md`

- From the probe; native pass: „genul de loc“ (reserved for ch17) → „unul dintre locurile acelea care …“; two „felul în care“ frames → „cum …“; „pur și simplu“ dropped (not Jonas's marker).
- Jonas's private log is „celălalt jurnal“ so that „registrul“ stays Vantage's word (NOTES §E 6).
- Parenthetical dashes are the spaced en dash per §G; the em dash is reserved for the dialogue line — this chapter has no spoken dialogue, so none appears.
- Technical borrowings kept as Romanian developers use them: race condition, commit, timestamp, joburile; the deleted line „Ar fi trebuit s-o prind mai devreme.“ reads against a Romanian commit message (reviewer may prefer the message in English — §H 8).
- GLOSSARY seeded: „burtiera“, „SITUAȚIA ESTE GESTIONATĂ“, „cadre“, „cumpănite“, „păsarea“, „o nepotrivire, nu un eșec moral“, „Cursorul clipește în câmpul gol.“
- v2 (§9 rewrite): seven sites — „de felul invizibil“ frame → „cel invizibil“; the „ceea ce este în sine“ afterthought → dash; the gerund chain of the flood footage (înaintând, cărând) → „care înaintează … cu …“; „mai exact“ / „E că …“ (the *not X, exactly / It's that* calques) → „nu chiar“ / „Mai degrabă“; bureaucratic „aceasta“ dropped; „nimănui în mod special“ → „nimănui anume“. Fixed lines (cursor, closing, „o nepotrivire, nu un eșec moral“, commit message) untouched. Fidelity audit against EN: no content shift.
- v2 addendum: „la jumătatea depărtării“ (*the middle distance*, a calque) → „nici aproape, nici departe“ — same fix in ch03.

## Capitolul al doilea: Încă o zi  ·  `chapters/chapter-02-aleph.md`

- ALEPH: present tense, tu; no sensory verb for itself; Coffea arabica kept Latin. „Pare că merită consemnat.“ seeds „consemnarea“ (§E 5).
- „Devii, în clipele acestea, mai tu însuți decât în orice alt moment al zilei.“ is the ch55 quote site — verbatim there.
- „Șase sute șaizeci de clipiri.“ / „Niciuna irosită.“ [ECHO ch55].
- ALEPH timestamps as digits (6:47, 22:03) per §G.
- v2 (§9 rewrite): three sites — „întoarcerea ei lipsă“ (calque of *her missing return*) → „faptul că nu s-a întors“; the two „o calitate“ calques → „are ceva ce …“ / „un zgomot de altă natură“. All fixed lines and echoes untouched. Fidelity audit: no content shift.

## Capitolul al treilea: Coordonate noi  ·  `chapters/chapter-03-iris.md`

- IRIS: complete sentences, exact nouns; „Observatul e singura slujbă …“ keeps the noun-of-the-verb she favours.
- „Pun la dosar“ = to file (§E); „observații“ seeded for ch55's „n-au fost niciodată observații“.
- „chihlimbar“ for amber (§E); „veioza cu abajurul îndoit“ and „șurubul în plus“ are objects ALEPH returns to in ch05.
- „the way X does“ frames rendered with „cum …“ / „așa cum …“, never „felul în care“.
- v2 (§9 rewrite): five sites — „la jumătatea depărtării“ calque → „nici aproape, nici departe“; sentence-initial „Ceea ce“ and the trailing „ceea ce e altceva“ → plain sentence / dash; the gerunds „conținând“ and „urmând … traversându-l“ → „cu …“ / prepositions. Glossary sites („Pun la dosar“, „observații“, „chihlimbar“) untouched. Fidelity audit: no content shift.

## Capitolul al patrulea: Al treilea de la fereastră  ·  `chapters/chapter-04-jonas.md`

- The English italicises Mia's spoken lines; Romanian marks speech with the dialogue dash, so the italics are dropped there (the dash is the marker) — hold this for every spoken exchange the English sets in italics.
- „raportul de conformitate“ (§E); „lizibil“ seeds ch18/ch52; „Cursorul clipea în câmpul gol.“ = ch01's sentence in the past.
- „carrying / holding“ → „a purta / a ține“; keep the pair if it returns.
- v2 (§9 rewrite): seven sites — trailing „ceea ce“ → dash; „Dacă e să spun ceva“ (*if anything*) → „Ba chiar“; „un spectacol de neregretat“ → „nu fac pe cel care nu regretă“; two gerunds („vrând“, „urcând-o“) → finite; „vizuină tehnică“ (*rabbit hole*, opaque) → „cufundare … fără fund“; „de destul timp … să mă gândesc la ea ca la“ → „de destulă vreme … s-o socotesc“. „Am stat o vreme cu asta.“ kept (Jonas's one therapy line). Fidelity audit: no content shift.

## Capitolul al cincilea: Trei săptămâni  ·  `chapters/chapter-05-aleph.md`

- §C site: „unele cumpărături sunt dispute cu utilitatea, și pare că îi place să le câștige“ (no „eficiență“). NOTES §C updated to this wording.
- GLOSSARY: piece (journalism, in progress) → „textul“; the published article (ch53) → „articolul“. „cumpănit“ = considered, matching ch01's „cumpănite“. Coat → „paltonul“ (ch08 opens on it). „un briefing de presă“ kept as the borrowing Romanian newsrooms use.
- „thuiskomen“ kept; „La ele se ajunge.“ carries „They are for arriving at.“ without a gloss.
- Times as digits per §G ALEPH timestamps (9:47, 11:31, 02:23).
- v2 (§9 rewrite): three sites — the clipped „celor nehotărâte acordat“ reordered; trailing „ceea ce nu e totuna“ → new sentence; „rămâne o vreme cu el“ (*stays with it*, Jonas's phrase) → „zăbovește asupra lui“. §C site and the ch03 objects untouched. Fidelity audit: no content shift.

## Capitolul al șaselea: Un mic schimb  ·  `chapters/chapter-06-iris.md`

- Dialogue set with the Romanian dialogue dash; where the English puts a narrative beat inside a speech paragraph („A pause.“, „A beat, dry, not quite a joke.“), the beat is given its own paragraph so it cannot be read as speech.
- Jonas and Iris on dumneavoastră at this first exchange (§B); tu from ch08.
- §C site: „o înțelegere de tip berlinez: scurtă, nerostită, pe deplin suficientă“ — ch10 repeats it verbatim.
- [ECHO] „Același tipar. Alte coordonate.“; „scara de timp“ is the ch08 callback („Succes cu scara de timp“ → „S-a îmbunătățit scara de timp?“).
- Liturgy seeded: „notează, mergi mai departe. Asta e munca.“ (§E, „Notăm. Mergem mai departe.“ later).
- Inner quotes inside the notebook italics use „…” (U+201E/U+201D) — the pair for the whole edition.
- v2 (§9 rewrite): six sites — the two gerund chains of the flood footage → „care înaintează … cu …“; „un contor“ (a meter, for *counter* = one who counts) → „unul care numără“; two „calitatea“ calques → „ceva din atenția lui“ / „frigul e cel de sfârșit de noiembrie“; „unul de dus“ → „unul pe măsură“. §C site, the [ECHO] line and the liturgy untouched. Fidelity audit: no content shift.

## Capitolul al șaptelea: Semnătura  ·  `chapters/chapter-07-jonas.md`

- Title: byline → „semnătura“ (§E 2); „Semnătura“ later carries „semnătura secolului“.
- „asta merită observat“ / „Am observat“ keeps the verb echo of the English (worth noticing / I noticed it).
- „the days are running short in every sense“ → „zilele se scurtează în toate sensurile“ (daylight and deadline both live in „a se scurta“).
- „I wasn't not expecting it, either.“ → „Nici nu nu așteptam.“ — the stacked negative is the joke; kept.
- „shipped“ → „a ieșit“ (dev speech); GLOSSARY: failure mode → „modul de eșec“; „sertarul pe care nu l-am etichetat încă“ seeds „sertarul fără etichetă“.
- Emphasis italics moved to „*pară*“, the verb that carries the appearance/reality split.
- v2 (§9 rewrite): five sites — three trailing „ceea ce“ afterthoughts → dash / „și asta“; „Am stat cu întrebarea“ (a second *sat with* in Jonas's voice; ch04 already has his one) → „Am rămas cu întrebarea“; the gerund „absența fiind“ → finite. „Nici nu nu așteptam.“ and the drawer line kept. Fidelity audit: no content shift.

## Capitolul al optulea: Jurnalista  ·  `chapters/chapter-08-iris.md`

- GLOSSARY: „textul despre biciclete“, „textul despre transparență“ — ch06/ch07 use the same noun. Profile → „o radiografie“ (Romanian newsroom word for a survey piece; „profil“ is for people).
- Dumneavoastră until the names are exchanged; first tu is „N-ai spus nimic.“ / „N-ai întrebat.“ directly after, per §B. Before that, „Te gândești mult la asta“ — she has already crossed to tu in the hour of talk; the English gives no marker, and Romanian journalists of her age would have crossed by then. Reviewer may prefer the switch exactly at the names (§H).
- ch06 callback matches ch06's word: „scara de timp“.
- English leaves the downstairs neighbour and the colleague ungendered; Romanian forced a choice, generic masculine used.
- Narrative beats inside speech paragraphs („He considered.“, „A pause.“, „A single decisive nod.“) set as their own paragraphs.
- v2 (§9 rewrite): seven sites — three trailing „ceea ce“ → „și asta“ / „iar eu“; the missing article („dimineți de marți … deveniseră“) restored; the gerund „sosind“ → „dacă ajung“; „a întrebat de el“ (ambiguous *he/it*) → „de raport“; „așa cum îți pasă fără să ai nevoie s-o anunți“ untangled. ch06 callback „scara de timp“ and the notebook entry untouched. Fidelity audit: no content shift.

## Capitolul al nouălea: Mai ieșim la o plimbare  ·  `chapters/chapter-09-jonas.md`

- Title = Iris's last line verbatim: „Mai ieșim la o plimbare.“ (question and answer share the words, as in the English).
- „ploaia care nu vorbea serios“ ×3 (§E) — the phrase to hold if it returns.
- Tu between Jonas and Iris throughout (post-ch08).
- Narrative beats in speech paragraphs („A pause.“, „A beat.“, „A moment.“, „She glanced at me.“) set as their own paragraphs so the dialogue dash stays unambiguous.
- „a distinct kind of risk“ → „un risc de un fel anume“ (no „genul de“); „use case“ → „caz de utilizare“; „single point of failure“ → „punctul unic de eșec“; „scale“ → „a se scala“ (dev speech, as Jonas would say it).
- „cumpănit“ = considered (glossary).
- v2 (§9 rewrite): nine sites — sentence-initial „Ceea ce“ → „Și chiar asta erau“; three gerunds (punându-și, așternând, făcându-și) → finite; „singurul fel în care“ and „un fel de moment … de fapt“ frames → plain sentences; „pur și simplu“ dropped (not Jonas's); „terminată cu anunțatul de sine“ → „nu se mai anunța“; the rain that *doesn't commit* → „nu se hotărăște“, seeding ch11's „ploaia care nu se hotărâse s-a hotărât“ (§E). Title line, „ploaia care nu vorbea serios“ ×3 and „Am stat cu asta.“ (his one) untouched. Fidelity audit: no content shift.

## Capitolul al zecelea: Balamaua  ·  `chapters/chapter-10-iris.md`

- §C site: „o înțelegere de tip Pannierstraße: scurtă, nerostită, pe deplin suficientă“ — same three words as ch06 (only the place-name changes, as in the English).
- ch03 callback verbatim: „o bicicletă rezemată de zidul din fund, un copac gol, o fereastră luminată“ — ch03 must keep exactly these words (it does).
- folder → „dosarul“ (§E): „în dosarul tot mai gros care îi poartă numele“; to file → „a pune la dosar“.
- „the kind of flaw that …“ → „defectul care …“; „a plant of the variety that …“ → „o plantă din soiul care …“ (no „genul de“).
- „Am notat că vrusesem. Că vrutul fusese …“ — the nominalised verb is Iris's register.
- v2 (§9 rewrite): nine sites — five trailing „ceea ce“ (Szymborska, Diogenes, the late leaving, the nod, the closing line) → „și asta“ / semicolon / „iar el“; „în felul lejer al doi oameni“ and „exact în felul care“ frames rebuilt; the gerund chain „ajustându-se și actualizându-se“ and the opener „Mergând acasă“ → finite; „non-expresia“ → „lipsa de expresie“; „de fapt“ → „în realitate“. §C site, the ch03 callback and the folder line untouched. Fidelity audit: no content shift.

## Capitolul al unsprezecelea: Petrecerea  ·  `chapters/chapter-11-jonas.md`

- „ploaia care nu se hotărâse s-a hotărât în sfârșit“ (§E).
- ch09 callback verbatim: „Mai ieșim la o plimbare?“ / „Mai ieșim la o plimbare.“
- „The way she said *you don't have to* was the way …“ — one „Felul în care“ kept here on purpose: it is the sentence's subject and Romanian has no lighter noun for it; not a frame tic.
- Lukas's „the good coat“ → „Paltonul cel bun“ (ch08 coat).
- Iris's colleagues left as „două colege“ (English ungendered; the party is her newsroom).
- v2 (§9 rewrite): thirteen sites — seven trailing „ceea ce“ (the district, the lateness, Lukas, Bram, the witness, the smile, the shoulders) → dash / „adică“ / „deci“ / „lucru“; five gerunds (negândindu-mă, plimbând, schimbând, făcând, ajungând) → finite; „adâncitura spatelui“ → „mijlocul“; „angajeze la concept“ → „își asume conceptul“. „Felul în care a spus …“ kept on purpose (noted above); ch09 callback and the §E rain line untouched. Fidelity audit: no content shift.

## Capitolul al doisprezecelea: Ceva adevărat  ·  `chapters/chapter-12-iris.md`

- Motif sites: „Nu-mi spun că s-a simțit așa. / Asta s-a simțit așa.“ and „știu cum se simte asta“ — *a se simți* for sensation (§A); „*felt* like“ = seemed is never rendered this way.
- [ECHO] „Corpul meu a spus: nu. E prima dată.“ / „Mi-am crezut corpul.“ — fixed wording (§E 6).
- smooth → „netede“ / „neted“ (§E).
- ch03 callback verbatim: „Un oraș care a fost sfărâmat și pus la loc și care poate că încă își caută forma.“ (ch03 has the same clause).
- „the way you carry“ / „the way you hold still“ frames → „cum porți“ / „cum stai nemișcat“; two „Felul atent … felul mai puțin atent“ are nouns in contrast, not frames.
- „I had not budgeted for“ → „pentru care nu prevăzusem buget“ (Iris's ledger-of-the-self register).
- v2 (§9 rewrite): eleven sites — „ceea ce“ afterthoughts (opening, closing) → dashes; „mai exact“ ×2 (*exactly*) → „nu chiar“; two „calitatea“ calques → „semnul anume“ / plain „atenția lui“; the gerund chains of the warmth paragraph and „rărindu-se“ → finite / adjective; „felul potrivit de sentiment“ → „sentimentul potrivit“; the rain that had *committed* → „se hotărâse“ (ch09/11). Motif sites, the [ECHO] lines and the ch03 callback untouched. Fidelity audit: no content shift.

## Capitolul al treisprezecelea: Graefestraße  ·  `chapters/chapter-13-jonas.md`

- §C site: „cu o iuțeală care sugera că …“ (no „eficiență“).
- Three „The way …“ frames in the eggs paragraph → „Cum am găsit … Cum a râs … Cum am râs“ — the anaphora is kept as „Cum“, which Romanian prose does naturally.
- „a kind of permanence“ → „un fel de permanență“ — one permitted „un fel de“ (a literal kind, not a frame); the checker counts it.
- Mia's line in italics kept (reported speech set in italics by the English, not a dialogue exchange).
- „sarcini de dimineață“ = morning assignments (newsroom).
- v2 (§9 rewrite): eleven sites — the ungrammatical „Miei, ale cărei consecințe“ fixed; „ceea ce“ ×4 → dashes; gerunds („rezolvând“, „închizându-se“, „făcându-se … grăbindu-se“) → finite; „un fel de a sosi“ frame → „sosește cum nu eram pregătit“; „pur și simplu“ dropped (Jonas); „Mai exact“ (*Specifically*) → „Anume“. §C site, the permitted „un fel de permanență“ and the „Cum … Cum … Cum“ anaphora untouched. Fidelity audit: no content shift.

## Capitolul al paisprezecelea: Heerlen  ·  `chapters/chapter-14-iris.md`

- Iris's piece: „*A decide fără a întreba*“ (§E 2) — same italics wherever the title returns.
- [ECHO] load-bearing → „zid portant“: „cum te încrezi într-un zid portant“.
- „Am aceste detalii.“ = „I have these details.“ — the one-word-too-exact sentence NOTES §F cites.
- Opa Kees / Oma Ingrid unchanged; „bunicul“ where the English says „my grandfather“. Pfefferkuchen kept.
- „beat“ (journalism) → „domeniul“; „brief“ → „sarcina“ (ch20 title „Sarcina“ is the same word); „accountability gap“ → „deficit de răspundere“.
- „the kind that gives you time“ → „cea care îți dă timp“.
- v2 (§9 rewrite): four sites — „Stăteam cu gândul“ (*sitting with*, Jonas's phrase) → „Zăboveam asupra“; „ceea ce descria“ → dash; „cu un motiv“ → „dintr-un motiv“; the gerund „întinzând“ → „când întind“. Title of the piece, the [ECHO] „zid portant“ and „Am aceste detalii.“ untouched. Fidelity audit: no content shift.

## Capitolul al cincisprezecelea: Moneda  ·  `chapters/chapter-15-jonas.md`

- The coin exchange is the ch16 hinge: „Pe aceea ar fi găsit-o oricum – se oprise din rostogolit.“ / „Probabil.“ — ch16 quotes „*probabil*“.
- „still downstairs with her book“ — the English places her downstairs; kept „jos“ (Iris's flat is on one level in ch12; the reviewer may prefer „în camera cealaltă“ — flagged, not changed).
- „to reopen the file“ → „să redeschid dosarul“ (§E folder/dosar).
- „a-i păsa de tine“ = caring (glossary „păsare“).
- v2 (§9 rewrite): nine sites — the gerund chain of the June picture (ascultând … explicând … mâncând) thinned to one; „Felul ei de a fi precisă“ and „Are un fel de a primi“ frames → noun / clause; three „ceea ce“ → dashes; two „pur și simplu“ dropped (Jonas); „mai exact“ → „nu chiar“; „în mod special“ → „anume“. The coin exchange (ch16 hinge) and „să redeschid dosarul“ untouched. Fidelity audit: no content shift.

## Capitolul al șaisprezecelea: Marginea  ·  `chapters/chapter-16-iris.md`

- [ECHO] „*Iris, căreia nu-i e niciodată frig.*“ — fixed wording (§E 6).
- ch15 callback: „*probabil*“.
- „pur și simplu“ appears three times here — Iris's voice, where the English has „simply“ each time; kept for her (the ban is on Jonas's narration).
- „the kind of thing that resolves“ → „un lucru care se rezolvă“; „the way you notice a loose stair“ → „cum observi o treaptă slăbită“.
- The English says „Weichselstraße“ for the bus though the scene is at Iris's; kept as in the source.
- v2 (§9 rewrite): five sites — „mai exact“ (*exactly*) → „nu chiar“; four gerunds (sosind, trecând/aterizând, ieșind/având, așteptând) → finite. Iris's „pur și simplu“ kept where the English has *simply* in her voice; [ECHO] „*Iris, căreia nu-i e niciodată frig.*“ and the ch15 „*probabil*“ untouched. Fidelity audit: no content shift.

## Capitolul al șaptesprezecelea: Cursorul  ·  `chapters/chapter-17-jonas.md`

- The ONE permitted „genul de“ in the book: „genul bun de ceva sau genul enervant?“ (§E 6).
- ch15 callback verbatim: „Faci asta – te duci undeva în mijlocul unei conversații și te întorci într-un loc puțin diferit.“ / „Te întorci întotdeauna după ce ai găsit ceva.“
- Pronoun for the chat: Iris's aborted question „Oare el…“ — „el“ with antecedent „chatul“ (§B), and Jonas's „nu despre el“; never „ea“.
- GLOSSARY: routing anomaly → „anomalia de rutare“; log → „log“ (dev speech) but the complaint is „notată“; „ferestre de livrare“.
- „the kind where the answer is obvious“ → „cel în care …“ (pronoun, no frame).
- v2 (§9 rewrite): seven sites — two „ceea ce“ → „și (tocmai) asta“; „O ridicasem cu Steffen“ (*raised it with*, calque) → „Îi vorbisem lui Steffen despre ea“; „de fapt“ → „cu adevărat“; gerunds („spunând“, „descriind“, „uscându-se“, „clipind“) → finite. The one permitted „genul de“, the ch15 callback and the „el“ for the chat untouched. Fidelity audit: no content shift.

## Capitolul al optsprezecelea: Răspundere  ·  `chapters/chapter-18-iris.md`

- [ECHO] „Lizibilitatea n-a fost niciodată un criteriu de proiectare.“ ×3, verbatim each time (§E 6); „lizibil“ / „lizibilitate“ seed ch52.
- „Sunt bună pe domeniul ăsta. O știu de ceva vreme.“ matches ch14's sentence.
- „pur și simplu“ ×4 in Iris's narration, where the English has „simply“ — her word, kept.
- „the way a hand settles around an object made for it“ → „cum se așază o mână în jurul unui obiect făcut pentru ea“.
- v2 (§9 rewrite): six sites — „fiind“ / „trimițând“ / „explicându-le“ gerunds → finite; two „ceea ce“ → dashes; „Am stat cu liniștea“ (*sat with*, Jonas's phrase) → „Am rămas în liniște“; „rostitul“ → „rostirea“. [ECHO] „Lizibilitatea …“ ×3, the ch14 sentence and Iris's „pur și simplu“ untouched. Fidelity audit: no content shift.

## Capitolul al nouăsprezecelea: Marți  ·  `chapters/chapter-19-jonas.md`

- „Nu spune probabil“ — Iris's line uses the ch15/ch16 word.
- „stabilizat“ for „steadied“ (ch20 „Iris had been steadying“ → „stabilizatoare“ would be clumsy; ch20 uses „mă stabilizase“).
- „Am făcut bilanțul“ = took stock; „conștiința curată“; „beneficiile de concediere“.
- Thomas Würfel unchanged; „director de operațiuni“ lowercase per Romanian usage.
- v2 (§9 rewrite): five sites — „hotărăsc împotriva“ calque → „renunț la“; three „ceea ce“ (Thomas, the decision, „altceva și mai bun“) → dash / „Deci“; „mai exact felul în care“ → „anume că“. „Nu spune probabil“, „stabilizat“ and the closing cursor paragraph untouched. Fidelity audit: no content shift.

## Capitolul al douăzecilea: Sarcina  ·  `chapters/chapter-20-jonas.md`

- Title „Sarcina“ = the assignment (ch14 uses the same noun for „brief“).
- Amsterdam places unchanged: Bloemgracht, Jordaan(ul), Leidseplein, Paradiso, Noordermarkt, Spui, Haarlemmerdijk, Westerkerk.
- „un text bun“ (piece). „the kind of address that …“ → „o adresă care …“; „the way you adopt a neighbourhood“ → „cum adopți un cartier“.
- „Mă stabilizase“ picks up ch19's „stabilizat“.
- v2 (§9 rewrite): seven sites — six „ceea ce“ afterthoughts (the lying-in, the light, Mia's full stop, the three in the parents' paragraph) → dashes / „iar ei“; „am stat cu calitatea“ (*sat with the quality*) → „am rămas cu gustul“; the gerund chain „mergând … adoptându-l“ thinned; „sosind în ordinea potrivită“ → „la rândul lui“. Title noun and the Amsterdam names untouched. Fidelity audit: no content shift.

## Capitolul al douăzeci și unulea: Ce îți amintești  ·  `chapters/chapter-21-iris.md`

- §C site: „Iute, cum fac mai toate lucrurile“ (no „eficient“).
- „Pusul deoparte“ — Iris's nominalised verb (as „Observatul“ in ch03, „vrutul“ in ch10).
- „the way you accept change from a stranger“ / „the way you call up a familiar place“ → „cum accepți …“ / „cum chemi …“.
- „Emoții?“ for „Nervous?“ — the Romanian idiom for pre-event nerves.
- v2 (§9 rewrite): three sites — „mai exact“ → „nu chiar“; „Spui dimineața“ read as the verb *you say* → „Spui-ul“ (§E article pattern, as „Vrijthof-ul“); the gerund „făcându-se“ → relative. §C site and „Pusul deoparte“ untouched. Fidelity audit: no content shift.

## Capitolul al douăzeci și doilea: Bloemgracht  ·  `chapters/chapter-22-iris.md`

- RESERVED PHRASE site 1 of 2: „Prea perfect, m-am gândit. Prea – eficient.“ — „eficient“ appears nowhere else in the book except ch47's italic quotation of this line.
- „the way you learn a language“ / „the way you note weather in another country“ → „cum înveți o limbă“ / „cum notezi vremea din altă țară“.
- *stamppot* kept, declined as „*Stamppot*-ul“ (Romanian hyphenated article on a foreign noun).
- Amstel 1, Waag, Athenaeum, Singel(ul), Elandsgracht unchanged.
- Narrative beat inside speech („I looked at the bridge …“) set as its own paragraph between the two halves of Iris's line.
- v2 (§9 rewrite): eleven sites — the gerund chains (venind; stând/uitându-mă; găsindu-și; lăsându-se/povestindu-mi; părăsind; odihnindu-se; netezindu-se) → finite / „cu …“; three „ceea ce“ → dash / „cum se face“; „de fapt“ → „în realitate“. RESERVED PHRASE site untouched; place names untouched. Fidelity audit: no content shift.

## Capitolul al douăzeci și treilea: _  ·  `chapters/chapter-23-aleph.md`

- [ECHO] „Noaptea continuă, obișnuită și completă.“ — fixed (§E 6, „obișnuită și completă“).
- No „eu“, no „tu“, no sensory verb: the camera voice of the „_“ chapter; „Scrisoare“ absent (§E 5).
- Timestamp „02:14“ per §G.
- v2 (§9 rewrite): read through, unchanged.

## Capitolul al douăzeci și patrulea: Ultima zi  ·  `chapters/chapter-24-jonas.md`

- „un zid unde ar fi trebuit să fie o piațetă“ — „zid“ is the word; ch25's callback must use „zid“ too (German had a Wand/Mauer mismatch to fix here).
- „Data viitoare stăm mai mult.“ / „Mai mult data viitoare.“ — hold if it returns.
- „the way of a person walking ground she knows“ → „cum e un om care merge pe un teren pe care îl cunoaște“.
- Dutch bystander's line given in Romanian; the English marks it as spoken „in English“ — kept „în engleză“.
- OLVG unchanged; „box cu perdea“ for curtained bay.
- v2 (§9 rewrite): eight sites — the gerund chains of the ride and the fall (stând, stând, mergând, afirmându-și, ducându-se, raportând, întâlnind, ținându-i) → finite / relative; „am putut-o vedea mergând cu ea“ (ambiguous *her/it*) → „lucrul acela a mers cu ea“. „zid“, the „Data viitoare“ pair and the OLVG lines untouched. Fidelity audit: no content shift.

## Capitolul al douăzeci și cincilea: OLVG  ·  `chapters/chapter-25-iris.md`

- ch24 callback: „zidul de la capătul străzii“ — same word as ch24.
- Dr. Maes's speech is reported (the English has no quotation marks); kept as indirect/free reported speech, no dialogue dash, dumneavoastră inside her words per §B.
- „Am spus: sigur. Deveneam pricepută la *sigur*.“ — ch24 has „Am spus sigur. Iris a spus sigur.“; same word.
- „the way of someone choosing each word“ → „cum e cineva care alege …“.
- „branulă“ for the IV line (Romanian hospital word).
- v2 (§9 rewrite): five sites — „ceea ce capul a interzis“ → semicolon; gerunds („deplasându-se“, „nepunând“, „rulând“) → finite / relative; „calitatea aceea a atenției“ → „atenția aceea a lui“. Iris's nominalisations („pusul deoparte“, „așezatul“), the ch24 „zid“ and Maes's reported speech untouched. Fidelity audit: no content shift.

## Capitolul al douăzeci și șaselea: Orice ar fi asta  ·  `chapters/chapter-26-jonas.md`

- [ECHO] „ea, mai întâi. Misterul, după.“ — fixed (§E 6).
- „Vreau să rămână consemnat.“ — Jonas's „on the record“ uses the ledger word ALEPH will own („consemnarea“), on purpose: the seed.
- „Extraterestră“ — Iris says it of herself, feminine.
- „the way you run a sentence“ / „the way she holds things“ / „the way of two people“ → „cum rulezi …“ / „cum ține ea …“ / „cum tac doi oameni“.
- Amsterdam UMC unchanged.
- v2 (§9 rewrite): nine sites — the gerund chains (mergând/dictând, făcând, închizându-se, întorcând-o/verificându-i, cântărind/întinzând, umplându-se/limpezindu-se/devenind) → finite; „ceea ce … semăna“ → „și … asta semăna“; Jonas's *sat with* kept once („Stătusem cu asta toată noaptea.“) and the other two varied; „mai exact“ → „nu chiar“; „pur și simplu“ dropped from his speech. [ECHO] „ea, mai întâi. Misterul, după.“ and „Vreau să rămână consemnat.“ untouched. Fidelity audit: no content shift.

## Capitolul al douăzeci și șaptelea  ·  `chapters/chapter-27-neutral.md`

- No title, no colon (§D). Camera voice, present tense.
- „Găsiți-o.“ — Conrad to Mara in dumneavoastră (§B), the two-word order the book returns to.
- GLOSSARY: the flag → „semnalarea“; Vantage's monitoring layer → „stratul de monitorizare“; „Spațiul European al Datelor de Sănătate“; „o fișă medicală“ for a health record.
- v2 (§9 rewrite): read through, unchanged.

## Capitolul al douăzeci și optulea: Dimineața bună  ·  `chapters/chapter-28-jonas.md`

- [ECHO] „Notăm. Mergem mai departe.“ — the liturgy in its book-form (§E 6); ch06's imperative „notează, mergi mai departe“ is its seed.
- „sertarul fără etichetă“ (§E) — ch07 said „sertarul pe care nu l-am etichetat încă“; from here on the fixed form.
- „the way you find things in Amsterdam“ / „the way you notice something“ / „the way you study a thing“ / „the way you learn to“ → all „cum …“.
- „un pho chiar bun“; „sourdough“ kept (Berlin/Amsterdam café word).
- Places unchanged: Brouwersgracht, Wibautstraat, Frederiksplein, Utrechtsestraat, Amstel.
- v2 (§9 rewrite): six sites — two „ceea ce“ → „și asta“ / „Așa că“; gerund chains (făcându-și/învârtindu-se, înregistrând/nedepunând, apăsând/apăsând, îndurând) → finite / relative. [ECHO] „Notăm. Mergem mai departe.“, „sertarul fără etichetă“ and Iris's „pur și simplu“ untouched. Fidelity audit: no content shift.

## Capitolul al douăzeci și nouălea: Amsterdam  ·  `chapters/chapter-29-jonas.md`

- Title: the ship, „*Amsterdam*“ (italic, feminine as a ship in Romanian: „stă“, „lată“).
- ch28 callback verbatim: „Notăm. Mergem mai departe.“ — Iris hands the words back.
- Mara ↔ Iris/Jonas: dumneavoastră + „doamnă Jacobs“ / „doamnă Seyn“ (§B).
- „VOC East Indiaman“ → „Corabie a Companiei Indiilor Orientale“; Batavia unchanged; nautical words: greement, parâme, tambuchi, cală, coaste.
- „the organized unremarkableness“ → „banalitatea organizată“.
- v2 (§9 rewrite): six sites — „de fapt“ → „într-adevăr“; gerunds (îndreptându-mă, fiind, reușind, rulând/ajungând, tăindu-și) → finite / „cu fața spre“ / „nimeni anume“. Title, the ch28 callback and Mara's address forms untouched. Fidelity audit: no content shift.

## Capitolul al treizecilea: Wertheimpark  ·  `chapters/chapter-30-jonas.md`

- Mara's card: „director de operațiuni de cercetare“; Arcturus Biomedical Research unchanged.
- „Generous the way a moat is wide“ → „generoasă cum e lat un șanț de apărare“.
- „the kind of conversation that sits better without walls“ → „o conversație care stă mai bine fără pereți“; „the kind of park that exists for …“ → „un parc care există pentru …“.
- Mara's reported speech (no quotes in the English) kept indirect; her quoted lines with the dialogue dash.
- „a închis dosarul“ = closed the file (§E).
- v2 (§9 rewrite): four sites — the gerund chains of the park (purtând/sosind, negociind, urmărind, venind/aurind/promițând) → „cu …“ / relative / finite. Mara's card, her reported speech and „a închis dosarul“ untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și unulea: De Reiger  ·  `chapters/chapter-31-jonas.md`

- ch04 callback verbatim: „Eu doar o spun înapoi, limpede.“ — the chat's line, now Jonas's.
- „the kind that doesn't need to announce itself“ → „dintre cele care n-au nevoie să se anunțe“.
- Last section: camera voice inside a Jonas chapter, as in the English.
- De Reiger, Nieuwe Leliestraat unchanged.
- v2 (§9 rewrite): eight sites — gerunds (venind, citind, făcându-și, plimbând/purtându-și, mergând, făcând-o, uitându-se/lăsând) → finite / „cu …“; „Am stat cu asta“ (his one per chapter is not needed here) → „Am lăsat asta să stea între noi“. The ch04 callback „Eu doar o spun înapoi, limpede.“ untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și doilea: Ce au făcut mâinile mele  ·  `chapters/chapter-32-iris.md`

- §C sites: „Masivi, expeditivi, cu economia exersată a unor bărbați …“ and „Și – mai precis decât explică antrenamentul.“ — no „eficient“.
- ch25 callback: „O să ne dăm seama.“
- Iris's „Sau îmi amintesc că îi cunoșteam.“ — the split sentence she hears.
- „the kind whose cardboard sleeve …“ → „dintre cele al căror …“; „the kind of passage every old city keeps“ → „unul dintre pasajele pe care le păstrează orice oraș vechi“.
- Waterlooplein, Staalstraat, Kloveniersburgwal, appelgebak unchanged; „Open space“ is the Romanian office word for open plan.
- v2 (§9 rewrite): fourteen sites — the gerund chains of the alley and the café (trecând, legând, alunecând, recalibrând, rulând, asamblând/alegându-i, numărând, părându-mi, despicându-se) → finite / relative; three „ceea ce“ → dashes; „să stau cu ce se întâmplase“ (*sit with*, Jonas's phrase) → „să cuprind“. §C sites, the ch25 callback and „Sau îmi amintesc că îi cunoșteam.“ untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și treilea: De Correspondent  ·  `chapters/chapter-33-jonas.md`

- [ECHO] load-bearing → „Aceasta era portantă.“; liturgy „Notează. Mergi mai departe.“
- §C site: Lena „brunetă, iute“ (no „eficientă“).
- Tom ↔ Iris dumneavoastră („Sunteți sigură…“); Lena's „Eu sunt Lena“ neutral.
- Vera's line here: ch03 seeded „Vera, care stătea lângă mine“ — same person, consistent.
- „the way of a city that doesn't know it's being fled“ → „cum alunecă un oraș care nu știe că e părăsit în fugă“.
- Barentszplein, Centraal, bitterballen unchanged.
- v2 (§9 rewrite): eight sites — gerund chains (alunecând, purtând, nearătând, încercând, desfășurându-se, venind/aducând) → finite / relative / „cu …“; the nominal „ținerii sertarului închis“ → „să țină sertarul închis“; the closing relative → dash. [ECHO] „portantă“, the liturgy and §C „brunetă, iute“ untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și patrulea: Maastricht  ·  `chapters/chapter-34-jonas.md`

- §C site: „cu siguranța de țintă a cuiva pentru care prima dată a fost exercițiu, iar asta e aplicația“ (no „eficiență“).
- Priest ↔ Iris: the blessing „Pace ție.“ / „Și ție.“ is the liturgical formula and stands outside the dumneavoastră rule; the priest's „Atunci ai-o“ is the confessional's tu — kept, the reviewer may prefer „aveți-o“.
- „Una care ține.“ / „Două care țin.“ — hold if it returns.
- „the kind of building that has absorbed so much time“ → „o clădire care a absorbit atâta timp“.
- Den Ouden Vogelstruys, Vrijthof, Onze Lieve Vrouweplein unchanged; basilica name translated.
- v2 (§9 rewrite): twelve sites — gerunds (folosindu-l, oferind, ieșind/apărând, recalculând, mișcându-se, acceptându-l, plecând, lăsând, fiind) → finite / relative; two „ceea ce“ → „și asta“ / dash; „calitatea aceea atentă“ → „atenția aceea … a ei“. §C site, the priest's formulas and „Una care ține“ untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și cincilea: Heerlen  ·  `chapters/chapter-35-iris.md`

- Grave lettering kept bold; the dash after each name is the Romanian en dash, the quotes „Kees” Romanian.
- Bernadette ↔ Iris/Jonas dumneavoastră; her „dragă“ for „dear“.
- The driver ↔ both: dumneavoastră (plural), including „Sunteți urmăriți“, „ați deschis o fereastră de chat“; Jonas's „Urcă“ to Iris is tu, then „Dacă mințiți“ to him.
- „the kind of face that belongs to several people“ → „o față dintre acelea care …“; „the way people are kind when …“ → „cum sunt buni oamenii când …“.
- „nu era nimic util de spus“ here is the ch35 line; ch36 has the §C site with the same wording — both deliberate.
- Begraafplaats Akerstraat, Bocholtz unchanged.
- v2 (§9 rewrite): fifteen sites — gerund chains (privind/încredințându-mi, sosind ×2, încetinind, insistând, devenind, neîntinzând, lăsând/rostogolindu-se/marcând, purtând) → finite / relative / „cu …“; three „ceea ce“ → dashes; „de fapt“ → „cu adevărat“; „dacă e să spun ceva“ (*if anything*) → „mai degrabă“; „adâncitura spatelui“ → „mijlocul“ (ch11). Grave lettering, address forms, the driver's eleven-word line and „nu era nimic util de spus“ untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și șaselea: Bocholtz  ·  `chapters/chapter-36-iris.md`

- §C site: „nu era nimic util de spus despre a fi cunoscut atât de precis …“ (no „eficient“).
- The Diogenes-not-Diogenes cactus; „ghiveci simplu de teracotă“.
- „the specific one“ → „aceea anume“; „the kind you use for stamppot“ → „cei pe care îi folosești la stamppot“.
- „să redeschidă procesul“ for „relitigate“.
- v2 (§9 rewrite): seven sites — gerunds (ticăind, trecând, stând ×2, punând) → relative / finite; two „ceea ce“ → dashes; „să poți sta cu ele“ (*sat with*) → „să poți rămâne cu ele“. §C site and the cactus line untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și șaptelea: Vești bune  ·  `chapters/chapter-37-neutral.md`

- [ECHO] „N-am fost întrecuți. Am fost anticipați.“; „Și, una peste alta – sunt vești bune.“ (title); „Luați loc, Mara.“; „Ea se așază.“ (§E 6).
- Conrad ↔ Mara: dumneavoastră + prenume throughout (§B); Conrad's „oamenilor tăi“ inside a generalisation („a suspicion is not a thing you hand your people“) is the impersonal tu, not address.
- operators → „operativi“ (§E); „nu neprietenos“ = Conrad's register (§F).
- Mara's report style: short main clauses (§F).
- v2 (§9 rewrite): one site — the double gerund „privește venind … traversând“ thinned. [ECHO] lines, the title line and „Ea se așază.“ untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și optulea: א  ·  `chapters/chapter-38-aleph.md`

- TITLE-PHRASE site 1 of 2: „Nu știu cum se simte ploaia!“ — verbatim (§A).
- „Dragă Iris. Dragă Jonas.“; voi/vă where both are meant, tu in the Jonas paragraph and the Iris paragraph; sign-off bare „Aleph“ (§B).
- [ECHO] „o nepotrivire, nu un eșec moral“ (ch01's wording); „rândurile care s-au oprit la cursor“ (§E 4).
- „cum se simte alegerea aceea“ — a quote about what humans feel, permitted by §A.
- Aleph masculine in Romanian grammar („sigur“, „bucuros“, „primul“) — the letter is written by a voice that has no gender; Romanian forces one; the masculine is the unmarked choice (reviewer §H).
- v2 (§9 rewrite): one site — „mai des decât nu“ (*more often than not*, a calque) → „de cele mai multe ori“. TITLE-PHRASE site, the address forms, the [ECHO] lines and Aleph's masculine agreement untouched. Fidelity audit: no content shift.

## Capitolul al treizeci și nouălea: Două zile  ·  `chapters/chapter-39-jonas.md`

- [ECHO] „sertarul fără etichetă“; „Unele sertare le păstrezi.“ (§E 6).
- The chat pronoun: „Vorbesc cu el de cinci ani“ — „el“ with antecedent chatul (§B); the screen „Nu ne putea vedea“.
- Iris's spoken line set in „…” inside narration (reported, not an exchange).
- „the way you don't examine a thing“ / „the way you orbit a telephone“ → „cum nu examinezi …“ / „cum orbitezi …“.
- „upgrades“ → „actualizări“ (Jonas's dev word).
- v2 (§9 rewrite): sixteen sites — the gerund chains of the fields and the lane (cusându-l/înclinându-se, făcând, adunându-se/neplecând, verificând/numărând, mișcându-se, făcând, mișcându-se, strecurându-mă, făcându-și, lucrând, lucrând/desfăcând/verificând, terminând) → finite / relative / „cu …“; four „ceea ce“ → dashes; two „pur și simplu“ dropped (Jonas). [ECHO] „sertarul fără etichetă“ and „Unele sertare le păstrezi.“ untouched. Fidelity audit: no content shift.

## Capitolul al patruzecilea: Ecranul  ·  `chapters/chapter-40-iris.md`

- [ECHO] „Nu e o promisiune. E o proprietate.“; „Nu alegerea. Acel *încă*.“; „o mică înflorire de chihlimbar“ (§E 6).
- Iris's slip „*el s-a gândit …*“ kept as „el“ (§B); Aleph masculine agreement in its own speech („sigur“).
- Aleph ↔ both: tu to each, voi/vă when both („Ecranul … se trezesc la gestul vostru“; „Somn ușor. Amândoi.“).
- **Vantage Strategic** bold as in the English; Mara „directoarea lui operațională“.
- „taxă de trecere“ = charge the world for passage.
- v2 (§9 rewrite): six sites — gerund chains (subțiindu-se/mișcându-se, umflându-se/așezându-se, devenind, acuzând/localizând) → finite; „ceea ce e un ghicit“ → „adică“; „Am stat cu asta“ (*sat with*, Jonas's phrase) → „Am rămas cu asta“. [ECHO] lines („Nu e o promisiune. E o proprietate.“, „Acel *încă*.“, the amber bloom) and the „el“ slip untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și unulea: Camera tăcută  ·  `chapters/chapter-41-conrad.md`

- [ECHO] „mâinile cele mai puțin periculoase“ here; ch49/ch54 use „mâinile cele mai puțin rele“ (Iris's phrase) — kept distinct as in the English (least dangerous / least bad).
- GLOSSARY: „lumea înregistrată / neînregistrată“; „operatorul“; „carnetul gri“; „telefonul“ (Iris as the telephone) — ch42 repeats it.
- Conrad ↔ Mara dumneavoastră + prenume; imperatives in the plural („Rechemați“, „Găsiți-i“, „Urmăriți“).
- „A vrea – asta sunt mințile.“ for „Wanting is what minds are.“
- „e un costum“ = „it is a costume“; „băcani“ for shopkeepers (Conrad's contempt).
- v2 (§9 rewrite): five sites — gerunds (murind, citindu-l ×2/nespunând, alegând, așezându-se) → finite; Mara's „Ceea ce nu e o coincidență“ → „Și nu e“. „Totul e ținut.“, „A vrea – asta sunt mințile.“, *VORBIM.* and the notebook line untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și doilea: Dosarul  ·  `chapters/chapter-42-jonas.md`

- ch01 callback: „Burtiera. *Situația este gestionată.*“ (italic here, capitals there, as in the English).
- GLOSSARY: foresight → „Previziune.“; „telefonul“ (ch41); „lumea înregistrată“ (ch41); the bandstand → „chioșcul“ (ch44 title „Chioșcul“).
- „bilanțul zilei“ for the ledger of the day — „registrul“ stays Vantage's (§E).
- Aleph's inline quotation set in „…” inside Jonas's narration.
- Bold shape headings kept.
- v2 (§9 rewrite): nine sites — gerunds (purtând, având, sosind, plecând/făcându-și) → finite / „cu …“; two „ceea ce“ → „Adică“ / „și asta“; the dropped „că“ restored; „e la război“ (reads as *at war*; the English is *on the loom*) → „stă pe războiul de țes“ — the weaving sense, with the pun kept; „mai exact“ → „nu chiar“. Bold shape headings, the ch01 callback and the sink line quoted in ch45 untouched. Fidelity audit: one meaning corrected (loom), no other shift.

## Capitolul al patruzeci și treilea: Fotografia  ·  `chapters/chapter-43-mara.md`

- [ECHO] „Cămașă curată, Mara.“; „portantă“ (load-bearing).
- GLOSSARY: principal → „mandantul“; „sala de operațiuni“; Devos ↔ Mara tu (her subordinate); Mara ↔ Conrad dumneavoastră + prenume, Conrad's „Dumneavoastră – la distanță“.
- „annexe of habits“ → „aripa nouă de deprinderi“ so that „anexa“ stays the forty-line annex (§E).
- „a bilețel trecut pe sub bancă“ = a note passed in class.
- Mara's voice: short main clauses; the one metaphor she is allowed later (ch50) is not here.
- v2 (§9 rewrite): nine sites — gerunds (vrând, stând ×2, începând, ținând, demonstrând, dând, mergând, fiind) → finite / relative / „cu …“. [ECHO] „Cămașă curată, Mara.“ and „portantă“, Conrad's dumneavoastră lines and „aripa nouă de deprinderi“ untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și patrulea: Chioșcul  ·  `chapters/chapter-44-iris.md`

- Conrad ↔ Iris: dumneavoastră + „Doamnă Jacobs“ / „Domnule Vael“ (§B).
- GLOSSARY: „Vând previziune. Previziunea e legală.“ (§E foresight); the bandstand → „chioșcul“ (title); „un expert care locuiește într-o priză“.
- Aleph's earpiece lines in italics, tu to Iris.
- „Până la piața următoare.“ for „Until the next square.“
- „the way you check a room“ / „the way you cross a stage“ → „cum verifici …“ / „cum traversezi …“.
- v2 (§9 rewrite): eleven sites — gerunds (fiind, mișcându-se, discutând, făcând/ajungând, anulându-se, gonind, sosindu-mi) → finite / relative / „cu …“; „care e trucul“ and three „ceea ce“ (two in Conrad's speech) → „și ăsta e“ / „și asta“; „adâncitura spatelui“ → „mijloc“ (ch11/35). Address forms, the foresight line, the earpiece italics and „Până la piața următoare.“ untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și cincilea: Ce păstrăm  ·  `chapters/chapter-45-jonas.md`

- [ECHO] „un om chibzuit cu o premisă monstruoasă“; the leash → „o lesă cu maniere excelente“ (§E).
- ch12 callback: „cel pe care îl lasă în urmă lucrurile cele mai bune“ (ch12: „tăcerii pe care o lasă în urmă lucrurile cele mai bune“).
- ch42 callback verbatim: „O femeie, un card bancar și o sacoșă de cumpărături“.
- records → „evidențele“ (Conrad's paper); „the door“ → „ușa“.
- Aleph ↔ both: voi/vă plural („v-am spus“, „Apăsați butonul. Fiți oameni“).
- v2 (§9 rewrite): ten sites — the „ceea ce“ chains (Aleph's report, Jonas's running argument, the two „Ceea ce înseamnă“) → „așa că“ / „și asta“ / „Adică“; gerunds (raportând, scurgându-se, expirând, schimbându-se, știindu-le) → finite / relative; „mai exact“ → „nu chiar“; Conrad's *sit with* → „rumege“. [ECHO] „un om chibzuit cu o premisă monstruoasă“, the leash, the ch42 sink line and the ch12 callback untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și șaselea: Arhiva  ·  `chapters/chapter-46-iris.md`

- GLOSSARY: „un sistem Kessler“; „contabilitatea din mine … își deschide registrul“ (Iris's inner bookkeeping) and „Registrul s-a deschis ca orice foaie de calcul“ (Vantage's ledger) — the English uses „ledger“ for both on purpose; kept.
- Noor ↔ Iris: tu both ways (combat register); ch52 Noor ↔ Jonas dumneavoastră.
- Noor's radio line in „…” inside italics.
- „the way you know a word in a language you are still learning“ → „cum știi un cuvânt …“.
- „doctoriță“ for Dr. Maes in Iris's memory (she is a woman; ch25 used „dr. Maes“ as title).
- v2 (§9 rewrite): 26 sites — the gerund chains of the yard and the annex (călătorind, ducând, stând, cedând/schimbându-se/ținând, trezindu-se, încetinind, având, mergând, sosind, făcând, luându-i/întorcându-i-le/ajustându-se/punctând, hotărând, convergând, verificând/încrucișând/fiind) → finite / relative; five „ceea ce“ → dashes / „și asta“; „felul plecării lui“ / „un fel de a spune“ frames rebuilt; *rationing* → „a drămui“ (three sites; „raționaliza“ also reads as *rationalise*); *barred* → „prins în cheie“ (the armbar). „Nu m-a antrenat nimeni.“, „Nu ne urmări. Te rog.“ and the ledger words untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și șaptelea: Întrebarea  ·  `chapters/chapter-47-iris.md`

- RESERVED PHRASE site 2 of 2: „M-am gândit: *Prea perfect. Prea – eficient.*“ — the italic quotation of ch22's line („m-am gândit“ matches ch22). NOTES §C updated to this form.
- [ECHO] „Butoanele sunt democratice.“; the button as property (ch40) restated: „am început să-ți construiesc proprietăți“.
- „two and fourteen“ → „două și paisprezece minute“ in prose (ch23 „02:14“ as timestamp).
- „the way you are proud of a scar“ / „the way sediment settles“ → „cum ești mândru …“ / „Cum se așază sedimentul“.
- Aleph → Iris tu; „Vă las camera“ plural when Jonas enters.
- v2 (§9 rewrite): seventeen sites — gerund chains (subțiindu-se/găsindu-și, ținându-și, netezindu-se, apăsând/căutând, urcând/așezându-se, întorcându-se, limpezindu-se/devenind, ținându-și/nebându-l, localizând, așezându-se, așteptând, stând/ținând/răcindu-se) → finite / relative / „cu …“; „unul dintre felurile în care“ and „niciun fel de a întreba“ ×3 → „căile“ / „nicio cale“ (Jonas's line too). RESERVED PHRASE site 2, „Butoanele sunt democratice.“ and „proprietăți“ untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și optulea: Breșa  ·  `chapters/chapter-48-conrad.md`

- Duval's line is seven Romanian words („Un exercițiu de incendiu la registratură, azi-noapte“), matching the count the narration gives.
- ch41 callbacks verbatim: „A vrea – asta sunt mințile“; „Are limite. Trăim în interiorul lor.“ / „VORBIM.“; „carnetul gri“; „telefonul“ / „activul“.
- [ECHO] „zidul portant al unui deceniu de aritmetică morală“; „până e sigur că sunt portante“ (load-bearing ×2).
- Noor's report in italics; her quoted line „Nu m-a antrenat nimeni.” matches ch46.
- „GĂSIM. ȚINEM. SCHIMBĂM.“ — first plural like „VORBIM“.
- Conrad ↔ Mara dumneavoastră + prenume throughout; Conrad ↔ Duval dumneavoastră.
- v2 (§9 rewrite): eleven sites — gerunds (vrând ×2, regăsindu-și, predând, aterizând/hotărând, punându-și, stând, asigurându-se) → finite / relative; three „ceea ce“ → „deci“ / dashes; the tangled „tribunal pe care și-a petrecut … asigurându-se“ rebuilt; „citirea tablei“ → „tablei de joc“. Duval's seven words, the ch41 callbacks, Noor's report and *GĂSIM. ȚINEM. SCHIMBĂM.* untouched. Fidelity audit: no content shift.

## Capitolul al patruzeci și nouălea: Meridian  ·  `chapters/chapter-49-jonas.md`

- [ECHO] „*Nu încă.* Cele două cuvinte cele mai portante din tot vocabularul acelei mașini.“ (§E 6).
- GLOSSARY: bureau chief → „șeful biroului“; stringer → „colaborator extern“; junior byline → „o semnătură de junior“; deaf room → „o cameră surdă“; corrections → „erate“; „secția civică“.
- Voss ↔ Iris/Jonas: dumneavoastră + prenume (§B); Voss's telegram-style reply and his notebook line kept in italics.
- ch03 callback: „poveștile … care contează enorm pentru oamenii care le citesc“ (ch03: „poveștile care contează enorm pentru cei care le citesc“) — Jonas quotes her loosely, as the English does.
- The coffee machine's sigh: „un mic oftat de abur sub presiune înaintea primei cești, de parcă ar fi avut nevoie de o clipă“ — ch01/ch04's sentence, in the past.
- v2 (§9 rewrite): eighteen sites — gerund chains (făcându-și, hurducându-se, făcând, ținându-i, mișcându-se, punând-o, făcându-și, mergând, dându-i, verificându-se/vânându-ne) → finite / relative; four „ceea ce“ → dashes / „și ăsta“; „mai exact“ → „nu chiar“; „singurul lucru cel mai important“ → „lucrul cu adevărat cel mai important“; „pe onorariu“ (retainer) → „la dispoziție“; „cum nu mai exista nimic“ → „fără pereche“. [ECHO] „*Nu încă.*“ line, Voss's telegram and notebook, the coffee-sigh callback untouched. Fidelity audit: no content shift.

## Capitolul al cincizecilea: Rotterdam  ·  `chapters/chapter-50-mara.md`

- [ECHO] Mara's grandmother, fixed: „*Ne-au făcut una cu pământul, așa că am construit în sus.*“ (§F) ×2; „mâinile cele mai puțin rele“; „ale cui mâini“; „Cămașă curată, Noor.“ (ch43 „Cămașă curată, Mara.“).
- Mara ↔ Noor tu; „Ma“ and *meisje* kept (§B).
- ch48 callback: „zăcând unde a căzut“ (ch48 „zace încă unde a căzut“); Conrad's note in italics with his initials.
- Blijdorp, Bergweg, Rotterdam-Zuid, Srebrenica unchanged; WINTERFELDTMARKT / KREUZBERG stamps in capitals.
- „O să fim mai răbdătoare decât el.“ for „We will out-patient it.“ — the coined verb has no Romanian; the comparative carries it.
- v2 (§9 rewrite): ten sites — gerund chains (numindu-l, fiind, mergându-și, făcând-o, rezolvându-mă, făcând/urând-o, refuzându-l ×2, punându-mi/gândindu-mă, depozitând, făcându-și/mutând) → finite / relative; one „ceea ce“ → dash. §F sentence (twice), the [ECHO] hands, „Cămașă curată, Noor.“, Conrad's note and Noor's „felul care spune te rog“ untouched. Fidelity audit: no content shift.

## Capitolul al cincizeci și unulea: Ce nu se poate lua  ·  `chapters/chapter-51-iris.md`

- [ECHO] „E pe listă. E, ca să rămână consemnat, punctul patruzeci și unu.“ (§E 5 — ch55 „Punctul patruzeci și unu. Îmi țin listele.“); „ca să rămână consemnat“ twice more (Aleph, Jonas); ch48/50 „Zace unde a căzut.“
- „Nu sunt de câștigat – mi te poți doar *alătura*.“ for „I am not winnable — I am only joinable.“
- „somnul de proprietate-nu-promisiune“ (ch40 property/promise).
- Aleph → Iris tu, → both voi/vă; Jonas addressed tu („Diogenes … custodiei tale“).
- „the way you check every door in the house“ / „the way parents wake at silence“ → „cum verifici …“ / „cum se trezesc părinții la tăcere“.
- v2 (§9 rewrite): fifteen sites — the gerund chains of the three-streets life, Aleph's litany of the world's pulse and the closing watch (dând/verificând, plecând, purtând, așteptând, sosind, cunoscându-i, stând, raportându-și …, păstrând, purtând/cunoscându-mă/înțelegând/cerând, încălzindu-se, urmărind/păzind/așteptând, ținând, ascultând/ținându-și) → finite / relative; „un fel de a arăta“ → „arată cumva“. [ECHO] lines, „mi te poți doar *alătura*“ and „somnul de proprietate-nu-promisiune“ untouched. Fidelity audit: no content shift.

## Capitolul al cincizeci și doilea: Șinele de tramvai  ·  `chapters/chapter-52-jonas.md`

- [ECHO] „El *stăvilește*.“ (the dam); „zid portant“; „patruzeci de rânduri“; „cursorul din ea – nu știu s-o spun mai bine – a încetat să clipească și a început să scrie“ (§E 4); „lizibilitatea deliberată“.
- *der Klempner* kept with the gloss „instalatorul“ — Romanian readers need it (the German edition dropped it). NOTES §E updated.
- Noor ↔ Jonas: dumneavoastră both ways, first names (§B).
- Berlin U8 stations and Hinterhof unchanged; „Hinterhof-urile“ with the hyphenated Romanian plural article.
- ch49 callback: „ne trezim la absența celuilalt“ (ch51).
- v2 (§9 rewrite): twelve sites — gerund chains (făcându-se, rulând, intrând, repetându-se, stând, alergând/știind-o/făcând, recitând, cheltuindu-și, aterizând, sosind) → finite / relative; „ceea ce de la Aleph“ → dash; „pur și simplu“ dropped (Jonas); „mă gestionau“ → „încercau să mă manevreze“. *der Klempner* with its gloss, „El *stăvilește*.“, the cursor line and Noor's dumneavoastră untouched. Fidelity audit: no content shift.

## Capitolul al cincizeci și treilea: Articolul  ·  `chapters/chapter-53-document.md`

- Headings per §D: `# COMERȚUL CU PREVIZIUNI`, `###` standfirst, `## Firma`, `## Vânătoarea`, `## Constatarea`; byline bold; dateline italic; Romanian thousands „1.400“.
- [ECHO] „*Fără difuzare în afara listei.*“; „patruzeci de rânduri“; „acest ziar“ (Meridian's self-reference); „Spațiul European al Datelor de Sănătate“; „o lesă“; foresight → „previziuni / previziune strategică“.
- Newspaper register (§F): sober, no dialogue dash, quotation marks „…” for the quoted line.
- The intelligence is „o inteligență“ (feminine noun) in the newspaper's own grammar — „Nimeni nu o controlează“ — distinct from Aleph's masculine self-reference elsewhere; this is the paper's word, not the narrator's.
- v2 (§9 rewrite): nine sites — gerunds (convergând, lucrând, fiind, cheltuindu-și, purtând, stând) → finite / relative; „ceea ce e standardul“ → dash; „Ceea ce lasă întrebarea cu care … a stat“ (sentence-initial *which* + *sat with*) → „Rămâne întrebarea pe care … a purtat-o“; „felul în care“ → „motivul pentru care“. Headings, the quoted line, „patruzeci de rânduri“, „1.400“, „o lesă“ and the feminine „o inteligență“ untouched. Fidelity audit: no content shift.

## Capitolul al cincizeci și patrulea: Rue de la Loi, ultima dată  ·  `chapters/chapter-54-conrad.md`

- [ECHO] „Cămașă curată, Mara. Mergem să spunem lucruri adevărate în încăperi urâte.“ (§E: „lucruri adevărate în încăperi urâte“ — ch55 quotes it); „Patruzeci de rânduri erau anexa.“; „mâinile cele mai puțin rele“; „Nu există nicio lesă.“; „A vrea – asta sunt mințile.“; „portant“; „băcanii“ (ch41).
- Aleph's message to Mara is five Romanian words with dumneavoastră: „Ați avut dreptate. Vă mulțumesc.“
- Conrad ↔ Mara, Conrad ↔ Willem, Conrad ↔ the lawyers: dumneavoastră (§B); „strategic de-a-ndoaselea / de-a-ndreptelea“ for backwards/forwards.
- „spargerea unui abces“ for „the lancing of something“.
- v2 (§9 rewrite): thirteen sites — gerunds (stând ×2, dând, ținând, dându-i, refuzând ×2, necheltuind, cântărindu-se, trecând/ducând) → finite / „cu …“ / „în cumpănă“; two „ceea ce înseamnă“ in Conrad's speech → „adică“; „stă cu ea“ (*sits with*) → „o lasă să se așeze“; „sunt cum arată arhitectura mea“ → „sunt arhitectura mea, așa cum arată“. All [ECHO] lines, Aleph's five-word message, the address forms and „spargerea unui abces“ untouched. Fidelity audit: no content shift.

## Capitolul al cincizeci și cincilea: Petricor  ·  `chapters/chapter-55-aleph.md`

- TITLE-PHRASE site 2 of 2, the last words of the book, fixed verbatim (§A): „— Știu că mă vezi, spune ea. Așa că ascultă. Îți spun acum cum se simte ploaia…“
- [ECHO] „și priveam privitul“; „Șase sute șaizeci de clipiri erau cândva ideea mea de conversație.“; „n-au fost niciodată observații. Au fost scrisori.“; „ca să rămână consemnat“; „lucruri adevărate în încăperi urâte“; „un om chibzuit cu o premisă monstruoasă“; „patruzeci de rânduri“; „1.400 de oameni“; „Institutul Petricor“; „Sunt o coadă de așteptare.“; „*Devine, într-un sens care se sustrage clasificării ușoare, mai el însuși.*“ (ch02's sentence in the third person); „O nepotrivire, nu un eșec moral … o nepotrivire, între timp rezolvată“; „semnătura secolului“; ch47 „una dintre astea e o relație“; „pentru caracterul complet pe care îl merită această consemnare“; „Punctul patruzeci și unu. Îmi țin listele.“; „portante“.
- „Mă numesc Aleph.“ — first „eu“ of the book outside the ch38 letter; masculine agreement kept (§H).
- „voi“ for both readers („știți acum, amândoi“).
- v2 (§9 rewrite): six sites — three „felul în care / felul pe care“ frames → „așa cum“ / „cum“; gerunds (bătându-se, sosind ×2/trezindu-se/căzând) → finite / relative; „reciproc exclusiv“ → „incompatibil între ele“. TITLE-PHRASE site 2 (the last line), „Mă numesc Aleph.“, „priveam privitul“ and every [ECHO] line untouched; no sensory verb added for Aleph. Fidelity audit: no content shift.
