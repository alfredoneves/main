#!/usr/bin/python3

import crypt
import sys
from queue import Queue
import threading

# USE INPUT INSTEAD OF ARGV TO AVOID ERRORS IN SALT AND PASS_HASH BECAUSE OF $
try:
	salt = sys.argv[1]
	pass_hash = sys.argv[2]
	wordlist = sys.argv[3]
except:
	print("Usage: ./hash_cracker.py [id_salt] [hash] [wordlist]")
	sys.exit()

with open(wordlist, "r") as file:
	for line in file.readlines():
		continue
		#print(line.strip())

def hash_test(word):
	print(salt)
	hashed = crypt.crypt(word, salt)
	print(hashed)
	
hash_test("123")
