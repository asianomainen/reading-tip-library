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
        for output in self._io.outputs:
            print(output)
        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def output_should_not_contain(self, value):
        outputs = self._io.outputs
        for output in self._io.outputs:
            print(output)
        if value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def database_should_contain_tips(self, value):
        number_of_tips = len(self._tip_service.get_all())
        if number_of_tips != int(value):
            raise AssertionError(
                f"Number of tips {str(number_of_tips)} is not {str(value)}"
            )
        return number_of_tips

    def input(self, value):
        self._io.add_input(value)

    def run_application(self):
        self._menu.run()
