from config import TELEGRAM_TOKEN
from weather import get_weather
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, я бот погоды! Напиши мне название города')


@dp.message_handler(content_types=['text'])
async def get_city_weather(message: types.Message):
    response = get_weather(message.text)
    await message.reply(response)


if __name__ == '__main__':
    executor.start_polling(dp)
