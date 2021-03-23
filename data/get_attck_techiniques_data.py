#!/usr/bin/env python3

import requests as req
import json
import re
import sys

GREEN = '\033[92m'             
RED = '\033[91m'            
BLUE = '\033[94m'           
ENDC = '\033[0m'            
BOLD = '\033[1m' 

usage_help = f'''
{RED}{BOLD}\n[!] Usar el argumento {ENDC}{BOLD}markdown{RED}{BOLD} o {ENDC}{BOLD}clean{ENDC}\n

[*] Ejemplo de uso: \n\n{BLUE}{BOLD}{sys.argv[0]} markdown \n

{sys.argv[0]} clean {ENDC}\n
             '''

if len(sys.argv[1:]) != 1:
    print(usage_help)
    exit()

frmt = sys.argv[1]

try:
    assert frmt in ['markdown', 'clean'], usage_help
except AssertionError as msg:  
    print(msg)
    exit()


#Code used to create the ATT&CK Techinques JSON data
def get_attck_data():

    response = req.get('https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json').json()

    # Dict Key ==> (str) techinque name 
    # Dict Value == (tuple) techinque ID , technique description
    techniques = {}

    if  frmt == 'markdown':

        for item in response['objects']:
            if 'type' in item:
                if 'attack-pattern' in item['type']:
                    try:
                        techniques[item['name']] = (item['external_references'][0]['external_id'], item['description'])
                    except:
                        pass
    else:

        for item in response['objects']:
            if 'type' in item:
                if 'attack-pattern' in item['type']:
                    try:
                        descr = re.sub(r"(<code>|</code>)|[\[]|<br>|&lt;|&gt;", '', item['description'])
                        descr = re.sub(r"[\]]", ' ', descr)
                        techniques[item['name']] = (item['external_references'][0]['external_id'], descr)
                    except:
                        pass

    json.dump(techniques, open("attck_techniques.json", "w"))
    print(f'\n{GREEN}{BOLD}[+]{ENDC} {BOLD}Json File saved.{ENDC}\n')


if __name__ == '__main__':
    get_attck_data()