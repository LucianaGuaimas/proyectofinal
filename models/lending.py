from sqlalchemy import Column, Date, ForeignKey, Integer
from database import Base

class Lending(Base):
    __tablename__ = "lending"
    id = Column(Integer, primary_key=True, index=True)
    date_entry = Column(Date)
    date_end = Column(Date)
    id_user = Column(Integer, ForeignKey("user.id"))

    