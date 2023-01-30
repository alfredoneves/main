#!/usr/bin/python3

def fibonacci(max):
	current_element, next_element = 0, 1
	
	while current_element < max:
		yield current_element	# like return, but with iteration
		
		current_element, next_element = next_element, current_element + next_element
		
if __name__ == "__main__":
	fibonacci_generator = fibonacci(1000)
	for number in fibonacci_generator:
		print(number)

