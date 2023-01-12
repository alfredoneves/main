#!/usr/bin/python3

import socket
import sys

try:
	target = sys.argv[1]
	port = int(sys.argv[2])
except:
	print("usage: ./banner_grabbing.py target_ip port")
	sys.exit()
	
def banner_grabbing(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	return s.recv(1024).decode()
	
print(banner_grabbing(target, port))

