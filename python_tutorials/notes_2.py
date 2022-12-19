#Mad Libs Game
color = input ('Enter your color: ')
plural_noun = input ('Enter your plural noun: ')
celebrity = input ('Enter your celebrity: ')

print ('Roses are ' + color)
print (plural_noun  + ' are blue')
print ('I love ' + celebrity)

#lists

frends = ['Jim', 'Bob', 'John', 'Sebastian', 'Damian']
frends [2] = 'Jan'
print (frends [2:])

lucky_numbers = [2, 4, 8, 14, 20, 22, 40]
frends = ['Jim', 'Bob', 'John', 'Sebastian', 'Damian', 'Mati', 'Patryk']

frends.extend (lucky_numbers)
frends.append ('Janusz')
frends.insert (1, 'Monika')
frends.remove ('Jim')
frends.sort()

print (frends.index ('Janusz'))
print (frends.count('Janusz'))
print (frends)