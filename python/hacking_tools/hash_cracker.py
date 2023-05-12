#!/usr/bin/python3

import hashlib
import sys
from queue import Queue
import threading

# USE INPUT INSTEAD OF ARGV TO AVOID ERRORS IN SALT AND PASS_HASH BECAUSE OF $
try:
	salt = input("SALT: ")
	pass_hash = input("password hash: ")
	wordlist = sys.argv[1]
	queue = Queue()
except:
	print("Usage: ./hash_cracker.py [wordlist]")
	sys.exit()

def hash_test(word):
	hash1 = hashlib.new("sha512")
	hash1.update((word + salt).encode())	# is the salt before or after the word???
	result_hash = hash1.hexdigest()

	if result_hash == pass_hash:
		print("PASSWORD FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		print(f"{word}:{result_hash}")
		sys.exit()
	else:
		print(f"{word}:{result_hash}")
		
def fill_queue(wordlist):
	with open(wordlist, "r") as file:
		try:
			for line in file.readlines():
				queue.put(line.strip())
		except:
			print("word not readable")

def attack():
        while not queue.empty():
                word = queue.get()
                hash_test(word)
               
print(f"using salt:{salt} and wordlist:{wordlist}")
print(f"cracking:{pass_hash}")

fill_queue(wordlist)   # fills the list of ports to scan
thread_list = []	# storages the threads

for i in range(32):
	t = threading.Thread(target=attack)
	thread_list.append(t)
	
for thread in thread_list:
	thread.start()
	thread.join()
