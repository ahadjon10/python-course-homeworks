# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 07:59:47 2023

@author: user
"""
numbers = [2,3,4,5,6,7,8,9,10]
son = int(input("Marhamat sonni kiriting!!!   "))
for num in numbers:
    if son%num == 0:
        print(f'\033[1;33mson {num} ga qoldiqsiz bo\'linadi!\033[0m')
    else:
        print(f'\033[1;31mson {num} ga qoldiqli bo\'linadi!\033[0m')
# Set the color of the text to red
#print("\033[1;31mHello, world!\033[0m")
