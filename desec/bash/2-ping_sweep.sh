#!/bin/bash

if [ "$1" == "" ]
then
	echo "Uso: $0 [network]"
	echo "Exemplo: $0 192.168.0"
	exit
fi

for ip in $(seq 1 254)
do
	ping -c1 -W 0.9 "$1.$ip" | grep "64 bytes from" | cut -d ":" -f 1 | cut -d " " -f 4
done
