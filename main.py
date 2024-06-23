# author : player-cli
# MIT license
# @2024

import telebot
import toml

from db import database

from handlers import client_h
from handlers import manager_h

from other import keyboard
from other import botsay

from art import tprint

# -- Init zone -- #

# config to tests
cfg = toml.load("./config.toml")

bot = telebot.TeleBot(cfg['api'])
DB = database.DB()
CL = client_h.Client(bot, DB._get_managers())
MNG = manager_h.Manager(bot)

BAN = DB._get_banned_users()

# -- Main zone -- #

@bot.message_handler(commands=['start'])
def start_command(message):
    managers = DB._get_managers()
    users = DB._get_users()
    if message.chat.id not in BAN:
        if message.chat.id not in managers:

            if not message.from_user.username:
                bot.send_message(message.chat.id, "Для работы бота вам нужно установить user id! ")
            else:
                if message.chat.id in users:
                    bot.send_message(message.chat.id, text=botsay.start, reply_markup=keyboard.startup_keyboard)
                else:
                    DB._add_user(message.chat.id, "@" + message.from_user.username)
                    bot.send_message(message.chat.id, text=botsay.start, reply_markup=keyboard.startup_keyboard)

        if message.chat.id in [i[1] for i in managers]:
            bot.send_message(message.chat.id, text="Вы являетесь менеджером!", reply_markup=keyboard.manager_startup_keyboard)
    else:
        bot.send_message(message.chat.id, "Вы не можете писать в этот бот, вы забанены!")
    
@bot.message_handler(commands=['faq'])
def faq_command(message):
    bot.send_message(message.chat.id, botsay.faq)

# -- Client zone -- #

@bot.message_handler(content_types=['text'])
def client_handlers(message):
    m = message.text
    match(m):
        case "Заказать самому":
            CL._self_order(message)
        case "Заказать вместе с менеджером":
            CL._manager_order(message)
        case "Химчистка":
            CL._shoes_clean(message)
        case "Задать вопрос":
            CL._qa(message)
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