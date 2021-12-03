from repositories.tip_repository import tip_repository
from entities.tip import Tip

class TipService:

    def __init__(self, tip_repo=tip_repository):
        self.tip_repository = tip_repo

    def create(self, name, url):
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        tip = Tip(name, url)
        self.tip_repository.create_tip(tip)

    def edit(self, id, name, url):
        tip = Tip(name, url)
        self.tip_repository.edit_tip(id, tip)

    def get_all(self):
        return self.tip_repository.find_all()
    
    def get_tip(self, id):
        tipdata = self.tip_repository.find_tip(id)
        if tipdata == None:
            raise Exception("Invalid ID")
        return Tip(tipdata["name"],tipdata["url"])

    def clear(self):
        self.tip_repository.clear()

tip_service = TipService()