#Controle de pass sanitaire
#Exercice 7 de l'epreuve de l'air : air06.py
import sys


def ma_fonction(tab, chaine):
    res = []
    for mot in tab:
        res.append(mot)
    for mot in tab:
        for lettre in mot:
            if lettre == str(chaine).lower():
                res.remove(mot)
            if lettre == str(chaine).upper():
                res.remove(mot)
    return res


def argument(args):
    l = len(args)
    reg = args[(l-1)]
    args.pop(l-1)
    args.pop(0)
    return args, reg


args, reg = argument(sys.argv)
if len(args) >= 1:
    res = ma_fonction(args, reg)
    if res == []:
        print("No match found")
    else:
        str_res = " ".join(map(str, res))
        print(str_res)
else:
    print("Error")
