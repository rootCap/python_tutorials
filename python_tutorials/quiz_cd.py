from quiz_cd_funkcja import Quiz
pytanie = [
    'Nietopierz to:\n (a) Ssak\n (b) Ptak\n (c) Gad\n',
    'Portret damy z gonostajem namalował:\n (a) Leonadro da Vinci\n (b) Michał Anioł\n (c) Jan Matejko\n',
    'Papierek lakmusowy stosuje się do:\n (a) Poziomu cukru we krwi\n (b) pH\n (c) Objetsść roztworu\n'
]

odpowiedzi = [
    Quiz (pytanie [0], 'a'),
    Quiz (pytanie [1], 'a'),
    Quiz (pytanie [2], 'b')
]
def test_quiz (odpowiedzi):
    wynik = 0
    for pyt in odpowiedzi:
        odpowiedz_uz = input (pyt.pytanie)
        if odpowiedz_uz == pyt.odp:
            wynik += 1
    print ('Twój wynik to ' + str(wynik) + '/' + str(len(odpowiedzi)))
test_quiz(odpowiedzi)