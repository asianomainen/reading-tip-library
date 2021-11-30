import unittest
from services.tipservice import TipService
from entities.tip import Tip

class FakeTipRepository:
    def __init__(self, tips = []):
        self.tips = tips

    def get_all(self):
        return self.tips

    def create(self, name, url):
        tip = Tip(name, url)
        self.tips.append(tip)

    def clear(self):
        self.tips = []

class TestTipService(unittest.TestCase):

    def setUp(self):
        self.tipservice = TipService(FakeTipRepository())
        self.tipservice.clear()
        

    def test_create_and_find_tip(self):
        self.tipservice.create("how to test", "urli")
        tips = self.tipservice.get_all()
        self.assertEqual(tips[0][1].url, "urli")