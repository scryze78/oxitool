#!/usr/bin/env python3

# fichier: scan_vuln.py
# auteur: Adrien Cellier
# entreprise: POP School
# date: 10/11/2020

"""Ce module cherche les vulnérabilités à la propagation d'un ransomware sur un système.
Il est prévu pour permettre à oxitool.py d'en appeler scan_et_envoi_resultats() ou les fonctions séparément.
Si il est lancé en programme principal, c'est la fonction main() qui sera executée.

Ce script utilise Vulmap pour analyser les vulnérabilités.

Nous développons deux implémentations en parallèle :
Les fonctions _a correspondent à la récupération des résultats de powershell directement dans des variables pour
les transférer à la base de données.
Les fonctions _b correspondent à l'export du résultat dans un fichier texte, puis à la récupération des données pour
les transférer à la base de données.
"""


import subprocess
import sys

# TODO : utiliser powershell au lieu de getmac pour récupérer le mac.
# pip3 install getmac
import getmac

import oxi_db

VULMAP = "C:\\Users\\inti\\Documents\\GitHub\\Vulmap-Windows\\vulmap-windows.ps1"


def scan_a():
    #lancement de la commande vulmap
    p = subprocess.Popen(["powershell.exe", VULMAP])
    #récupération de la sortie dans out et des erreurs dans err.
    out, err = p.communicate()
    print(out)


def scan_b():
    #% TEMP % and % TMP % C:\Users\Username\AppData\Local\Temp
    #$env:computername  #computername donne le nom de l'ordinateur.

    #TODO : Vérifier que le fichier oxitool.tmp n'existe pas.
    #lancement de la commande vulmap
    p = subprocess.run(["powershell.exe", "Write-Output $env:TEMP"])
    print(p)
    #p = subprocess.run(["powershell.exe", VULMAP+" > $env:TEMP\\oxitool.tmp"])
    #print(p)
    #while open('oxitool.tmp')


#oxi_db.insert_vuln() fait la liaison avec la base de données.
def envoi_resultats(mac, results):
    oxi_db.insert_vuln(mac, results.product, results.cve, results.risk_score, results.details)

#alternative à envoi_resultats, pour le test.
def afficher_resultats(mac, results):
    print(mac, results.product, results.cve, results.risk_score, results.details)


def scan_et_envoi_resultats():
    #TODO : utiliser powershell au lieu de getmac pour récupérer le mac.
    mac = getmac.get_mac_address()
    results = scan()
    envoi_resultat(mac, results)


def main():
    scan_a()
    scan_b()


#Lance main() si le script est lancé comme programme principal.
if __name__ == '__main__':
    main()
