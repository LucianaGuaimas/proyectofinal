from datetime import date
from pydantic import BaseModel

class BookCreate(BaseModel):

    name : str
    description : str
    author : str
    date_publication : date
    disponibity : bool
    id_lending : int

class BookOut(BaseModel):
    name : str
    description : str
    author : str
    date_publication : date
    disponibity : bool
    id_lending : int

    class Config:
        orm_mode = True