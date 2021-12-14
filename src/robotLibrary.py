from stub_io import StubIO
from textui.color_message import Color_message
from textui.menu import Menu, HELP, COMMANDS
from services.tipservice import tip_service
from initialize_database import initialize_database, reset_database

class robotLibrary:
    def __init__(self):
        initialize_database()
        reset_database()
        self._tip_service = tip_service
        self._io = StubIO()
        self.color_message = Color_message
        self._menu = Menu(self._io, self._tip_service, self.color_message)

    def output_should_contain(self, value):
        outputs = self._io.outputs
        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def output_should_contain_colored(self, color, text):
        message = ""
        if color == "cyan":
            message = self.color_message.cyan(text)
        if color == "red":
            message = self.color_message.red(text)
        if color == "green":
            message = self.color_message.green(text)
        if color == "yellow":
            message = self.color_message.yellow(text)
        self.output_should_contain(message)

    def output_should_contain_favourited(self, text):
        star = self.color_message.yellow("*")
        message = f"{star}{text}"
        self.output_should_contain(message)

    def output_should_contain_help(self):
        help_messages = HELP.values()
        for help_info in help_messages:
            self.output_should_contain(help_info)

    def output_should_not_contain(self, value):
        outputs = self._io.outputs
        if value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def output_should_contain_commands(self):
        outputs = self._io.outputs
        commands = COMMANDS.values()
        for command in commands:
            command = self.color_message.cyan(command)
            if outputs.count(command) != 2:
                raise AssertionError(
                    "Commands are not printed after every command given"
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
