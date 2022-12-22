from sqlalchemy import (
    Column,
    ForeignKey,
    Table,
)

from .database import db


books_authors = Table(
    "books_authors",
    db.metadata,
    Column("author_id", ForeignKey("author.id")),
    Column("book_id", ForeignKey("book.id")),
)
