#!/usr/bin/env python3

# fichier: scanDeVulnerabilites.py
# auteur: Adrien Cellier
# entreprise: POP School
# date: 30/10/2020

# Nécessite nmap sur le système.

# pip3 install python3-nmap
import nmap3
# pip3 install getmac
import getmac


# import module_bdd.py


def scan(host):
    # results = nmap3.Nmap().nmap_version_detection(host)
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
        module_bdd.insert_vuln(mac,
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


def main():
    host = "127.0.0.1"
    mac = getmac.get_mac_address()
    results = scan(host)
    affichage_resultats(results, mac)


if __name__ == '__main__':
    main()

# Explorer https://github.com/Tengrom/Python_nmap/blob/master/README.md
