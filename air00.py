#Split
#Exercice 1 de l'epreuve de l'air : air00.py
import sys
def ma_fonction(str_a_couper, str_separateur):
    str_c=""
    tableau=[]
    mot=""
    # chaque separateur est recherche
    for separateur in str_separateur:
        #ajout du separateur a la fin de la phrase
        str_c=str_a_couper+separateur
        for caractere in str_c:
            #si le caractere n'est pas un separateur le caractere est ajoute au mot
            if str(caractere)!=str(separateur):
                mot=str(mot)+str(caractere)
            else:
                #si le mot est le meme que la chaine a couper, on continue
                if str(mot)==str(str_a_couper):
                    mot=""
                    continue
                #sinon on ajoute le mot au tableau
                else:
                    tableau.append(mot)
                    mot=""
        mot=""
    return tableau


args=sys.argv
separateurs = "\n\t "
if len(args)!=2:
    print("Error : 1 argument needed")
else:
    res = ma_fonction(args[1], separateurs)
    if res==[]:
        print("Error : no separator found ")
    else:
        for mot in res:
            print(mot)
