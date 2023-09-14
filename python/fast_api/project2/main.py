#!/usr/bin/python3

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import CONN, Person, Tokens
from secrets import token_hex

app = FastAPI()


def connect_db():
	engine = create_engine(CONN, echo=True)
	Session = sessionmaker(bind=engine)
	return Session()
	

@app.post("/logon")
def logon(name: str, user: str, password: str):
	session = connect_db()
	# attention to the variables here if there's a problem
	user_info = session.query(Person).filter_by(user=user, password=password).all()
	if len(user_info) == 0:
		data = Person(name=name, user=user, password=password)	# instances an object of the class Person
		session.add(data)	# adds the data into the database
		session.commit()	# commits
		return {"status": "success"}
	else:
		return {"status": "user already on the system"}
