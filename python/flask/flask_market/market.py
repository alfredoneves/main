#!/usr/bin/python3

from flask import Flask, render_template

# https://getbootstrap.com/docs/4.5/getting-started/introduction/ bootstrap will take care of style for me

app = Flask(__name__)	# creates an instance of Flask with the current script

@app.route("/")	# decorator that runs before the function and tells the root path to the app
@app.route("/home")	# two links to the same page
def home_page():
	return render_template("home.html")	# renders page from templates directory
	
@app.route("/about/<username>")	# dynamic route because of the <username>
def about(username):
	return f"About page of {username}"
