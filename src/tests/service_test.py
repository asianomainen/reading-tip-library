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
        name = tip.name
        url = tip.url
        if name == "":
            name = self.tips[id-1][1].name
        if url == "":
            url = self.tips[id-1][1].url
        tip = Tip(name, url) 
        self.tips[id-1] = (id, tip)

    def remove_tip(self, id):
        print(id)
        try:
            self.tips.pop(id-1)
        except:
            print("pieleen")
            return

    def find_tip(self, id):
            tip = self.tips[id-1][1]
            tipdata = {"name": tip.name, "url": tip.url}
            return tipdata
        
class TestTipService(unittest.TestCase):

    def setUp(self):
        self.tipservice = TipService(FakeTipRepository())
        self.tipservice.clear()
        
    def test_remove_tip_valid_id(self):
        self.tipservice.create("how to test", "www.test.test")
        self.tipservice.remove_tip(1)
        tips = self.tipservice.get_all()
        self.assertEqual(len(list(tips)), 0)

    def test_remove_tip_invalid_id(self):
        self.tipservice.create("how to test", "www.test.test")
        with self.assertRaises(Exception):
            self.tipservice.remove_tip(5)
        tips = self.tipservice.get_all()
        self.assertEqual(len(list(tips)), 1)

    def test_remove_tip_invalid_input(self):
        self.tipservice.create("how to test", "www.test.test")
        with self.assertRaises(Exception):
            self.tipservice.remove_tip("a")
        tips = self.tipservice.get_all()
        self.assertEqual(len(list(tips)), 1)

    def test_create_and_find_tip(self):
        self.tipservice.create("how to test", "www.test.test")
        tips = self.tipservice.get_all()
        self.assertEqual(tips[0][1].url, "www.test.test")
    
    def test_create_no_name(self):
        with self.assertRaises(Exception):
            self.tipservice.create("", "www.test.test")

    def test_edit_new_name_and_url(self):
        self.tipservice.create("how to test", "www.test.test")
        self.tipservice.edit(1, "edited", "edited")
        tips = self.tipservice.get_all()
        self.assertEqual(tips[0][1].name, "edited")
        self.assertEqual(tips[0][1].url, "edited")
        
    def test_edit_new_name_and_old_url(self):
        self.tipservice.create("how to test", "www.test.test")
        self.tipservice.edit(1, "", "edited")
        tips = self.tipservice.get_all()
        self.assertEqual(tips[0][1].name, "how to test")
        self.assertEqual(tips[0][1].url, "edited")
        