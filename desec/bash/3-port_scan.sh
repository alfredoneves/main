#!/bin/bash

if [ "$1" == "" ] || [ "$2" == "" ]
then
	echo "Uso: $0 [network] [port]"
	echo "Exp: $0 192.169.0 80"
	exit
fi

for i in $(seq 1 254)
do
	hping3 -S -p $2 -c 1 "$1.$i" 2>/dev/null | grep "flags=SA" | cut -d "=" -f 3 | cut -d " " -f 1
done
