# -*- coding: UTF-8 -*-

from hip2unicode.representations.RE import *
from hip2unicode.representations.antconc import *

conversion = (

    # Сноски и комментарии у нас в текстах заключаются
    # в фигурные скобки, поэтому заменяем их на 
    # двойные круглые скобки при этом перед открывающей
    # круглой скобкой добавляем пробел.
    (u'\{',  u'\u0020(('),
    (u'\}',  u'))'),

    # Знаки кавычек:
    (u'@',  u'\u00B0'),

)
