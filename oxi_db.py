#!/usr/bin/env python3
# fichier: oxi_db.py
# auteur: Rony MOUNIAPIN 
# entreprise: POP School
# date: 30/10/2020

import sqlite3

connect = sqlite3.connect("oxitool.db")          #connection à la base de donnees
cursor = connect.cursor()                        #Creation d'un curseur pour utiliser la base de donnees

                                                 #Mise en place du CRUD: CREATE, READ, UPDATE, DELETE.
                                                 # Definition des fonctions d'insertion des différentes tables
    def insert_fichier():
        cursor.execute('INSERT')

    def insert_machine():
        cursor.execute('INSERT')

    def insert_vuln(protocol, port, state, service_name, service_product, service_version, service_extrainfo, cpe):
        protocol_vul = (protocol,)               #Mise en place de tuples pour la sécurisation de SQLI
        port_vul = (port,)
        state_vul = (state,)
        s_name_vul = (service_name,)
        s_product_vul = (service_product,)
        s_version_vul = (service_version,)
        s_extrainfo_vul = (service_extrainfo,)
        cpe_vul = (cpe,)
        cursor.execute('INSERT')

    def insert_service():
        cursor.execute('INSERT')

    def insert_desc_port():
        cursor.execute('INSERT')

                                                 #Definition des fonctions d'affichage des différentes tables
    def select_fichier():
        cursor.execute('SELECT')

    def select_machine():
        cursor.execute('SELECT')

    def select_vuln():
        cursor.execute('SELECT')

    def select_service():
        cursor.execute('SELECT')

    def select_desc_port():
        cursor.execute('SELECT')

                                                 #Definition des fonctions de modification des différentes tables
    def update_fichier():
        cursor.execute('UPDATE')

    def update_machine():
        cursor.execute('UPDATE')

    def update_vuln():
        cursor.execute('UPDATE')

    def update_service():
        cursor.execute('UPDATE')

    def update_desc_port():
        cursor.execute('UPDATE')

                                                 # Definition des fonctions pour effacer dans les différentes tables
    def delete_fichier():
        cursor.execute('DELETE')

    def delete_machine():
        cursor.execute('DELETE')

    def delete_vuln():
        cursor.execute('DELETE')

    def delete_service():
        cursor.execute('DELETE')

    def delete_desc_port():
        cursor.execute('DELETE')


    def db_close():
     	connect.close()
