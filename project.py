from fastapi import FastAPI
from database import get_db, engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel, field_validator
from fastapi import Depends
import datetime

app = FastAPI()

class Bookstore(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str
    @field_validator('publish_date')
    @classmethod
    def parse_custom_date(cls, value: str):
        try:
            # Parse 'DD-MM-YYYY' string into a real date object
            return datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Date must be in DD-MM-YYYY format")

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