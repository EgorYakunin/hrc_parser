import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('keys_base.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS search_keys (id TEXT PRIMARY KEY, keys TEXT)')
    base.commit()


async def sql_add_command(user_id, key, message):
    if cur.execute('SELECT keys FROM search_keys WHERE id == ?', (str(user_id),)).fetchone() is None:
        cur.execute('INSERT INTO search_keys VALUES (?, ?)', (user_id, key))
        base.commit()
    else:
        await bot.send_message(message.from_user.id, 'Ключи уже занесены')


async def my_keys(user_id, message):
    try:
        text = ''.join(cur.execute('SELECT keys FROM search_keys WHERE id == ?', (str(user_id),)).fetchone())
        await bot.send_message(message.from_user.id, text)
    except:
        await bot.send_message(message.from_user.id, 'Сначала внеси ключи')


async def change_keys(id, keys):
    cur.execute('UPDATE search_keys SET keys == ? WHERE id == ?', (str(keys), id))
    base.commit()
