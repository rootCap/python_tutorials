#strings
print ('  /|')  
print (' / |')
print ('/__|')

character_name = 'Emil'
character_age = '30'

print ('Był sobie człowiek o imieniu ' + character_name + ',')
print (character_name + ' miał ' + character_age + ' lat')

character_name = 'Papaja'
character_age = '80'

print ('Bardzo podobało mu się imie ' + character_name + ',')
print ('ale nie chciał mieć ' + character_age + ' lat')

tekst = 'emil the boss'
print ('what\'s up')    
print (tekst[2:8])
print (tekst.index('b'))
print (tekst.replace('boss', 'master of python'))

print ('emil to mistrz '*10)

#numbers
print (2*2)
print (12%5)
print (2*(4+8))

my_number = -30
print (str(my_number) + ' is my favorite number')
print (abs(my_number))
print (pow(2,3))
print (max(my_number, 12))
print (min(my_number, 12))
print (round(3.6))

from math import *
print (floor(3.6))
print (ceil(3.2))
print (sqrt(36))

#user input

user_name = input ('Enter your stupid name user: ')
print ('Hello ' + user_name +'!')

#my idea

tekst_do_mnozenia = input ('Podaj tekst: ')
mnoznik = input ('Podaj ile razy przemnożyć: ')
print ((tekst_do_mnozenia + ' ') * int(mnoznik))

#calculator

num1 = input ('Enter your number: ')
num2 = input ('Enter another number: ')
result = float(num1) + float(num2)
print (result)