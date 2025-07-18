from datetime import date
from typing import Optional
from pydantic import BaseModel

class BookCreate(BaseModel):

    name : str
    description : str
    author : str
    date_publication : date
    disponibility : bool

class BookUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    date_publication: Optional[date] = None
    disponibility: Optional[bool] = None
    

class BookOut(BaseModel):
    id : int
    name : str
    description : str
    author : str
    date_publication : date
    disponibility : bool
    

    class Config:
        from_attributes = True