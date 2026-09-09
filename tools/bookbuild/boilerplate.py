"""Localised legal boilerplate — the copyright page, in every edition’s language.

The copyright page is the one page in the book that is pure boilerplate: the
same six or seven statements, in the same order, with only the title, year,
name, imprint and ISBN changing. Nothing about it belongs to the novel, so it
is generated at build time from the strings here rather than being carried as a
file a translator has to re-derive per language.

Adding a language: one entry in `TEXT`. If the edition being built has no entry,
the build falls back to the base language and reports it as a blocker — an
English copyright page in a German book is wrong, but it should be visible in
the proof rather than crash the build.

    Assembly order (lines that have no value are dropped):

        <title>                     italic
        Copyright © <year> <legal name>
        all-rights-reserved
        work-of-fiction
        original-title              translations only
        translator                  translations only, if declared
        cover credit
        Published by <imprint> / <city>
        <edition>, <year>.
        ISBN <isbn> (paperback)
        printed-by

CAVEAT: the non-English strings below are standard rights-page boilerplate, not
legal advice, and they have not been through a native reviewer. Send them
through the same native pass `translations/TRANSLATION-PROMPT.md` mandates for
the prose before that edition is published.
"""

from __future__ import annotations

import re

from . import config as c

# Every key is optional except the ones that carry a value from config, so a
# language may drop a line it does not need (many European rights pages omit
# "printed by", for instance) simply by leaving the key out.
TEXT: dict[str, dict[str, str]] = {
    "en": {
        "heading": "Copyright",
        "reserved": (
            "All rights reserved. No part of this book may be reproduced, stored "
            "in a retrieval system, or transmitted in any form or by any means — "
            "electronic, mechanical, photocopying, recording, or otherwise — "
            "without the prior written permission of the author, except for brief "
            "quotations embodied in reviews."
        ),
        "fiction": (
            "This book is a work of fiction. Names, characters, and incidents are "
            "the products of the author’s imagination. Real places are used "
            "fictitiously; any resemblance to actual persons, living or dead, or "
            "to actual events, is entirely coincidental."
        ),
        "original": "Originally published in English as {original_title}.",
        "translator": "Translated from the English by {translator}.",
        "cover": (
            "Cover art and design by {author}. Cover produced with AI image tools."
        ),
        "published": "Published by {imprint}",
        "edition": "First edition, {year}.",
        "isbn": "ISBN {isbn} (paperback)",
        "printed": "Printed by Amazon in the region of sale.",
    },
    "de": {
        "heading": "Impressum",
        "reserved": (
            "Alle Rechte vorbehalten. Kein Teil dieses Buches darf ohne vorherige "
            "schriftliche Genehmigung des Autors in irgendeiner Form oder mit "
            "irgendwelchen Mitteln — elektronisch, mechanisch, durch Fotokopie, "
            "Aufzeichnung oder auf andere Weise — reproduziert, in einem "
            "Datenverarbeitungssystem gespeichert oder übertragen werden, "
            "ausgenommen kurze Zitate in Rezensionen."
        ),
        "fiction": (
            "Dieses Buch ist ein Werk der Fiktion. Namen, Figuren und Ereignisse "
            "sind Erzeugnisse der Fantasie des Autors. Reale Orte werden fiktiv "
            "verwendet; jede Ähnlichkeit mit tatsächlichen Personen, lebend oder "
            "verstorben, oder mit tatsächlichen Ereignissen ist rein zufällig."
        ),
        "original": (
            "Die englische Originalausgabe erschien unter dem Titel {original_title}."
        ),
        "translator": "Aus dem Englischen von {translator}.",
        "cover": (
            "Covergestaltung und -illustration von {author}. Das Cover wurde mit "
            "KI-Bildwerkzeugen erstellt."
        ),
        "published": "Verlegt von {imprint}",
        "edition": "Erste Auflage, {year}.",
        "isbn": "ISBN {isbn} (Taschenbuch)",
        "printed": "Gedruckt von Amazon in der Region des Verkaufs.",
    },
    "fr": {
        "heading": "Droits d’auteur",
        "reserved": (
            "Tous droits réservés. Aucune partie de ce livre ne peut être "
            "reproduite, stockée dans un système d’archivage ou transmise sous "
            "quelque forme et par quelque moyen que ce soit — électronique, "
            "mécanique, par photocopie, enregistrement ou autre — sans "
            "l’autorisation écrite préalable de l’auteur, à l’exception de brèves "
            "citations insérées dans des critiques."
        ),
        "fiction": (
            "Ce livre est une œuvre de fiction. Les noms, les personnages et les "
            "événements sont le fruit de l’imagination de l’auteur. Les lieux "
            "réels sont utilisés de manière fictive ; toute ressemblance avec des "
            "personnes réelles, vivantes ou décédées, ou avec des événements "
            "réels, serait purement fortuite."
        ),
        "original": "Publié à l’origine en anglais sous le titre {original_title}.",
        "translator": "Traduit de l’anglais par {translator}.",
        "cover": (
            "Illustration et conception de couverture par {author}. Couverture "
            "réalisée à l’aide d’outils de génération d’images par IA."
        ),
        "published": "Publié par {imprint}",
        "edition": "Première édition, {year}.",
        "isbn": "ISBN {isbn} (broché)",
        "printed": "Imprimé par Amazon dans la région de vente.",
    },
    "ro": {
        "heading": "Drepturi de autor",
        "reserved": (
            "Toate drepturile rezervate. Nicio parte a acestei cărți nu poate fi "
            "reprodusă, stocată într-un sistem de regăsire a informațiilor sau "
            "transmisă sub nicio formă și prin niciun mijloc — electronic, "
            "mecanic, prin fotocopiere, înregistrare sau altfel — fără permisiunea "
            "scrisă prealabilă a autorului, cu excepția citatelor scurte incluse "
            "în recenzii."
        ),
        "fiction": (
            "Această carte este o operă de ficțiune. Numele, personajele și "
            "întâmplările sunt rodul imaginației autorului. Locurile reale sunt "
            "folosite în mod fictiv; orice asemănare cu persoane reale, în viață "
            "sau decedate, ori cu evenimente reale este pur întâmplătoare."
        ),
        "original": "Publicată inițial în limba engleză sub titlul {original_title}.",
        "translator": "Traducere din limba engleză de {translator}.",
        "cover": (
            "Ilustrația și designul copertei: {author}. Coperta a fost realizată "
            "cu instrumente de generare a imaginilor bazate pe inteligență "
            "artificială."
        ),
        "published": "Publicată de {imprint}",
        "edition": "Prima ediție, {year}.",
        "isbn": "ISBN {isbn} (broșată)",
        "printed": "Tipărită de Amazon în regiunea de vânzare.",
    },
    "hu": {
        "heading": "Szerzői jog",
        "reserved": (
            "Minden jog fenntartva. A könyv egyetlen része sem sokszorosítható, "
            "nem tárolható adatvisszakereső rendszerben, és nem továbbítható "
            "semmilyen formában és semmilyen eszközzel — elektronikus, mechanikus, "
            "fénymásolásos, hangrögzítéses vagy egyéb úton — a szerző előzetes "
            "írásbeli engedélye nélkül, kivéve a recenziókban szereplő rövid "
            "idézeteket."
        ),
        "fiction": (
            "Ez a könyv fikció. A nevek, a szereplők és az események a szerző "
            "képzeletének szüleményei. A valós helyszínek fiktív módon szerepelnek; "
            "bármely hasonlóság valós — élő vagy elhunyt — személyekkel, illetve "
            "valós eseményekkel a véletlen műve."
        ),
        "original": "Eredetileg angol nyelven jelent meg {original_title} címmel.",
        "translator": "Angolból fordította: {translator}.",
        "cover": (
            "A borító illusztrációja és tervezése: {author}. A borító mesterséges "
            "intelligencián alapuló képalkotó eszközökkel készült."
        ),
        "published": "Kiadja: {imprint}",
        "edition": "Első kiadás, {year}.",
        "isbn": "ISBN {isbn} (papírkötés)",
        "printed": "Nyomtatta az Amazon az értékesítés régiójában.",
    },
    "ru": {
        "heading": "Авторские права",
        "reserved": (
            "Все права защищены. Никакая часть этой книги не может быть "
            "воспроизведена, сохранена в поисковой системе или передана в любой "
            "форме и любыми средствами — электронными, механическими, путём "
            "фотокопирования, записи или иными — без предварительного письменного "
            "разрешения автора, за исключением кратких цитат в рецензиях."
        ),
        "fiction": (
            "Эта книга — художественное произведение. Имена, персонажи и события "
            "являются плодом воображения автора. Реальные места использованы "
            "вымышленным образом; любое сходство с реальными людьми, живыми или "
            "умершими, а также с реальными событиями является случайным."
        ),
        "original": (
            "Оригинальное издание вышло на английском языке под названием "
            "{original_title}."
        ),
        "translator": "Перевод с английского: {translator}.",
        "cover": (
            "Обложка и оформление — {author}. Обложка создана с использованием "
            "инструментов генерации изображений на основе искусственного "
            "интеллекта."
        ),
        "published": "Издано {imprint}",
        "edition": "Первое издание, {year}.",
        "isbn": "ISBN {isbn} (мягкая обложка)",
        "printed": "Отпечатано Amazon в регионе продажи.",
    },
    "uk": {
        "heading": "Авторське право",
        "reserved": (
            "Усі права застережено. Жодну частину цієї книжки не можна відтворювати, "
            "зберігати в пошуковій системі або передавати в будь-якій формі та "
            "будь-якими засобами — електронними, механічними, шляхом "
            "фотокопіювання, запису чи іншим способом — без попереднього "
            "письмового дозволу автора, за винятком коротких цитат у рецензіях."
        ),
        "fiction": (
            "Ця книжка — художній твір. Імена, персонажі та події є плодом уяви "
            "автора. Реальні місця використано у вигаданий спосіб; будь-яка "
            "схожість із реальними людьми, живими чи померлими, або з реальними "
            "подіями є випадковою."
        ),
        "original": (
            "Оригінальне видання вийшло англійською мовою під назвою "
            "{original_title}."
        ),
        "translator": "Переклад з англійської: {translator}.",
        "cover": (
            "Обкладинка та оформлення — {author}. Обкладинку створено за допомогою "
            "інструментів генерації зображень на основі штучного інтелекту."
        ),
        "published": "Видано {imprint}",
        "edition": "Перше видання, {year}.",
        "isbn": "ISBN {isbn} (м’яка обкладинка)",
        "printed": "Надруковано Amazon у регіоні продажу.",
    },
    "sr": {
        "heading": "Ауторска права",
        "reserved": (
            "Сва права задржана. Ниједан део ове књиге не сме се репродуковати, "
            "чувати у систему за претраживање нити преносити у било ком облику и "
            "на било који начин — електронски, механички, фотокопирањем, снимањем "
            "или на други начин — без претходне писмене дозволе аутора, осим "
            "кратких цитата у приказима."
        ),
        "fiction": (
            "Ова књига је дело фикције. Имена, ликови и догађаји плод су ауторове "
            "маште. Стварна места употребљена су на измишљен начин; свака "
            "сличност са стварним особама, живим или мртвим, или са стварним "
            "догађајима је случајна."
        ),
        "original": "Изворно објављено на енглеском језику под насловом {original_title}.",
        "translator": "Превод с енглеског: {translator}.",
        "cover": (
            "Илустрација и дизајн корица: {author}. Корице су израђене помоћу "
            "алата за генерисање слика заснованих на вештачкој интелигенцији."
        ),
        "published": "Издаје {imprint}",
        "edition": "Прво издање, {year}.",
        "isbn": "ISBN {isbn} (меки повез)",
        "printed": "Штампано код Amazon-а у региону продаје.",
    },
}


