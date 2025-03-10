from functools import wraps
from demo_sqlalchemy.database.models import async_session, Usert, Authort
from sqlalchemy import select
from sqlalchemy.orm import joinedload


def connection(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            return await function(session, *args, **kwargs)

    return wrapper


@connection
async def create_user(session, username):
    user = Usert(
        username=username
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@connection
async def create_author(session, name: str, user: Usert):
    author = Authort(
        name=name,
        user_id=user.id
    )

    session.add(author)
    await session.commit()
    await session.refresh(author)
    return author


@connection
async def fetch_users_with_authors(session: async_session) -> list[Usert]:
    users = await session.scalars(select(Usert).options(joinedload(Usert.author)))
    result = users.unique()
    # for user in users:
    #     print(f'user: {user}')
    # print(f'{[userd for userd in users]}')
    print(result)
    for user in result:
        print(f'user: {user}, type: {type(user)}')
        print(f'author: {user.author}, type: {type(user.author)}')

        # if len(user.author) > 0:
        #     print(f' author: {user.author[0].name}, type: {type(user.author[0])}')
