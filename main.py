from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from handlers import client, other


async def on_startup(_):
    print('Status:online')
    sqlite_db.sql_start()


client.register_client_handlers(dp)
other.register_other_handlers(dp)


executor.start_polling(dp, on_startup=on_startup)
