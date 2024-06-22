from telebot import types

startup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Что вас интересует?", one_time_keyboard=True)
startup_keyboard.row(types.KeyboardButton(text='Заказать самому'))
startup_keyboard.row(types.KeyboardButton(text='Заказать вместе с менеджером'))
startup_keyboard.row(types.KeyboardButton(text='Химчистка'))
startup_keyboard.row(types.KeyboardButton(text='Задать вопрос'))

admin_startup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin_startup_keyboard.row(types.KeyboardButton('Управление менеджерами'))
admin_startup_keyboard.row(types.KeyboardButton('Статистика'))
