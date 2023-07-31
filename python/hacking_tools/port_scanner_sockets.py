#!/usr/bin/python3

import socket
import threading
import sys
from queue import Queue
from datetime import datetime


def port_scan(host, port) -> bool:
	"""
	This function tries to connect to a host and port.
	:param host: IP address of target
	:param port: port to connect to
	:return: True if the connection succeeds and False in case of error
	"""
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		s.settimeout(1.5)
		s.close()
		return True
	except:
		return False


def fill_queue(ports: list, my_queue: Queue):
	"""
	This function receives a list and a queue and fills the queue with the list.
	:param ports: list of ports
	:param my_queue: queue object
	"""
	for port in ports:
		my_queue.put(port)


def attack():
	global host
	global queue

	while not queue.empty():
		port: int = queue.get()
		if port_scan(host, port):
			print(f"port {port} is open!")


def start():
	"""
	This function takes the host and the number of threads
	:return host, threads
	"""
	try:
		host = str(sys.argv[1])
		threads = int(sys.argv[2])
		return host, threads
	except:
		print("usage: python3 port_scanner.py [host] [threads] \nEXP: python3 port_scanner.py nmap.org 300")
		sys.exit()


def main(function):
	for i in range(threads):
		thread = threading.Thread(target=function)  # tells the thread what function to execute
		thread_list.append(thread)

	# The following 2 for need to be separate, otherwise only 1 thread will be launched in the beginning
	for thread in thread_list:
		thread.start()

	for thread in thread_list:
		thread.join()  # waits for all threads to finish


queue = Queue()
fill_queue([i for i in range(1, 65535)], queue)
thread_list = []
host, threads = start()

if __name__ == '__main__':
	main(attack)
	print(f'Scan finished at: {datetime.utcnow()}')
