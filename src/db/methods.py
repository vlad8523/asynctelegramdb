from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from .user import User
from .message import Message


async def insert_user(async_session: async_sessionmaker[AsyncSession], user: User) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add(user)


async def insert_message(async_session: async_sessionmaker[AsyncSession], message: Message) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add(message)


async def is_reg(async_session: async_sessionmaker[AsyncSession], user: User) -> bool:
    print('start_check')
    async with async_session() as session:
        stmt = select(User).where(User.user_id == user.user_id)
        result = await session.execute(stmt)
    print('end_check')
    return True if result.first() is not None else False
