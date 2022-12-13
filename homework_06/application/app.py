from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from models import db
from models import Author
from models import Book
from views.authors import authors_bp
from views.books import books_bp

app = Flask(__name__)
app.register_blueprint(authors_bp, url_prefix="/authors/")
app.register_blueprint(books_bp, url_prefix="/books/")

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://username:passwd!@localhost:5432/library"
app.config["SECRET_KEY"] = "asdf"

CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.get("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
