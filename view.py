from control import *

class View:
    def __init__(self):
        self.dict_commands = get_commands()

    def run(self):
        print("Список команд:")
        for k, v in self.dict_commands.items():
            print(f"{k} - {v}")
        input_command(int(input("Введите номер команды:")))

