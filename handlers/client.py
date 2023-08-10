from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client, kb_user
from create_bot import ID
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base import sqlite_db


class FSMAdmin(StatesGroup):
    keys = State()
    new_keys = State()


async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать!\nДля продолжения пройдите авторизацию',
                           reply_markup=kb_client)


async def authorization(message: types.Message):
    if str(message.from_user.id) in ID:
        await bot.send_message(message.from_user.id, 'Авторизация прошла успешно', reply_markup=kb_user)
    else:
        await bot.send_message(message.from_user.id, 'Доступ запрещен')
        await bot.send_message(ID[0], f'{message.from_user.username} '
                                      f'пытается воспользоваться ботом\nid пользователя:{message.from_user.id}')


async def cm_start(message: types.Message):
    if str(message.from_user.id) in ID:
        await FSMAdmin.keys.set()
        await bot.send_message(message.from_user.id, 'Введите ключи через запятую')


async def load_keys(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in ID:
        await sqlite_db.sql_add_command(message.from_user.id, message.text.lower(), message)
        await state.finish()


async def show_keys(message: types.Message):
    if str(message.from_user.id) in ID:
        await sqlite_db.my_keys(message.from_user.id, message)


async def ed_start(message: types.Message):
    if str(message.from_user.id) in ID:
        await FSMAdmin.new_keys.set()
        await bot.send_message(message.from_user.id, 'Введите ключи через запятую')


async def edit_keys(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in ID:
        await sqlite_db.change_keys(message.from_user.id, message.text.lower())
        await bot.send_message(message.from_user.id, 'Ключи изменены')
        await state.finish()


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(authorization, commands='Авторизация')
    dp.register_message_handler(cm_start, commands='Задать_ключи', state=None)
    dp.register_message_handler(load_keys, state=FSMAdmin.keys)
    dp.register_message_handler(show_keys, commands='Текущие_ключи')
    dp.register_message_handler(ed_start, commands='Изменить_ключи', state=None)
    dp.register_message_handler(edit_keys, state=FSMAdmin.new_keys)
