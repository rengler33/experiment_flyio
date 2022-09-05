from pydantic import BaseModel


class Dream(BaseModel):
    id: int
    description: str

    class Config:
        orm_mode = True
