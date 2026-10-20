from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet")
def greet():
    return {"message": "Hello Nigga"}

@app.get("/greet/{name}") #path parameter
def greet_name(name: str, age: Optional[int] = None):
    if age is not None:
        return {"message": f"Hello, {name}! You are {age}, bitch."}
    return {"message": f"Hello, {name}!"}

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/students")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }