#!/usr/bin/python3

import random
import string

size = 20	# password's size
chars = string.ascii_letters + string.digits + "!@#$%¨&*()-_+=<>,.:;?çÇ/\|'[{]}"	# group of symbols that will be used
rnd = random.SystemRandom()	# module to use the SO to generate a random choice
print(''.join(rnd.choice(chars) for i in range(size)))

