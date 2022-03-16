#Rotation vers la gauche
#Exercice 10 de l'epreuve de l'air : air09.py

import sys


def rotation(tab):
    a = tab[0]
    tab.pop(0)
    tab.append(a)
    return tab


sys.argv.pop(0)
if len(sys.argv) > 1:
    res = rotation(sys.argv)
    str_res = ", ".join(map(str, res))
    print(str_res)
else:
    print("Error : more arguments needed")
