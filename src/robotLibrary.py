from stub_io import StubIO
from textui.menu import Menu
from services.tipservice import tip_service

class robotLibrary:
    def __init__(self):
        self._tip_service = tip_service
        self._io = StubIO()
        self._menu = Menu(self._io, self._tip_service)
    
    def number_of_items(self, n):
        if len(self._tip_service.get_all()) != int(n):
            raise AssertionError("Dont match")
        return len(self._tip_service.get_all())

    def input(self, value):
        self._io.add_input(value)

    def run_application(self):
        self._menu.run()
    
        
