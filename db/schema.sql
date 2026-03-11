
CREATE TABLE members (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50)
);

CREATE TABLE books (
    id UUID PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    isbn VARCHAR(50),
    total_copies INT,
    available_copies INT
);

CREATE TABLE borrow_records (
    id UUID PRIMARY KEY,
    member_id UUID,
    book_id UUID,
    status VARCHAR(20),
    due_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
