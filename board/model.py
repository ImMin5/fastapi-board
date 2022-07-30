from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from datetime import datetime


class Board(Base):
    __tablename__= "boards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now)

