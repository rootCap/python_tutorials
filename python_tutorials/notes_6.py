from notes_6_funkcja import Qizowanie

lista_pytan = [
    'Jak wabi się twój pies:\n a)Papaja\n b)Rex\n c)Burek\n',
    'Przy jakiej ulicy mieszkasz:\n a)Spisaka\n b)Prawnicza\n c)Melcera\n',
    'Kto namalował damę z gronostajem:\n a)Jan Matejko\n b)Leonardo da Vinci\n c)Michał Anioł\n',
    'Kto lideruje w tabeli ekstraklasy:\n a)Legia Warszawa\n b)Lech Poznań\n c)Ursus Warszawa\n'
]

odp = [
    Qizowanie (lista_pytan [0], 'a'),
    Qizowanie (lista_pytan [1], 'c'),
    Qizowanie (lista_pytan [2], 'b'),
    Qizowanie (lista_pytan [3], 'a')
]

def test (odp):
    wynik = 0
    for odpowiedz in odp:
        user_input = input (odpowiedz.lista)
        user_input = user_input.lower()
        if user_input == odpowiedz.odpowiedz:
            wynik += 1
        elif user_input is not('abc'):
            print ('Nie ma takiej odpowiedzi, spróbuj ponownie!')  
    print ('Twój wynik to ' + str(wynik) + '/' + str(len(odp)) )   

      


test (odp) 
