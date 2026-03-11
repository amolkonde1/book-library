"use client";

import { useEffect, useState } from "react";

export default function Home() {

  const [books, setBooks] = useState([]);

  useEffect(() => {

    fetch("/api/books")
      .then(res => res.json())
      .then(data => {
        setBooks(data.books || []);
      });

  }, []);

  return (

    <div style={{ padding: 40 }}>

      <h1>Library Books</h1>

      <ul>
        {books.map(book => (
          <li key={book.id}>
            {book.title} - {book.author}
          </li>
        ))}
      </ul>

    </div>

  );
}