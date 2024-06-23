import sqlite3

class DB:

    def __init__(self) -> None:
        self.db = sqlite3.connect('./db/data.db',check_same_thread=False)
        self.cursor = self.db.cursor()

    def _get_managers(self) -> list:
        self.cursor.execute("SELECT * FROM managers")
        row = self.cursor.fetchall()
        return [x for x in row]


    def _get_users(self):
        self.cursor.execute("SELECT * FROM 'users'")
        row = self.cursor.fetchall()
        return [x for x in row]

    def _add_user(self, chat_id: int, username: str) -> None:
        self.cursor.execute("INSERT INTO users (chat_id, username) VALUES (?, ?)", (chat_id, username))
        self.db.commit()

    def _search_user(self, username: str):
        users = self._get_users()
        for user in users:
            if user[2] == username:
                return user[0]
            else:
                return "Нет такого пользователя!"

    def _ban_user(self, id: int) -> None:
        if id in [i[0] for i in self._get_users()]:
            users = self._get_users()
            self.cursor.execute("INSERT INTO banned (chat_id, username) VALUES (?, ?)", (users[id-1][1], users[id-1][2]))
            self.cursor.execute("REMOVE FROM users WHERE id = (?)", (id))
            self.db.commit()

    def _get_banned_users(self) -> list:
        self.cursor.execute("SELECT * FROM 'banned'")
        row = self.cursor.fetchall()
        return [x[1] for x in row]

    