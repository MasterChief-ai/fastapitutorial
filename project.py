from fastapi import FastAPI
from database import get_db, engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel, field_validator
from fastapi import Depends
from datetime import datetime

app = FastAPI()

class Bookstore(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/books")
def create_book(book: Bookstore, db: Session = Depends(get_db)):
    new_book = model.Book(
        id=book.id,
        title=book.title,
        author=book.author,
        publish_date=book.publish_date
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(model.Book).all()
    return books