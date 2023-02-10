#!/bin/bash

# this program takes html code and find links on it

html=$1
cat $html | grep "href" | grep "http" | cut -d '"' -f 2

