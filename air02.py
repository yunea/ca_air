#Concat
#Exercice 3 de l'epreuve de l'air : air02.py
import sys


def str_to_tab(str_a_couper):
    str_separateur = " \n\t"
    str_c = ""
    tableau = []
    mot = ""
    # chaque separateur est recherche
    for separateur in str_separateur:
        #ajout du separateur a la fin de la phrase
        str_c = str_a_couper+separateur
        for caractere in str_c:
            #si le caractere n'est pas un separateur le caractere est ajoute au mot
            if str(caractere) != str(separateur):
                mot = str(mot)+str(caractere)
            else:
                #si le mot est le meme que la chaine a couper, on continue
                if str(mot) == str(str_a_couper):
                    mot = ""
                    continue
                #sinon on ajoute le mot au tableau
                else:
                    tableau.append(mot)
                    mot = ""
        mot = ""
    return tableau


def ma_fonction(array_de_str, separateur):
    chaine = ""
    i = len(array_de_str)
    for mot in array_de_str:
        if i == 1:
            chaine = chaine+mot
        else:
            chaine = chaine+mot+separateur
        i = i-1
    return chaine


if len(sys.argv) < 3:
    print("Error : more arguments needed")
else:
    args = sys.argv
    l = len(args)
    separateur = args[l-1]
    args.pop(l-1)
    args.pop(0)
    res = ma_fonction(args, separateur)
    print(res)
