#!/usr/bin/python3
# this script receives the name and test result of students and shows the overall information about it

counter = 0
grades = {}

# storage the values in a dict with an index
while True:
	name = str(input("name of studdent (q to quit):"))
	if name.lower() == "q":
		break
	result = input("result (1- fail / 2- pass) (q to cancel and quit):")
	if result.lower() == "q":
		break
	while result != "1" and result != "2":
		result = input("result (1- fail / 2- pass) (q to cancel and quit):")
	grades[counter] = [name, int(result)]
	counter += 1
	
# calculate the results
total1 = 0
total2 = 0

for i in grades.values():
	if i[1] == 1:
		total1 += 1
	else:
		total2 += 1
		
print(f"fail counter = {total1}")
print(f"pass counter = {total2}")
print(f"total number of grades:{counter}")

if total2 >= 8:
	print("Bonus to instructor!")
