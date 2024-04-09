from control import *

class View:
    def __init__(self):
        self.dict_commands = get_commands()

    def run(self):
        flag = True
        while flag:
            print("Список команд:")
            for k, v in self.dict_commands.items():
                print(f"{k} - {v[0]}")
            print(input_command(int(input("Введите номер команды:\n"))))

