
# Library Management Service

Tech Stack:
- Python
- gRPC + Protocol Buffers
- PostgreSQL
- SQLAlchemy
- Prometheus Metrics

Architecture:

Controller → Service → Repository → Database

Features:

- Borrow / Return workflow
- UUID identifiers
- Pagination support
- Due date tracking
- Structured logging
- Prometheus observability
- Docker database setup

Setup:

pip install -r requirements.txt

Create DB:

CREATE DATABASE library_db;

Run schema:

psql -d library_db -f db/schema.sql

Generate protobuf:

python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/library.proto

Run server:

python app/main.py

Server:
localhost:50051

Metrics:
http://localhost:8000/metrics
