import commands

commands = commands.Commands()
dict_com = commands.dict_commands

def text_menu():
    for k, v in dict_com.items():
        print(f"{k} - {v[0]}")


def input_command(comm):
    dict_com[comm][1]()
