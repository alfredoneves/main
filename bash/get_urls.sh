#!/bin/bash
# this script dumps a google search for a site and extract urls

target=$1

if [ "$target" == "" ]
then
        echo "Usage: $0 [TARGET]"
        echo "Example: $0 businesscorp.com.br"
        exit
fi

# num=1000 determines the max number of results
lynx --dump "http://google.com/search?num=1000&q=site:*$1" | grep "$1" | cut -d "=" -f 2 | grep http | sed s'/...$//'g
