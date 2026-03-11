
from app.models.member import Member

class MemberRepository:

    def __init__(self, db):
        self.db = db

    def create(self, member):
        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)
        return member

    def get(self, member_id):
        return self.db.query(Member).filter(Member.id == member_id).first()
