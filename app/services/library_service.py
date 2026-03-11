
from datetime import datetime, timedelta
from app.models.book import Book
from app.models.member import Member
from app.models.borrow_record import BorrowRecord

class LibraryService:

    def __init__(self, book_repo, member_repo, borrow_repo):
        self.book_repo = book_repo
        self.member_repo = member_repo
        self.borrow_repo = borrow_repo

    def create_book(self, title, author, isbn, total_copies):
        book = Book(
            title=title,
            author=author,
            isbn=isbn,
            total_copies=total_copies,
            available_copies=total_copies
        )
        return self.book_repo.create(book)

    def create_member(self, name, email, phone):
        member = Member(name=name, email=email, phone=phone)
        return self.member_repo.create(member)

    def borrow_book(self, member_id, book_id):
        book = self.book_repo.get(book_id)

        if not book:
            raise Exception("Book not found")

        if book.available_copies <= 0:
            raise Exception("Book unavailable")

        # reduce inventory
        book.available_copies -= 1
        self.book_repo.commit()

        record = BorrowRecord(
            member_id=member_id,
            book_id=book_id,
            status="BORROWED",
            due_date=datetime.utcnow() + timedelta(days=14)
        )

        return self.borrow_repo.create(record)

    def return_book(self, borrow_id):
        record = self.borrow_repo.get(borrow_id)
        if not record:
            raise Exception("Borrow record not found")

        record.status = "RETURNED"
        self.borrow_repo.db.commit()

        book = self.book_repo.get(record.book_id)
        book.available_copies += 1
        self.book_repo.db.commit()

        return record

    def borrowed_books_by_member(self, member_id):
        return self.borrow_repo.list_by_member(member_id)
