#!/usr/bin/python3
# this program reads a wordlist and a url, then adds each word of the wordlist to the end of the url and make a request with it

import requests
import sys
import threading
from queue import Queue

try:
	url = sys.argv[1]
	wordlist_path = sys.argv[2]
	queue = Queue()
except:
	print("usage: ./fuzzing.py domain.com /path/to/wordlist")
	sys.exit()

def fuzzing(url, word):	# change wordlist to a single word
		url_word = "http://" + url + "/" + word
		r = requests.get(url_word)
		if r.status_code != 404:
			print(url_word + "---" + str(r.status_code))

def fill_queue(wordlist_path):
	with open(wordlist_path, "r") as wordlist:
		for word in wordlist:
			queue.put(word.strip())

def attack():
	while not queue.empty():
		directory = queue.get()
		fuzzing(url, directory)
	
fill_queue(wordlist_path)
thread_list = []

for i in range(16):
	thread = threading.Thread(target=attack)
	thread_list.append(thread)
	
for thread in thread_list:
	thread.start()

for thread in thread_list:
	thread.join()
	
print("fuzzing finished!")

