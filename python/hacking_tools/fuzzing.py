#!/usr/bin/python
import requests

def fuzzing(url, wordlist):
	with open(wordlist, "r") as file:
		for word in file:
			url_word = url + word.strip()
			r = requests.get(url_word)
			print(url_word + "---" + str(r.status_code))
		
url = "https://nmap.org/"
wordlist = "wordlist"
fuzzing(url, wordlist)

