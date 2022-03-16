#Afficher une pyramide
#Exercice 12 de l'epreuve de l'air : air11.py
import sys


def pyramide(n1, n2):
    #recuperation des lignes
    tab = []
    res = []
    mot = str(n1)
    i = 0
    j = 1
    tab.append(str(n1))
    while i < int(n2)-1:
        j = i
        while j >= i:
            mot = mot+str(n1)+str(n1)
            j = j-1
        tab.append(mot)
        i = i+1
    #ajout espace pour la forme de la pyramide
    k = int(n2)
    l = int(n2)
    mot = ""
    for n in tab:
        k = l
        while k > 0:
            mot = mot+" "
            k = k-1
        l = l-1
        res.append(str(mot)+str(n)+str(mot))
        mot = ""
    return res


def is_int(tab):
    try:
        tab[1]
        return True
    except:
        return False


sys.argv.pop(0)
if len(sys.argv) == 2:
    if is_int(sys.argv) == True:
        res = pyramide(sys.argv[0], sys.argv[1])
        str_res = "\n".join(map(str, res))
        print(str_res)
    else:
        print("Error : arguments must be integer")
else:
    print("Error : 2 arguments needed")
