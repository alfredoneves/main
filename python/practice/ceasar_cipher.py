#!/usr/bin/python3

import sys
import string

try:
	if len(sys.argv) == 3:
		rotation = int(sys.argv[1])
		phrase = sys.argv[2]
	else:
		rotation = 3
		phrase = sys.argv[1]
except:
	print("Usage: ./ceasar_cipher.py [rotation (optional)] [string]")
	sys.exit()
	

def ceasar(phrase, rotation):
	alphabet = string.ascii_letters
	size = len(phrase)
	new_phrase = ""
	
	# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
	
	for i in range(size):
		character = phrase[i]
		if character.isalpha() and character != "ç":
			if character.isupper():
				location = alphabet.find(character)	# index of the character in the alphabet
				new_location = (location + rotation) % 52
				if new_location < 26:
					new_location += 26
				new_phrase += alphabet[new_location]
			else:
				print("")
		else:
			new_phrase += character
	return new_phrase
	
print(ceasar(phrase, rotation))
	
