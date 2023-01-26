#!/usr/bin/python3
# this tool works with permutations, so the lenght of the word can't be smaller than the size chosed

import itertools
import sys
import string

def wordlist(word="", brute=False, size=8):
	if brute:
		chars = string.ascii_letters + string.digits + "!@#$%¨&*()-_+=<>,.:;?çÇ/\|'[{]}"
		result = itertools.permutations(chars, size)
		for i in result:
			print("".join(i))
	else:
		result = itertools.permutations(word, size)
		for i in result:
			print("".join(i))

try:
	word = sys.argv[1]
	size = sys.argv[2]
except:
	print("Usage: ./wordlist_generator.py [word | --brute] [size]")
	sys.exit()
	
if word == "--brute":
	wordlist(brute=True, size=int(size))
else:
	wordlist(word, size=int(size))

