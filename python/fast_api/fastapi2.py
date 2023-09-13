#!/usr/bin/python3

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
	uid: int
	name: Optional[str]
	password: str

	
user_list = [User(uid=0, name="Alfredo", password="strongpass")]	

@app.post("/user")
def main(user: User):
	user_list.append(user)
	return "Registered user"
	
@app.get("/users")
def users():
	return user_list
	
