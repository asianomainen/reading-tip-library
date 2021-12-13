class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'

class Color_message:
    def red(text):
        return f"{Colors.RED}{text}{Colors.END}"

    def cyan(text):
        return f"{Colors.CYAN}{text}{Colors.END}"

    def green(text):
        return f"{Colors.GREEN}{text}{Colors.END}"

    def yellow(text):
        return f"{Colors.YELLOW}{text}{Colors.END}"
        