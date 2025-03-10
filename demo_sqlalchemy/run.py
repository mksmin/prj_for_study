import asyncio

from demo_sqlalchemy.database.models import create_db
import demo_sqlalchemy.database.request as rq


async def main():
    # await create_db()

    # sam = await rq.create_user(
    #     username='Maxxname'
    # )
    # #
    # print(f'{sam = }, type(sam) = {type(sam)}')
    # author_sam = await rq.create_author(
    #     name='Max M.>',
    #     user=sam
    # )
    #
    # print(f'{author_sam = }')

    await rq.fetch_users_with_authors()



if __name__ == '__main__':
    asyncio.run(main())
