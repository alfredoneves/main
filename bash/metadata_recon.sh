#!/bin/bash

echo "THIS PROGRAM SEARCHES FOR FILES, WAIT 10 SECONDS TO AVOID BE BLOCKED BY GOOGLE, DOWNLOADS THE FILES AND EXTRACT THE METADATA"
target=$1
#pdf
lynx --dump "https://www.google.com/search?q=site%3A$target+ext%3Apdf" | grep "http" | cut -d "=" -f 2 | egrep -v "site:|google.com|pt-BR|search" | sed 's/...$//' >> files_to_download.txt
sleep 10
#xlsx
lynx --dump "https://www.google.com/search?q=site%3A$target+ext%3Axlsx" | grep "http" | cut -d "=" -f 2 | egrep -v "site:|google.com|pt-BR|search" | sed 's/...$//' >> files_to_download.txt
sleep 10
#sql
lynx --dump "https://www.google.com/search?q=site%3A$target+ext%3Asql" | grep "http" | cut -d "=" -f 2 | egrep -v "site:|google.com|pt-BR|search" | sed 's/...$//' >> files_to_download.txt
sleep 10
#txt
lynx --dump "https://www.google.com/search?q=site%3A$target+ext%3Atxt" | grep "http" | cut -d "=" -f 2 | egrep -v "site:|google.com|pt-BR|search" | sed 's/...$//' >> files_to_download.txt

mkdir downloaded_files
for url in $(cat files_to_download.txt);do wget $url -P downloaded_files/;done
for file in $(ls downloaded_files); do exiftool "downloaded_files/$file" >> exiftool_results.txt; done
cat exiftool_results.txt | egrep "Creat|Author|Version" | sort -u
rm -r downloaded_files exiftool_results.txt files_to_download.txt
