import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ParseMode
import requests
import json


async def gpt_mess(text):
    prompt = {
                "modelUri": "gpt://b1g6ciet5rgs1gajvnjc/yandexgpt-lite",
                "completionOptions": {
                    "stream": False,
                    "temperature": 0.6,
                    "maxTokens": "2000"
                },
                "messages": [
                    {
                        "role": "system",
                        "text": text
                    },
                ]
            }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNw2SfjLFhTX0EzKsTHaBQSLPmtobmlha8814s"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.text
    y = json.loads(result)

    retText = y['result']['alternatives'][0]['message']['text']
    
    return retText



#Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

#Объект бота
bot = Bot(token="6841478496:AAF6TfBkYysVzfe0DRgqVzQ6kffUfpq6nIM")

#Диспетчер
dp = Dispatcher()


#/////////////////////////////////////////////////////////////////////////

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('''Доброго времени суток,👋 
здесь вы можете найти БЕСПЛАТНУЮ моральную помощь!😁 Я бот, 🤖 меня зовут  IHelpYouNow и сейчас вы можете записаться на приём. Я с радостью помогу вам!😄 Всё абсолютно бесплатно, но стоит чучуть подождать, надеюсь вас это незатруднит!😉
✍Что бы записаться на приём, напишите: /rec
💬Что бы получить больше информации, напишите: /help''')

@dp.message(F.text)
async def pr(message: Message):
    a = await gpt_mess(message.text)
    await message.answer(a)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())