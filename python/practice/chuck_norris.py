import requests
import json

try:
	r = requests.get("https://api.chucknorris.io/jokes/random")
	r_json = r.json()
	joke = r_json["value"]
	print(joke)
except:
	print("no joke this time")
	
