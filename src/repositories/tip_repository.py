from entities.tip import Tip
from database_connection import get_database_connection


class TipRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def create_tip(self, tip):
        sql = "INSERT INTO Tips (name, url) VALUES (?, ?)"
        self._connection.execute(sql, (tip.name, tip.url))
        self._connection.commit()

    def edit_tip(self, id, tip):
        sql = "UPDATE Tips SET name = ?, url = ? WHERE id == ?"
        self._connection.execute(sql, (tip.name, tip.url, id))
        self._connection.commit()

    def find_tip(self, id):
        sql = "SELECT * FROM Tips WHERE id = ?"
        res = self._connection.execute(sql, (id,)).fetchone()
        return res

    def remove_tip(self, id):
        sql = "DELETE FROM Tips WHERE id = ?"
        self._connection.execute(sql, (id,))
        self._connection.commit()
        
    def find_all(self):
        tips = []
        sql = "SELECT * FROM Tips"
        result = self._connection.execute(sql)
        for row in result:
            tips.append((row["id"] ,Tip(row["name"],row["url"])))
        return tips

    def clear(self):
        sql = "DELETE FROM Tips"
        self._connection.execute(sql)
        self._connection.commit()

tip_repository = TipRepository()