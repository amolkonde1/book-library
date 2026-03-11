
import library_pb2
import library_pb2_grpc

from app.db.session import SessionLocal
from app.repositories.book_repository import BookRepository
from app.repositories.member_repository import MemberRepository
from app.repositories.borrow_repository import BorrowRepository
from app.services.library_service import LibraryService

from app.observability.metrics import borrow_requests_total, borrow_latency_seconds
from app.utils.logger import logger

class LibraryController(library_pb2_grpc.LibraryServiceServicer):

    def _service(self):
        db = SessionLocal()
        return LibraryService(
            BookRepository(db),
            MemberRepository(db),
            BorrowRepository(db)
        )

    def BorrowBook(self, request, context):

        borrow_requests_total.inc()

        with borrow_latency_seconds.time():

            logger.info(f"Borrow request member={request.member_id} book={request.book_id}")

            service = self._service()

            record = service.borrow_book(request.member_id, request.book_id)

            return library_pb2.BorrowResponse(
                borrow_id=record.id,
                due_date=str(record.due_date)
            )
