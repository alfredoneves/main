#!/usr/bin/python3

import sys
import socket

host = sys.argv[1]	# receives the host
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# ipv4 socket
s1.connect(("whois.iana.org", 43))
s1.send((host + "\r\n").encode())
s1_answer = (s1.recv(1024)).decode()
refer = s1_answer.split()[19]	# takes the refer from iana to look in the right NIR
s1.close()

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((refer, 43))
s2.send((host + "\r\n").encode())
s2_answer = (s2.recv(1024)).decode()
print(s2_answer)
s2.close()

