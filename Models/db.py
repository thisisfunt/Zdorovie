import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../main.db")


class Users:
    def __init__(self):
        self._con = sqlite3.connect(db_path)
        self._cur = self._con.cursor()

    def InsertNewUser(self, user_id_in_yandex : str, name : str, gender : str, age : int) -> None:
        with sqlite3.connect('/main.db'):
            self._cur.execute(
            f"""
                INSERT INTO Users (user_id_in_yandex, name, gender, age) VALUES(
                    "{user_id_in_yandex}", "{name}", "{gender}", {age}
                )
            """)
            self._con.commit()

    def CheckUserExist(self, user_id_in_yandex : str) -> bool:
        self._cur.execute(f"""
            SELECT * FROM Users WHERE user_id_in_yandex = "{user_id_in_yandex}"
        """)
        result = self._cur.fetchall()
        return len(result) > 0

    def __del__(self):
        self._con.close()
