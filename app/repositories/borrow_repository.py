
from app.models.borrow_record import BorrowRecord

class BorrowRepository:

    def __init__(self, db):
        self.db = db

    def create(self, record):
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def get(self, record_id):
        return self.db.query(BorrowRecord).filter(BorrowRecord.id == record_id).first()

    def list_by_member(self, member_id):
        return self.db.query(BorrowRecord).filter(BorrowRecord.member_id == member_id).all()
