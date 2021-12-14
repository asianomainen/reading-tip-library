from os import name
import unittest
from repositories.tip_repository import tip_repository
from entities.tip import Tip
from initialize_database import initialize_database 

class TestTipRepository(unittest.TestCase):

    def setUp(self):
        initialize_database()
        tip_repository.clear()

    def test_create(self):
        tip = Tip("book", "www.test.test")
        tip_repository.create_tip(tip)
        tips = tip_repository.find_all()

        self.assertEqual(len(tips), 1)
    
    def test_clear(self):
        tip = Tip("book", "www.test.test")
        tip_repository.create_tip(tip)
        tip_repository.clear()
        tips = tip_repository.find_all()
        self.assertEqual(len(tips), 0)

    def test_remove(self):
        tip = Tip("book", "www.test.test")
        tip_repository.create_tip(tip)
        tip_repository.remove_tip(1)
        tips = tip_repository.find_all()
        self.assertEqual(len(tips), 0)

    def test_mark_as_read(self):
        tip = Tip("how to test", "www.test.test")
        tip_repository.create_tip(tip)
        tip.read = 1
        tip_repository.mark_as_read(1,tip)
        found_tip = tip_repository.find_tip(1)
        self.assertEqual(found_tip[1].read, 1)

    def test_find_only_not_read(self):
        tip = Tip("how to test", "www.test.test")
        tip_repository.create_tip(tip)
        tip.read = 1
        tip_repository.mark_as_read(1,tip)
        tips = tip_repository.find_all ("not read")
        self.assertEqual(len(tips), 0)

    def test_find_only_read(self):
        tip = Tip("how to test", "www.test.test")
        tip_repository.create_tip(tip)
        tip.read = 1
        tip_repository.mark_as_read(1,tip)
        tips = tip_repository.find_all("read")
        self.assertEqual(len(tips), 1)

    def test_edit(self):
        tip = Tip("how to test", "www.test.test")
        tip_repository.create_tip(tip)
        edited_tip = Tip("how not to test", "www.test.test")
        tip_repository.edit_tip(1, edited_tip)
        found_tip = tip_repository.find_tip(1)
        self.assertEqual(found_tip[1].name, "how not to test")

    def test_find(self):
        tip = Tip("book", "www.test.test")
        tip_repository.create_tip(tip)
        found = tip_repository.find_tip(1)
        self.assertEqual(found[1].name, tip.name)

    def test_find_with_invalid_id(self):
        tip = Tip("book", "www.test.test")
        tip_repository.create_tip(tip)
        found = tip_repository.find_tip(100)
        self.assertEqual(found, None)

    def test_find_all(self):
        tip1 = Tip("book", "www.test.test")
        tip_repository.create_tip(tip1)
        tip2 = Tip("podcast", "www.test.test")
        tip_repository.create_tip(tip2)

        tips = tip_repository.find_all()
        self.assertEqual(len(tips), 2)

    def test_mark_as_favourite(self):
        tip = Tip("testing", "www.test.tt")
        tip_repository.create_tip(tip)
        tip.favourite = 1
        tip_repository.mark_as_favourite(1, tip)
        found_tip = tip_repository.find_tip(1)
        self.assertEqual(found_tip[1].favourite, 1)

    def test_create_tip_with_tags(self):
        tip = Tip("book", "www.test.test", ["tag1", "tag2"])
        tip_repository.create_tip(tip)
        found_tip = tip_repository.find_tip(1)
        self.assertEqual(len(found_tip[1].tags), 2)

    def test_create_and_find_tag(self):
        tip_repository.create_tag("tagi")
        self.assertEqual(tip_repository.tag_exists("tagi"), True)

    def test_create_tip_with_existing_tag(self):
        tip_repository.create_tag("tagi")
        tip = Tip("book", "www.test.test", ["tagi", "tag2"])
        tip_repository.create_tip(tip)
        found_tip = tip_repository.find_tip(1)
        self.assertEqual(len(found_tip[1].tags), 2)