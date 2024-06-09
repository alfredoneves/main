#!/usr/bin/python3
import sys
import socket

try:
	ip = sys.argv[1]
	porta = int(sys.argv[2])
except:
	print(f"Uso: {sys.argv[0]} [IP] [PORTA]")
	sys.exit()
	
	
def get_ban(ip, porta):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	try:
		s.connect((ip,porta))
		print(f"Porta {porta} aberta")
	except:
		pass
	try:
		print(s.recv(1024).decode())
		s.close()
	except Exception as error:
		print(error)
	

get_ban(ip, porta)
