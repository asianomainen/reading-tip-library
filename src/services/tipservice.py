
from repositories.tip_repository import tip_repository
from entities.tip import Tip
import difflib

class TipService:

    def __init__(self, tip_repo=tip_repository):
        self.tip_repository = tip_repo

    def create(self, name, url):
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        if len(url) == 0 or url[0:4] != "www." or url[4:].count(".") != 1:
            raise Exception("Invalid url")
        tip = Tip(name, url)
        self.tip_repository.create_tip(tip)

    def edit(self, id, name, url):
        tip = Tip(name, url)
        self.tip_repository.edit_tip(id, tip)

    def mark_as_read(self, read, id):
        old = self.get_tip(id)
        tip = Tip(old.name, old.url, read)
        self.tip_repository.mark_as_read(id, tip)

    def get_all(self):
        return self.tip_repository.find_all()

    def get_only_not_read(self):
        return self.tip_repository.find_only_not_read(True)

    def get_only_read(self):
        
        return self.tip_repository.find_only_not_read(False)
        
    def get_close_matches(self, search):
        tips = tip_repository.find_all()
        matches = difflib.get_close_matches(search, map(lambda x: x[1].name, tips))
        return filter(lambda x: x[1].name in matches, tips)

    def get_tip(self, id):
        tip = self.tip_repository.find_tip(id)
        if tip == None:
            raise Exception("Invalid ID")
        return tip

    def remove_tip(self, id):
        self.get_tip(id)
        self.tip_repository.remove_tip(id)
        
    def clear(self):
        self.tip_repository.clear()


tip_service = TipService()