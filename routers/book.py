from typing import List
from fastapi import APIRouter, Depends, HTTPException
from auth.jwt import get_db
from models.book import Book
from schemas.book import BookCreate, BookOut, BookUpdate
from sqlalchemy.orm import Session



router = APIRouter(prefix="/book", tags=["book"])

@router.post("/register", response_model=BookOut)
def register(book : BookCreate, db: Session = Depends(get_db)):
    new_book = Book(name=book.name, description=book.description, author=book.author, date_publication=book.date_publication, disponibility=book.disponibility)
    db.add(new_book) #inserto a la base el nuevo libro
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/view", response_model=List[BookOut])
def view_list(db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.put("/update/{id}")
def update_book(id:int, book_update:BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first() #aqui trae la instacia de Book

    if not book:
        raise HTTPException(status_code=404, detail="El libro no existe")
    
    if book_update.disponibility is not None:
        book.disponibility = book_update.disponibility  #cambio el valor
    db.commit()
    db.refresh()
    return {"mensaje": "Libro actualizado correctamente"}
    

@router.delete("/delete/{id}")
def delete_book(id:int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first() #aqui trae la instacia de Book
 
    if not book:
        raise HTTPException(status_code=404, detail="El libro no existe")
    db.delete(book) #eliminamos el libro 
    db.commit()
    return {"mensaje": "Libro eliminado correctamente"}
    