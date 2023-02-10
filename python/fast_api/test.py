#!/usr/bin/python3

from fastapi import FastAPI

app = FastAPI()	# instances the class

@app.get("/")	# works when the root directory in the site is requested with a get
def root():
	return {"message": "hello world"}
	
@app.get("/login")
def login():
	return {"message:" :"login page"}


