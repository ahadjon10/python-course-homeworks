# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:43:28 2023

@author: user
"""

"""
15-DARS. LUG'AT ELEMENTLARI BILAN ISHLASH
Lug'at ichida ro'yxat, lug'at ichida lug'at?



Avvalgi darsimizda lug'at bilan tanishdik, va lug'atdagi elementlarga kalit so'z bo'yicha murojat qilishni o'rgandik. Lug'atlar katta yoki kichik bo'lishi mumkin. Ba'zida lug'atdagi barcha kalitlarni yoki qiymatlarni bilmasligimiz mumkin. Bunday holatda qanday yo'l tutamiz?

Ushbu darsimizda lug'at elementlarini turli usullar yordamida chiqarishni o'rganamiz.

.items() METODI
Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.

talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba_0.items())
dict_items([('ism', 'alijon'), ('familiya', 'shamshiyev'), ('yosh', 22), ('fakultet', 'matematika'), ('kurs', 4)])
Bu metodni to'g'ridan-to'g'ri emas, for tsikli yordamida chaqirish orqali lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.

for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")
Kalit: ism
Qiymat: alijon 

Kalit: familiya
Qiymat: shamshiyev 

Kalit: yosh
Qiymat: 22 

Kalit: fakultet
Qiymat: matematika 

Kalit: kurs
Qiymat: 4 

Yuoqirdagi kodda, talaba_0 lug'atidagi har bir kalit va qiymat juftligini konsolga chiqardik. E'tibor bering, for tsiklida biz bir emas ikkita o'zgaruvchi yaratib oldik (kalit va qiymat).

Bu usul ba'zi lug'atlardagi ma'lumotlarni chiroyli ko'rinishda chiqarish uchun juda qo'l keladi.

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
Alining telefoni iphone x
Valining telefoni galaxy s9
Olimning telefoni mi 10 pro
Orifning telefoni nokia 3310
.keys() METODI
Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa, .keys() metodidan foydalanishimiz mumkin.

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())
dict_keys(['olma', 'anor', 'uzum', 'anjir', 'shaftoli'])
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
Do'kondagi mahsulotlar:
Olma
Anor
Uzum
Anjir
Shaftoli
Yuqoridagi kodimizda, for tsiklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.

for tsikli va if sharti yordamida lug'atdagi biror qiymatlarni alohida chiqarishimiz ham mumkin:

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
Anor 20000 so'm
Uzum 40000 so'm
Yuqordagi kodga e'tibor bering. Biz avval borolik degan ro'yxat yaratdik (uyga bozor qilyapmiz), keyin esa mahsulotlar lug'atidagi har bir mahsulotni bizdagi bozorlik ro'yxati bilan solishtirdik. Agar mahsulot bizning bozorlik ro'yxatimizda bo'lsa, uning narxini konsolga chiqardik.

Quyidagi misolda esa aksincha, bozorlik ro'yxatidagi har bir elementni do'kondagi mahsulotlar bilan solishtiramiz, va mahsulot do'konda yo'q bo'lsa, do'konga murojat qoldiramiz:

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
Iltimos, do'koningizga non ham olib keling
Iltimos, do'koningizga baliq ham olib keling
LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
Pythonda lug'at elementlari siz (foydalanuvchi) kiritgan tartibda saqlanadi. Agar lug'at elementlarini alifbo bo'yicha chiqarish talab qilinsa, sorted() funktsiyasidan foydalanamiz.

print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
Do'konimizdagi mahsulotlar:
Anjir
Anor
Olma
Shaftoli
Uzum
.values() METODI
Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin.

print(telefonlar.values())
dict_values(['iphone x', 'galaxy s9', 'mi 10 pro', 'nokia 3310'])
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
iphone x
galaxy s9
mi 10 pro
nokia 3310
Yuqoridagi usul bilan qiymatlarni chiqrganimizda, lug'atdagi barcha qiymatlar chiqib keladi. Agar, biror qiymat ko'p marta qaytarilsa, konsolga ham ko'p marta chiqib keladi.

Quyidagi misloni ko'raylik:

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
iphone x
galaxy s9
mi 10 pro
nokia 3310
galaxy s9
huawei p30
iphone x
iphone x
Yuoqirdagi natijaga e'tibor bersanigz, bir nechta foydalanuvchilar iphone x va galaxy s9 telefonidan foydalanishar ekan, va bu modellar qayta-qayta konsolga chiqdi.

Buning oldini olish uchun set() funktsiyasidan foydalanishimiz mumkin.

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
Foydalanuvchilar quyidagi telefonlarni ishlatishadi:
galaxy s9
mi 10 pro
nokia 3310
huawei p30
iphone x
Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, set ichidagi elementlar biror tartibda saqlanmaydi, va ularga indeks orqali murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.

AMALIYOT
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

JAVOBLAR
python_words = {
    'integer':'Butun son',
    'float': "O'nlik son",
    'boolean':"Mantiqiy qiymat",
    'for':"Biror amalni qayta-qayta bajarish tsikli",
    'if':'Shartlarni tekshirish operatori'}

for key, value in sorted(python_words.items()):
    print(f"{key.title()} - {value}")
Boolean - Mantiqiy qiymat
Float - O'nlik son
For - Biror amalni qayta-qayta bajarish tsikli
If - Shartlarni tekshirish operatori
Integer - Butun son
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
Dunyo davlatlari:
AQSH
ITALIYA
MALAYZIYA
O'ZBEKISTON
QIRG'IZISTON
QOZOG'ISTON
ROSSIYA
SINGAPUR
TOJIKISTON

Davlatlarning poytaxtlari
Bishkek
Dushanbe
Kuala-Lumpur
Moskva
Nursulton
Rim
Sungapur
Toshkent
Washington D.C.
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
Qaysi davlatning poytaxtini bilishni istaysiz?:Rossiya
ROSSIYAning poytaxti Moskva shahri
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
3 ta taom buyurtma bering.
1-taom:osh
2-taom:non
3-taom:norin
Osh 20000 so'm
Non 4000 so'm
Kechirasiz, bizda norin yo'q.
Hosted on Jovian
View File

"""