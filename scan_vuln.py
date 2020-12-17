#!/usr/bin/env python3

# fichier: scan_vuln.py
# auteur: Adrien Cellier, Raphaël Aubin
# entreprise: POP School
# date: 17/12/2020

"""Ce module retourne l'état des ports.
Il est prévu pour permettre à oxitool.py d'en appeler scan_et_envoi_resultats().
"""


import socket


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return True
    except:
        return False


def scan_et_envoi_resultats():
    liste_resultats = []
    host = socket.gethostname()
    for port in range(0, 65536):
        result = portscan(port)
        if(result):
            #print("Port {} OPEN".format(port))
            liste_resultats += [(port,"OPEN")]
        else:
            #print("Port {} CLOSED".format(port))
            liste_resultats += [("{}".format(port),"CLOSED")]
    #print(liste_resultats)
    return liste_resultats
