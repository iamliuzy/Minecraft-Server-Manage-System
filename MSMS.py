import datetime
import os

from constants import *


class MSMSError(object):
    """The base error class of MSMS."""
    def __init__(self, code, what=""):
        """If the code is in list CRITICAL_ERROR_CODES, it will crash, else it will show a warning."""
        if not code in SUPPORT_ERROR_CODES:
            MSMSError(1000, "Undefiled error code " + str(code) + ".")
        self.code = code
        if self.code in CRITICAL_ERROR_CODES:
            CRITICAL = True
        else:
            CRITICAL = False
        if CRITICAL:
            f = open(os.path.dirname(__file__).replace("/", "\\") + "\\crash.log", "w", encoding="utf-8")
            t = "MSMS Crash Log.\n" + datetime.datetime.strftime("%Y %m %d %X") + "\nException:" + what
            f.write(t)
            f.close()
            exit()
        else:
            print("ERROR CODE: " + str(code) + "\nFor more information, please go to https://github.com/iamliuzhiyu/Minecraft-Server-Manage-System/wiki/Error-Code-" + str(code))
            return
def about():
    print("Minecraft Server Manage System. Version " + VERSION)
    print(COPYRIGHT)
def parsting_command(command:str, commandlist:list):
    command_head = str(command.split(" ")[0])
    if not command_head in commandlist:
        MSMSError(2001)
    else:
        eval(COMMANDS_TO_FUNCTIONS[command_head])
try:
    print("Welcome to use Minecraft Server Manage System.")
    print('Type "help" for more information.')
    repeat = True
    while repeat == True:
        command = input(">")
        parsting_command(command, COMMANDS_TO_FUNCTIONS)
except Exception:
    MSMSError(1000, Exception.__name__)
