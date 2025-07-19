from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth.hash import hash_password, verify_password
from schemas.user import UserCreate, UserOut
from models.user import User
from auth.jwt import  create_token, get_db


router = APIRouter(prefix="/user", tags=["user"]) #defino la ruta

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    hashed = hash_password(user.password)
    nuevo = User(email=user.email, hashed_password=hashed)
    db.add(nuevo) #inserto a la base
    db.commit()
    db.refresh(nuevo)
    return {"msg": "Usuario creado"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales incorrectas",
        headers={"WWW-Authenticate": "Bearer"})
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise credentials_exception #valido si las credenciales ingresadas son correctas
    #return {"msg": "Login exitoso"}
    
    access_token = create_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/view", response_model = List[UserOut])
def view_list(db: Session = Depends(get_db)):
    return db.query(User).all()
    