from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException, Request, Response, Form, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine

import crud, models, schemas


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/guitars/", response_model=list[schemas.Guitar])
def read_guitar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    guitars = crud.get_guitars(db, skip=skip, limit=limit)
    return guitars

@app.post("/create/guitars/", response_model=schemas.Guitar)
def create_guitar(guitar: schemas.Guitar, db: Session = Depends(get_db)):
    db_guitar = crud.get_guitar(db, id=guitar.id)
    if db_guitar:
        raise HTTPException(status_code=400, detail="Guitar is exist")
    return crud.create_guitar(db=db, guitar=guitar)

@app.post("/update/guitars/")
def update_guitar(guitar: schemas.Guitar, db: Session = Depends(get_db)):
    db_guitar = crud.get_guitar(db, id=guitar.id)
    if not db_guitar:
        raise HTTPException(status_code=400, detail="Guitar is not exist")
    return crud.update_guitar(db=db, guitar=guitar)

@app.post("/delete/guitars/")
def update_guitar(id:int, db: Session = Depends(get_db)):
    db_guitar = crud.get_guitar(db, id)
    if not db_guitar:
        raise HTTPException(status_code=400, detail="Guitar is not exist")
    crud.delete_guitar(db, id)
    return {"message": "Delete success"}