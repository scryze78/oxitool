#!/usr/bin/env python3
# fichier: oxi_db.py
# auteur: Rony MOUNIAPIN, ZARQOUN kawtar
# entreprise: POP School
# date: 05/01/2021 --Rony

import sqlite3
from sqlite3 import Error


# Definition de la fonction de connection et de creation de la base de donnees
def create_connection(db_file):
    """ création de la conncetion à la base de données vers SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


# Creation des tables
def create_table(conn):
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS File (id_file integer primary key autoincrement, name text, extend text, size integer)")  # en attente groupe scan fichier
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Host (id_Host integer primary key autoincrement, ip_address text, mac_address text, name text, os_name text, os_flavor text, os_sp text, purpose text, info text)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Ports (id_Port integer primary key autoincrement, num_port integer, state text)")
    #cur.execute(
     #   "CREATE TABLE IF NOT EXISTS Service (id_service integer primary key autoincrement,)")  # en attente premiere itération
    #cur.execute(
     #   "CREATE TABLE IF NOT EXISTS port (id_port integer primary key autoincrement,)")  # en attente premiere itération



# Mise en place du CRUD: CREATE, READ, UPDATE, DELETE.
# Definition des fonctions d'insertion des différentes tables
def insert_file(conn, file):
    cur = conn.cursor()
    # cursor.execute('request')
    sql_insert_file = """INSERT INTO File (name,extend,size) VALUES ( ?, ?, ?);"""
    cur.executemany(sql_insert_file, file)
    conn.commit()


def insert_host(conn):
    cursor.execute('INSERT')


def insert_port(conn, port):
    cur = conn.cursor()
    # cursor.execute(request)
    sql_insert_port = """INSERT INTO Ports (num_port,state) VALUES (?, ?);"""
    cur.executemany(sql_insert_port, port)
    conn.commit()


def insert_service(conn):
    cur = conn.cursor()
    cur.execute('INSERT')


def insert_desc_port(conn):
    cur = conn.cursor()
    cur.execute('INSERT')


# Definition des fonctions d'affichage des différentes tables
def select_file(conn):
    cur = conn.cursor()
    # cursor.execute('SELECT')
    cur.execute("SELECT * FROM oxitool_db.File WHERE name = '...'")
    resultat = list(cursor)
    # print(resultat)


def select_host(conn):
    cur = conn.cursor()
    cur.execute('SELECT')


def select_vuln(conn):
    cur = conn.cursor()
    cur.execute('SELECT')


def select_service(conn):
    cur = conn.cursor()
    cur.execute('SELECT')


def select_desc_port(conn):
    cur = conn.cursor()
    cur.execute('SELECT')


# Definition des fonctions de modification des différentes tables
def update_file(conn):
    cur = conn.cursor()
    cur.execute('UPDATE')


def update_host(conn):
    cur = conn.cursor()
    cur.execute('UPDATE')


def update_vuln(conn):
    cur = conn.cursor()
    cur.execute('UPDATE')


def update_service(conn):
    cur = conn.cursor()
    cur.execute('UPDATE')


def update_desc_port(conn):
    cur = conn.cursor()
    cur.execute('UPDATE')


# Definition des fonctions pour effacer dans les différentes tables
def delete_file(conn):
    cur = conn.cursor()
    cur.execute('DELETE')


def delete_host(conn):
    cur = conn.cursor()
    cur.execute('DELETE')


def delete_vuln(conn):
    cur = conn.cursor()
    cur.execute('DELETE')


def delete_service(conn):
    cur = conn.cursor()
    cur.execute('DELETE')


def delete_desc_port(conn):
    cur = conn.cursor()
    cur.execute('DELETE')


# Définition de la fonction de fermeture de la base de donnees
def db_close(conn):
    cur = conn.cursor()
    cur.close()
