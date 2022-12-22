from models import Book, db


# ***************************** CREATE *****************************
def create_book(**book_params) -> Book:
    book: Book = Book(**book_params)
    db.session.add(book)
    db.session.commit()

    return book


# ***************************** READ *****************************
def get_all_books() -> list[Book]:
    return Book.query.order_by(Book.title).all()


def get_book_by_id(book_id: int) -> Book | None:
    return Book.query.get(book_id)

# ***************************** UPDATE *****************************
# ***************************** DELETE *****************************
