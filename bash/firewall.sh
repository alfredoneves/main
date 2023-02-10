#!/bin/bash

# clear the rules
iptables -F
iptables -t nat -F
iptables -t mangle -F

# DOS block
echo 1 > /proc/sys/net/ipv4/tcp_syncookies

# necessary services INPUT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 53 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp --dport 3306 -j ACCEPT

# block other ports (remember that the firewall reads the lines in sequence)
iptables -P INPUT DROP	# configures the policy to drop packets
# iptables -A INPUT -p tcp --syn -j DROP can drop hosts that try to connect in other ports
