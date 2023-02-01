#!/usr/bin/python3

import socket
import sys
import re
from queue import Queue
import threading


if len(sys.argv) !=3:	# verifies if the three parameters were passed (program name, ip address and wordlist of users
	print("Usage: ./smtp_enum.py [IP] [wordlist]")
	sys.exit()
	
queue = Queue()
thread_list = []	# list to storage the threads before start
ip = sys.argv[1]
wordlist = sys.argv[2]

def attack():
	while not queue.empty():
		user = queue.get()
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, 25))
			s.recv(1024)
			s.send(f"VRFY {user}\r\n".encode())
			result = s.recv(1024).decode()
			if not re.search("rejected", result):	# if "rejected" appears it means that the user is incorrect
				print(result.strip())
		except Exception as error:
			print(error) 

def fill_queue(wordlist):
	with open(wordlist) as file:
		for line in file:
			queue.put(line.strip())
			
fill_queue(wordlist)

for i in range(4):
	t = threading.Thread(target=attack)
	thread_list.append(t)

for thread in thread_list:
	thread.start()
	thread.join()
	
