def pocet_znaku(retezec):
    '''Funkce dostane na argumentu řetězec a vrátí slovník, kde budou jako
    klíče jednotlivé znaky ze zadaného řetězce a jako hodnoty počty výskytů
    těchto znaků v řetězci.
    '''
    seznam = []
    for i in range(len(retezec)):
        while True:
            dvojice = (retezec[i], retezec[i].count())
            if retezec[i] not in dvojice:





        #
        # seznam = []
        # for i in range(1, n+1):
        #     dvojice = (i, i**2)
        #     seznam.append(dvojice)
        # mocniny = dict(seznam)
        # return mocniny
