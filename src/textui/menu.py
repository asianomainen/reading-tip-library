
COMMANDS = {
    "1": "1 Add tip",
    "2": "2 List tips",
    "3": "3 Modify tip",
    "4": "4 Remove tip",
    "5": "5 Search tip",
    "6": "6 Mark tip as read",
    "7": "7 Cycle filter",
    "h": "h Help",
    "x": "x Quit"
}

HELP= {
    "1": "1 Add tip, tip can be added if name is not empty and url is valid",
    "2": "2 List tips, lists all tips",
    "3": "3 Modify tip, modify name/ url or both based on id",
    "4": "4 Remove tip, removes tip based on id",
    "5": "5 Search tip, search for a certain tip in database",
    "6": "6 Mark tip as read, option to mark a tip with 'read'",
    "7": "7 Cycle filter, modify filter determining what tips are displayed",
    "h": "h Help",
    "x": "x Quit, exit reading-tip library"
}

FILTERS = {
    "ALL": "all",
    "READ": "read",
    "NOT READ": "not read"
}

class Menu:
    def __init__(self, io, tip_service):
        self.io = io
        self.tip_service = tip_service
        self.filter = "ALL"

    def print_commands(self):
        self.io.write("")
        for command in COMMANDS:
            self.io.write(COMMANDS[command])
    
    def print_help(self):
        for help in HELP:
            self.io.write(HELP[help])


    def run(self):
        self.io.write("Welcome dear reader")
        self.print_commands()

        while True:
            self.io.write(f"\nYou are seeing {self.filter} tips")
            command = self.io.read("Command: ")
            if not command in COMMANDS:
                self.io.write("Invalid command")
                self.print_commands()

            if command == "1":
                name = self.io.read("name: ")
                url = self.io.read("url: ")
                if len(url) == 0 or url[0:4] != "www." or url[4:].count(".") != 1:
                    self.io.write("Invalid url")
                    url = self.io.read("url: ")
                try:
                    self.tip_service.create(name, url)
                except Exception as e:
                    self.io.write(e)

            if command == "2":
                tips = self.tip_service.get_all(FILTERS[self.filter])
                for tip in tips:
                    id = tip[0]
                    name = tip[1].name
                    url = tip[1].url
                    self.io.write(f"id:{id} {name}, {url}")

            if command == "3":
                id = self.io.read("Tip id to edit: ")
                print(self.tip_service.get_tip(id).name)
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

            if command == "5":
                i = self.io.read("search: ")
                for tip in self.tip_service.get_close_matches(i, FILTERS[self.filter]):
                    id = tip[0]
                    name = tip[1].name
                    url = tip[1].url
                    self.io.write(f"id:{id} {name}, {url}")

            if command == "6":
                id = self.io.read("tip id to mark: ")
                try:
                    old = self.tip_service.get_tip(id)
                    if old.read == 0:
                        read = 1
                    else:
                        read = 0
                    self.tip_service.mark_as_read(read, id)
                except Exception as e:
                    self.io.write(e)

            if command == "7":
                if self.filter == "ALL":
                    self.filter = "NOT READ"
                elif self.filter == "NOT READ":
                    self.filter = "READ"
                elif self.filter == "READ":
                    self.filter = "ALL"
            
            if command == "h":
                self.print_help()

            if command == "x":
                break

            self.io.write("")
            self.print_commands()
