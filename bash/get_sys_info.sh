#!/bin/bash

# gets information about time and date
echo "TIME AND DATE"
date
cat /etc/timezone
uptime
echo ===========================================================================================================

# gets information about network and logging
echo "NETWORK AND LOGGING"
w
ip address
iwconfig
ip route show
netstat -nltp
resolvectl status       # dns info
last
echo ===========================================================================================================

# gets processes information
echo "PROCESSES"
ps aux | awk '{$1=$1;print}' | cut -d " " -f 2,3,4,9,10,11
echo ===========================================================================================================

# gets hardware information
echo "HARDWARE"
commands=("uname -a" "lshw" "lscpu" "sensors" "lspci" "inxi" "free -h" "df -h")

for ((i=0; i<${#commands[@]}; i++)); do
echo command:${commands[i]}
${commands[i]}
echo ===========================================================================================================
done
