#!/usr/bin/python3

import socket

address     = "127.0.0.1"
port   = 5001
bufferSize  = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creates the socket for UDP
s.bind((address, port))	# Bind to address and port
print("UDP server listening")	# Listens for incoming datagrams

while(True):
	data, address = s.recvfrom(bufferSize)	# receives 2 values
	client_msg = f"Message from Client:{data.decode()}"
	print(client_msg)
	server_message = input("write the message: ")
	bytes_to_send = server_message.encode()
	s.sendto(bytes_to_send, address)     # sends a message to the address
	
