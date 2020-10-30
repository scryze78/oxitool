#!/usr/bin/env python3

# fichier: scan_vuln.py
# auteur: Adrien Cellier
# entreprise: POP School
# date: 30/10/2020

"""Ce module cherche les vulnérabilités à la propagation d'un ransomware sur un système.
Il est prévu pour permettre à oxitool.py d'en appeler scan_et_envoi_resultats() ou les fonctions séparément.
Si il est lancé en programme principal, c'est la fonction main() qui sera executée.

Les fonctions de scan_sV nécessitent d'installer nmap sur le système et d'importer nmap3.
"""
# Nécessite nmap sur le système.

# pip3 install python3-nmap
import nmap3
# pip3 install getmac
import getmac

import oxi_db


def scan_sV(host):
    results = nmap3.Nmap().nmap_version_detection(host)
    return results


def fake_scan_sV(host):
    results = [{'protocol': 'tcp', 'port': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128',
                'service': {'name': 'http', 'product': 'Microsoft IIS httpd', 'version': '10.0', 'ostype': 'Windows',
                            'method': 'probed', 'conf': '10'}, 'cpe': [{'cpe': 'cpe:/o:microsoft:windows'}]},
               {'protocol': 'tcp', 'port': '135', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128',
                'service': {'name': 'msrpc', 'product': 'Microsoft Windows RPC', 'ostype': 'Windows',
                            'method': 'probed', 'conf': '10'}, 'cpe': [{'cpe': 'cpe:/o:microsoft:windows'}]},
               {'protocol': 'tcp', 'port': '445', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128',
                'service': {'name': 'microsoft-ds', 'method': 'table', 'conf': '3'}},
               {'protocol': 'tcp', 'port': '1072', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128',
                'service': {'name': 'http', 'product': 'Apache httpd', 'version': '2.4.46',
                            'extrainfo': '(Win32) mod_fcgid/2.3.9', 'method': 'probed', 'conf': '10'},
                'cpe': [{'cpe': 'cpe:/a:apache:http_server:2.4.46'}]},
               {'protocol': 'tcp', 'port': '1077', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128',
                'service': {'name': 'http', 'product': 'Microsoft IIS httpd', 'version': '10.0', 'ostype': 'Windows',
                            'tunnel': 'ssl', 'method': 'probed', 'conf': '10'},
                'cpe': [{'cpe': 'cpe:/o:microsoft:windows'}]},
               {'protocol': 'tcp', 'port': '1078', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '128',
                'service': {'name': 'http', 'product': 'Microsoft IIS httpd', 'version': '10.0', 'ostype': 'Windows',
                            'method': 'probed', 'conf': '10'}, 'cpe': [{'cpe': 'cpe:/o:microsoft:windows'}]}]
    return results


def envoi_resultats(results, mac):
    for i in results:
        oxi_db.insert_vuln(mac,
                               i.get('protocol', '0'),
                               i.get('port', '0'),
                               i.get('state', '0'),
                               i.get('service', {}).get('name', '0'),
                               i.get('service', {}).get('product', '0'),
                               i.get('service', {}).get('version', '0') + i.get('service', '0').get('extrainfo', ''),
                               i.get('cpe', [{}])[0].get('cpe', '0'))


def affichage_resultats(results, mac):
    for i in results:
        print(mac,
              i.get('protocol', '0'),
              i.get('port', '0'),
              i.get('state', '0'),
              i.get('service', {}).get('name', '0'),
              i.get('service', {}).get('product', '0'),
              i.get('service', {}).get('version', '0') + i.get('service', '0').get('extrainfo', ''),
              i.get('cpe', [{}])[0].get('cpe', '0'))


def scan_et_envoi_resultats():
    host = "127.0.0.1"
    mac = getmac.get_mac_address()
    results = scan_sV(host)
    envoi_resultats(results, mac)


def main():
    host = "127.0.0.1"
    mac = getmac.get_mac_address()
    results = scan_sV(host)
    affichage_resultats(results, mac)


if __name__ == '__main__':
    main()