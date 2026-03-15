import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


bot = Bot(token="8729617934:AAHw2RkCeAk01QnQrTb_O_CzH_bwxdLBwbw")
dp = Dispatcher()

facts = [
    "Осьминоги имеют три сердца.",
    "Мёд не портится тысячи лет.",
    "На Венере день длиннее года.",
    "У улиток около 25 000 зубов.",
    "Банан — это ягода, а клубника — нет.",
]


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот. Напиши /random_fact чтобы узнать случайный факт.")


@dp.message(Command("random_fact"))
async def random_fact(message: Message):
    await message.answer(random.choice(facts))


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())