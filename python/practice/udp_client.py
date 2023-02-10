#!/usr/bin/python3

import socket

address = "127.0.0.1"
port = 5001
buffer_size = 1024
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	# Create a UDP socket at client side
while True:
	client_message = input("write the message: ")
	bytes_to_send = client_message.encode()
	s.sendto(bytes_to_send, (address, port))	# Send to server using created UDP socket
	server_msg, server_address = s.recvfrom(buffer_size)
	msg = f"Message from Server {server_msg.decode()}"
	print(msg)
