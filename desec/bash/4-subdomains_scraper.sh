#!/bin/bash

if [ "$1" == "" ]
then
	echo "Uso: $0 [domain]"
	exit
fi

wget $1 -O "source_cod3.html" -q
cat source_cod3.html | grep -E -o '\b((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])\.)+[a-zA-Z]{2,}|(?:\d{1,3}\.){3}\d{1,3})\b' 2>/dev/null | sort | uniq > urlxx.txt

for url in $(cat urlxx.txt)
do
	host -W 1 $url | grep -v "NXDOMAIN"
done
rm source_cod3.html urlxx.txt
