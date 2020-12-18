#!/usr/bin/env python3

# fichier: oxitool.py
# auteur: Rony MOUNIAPIN, Adrien CELLIER
# entreprise: POP School
# date: 15/12/2020 --Rony

import scan_vuln
import oxi_db

#Appel de la fonction create_connection() et permet de récupérer le curseur de connection dans la variable "conn"
conn = create_connection(r"chemin_sur_la_clé) """en attente"""
#Si on a réussi à creer la base on fait ce qu'il y a dans le main
if conn is not None:
  create_table(conn)
  #appel des fonctions de connection, creation et fermeture de la base de données
  oxi_db.create_table(conn)
  #appel de la fonction scan et envoi resultats de la scan_vuln
  vulnerabilites = scan_vuln.scan_et_envoi_resultats()
  
  oxi_db.db_close(conn)# à voir si je supprime

#sinon erreur
else:
  print ("Erreur! problème de connexion à la base de données")

