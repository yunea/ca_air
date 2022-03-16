#Melanger deux tableaux tries
#Exercice 9 de l'epreuve de l'air : air08.py
import sys


def two_tabs(args):
    tab1 = []
    tab2 = []
    b = False
    for arg in args:
        if b == True:
            tab2.append(arg)
        elif arg == 'fusion':
            b = True
        else:
            tab1.append(arg)
    return tab1, tab2


def sorted_fusion(tab1, tab2):
    l1 = len(tab1)-1
    l2 = len(tab2)-1
    res = []
    for t1 in tab1:
        t1 = int(t1)
        for t2 in tab2:
            t2 = int(t2)
            if t1 > t2:
                if in_tab(res, t1) == False and in_tab(res, t2) == False:
                    res.append(t2)
            elif t2 > t1:
                if in_tab(res, t1) == False and in_tab(res, t2) == False:
                    res.append(t1)
            else:
                res.append(t2)
    #ajout dernier nombre
    l1 = len(tab1)-1
    l2 = len(tab2)-1
    if tab1[l1] > tab2[l2]:
        res.append(int(tab1[l1]))
    else:
        res.append(int(tab2[l2]))
    return res


def in_tab(tab, a):
    res = False
    for n in tab:
        if n == a:
            res = True
            break
    return res


def need_fusion(tab):
    res = False
    for n in tab:
        if n == "fusion":
            res = True
    return res


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
            if n == "fusion":
                continue
            else:
                int(n)
        return True
    except:
        return False


def same_len(tab1, tab2):
    if len(tab1) == len(tab2):
        return True
    else:
        return False


sys.argv.pop(0)
if need_fusion(sys.argv) == True:
    if is_int(sys.argv) == True:
        tab1, tab2 = two_tabs(sys.argv)
        if same_len(tab1, tab2) == True:
            if is_sorted(tab1) == True and is_sorted(tab2) == True:
                res = sorted_fusion(tab1, tab2)
                str_res = " ".join(map(str, res))
                print(str_res)
            else:
                print("Error : at least one list is not sorted")
        else:
            print("Error : lists must be the same lenght")
    else:
        print("Error : must be integer in lists")
else:
    print("Error : need 'fusion' keyword")
