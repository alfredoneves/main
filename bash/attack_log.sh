#!/bin/bash

cat access.log | cut -d " " -f1 | sort -n | uniq -c | sort -nr | head | awk '{$1=$1;print}' > top10.txt
echo "TRAFFIC / IP ADDRESS"
cat top10.txt
echo "--------------------"

attacker=$(cat top10.txt | head -1 | cut -d " " -f2)
echo "ANALYZING TOP 1 IP:$attacker"
start=$(cat access.log | grep $attacker | cut -d " " -f4,5 | head -1)
echo "START DATE AND TIME:$start"
end=$(cat access.log | grep $attacker | cut -d " " -f4,5 | tail -1)
echo "END DATE AND TIME:$end"
echo "REQUEST METHODS USED"
requests=$(cat access.log | grep $attacker | cut -d '"' -f 2 | cut -d " " -f 1 | sort -u)
echo $requests
cat access.log | grep $attacker | cut -d '"' -f6 | sort -u > user_agents.txt
echo "USER AGENTS SAVED IN:user_agents.txt"

