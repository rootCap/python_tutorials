
try:
    num = int (input ('Podaj cyfrę: '))
    print (num)
except ZeroDivisionError:
    print ('dzielenie przez zero')
except ValueError:
    print (wartosc nierozpozna)