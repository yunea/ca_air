#Meta exercice
#Exercice 12 de l'epreuve de l'air : air13.py

import os
import re
import random
from collections import OrderedDict

#liste de tous les noms de scripts


def files():
    #recuperer les fichiers airXX.py present dans le repertoire
    list_files = {}
    f = os.popen('ls -al').read()
    regex = re.compile("air\d\d.py")
    list_files = regex.findall(f)
    #supprimer le fichier air13.py de la liste
    i = 0
    for file in list_files:
        if file == "air13.py":
            list_files.pop(i)
        i = i+1
    #print(list_files)
    return list_files


#liste de tous les arguments pour chaque scripts


def arguments():
    tab = {"air00.py": ["Bonjour les gars", "Bonsoir les gars", "Salut les gars"],
           "air01.py": ["Crevette magique dans la mer des étoiles/la", "Poisson fluorescent dans l'océan de papillons/dans", "Dauphin volant parmis une nuée d'hirondelle/une"],
           "air02.py": ["je/teste/des/trucs/ ", "je/me/fais/plaisir/ ", "j'aime/les/fruits/ "],
           "air03.py": ["1/2/3/4/3/2/1", "1/2/3/4/5/6/5/3/2/1", "10/9/8/9/10"],
           "air04.py": ["Hello milady,  bien ou quoi ??", "Hello, howw arre  you??", "Comment çaa vva chezz toii?"],
           "air05.py": ["1/2/3/4/5/+2", "1/3/5/7/-3", "5/8/9/11/-1"],
           "air06.py": ["Michel/Albert/Thérèse/Benoît/t", "Margot/Samy/Morgane/Hortence/o", "Sidonie/Alice/Lucie/Laure/l"],
           "air07.py": ["1/3/4/2", "2/4/8/9/10/7", "1/5/8/12/23/36/18"],
           "air08.py": ["10/20/30/fusion/15/25/35", "11/16/30/fusion/7/24/27", "12/50/86/fusion/34/62/89"],
           "air09.py": ["Michel/Albert/Thérèse/Benoît", "Margot/Samy/Morgane/Hortence", "Sidonie/Alice/Lucie/Laure"],
           "air10.py": ["exo_air10.txt", "test1.txt", "test2.txt"],
           "air11.py": ["0/5", "o/7", "X/4"],
           "air12.py": ["6/4/5", "9/3/8", "5/3/7"]
           }
    return tab


#comparer les fichiers du dictionaire d'arguments et ceux presents dans le repertoire


def test_file(list_files, list_arg):
    res = {}
    for file in list_files:
        for f in list_arg.keys():
            if file == f:
                res[file] = True
    for file in list_files:
        try:
            res[file]
        except:
            res[file] = False
    for file in list_arg:
        try:
            res[file]
        except:
            res[file] = False
    return res

#execution des scripts et recuperation des resultats dans une variable


def exec_cmd(arguments, file_in_repo):
    str_args = ''
    res = {}
    i = 0
    j = 1
    k = i = random.randint(1, 3)
    t = k
    while k > 0:
        for file, status in file_in_repo.items():
            if status == False:
                res[file] = "Error"
            else:
                str_args = ''
                i = random.randint(0, 2)
                args = arguments[file][i].split("/")
                for arg in args:
                    str_args = str_args+'"'+arg+'" '
                macommande = "python3 "+file+" "+str(str_args)
                res[file+".("+str(j)+"/"+str(t)
                    + ")"] = os.popen(macommande).read()
        k = k-1
        j = j+1
    return res

#test : si error est present dans le resultat -> failure sinon success


def recup_status(resultats):
    status = {}
    regex = re.compile(r"[E-e]rr")
    for file, resultat in resultats.items():
        match = regex.match(resultat)
        if match:
            status[file] = "failure"
        else:
            status[file] = "success"
    return status


def afficher(old_status):
    #trier les fichiers dans l'ordre alphabetique
    status = OrderedDict(sorted(old_status.items(), key=lambda t: t[0]))
    #recuperation des noms de fichier sans .py
    file_name = []
    for file, stat in status.items():
        file_name = file.split(".")
        print(file_name[0]+" "+file_name[2]+" : "+stat)


#-------------main-------------
#test des fichiers dans le repertoire
file_in_repository = test_file(files(), arguments())
#execution des commandes et recuperation des resultats dans un dict
res_cmd = exec_cmd(arguments(), file_in_repository)
#recuperation des status de chaque execution
res_status = recup_status(res_cmd)
#affichage du resultat
afficher(res_status)
