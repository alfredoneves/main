#!/usr/bin/python3
# this program requires administrator permissions

import sys
from scapy.all import *

try:
	ip = sys.argv[1]
except:
	print("usage: ./scapy_sweep.py [ip]")
	sys.exit()
	
# conf.verb = 0	uncomment to disable default output
ports = [21, 22, 25, 80, 443, 3306, 3389, 8080]
pIP = IP(dst=ip, ttl=128)
pTCP = TCP(dport=ports,flags="S")
packet = pIP/pTCP	# encapsulates 
ans, no_ans = sr(packet)
for a in ans:
	port = a[1][TCP].sport	# 0 for packet sent 1 for received
	flag = a[1][TCP].flags
	if flag == "SA":
		print(port, flag)
		
