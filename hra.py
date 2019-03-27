# Úkolem je vytvořit známou skautskou hru „Kdo? S kým? Co dělali?“. Hra se
# hráče zeptá postupně na různé otázky, například „Kdo?“, „S kým?“, „Co dělali?“,
# „Kde?“, „Kdy?“, a nakonec „Proč?“, s tím, že mu umožní na jednu otázku odpovědět
# vícekrát a všechny odpovědi si uloží. Na závěr pak hra z každé sady odpovědí vybere
# náhodně jednu odpověď a z takto vybraných odpovědí složí větu, kterou vypíše
# uživateli. Seznam otázek by mělo být možné změnit v kódu na jednom místě bez zásahu
# do logiky programu.
import random


kdo = input('Kdo? ')
sKym = input('S kým? ')
co = input('Co dělali? ')
kde = input('Kde? ')
kdy = input('Kdy? ')
proc = input('Proč? ')

def ptej_se(otazka)
    '''Část hry, která uživateli pokládá otázky a ukládá je.
    '''
    
