"""
utils.py - Database and helper functions for Jigyasa V2
Author: [Your Name]
"""

import sqlite3
from contextlib import closing
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Tuple, Optional

DB_PATH = Path("jigyasa_data.db")


def get_conn() -> sqlite3.Connection:
    """Return a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db() -> None:
    """Initialize the database tables if not present."""
    with closing(get_conn()) as conn, conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS books(
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT,
                total_copies INTEGER NOT NULL DEFAULT 0,
                available_copies INTEGER NOT NULL DEFAULT 0
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                book_id TEXT NOT NULL,
                borrow_date TEXT NOT NULL,
                due_date TEXT NOT NULL,
                return_date TEXT,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(book_id) REFERENCES books(id)
            )
        """)


# ------------------ Books ------------------

def upsert_book(book: Tuple[str, str, str, int, int]) -> None:
    """Insert or update a book record."""
    with closing(get_conn()) as conn, conn:
        conn.execute("""
            INSERT INTO books(id, title, author, total_copies, available_copies)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                title=excluded.title,
                author=excluded.author,
                total_copies=excluded.total_copies,
                available_copies=excluded.available_copies
        """, book)


def list_books() -> List[Tuple]:
    """Return all books ordered by title."""
    with closing(get_conn()) as conn, conn:
        return conn.execute("SELECT id, title, author, total_copies, available_copies FROM books ORDER BY title").fetchall()


# ------------------ Students ------------------

def upsert_student(student: Tuple[str, str, str]) -> None:
    """Insert or update a student record."""
    with closing(get_conn()) as conn, conn:
        conn.execute("""
            INSERT INTO students(id, name, email)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                name=excluded.name,
                email=excluded.email
        """, student)


def list_students() -> List[Tuple]:
    """Return all students ordered by name."""
    with closing(get_conn()) as conn, conn:
        return conn.execute("SELECT id, name, email FROM students ORDER BY name").fetchall()
