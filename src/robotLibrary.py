from stub_io import StubIo
from textui.menu import Menu
from services.tipservice import tip_service

class robotLibrary:
    def __init__(self):
        self.added_items = []
        self.io = StubIo()
        self.menu = Menu(self.io, tip_service)
    
    def number_of_items(self, n):
        if len(self.added_items) != int(n):
            raise AssertionError("Dont match")
        return len(self.added_items)

    def input(self, value):
        self._io.add_input(value)

    
        
