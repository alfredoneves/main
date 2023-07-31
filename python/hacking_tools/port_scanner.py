#!/usr/bin/python3
# this script requires administrative privileges to craft the packet with a SYN flag and analyzes the response
import threading
import sys
import pyfiglet
from queue import Queue
from datetime import datetime
from scapy.all import *
from time import sleep


def port_test(ip, port) -> scapy.layers.inet.IP:
	"""
	This function tests if a port is open.
	:param ip: Host ip address or domain name
	:param port: Port to test
	:return: Returns a scapy object that can be retrieved with 2 variables. EXP: ans, no_ans = test_port(ip, port)
	"""
	p_ip = IP(dst=ip, ttl=128)
	p_tcp = TCP(dport=port, flags='S')
	packet = p_ip/p_tcp	# Encapsulates the packet
	return sr(packet, timeout=3)	# Sends the packet


def fill_queue(ports: list, my_queue: Queue):
	"""
	This function receives a list and a queue and fills the queue with the list.
	:param ports: List of ports
	:param my_queue: Queue object
	"""
	for port in ports:
		my_queue.put(port)


def attack():
	"""
	This function is calling the port_test and printing if the port is open
	"""
	global host
	global queue

	while not queue.empty():
		port: int = queue.get()
		ans, no_asn = port_test(host, port)
		try:
			flag = ans[0][1][TCP].flags
			
			if flag == 'SA':
				print(f'Port {port} is open!')

		except IndexError:
			if filtered:
				print(f'Port {port} is filtered!')
		sleep(0.05)


def start():
	"""
	This function takes the host and the number of threads.
	:return: host -> str, threads -> int
	"""
	global filtered
	
	try:
		host = str(sys.argv[1])
		threads = int(sys.argv[2])
		
		if '-f' in sys.argv:
			filtered = True
		else:
			filtered = False
			
		return host, threads
	except:
		print('usage: python3 port_scanner.py [host] [threads] [-f]')
		print('EXP: python3 port_scanner.py nmap.org 50')
		print('    -f	# show filtered ports')
		sys.exit()


def main(function, threads, thread_list):
	"""
	Executes a function with multi threading.
	:param function: function to be executed
	:param threads: number of threads to execute the function
	:param thread_list: control list to save the threads during execution
	"""
	for i in range(threads):
		thread = threading.Thread(target=function)  # tells the thread what function to execute
		thread_list.append(thread)

	# The following 2 for need to be separate, otherwise only 1 thread will be launched in the beginning
	for thread in thread_list:
		thread.start()

	for thread in thread_list:
		thread.join()  # waits for all threads to finish


ascii_banner = pyfiglet.figlet_format("snows\nPort Scanner")
print(ascii_banner)
conf.verb = 0	# reduces the output from scapy
queue = Queue()
fill_queue([i for i in range(1, 65536)], queue)
thread_list = []
host, threads = start()

if __name__ == '__main__':
	main(attack, threads, thread_list)
	print(f'Scan finished at: {datetime.utcnow()}')
