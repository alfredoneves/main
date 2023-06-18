#!/usr/bin/python3

start = 200
hours = [0, 5, 10, 15]

print("Hour	Number of Bacteria")
for hour in hours:
	end = start * 2 ** hour
	size = 18 - len(str(end))
	print(f"{hour}	{size * ' '}{end}")
