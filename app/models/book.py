
import uuid
from sqlalchemy import Column, String, Integer
from app.db.base import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    author = Column(String)
    isbn = Column(String, unique=True)
    total_copies = Column(Integer)
    available_copies = Column(Integer)
