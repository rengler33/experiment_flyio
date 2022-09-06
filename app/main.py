from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database.db import mapper_registry, start_mappers
from app.dreams import schemas, services
from app.settings import DATABASE_URL
from app.utils import get_message

start_mappers()

connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
get_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mapper_registry.metadata.create_all(engine)
app = FastAPI()


def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()


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
