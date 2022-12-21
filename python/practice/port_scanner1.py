#!/usr/bin/python3

import socket
import sys

try:
	ip = sys.argv[1]
except:
	print("usage: python3 port_scanner1.py [ip]")

print("scanner initialized")
for port in range(0, 65536):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip, port)) == 0:
		print(f"port {port} open!")
		s.close()

