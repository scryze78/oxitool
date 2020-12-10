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


def scan():
    #$env:TEMP C:\Users\Username\AppData\Local\Temp
    #$env:computername  #computername donne le nom de l'ordinateur.

    #lancement de la commande vulmap
    p = subprocess.Popen(["powershell.exe", VULMAP])
    #récupération de la sortie dans out et des erreurs dans err.
    out, err = p.communicate()
    print(out)
    vulns =
    #retourner une lister de tuples : dans le style [(product, cve, risk_score, vulnerability_detail),(product, cve, risk_score, vulnerability_detail),(product, cve, risk_score, vulnerability_detail)]
    return vulns


def main():
    vulns = scan()
    print(vulns)        #pour le test
    return vulns

#Lance main() si le script est lancé comme programme principal.
if __name__ == '__main__':
    main()