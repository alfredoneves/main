#!/usr/bin/python3
# this script sends requests to the target to check if a certain subdomain exists

import requests
import sys

try:
	domain = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print('./subdomain_brute.py [domain] [wordlist]')
	print('EXP: ./subdomain_brute.py nmap.org subdomains.txt')
	sys.exit()
	
sub_list = open(wordlist).read() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f'http://{sub}.{domain}' 

    try:
        requests.get(sub_domains)
    except requests.ConnectionError: 
        pass
    
    else:
        print(f'Valid domain: {sub_domains}')
