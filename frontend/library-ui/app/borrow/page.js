"use client";

import { useState } from "react";

export default function Borrow() {

  const [memberId,setMemberId] = useState("");
  const [bookId,setBookId] = useState("");

  const borrow = async () => {

    await fetch("/api/borrow",{
      method:"POST",
      body:JSON.stringify({member_id:memberId,book_id:bookId})
    });

    alert("Book borrowed!");
  };

  return (

    <div>

      <h1>Borrow Book</h1>

      <input placeholder="Member ID"
        onChange={e=>setMemberId(e.target.value)}
      />

      <input placeholder="Book ID"
        onChange={e=>setBookId(e.target.value)}
      />

      <button onClick={borrow}>
        Borrow
      </button>

    </div>

  );
}