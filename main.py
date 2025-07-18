from fastapi import FastAPI
from database import Base, engine
from routers import book, user

#Base.metadata.drop_all(bind=engine)

#Se crean las tablas
Base.metadata.create_all(bind=engine)

# App
app = FastAPI()

app.include_router(user.router)
app.include_router(book.router)

@app.get("/")
def read_root():
    return {"message": "La app funciona correctamente"}

 