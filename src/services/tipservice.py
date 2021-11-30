from repositories.tip_repository import tip_repository
from entities.tip import Tip

class TipService:

    def __init__(self):
        self.tip_repository = tip_repository

    def create(self, name, url):
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        tip = Tip(name, url)
        tip_repository.create_tip(tip)

    def edit(self, id, name, url):
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        tip = Tip(name, url)
        tip_repository.edit_tip(id, tip)

    def get_all(self):
        return tip_repository.find_all()
    
    def get_tip(self, id):
        tipdata = tip_repository.find_tip(id)
        if tipdata == None:
            raise Exception("Invalid ID")
        return Tip(tipdata["name"],tipdata["url"])

tip_service = TipService()