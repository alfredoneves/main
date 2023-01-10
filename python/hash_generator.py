#!/usr/bin/python3

import hashlib
import sys

try:
	hash_type = sys.argv[1].lower()
	string = sys.argv[2]
except:
	print("example: ./hash_genarator.py [md5,sha1,sha256,sha512,sha3_512] some_string")
	sys.exit()

def hash_generator(h, s):
	if h == "md5":
		result = hashlib.md5(s.encode())	
	elif h == "sha1":
		result = hashlib.sha1(s.encode())
	elif h == "sha256":
		result = hashlib.sha256(s.encode())
	elif h == "sha512":
		result = hashlib.sha512(s.encode())
	elif h == "sha3_512":
		result = hashlib.sha3_512(s.encode())
	else:
		print("hash not suported by the program")
		return False
	return result.hexdigest()
	
result = hash_generator(hash_type, string)
print(result)

