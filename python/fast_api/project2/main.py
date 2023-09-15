#!/usr/bin/python3

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import CONN, Person, Tokens
from secrets import token_hex

app = FastAPI()


def connect_db():
	"""Creates a session in the database (you need it to interact with the database)"""
	engine = create_engine(CONN, echo=True)
	Session = sessionmaker(bind=engine)
	return Session()
	

@app.post("/logon")
def logon(name: str, user: str, password: str):
	session = connect_db()
	user_info = session.query(Person).filter_by(user=user, password=password).all()	# Person is a database class
	if len(user_info) == 0:
		data = Person(name=name, user=user, password=password)	# instances an object of the class Person
		session.add(data)	# adds the data into the database
		session.commit()	# commits
		return {"status": "success"}
	else:
		return {"status": "user already on the system"}

@app.post("/login")
def login(user: str, password: str):
	session = connect_db()
	user_info = session.query(Person).filter_by(user=user, password=password).all()
	
	if len(user_info) == 0:
		return {"status": "User not found"}
	
	while True:
		token = token_hex(50)	# generates 50 bytes (or 100 hex characters)
		token_exist = session.query(Tokens).filter_by(token=token).all()	
		
		if len(token_exist) == 0:
			person_exist = session.query(Tokens).filter_by(id_person=user_info[0].id).all()
			
			if len(person_exist) == 0:
				new_token = Tokens(id_person=user_info[0].id, token=token)
				session.add(new_token)
			else:
				person_exist[0].token = token
			
			session.commit()
			break
	return token
		
