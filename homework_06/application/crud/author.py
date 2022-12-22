from models import Author, db


# ***************************** CREATE *****************************
def create_author(**author_params) -> Author:
    author: Author = Author(**author_params)
    db.session.add(author)
    db.session.commit()

    return author


# ***************************** READ *****************************
def get_all_authors() -> list[Author]:
    return Author.query.order_by(Author.name).all()


def get_author_by_id(author_id: int) -> Author | None:
    return Author.query.get(author_id)

# ***************************** UPDATE *****************************
# ***************************** DELETE *****************************
