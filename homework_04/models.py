"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
)
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    relationship,
    sessionmaker,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, unique=True, primary_key=True)


async_engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=False)
Base = declarative_base(bind=async_engine, cls=Base)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)

    posts = relationship('Post', back_populates='user', uselist=True)


class Post(Base):
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)

    user = relationship('User', back_populates='posts', uselist=False)
