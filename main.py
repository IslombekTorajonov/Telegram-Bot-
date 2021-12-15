from aiogram import Dispatcher, Bot
from aiogram.dispatcher.filters import Command
from aiogram.types.message import Message
from config import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot)
@dp.message_handler(Command("start"))
@dp.message_handler(Command("help"))

@dp.message_handler(Command("kanal"))

@dp.message_handler()
async def lalala(message: Message):
    if message.text == "/start":
       await bot.send_message(chat_id=message.from_user.id, text="Salom hurmatli foydalanuvchi bizning botimizga xush kelibsiz iltimos savolingizni yollang biz sizga tez orada javob beramiz")

    if message.text == "/kanal":
       await bot.send_message(chat_id=message.from_user.id, text="Hurmatli foydalanuvchi bizning rasmiy kanal bot biogrammasida korsatib qoyilgan bemalol kirib ozingiz uchun kerakli malumotga ega bolishingiz mumkin")

    if message.text == "/help":
        await bot.send_message(chat_id=message.from_user.id,text="Hurmatli foydalanuvchi biz sizga qanday yordam korsata olamiz bizga savol yoki takliflaringizni yollang bit sizga tez orada javob beramiz")


if __name__=="__main__":
    from aiogram import executor
    executor.start_polling(dp)
