from commands import Commands

classCom = Commands()
def get_commands():
    return classCom.get_dict_commands
def input_command(com):
    return classCom.input_com(com)