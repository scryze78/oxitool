#!/usr/bin/env python3
# auteur Kamel, Sekou, Josoa
# date 13/11/2020
import scannefichier
import oxi_db

#appel les fonctions de la base de données oxi_db
oxi_db.connect_db()
oxi_db.create_table()
#appel de la fonction scan_files_envoi_resultats et envoi les resultats du scanne
scannefichier.scan_files_envoi_resultats()
oxi_db.db_close()
