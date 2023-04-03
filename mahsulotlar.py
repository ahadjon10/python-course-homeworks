# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

mahsulotlar =['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun'] 
savat = []
for i in range(5):
    mahsulot = str(input("Mahsulot nomii kiriting  "))
    savat.append(mahsulot)
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"ha bizda {mahsulot} bor!!")
    else:
        print(f"bizda {mahsulot} topilmadi")
            