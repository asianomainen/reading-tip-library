
from entities.tip import Tip
from database_connection import get_database_connection


class TipRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def create_tip(self, tip):
        sql = "INSERT INTO Tips (name, url, read) VALUES (?, ?, ?)"
        self._connection.execute(sql, (tip.name, tip.url, 0))
        self._connection.commit()

    def edit_tip(self, tip_id, tip):
        sql = "UPDATE Tips SET name = ?, url = ? WHERE id == ?"
        self._connection.execute(sql, (tip.name, tip.url, tip_id))
        self._connection.commit()

    def find_tip(self, tip_id):
        sql = "SELECT * FROM Tips WHERE id = ?"
        res = self._connection.execute(sql, (tip_id,)).fetchone()
        if res is None:
            return None
        return (res["id"], Tip(res["name"], res["url"], res["read"]))

    def mark_as_read(self, tip_id, tip):
        sql = "UPDATE Tips SET read = ? WHERE id == ?"
        self._connection.execute(sql, (tip.read, tip_id,))
        self._connection.commit()

    def remove_tip(self, tip_id):
        sql = "DELETE FROM Tips WHERE id = ?"
        self._connection.execute(sql, (tip_id,))
        self._connection.commit()

    def find_all(self, filters="all"):
        tips = []
        if filters == "all":
            sql = "SELECT * FROM Tips"
        elif filters == "read":
            sql = "SELECT * FROM Tips WHERE read == 1"
        else:
            sql = "SELECT * FROM Tips WHERE read == 0"
        result = self._connection.execute(sql)
        for row in result:
            tips.append((row["id"], Tip(row["name"], row["url"], row["read"])))
        return tips

    def clear(self):
        sql = "DELETE FROM Tips"
        self._connection.execute(sql)
        self._connection.commit()

tip_repository = TipRepository()
