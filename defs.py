from errorclass import MSMSError
def parsting_command(command:str, commandlist:list):
    command_head = str(command.split(" ")[0])
    if not command_head in commandlist:
        raise MSMSError("Command error", "2001", "Unkdown command:" + command)

