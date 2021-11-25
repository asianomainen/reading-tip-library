from textui.consoleio import ConsoleIO
from textui.menu import Menu
from services.tipservice import tip_service

def main():
    io = ConsoleIO
    menu = Menu(io, tip_service)
    menu.run()

if __name__ == "__main__":
    main()