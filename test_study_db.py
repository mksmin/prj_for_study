import asyncio

from datetime import datetime
from functools import wraps
from sqlalchemy import Integer, DateTime, String, Column, select, text, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config.config import get_tokens

postgres_token = asyncio.run(get_tokens('PostSQL_host'))
engine = create_async_engine(url=postgres_token,
                             echo=True)
async_session = async_sessionmaker(bind=engine)

str_users = {
    "1": {
        "name": "Max",
        "last_name": "Minin",
        "email": "max@max.ru",
        "posts": {
            "1": "money",
            "2": "power"
        }
    },
    "2": {
        "name": "Dima",
        "last_name": "Bokach",
        "email": "dima@b.ru",
    },
    "3": {
        "name": "Nastya",
        "last_name": "Ivanova",
        "email": "sexy@babe.ru",
    },
    "4": {
        "name": "Anna",
        "last_name": "Kolycheva",
        "email": "nice@boobs.ru",
    },
    "5": {
        "name": "Bayram",
        "last_name": "Mamedov",
        "email": "teamlead@cool.ru",
    },
    "6": {
        "name": "Mark",
        "last_name": "Malinovsky",
        "email": "kamen@game.ru",
    }
}


def connector(function):
    # print(f'1. Type of func: {type(function)}')

    @wraps(function)
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            # print(f'2. Type of func: {type(function)}')
            # print(f'args = {list(*args)}')
            # print(f'kwargs = {list(kwargs)}')
            return await function(session, *args, **kwargs)

    # print(f'3. Type of wrapper: {type(wrapper)}')
    return wrapper


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class TimestampsMixin:
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)


class User(TimestampsMixin, Base):
    __tablename__ = 'users'

    first_name: Mapped[String] = mapped_column(String(30), nullable=True)
    last_name: Mapped[String] = mapped_column(String(30), nullable=True)
    email: Mapped[String] = mapped_column(String(50), nullable=True)
    posts = mapped_column(JSON, nullable=True)

    # def __str__(self):
    #     return (
    #         f'{self.__class__.__name__}(name='
    #         f'{self.first_name + ' ' + self.last_name!r}, '
    #         # f'email={self.email!r}, '
    #         f'posts={self.posts!r})'
    #     )


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


@connector
async def create_user(session, name, last_name, email, posts: JSON = None):
    user = User(
        first_name=name,
        last_name=last_name,
        email=email,
        posts=posts
    )
    # print(f'{user = }')
    # print(f'repr user = {repr(user)}')
    # print(f'dict_user = {user.__dict__}')
    # print(type(user))
    # print()

    session.add(user)
    await session.commit()


async def add_user(users_list):
    for user in users_list:
        await asyncio.sleep(1)
        # list_ = [f'{x}']
        print(f"users list = {users_list[user].items()}")
        await create_user(**users_list[user])


@connector
async def read_db(session):
    # result = await session.scalar(select(User))  # выбираем одного
    # users = await session.execute(select(User))  # Выбираем все объекты получаем тюпл с объектами внутри
    # like_as = await session.execute(select(User).where(User.first_name.like('M%')))
    # column_name = await session.execute(text("select * from users"))
    # column_name = await session.execute(select(Base.metadata.tables['users']))
    # print(f'column_name = {column_name.keys()}')

    # users_as_scalar = await session.scalars(select(User).where(User.posts.op('->>')('1') == 'money'))  # Пример, что есть значение у такого ключа
    users_as_scalar = await session.scalar(select(User).filter(User.posts.op('->')('1') != None))  # Пример, что такой ключ есть
    #
    print(f'users_as_scalar = {type(users_as_scalar)}')
    print(f'{dir(users_as_scalar)}')
    print(users_as_scalar)

    # for user in users_as_scalar:
    #     print(user)

    # users_as_execute = await session.execute(select(User))
    # print(f'users_as_execute = {users_as_execute}')
    #
    # for user in users_as_execute:
    #     print(user[0])


    #
    # for user in users:
    #     # user = [*user]
    #     user = user[0]
    #     print(f'user = {user}')
    #     print(f"user name = {user.first_name}")
    #     print()
    #
    # like_1 = [row._asdict() for row in like_as]
    # print(f"like_as = {like_as}")
    #
    # print(f"result = {result}")
    # print(f'user = {users}')
    # print(f"like_1 = {like_1}")


async def main():
    # await create_tables()
    # await create_user(name, last_name, email)
    # await add_user(str_users)
    await read_db()


if __name__ == '__main__':
    asyncio.run(main())
