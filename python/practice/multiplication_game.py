#!/usr/bin/python3

from random import randint


player_points = 0
computer_points = 0
print("Game started, answer with the product of the two numbers to win! (press q to exit)")

while True:
	a = randint(1, 10)
	b = randint(1, 10)
	computer_unluck = randint(1, 8)
	
	# receive the answer
	answer = input(f"{a} X {b} = ? ")
	if answer.lower() == "q":
		break
	else:
		answer = int(answer)
		
	if answer == a * b:
		print(f"Your answer: {answer} ---> Correct!")
		player_points += 1
	else:
		print(f"Your answer: {answer} ---> Incorrect!")
		
	# computer answer
	if computer_unluck == 1:
		computer = a * b - (randint(1, 10))
		print(f"Computer answer: {computer} ---> Incorrect!")
	elif computer_unluck == 2:
		computer = a * b + (randint(1, 10))
		print(f"Computer answer: {computer} ---> Incorrect!")
	else:
		computer = a * b
		computer_points += 1
		print(f"Computer answer: {computer} ---> Correct!")

		
if player_points > computer_points:
	print("You won!")
elif player_points < computer_points:
	print("You lost!")
else:
	print("Draw!")
	
print(f"Your points: {player_points}")
print(f"Computer points: {computer_points}")
