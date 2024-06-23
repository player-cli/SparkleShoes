# author : player-cli
# MIT license
# @2024

# webhook part of imports

import fastapi
import uvicorn
import logging

# telegram imports

import telebot
import toml

from db import database

from handlers import client_h
from handlers import manager_h

from other import keyboard
from other import botsay

from art import tprint

# -- Init zone -- #


API_TOKEN = 'TOKEN'

WEBHOOK_HOST = '<ip/domain>'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

app = fastapi.FastAPI(docs=None, redoc_url=None)
bot = telebot.TeleBot(API_TOKEN)
DB = database.DB()
CL = client_h.Client(bot, DB._get_managers())
MNG = manager_h.Manager(bot)

# -- Main zone -- #


@app.post(f'/{API_TOKEN}/')
def process_webhook(update: dict):
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return

@bot.message_handler(commands=['start'])
def start_command(message):
    managers = DB._get_managers()
    users = DB._get_users()
    BAN = DB._get_banned_users()
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

        else:
            bot.send_message(message.chat.id, text="Вы являетесь менеджером!", reply_markup=keyboard.manager_startup_keyboard)
    else:
        bot.send_message(message.chat.id, "Вы не можете писать в этот бот, вы забанены!")
    
@bot.message_handler(commands=['faq'])
def faq_command(message):
    bot.send_message(message.chat.id, botsay.faq)

# -- Handlers zone -- #

@bot.message_handler(content_types=['text'])
def client_handlers(message):
    m = message.text
    BAN = DB._get_banned_users()
    if message.chat.id in BAN:
        bot.send_message(message.chat.id, text = "Вы забанены! ")
    if message.chat.id not in DB._get_managers() and message.chat.id not in BAN:
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
    
    else:
        match(m):
            case "Забанить пользователя":
                MNG._ban_user(message)        


# -- Startup zone -- #

# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

# Set webhook
bot.set_webhook(
    url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
    certificate=open(WEBHOOK_SSL_CERT, 'r')
)

if __name__ == "__main__":
    uvicorn.run(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    ssl_certfile=WEBHOOK_SSL_CERT,
    ssl_keyfile=WEBHOOK_SSL_PRIV
    )