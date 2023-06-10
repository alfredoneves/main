#!/bin/bash

echo "this script generates rsa keys and encrypts a file"

echo "generating private.key ..."
openssl genrsa -aes256 -out private.key 4096
echo "private.key generated"

echo "generating public.key with private.key ..."
openssl rsa -in private.key -pubout -out public.key
echo "public.key generated"

echo "file name to encrypt:"
read file_name

echo "encrypting $file_name with public.key ..."
openssl pkeyutl -encrypt -pubin -inkey public.key -in $file_name -out $file_name.crypt
echo "encrypted file saved in $file_name.crypt"
