#dostlar = ['Hasan', 'Husan', 'Karim', 'Salim', 'Vali']
#for kimsa in dostlar:
#    print("Assalomu Alaykum ", kimsa, ' akasi. shu to\'y boridi mobodo!!!')
#print(f"kod {len(dostlar)} marta takrorlanipti")
#

#ords = list[range(11,100,2)]
#for i in ords:
#    print(i)
#    i.append(i**3)
#    print(f"{i} ning kubi {ords}")
#

#kinolar = []
#for n in range(5):
#    kinolar.append(input(f"{n+1}-yoqtirgan kinoyingiz"))
#print("kinolar", kinolar)
#

# Foydalanuvchidan bugun nechta odam bilan
# uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)
