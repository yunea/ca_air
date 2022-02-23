#Sur chacun d'entre eux (addition et soustraction)
#Exercice 6 de l'epreuve de l'air : air05.py
import sys


def calcul(tab, num):
    res = []
    for n in tab:
        res.append(int(n)+int(num))
    return res


def is_int(tab):
    try:
        for n in tab:
            int(n)
        return True
    except:
        return False


args = sys.argv
args.pop(0)
int_only = is_int(args)
l = len(args)
cal = args[l-1]
args.pop(l-1)
if int_only == True:
    res = calcul(args, cal)
    str_res = " ".join(map(str, res))
    print(str_res)
else:
    print("Error : arguments must be integer")
