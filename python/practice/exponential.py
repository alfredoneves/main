#!/usr/bin/python3
# recursion example

def exponential(num):
	if num > 0:
		result = num * exponential(num-1)
	else:
		result = 1
	return result

num = int(input("type a number and receive it's exponential: "))
print(exponential(num))

