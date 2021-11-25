import unittest
from repositories.tip_repository import tip_repository
from entities.tip import Tip

class TestTipRepository(unittest.TestCase):

    def setUp(self):
        tip_repository.clear()

    def test_create(self):
        tip = Tip("book", "urli")
        tip_repository.create_tip(tip)
        tips = tip_repository.find_all()

        self.assertEqual(len(tips), 1)