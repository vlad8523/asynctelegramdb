from typing import Union

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine


def create_engine(url: Union[URL, str]) -> AsyncEngine:
    """

    :param url:
    :return:
    """
    return create_async_engine(url=url,
                               echo=True,
                               pool_pre_ping=True)


def get_session_maker(engine: AsyncEngine) -> async_sessionmaker:
    """

    :param engine:
    :return:
    """
    return async_sessionmaker(engine, class_=AsyncSession)
