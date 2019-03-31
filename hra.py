import random

print('''Ahoj, vítej u této suprové hry. Počítač ti vždy položí otázku a ty
budeš odpovídat, dokud tě to nepřestane bavit. Napíšeš-li "konec", hra skočí
na další otázku, dokud nedojdeš k té poslední.''')

def ptej_se(otazka):
    '''Část hry, která uživateli pokládá otázky a ukládá je.
    '''
    odpovedi = []
    while True:
        odpoved = input(otazka)
        if odpoved != 'konec':
            odpovedi.append(odpoved)
        else:
            break
    return odpovedi

otazky = ['Kdo? ', 'S kým? ', 'Co dělali? ', 'Kde? ', 'Kdy? ', 'Proč? ']
slovnik = {}
for prvek in otazky:
    slovnik[prvek]=ptej_se(prvek)

for odpoved in slovnik.values():
    print(random.choice(odpoved), end=' ')
