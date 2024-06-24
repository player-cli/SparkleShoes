from other import keyboard

from db import database

class Manager:
    
    def __init__(self, bot):
        self.bot = bot
        self.DB = database.DB()

    def _ban_user(self, message):
        self.bot.send_message(message.chat.id, text = "Введите username пользователя", reply_markup = None)
        self.bot.register_next_step_handler(message, self._ban_user_func)

    def _ban_user_func(self, message):
        username = message.text
        self.DB._ban_user(username)
        self.bot.send_message(message.chat.id, text = f"Пользователь {username} забанен")
