#!/usr/bin/python3

import socket
import sys

try:
	ip = sys.argv[1]
	port = int(sys.argv[2])
except:
	print("usage: python3 port_tester.py [ip] [port]")
	sys.exit()
	
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection = s.connect_ex((ip, port))
except Exception as error:
	print(error)
	
if connection == 0:
	print("port open")
else:
	print("port closed")
s.close()

