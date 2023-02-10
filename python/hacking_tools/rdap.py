#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup

try:
	option = sys.argv[1]
	host = sys.argv[2]
except:
	print("USAGE: ./rdap.py [option] [host]")
	print("OPTIONS:\n-d	# domain\n-i	# ip")
	sys.exit()

if option == "-d":
	r = requests.get(f"https://client.rdap.org/?type=domain&object={host}")
elif option == "-i":
	exit()

soup = BeautifulSoup(r.text, 'lxml')
print(r.text)
card_body = soup.find("div", class_="card-body")
print(card_body)

