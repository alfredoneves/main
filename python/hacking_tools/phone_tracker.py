#!/usr/bin/python3

import sys
import phonenumbers
from phonenumbers import geocoder, carrier

try:
	phone_number = phonenumbers.parse("+55" + sys.argv[1])
	carrier = carrier.name_for_number(phone_number, 'pt-br')
	region = geocoder.description_for_number(phone_number, 'pt=br')
	print(carrier)
	print(region)
except Exception as error:
	print("usage: ./phone_tracker.py 21999999999")
	answer = input("do you want to see the error report? (y/n)").lower()
	if answer == "y":
		print(error)
	else:
		print("finished")
		
