import random

def guessing_game():
	"""
		Try to guess the number the machine choose !
	"""
	machine = random.randint(1, 10)
	print("I choose a number (1-10)")
	print("You have 3 chances to guess it !")
	cont = 0
	while cont < 3:
		try:
			user = int(input("Guess what number a choose: "))
			cont += 1
		except:
			print("Something went wrong, please try to select an integer number (1-10) again :( ")
		# compares the number
		if user == machine:
			print(f"Congratulations you won with {cont} tries !")
			break
		elif cont == 3:
			print("You lose, but you can try again !")
		elif user < machine:
			print("My number is higher !")
		else:
			print("My number is lower !")
	
while True:
	guessing_game()
	again = input("Do you want to play again (y/n)? ").lower()
	if again == "n":
		break
	print("----------- NEW GAME ------------")
print("Thanks for playing :)")

