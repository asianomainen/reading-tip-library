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

    
    def test_display_help(self):
        initialize_database()
        io = StubIO(["h", "x"])
        menu = Menu(io, tip_service)
        menu.run()
        print(io.outputs)
        self.assertEqual(("1 Add tip, tip can be added if name is not empty and url is valid" in io.outputs), True)
        
