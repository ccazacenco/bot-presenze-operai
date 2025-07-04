
import sqlite3
from contextlib import closing

class WorkerDB:
    def __init__(self):
        self.conn = sqlite3.connect("data/workers.db")
        self._init_db()

    def _init_db(self):
        with closing(self.conn.cursor()) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS workers (
                    user_id INTEGER PRIMARY KEY,
                    full_name TEXT,
                    pin TEXT,
                    drive_folder_id TEXT
                )""")
            self.conn.commit()

    def get_worker(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM workers WHERE user_id=?", (user_id,))
        return cursor.fetchone()
