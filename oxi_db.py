#!/usr/bin/env python3
# fichier: oxi_db.py
# auteur: Rony MOUNIAPIN, ZARQOUN kawtar 
# entreprise: POP School
# date: 12/11/2020

import sqlite3

#Definition de la fonction de connection et de creation de la base de donnees
def connect_db():
    connect = sqlite3.connect("oxitool_db.sq3")
    #Creation d'un curseur pour utiliser la base de donnees
    cursor = connect.cursor()
 
#Creation des tables
def create_table():
    curseur.execute("CREATE TABLE IF NOT EXISTS Fichier (id_fichier integer primary key autoincrement, nom text, extension text, taille integer)")# en attente groupe scan fichier
    curseur.execute("CREATE TABLE IF NOT EXISTS Machine (id_machine integer primary key autoincrement, address_ip text, address_mac text, name text, os_name text, os_flavor text, os_sp text, purpose text, info text)")
    curseur.execute("CREATE TABLE IF NOT EXISTS Vulnerabilite (id_vuln integer primary key autoincrement, mac_address text, protocol text, port text, state text, service_name text, service product text, service_version text, cpe text)")
    curseur.execute("CREATE TABLE IF NOT EXISTS Service (id_service integer primary key autoincrement,)")#en attente premiere itération
    curseur.execute("CREATE TABLE IF NOT EXISTS port (id_port integer primary key autoincrement,)")#en attente premiere itération
    
#Mise en place du CRUD: CREATE, READ, UPDATE, DELETE.
# Definition des fonctions d'insertion des différentes tables
def insert_fichier(nom, extension, taille):
    #Mise en place de tuples pour la sécurisation de SQLI
    nom_f = (nom,)
    extension_f = (extension,)
    taille_f = (taille,)
    #cursor.execute('request')
    request= [(nom_f, extension_f, taille_f)]
    c.executemany('insert into stocks values (?,?,?)', request)
    connection.commit()

def insert_machine():
    cursor.execute('INSERT')

def insert_vuln(mac_addr, protocol, port, state, service_name, service_product, service_version, cpe):
    #Mise en place de tuples pour la sécurisation de SQLI
    mac_addr_vuln = (mac_addr,)
    protocol_vul = (protocol,) 
    port_vul = (port,)
    state_vul = (state,)
    s_name_vul = (service_name,)
    s_product_vul = (service_product,)
    s_version_vul = (service_version,)
    cpe_vul = (cpe,)
    #cursor.execute(request)
    request = [(mac_addr_vuln, protocol_vul, port_vul, state_vul, s_name_vul, s_product_vul, s_version_vul, cpe_vul)]
    c.executemany('insert into stocks values (?,?,?,?,?,?,?,?)', request) ##pour enregister les resultats dans DB
    connection.commit()
def insert_service():
    cursor.execute('INSERT')

def insert_desc_port():
    cursor.execute('INSERT')

#Definition des fonctions d'affichage des différentes tables
def select_fichier():
    #cursor.execute('SELECT')
    curseur.execute("SELECT * FROM oxitool_db.Fichier WHERE name = '...'")
    resultat = list(curseur)
    #print(resultat)
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

#Définition de la fonction de fermeture de la base de donnees
def db_close():
  connect.close()
