# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="hasegawa"
__date__ ="$2013/01/23 15:05:53$"

import sekki24

if __name__ == "__main__":
    #print sekki24.sekki24Calc(2013, 2)
    #print sekki24.get24SekkiDay(2013,[1,2,3,4])
    #print "aho"
    for year in [2013,2014,2015]:
        result = sekki24.get24SekkiDay(year)
        for i in result:
            print "{0},{1},,{1},,1,,,,,,,,".format(
                i["name"].encode("utf-8"),
                str(i["year"]) + "/" + str(i["month"]) + "/" + str(i["day"]))