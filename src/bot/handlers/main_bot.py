from aiogram import types
from src.bot.text import locale_text as text
from loader import dp, session_maker
from src.db.methods import insert_user, is_reg
from src.db.user import User


users = set()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=text['start'])
    await message.delete()


@dp.message_handler(commands=['registry'])
async def reg(message: types.Message):
    cur_user = User(user_id=message.from_user.id,
                name=message.from_user.full_name)

    if await is_reg(async_session=session_maker,user=cur_user):
        await message.answer(text=text['is_registry'])
    else:
        users.add(message.from_user.id)
        await insert_user(async_session=session_maker, user=cur_user)
        await message.answer(text=text['registry'])


@dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.id in users:
        await message.answer(text=message.text)
    else:
        await message.answer(text=text['no_registry'])
    print(f"message from {message.from_user.id} and text = {message.text}")
