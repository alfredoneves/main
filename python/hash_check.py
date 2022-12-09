#!/usr/bin/python3

import hashlib

# asks for the files
file1 = input("type the name or the full path to file1: ")
file2 = input("type the name or the full path to file2: ")

# creates the hash objects
hash1 = hashlib.new("sha256")
hash2 = hashlib.new("sha256")

# storages the hash
hash1.update(open(file1, "rb").read())
hash2.update(open(file2, "rb").read())

print(f"{file1}:{hash1.hexdigest()}")
print(f"{file2}:{hash2.hexdigest()}")

# compares the hashes
if hash1.digest() == hash2.digest():
	print("THE FILES ARE EQUAL!")
else:
	print("THE FILES ARE DIFFERENT!")
	
