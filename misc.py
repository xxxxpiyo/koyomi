# -*- coding: utf-8 -*-

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="hasegawa"
__date__ ="$2013/01/23 14:35:38$"

#閏年判定
def isUruu(year):
    uruu = False
    if 0 == year % 4:
        uruu = True
    if uruu:
        if 0 == year % 100:
            uruu = False
    
    if uruu == False:
        if 0 == year % 400:
            uruu = True
    
    return uruu