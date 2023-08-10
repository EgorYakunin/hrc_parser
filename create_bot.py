from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(token="5390158411:AAFop1H1ld_Pfteax2C28LOeWUyAf8tsPRc")
dp = Dispatcher(bot, storage=storage)
ID = ['629150228', '736301626']
chat_id = '-1001927201631'
