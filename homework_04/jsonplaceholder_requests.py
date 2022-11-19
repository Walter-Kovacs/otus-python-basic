"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientResponse, ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> list[dict]:
    async with ClientSession() as session:
        response: ClientResponse = await session.get(url)
        data: list = await response.json()
        return data


async def fetch_users_data() -> list[dict]:
    users = await fetch_json(USERS_DATA_URL)
    return users


async def fetch_posts_data() -> list:
    posts = await fetch_json(POSTS_DATA_URL)
    return posts
