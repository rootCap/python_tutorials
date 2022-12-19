
# Zmienia samogłoski na literkę g

def tlumacz (slowo):
    tl_slowo = ''
    for literka in slowo:
        if literka in ('AEIOUaeiou'):
            tl_slowo = tl_slowo + 'g'
        else:
            tl_slowo = tl_slowo + literka
    return tl_slowo

print (tlumacz(input('Wpisz słowo do tłumaczenia: ')))
