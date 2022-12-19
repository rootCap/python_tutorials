tajne_slowo = 'szczylu'
strzal = ''
n = 0
ilosc_prob = 3
przekroczenie = False

while strzal != tajne_slowo and not(przekroczenie):
    if n < ilosc_prob:
        strzal = input ('Podaj słowo: ')
        n += 1
    else:
         przekroczenie = True

if przekroczenie:
    print ('You lose!!')
else:
    print ('Wygrałeś!!!')