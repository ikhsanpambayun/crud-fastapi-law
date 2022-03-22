from secrets import token_hex
from sqlalchemy.orm import Session
import models, schemas


# get guitar by id
def get_guitar(db: Session, id: int):
    return db.query(models.Guitar).filter(models.Guitar.id == id).first()


# get all guitar
def get_guitars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Guitar).offset(skip).limit(limit).all()


# create guitar
def create_guitar(db: Session, guitar: schemas.Guitar):
    db_guitar = models.Guitar(
        id = guitar.id,
        name = guitar.name,
        type = guitar.type,
        description = guitar.description
        )
    db.add(db_guitar)
    db.commit()
    db.refresh(db_guitar)
    return db_guitar


# update guitar
def update_guitar(db: Session, guitar: schemas.Guitar):
    db_guitar = get_guitar(db, guitar.id)
    db_guitar.name = guitar.name
    db_guitar.type = guitar.type
    db_guitar.description = guitar.description
    db.commit()
    db.refresh(db_guitar)
    return get_guitar(db, guitar.id)


# delete guitar
def delete_guitar(db: Session, id:int):
    db.query(models.Guitar).filter(models.Guitar.id == id).delete()
    db.commit()
    return True