#!/usr/bin/python
import dns.resolver
import sys

try:
	target = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print("Usage: python3 dns_brute.py [url] [wordlist]")
	sys.exit()

res = dns.resolver.Resolver()
my_file = open(wordlist, "r")
subdomains = my_file.read().splitlines()

for subdomain in subdomains:
	try:
		sub_target = subdomain + "." + target
		result = res.resolve(sub_target, "A")
		for ip in result:
			print(sub_target, "-", ip)
	except:
		pass
