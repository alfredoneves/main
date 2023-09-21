#!/usr/bin/python3


def calculate_product(*args):
	"""
	This function can receive multiple arguments
	"""
	result = 1
	
	for arg in args:
		result = result * arg

	return result


print(calculate_product(10, 20, 30))
print(calculate_product(*range(1,6,2)))	# * is needed to pass a list for example
