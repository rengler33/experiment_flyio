from sqlalchemy.orm import Session

from app.dreams import db_models, schemas


def create_dream(db: Session, dream: schemas.Dream):
    db_dream = db_models.Dream(description=dream.description)
    db.add(db_dream)
    db.commit()
    db.refresh(db_dream)
    return db_dream


def get_dreams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Dream).offset(skip).limit(limit).all()
