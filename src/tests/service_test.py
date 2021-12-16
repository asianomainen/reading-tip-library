import unittest
from services.tipservice import TipService
from entities.tip import Tip

class FakeTipRepository:
    def __init__(self, tips = []):
        self.id = 1
        self.tips = tips

    def find_all(self, filter = "all"):
        if filter == "all":
            return self.tips
        if filter == "read":
            return self.find_only_not_read(False)
        return self.find_only_not_read(True)

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
        self.tips.remove(self.tips[id-1])
        

    def find_tip(self, id):
        return self.tips[id-1]

    def mark_as_read(self, id, tip):
        self.tips[id-1]= (id,tip)

    def find_only_not_read(self, only_not_read):
        tips = []
        if only_not_read == True:
            read = 0
        else: 
            read = 1
        for tip in self.tips:
            if tip[1].read == read:
                print(tip[1].read)
                tips.append(tip)
        return tips

    def mark_as_favourite(self, tip_id, tip):
        self.tips[tip_id-1] = (tip_id, tip)

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

    def test_create_no_url(self):
        with self.assertRaises(Exception):
            self.tipservice.create("how to test", "")

    def test_create_invalid_url_prefix(self):
        with self.assertRaises(Exception):
            self.tipservice.create("how to test", "qqq.test.test")

    def test_create_invalid_url_period_amount(self):
        with self.assertRaises(Exception):
            self.tipservice.create("how to test", "www.testtest")

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

    def test_search_matching_name(self):
        self.tipservice.create("how to test", "www.test.test")
        tips = self.tipservice.get_close_matches("how to test", "all")
        self.assertEqual(len(list(tips)), 1)  

    def test_search_almost_matching_name(self):
        self.tipservice.create("how to test", "www.test.test")
        tips = self.tipservice.get_close_matches("how to test1", "all")
        self.assertEqual(len(list(tips)), 1)

    def test_mark_tip_as_read_and_find(self):
        self.tipservice.create("how to test", "www.test.test")
        self.tipservice.create("how to test2", "www.test.test")
        self.tipservice.mark_as_read(1)
        tips = self.tipservice.get_all("read")
        self.assertEqual(len(list(tips)), 1)

    def test_mark_read_tip_as_unread(self):
        self.tipservice.create("how to test", "www.test.test")
        self.tipservice.mark_as_read(1)
        self.tipservice.mark_as_read(0)
        tips = self.tipservice.get_all("not read")
        self.assertEqual(len(list(tips)), 1)

    def test_mark_tip_as_favourite(self):
        self.tipservice.create("how to test", "www.test.test")
        self.tipservice.mark_as_favourite(1)
        found_tip = self.tipservice.get_tip(1)
        self.assertEqual(found_tip.favourite, 1)

    def test_remove_mark_tip_as_favourite(self):
        self.tipservice.create("how to test", "www.test.test")
        self.tipservice.mark_as_favourite(1)
        self.tipservice.mark_as_favourite(0)
        found_tip = self.tipservice.get_tip(1)
        self.assertEqual(found_tip.favourite, 0)
