#!/usr/bin/python3

from functools import reduce

def my_sum(a, b):
	print(f"{a} + {b}")
	return a + b
	
my_list = [1, 5, 19, 32]

# use a function
print(reduce(my_sum, my_list))	# the reduce function applies a function to a list and reduces it

print("--------------\n")
# use lambda function
print(reduce(lambda x,y: x * y, my_list))
