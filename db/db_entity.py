from . import mysql


class DBEntity:
    def __init__(self):
        self.cursor = mysql.get_db().cursor()

    def close(self):
        return self.cursor.close
