from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql://username:passwd!@localhost:5432/library",
)

SECRET_KEY = getenv(
    "SECRET_KEY",
    "asdfqwerzxcvwertasfd08345-1sfaq0jaz1!!a==andlq34t"
)


class Config:
    ENV = ""
    DEBUG = False
    TESTING = False
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
