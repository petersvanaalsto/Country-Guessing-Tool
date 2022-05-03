from countries import *
from gui import *


class Game:
    def __init__(self):
        self.root = Tk()
        self.load_countries()

    def load_countries(self):
        North_America()
        South_America()
        Europe()
        Asia()
        Africa()
        Australia()
        Countries()
        GUI_Menu(self.root)


