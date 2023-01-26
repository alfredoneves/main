#!/usr/bin/python3
#admin user required

from scapy.all import *
import sys
import ipaddress
import threading
from queue import Queue

conf.verb = 0	# removes verbosity
try:
	network = ipaddress.ip_network(sys.argv[1])
	queue = Queue()
	thread_list = []
	print("hosts that respond to ICMP type 8 will be shown below:")
except:
	print("usage: ./scapy.sweep.py [network]")
	sys.exit()
	
def sweep(host):
	try:
		pIP = IP(dst=host,ttl=128)	# object host must be converted to string
		packet = pIP/ICMP()
		answer, no_answer = sr(packet, timeout=1)
		print(answer[0][1][IP].src)
		return True
	except:
		return False

def fill_queue(network):	# fills the queue with the hosts as strings
	for host in network.hosts():
		queue.put(str(host))
		
def attack():
	while not queue.empty():
		host = queue.get()
		sweep(host)
		
fill_queue(network)

for i in range(16):	# creates the threads
	thread = threading.Thread(target=attack)
	thread_list.append(thread)

for thread in thread_list:	# starts the threads
	thread.start()

for thread in thread_list:
	thread.join()

