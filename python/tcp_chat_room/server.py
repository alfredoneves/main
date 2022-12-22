#!/usr/bin/python3

import threading
import socket

try:
	host = "127.0.0.1"
	port = 4444
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((host, port))
	server.listen()
except:
	print("error creating the socket")
	
clients = []
nicknames = []

def broadcast(message, sender):
	for client in clients:
		if client != sender:
			client.send(message)
		
def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message, client)
		except:
			index = clients.index(client)
			clients.remove(client)
			clients.close()
			nickname = nicknames[index]
			broadcast(f"{nickname} has left the room!".encode("ascii"))
			nicknames.remove[nickname]
			break
			
def receive():
	while True:
		client, address = server.accept()
		print(f"connected with {str(address)}")
		
		client.send("NICK".encode("ascii"))
		nickname = client.recv(1024).decode("ascii")
		nicknames.append(nickname)
		clients.append(client)
		
		print(f"the nickname of the client is: {nickname}")
		broadcast(f"{nickname} joined the room".encode("ascii"), "server")
		client.send(f"connected to the server!".encode("ascii"))
		
		thread = threading.Thread(target=handle, args=(client,))
		thread.start()
		
print("listenning for clients ...")
receive()
		
		
		
		
		
			
			
			
			
