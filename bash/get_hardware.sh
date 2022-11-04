#!/bin/bash
# script to get information about the kernel, CPU, peripheral, memory and temperature
# https://www.linkedin.com/in/alfredo-neves-56398a218/

commands=("uname -a" "lshw" "lscpu" "sensors" "lspci" "inxi" "free -h" "df -h")

for ((i=0; i<${#commands[@]}; i++)); do
echo command:${commands[i]}
${commands[i]}
echo --------------------------------------------------------------------------------------------------------------------------
done

