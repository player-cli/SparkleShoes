from other import botsay
from other import keyboard

import random



class Client:
    
    def __init__(self, bot, managers: list):
        self.bot = bot
        self.managers = managers

    def _self_order(self, message):
        self.bot.send_message(message.chat.id, botsay.order, reply_markup = None)
        self.bot.register_next_step_handler(message, self.__forward_to_manager)

    def _manager_order(self, message):
        self.bot.send_message(message.chat.id, botsay.managerorder, reply_markup = keyboard.startup_keyboard)
        self.bot.send_message(random.choice(self.managers), text = f"Заявка по китаю от @{message.from_user.username}")

    def _shoes_clean(self, message):
        self.bot.send_message(message.chat.id, botsay.shoesclean, reply_markup = keyboard.startup_keyboard)
        self.bot.send_message(random.choice(self.managers), text = f"Заявка по кроссовкам от @{message.from_user.username}")

    def _qa(self, message):
        self.bot.send_message(message.chat.id, botsay.help, reply_markup = keyboard.startup_keyboard)

    def __forward_to_manager(self, message):
        self.bot.forward_message(random.choice(self.managers), message.chat.id, message.message_id)
        self.bot.send_message(message.chat.id, "Отправили заявку на покупку, скоро вам напишет менеджер для подтверждения! :3", reply_markup = keyboard.startup_keyboard)