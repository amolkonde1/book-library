
import grpc
from concurrent import futures
from prometheus_client import start_http_server

import library_pb2_grpc
from app.controllers.library_controller import LibraryController

def serve():

    start_http_server(8000)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    library_pb2_grpc.add_LibraryServiceServicer_to_server(
        LibraryController(),
        server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("gRPC server running on port 50051")
    print("Metrics at http://localhost:8000/metrics")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()
