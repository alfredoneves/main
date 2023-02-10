#!/usr/bin/python3
# took from dio, it isn't working, I will make my own

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
	wordlist = []
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code, "lxml")
	
	for each_text in soup.findAll('div', {'class': 'entry-content'}):
		content = each_text.text
		words = content.lower().split()
		
		for each_word in words:
			wordlist.append(each_word)
		clean_wordlist(wordlist)
		
def clean_wordlist(wordlist):	# removes some symbols to avoid interference in the wordlist
	clean_list = []
	symbols = '!@#$%¨&*()[]{}~^?/\|;:<>,. -_=+'
	for word in wordlist:
		for i in range(0, len(symbols)):
			word = word.replace(symbols[i], "")
			if len(word) > 0:
				clean_list.append(word)
		create_dictionary(clean_list)
		
def create_dictionary(clean_list):
	word_count = {}
	
	for word in clean_wordlist:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
			
	for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
		print(key, ":", value)
		
	c = Counter(word_count)
	top = c.most_common(10)
	print(top)
	
if __name__ == '__main__':
	start('https://www.geeksforgeeks.org/taking-input-in-python/?ref=lbp')
