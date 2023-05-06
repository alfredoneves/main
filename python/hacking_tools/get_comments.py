#!/usr/bin/python3
# this tool takes an url as argument and retrieves all the comments found

import requests
from bs4 import BeautifulSoup, Comment
import sys

if len(sys.argv) != 2:
	print("Usage: python3 get_comments.py [url]")
	sys.exit()

# checking and receiving url
url = sys.argv[1]
if url[:4] != "http":
	url = "http://" + url
r = requests.get(url)

print(f"analizing url: {url} and printing comments found")
soup = BeautifulSoup(r.text, "lxml")
print("-------------------------------------\n")
for comments in soup.findAll(string=lambda string:isinstance(string, Comment)):
    print(comments)
