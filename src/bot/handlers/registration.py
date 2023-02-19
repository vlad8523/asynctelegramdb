from src.db.user import User
from src.db.methods import insert_user, is_reg
from loader import dp, session_maker
from src.bot.text.bot_commands import locale_text as t
from aiogram import types


@dp.message_handler(commands=['registry'])
async def reg(message: types.Message):
    cur_user = User(user_id=message.from_user.id,
                    name=message.from_user.full_name)
    if await is_reg(async_session=session_maker, user=cur_user):

        await message.answer(text=t['is_registry'])
    else:
        await insert_user(async_session=session_maker, user=cur_user)
        await message.answer(text=t['registry'])