from src.bot.text.bot_commands import locale_text as t
from loader import dp
from aiogram import types


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(text=t['help'])
