from datetime import date
from pydantic import BaseModel

class BookCreate(BaseModel):

    name : str
    description : str
    author : str
    date_publication : date
    disponibility : bool
    id_lending : int

class BookOut(BaseModel):
    id : int
    name : str
    description : str
    author : str
    date_publication : date
    disponibility : bool
    id_lending : int

    class Config:
        from_attributes = True