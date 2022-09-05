from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.dreams import schemas, services
from app.utils import get_message

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": get_message()}


@app.get("/dreams/", response_model=list[schemas.Dream])
def read_dreams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dreams = services.get_dreams(db, skip=skip, limit=limit)
    return dreams

@app.post("/dreams/", response_model=schemas.Dream)
def create_dream(dream: schemas.Dream, db: Session = Depends(get_db)):
    return services.create_dream(db=db, dream=dream)
