#!/bin/bash

url=$1
if [ "$url" == "" ]
then
	echo "Usage: ./extract_subdomains.sh url"
	echo "Exp: ./extract_subdomains.sh https://www.my_site.com"	
exit
fi

curl $url -s | grep -o '[^/]*\.terra\.com' | sort -u
