from aiogram import types
from loader import dp
from src.bot.text.bot_commands import locale_text as t


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=t['start'])
    await message.delete()
