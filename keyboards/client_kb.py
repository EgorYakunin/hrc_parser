from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reg_bt = KeyboardButton('/Авторизация')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(reg_bt)


set_keys_bt = KeyboardButton('/Задать_ключи')
change_keys_bt = KeyboardButton('/Изменить_ключи')
current_keys_bt = KeyboardButton('/Текущие_ключи')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True)
kb_user.add(set_keys_bt).add(change_keys_bt).add(current_keys_bt)
