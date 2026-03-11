
import library_pb2
import library_pb2_grpc

from app.db.session import SessionLocal
from app.repositories.book_repository import BookRepository
from app.repositories.member_repository import MemberRepository
from app.repositories.borrow_repository import BorrowRepository
from app.services.library_service import LibraryService

class LibraryController(library_pb2_grpc.LibraryServiceServicer):

    def _service(self):
        db = SessionLocal()
        return LibraryService(
            BookRepository(db),
            MemberRepository(db),
            BorrowRepository(db)
        )

    def CreateBook(self, request, context):
        service = self._service()
        book = service.create_book(
            request.title,
            request.author,
            request.isbn,
            request.total_copies
        )

        return library_pb2.BookResponse(
            book=library_pb2.Book(
                id=book.id,
                title=book.title,
                author=book.author,
                isbn=book.isbn,
                total_copies=book.total_copies,
                available_copies=book.available_copies
            )
        )

    def ListBooks(self, request, context):
        service = self._service()
        books = service.book_repo.list(request.page, request.page_size)

        return library_pb2.ListBooksResponse(
            books=[
                library_pb2.Book(
                    id=b.id,
                    title=b.title,
                    author=b.author,
                    isbn=b.isbn,
                    total_copies=b.total_copies,
                    available_copies=b.available_copies
                )
                for b in books
            ]
        )

    def CreateMember(self, request, context):
        service = self._service()
        member = service.create_member(request.name, request.email, request.phone)

        return library_pb2.MemberResponse(
            member=library_pb2.Member(
                id=member.id,
                name=member.name,
                email=member.email,
                phone=member.phone
            )
        )

    def BorrowBook(self, request, context):
        service = self._service()
        record = service.borrow_book(request.member_id, request.book_id)

        return library_pb2.BorrowResponse(
            record=library_pb2.BorrowRecord(
                id=record.id,
                member_id=record.member_id,
                book_id=record.book_id,
                status=record.status,
                due_date=str(record.due_date)
            )
        )

    def ReturnBook(self, request, context):
        service = self._service()
        service.return_book(request.borrow_id)
        return library_pb2.ReturnResponse(message="Book returned")

    def GetBorrowedBooksByMember(self, request, context):
        service = self._service()
        records = service.borrowed_books_by_member(request.member_id)

        return library_pb2.BorrowListResponse(
            records=[
                library_pb2.BorrowRecord(
                    id=r.id,
                    member_id=r.member_id,
                    book_id=r.book_id,
                    status=r.status,
                    due_date=str(r.due_date)
                )
                for r in records
            ]
        )
