import datetime
import os
from constants import *
class MSMSError(Exception):
    """description of class"""
    def __init__(self, code, what=""):
        if code == 1000:
            self.what = what
        else:
            del what
        self.code = code
        codelist = []
        for i in str(code):
            codelist = codelist.append(i)
        if codelist[0] == "1":
            f = open(os.path.dirname(__file__).replace("/", "\\") + "\\crash.log", "w", encoding="utf-8")
            t = "# MSMS Crash Log.\n" + datetime.datetime.strftime("%Y %m %d %X") + "\nException:" + self.what
            f.write(t)
            f.close()
            exit()
        else:
            print("ERROR CODE: " + str(code) + "\nFor more information, please go to https://github.com/iamliuzhiyu/Minecraft-Server-Manage-System/wiki/Error")
def about():
    print("Minecraft Server Manage System. Version " + VERSION)
    print(COPYRIGHT)
    print("\n")
def parsting_command(command:str, commandlist:list):
    command_head = str(command.split(" ")[0])
    if not command_head in commandlist:
        raise MSMSError(2001)
    else:
        eval(COMMANDS_TO_FUNCTIONS[command_head])
print("Welcome to use Minecraft Server Manage System.")
print('Type "help" for more information.')
repeat = True
while repeat == True:
    command = input(">")
    parsting_command(command, COMMANDS_TO_FUNCTIONS)
