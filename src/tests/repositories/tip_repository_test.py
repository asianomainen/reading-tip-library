import unittest
from repositories.tip_repository import tip_repository
from entities.tip import Tip
from initialize_database import initialize_database 

class TestTipRepository(unittest.TestCase):

    def setUp(self):
        initialize_database()
        tip_repository.clear()

    def test_create(self):
        tip = Tip("book", "urli")
        tip_repository.create_tip(tip)
        tips = tip_repository.find_all()

        self.assertEqual(len(tips), 1)
    
    def test_clear(self):
        tip = Tip("book", "urli")
        tip_repository.create_tip(tip)
        tip_repository.clear()
        tips = tip_repository.find_all()
        self.assertEqual(len(tips), 0)