#!/bin/bash

echo "this script takes a private key and decrypts a file"

echo "file name:"
read file_name
echo "private key:"
read private_key

echo "decrypting $file_name with key $private_key ..."
openssl pkeyutl -decrypt -inkey $private_key -in $file_name -out $file_name.decrypt
echo "output saved in $file_name.decrypt"
