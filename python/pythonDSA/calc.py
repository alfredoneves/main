#!/usr/bin/python3

print("CALCULATOR")
print("---" * 10)

def calculator():
	operation = input("options:\n[1]-sum\n[2]-subtraction\n[3]-multiplication\n[4]-division\n[5]-quit\noperation:")
	if operation == "5":
		return "quit"
	n0 = float(input("first number:"))
	n1 = float(input("second number:"))
	
	if operation == "1":
		print(f"{n0} + {n1} = {n0 + n1}")
	elif operation == "2":
		print(f"{n0} - {n1} = {n0 - n1}")
	elif operation == "3":
		print(f"{n0} X {n1} = {n0 * n1}")
	elif operation == "4" and n1 == 0:
		print("I can't divide by zero")
	elif operation == "4":
		print(f"{n0} / {n1} = {n0 / n1}")
	else:
		print("wrong option")
	print("-" * 10 + "\n")
while True:
	try:
		if calculator() == "quit":
			break
	except:
		print("choose only one numeric option and 2 numbers")
