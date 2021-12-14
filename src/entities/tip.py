
class Tip:
    def __init__(self, name, url, tags=[], read=0, favourite=0): # pylint: disable=dangerous-default-value, too-many-arguments
        self.name = name
        self.url = url
        self.read = read
        self.favourite = favourite
        self.tags = tags
