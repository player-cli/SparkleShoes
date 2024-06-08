from telebot import types

startup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Что вас интересует?", one_time_keyboard=True)
startup_keyboard.row(types.KeyboardButton(text='Заказать самому'))
startup_keyboard.row(types.KeyboardButton(text='Заказать вместе с менеджером'))
startup_keyboard.row(types.KeyboardButton(text='Химчистка'))
startup_keyboard.row(types.KeyboardButton(text='Задать вопрос'))
startup_keyboard.row(types.KeyboardButton(text='FAQ'))

self_order_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
self_order_keyboard.row(types.KeyboardButton('Главное меню'))

manager_order_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
manager_order_keyboard.row(types.KeyboardButton('Вызов менеджера'))
manager_order_keyboard.row(types.KeyboardButton('Главное меню'))

shoes_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
shoes_keyboard.row(types.KeyboardButton('Написать по поводу химчистки'))
shoes_keyboard.row(types.KeyboardButton('Главное меню'))

admin_startup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin_startup_keyboard.row(types.KeyboardButton('Управление менеджерами'))
admin_startup_keyboard.row(types.KeyboardButton('Управление пользователями'))

admin_managers_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin_managers_keyboard.row(types.KeyboardButton('Добавить менеджера'))
admin_managers_keyboard.row(types.KeyboardButton('Удалить менеджера'))
admin_managers_keyboard.row(types.KeyboardButton('Админ меню'))

admin_users_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin_users_keyboard.row(types.KeyboardButton('Забанить пользователя'))
admin_users_keyboard.row(types.KeyboardButton('Админ меню'))

manager_startup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
manager_startup_keyboard.row(types.KeyboardButton('Управление пользователями'))

manager_users_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
manager_users_keyboard.row(types.KeyboardButton('Забанить пользователя'))
manager_users_keyboard.row(types.KeyboardButton('Меню менеджера'))
