#!/usr/bin/python3

import threading
import socket
from queue import Queue
import sys
import ipaddress

try:
	network = ipaddress.ip_network(sys.argv[1])
	port = int(sys.argv[2])
	ips = Queue()
	thread_list = []
	hosts_up = []
	flag_v = False
	if "-v" in sys.argv:
		flag_v = True
except:
	print("usage: ./python_sweep.py [network] [port]")
	print("example: ./python_sweep.py 192.168.0.0/24 80")
	sys.exit()
	
def scan(target, v=flag_v):
	try:
		if v:
			print(f"testing {target}:{port}")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(3)
		s.connect((target, port))
		s.close()
		return True
	except Exception as error:
		if v:
			print(error)
		return False
		
def fill_queue():
	for ip in network.hosts():
		ips.put(str(ip))
		
def attack():
	while not ips.empty():
		target_ip = ips.get()
		if scan(target_ip):
			print("host up: " + target_ip)
			hosts_up.append(target_ip)

fill_queue()
for i in range(16):
	t = threading.Thread(target=attack)
	thread_list.append(t)
	
for thread in thread_list:
	thread.start()

for thread in thread_list:
	thread.join()

print("\nSCAN FINISHED!")
print(hosts_up)
	
