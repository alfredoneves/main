#!/bin/bash

# this program takes a list of urls and dumps all the html contents

urls=$1
for url in $(cat urls);do
curl -s -H "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36" $url >> html_dump.txt
done

