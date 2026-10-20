from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "publish_date": "1948-06-08"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publish_date": "1960-07-11"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publish_date": "1925-04-10"
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publish_date": "1813-01-28"
    }
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{title}")
def get_book_by_title(title: str):
    for book in books:
        if book["title"] == title:
            return {"message": f"Book found", "book": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with title '{title}' not found")

class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/books")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

class BookUpdate(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.put("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publish_date"] = book_update.publish_date
            return {"message": f"Book with ID {book_id} updated successfully", "book": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID '{book_id}' not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": f"Book with ID {book_id} deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID '{book_id}' not found")