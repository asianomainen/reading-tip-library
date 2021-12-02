from stub_io import StubIO
from textui.menu import Menu
from services.tipservice import tip_service
from initialize_database import initialize_database, reset_database

class robotLibrary:
    def __init__(self):
        initialize_database()
        reset_database()
        self._tip_service = tip_service
        self._io = StubIO()
        self._menu = Menu(self._io, self._tip_service)
    
    def output_should_contain(self, value):
        outputs = self._io.outputs
        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def input(self, value):
        self._io.add_input(value)

    def run_application(self):
        self._menu.run()
    
        
