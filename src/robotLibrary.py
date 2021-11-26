from repositories.tip_repository import TipRepository

class robotLibrary:
    def __init__(self):
        self.added_items = []
    
    def number_of_items(self, n):
        if len(self.added_items) != int(n):
            raise AssertionError("Dont match")
        return len(self.added_items)
