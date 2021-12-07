import unittest
from textui.menu import Menu
from services.tipservice import tip_service
from stub_io import StubIO
from initialize_database import initialize_database

class TestTextUi(unittest.TestCase):

    def setUp(self):
        initialize_database()
        tip_service.clear()

    def test_tip_can_be_created_and_read(self):
        initialize_database()
        io = StubIO(["1", "how to test", "www.test.test", "2", "x"])
        menu = Menu(io, tip_service)
        menu.run()
        self.assertEqual(("id:1 how to test, www.test.test" in io.outputs), True)

