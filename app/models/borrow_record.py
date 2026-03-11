
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from app.db.base import Base

class BorrowRecord(Base):
    __tablename__ = "borrow_records"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    member_id = Column(String)
    book_id = Column(String)
    status = Column(String)
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
