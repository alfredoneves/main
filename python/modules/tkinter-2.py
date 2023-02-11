#!/usr/bin/python3

import requests
from tkinter import *
import random
import webbrowser
from bs4 import BeautifulSoup

def random_music():
	urls = ["https://www.youtube.com/watch?v=B1zCN0YhW1s", "https://www.youtube.com/watch?v=JGNqvH9ykfA",
	"https://www.youtube.com/watch?v=XqmknZNg1yw", "https://www.youtube.com/watch?v=xj7RMPM3A2c",
	"https://www.youtube.com/watch?v=FHypEgzJFlc", "https://www.youtube.com/watch?v=RUV5-ZqQ4o0",
	"https://www.youtube.com/watch?v=t_zOe7lmfKg", "https://www.youtube.com/watch?v=GiLYto-PhRY"]
	
	music = random.choice(urls)	# selects one element of the urls list
	
	r = requests.get(music)
	soup = BeautifulSoup(r.text, "lxml")
	music_playing['text'] = soup.find(["title"]).text
	
	webbrowser.open(music)
	
window = Tk()	# creates tkinter window
window.title("Random music")	# changes the title of the window
# window.geometry("400x400") this can change the format of the window


main_text = Label(window, text="click on the button to hear a random music")
main_text.grid(column=0, row=0, padx=10, pady=10)	# positions the main_text in the window

button = Button(window, text="open music", command=random_music)	# creates the button
button.grid(column=0, row=1, padx=10, pady=10)	# positions the button

secondary_text = Label(window, text="Music playing:")
secondary_text.grid(column=0, row=2, padx=10, pady=10)
music_playing = Label(window, text="...")
music_playing.grid(column=0, row=3, padx=10, pady=10)

window.mainloop()	# the window will stay in the screen
