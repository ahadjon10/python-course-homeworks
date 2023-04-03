list = []
list.append('Farhod')
list.append('MIrzohid')
list.append('Xurshid')
list.append('Hikmatillo')

#print(list)
#print('salom', list[1].title(), 'Play station o\'ynaymizmi')
#print('salom', list[-1].upper(), 'pythonni o\'rganamizmi')

list[0]='Jasur'
#print('salom', list[0].title(), 'Play station o\'ynaymizmi')

#t_shaxslar = ['Buxoriy', 'Mirzo Ulug\'bek']
#z_shaxslar = ['Hazrat', 'O\'tkir Hoshhimov', 'Tohir Malik']
#
#print(f'men tartixiy shaxslardan {t_shaxslar.pop(0)}ni \n'
#       f'zamonaviy shaxslardan esa {z_shaxslar.pop(0)} ni xurmat qilaman')

list.append('Farhod')
list.append('Ka Xurshid')
print(list)
list.remove('Farhod')
print(list)
del list[-1]
print(list)

list.insert(0, "Hushnud")
list.append("Husanboy")
print(list)

gasts=[]
gasts.append(list[0])
gasts.append(list[4])
gasts.append(list.pop(2).upper())
print(gasts)
