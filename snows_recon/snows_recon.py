#!/usr/bin/python3
import queue
import subprocess
import sys
import requests
import threading
import pyfiglet
import dns.resolver
from bs4 import BeautifulSoup
from queue import Queue

ascii_banner = pyfiglet.figlet_format("snows_recon")
print(ascii_banner)


def help_menu():
	text = """This tool executes basic enumeration of dns and subdomains
		Usage: ./snows_recon.py [domain] [subdomains_wordlist] [num_threads]
	"""
	print(text)
	

try:
	domain = sys.argv[1]
	wordlist = sys.argv[2]
	num_threads = int(sys.argv[3])
	subdomains_list = []	# storages the subdomains
	subdomain_takeover_list = []	# storages the subdomains to test for takeover
	my_queue = Queue()
	res = dns.resolver.Resolver()
except:
	help_menu()
	sys.exit()
	
	
def exec_linux(command):
	"""
	Executes a linux command
	:param command: the command to be executed
	:return: return the stdout and stderr
	"""
	try:
		proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
								stdin=subprocess.PIPE)
		result = proc.stdout.read() + proc.stderr.read()
		return result
	except Exception as error:
		print(error)


def crt_scraping(domain):
	"""
	Executes the web scraping of crt.sh
	:param domain: domain to be used in url
	:return: appends subdomains to the list below
	"""
	global subdomains_list
	
	r = requests.get(f"https://crt.sh/?q={domain}")
	soup = BeautifulSoup(r.content, "lxml")
	trs = soup.find_all("tr")
	
	for tr in trs[3:]:
		tds = tr.find_all("td")
		cont = 0
		
		for td in tds[2:]:
			if cont == 2 and domain in td.get_text() and "*" not in td.get_text() and domain != td.get_text():
				subdomains_list.append(td.get_text())
			cont += 1
			

def fill_queue(file_name, my_queue):
	"""This function reads a file and insert each line inside a queue"""	
	with open(file_name, "r") as my_file:
		for line in my_file.readlines():
			my_queue.put(line.strip())


def test_subdomain(domain, sub):
	"""
	Tests a subdomain to check if it exists
	:param domain: base domain
	:param sub: subdomain to be prepended
	:return: appends the subdomain to the list below
	"""
	global subdomains_list
	url = f"{sub}.{domain}"

	try:
		result = res.resolve(url, "A")
		subdomains_list.append(url)
	except:
		pass


def attack():
	while not my_queue.empty():
		sub = my_queue.get()
		test_subdomain(domain, sub)
		query_cname(domain, sub)


def treat_list():
	"""
	Removes duplicates found and delete the temporary file created by subfinder
	Added the subdomain takeover test too, this function writes it to the file
	"""
	
	with open(f"{domain}_temp.txt", "r") as my_file:
		lines = my_file.readlines()

		for line in lines:
			subdomains_list.append(line.strip())

	# write the subdomains to a file
	with open(f"{domain}_subdomains.txt", "w") as my_file:
		for line in set(subdomains_list):
			my_file.write(f"{line}\n")
			
	# write file for subdomain takeover
	with open(f"{domain}_subdomain_takeover.txt", "w") as my_file:
		for line in subdomain_takeover_list:
			my_file.write(f"{line}\n")

	exec_linux(f"rm {domain}_temp.txt")


def organize_files(domain):
	"""Creates a directory to storage the files generated for the domain"""
	exec_linux(f"mkdir snows_{domain}")
	exec_linux(f"mv {domain}* snows_{domain}")


def query_cname(domain, sub):
	"""This function tests for cname information in subdomains for subdomain takeover"""
	global subdomain_takeover_list

	try:
		url = f"{sub}.{domain}"
		answers = dns.resolver.resolve(url, 'CNAME')
		cnames = [rdata.target.to_text() for rdata in answers]
		subdomain_takeover_list.append(f"{sub}.{domain} is an alias for {cnames}")
	except:
		pass



print("Executing whois...")
exec_linux(f"whois {domain} >> {domain}_whois.txt")

print("Executing reverse whois...")
exec_linux(f"whois $(host {domain} | grep 'has address' | cut -d ' ' -f 4) >> {domain}_reverse_whois.txt")

print("Executing dns enumeration...")
exec_linux(f"dnsenum {domain} >> {domain}_dnsenum.txt")
exec_linux(f"dnsrecon -a -k -d {domain} >> {domain}_dnsrecon.txt")	# zone transfer included

print("Executing subfinder...")
exec_linux(f"subfinder -d {domain} -silent >> {domain}_temp.txt")

print("Executing crt.sh web scraping...")
crt_scraping(domain)

print("Executing subdomain brute force, this may take a while depending on the wordlist and number of threads...")
fill_queue(wordlist, my_queue)
thread_list = []  # list to save threads

for i in range(num_threads):
	t = threading.Thread(target=attack)
	thread_list.append(t)

for thread in thread_list:
	thread.start()

for thread in thread_list:
	thread.join()

treat_list()
organize_files(domain)
