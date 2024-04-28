#!/bin/bash

target=$1
if [ "$1" == "" ]; then
	echo "Usage: ./google_hacking.sh domain_name"
	echo "EXP: ./google_hacking.sh google.com"
	echo "Close firefox before starting the script to avoid oppening all the tabs at once"
	exit
fi

echo "STARTING GOOGLE HACKING!"
echo "TARGET:$target"

echo "Searching for subdomains"
firefox https://www.google.com/search?q=site%3A*$target+-www 2>/dev/null

echo "Searching per filetype"
firefox https://www.google.com/search?q=site%3A$target+filetype%3Apdf 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Atxt 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Asql 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Axls 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Axlsx 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Abkp 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Abackup 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Aold 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Abak 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Axml 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Aasp 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+filetype%3Acsv 2>/dev/null

echo "Intitle"
firefox https://www.google.com/search?q=site%3A$target+intitle%3Awelcome 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intitle%3A"NETSurveillance WEB" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intitle%3Anetwork 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intitle%3Apasswd 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intitle%3A"NETSurveillance WEB" 2>/dev/null

echo "Intext for juicy words"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"syntax near" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"index of" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"password" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"admin" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"administrator" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"shell" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"/webdynpro/resources/sap.com/" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"@" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"backup" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+intext%3A"error" 2>/dev/null

echo "Inurl for files, configs and services"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"/etc" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"wp-config.php" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"log" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"admin" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"SUID" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"root" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"hack" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"ftp" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"smb" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"key" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"/wp-content" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"/wp-includes" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"ovpn" 2>/dev/null

echo "Searching for parameters in url"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"id=" 2>/dev/null
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"s=" 2>/dev/null

echo "searching in pastebin, trello and github"
firefox https://www.google.com/search?q=site%3Apastebin.com+intext%3A$target 2>/dev/null
firefox https://www.google.com/search?q=site%3Atrello.com+intext%3A$target 2>/dev/null
firefox https://www.google.com/search?q=site%3Agithub.com+intext%3A$target 2>/dev/null
