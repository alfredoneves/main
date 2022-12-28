#!/bin/bash

# program to find subdomains based on a wordlist

target=$1
wordlist=$2
subdomains=$(cat $wordlist)
for subdomain in $subdomains; do
host $subdomain.$target; done | grep -v "NXDOMAIN"

