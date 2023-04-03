# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 07:54:12 2023

@author: user
"""

login = ['alisher','aziza','yasina','umar']
new_login = str(input('Marhamat loginni kiiriting!!!'))
if new_login in login:
    print("Iltimos boshqa login tanlang bunisi band qilingan!!!")
else:
    login.append(new_login)
    print(f'sizning loginigiz {new_login}')