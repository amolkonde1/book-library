
# Book Library Service

This service manages:

- Books
- Members
- Borrow/Return operations

Tech stack:

Python
gRPC + Protocol Buffers
PostgreSQL
SQLAlchemy
Prometheus metrics

---

# Features

Clean Architecture

Controller → Service → Repository

Transaction-aware borrow logic

Due date tracking

Pagination support

Metrics scaffold

Docker database setup

---

# Setup

## Install dependencies

pip install -r requirements.txt

## Create database

CREATE DATABASE library_db;

Run schema

psql -d library_db -f db/schema.sql

---

# Generate gRPC Code

python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/library.proto

Generated:

library_pb2.py
library_pb2_grpc.py

---

# Run Application

python app/main.py

Server runs at

localhost:50051

---

# Test

grpcurl -plaintext localhost:50051 list

---

# Architecture

Controller Layer → gRPC transport

Service Layer → business rules

Repository Layer → database access

Observability → Prometheus metrics

---
