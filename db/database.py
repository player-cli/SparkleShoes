import sqlite3

class DB:
    def __init__(self) -> None:
        self.db = sqlite3.connect('./db/data.db',check_same_thread=False)
        self.cursor = self.db.cursor()

    def _get_admins(self) -> list:
        self.cursor.execute("SELECT * FROM admins")
        row = self.cursor.fetchall()
        return [x for x in row]

    def _get_managers(self) -> list:
        self.cursor.execute("SELECT * FROM managers")
        row = self.cursor.fetchall()
        return [x for x in row]

    def _add_manager(self, name: str, chat_id: int) -> None:
        self.cursor.execute("INSERT INTO 'managers' (name, chat_id) VALUES (?, ?)", (name, chat_id,))
        self.db.commit()

    def _delete_manager(self, chat_id: int):
        self.cursor.execute("DELETE FROM managers WHERE chat_id = ?", (chat_id, ))

    def _get_users(self):
        self.cursor.execute("SELECT * FROM 'users'")
        row = self.cursor.fetchall()
        return [res for res in row]

    def _add_user(self, name: str, chat_id: int) -> None:
        self.cursor.execute("INSERT INTO 'users' (name, chat_id) VALUES (?, ?)", (name, chat_id,))
        self.db.commit()

    def _ban_user(self, chat_id: int) -> None:
        users = self._get_users()
        for user in users:
            if user[2] == chat_id:
                self.cursor.execute("DELETE FROM users WHERE chat_id = ?", (chat_id, ))
                self.cursor.execute("INSERT INTO banned (chat_id) VALUES (?)", (chat_id,))