#!/usr/bin/env python3

# fichier: oxitool.py
# auteur: Rony MOUNIAPIN, Adrien CELLIER
# entreprise: POP School
# date: 10/11/2020

import scan_vuln
import oxi_db

#appel des fonctions de connection, creation et fermeture de la base de données
oxi_db.connect_db()
oxi_db.create_table()
oxi_db.db_close()
#appel de la fonction scan et envoi resultats de la scan_vuln
scan_vuln.scan_et_envoi_resultats()


