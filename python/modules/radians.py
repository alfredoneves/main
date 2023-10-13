#!/usr/bin/python3

import math

# rad = degrees * pi/180
pi = math.pi

for i in range(181):
	radians = i * pi / 180
	print("---------------------")
	print(f"|{i}° | {radians:.2f} radians|")
	
print("---------------------")
