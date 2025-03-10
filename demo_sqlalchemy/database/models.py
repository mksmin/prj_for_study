import asyncio

from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

PostSQL_host = ...
post_host_token = PostSQL_host
engine = create_async_engine(url=post_host_token,
                             echo=True)
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Usert(Base):
    __tablename__ = 'test_users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)

    author = relationship('Authort', back_populates='user', uselist=False)

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, username={self.username})'

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, username={self.username})'


class Authort(Base):
    __tablename__ = 'test_authors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('test_users.id'), nullable=False, unique=True)

    user = relationship('Usert', back_populates='author')

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, username={self.name}, user_id={self.user_id})'


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
