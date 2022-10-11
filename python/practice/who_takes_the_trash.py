# program to decide who is going to take out the trash

import random 

print("write the name of the participants to take out the trash")

# make a list with the participants
participants = []
while True:
	participant = input("type the name of a participant (q for stop and choose): ")
	if participant != "q":
		participants.append(participant)
	else:
		break

# choose one participant to take out the trash
print(random.choice(participants))

