#!/usr/bin/python3

from fastapi import FastAPI

app = FastAPI()	# instances the class

users = [(0, 'alfredo'), (1, 'ana')]

@app.get("/")	# works when the root directory in the site is requested with a get
def root():
	return {"message": "hello world"}
	
@app.get("/login")
def login():
	return {"message:" :"login page"}

@app.get("/users/{id}")
def return_user_by_id(id: int):
	for user in users:
		if user[0] == id:
			return user
	
	return "User not found"

@app.post("/users/{name}")
def return_user_by_name(name: str):
	for user in users:
		if user[1] == name:
			return user
			
	return "User not found"
	
