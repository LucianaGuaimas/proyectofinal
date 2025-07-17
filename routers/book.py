from typing import List
from fastapi import APIRouter, Depends
from auth.jwt import get_db
from models.book import Book
from models.lending import Lending
from schemas.book import BookCreate, BookOut
from sqlalchemy.orm import Session



router = APIRouter(prefix="/book", tags=["book"])

@router.post("/register", response_model=BookOut)
def register(book : BookCreate, db: Session = Depends(get_db)):
    new_book = Book(name=book.name, description=book.description, author=book.author, date_publication=book.date_publication, disponibility=book.disponibility, id_lending=book.id_lending)
    db.add(new_book) #inserto a la base el nuevo libro
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/view", response_model=List[BookOut])
def view_list(db: Session = Depends(get_db)):
    return db.query(Book).all()

    