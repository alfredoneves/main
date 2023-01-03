#!/bin/bash

network=$1
if [ "$network" == "" ]
then 
	echo "EXP: ./arping_sweep.sh 192.168.0"
else
for i in $(seq 1 254);do 
sudo arping -c 1 $network.$i | grep "Unicast reply"
done
fi
