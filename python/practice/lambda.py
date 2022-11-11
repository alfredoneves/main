#!/usr/bin/python3

x = lambda x: x ** 2
list1 = [2, 4, 6, 8]
for i in list1:
	print(x(i))
print("------------------------")

list2 = ["a", "b", "c"]
y = lambda x: x.upper() 
print(list(map(y, list2)))
print("------------------------")

def myfunc(x):
	return lambda a: a / x
first = myfunc(2)
print(first(20))
print("------------------------")


