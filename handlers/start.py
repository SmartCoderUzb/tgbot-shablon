from aiogram.types import Message
from loader import dp

@dp.message_handler(commands=['start'])
async def start(message:Message):
    await message.answer("Salom")