
COMMANDS = {
    "1": "1 Add tip",
    "2": "2 List tips",
    "3": "3 Modify tip",
    "4": "4 Remove tip",
    "x": "x quit"
}

class Menu:
    def __init__(self, io, tip_service):
        self.io = io
        self.tip_service = tip_service

    def print_commands(self):
        for command in COMMANDS:
            self.io.write(COMMANDS[command])

    def run(self):
        self.io.write("Welcome dear reader")
        self.print_commands()

        while True:
            command = self.io.read("Command: ")
            if not command in COMMANDS:
                self.io.write("Invalid command")
                self.print_commands()
            if command == "1":
                name = self.io.read("name: ")
                url = self.io.read("url: ")
                try:
                    self.tip_service.create(name, url)
                except Exception as e:
                    self.io.write(e)

            if command == "2":
                tips = self.tip_service.get_all()
                for tip in tips:
                    id = tip[0]
                    name = tip[1].name
                    url = tip[1].url
                    self.io.write(f"id:{id} {name}, {url}")

            if command == "3":
                id = self.io.read("Tip id to edit: ")
                try:
                    old = self.tip_service.get_tip(id)
                    name = self.io.read("New name (leave blank to keep old): ")
                    if len(name) == 0:
                        name = old.name
                    url = self.io.read("New url (leave blank to keep old): ")
                    if len(url) == 0:
                        url = old.url
                    self.tip_service.edit(id, name, url)
                except Exception as e:
                    self.io.write(e)

            if command == "4":
                id = self.io.read("Tip id to remove: ")
                try:
                    remove_status = self.tip_service.remove_tip(id)
                    self.io.write("Tip removed")
                except Exception as e:
                    self.io.write(e)
                

            if command == "x":
                break
                

