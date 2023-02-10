#!/usr/bin/python3

from cryptography.fernet import Fernet	# the cryptography library has a lot of modules

key = Fernet.generate_key()	# generate a secret key that will be used in the cryptography
print(f"key: {key}")

f = Fernet(key)	# instances the Fernet class and uses the key to future cryptography
print(f"fernet: {f}")

message = f.encrypt(b"this is a secret message")	# encrypts the message
print(f"encrypted message: {message}")

dec = f.decrypt(message)	# decrypts the message
print(f"decrypted message: {dec}")
