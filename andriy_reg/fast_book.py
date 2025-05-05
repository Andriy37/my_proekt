from fastapi import FastAPI, HTTPException, Query, Request
from pydantic import BaseModel, Field, Annotated 
app = FastAPI()

library = {}

class Book(BaseModel):
    title: str = Field(...,title="Назва книги", description="Назва книги повинна бути", min_length=1)
    author: str = Field(...,title="Автор", description="Імя автора", min_length=3, max_length=30)
    pages: int = Field(...,title="Кількість сторінок", description="більше 10",gt=10 )
    
@app.post("/books/", response_model=Book)
async def create_book(book:Book):
    author = book.author
    if author not in library:
        library[author] = []
    library[author].append(book)
    return book

@app.get("/books")
async def get_books(author = Query(..., title="Автор")):
    if author not in library:
        raise HTTPException(status_code=404,detail="автор не знайдений")
    return library[author]

@app.put("/books/")
async def update_book(book:Book):
    author = book.author
    if author not in library:
        raise HTTPException(status_code=404,detail="автор не знайдений")
    for b in library[author]:
        if b.title == book.title:
            b.pages = book.pages
            return {"Книга оновлена"}
    raise HTTPException(status_code=404, detail="Лєєєє брат нема книжки")

@app.delete("/books/")
async def delete_book(title: str, author: str):
    if author not in library:
        raise HTTPException(status_code=404,detail="автор не знайдений")
    for book in library[author]:
        if book.title == title:
            library[author].remove(book)
            return {"ААЙЙЙ брат видалили"}
    raise HTTPException(status_code=404,detail="автор не знайдений")