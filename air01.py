#Split en fonction
#Exercice 2 de l'epreuve de l'air : air01.py
import sys

#retourne un tableau avec tous les mots de la phrase


def separateur(str_a_couper):
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

#compare chaque mot avec le separateur


def ma_fonction(str_a_couper, str_separateur):
    tableau = []
    tab = separateur(str_a_couper)
    #tab_mot = []
    liste_mot = ""
    tab.append(str_separateur)
    for mot in tab:
        if str(mot) == str(str_separateur):
            tableau.append(liste_mot)
            liste_mot = ""
            mot = ""
        else:
            liste_mot = liste_mot+" "+mot
            mot = ""
        mot = ""
    return tableau


if len(sys.argv) != 3:
    print("Error : 2 arguments needed")
else:
    res = ma_fonction(sys.argv[1], sys.argv[2])
    if res == []:
        print("Error : separator not found ")
    else:
        for r in res:
            print(r)
