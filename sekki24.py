# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="hasegawa"
__date__ ="$2013/01/23 11:38:37$"


sekki24_DA = [
    {"index":1,"y": -1, "month": 1, "name":u"小寒","D":6.3811,"A":0.242778},
    {"index":2,"y": -1, "month": 1, "name":u"大寒","D":21.1046,"A":0.242765},
    {"index":3,"y": -1, "month": 2, "name":u"立春","D":4.8693,"A":0.242713},
    {"index":4,"y": -1, "month": 2, "name":u"雨水","D":19.7062,"A":0.242627},
    {"index":5,"y": -1, "month": 3, "name":u"啓蟄","D":6.3968,"A":0.242512},
    {"index":6,"y": 0, "month": 3, "name":u"春分","D":21.4471,"A":0.242377},
    {"index":7,"y": 0, "month": 4, "name":u"清明","D":5.6280,"A":0.242231},
    {"index":8,"y": 0, "month": 4, "name":u"穀雨","D":20.9375,"A":0.242083},
    {"index":9,"y": 0, "month": 5, "name":u"立夏","D":6.3771,"A":0.241945},
    {"index":10,"y": 0, "month": 5, "name":u"小満","D":21.9300,"A":0.241825},
    {"index":11,"y": 0, "month": 6, "name":u"芒種","D":6.5733,"A":0.241731},
    {"index":12,"y": 0, "month": 6, "name":u"夏至","D":22.2747,"A":0.241669},
    {"index":13,"y": 0, "month": 7, "name":u"小暑","D":8.0091,"A":0.241642},
    {"index":14,"y": 0, "month": 7, "name":u"大暑","D":23.7317,"A":0.241654},
    {"index":15,"y": 0, "month": 8, "name":u"立秋","D":8.4102,"A":0.241703},
    {"index":16,"y": 0, "month": 8, "name":u"処暑","D":24.0125,"A":0.241786},
    {"index":17,"y": 0, "month": 9, "name":u"白露","D":8.5186,"A":0.241898},
    {"index":18,"y": 0, "month": 9, "name":u"秋分","D":23.8896,"A":0.242032},
    {"index":19,"y": 0, "month": 10, "name":u"寒露","D":9.1414,"A":0.242179},
    {"index":20,"y": 0, "month": 10, "name":u"霜降","D":24.2487,"A":0.242328},
    {"index":21,"y": 0, "month": 11, "name":u"立冬","D":8.2396,"A":0.242469},
    {"index":22,"y": 0, "month": 11, "name":u"小雪","D":23.1189,"A":0.242592},
    {"index":23,"y": 0, "month": 12, "name":u"大雪","D":7.9152,"A":0.242689},
    {"index":24,"y": 0, "month": 12, "name":u"冬至","D":22.6587,"A":0.242752},
]

# 黄経角度から日付を返す
def koukeikaku2date(year, kaku, jisa = 9):
    pass

def get24SekkiDay(year, no = None):
    result = []
    if no == None:
        no = []
        i = 1
        while i <= 24:
            no.append(i)
            i = i + 1

    for n in no:
        sekki = n - 1
        result.append({
            #"year": year + sekki24_DA[sekki]["y"],
            "index": sekki24_DA[sekki]["index"],
            "year": year,
            "month": sekki24_DA[sekki]["month"],
            "name": sekki24_DA[sekki]["name"],
            "day": sekki24Calc(year, n),
        })
    
    return result
        

def sekki24Calc(year, no):
    sekki = no - 1
    result = int(sekki24_DA[sekki]["D"] + sekki24_DA[sekki]["A"] * (year - 1900) - (year - 1900) / 4)
    return result