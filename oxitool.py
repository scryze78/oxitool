#!/usr/bin/env python3

# fichier: oxitool.py
# auteur: Rony MOUNIAPIN, Adrien CELLIER
# entreprise: POP School
# date: 05/01/2021 --Rony
import scan_file
import scan_vuln
import oxi_db


#Appel de la fonction create_connection() et permet de récupérer le curseur de connection dans la variable "conn"
conn = oxi_db.create_connection(r"H:\Sqlite\db\pornhub.db")
PATH = "C:\\"
liste_ini = []
#Si on a réussi à creer la base on fait ce qu'il y a dans le main
if conn is not None:
  #appel des fonctions de connection, creation et fermeture de la base de données
  oxi_db.create_table(conn)
  #appel de la fonction recherche de fichier
  var_fichier = scan_file.recherche(liste_ini, PATH)
  #appel de la fonction d'insertion de fichiers
  oxi_db.insert_file(conn, var_fichier)
  #appel de la fonction scan et envoi resultats de la scan_vuln
  vulnerabilites = scan_vuln.scan_et_envoi_resultats()
  #appel de la fonction d'insertion de vulnérabilités
  oxi_db.insert_port(conn, vulnerabilites)
  """:param conn pour la connection à la bdd
     :param vulnerabilites tuple des ports et leurs états """
  oxi_db.db_close(conn)# à voir si je supprime

#sinon erreur
else:
  print ("Erreur! problème de connexion à la base de données")
