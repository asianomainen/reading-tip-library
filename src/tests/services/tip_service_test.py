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

    def clear(self):
        self.tips = []

class TestTipService(unittest.TestCase):

    def setUp(self):
        self.tipservice = TipService(FakeTipRepository())

    def test_create_and_find_tip(self):
        self.tipservice.create("how to test", "urli")
        tips = self.tipservice.get_all()
        self.assertEqual(tips[0].url, "urli")