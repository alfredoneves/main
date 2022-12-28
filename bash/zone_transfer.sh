#!/bin/bash

target=$1
name_servers=$(host -t ns $target | cut -d " " -f 4)
for server in $name_servers; do host -l -a $server; done

