#!/usr/bin/python3

class fibonacci:
	def __init__(self, max=1000):
		self.current_element, self.next_element = 0, 1
		self.max = max	# defines the limit for the sequence
		
	def __iter__(self):
		return self	# returns the iterable object
		
	def __next__(self):
		if self.next_element > self.max:	# stops at the max value
			raise StopIteration
		
		return_value = self.current_element	# saves the value to be returned
		# updates the sequence
		self.current_element, self.next_element = self.next_element, self.current_element + self.next_element
		return return_value
		
if __name__ == "__main__":	# executed the code
	fibonacci_object = fibonacci(max=1000)
	
for number in fibonacci_object:
	print(number)

