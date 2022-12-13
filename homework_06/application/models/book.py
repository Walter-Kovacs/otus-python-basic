from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from .associations import books_authors
from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Book(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(
        String(200),
        nullable=False,
    )
    abstract = Column(Text)
    count = Column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )

    authors = relationship("Author", secondary=books_authors, back_populates="books", order_by="Author.name")

    if TYPE_CHECKING:
        query: Query
