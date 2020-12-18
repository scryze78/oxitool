#!/usr/bin/env python3

# fichier: scan_vuln.py
# auteur: Adrien Cellier, Raphaël Aubin
# entreprise: POP School
# date: 18s/12/2020

"""Ce module retourne l'état des ports.
Il est prévu pour permettre à oxitool.py d'en appeler scan_et_envoi_resultats().
"""


import socket


def portscan(port,host):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        sock.connect((host, port))
        return True
    except:
        return False

def scan_et_envoi_resultats():
    host = socket.gethostname()
    liste_resultats = []
    for port in range(0, 65536):
        result = portscan(port,host)
        if(result):
            #print("Port {} OPEN".format(port))
            liste_resultats += [(port,"OPEN")]
        else:
            #print("Port {} CLOSED".format(port))
            liste_resultats += [(port,"CLOSED")]
    #print(liste_resultats)
    return liste_resultats

scan_et_envoi_resultats()
