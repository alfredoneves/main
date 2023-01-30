#!/bin/bash

# takes a wordlist and generates a rainbow table with various hashes
# you can add more hash types (the last is without -z)

wordlist=$1
rainbow=$2
for word in $(cat $wordlist); do echo -n "$word "; echo -n $word | md5sum -z; echo -n $word | sha1sum -z; echo -n $word | sha256sum -z; echo -n $word | sha512sum; done >> $rainbow.rainbow
echo "rainbow table saved to $rainbow.rainbow"
