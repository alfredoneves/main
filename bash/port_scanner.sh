#!/bin/bash

# this program uses netcat to check if a port is open

echo "usage: ./port_scanner.sh [ip]"
target=$1
for port in {0..1024}; do
nc -nvz $target $port -w 2 |& grep -v "failed" | grep -v "timed out"
done

