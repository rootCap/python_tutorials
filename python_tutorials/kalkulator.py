liczba1 = float(input('Podaj pierwszą liczbę: '))
symbol = input('Podaj symbol działania: ')
liczba2 = float(input('Podaj drugą liczbę: '))

if symbol == '+':
    print (liczba1 + liczba2)
elif symbol == '-':
        print (liczba1 - liczba2)
elif symbol == '*':
        print (liczba1 * liczba2)
elif symbol == '/':
        print (liczba1 / liczba2)
else:
    print ("bład")
        