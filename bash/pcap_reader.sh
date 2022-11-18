#!/bin/bash

file=$1
echo "ARP report"
tcpdump arp -nvr $file
echo "------------------------------------------------------------------------------------------"
echo "ICMP report with IP's, type of ICMP and length"
tcpdump icmp -nvr $file | grep ">" | cut -d "," -f 1,4 | sort | uniq -c | awk '{$1=$1;print}'
echo "------------------------------------------------------------------------------------------"
echo "TCP report"
tcpdump tcp -vnr $file | grep "Flags" | cut -d "," -f 1 | awk '{$1=$1;print}'
echo "------------------------------------------------------------------------------------------"
echo "UDP report"	
tcpdump udp -vnr $file | grep -v tos | awk '{$1=$1;print}'
