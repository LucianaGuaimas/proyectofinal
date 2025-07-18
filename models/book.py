from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    author = Column(String)
    date_publication = Column(Date)
    disponibility = Column(Boolean)
    