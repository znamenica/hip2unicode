# -*- coding: UTF-8 -*-

from hip2unicode.representations import cslav

cslav2ucs = (
{
    
    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)

    cslav.Izhica_double_gravis: u'm',
    cslav.izhica_double_gravis: u'M' ,
},
{
    cslav.Wide_E: u'Е' ,
    cslav.wide_e: u'є' ,

    cslav.Yat: u'Э' ,
    cslav.yat: u'э' ,

    cslav.Ksi: u'X' ,
    cslav.ksi: u'x' ,

    cslav.Wide_O : u'O',
    cslav.wide_o: u'o' ,

    cslav.Omega: u'W' ,
    cslav.omega: u'w' ,

    cslav.Ole: u'Q' ,
    cslav.ole: u'q',

    cslav.Ot: u'T' ,
    cslav.ot: u't' ,

    cslav.Psi: u'P' ,
    cslav.psi: u'p' ,

    cslav.Fita: u'F',
    cslav.fita: u'f',

    cslav.Ja: u'Я' ,
    cslav.ja: u'я',

    cslav.Small_Yus: u'Z' ,
    cslav.small_yus: u'z' ,
},
{
    cslav.aspiration + cslav.acute: u'4' ,
    cslav.acute + cslav.aspiration: u'4' ,
    cslav.aspiration + cslav.gravis: u'5' ,
    cslav.gravis + cslav.aspiration: u'5' ,
},
{
    cslav.aspiration: u'3' ,
    cslav.acute: u'1' ,
    cslav.gravis: u'2' ,
    cslav.circumflex: u'6' ,
    cslav.titlo: u'7' ,

    cslav.paerok: u'8' ,
    cslav.glagol_titlo: u'g' ,
    cslav.dobro_titlo: u'd' ,
    cslav.on_titlo: u'b' ,
    cslav.rcy_titlo: u'>' ,
    cslav.slovo_titlo : u'c',
    cslav.kher_titlo: u'<' ,
    cslav.cherv_titlo: u'?' ,
    
},
{
    cslav.Oy: u'U' ,
    cslav.oy: u'u' ,
},
{   
    cslav.Uk: u'У' ,
    cslav.uk: u'у' ,

    ur'\u0131': u'i', # U+0131 LATIN SMALL LETTER DOTLESS I
},
)
