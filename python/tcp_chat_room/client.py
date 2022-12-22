#!/usr/bin/python3

import threading
import socket

nickname = input("type your nickname: ")
try:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(("127.0.0.1", 4444))
except:
	print("the socket couldn't be created")
	
def receive():
	while True:
		try:
			message = client.recv(1024).decode("ascii")
			if message == "NICK":
				client.send(nickname.encode("ascii"))
			else:
				print(message)
		except Exception as error:
			print(f"an error occurred: {error}")
			client.close()
			break

def send():
	while True:
		message = f"{nickname}:" + input("")
		client.send(message.encode("ascii"))
		
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()

