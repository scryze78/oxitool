#!/usr/bin/env python3
# auteur: Adrien, Rony, Kamel, Sekou, Josoa
# date 05/01/2021 Rony
import os


def recherche(liste, path):
    try:
        dirList= os.listdir(path)
        liste_result = liste
        for fname in dirList:
            #    print(fname)
            chemin=path+"\\"+fname
            if os.path.isfile(chemin):
                r = os.path.splitext(fname)
                print(r[0], r[1], os.path.getsize(chemin))
                liste_result += [(r[0], r[1], os.path.getsize(chemin))]
            #        envoyer(fname, os.path.getsize(chemin))
            elif os.path.isdir(chemin):
                recherche(liste_result, chemin)
        #print("etape 2")
        return liste_result
    except PermissionError:
        pass






