#!/usr/bin/python3

import webbrowser
from tkinter import *

root = Tk( )
root.title("Open browser")
root.geometry("300x200")

def google():
	webbrowser.open("www.google.com")
	
def youtube():
	webbrowser.open("www.youtube.com")
	
my_google = Button(root, text="Open Google", command=google).pack(pady=1)
youtube = Button(root, text="Open Youtube", command=youtube).pack(pady=1)
root.mainloop()
print("finished")
