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

    def get_all(self):
        return tip_repository.find_all()
    
tip_service = TipService()