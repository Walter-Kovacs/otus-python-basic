from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    SelectMultipleField,
    StringField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Length,
)


class BookForm(FlaskForm):
    authors = SelectMultipleField(
        label="Author",
        validators=[
            DataRequired(),
        ],
        coerce=int,
    )
    title = StringField(
        label="Title",
        validators=[
            DataRequired(),
            Length(min=2, max=200),
        ],
    )
    abstract = TextAreaField()
    count = IntegerField()

