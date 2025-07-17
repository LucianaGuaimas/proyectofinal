from database import SessionLocal

#aqui se crea la conexiom  
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()