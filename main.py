import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot, storage=MemoryStorage())
unli = ["A", "E", "U", "I", "O", "a", "e", "u", "i", 'o']


@dp.message_handler(commands='start')
async def start_handler(msg: types.Message):
    await msg.answer(text="Botga habar yuborganingizda u habarda 5 ta unli bo`lsa habar o`chiriladi")


@dp.message_handler()
async def delete_message(msg: types.Message):
    s = 0
    for i in msg.text:
        if i in unli:
            s += 1
    if s > 4:
        await msg.delete()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)