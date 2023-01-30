#!/usr/bin/python3

from urllib.request import urlopen
import json

url = "https://ipinfo.io/json"
answer = urlopen(url)
data = json.load(answer)

for k,v in data.items():
	print(k, v)


