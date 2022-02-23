#Un seul a la fois
#Exercice 5 de l'epreuve de l'air : air04.py


import sys


def no_same(chaine):
    tab2 = []
    for n in chaine:
        tab2.append(n)
    res = []
    mot = ""
    i = 1
    for car in chaine:

        if i == len(tab2):
            mot = mot+car
            break
        elif str(car) == str(tab2[i]):
            res.append(car)
        else:
            mot = mot+car
        i = i+1
    return mot


if len(sys.argv) != 2:
    print("Error : 1 argument needed")
else:
    res = no_same(sys.argv[1])
    print(res)
    #str_res = " ".join(map(str, res))
    #print(str_res)
