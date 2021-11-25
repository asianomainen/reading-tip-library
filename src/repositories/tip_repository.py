

class TipRepository:
    def __init__(self):
        self.tips =[]

    def create_tip(self, tip):
        self.tips.append(tip)

    def find_all(self):
        return self.tips

    def clear(self):
        self.tips = []

tip_repository = TipRepository()