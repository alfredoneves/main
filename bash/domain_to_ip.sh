#!/bin/bash

file=$1
if [ "$file" == "" ]
then
        echo "Usage: ./domain_to_ip.sh file"
        echo "Exp: ./domain_to_ip.sh subdomains_file.txt"
	exit
fi

for line in $(cat $file);do host $line;done
