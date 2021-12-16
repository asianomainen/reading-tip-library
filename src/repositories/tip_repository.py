
from entities.tip import Tip
from database_connection import get_database_connection


class TipRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def create_tag(self, name):
        sql = "INSERT INTO Tags (name) VALUES (?)"
        self._connection.execute(sql, (name,))
        self._connection.commit()

    def assign_tag(self, tipid, tagid):
        sql = "INSERT INTO Tiptags (tipid, tagid) VALUES (?, ?)"
        self._connection.execute(sql, (tipid, tagid))
        self._connection.commit()

    def get_tags(self, tipid):
        sql = "SELECT T.name FROM Tags T, Tiptags TT WHERE T.id = TT.tagid AND TT.tipid = ?"
        tagsdata = self._connection.execute(sql, (tipid,)).fetchall()
        tags = [x[0] for x in tagsdata]
        return tags

    def tag_exists(self, name):
        sql = "SELECT * FROM Tags WHERE name = ?"
        res = self._connection.execute(sql, (name,)).fetchone()
        if res is None:
            return None
        return res["id"]

    def create_tip(self, tip):
        sql = "INSERT INTO Tips (name, url, read, favourite) VALUES (?, ?, ?, ?)"
        self._connection.execute(sql, (tip.name, tip.url, 0, 0))
        self._connection.commit()
        tip_id = self._connection.execute("SELECT last_insert_rowid()").fetchone()[0]
        for tag in tip.tags:
            tag_id = self.tag_exists(tag)
            if tag_id is None:
                self.create_tag(tag)
                tag_id = self._connection.execute("SELECT last_insert_rowid()").fetchone()[0]
            self.assign_tag(tip_id, tag_id)
        self._connection.commit()

    def edit_tip(self, tip_id, tip):
        sql = "UPDATE Tips SET name = ?, url = ? WHERE id == ?"
        self._connection.execute(sql, (tip.name, tip.url, tip_id))
        self._connection.commit()

    def find_tip(self, tip_id):
        sql = "SELECT * FROM Tips WHERE id = ?"
        res = self._connection.execute(sql, (tip_id,)).fetchone()
        tags = self.get_tags(tip_id)
        if res is None:
            return None
        return (res["id"], Tip(res["name"], res["url"], tags, res["read"], res["favourite"]))

    def mark_as_read(self, tip_id, tip):
        sql = "UPDATE Tips SET read = ? WHERE id == ?"
        self._connection.execute(sql, (tip.read, tip_id,))
        self._connection.commit()

    def mark_as_favourite(self, tip_id, tip):
        sql = "UPDATE Tips SET favourite = ? WHERE id == ?"
        self._connection.execute(sql, (tip.favourite, tip_id))
        self._connection.commit()

    def remove_tip(self, tip_id):
        sql = "DELETE FROM Tips WHERE id = ?"
        self._connection.execute(sql, (tip_id,))
        self._connection.commit()

        sql = "DELETE FROM Tiptags WHERE tipid = ?"
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
            tags = self.get_tags(row["id"])
            tips.append((row["id"], Tip(row["name"],
            row["url"], tags, row["read"], row["favourite"])))
        return tips

    def clear(self):
        sql = "DELETE FROM Tips"
        self._connection.execute(sql)
        self._connection.commit()

        sql = "DELETE FROM Tags"
        self._connection.execute(sql)
        self._connection.commit()

        sql = "DELETE FROM Tiptags"
        self._connection.execute(sql)
        self._connection.commit()

tip_repository = TipRepository()
