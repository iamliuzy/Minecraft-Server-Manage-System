import datetime
import json
import os
import shelve
from sys import exit

# width = x
# height = y

VERSION = "Indev 0.0.3"
COMMANDS_TO_FUNCTIONS = {"about":  "self.about()", "exit":  "exit()", "quit":  "exit()"}
COPYRIGHT = "Copyright (c) 2021 Shanghai Kouao Infotec Co., Ltd.\nLicense: GPL v3.0\nLicense file: %s\\LICENSE.txt"

class MSMS(object):
    class Display(object):
        def print_rich_text(self, text:str, mode:str):
            return "\033[" + mode + "m" + text
        def _cls(self):
            if os.name == "nt":
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")
            else:
                print("Undefined system type.")
                exit()
        def update(self):
            self._cls()
            print(self.content)
        def _set_title(self, title:str = "MSMS") -> None:
            for i in range(self.width):
                self.content += "-"
            self.content += "|"
            for i in range((self.width // 2 - len(self.title) // 2) - 1):
                self.content += self.print_rich_text(" ", "7")
            self.content += title
            for i in range((self.width // 2 - len(self.title) // 2 - 1)):
                self.content += " "
            self.content += self.print_rich_text("|\n|", "0")
            for i in range(self.width - 2):
                self.content += "-"
            self.content += "|\n"
        def __init__(self, width, height, title:str="MSMS"):
            self.content = ""
            self.width = width
            self.height = height
            self.title = title
            try:
                int(width / 2)
                int(height / 2)
                int(len(title) / 2)
            except:
                raise
            self._set_title(title)
        def add_object(self, o, line:int, column:int):
            self._set_title()

    class Text(object):
        def __init__(self, SURF:object, o:str, line:int, column:int):
            self.SURF = SURF
            self.o = o
            self.pos = (line, column)


    def __init__(self):
        try:
            self.SCREEN = self.Display(os.get_terminal_size()[0], os.get_terminal_size()[1])
            self.SCREEN.update()
        except KeyboardInterrupt:
            exit()
MSMS()