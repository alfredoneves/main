#!/usr/bin/python3

x = 7
print(f"object identity of variable x={id(x)}")


def test_id(param):
	print(f"object identity of parameter received: {id(param)}")
	
	
test_id(x)

# an int is a immutable object, so when you try to change it in a function the function creates a new object
def change_obj(param):
	print(f"parameter identity before modification: {id(param)}")
	param = 1
	print(f"new object created because of the modification: {id(param)}")
	

change_obj(x)
