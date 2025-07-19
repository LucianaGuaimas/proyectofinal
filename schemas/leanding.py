from datetime import date
from pydantic import BaseModel

class LendingCreate(BaseModel):

    date_entry : date
    date_end : date
    id_user : int
    id_book : int

class LeandingOut(BaseModel):
    date_entry : date
    date_end : date
    id_user : int
    id_book : int

    class Config:
        from_attributes = True