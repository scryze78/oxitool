#!/usr/bin/env python3

# fichier: scan_vuln.py
# auteur: Adrien Cellier
# entreprise: POP School
# date: 10/11/2020

"""Ce module cherche les vulnérabilités à la propagation d'un ransomware sur un système.
Il est prévu pour permettre à oxitool.py d'en appeler scan_et_envoi_resultats() ou les fonctions séparément.
Si il est lancé en programme principal, c'est la fonction main() qui sera executée.
"""

import subprocess
import sys

# pip3 install getmac
import getmac

import oxi_db

VULMAP = "C:\\Users\\inti\\Documents\\GitHub\\Vulmap-Windows\\vulmap-windows.ps1"


def scan():
    #lancement de la commande VULMAP
    p = subprocess.Popen(["powershell.exe", VULMAP])
    #récupération de la sortie dans out et les erreurs dans err.
    out, err = p.communicate()
    print(out)


def main():
    #mac = getmac.get_mac_address()
    scan()

#Lance main() si le script est lancé comme programme principal.
if __name__ == '__main__':
    main()
