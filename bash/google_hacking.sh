#!/bin/bash

target=$1
echo "STARTING GOOGLE HACKING!"
echo "TARGET:$target"

#subdomains
firefox https://www.google.com/search?q=site%3A*$target+-www

# filetype
firefox https://www.google.com/search?q=site%3A$target+filetype%3Apdf
firefox https://www.google.com/search?q=site%3A$target+filetype%3Atxt
firefox https://www.google.com/search?q=site%3A$target+filetype%3Asql
firefox https://www.google.com/search?q=site%3A$target+filetype%3Axls
firefox https://www.google.com/search?q=site%3A$target+filetype%3Axlsx
firefox https://www.google.com/search?q=site%3A$target+filetype%3Abkp
firefox https://www.google.com/search?q=site%3A$target+filetype%3Abackup
firefox https://www.google.com/search?q=site%3A$target+filetype%3Aold
firefox https://www.google.com/search?q=site%3A$target+filetype%3Abak
firefox https://www.google.com/search?q=site%3A$target+filetype%3Axml
firefox https://www.google.com/search?q=site%3A$target+filetype%3Aasp
firefox https://www.google.com/search?q=site%3A$target+filetype%3Acsv

# intitle
firefox https://www.google.com/search?q=site%3A$target+intitle%3Awelcome
firefox https://www.google.com/search?q=site%3A$target+intitle%3A"NETSurveillance WEB"
firefox https://www.google.com/search?q=site%3A$target+intitle%3Anetwork
firefox https://www.google.com/search?q=site%3A$target+intitle%3Apasswd
firefox https://www.google.com/search?q=site%3A$target+intitle%3A"NETSurveillance WEB"

# intext
firefox https://www.google.com/search?q=site%3A$target+intext%3A"index of"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"password"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"admin"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"administrator"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"shell"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"/webdynpro/resources/sap.com/"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"@"
firefox https://www.google.com/search?q=site%3A$target+intext%3A"backup"

# inurl
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"/etc"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"wp-config.php"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"log"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"admin"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"SUID"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"root"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"hack"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"ftp"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"smb"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"key"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"/wp-content"
firefox https://www.google.com/search?q=site%3A$target+inurl%3A"ovpn"

# external
firefox https://www.google.com/search?q=site%3Apastebin.com+intext%3A$target
firefox https://www.google.com/search?q=site%3Atrello.com+intext%3A$target
firefox https://www.google.com/search?q=site%3Agithub.com+intext%3A$target
