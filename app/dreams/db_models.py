from sqlalchemy import Column, Integer, String

from app.database import Base


class Dream(Base):
    __tablename__ = "dreams"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
