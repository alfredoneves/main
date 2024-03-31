#!/bin/bash
# this program reads a log file from apache 2 and analyze it

file=$1
cat $file | cut -d " " -f1 | sort -n | uniq -c | sort -nr | awk '{$1=$1;print}' > ips.txt
echo "TRAFFIC / IP ADDRESS (top 10)"
head ips.txt
echo "--------------------"

attacker=$(head -n1 ips.txt | cut -d " " -f2)	# takes only the first IP
echo "ANALYZING TOP 1 IP:$attacker"
start=$(cat $file | grep $attacker | cut -d " " -f4,5 | head -1)
echo "START DATE AND TIME:$start"
end=$(cat $file | grep $attacker | cut -d " " -f4,5 | tail -1)
echo "END DATE AND TIME:$end"
echo "REQUEST METHODS USED"
requests=$(cat $file | grep $attacker | cut -d '"' -f 2 | cut -d " " -f 1 | sort -u)
echo $requests
cat $file | grep $attacker | cut -d '"' -f6 | sort -u > user_agents.txt
echo "IPS SAVED IN: ips.txt"
echo "USER AGENTS SAVED IN: user_agents.txt"

