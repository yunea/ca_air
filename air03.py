#Chercher l'intrus
#Exercice 4 de l'epreuve de l'air : air03.py

import sys


def no_pair(tab):
    tab2 = []
    for n in tab:
        tab2.append(n)
    res = []
    i = 0
    for n in tab:
        tab2.pop(0)
        while i < len(tab2):
            if str(n) == str(tab2[i]):
                res.append(n)
            i = i+1
        i = 0
    for p in res:
        for n in tab:
            if n == p:
                tab.remove(n)
    return tab


if len(sys.argv) < 3:
    print("Error : more arguments needed")
else:
    args = sys.argv
    args.pop(0)
    res = no_pair(args)
    str_res = " ".join(map(str, res))
    print(str_res)
