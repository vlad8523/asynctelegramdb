import asyncio

from aiogram import Bot, Dispatcher, types
from sqlalchemy.ext.asyncio import AsyncEngine
from src.db.engine import create_engine,get_session_maker,async_sessionmaker
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

import data

bot = Bot(token=data.TOKEN_API)
dp = Dispatcher(bot)
loop = asyncio.get_event_loop()
engine: AsyncEngine = create_engine(url = data.DATABASE_URL)
session_maker: async_sessionmaker = get_session_maker(engine)
