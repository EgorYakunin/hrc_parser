from aiogram import types, Dispatcher
from create_bot import bot
from data_base import sq
from create_bot import chat_id


base = sq.connect('keys_base.db')
cur = base.cursor()


async def search_keys(message: types.Message):
    for ret in cur.execute('SELECT * FROM search_keys').fetchall():
        for i in str(ret[1]).split(','):
            if i.strip() in message.text.lower():
                await bot.send_message(chat_id, '@' + message.from_user.username + ' ' + message.text)


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(search_keys)
