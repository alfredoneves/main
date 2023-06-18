# run in virtual environment
# pip install chatterbot && pip install spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer	# lib to train using a list
from os import system

# bug fix
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
	ISO_639_1 = "en_core_web_sm"

chatbot = ChatBot("my_bot", tagger_language=ENGSM)

conversation = ["Hi", "Hey, what's up?", "I'm ok", "Cool!", "What are you studying?", "python", "I'm sleepy", "Coffe time!"]

trainer = ListTrainer(chatbot)	# selects the bot
trainer.train(conversation)	# train the bot using the conversation
system("clear")	# removes the output from download

while True:
	user_message = input("Talk to chatbot: ")
	if user_message.lower() == "quit":
		break
	bot_message = chatbot.get_response(user_message)
	print(bot_message)
print("Goodbye!")

# chatbot.storage.drop() removes the saved train
