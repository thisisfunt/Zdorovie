import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../main.db")

class Users:
    def InsertNewUser(self, user_id_in_yandex : str, name : str, gender : str, age : int) -> None:
        with sqlite3.connect(db_path) as con:
            _cur = con.cursor()
            _cur.execute(
            f"""
                INSERT INTO Users (user_id_in_yandex, name, gender, age) VALUES(
                    "{user_id_in_yandex}", "{name}", "{gender}", {age}
                )
            """)
            con.commit()

    def CheckUserExist(self, user_id_in_yandex : str) -> bool:
        with sqlite3.connect(db_path) as con:
            _cur = con.cursor()
            _cur.execute(f"""
                SELECT * FROM Users WHERE user_id_in_yandex = "{user_id_in_yandex}"
            """)
            result = _cur.fetchall()
            return len(result) > 0

    def GetUserData(self, user_id_in_yandex : str):
        with sqlite3.connect(db_path) as con:
            _cur = con.cursor()
            _cur.execute(f"""
                SELECT * FROM Users WHERE user_id_in_yandex = "{user_id_in_yandex}"
            """)
            result = _cur.fetchall()[0]
            return result


class Pulse:
    def InsertNewPulseData(self,user_id : str, pulse_count : int, date : str):
        with sqlite3.connect(db_path) as con:
            _cur = con.cursor()
            _cur.execute(f"""
                INSERT INTO Pulse (user_id, count, date) VALUES (
                    "{user_id}", "{pulse_count}", "{date}"
                )
            """)
            con.commit()

    def GetLastPulse(self, user_id : int):
        with sqlite3.connect(db_path) as con:
            _cur = con.cursor()
            _cur.execute(f"""
                SELECT date, count FROM Pulse WHERE user_id = {user_id} ORDER BY id DESC LIMIT 5
            """)
            result = _cur.fetchall()
            return result