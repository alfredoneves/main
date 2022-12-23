#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

for i in range(100, 200):
	try:
		r = requests.get(f"http://10.10.145.36:8080/users/{i}.html")
		soup = BeautifulSoup(r.text, "lxml")
		div = soup.find("div", class_="card")
		name = div.h1.text
		content = div.find_all("p")
		print(name)
		for c in content:
			print(c.text)
		print("---" * 30)
	except:
		continue

