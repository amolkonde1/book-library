
from sqlalchemy import text
from app.models.book import Book

class BookRepository:

    def __init__(self, db):
        self.db = db

    def create(self, book):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def get_for_update(self, book_id):
        # transaction safe row lock
        return self.db.execute(
            text("SELECT * FROM books WHERE id = :id FOR UPDATE"),
            {"id": book_id}
        ).fetchone()

    def get(self, book_id):
        return self.db.query(Book).filter(Book.id == book_id).first()

    def list(self, page, page_size):
        return self.db.query(Book).offset(page * page_size).limit(page_size).all()

    def commit(self):
        self.db.commit()
