import unittest
from textui.menu import Menu
from services.tipservice import tip_service
from stub_io import StubIO
from initialize_database import initialize_database
from textui.color_message import Color_message

class TestTextUi(unittest.TestCase):

    def setUp(self):
        initialize_database()
        tip_service.clear()

    
    def test_display_help(self):
        initialize_database()
        io = StubIO(["h", "x"])
        color_message = Color_message
        menu = Menu(io, tip_service, color_message)
        menu.run()
        self.assertEqual(("1 Add tip, tip can be added if name is not empty and url is valid" in io.outputs), True)
        
