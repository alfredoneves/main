#!/usr/bin/python3

import socket
import threading
from queue import Queue
import sys

try:
	target = sys.argv[1]
	queue = Queue()
	# take the range of ports to scan
	port_range = sys.argv[2]
	delimiter = port_range.find("-")
	first = int(port_range[0:delimiter])
	last = int(port_range[delimiter+1::])
	port_list = list(range(first, last))	# list of ports that will be used to scan
	# save open ports
	open_ports = []
except:
	print("usage: python3 port_scanner2.py [ip] [port_range]. EXP: python3 port_scanner2.py 192.168.0.1 1-1024")

def port_scan(port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.close()
		return True
	except:
		return False
	
def fill_queue(port_list):
	for port in port_list:
		queue.put(port)
		
def attack():
	while not queue.empty():
		port = queue.get()
		if port_scan(port):
			print(f"port {port} is open!")
			open_ports.append(port)

fill_queue(port_list)	# fills the list of ports to scan
thread_list = []

for i in range(16):
	thread = threading.Thread(target=attack)	# tells the thread what function to execute
	thread_list.append(thread)
for thread in thread_list:
	thread.start()
for thread in thread_list:
	thread.join()	# waits for all threads to finish
print(f"open ports: {open_ports}")

