from textui.consoleio import ConsoleIO
from textui.menu import Menu
from services.tipservice import tip_service
from textui.color_message import Color_message

def main():
    io = ConsoleIO
    color_message = Color_message
    menu = Menu(io, tip_service, color_message)
    menu.run()

if __name__ == "__main__":
    main()
