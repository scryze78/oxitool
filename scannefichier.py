import os # module OS est d'interagir avec votre système d'exploitation
import time # Ce module fournit différentes fonctions liées au temps

start_time = time.time() # Renvoie le temps en secondes depuis epoch(est le point de départ du temps)
PATH="C:\\"
a=0
def recherche(path): # Function
    try: # Le try bloc vous permet de tester un bloc de code pour les erreurs.
        dirList= os.listdir(path) # La méthode listdir() retourne une liste contenant les noms des entrées du répertoire donné par path
        for fname in dirList: # variable contenant les resultats de os.listdir()
            #    print(fname) # Afficher fname
            chemin=path+"\\"+fname # Afficher le chemin + le nom de fichier
            if os.path.isfile(chemin): # La méthode en Python est utilisée pour vérifier si le chemin spécifié est un fichier régulier existant ou non.
                print(fname, os.path.getsize(chemin)) # si la condition est verifier il affiche le chemein + nom de fichier + la taille
                    #envoyer(fname, os.path.getsize(chemin))
            elif os.path.isdir(chemin): # sinon La méthode en Python est utilisée pour vérifier si le chemin spécifié est un répertoire existant ou non
                recherche(chemin) # Appeler  la fonction recherche
    except PermissionError:
        # Si aucune exception n’intervient, la clause except est sautée et l’exécution de l’instruction try est terminée.
        # Si une exception intervient pendant l’exécution de la clause “try”, le reste de cette clause est sauté
        pass  # Cette fonction ne fait rien, mais elle est définie. Sans pass il y aurait une erreur de syntaxe


#recherche(PATH)
variable = recherche(PATH)
print(variable)
print("--- %s seconds ---" % (time.time() - start_time)) # Afficher le temps écouler( exp: --- 129.3752098083496 seconds ---)

import sqlite3
# Definition de la fonction de connection et de creation de la base de donnees
def connect_db():
    connect = sqlite3.connect("oxitool_db.sq3")
    # Creation d'un curseur pour utiliser la base de donnees
    cursor=connect.cursor()


# Creation des tables
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Fichier (id_fichier integer primary key autoincrement, nom text, extension text, taille integer)")
def insert_fichier(nom, extension, taille):
    #Mise en place de tuples pour la sécurisation de SQLI
    nom_f = (nom,)
    extension_f = (extension,)
    taille_f = (taille,)
    #cursor.execute('request')
    request= [(nom_f, extension_f, taille_f)]
    # executemany()méthode effectue une itération dans la séquence de paramètres, passant à chaque fois les paramètres actuels à la execute()
    c.executemany('insert into Fichier values (?,?,?)', request)
    connection.commit()

#oxi_db.insert_scan() fait la liaison avec la base de données oxi_db
#def envoi_resultats(results):
    #oxi_db.insert_scan(results.nom_f, results.extension_f, results.taille_f)

#def affich_resultats(results):
    #print(results.Nom, results.extension, results.taille)