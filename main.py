# author : player-cli
# MIT license
# @2024

import telebot
import testapi

from db import database

from handlers import client_h
from handlers import admin_h

from other import keyboard
from other import botsay

from art import tprint

# -- Init zone -- #

bot = telebot.TeleBot(testapi.api)
client = client_h.Client(bot)
admin = admin_h.Admin(bot)
db = database.DB()

# -- Main zone -- #

@bot.message_handler(commands=['start'])
def start_command(message):
    admins = db._get_admins()
    managers = db._get_managers()
    users = db._get_users()
    if message.chat.id not in admins and message.chat.id not in managers:

        if message.chat.id in users:
            bot.send_message(message.chat.id, text=botsay.start + botsay.add, reply_markup=keyboard.startup_keyboard)
        else:
            db._add_user(message.chat.username, message.chat.id)
            bot.send_message(message.chat.id, text=botsay.start + botsay.add, reply_markup=keyboard.startup_keyboard)

    if message.chat.id not in admins and message.chat.id in managers and message.chat.id not in users:
        bot.send_message(message.chat.id, text="Вы являетесь менеджером!", reply_markup=keyboard.manager_startup_keyboard)
    else:
        bot.send_message(message.chat.id, text="Вы являетесь администратором!", reply_markup=keyboard.admin_startup_keyboard)
    

# -- Client zone -- #

@bot.message_handler(content_types=['text'])
def client_handlers(message):
    m = message.text
    match(m):
        case "Заказать самостоятельно":
            pass
        case "Заказать с помощью менеджера":
            pass
        case "Химчистка":
            pass
        case "Задать вопрос":
            pass

        case _:
            bot.send_message(message.chat.id, text = "Нет такой команды")

# -- Admin zone -- #

@bot.message_handler(content_types=['text'])
def admin_handlers(message):
    pass

# -- Startup zone -- #

def main() -> int:
    tprint("PLAYER BOT")
    bot.polling()
    return 1

if __name__ == "__main__":
    main()