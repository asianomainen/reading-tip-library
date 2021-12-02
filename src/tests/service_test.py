import unittest
from services.tipservice import TipService
from entities.tip import Tip

class FakeTipRepository:
    def __init__(self, tips = []):
        self.id = 1
        self.tips = tips

    def find_all(self):
        return self.tips

    def create_tip(self, tip):
        self.tips.append((self.id, tip))
        self.id += 1

    def clear(self):
        self.tips = []

    def edit_tip(self, id , tip):
        self.tips[id-1] = tip


class TestTipService(unittest.TestCase):

    def setUp(self):
        self.tipservice = TipService(FakeTipRepository())
        self.tipservice.clear()
        

    def test_create_and_find_tip(self):
        self.tipservice.create("how to test", "urli")
        tips = self.tipservice.get_all()
        self.assertEqual(tips[0][1].url, "urli")
    
    def test_create_no_name(self):
        with self.assertRaises(Exception):
            self.tipservice.create("", "urli")
    
    
        
