# Script to get all the IP ranges for a company based on the domain
# Get your API key in https://ipinfo.io/account/home after creating an account
# Documentation https://ipinfo.io/developers/ranges
# pip install ipinfo

import requests
import sys

try:
    access_token = sys.argv[1]
    domain = sys.argv[2]
except:
    print(f"Usage: python {sys.argv[0]} [API_TOKEN] [DOMAIN]")
    sys.exit()

print(f"Fetching IP ranges for {domain}...")

url = f"https://ipinfo.io/ranges/{domain}?token={access_token}"

try:
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    response.raise_for_status()
    
    # Parse the JSON response
    data = response.json()
    
    # Check if 'ranges' key exists and has data
    if 'ranges' in data and data['ranges']:
        print(f"IP Ranges for {domain}:")
        for ip_range in data['ranges']:
            print(f"{ip_range}")
    else:
        print("No IP ranges found for this domain.")
        
except requests.exceptions.HTTPError as e:
    # Handle HTTP errors (e.g., 404, 403, 429)
    print(f"API Error: {e}")
except requests.exceptions.RequestException as e:
    # Handle network or other request-related errors
    print(f"Request Failed: {e}")
except ValueError:
    # Handle JSON parsing errors
    print("Error: Invalid response format from API.")
