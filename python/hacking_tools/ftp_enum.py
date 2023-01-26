#!/usr/bin/python3
# this tools grabs ftp banners and tests for anonymous logins

import socket
import sys

try:
	host = sys.argv[1]
	port = int(sys.argv[2])
except:
	print("usage: ./ftp_enum.py [host_ip] [port]")
	sys.exit()
	
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	banner = s.recv(1024)
	print(banner)
except:
	print("connection failed")
	sys.exit()
	
try:
	# testing anonymous login
	s.send("USER anonymous\r\n")
	user = s.recv(1024)
	print(user)

	s.send("PASS anonymous\r\n")
	password = s.recv(1024)
	print(password)
except:
	print("anonymous login failed")
	
