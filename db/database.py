import sqlite3

class DB:
    def __init__(self) -> None:
        self.db = sqlite3.connect('./db/data.db',check_same_thread=False)
        self.cursor = self.db.cursor()

    def _get_admin(self) -> list:
        self.cursor.execute("SELECT * FROM 'admin'")
        row = self.cursor.fetchone()
        return row[1]

    def _get_managers(self) -> list:
        self.cursor.execute("SELECT * FROM managers")
        row = self.cursor.fetchall()
        return [x[1] for x in row]

    def _add_manager(self, chat_id: int) -> None:
        self.cursor.execute("INSERT INTO managers (chat_id) VALUES (?)", (chat_id,))
        self.db.commit()

    def _delete_manager(self, chat_id: int):
        self.cursor.execute("DELETE FROM managers WHERE chat_id = ?", (chat_id, ))

    def _get_users(self):
        self.cursor.execute("SELECT * FROM 'users'")
        row = self.cursor.fetchall()
        return [x[1] for x in row]

    def _add_user(self, chat_id: int) -> None:
        self.cursor.execute("INSERT INTO users (chat_id) VALUES (?)", (chat_id,))
        self.db.commit()

    