from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Length,
)


class AuthorForm(FlaskForm):
    name = StringField(
        label="Author name",
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ],
    )
    description = TextAreaField()
