# -*- coding: UTF-8 -*-

"""
HIP to Civil Russian

Перекодировка в русскую гражданку.

"""

from hip2unicode.representations.RE import *
from hip2unicode.representations.hip import *
from hip2unicode.representations import antconc

ACCENT = u'\u0301'

# Для удаления ударений в односложных словх
SINGLE_SYLLABLE_WITHOUT_ACCENT = (
    ur'(' +
          ur'(?:^|[^аАбБвВгГдДеЕжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ{0}])'.format(ACCENT) +
          ur'[бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩъЪьЬ]*?' +
          ur'[аяеоуюиыАЯЕОУЮИЫ]' +
    ur')' +
    ACCENT +
    ur'(' +
          ur'[бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩъЪьЬ]*?' +
          ur'(?:[\,\.\!\?\;\s]|$|[^аАбБвВгГдДеЕжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ{0}])'.format(ACCENT) +
    ur')',
                                       ur'\g<1>\g<2>')

conversion = (
    (ur'<\(\(>', u'«'),      # замена кавычек <((>
    (ur'<\)\)>', u'»'),      # <))>
    (ur'<->',    u'\u2014'), # тире EM DASH

    # удаление ненужных html-тегов 
    (ur'<p>',    u''),
    (ur'<a.*?>', u''),
    (ur'</a>',   u''),
    (ur'<br>',   u''),
    (ur'<hip>',  u''),
    (ur'</hip>',     u''),
    (ur'<title>',    u''),
    (ur'</title>',   u''),
    (ur'<pre>',      u''),
    # hip-нормализация
    # ...
    # удаление ненужной разметки
    # киноварь
    (ur'%<',    u''),
    (ur'%>',    u''),

    (ur'%\(',   u''),
    (ur'%\)',   u''),

    (ur'%\[',   u''),
    (ur'%\]',   u''),

    (ur'\([cсCС]\.\ *\d+\)',    u''),

    (ur'%{![^{}]+?{[^{}]*?}[^{}]*?}',   u''),
    (ur'%{![^{}]+?}',                   u''),
    (ur'%{Глава`}',                     u'Глава '),
    (ur'%t',                            u''),

    # сноски
    # <сноска 1> ::= *{  <текст сноски> *  <текст сноски> }
    (ur'\*{.*?\*.*?}',          u''),
    # <сноска 2> ::= **{ <текст сноски> ** <текст сноски> }
    (ur'\*\*{.*?\*\*.*?}',      u''),

    # Знаки типикона для обозначения разных типов служб (шестеричная,
    # полиелейная и т.п.)
    (ur'<\(\+\)>',  u''), #     <(+)>   Бдение под великие праздники
    (ur'<\\\+/>',   u''), #     <\+/>   Бдение
    (ur'<\+>',      u''), #      <+>    Полиелей
    (ur'<\(:\.>',   u''), #     <(:.>   Славословие или шестеричная служба
    (ur'<М\\р>',    u''), #     <М\р>

    # символ "бреве" над буквой, иногда кавыка (?)
    (ur'\\\@',      u''), #     \@
    (ur'\\\[\@\]',  u''), #     \[@]

    # настоящие сноски
    # Имеют вид:
    #
    #    <text> ::= <текст, к которому относится сноска>
    #    <note> ::= <текст сноски>
    #
    #    1) <text>@{<note>}
    #    2) @<text>@{@<note>@}
    #    3) @@<text>@@{@@<note>@@}
    #

    (ur'\{\s+\@',   u'{@'),
    (ur'\@\s+\}',   u'@}'),

    # звездочки для поющих на клиросе
    (ur'\*',    u''),
    # разделения на строки -- //
    # и разделители для поющих на клиросе -- /
    (ur'/',    u''),
    # широкая омега
    (ur'<_w>',  u'о'),
    (ur'<_W>',  u'О'),
    # (сверх)узкое о
    (ur'<о_>',  u'о'), # кирил.
    (ur'<o_>',  u'о'), # лат.
    # разные зело и земли
    (ur'<з>',    u'з'),
    (ur'<_з>',   u'з'),

    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)
    (A, u'А'),
    (a, u'а'),

    (B, u'В'),
    (b, u'в'),

    (E, u'Е'),
    (e, u'е'),

    (ur's', u'з'),
    (ur'S', u'З'),
    (i_without_dot, ur'\u0131'), # U+0131 LATIN SMALL LETTER DOTLESS I

    (K, u'К'),
    (k, u'к'),

    (M, ur'М'),
    (m, ur'м'),

    (H, u'Н'),
    (h, u'н'),

    (O, u'О'),
    (o, u'о'),

    (P, u'Р'),
    (p, u'р'),

    (C, u'С'),
    (c, u'с'),

    (T, u'Т'),
    (t, u'т'),

    (X, u'Х'),
    (x, u'х'),

    (V_double_gravis, antconc.CAPITAL_IZHICA),
    (v_double_gravis, antconc.SMALL_IZHICA),

    (Ole, u'О'),
    (ole, u'о'),

    (Wide_E, u'Е'),
    (wide_e, u'е'),

    (Yat, u'Е'),
    (yat, u'е'),

    (V, antconc.CAPITAL_IZHICA),
    (v, antconc.SMALL_IZHICA),

    (Ksi, u'Кс'),
    (ksi, u'кс'),

    (Wide_O, u'О'),
    (wide_o, u'о'),

    (Ot, u'От'),
    (ot, u'от'),

    (Psi, u'Пс'),
    (psi, u'пс'),

    (F, u'Ф'),
    (f, u'ф'),

    (J_a, u'Я'),
    (j_a, u'я'),

    (Ja, u'Я'),
    (ja, u'я'),

    (equal_sign, ur''),  # ur'’',
                         # U+2019 RIGHT SINGLE QUOTATION MARK :
                         # single comma quotation mark

    (ur'\\[бБ]', ur'\Б'),
    (ur'\\[вВ]', ur'\В'),
    (ur'\\[гГ]', ur'\Г'),
    (ur'\\[дД]', ur'\Д'),
    (ur'\\[жЖ]', ur'\Ж'),
    (ur'\\[зЗ]', ur'\З'),
    (ur'\\[кК]', ur'\К'),
    (ur'\\[лЛ]', ur'\Л'),
    (ur'\\[мМ]', ur'\М'),
    (ur'\\[нН]', ur'\Н'),
    (ur'\\[оО]', ur'\О'),
    (ur'\\[пП]', ur'\П'),
    (ur'\\[рР]', ur'\Р'),
    (ur'\\[сС]', ur'\С'),
    (ur'\\[тТ]', ur'\Т'),
    (ur'\\[{0}{1}]'.format(antconc.SMALL_FITA, antconc.CAPITAL_FITA),
                 ur'\Ф'),
    # ^ нельзя писать ur'\\[fF]', т.к. они уже ранее были заменены на
    # антконковские фиты.

    (ur'\\[хХ]', ur'\Х'),
    (ur'\\[цЦ]', ur'\Ц'),
    (ur'\\[чЧ]', ur'\Ч'),
    (ur'\\[шШ]', ur'\Ш'),
    (ur'\\[ъЪ]', ur'\Ъ'),

    (Oy, u'У'),
    (oy, u'у'),

    (W, u'О'),
    (w, u'о'),

    (ur'(?<!_)' + Y, u'У'),
    (ur'(?<!_)' + y, u'у'),

    (ur'i', u'и'),
    (ur'I', u'И'),

    (ur'_у', u'у'),
    (ur'#', u'\u0482'),  # знак тысячи

    (ur'\ {2,}', u' '),  # два и более пробелов заменяем на один
    (ur"['`\^]", ACCENT),

    (ur'([Аа])[Пп]\\С[Лл]', ur'\g<1>постол'),
    (ur'([Аа])п\\Стол',     ur'\g<1>постол'),
    (ur'([Бб])[Гг]~',       ur'\g<1>ог'),
    (ur'([Бб])ж~тв',        ur'\g<1>ожеств'),
    (ur'([Бб])ж~',          ur'\g<1>ож'),
    (ur'([Бб])ж\\Ств',      ur'\g<1>ожеств'),
    (ur'([Бб])з~',          ur'\g<1>оз'),
    (ur'([Бб])л~г',     ur'\g<1>лаг'),
    (ur'([Бб])л~ж',     ur'\g<1>лаж'),
    (ur'([Бб])л~з',     ur'\g<1>лаз'),
    (ur'([Бб])л\\Гв',   ur'\g<1>лагов'),
    (ur'([Бб])лг\\Дт',  ur'\g<1>лагодат'),
    (ur'([Бб])лг\\Св',  ur'\g<1>лагослов'),
    (ur'([Бб])лг\\Сл',  ur'\g<1>лагосл'),
    (ur'([Бб])лг\\С',   ur'\g<1>лагос'),
    (ur'([Бб])ч\\Ден',  ur'\g<1>огородичен'),
    (ur'([Бб])ц\\Д',    ur'\g<1>огородиц'),
    (ur'([Вв])л\\Дк',   ur'\g<1>ладык'),
    (ur'([Вв])л\\Дц',   ur'\g<1>ладыц'),
    (ur'([Вв])л\\Дчц',  ur'\g<1>ладычиц'),
    (ur'([Вв])л\\Дч',   ur'\g<1>ладыч'),
    (ur'ѵ\\Гл',         ur'вангел'),     # Евангел...
    (ur'ѵ\\Г',          ur'ванг'),       # Евангел...
    (ur'гг[е~]л',       ur'нгел'),       # ангел
    (ur'([Гг])л~',      ur'\g<1>лагол'),
    (ur'([Гг])л\\В',    ur'\g<1>лав'),
    (ur'([Гг])д\\Снь',  ur'\g<1>осподень'),
    (ur'([Гг])д\\Св',   ur'\g<1>осподев'),
    (ur'([Гг])д\\С',    ur'\g<1>оспод'),
    (ur'([Гг])п\\Сж',   ur'\g<1>оспож'),
    (ur'([Дд])в~д',     ur'\g<1>авид'),
    (ur'([Дд])в~',      ur'\g<1>ев'),
    (ur'([Дд])в\\Ств',  ur'\g<1>евств'),
    (ur'([Дд])с~',      ur'\g<1>ус'),
    (ur'([Дд])х~',      ur'\g<1>ух'),
    (ur'([Дд])ш~',      ur'\g<1>уш'),
    (ur'([Ии])~с',      ur'\g<1>сус'),
    (ur'([Ии])и~л',     ur'\g<1>зраил'),
    (ur'([Кк])р~с',     ur'\g<1>рес'),
    (ur'([Кк])р~ш',     ur'\g<1>реш'),
    (ur'([Кк])р~щ',     ur'\g<1>рещ'),
    (ur'([Кк])р\\Ст',   ur'\g<1>рест'),
    (ur'([Кк])р\\Сни',  ur'\g<1>ресени'),  # К сожалению это правило
    # не 100%-ное, потому что, например, для формы ``воскрСнiи`` встречается
    # как предложный падеж существительного ВОСКРЕСЕНИЕ, так и мн.ч.
    # прилагательного ВОСКРЕСНЫЙ, хотя последний случай довольно редкий. Также
    # это правило будет работать ещё хуже в текстах с ненормированной
    # орфографией.

    (ur'([Кк])р\\С',    ur'\g<1>рес'),
    (ur'([Кк])\\Ср',    ur'\g<1>рес'),
    (ur'([Мм])\\Др',    ur'\g<1>удр'),
    (ur'([Мм])л~тв',    ur'\g<1>олитв'),
    (ur'([Мм])л\\Днцъ', ur'\g<1>ладенец'),
    (ur'([Мм])л\\Дн',   ur'\g<1>ладен'),
    (ur'([Мм])л\\Срд',  ur'\g<1>илосерд'),
    (ur'([Мм])л\\Ст',   ur'\g<1>илост'),
    (ur'([Мм])л\\С',    ur'\g<1>илос'),
    (ur'([Мм])т~р',     ur'\g<1>атер'),
    (ur'([Мм])т~',      ur'\g<1>ат'),
    (ur'([Мм])р~и',     ur'\g<1>ари'),
    (ur'([Мм])\\Рк',    ur'\g<1>ярек'),   # Имярек
    (ur'([Мм])ч~нк',    ur'\g<1>ученик'),
    (ur'([Мм])ч~нц',    ur'\g<1>учениц'),
    (ur'([Мм])ч~нч',    ur'\g<1>ученич'),
    (ur'([Мм])ч~н',     ur'\g<1>учен'),
    (ur'([Мм])ц\\С',    ur'\g<1>есяц'),
    (ur'([Нн])б~с',     ur'\g<1>ебес'),
    (ur'([Нн])б\\Сс',   ur'\g<1>ебес'),
    (ur'([Нн])б\\С',    ur'\g<1>ебес'),
    (ur'([Нн])б~',      ur'\g<1>еб'),
    (ur'([Нн])л\\Д',    ur'\g<1>едел'),
    (ur'([Нн])н~',      ur'\g<1>ын'),
    (ur"([Оо])ч~ь",     ur'\g<1>течь'),
    (ur"([Оо])ч~ес",    ur'\g<1>течес'),
    (ur"([Оо])ч~",      ur'\g<1>тч'),
    (ur"([Оо])ц~ъ",     ur'\g<1>тец'),
    (ur"([Оо])ц~",      ur'\g<1>тц'),
    (ur'([Пп])ра\\З\\b[\.]!', ur'\g<1>раз.'), # праЗ(.) --> праз.[дник-]
    (ur'([Пп])рв\\Днъ', ur'\g<1>раведен'),
    (ur'([Пп])рв\\Дн',  ur'\g<1>раведн'),
    (ur'([Пп])р\\Дтч',  ur'\g<1>редтеч'), # Предтеча
    (ur'([Пп])р\\Дт',   ur'\g<1>редт'),   # Предтеча
    (ur'([Пп])рп\\Дб',  ur'\g<1>реподоб'),
    (ur'([Пп])реп\\Дб', ur'\g<1>реподоб'),
    (ur'([Пп])р\\Ор',   ur'\g<1>рор'),    # Пророк
    (ur'([Пп])р\\Сн',   ur'\g<1>рисн'),
    (ur'([Пп])р\\Ст',   ur'\g<1>рест'),
    (ur'([Пп])рч\\Ст',  ur'\g<1>речист'),
    (ur'([Пп])\\Скп',   ur'\g<1>ископ'),  # епископ
    (ur'([Пп])\\Ск',    ur'\g<1>иск'),
    (ur'([Рр])ж\\Ств',  ur'\g<1>ождеств'),
    (ur'([Рр])\\Сл',    ur'\g<1>усал'),   # Иерусалим
    (ur'([Сс])л~нц',    ur'\g<1>олнц'),
    (ur'([Сс])н~',      ur'\g<1>ын'),
    (ur'([Сс])п~с',     ur'\g<1>пас'),
    (ur'([Сс])п\\Сн',   ur'\g<1>пасен'),
    (ur'([Сс])п\\С',    ur'\g<1>пас'),
    (ur'([Сс])р\\Дц',   ur'\g<1>ердц'),
    (ur'([Сс])р\\Дч',   ur'\g<1>ердеч'),
    (ur'([Сс])т~',      ur'\g<1>вят'),
    (ur'([Сс])тр\\Ст',  ur'\g<1>траст'),
    (ur'([Сс])\\Х',     ur'\g<1>тих'),
    (ur'([Сс])т\\Хр',   ur'\g<1>тихир'),
    (ur'([Сс])щ~',      ur'\g<1>вящ'),
    (ur'([Тт])р\\Оц',   ur'\g<1>роиц'),
    (ur'([Тт])р\\Оч',   ur'\g<1>роич'),
    (ur'([Тт])р\\Ст',   ur'\g<1>рисвят'),
    (ur'([Хх])р\\Ст',   ur'\g<1>рист'),
    (ur'([Цц])р~к',     ur'\g<1>ерк'),
    (ur'([Цц])р~',      ur'\g<1>ар'),
    (ur'([Цц])р\\С',    ur'\g<1>арс'),
    (ur'([Цц])\\Ср',    ur'\g<1>арс'),
    (ur'([Чч])л~в',     ur'\g<1>елов'),
    (ur'([Чч])~нк',     ur'\g<1>еник'),
    (ur'([Чч])~нц',     ur'\g<1>ениц'),
    (ur'([Чч])~тл',     ur'\g<1>ител'),
    (ur'([Чч])н~к',     ur'\g<1>еник'),
    (ur'([Чч])н~ц',     ur'\g<1>ениц'),
    (ur'([Чч])н~',      ur'\g<1>ен'),
    (ur'([Чч])\\Стн',   ur'\g<1>естн'),
    (ur'([Чч])т\\Сн',   ur'\g<1>естн'),
    (ur'([Чч])\\Ст',    ur'\g<1>ист'),
    (ur'([Чч])т\\С',    ur'\g<1>ист'),
    (ur'([Чч])т~л',     ur'\g<1>ител'),

    (ur'а' + antconc.SMALL_IZHICA,  u'ав'),
    (ur'е' + antconc.SMALL_IZHICA,  u'ев'),
    (ur'а{0}{1}'.format(ACCENT, antconc.SMALL_IZHICA), u'а{0}в'.format(ACCENT)),
    (ur'е{0}{1}'.format(ACCENT, antconc.SMALL_IZHICA), u'е{0}в'.format(ACCENT)),
    (antconc.SMALL_IZHICA,          u'и'),

    (ur'\\З', u'з'),
    (ur'\\Ъ', u'ъ'),

    (ur'(ъ$)|(ъ(?=[\sБбВбГгДдЖжЗзКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщ,\.;:\?\!]))',
              u''),

    (ur'ъа', u'а'),
    (ur'ъо', u'о'),
    (ur'ъу', u'у'),
    (ur'ъы', u'ы'),
    (ur'ъи', u'ы'),

    (ur'жы', u'жи'),
    (ur'шы', u'ши'),
    (ur'щы', u'щи'),
    (ur'жя', u'жа'),
    (ur'шя', u'ша'),
    (ur'щя', u'ща'),

    # Удаляем ударения у слов с единственным слогом.
    SINGLE_SYLLABLE_WITHOUT_ACCENT,

    # намеренно повторная конвертация, так как за один проход почему-то
    # конвертируется не всегда всё.
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
    SINGLE_SYLLABLE_WITHOUT_ACCENT,
)
