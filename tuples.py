lands = ['Uzbekistan', 'Deutshland', 'FinlAND', 'Britain']
#print(len(lands))
#print('sorted holda', sorted(lands))
#print('sorted holda reversed', sorted(lands, reverse=True))
#lands.sort()
#print(lands)
#lands.sort(reverse=True)
#print(lands)

#ums = list(range(120,1200,2))
#print(nums)
#print(sum(nums))
#print(max(nums)-min(nums))
#print(len(nums))
#rint(nums[:20])
#rint(nums[-20:])


meals = ['Palov', 'Manty', 'Ssamsa', 'Shashkyk', 'Yoghurt']
zum_fruhstuck = meals[:]
#print(meals, '\n', zum_fruhstuck)
zum_fruhstuck.remove('Yoghurt')
zum_fruhstuck.append('Zuker')
zum_fruhstuck = tuple(zum_fruhstuck)
#zum_fruhstuck[0] = 'shashlik'
print(zum_fruhstuck)
