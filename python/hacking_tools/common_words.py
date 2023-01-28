#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup
import operator

try:
	url = sys.argv[1]
except:
	print("Usage: ./common_words.py [url]")
	sys.exit()
	
def get_html(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	body_text = soup.body.text
	return body_text

def create_dictionary(wordlist):
	word_count = {}
	for word in wordlist:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	for k, v in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True):	# the sorting is with the values because of the key
		print(k,v)
	return word_count
	
wordlist = get_html(url).split()
create_dictionary(wordlist)


