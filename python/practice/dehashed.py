import requests

email = "shark%40tesla.com"

# headers
headers = {'Host': 'www.dehashed.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'DNT': '1',
'Connection': 'keep-alive',
'Cookie': 'cf_clearance=c0b8905cfdbb820193c6b6ca2d048acf2a627f6e-1667951161-0-250; mysession=MTY2Nzk0MTk5MHxEdi1CQkFFQ180SUFBUkFCRUFBQUlQLUNBQUVHYzNSeWFXNW5EQVlBQkhWelpYSUZhVzUwTmpRRUJRRDlCX1dRfG6OA7yinyUTQjFbY9OZX5Y15MEEjQw9So9lmyJQFiUS; __cf_bm=JHJ22x267dQ0b3AtkpEPL1db5UOGODG_8HgFjyLFxfc-1667950885-0-ARkRixz2PKslWLTzW6TXLqXjm/aPTLKHO9Z2hLWEYhdi+xkJ0MbN6jlenkNpP0uSmPNJoHXpqLETN7Mj5C2vVxZNFI+X4XM8DoSYsPPYTGy/lqZ4OyVkqG/4WqMjFMdFqw==',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'TE': 'trailers'}

# request
r = requests.get("https://www.dehashed.com/search?query=email%3Ashark%40tesla.com", headers=headers)
print(r)	# response 200, I did it
print(type(r.text))
print(r.content)

