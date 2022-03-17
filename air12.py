#Le roi des tris
#Exercice 11 de l'epreuve de l'air : air12.py
#Pas possible avec bcp de nombre -> lie au code, la puissance de calcul ?

import sys


def echange(t, i, j):
    t[i], t[j] = t[j], t[i]


def is_sorted(tab):
    i = 0
    res = True
    for n in tab:
        if int(n) > int(tab[i-1]):
            res = False
            break
        elif i-1 < 0:
            continue
        i = i+1
    return res


def partionner(t, premier, dernier):
    pivot = t[premier]
    gauche = premier
    droite = dernier
    flag = 0
    while flag == 0:
        while t[droite] >= pivot and droite >= gauche:
            droite = int(droite) - 1
        if droite >= gauche:
            echange(t, gauche, droite)
            pivot = t[droite]
        while gauche <= droite and t[gauche] <= pivot:
            gauche = int(gauche) + 1
        if gauche <= droite:
            echange(t, gauche, droite)
            pivot = t[gauche]
        if int(droite) < int(gauche):  # condition d’arret
            flag = 1
    return droite


def tri_rapide(t, premier, dernier):
    if (int(premier) < int(dernier)):
        pivot = partionner(t, premier, dernier)
        tri_rapide(t, premier, pivot-1)
        tri_rapide(t, pivot+1, dernier)
    return t


def is_int(tab):
    try:
        for n in tab:
            int(n)
        return True
    except:
        return False


sys.argv.pop(0)
if len(sys.argv) > 1 and len(sys.argv) < 5:
    if is_int(sys.argv) == True:
        res = tri_rapide(sys.argv, 0, len(sys.argv)-1)
        str_res = " ".join(map(str, res))
        print(str_res)
    else:
        print("Error : arguments must be integer")
else:
    print("Error : between 2 and 4 arguments needed")