def has_copyright(lang: str) -> bool:
    return lang in TEXT


def copyright_heading(lang: str | None = None) -> str:
    lang = lang or c.LANG
    return TEXT.get(lang, TEXT[c.BASE_LANG])["heading"]


def copyright_blocks(lang: str | None = None) -> list[tuple[str, list[str]]]:
    """The copyright page as (css class, lines) paragraphs.

    Lines within a paragraph are one visual line each — `<br/>` in HTML, a
    newline in Markdown. A line may contain `*emphasis*`, which each renderer
    turns into its own italic markup. The renderers differ only in that.
    """
    lang = lang or c.LANG
    t = TEXT.get(lang, TEXT[c.BASE_LANG])

    # The original title is a book title quoted inside a sentence, so it is
    # italicised. Lines may carry `*emphasis*`; both renderers honour it.
    base_title = f'*{c.EDITIONS[c.BASE_LANG]["title"]}*'
    translator = (c.EDITIONS[lang].get("translator") or "").strip()
    fields = {
        "author": c.AUTHOR_DISPLAY,
        "imprint": c.IMPRINT,
        "year": c.YEAR,
        "isbn": c.ISBN_PAPERBACK,
        "translator": translator,
        "original_title": base_title,
    }

    def line(key: str) -> str | None:
        raw = t.get(key)
        return raw.format(**fields) if raw else None

    blocks: list[tuple[str, list[str] | None]] = [
        ("cp-title", [c.TITLE]),
        ("", [f"Copyright © {c.YEAR} {c.AUTHOR_LEGAL}"]),
        ("", [line("reserved")]),
        ("", [line("fiction")]),
    ]

    # A translation says what it is a translation of, and by whom.
    if lang != c.BASE_LANG:
        blocks.append(("", [line("original")]))
        if translator:
            blocks.append(("", [line("translator")]))

    blocks.append(("", [line("cover")]))

    # "Published by Independently published" doubles the word — a self-published
    # book states the fact by itself, in any language.
    if c.IMPRINT.strip().lower() in ("independently published",
                                     "unabhängig veröffentlicht"):
        blocks.append(("cp-imprint", [c.IMPRINT, c.IMPRINT_CITY or None]))
    else:
        blocks.append(("cp-imprint", [line("published"), c.IMPRINT_CITY or None]))

    blocks.append(("", [line("edition")]))
    # The ISBN exists only after KDP assigns it. Until then the line is left
    # off rather than printing a bracketed placeholder; --check still reports
    # the placeholder so it cannot be forgotten for the paperback rebuild.
    if not re.search(r"\[[^\]]+\]", c.ISBN_PAPERBACK or ""):
        blocks.append(("", [line("isbn")]))
    blocks.append(("", [line("printed")]))

    out = []
    for css, lines in blocks:
        kept = [ln for ln in (lines or []) if ln and ln.strip()]
        if kept:
            out.append((css, kept))
    return out
