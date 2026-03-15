
import asyncio
from aiogram import Bot, Dispatcher


bot = Bot(token="8729617934:AAHw2RkCeAk01QnQrTb_O_CzH_bwxdLBwbw")
dp = Dispatcher()





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())