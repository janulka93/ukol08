def mocniny(n):
    '''Funce pro argumentem zadané číslo n vytvoří a vrátí další slovník,
    kde budou klíče čísla od jedné do n, a hodnoty k nim jejich druhé mocniny.
    '''
    seznam = []
    for i in range(1, n+1):
        dvojice = (i, i**2)
        seznam.append(dvojice)
    mocniny = dict(seznam)
    return mocniny

n = int(input('Zadej číslo, pro které chceš vytvořit slovník s mocninami: '))

print(mocniny(n))

def soucet_klicu_a_hodnot(slovnik):
    '''
    Funkce sečte a vrátí sumu všech klíčů a sumu všech hodnot ve slovníku, který
    dostane jako argument.
    '''
    klice = 0
    hodnoty = 0
    for klic, hodnota in slovnik.items():
        klice = klic + klice
        hodnoty = hodnota + hodnoty
    soucet = (klice, hodnoty)
    return soucet

print(soucet_klicu_a_hodnot(mocniny(n)))

def vypis_slovnik(slovnik):
    '''
    '''
    for klic, hodnota in slovnik.items():
        print('Klíč', klic, ', hodnota', hodnota)

vypis_slovnik(mocniny(n))
