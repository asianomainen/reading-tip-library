
COMMANDS = {
    "x": "x quit",
    "1": "1 add tip",
    "2": "2 list tips"
}

class Menu:
    def __init__(self, io, tip_service):
        self.io = io
        self.tip_service = tip_service

    def print_commands(self):
        for command in COMMANDS:
            self.io.write(command)

    def run(self):
        self.io.write("Welcome dear reader")
        self.print_commands()

        while True:
            command = self.io.read("Command: ")
            if not command in COMMANDS:
                self.io.write("Invalsid command")
            if command == "x":
                break
            if command == "1":
                name = self.io.read("name: ")
                url = self.io.read("url: ")
                self.tip_service.create(name, url)

            if command == "2":
                tips = self.tip_service.get_all()
                for tip in tips:
                    self.io.write(f"{tip.name}, {tip.url}")