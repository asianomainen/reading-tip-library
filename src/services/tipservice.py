import difflib
from repositories.tip_repository import tip_repository
from entities.tip import Tip

class TipService:

    def __init__(self, tip_repo=tip_repository):
        self.tip_repository = tip_repo

    def create(self, name, url, tags=[]): # pylint: disable=dangerous-default-value
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        if len(url) == 0 or url[0:4] != "www." or url[4:].count(".") != 1:
            raise Exception("Invalid url")
        tip = Tip(name, url, tags)
        self.tip_repository.create_tip(tip)

    def edit(self, tip_id, name, url):
        tip = Tip(name, url)
        self.tip_repository.edit_tip(tip_id, tip)

    def mark_as_read(self, tip_id):
        tip = self.get_tip(tip_id)
        if tip.read == 0:
            tip.read = 1
        else:
            tip.read = 0
        self.tip_repository.mark_as_read(tip_id, tip)

    def mark_as_favourite(self, tip_id):
        tip = self.get_tip(tip_id)
        if tip.favourite == 0:
            tip.favourite = 1
        else:
            tip.favourite = 0
        self.tip_repository.mark_as_favourite(tip_id, tip)

    def get_all(self, filters="all"):
        return self.tip_repository.find_all(filters)

    def get_close_matches(self, search, filters="all"):
        tips = self.tip_repository.find_all(filters)
        matches = difflib.get_close_matches(search, map(lambda x: x[1].name, tips))
        return filter(lambda x: x[1].name in matches, tips)

    def get_tip(self, tip_id):
        try:
            tip = self.tip_repository.find_tip(tip_id)[1]
        except Exception as e:
            raise Exception("Invalid ID") from e
        return tip

    def remove_tip(self, tip_id):
        self.get_tip(tip_id)
        self.tip_repository.remove_tip(tip_id)

    def clear(self):
        self.tip_repository.clear()


tip_service = TipService()
