def pocet_znaku(retezec):
    '''Funkce dostane na argumentu řetězec a vrátí slovník, kde budou jako
    klíče jednotlivé znaky ze zadaného řetězce a jako hodnoty počty výskytů
    těchto znaků v řetězci.
    '''
    seznam = []
    prevod = list(retezec)
    for prvek in prevod:
        if prvek not in seznam:
            dvojice = (prvek, prevod.count(prvek))
            seznam.append(dvojice)
    return dict(seznam)

print(pocet_znaku('hello world'))
