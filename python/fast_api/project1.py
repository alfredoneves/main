#!/usr/bin/python3

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()


class Todo(BaseModel):
	task: str
	done: bool
	deadline: Optional[date]
	
	
todo_list = []

@app.post("/insert")
def insert(todo: Todo):
	try:
		todo_list.append(todo)
		return {"status": "success"}
	except:
		return {"status": "error"}
		
@app.post("/list")
def list_tasks(option: int=0):
	if option == 0:
		return todo_list
	elif option == 1:
		return list(filter(lambda x: x.done == False, todo_list))
	elif option == 2:
		return list(filter(lambda x: x.done == True, todo_list))
	else:
		return "Invalid option, chose 1, 2 or 3!"

@app.get("/task/{id}")
def get_task(id: int):
	try:
		return todo_list[id]
	except:
		return "task id not found!"

@app.post("/change_status")
def change_status(id: int):
	try:
		todo_list[id].done = not todo_list[id].done
		return {"status": "success"}
	except:
		return {"status": "error"}
		
@app.post("/delete")
def delete(id: int):
	try:
		del todo_list[id]
		return {"status": "success"}
	except:
		return {"status": "error"}
