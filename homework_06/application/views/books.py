from http import HTTPStatus

from flask import (
    Blueprint,
    Response,
    redirect,
    render_template,
    request,
    url_for,
)

from crud.author import (
    get_all_authors,
    get_author_by_id,
)
from crud.book import (
    create_book,
    get_all_books,
    get_book_by_id,
)
from forms.book import BookForm
from models import (
    Author,
    Book,
)

books_bp = Blueprint(
    "books",
    __name__,
)

END_POINT_LIST = "LIST"
END_POINT_DETAILS = "DETAILS"
END_POINT_ADD = "ADD"


@books_bp.get(
    "/",
    endpoint=END_POINT_LIST,
)
def list_books():
    books: list[Book] = get_all_books()
    return render_template("books/list.html", books=books)


@books_bp.get(
    "/<int:book_id>/",
    endpoint=END_POINT_DETAILS,
)
def book_details(book_id: int):
    book: Book = get_book_by_id(book_id)
    if book is not None:
        return render_template("books/details.html", book=book)

    return Response(status=HTTPStatus.NOT_FOUND)


@books_bp.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint=END_POINT_ADD,
)
def add_book():
    form = BookForm()
    form.authors.choices = [(author.id, author.name) for author in get_all_authors()]

    if request.method == "GET":
        return render_template("books/add.html", form=form)

    # method POST
    if not form.validate_on_submit():
        return render_template("books/add.html", form=form), HTTPStatus.BAD_REQUEST

    authors: list[Author] = [get_author_by_id(author_id) for author_id in form.authors.data]
    book: Book = create_book(
        authors=authors,
        title=form.title.data,
        abstract=form.abstract.data,
        count=form.count.data,
    )

    return redirect(
        url_for(
            f"{books_bp.name}.{END_POINT_DETAILS}",
            book_id=book.id,
        )
    )
