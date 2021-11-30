from entities.tip import Tip
from database_connection import get_database_connection


class TipRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def create_tip(self, tip):
        sql = "INSERT INTO Tips (name, url) VALUES (?, ?)"
        self._connection.execute(sql, (tip.name, tip.url))
        self._connection.commit()


    def find_all(self):
        tips = []
        sql = "SELECT * FROM Tips"
        result = self._connection.execute(sql)
        for row in result:
            tips.append(Tip(row["name"],row["url"]))
        return tips

    def clear(self):
        sql = "DELETE FROM Tips"

tip_repository = TipRepository()