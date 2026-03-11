
import grpc
from concurrent import futures

import library_pb2_grpc
from app.controllers.library_controller import LibraryController
# from prometheus_client import start_http_server

def serve():

    # start_http_server(8000)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    library_pb2_grpc.add_LibraryServiceServicer_to_server(
        LibraryController(),
        server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("Library gRPC server running on port 50051")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()
