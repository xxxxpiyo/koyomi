# -*- coding: utf-8 -*-

MONTH_NUM = ["",0,2,0,2,2,4,5,6,7,8,9,10]
MOON_NAME = {
    0: u"新月",
    3: u"三日月",
    7.5: u"上弦の月",
    10: u"十日夜",
    13: u"十三夜",
    15: u"満月",
    16: u"十六夜",
    17: u"立待月",
    18: u"居待月",
    19: u"寝待月",
    20: u"更待月",
    22.5: u"下弦の月",
     26: u"二十六夜",
     29: u"晦"
}

def getAoM(year,month,day):

    ret = ()
    print year
    print month
    print day
    year_num = (int(year)-11) % 19 * 11
    month_num = MONTH_NUM[int(month)]
    aom = (year_num + month_num + int(day)) % 30

    try:
        ret = (aom, MOON_NAME[aom])
    except:
        ret = (aom, None)

    return ret




