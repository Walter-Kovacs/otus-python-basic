from os import getenv

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

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.get("/")
def home():
    return render_template("home.html")
