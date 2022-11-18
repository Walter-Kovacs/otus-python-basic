"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_posts_data, fetch_users_data
from homework_04.models import async_engine, Base, User, Post, Session


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def load_users_into_db(session: AsyncSession, users_data: list[dict]):
    for ud in users_data:
        user = User(id=ud['id'], name=ud['name'], username=ud['username'], email=ud['email'])
        session.add(user)

    await session.commit()


async def load_posts_into_db(session: AsyncSession, posts_data: list[dict]):
    for pd in posts_data:
        post = Post(id=pd['id'], user_id=pd['userId'], title=pd['title'], body=pd['body'])
        session.add(post)

    await session.commit()


async def create_data_in_db(session: AsyncSession):
    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(fetch_users_data(), fetch_posts_data())
    
    await load_users_into_db(session, users_data)
    await load_posts_into_db(session, posts_data)


async def async_main():
    await create_tables()

    async with Session() as session:
        await create_data_in_db(session)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
