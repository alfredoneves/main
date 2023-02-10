#!/usr/bin/python3

import socket
import sys
import time

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)	# creates the socket object to use TCP
		host = "google.com"	# str IP addr or domain
		port = 80	# int port
	except Exception as error:
		print("ERROR IN SOCKET CREATION\n", error)
		sys.exit()
		
	try:
		s.connect((host, port))
		print("closing the connection")
		time.sleep(3)
		s.close()
	except Exception as error:
		print("ERROR IN CONNECTION\n", error)

if __name__ == "__main__":
	main()

