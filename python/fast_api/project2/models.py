#!/usr/bin/python3

import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# preparation of the database
#CREATE DATABASE fast_api;
#CREATE USER 'test'@'localhost' IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON fast_api.* TO 'test'@'localhost';
#FLUSH PRIVILEGES;
#SHOW GRANTS FOR 'test'@'localhost';

USER = "test"
PASSWORD = "password"
HOST = "localhost"
DATABASE = "fast_api"	# database created
PORT = 3306

CONN = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"	# connection string

engine = create_engine(CONN, echo=True)	# when in production change echo to False
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()	# class that is a table of the database, so the other class will inherit it


class Person(Base):
	__tablename__ = "Person"	# creates tables
	id = Column(Integer, primary_key=True)	# defines a column characteristcs
	name = Column(String(50))	# limits the size of the string
	user = Column(String(20))
	password = 	Column(String(10))
	
	
class Tokens(Base):
	__tablename__ = "Tokens"
	id = Column(Integer, primary_key=True)
	id_person = Column(Integer, ForeignKey("Person.id"))
	token = Column(String(100))
	data = Column(DateTime, default=datetime.datetime.utcnow())
	
	
Base.metadata.create_all(engine)
