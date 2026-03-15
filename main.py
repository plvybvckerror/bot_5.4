import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import FSInputFile, Message

import random
bot = Bot(token="8729617934:AAHw2RkCeAk01QnQrTb_O_CzH_bwxdLBwbw")
dp = Dispatcher()



@dp.message('/add_meme')
async def add_meme (message: Message):
    os.makedirs("img", exist_ok=True)
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_memes = f"img/{file_id}.jpg"
    await bot.download_file(file.file_memes, file_memes)
    await message.answer("Мем сохранен")

@dp.message('/meme')
async def meme (message: Message):
    meme_photo=random.choice(os.listdir('img'))
    photo=FSInputFile(f'img/{meme_photo}')
    await message.answer_photo(photo)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())