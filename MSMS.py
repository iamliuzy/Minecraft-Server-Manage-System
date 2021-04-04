import datetime
import json
import os
from sys import exit

from constants import *
class MSMS(object):
    class Configuation(object):
        def __init__(self, id:str, displayname:str, ver:str):
            self.id = id
            self.displayname = displayname
            self.version = ver
            self.info = {"id": id, "disname": displayname, "version": ver}
            f = open(os.path.dirname(__file__).replace("/", "\\") + "\\configuations.json", "w", encoding="utf-8")
            f.write(json.dumps(self.info))
            f.close()
        def edit(self, key:str, value:str):
            self.info[key] = value
            if key == "id":
                self.id = value
            if key == "displayname" or key == "disname":
                self.displayname = value
            if key == "ver" or key == "version":
                self.version = value

    def about(self):
        print("Minecraft Server Manage System. Version " + VERSION)
        print(COPYRIGHT)

    def parsting_command(self, command: str, commandlist: list):
        command_head = str(command.split(" ")[0])
        if command_head not in commandlist:
            print("Unkdown command:" + command)
        else:
            eval(COMMANDS_TO_FUNCTIONS[command_head])

    def __init__(self):
        try:
            print("Welcome to use Minecraft Server Manage System.")
            print('Type "help" for more information.')
            repeat = True
            while repeat == True:
                command = input(">")
                self.parsting_command(command, COMMANDS_TO_FUNCTIONS)
        except KeyboardInterrupt:
            exit()

MSMS()