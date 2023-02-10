#!/usr/bin/python3
import requests

# this program verifies email reputation

def query_email(email, flag=False):
	try:
		header = {"User-Agent": "student_learning"}
		r = requests.get(f"https://emailrep.io/{email}", header)
		r_json = r.json()
		important = f"email:{r_json['email']}\nreputation:{r_json['reputation']}\nsuspicious:{r_json['suspicious']}			\nmalicious_activity:{r_json['malicious_activity']}\ncredentials_leaked:{r_json['credentials_leaked']}\ndomain_exists:	{['domain_exists']}"
	
		if flag:
			return important
		else:
			return r.text
	except Exception as error:
		return error
		
email = input("type the email to be verified: ")

response = query_email(email)
print(response)
