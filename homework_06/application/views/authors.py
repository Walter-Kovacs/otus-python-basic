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
    create_author,
    get_all_authors,
    get_author_by_id,
)
from forms.author import AuthorForm
from models import Author

authors_bp = Blueprint(
    "authors",
    __name__,
)


END_POINT_LIST = "LIST"
END_POINT_DETAILS = "DETAILS"
END_POINT_ADD = "ADD"


@authors_bp.get(
    "",
    endpoint=END_POINT_LIST,
)
def list_authors():
    authors: list[Author] = get_all_authors()
    return render_template("authors/list.html", authors=authors)


@authors_bp.get(
    "/<int:author_id>/",
    endpoint=END_POINT_DETAILS,
)
def author_details(author_id: int):
    author = get_author_by_id(author_id)
    if author is not None:
        return render_template("authors/details.html", author=author)

    return Response(status=HTTPStatus.NOT_FOUND)


@authors_bp.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint=END_POINT_ADD,
)
def add_author():
    form = AuthorForm()

    if request.method == "GET":
        return render_template("authors/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("authors/add.html", form=form), HTTPStatus.BAD_REQUEST

    author: Author = create_author(
        name=form.name.data,
        description=form.description.data,
    )

    return redirect(
        url_for(
            f"{authors_bp.name}.{END_POINT_DETAILS}",
            author_id=author.id
        )
    )

