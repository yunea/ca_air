#Afficher le contenu
#Exercice 11 de l'epreuve de l'air : air10.py

import sys


def afficher(name):
    try:
        with open(str(name), 'r') as fichier:
            contenu = fichier.read()
        print(contenu)
    except:
        print("Error : file could not be open")


afficher(sys.argv[1])
