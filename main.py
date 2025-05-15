
import asyncio
from aiogram import Bot, Dispatcher
from handlers import router

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
