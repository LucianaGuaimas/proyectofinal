from typing import List
from fastapi import APIRouter, Depends, HTTPException
from auth.jwt import get_current_user, get_db
from models.book import Book
from models.lending import Lending
from models.user import User
from schemas.leanding import LeandingOut, LendingCreate
from sqlalchemy.orm import Session


router = APIRouter(prefix="/lending", tags=["lending"])

@router.post("/register", response_model = LendingCreate)
def register_lend(lend: LendingCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    book = db.query(Book).filter(Book.id == lend.id_book).first()    
    if not book:
        raise HTTPException(status_code=404, detail="El libro no existe")
    
    if not book.disponibility:
        raise HTTPException(status_code=400, detail="El libro no está disponible")
 
    new_lend = Lending(date_entry=lend.date_entry, date_end=lend.date_end, id_user=user.id, id_book=lend.id_book)
    db.add(new_lend) #agrego a la base
    book.disponibility = False
    db.commit()
    db.refresh(new_lend)
    return new_lend

@router.get("/view", response_model=List[LeandingOut])
def view_list(db: Session = Depends(get_db)):
    return db.query(Lending).all()

@router.get("/devolution/{id}")
def devolution_lend(id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    lending = db.query(Lending).filter(Lending.id == id).first() #busca el préstamo por id
 
    if not lending:
        raise HTTPException(status_code=404, detail="El préstamo no existe")
 
    if lending.id_user != user.id:
        raise HTTPException(status_code=403, detail="El préstamo que intentas devolver no te pertenece") #Verifica que el préstamo pertenece al usuario autenticado
 
    book = db.query(Book).filter(Book.id == lending.id_book).first() #busco el libro asociado al préstamo
   
    book.disponibility = True #devuelvo el libro marcandolo como disponible
    db.commit()
    return {"mensaje": "Libro devuelto con éxito"}