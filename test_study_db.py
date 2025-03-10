import asyncio

from datetime import datetime
from functools import wraps
from demo_sqlalchemy import Integer, DateTime, String, Column, select, text, JSON, BigInteger
from demo_sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from demo_sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


from config.config import get_tokens

postgres_token = asyncio.run(get_tokens('PostSQL_host'))
engine = create_async_engine(url=postgres_token,
                             echo=True)
async_session = async_sessionmaker(bind=engine)

str_users = {
    "1": {
        "firstname": "Max",
        "lastname": "Minin",
        "email": "max@max.ru",
        "posts": {
            "1": "money",
            "2": "power"
        },
        'maxxx': 'minins'
    },
    "2": {
        "firstname": "Dima",
        "lastname": "Bokach",
        "email": "dima@b.ru",
    },
    "3": {
        "firstname": "Nastya",
        "lastname": "Ivanova",
        "email": "sexy@babe.ru",
    },
    "4": {
        "firstname": "Anna",
        "lastname": "Kolycheva",
        "email": "nice@boobs.ru",
    },
    "5": {
        "firstname": "Bayram",
        "lastname": "Mamedov",
        "email": "teamlead@cool.ru",
    },
    "6": {
        "firstname": "Mark",
        "lastname": "Malinovsky",
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


class User2(Base):
    __tablename__ = 'usernew'

    datebid: Mapped[datetime] = mapped_column(nullable=True)
    idbid: Mapped[int] = mapped_column(nullable=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(50), nullable=True)
    birthday: Mapped[datetime] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    sex: Mapped[str] = mapped_column(String(10), nullable=True)
    country: Mapped[str] = mapped_column(String(100), nullable=True)
    city: Mapped[str] = mapped_column(String(250), nullable=True)
    citizenship: Mapped[str] = mapped_column(String(100), nullable=True)
    mobile: Mapped[str] = mapped_column(String(30), nullable=True)
    tgid = mapped_column(BigInteger, nullable=True)
    tgusername: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    studyplace: Mapped[str] = mapped_column(String(300), nullable=True)
    levelstudy: Mapped[str] = mapped_column(String(150), nullable=True)
    posts = mapped_column(JSON, nullable=True)

    def copy_attributes(self, other):
        self.__dict__.update(other.__dict__)

    def __str__(self):
        list_to_str = []
        print(self.__dict__)
        for key in self.__dict__:
            list_to_str.append(f'{key}={str(self.__dict__[key])}\n')

        return (
            f'{self.__class__.__name__}('
            f'{" ".join(list_to_str)})'
        )

    def dict_2_obj(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, (dict, list, tuple)):
                setattr(self, key, str(value))
                continue
            setattr(self, key, value)

            # if isinstance(value, dict):
            #     value = UserAttrs(**value)
            # if isinstance(value, (list, tuple)):
            #     setattr(self, key, [x for x in value])
            # else:
            #     setattr(self, key, value)


# class UserAttrs(object):
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             if isinstance(value, dict):
#                 value = UserAttrs(**value)
#             setattr(self, key, value)


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


@connector
async def create_user(session, kwargs):

    user = User2()
    user.dict_2_obj(kwargs)
    text_request = text(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{'usernew'}'")
    column_name = await session.execute(text_request)
    columns = set([col[0] for col in column_name])

    sql_types = {
        'str': 'VARCHAR(250)',
        'int': 'int',
        'date': 'date'
    }

    difference_column = set(user.__dict__.keys()).difference(columns)

    difference_column.discard('_sa_instance_state')


    # if difference_column:
    #     for name_col in difference_column:
    #         name_db = 'usernew'
    #         col = name_col
    #
    #         text_table = text(f'ALTER TABLE {name_db} ADD {col} {String(25)}')
    #
    #         await session.execute(text_table)

    session.add(user)
    await session.commit()


async def add_user(users_list):
    for user in users_list:
        # await asyncio.sleep(1)
        print(users_list[user])
        print(f"users list = {users_list[user].items()}")
        await create_user(users_list[user])


@connector
async def read_db(session):
    # result = await session.scalar(select(User))  # выбираем одного
    # users = await session.execute(select(User))  # Выбираем все объекты получаем тюпл с объектами внутри
    # like_as = await session.execute(select(User).where(User.first_name.like('M%')))
    # column_name = await session.execute(text("select * from users"))
    column_name = await session.execute(select(Base.metadata.tables['users']))
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
    data = {
        'name': 'John',
        'age': '30',
        'pets': 'cats',
        'address': {
            'city': 'New York',
            'street': 'Broadway',
            'building': 123,
            'fact': None
        }
    }

    await create_tables()
    # await create_user(data)
    await add_user(str_users)
    # await read_db()


if __name__ == '__main__':
    asyncio.run(main())
