from fastapi import FastAPI
from database import Base, engine

#Se crean las tablas
Base.metadata.create_all(bind=engine)

# App
app = FastAPI()