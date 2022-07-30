from pydantic import BaseModel
from datetime import datetime


# base model
class BoardBase(BaseModel):
    title: str
    content: str
    created_at: datetime


# when you create with BoardBase
class BoardCreate(BoardBase):
    pass


# when you read
class Board(BoardBase):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True



