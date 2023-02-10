#!/usr/bin/python3
# this program needs enough privilege to read the file with the api key

import requests
import sys
import hashlib

intro = """./virus_total [option=value]"
input options:\n-h	# hash\n-u	# url\n-f	# file name"""

def read_key(path):
	try:
		key = open(path, 'r')
		return key.readline().strip()
	except Exception as error:
		print(error)
		
def virus_hash(file_hash, api_key):
	try:
		url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
		
		headers = {
		    "accept": "application/json",
		    "x-apikey": api_key
		}
		
		response = requests.get(url, headers=headers)
		return response.text
	except Exception as error:
		print(error)
		
def virus_url(url, api_key):
	try:
		url = "https://www.virustotal.com/api/v3/urls"

		payload = f"url={url}"
		headers = {
		    "accept": "application/json",
		    "x-apikey": api_key,
		    "content-type": "application/x-www-form-urlencoded"
		}

		response = requests.post(url, data=payload, headers=headers)
		return response.text
	except Exception as error:
		print(error)
		
"""def json_extracter(json_object):"""

key = read_key("/root/virus_total_api")

try:
	if "-h=" in sys.argv[1][:3]:
		file_hash = sys.argv[1][3:]
		result = virus_hash(file_hash, key)
	elif "-u=" in sys.argv[1][:3]:
		url = sys.argv[1][3:]
		result = virus_url(url, key)
	elif "-f=" in sys.argv[1][:3]:
		file = sys.argv[1][3:]
		file_hash = hashlib.new("md5")
		file_hash.update((open(file, "rb").read()))
		result = virus_url(file_hash.hexdigest(), key)
	else:
		print(intro)
	print(result)
except:
	print(intro)
	sys.exit()
	



