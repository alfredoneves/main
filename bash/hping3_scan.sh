#!/bin/bash

network=$1
port=$2

if [ "$port" == "" ]
then
	echo "USAGE: ./hping3_scan.sh 192.168.0 80"
else
for i in {1..254};do
sudo hping3 -c 1 -S -p $port $network.$i 2>/dev/null | grep "flags" | cut -d " " -f 2,6,7
done
fi
