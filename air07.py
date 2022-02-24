#Insertion dans un tableau trié
#Exercice 7 de l'epreuve de l'air : air06.py

import sys


def insertion(tab, element):
    element = int(element)
    i = 0
    new_tab = []
    for n in tab:
        n = int(n)
        if n > element and int(tab[i-1]) < element:
            new_tab.append(element)
        elif i-1 < 0:
            new_tab.append(n)
        else:
            new_tab.append(n)
        i = i+1
    l = len(tab)
    new_tab.append(tab[l-1])
    return new_tab


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


def is_int(tab):
    try:
        for n in tab:
            int(n)
        return True
    except:
        return False


sys.argv.pop(0)
if len(sys.argv) > 2:
    if is_int(sys.argv) == True:
        if is_sorted(sys.argv) == False:
            l = len(sys.argv)
            element = sys.argv[(l-1)]
            sys.argv.pop(l-1)
            res = insertion(sys.argv, element)
            str_res = " ".join(map(str, res))
            print(str_res)
        else:
            str_res = " ".join(map(str, sys.argv))
            print(str_res)
    else:
        print("Error : arguments must be integer")
elif len(sys.argv) == 2:
    if is_int(sys.argv) == True:
        if is_sorted(sys.argv) == False:
            print(sys.argv[1]+" "+sys.argv[0])
        else:
            str_res = " ".join(map(str, sys.argv))
            print(str_res)
    else:
        print("Error : arguments must be integer")
else:
    print('Error : more arguments needed')
