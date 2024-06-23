from other import keyboard

from db import database

class Manager:
    
    def __init__(self, bot):
        self.bot = bot
        DB = database.DB()

    def _search_user(self, message):
        self.bot.send_message(message.chat.id, text = "Введите username пользователя", reply_markup = None)
        self.bot.register_next_step_handler(message, self._search_user_func)

    def _ban_user(self, message):
        user_id = int(message.text)
        self.DB._ban_user(user_id)
        self.bot.send_message(message.chat.id, text = f"Пользователь {user_id} забанен")

    def _search_user_func(self, message):
        username = message.text
        user_id = self.DB._search_user(username)
        self.bot.send_message(message.chat.id, text = f"Id пользователя {user_id}")