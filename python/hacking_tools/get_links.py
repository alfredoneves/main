#!/usr/bin/python3
# this tool takes an url as argument and retrieves all the comments found

import requests
from bs4 import BeautifulSoup, Comment
import sys

if len(sys.argv) != 2:
	print("Usage: python3 get_links.py [url]")
	sys.exit()

# checking and receiving url
url = sys.argv[1]
if url[:4] != "http":
	url = "http://" + url
r = requests.get(url)

print(f"analizing url: {url} and printing links found")
soup = BeautifulSoup(r.text, "lxml")
links = []

print("-------------------------------------\n")
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

for i in set(links):
	print(i)

