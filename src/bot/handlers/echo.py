from aiogram import types
from loader import dp, session_maker
from src.db.methods import is_reg, insert_message
from src.db.message import Message
from src.db.user import User
from src.bot.text.bot_commands import locale_text as t


@dp.message_handler()
async def echo(message: types.Message) -> None:
    cur_user = User(
        user_id=message.from_user.id,
        name=message.from_user.full_name
    )
    if await is_reg(async_session=session_maker, user=cur_user):
        mess = Message(
            message_id=message.message_id,
            text=message.text,
            user_id=message.from_user.id
        )
        await insert_message(async_session=session_maker, message=mess)
        await message.answer(text=t['save_mess'])
    else:
        await message.answer(text=t['no_registry'])
