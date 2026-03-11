
import uuid
from sqlalchemy import Column, String
from app.db.base import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
